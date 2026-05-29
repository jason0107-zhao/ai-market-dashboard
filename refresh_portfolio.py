#!/usr/bin/env python3
"""
刷新持仓数据脚本 — 每日盘后抓取14只持仓实时行情并更新 portfolio.json

定时调度：
  每周一至周五，15:30 (收盘后) 和 20:00 (美股收盘后各运行一次)
  也可手动运行：python3 refresh_portfolio.py

持仓列表（14只）：
  阿里巴巴-W  09988.HK   港股
  纳斯达克ETF华夏 513300  A股ETF
  中信证券    600030.SH   A股
  蓝色光标    300058.SZ   A股
  上纬新材    688585.SH   A股
  黄金ETF易方达 159934.SZ ETF
  中韩半导体ETF华泰 513310.SH ETF
  科创半导体ETF华夏 588170.SH ETF
  湖南白银    002716.SZ   A股
  江西铜业    600362.SH   A股
  农业银行    601288.SH   A股
  招商银行    600036.SH   A股
  上海电力    600021.SH   A股
  人工智能ETF易方达 159819.SZ ETF
"""

import json, os, time, subprocess
from datetime import datetime, timedelta

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(REPO_DIR, "data")
PORTFOLIO_FILE = os.path.join(DATA_DIR, "portfolio.json")
INDEX_FILE = os.path.join(REPO_DIR, "index.html")

# GitHub token from env or .env
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
if not GITHUB_TOKEN:
    env_path = os.path.join(REPO_DIR, ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line.startswith("GITHUB_TOKEN="):
                    GITHUB_TOKEN = line.split("=", 1)[1].strip("\"'")
                    break
if GITHUB_TOKEN:
    REPO_URL = f"https://jason0107-zhao:{GITHUB_TOKEN}@github.com/jason0107-zhao/ai-market-dashboard.git"
else:
    REPO_URL = None

# 东方财富行情API
def fetch_eastmoney_prices(codes):
    """
    从东方财富批量获取实时行情
    codes: list of (market_code, name)
    """
    secids = []
    map_code = {}
    for c, n in codes:
        if c.endswith(".HK"):
            # 港股: hk prefix
            secid = f"116.{c.replace('.HK','').lstrip('0')}"
            secids.append(secid)
            map_code[secid] = {"name": n, "code": c}
        elif c.endswith(".SH"):
            secid = f"1.{c.replace('.SH','')}"
            secids.append(secid)
            map_code[secid] = {"name": n, "code": c}
        elif c.endswith(".SZ"):
            secid = f"0.{c.replace('.SZ','')}"
            secids.append(secid)
            map_code[secid] = {"name": n, "code": c}
        else:
            # ETF без суффикса или другое
            if c.startswith("159") or c.startswith("300") or c.startswith("301"):
                secid = f"0.{c}"
            else:
                secid = f"1.{c}"
            secids.append(secid)
            map_code[secid] = {"name": n, "code": c}
    
    url = f"https://push2.eastmoney.com/api/qt/ulist.np/get?fltt=2&secids={','.join(secids)}&fields=f2,f3,f4,f12,f14,f15,f16,f17,f18"
    try:
        import urllib.request
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://quote.eastmoney.com/"
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            items = data.get("data", {}).get("diff", [])
            result = {}
            for item in items:
                code = item.get("f12", "")
                price = item.get("f2", 0)
                change_pct = item.get("f3", 0)
                open_p = item.get("f15", 0)
                high = item.get("f16", 0)
                low = item.get("f17", 0)
                volume = item.get("f18", 0)
                result[code] = {
                    "price": price if price else 0,
                    "change": change_pct if change_pct else 0,
                    "open": open_p if open_p else 0,
                    "high": high if high else 0,
                    "low": low if low else 0,
                    "volume": volume if volume else 0
                }
            return result
    except Exception as e:
        print(f"[ERROR] fetch_eastmoney error: {e}")
        return {}

def get_rating(chg_pct, is_etf=False):
    """基于涨跌幅和趋势给出建议评级"""
    if is_etf:
        if chg_pct > 1.5: return "B"  # 增持
        if chg_pct < -3: return "S"   # 减持
        return "H"                    # 观望
    # 个股
    if chg_pct > 3: return "B"
    if chg_pct < -3: return "S"
    return "H"

def get_macd_signal(chg_pct):
    """简化的MACD信号"""
    if chg_pct > 0.5: return {"v": round(chg_pct * 0.3, 2), "s": "多头"}
    if chg_pct > 0: return {"v": round(chg_pct * 0.2, 2), "s": "多头收敛"}
    if chg_pct > -2: return {"v": round(chg_pct * 0.15, 2), "s": "空头收敛"}
    return {"v": round(chg_pct * 0.2, 2), "s": "空头"}

def generate_portfolio_data():
    """获取14只持仓的实时行情并生成完整数据"""
    codes = [
        ("09988.HK", "阿里巴巴-W"),
        ("513300", "纳斯达克ETF华夏"),
        ("600030.SH", "中信证券"),
        ("300058.SZ", "蓝色光标"),
        ("688585.SH", "上纬新材"),
        ("159934.SZ", "黄金ETF易方达"),
        ("513310.SH", "中韩半导体ETF华泰"),
        ("588170.SH", "科创半导体ETF华夏"),
        ("002716.SZ", "湖南白银"),
        ("600362.SH", "江西铜业"),
        ("601288.SH", "农业银行"),
        ("600036.SH", "招商银行"),
        ("600021.SH", "上海电力"),
        ("159819.SZ", "人工智能ETF易方达"),
    ]
    
    market_data = fetch_eastmoney_prices(codes)
    now = datetime.now() + timedelta(hours=8)  # CST
    time_str = now.strftime("%Y-%m-%d %H:%M") + " CST"
    
    stocks = []
    for c, n in codes:
        md = market_data.get(c, market_data.get(c.replace(".SH","").replace(".SZ",""), {}))
        price = md.get("price", 0)
        chg = md.get("change", 0)
        
        # Map exchange type
        if ".HK" in c:
            exch = "港股"
            ec = "pfl-exgH"
            currency = "HK$"
        elif c in ("513300","513310","588170","159934","159819"):
            exch = "ETF"
            ec = "pfl-exgE"
            currency = "¥"
        elif c in ("688585",):
            exch = "科创板"
            ec = "pfl-exgA"
            currency = "¥"
        else:
            exch = "A股"
            ec = "pfl-exgA"
            currency = "¥"
        
        is_etf = (exch == "ETF")
        rt = get_rating(chg, is_etf)
        macd = get_macd_signal(chg)
        
        # KDJ simplified
        k_val = 50 + chg * 5
        kd = f"K{max(10, min(90, round(k_val)))} D{max(10, min(90, round(k_val - 5)))}"
        
        rsi = 50 + chg * 3
        rsi = max(10, min(90, rsi))
        if rsi > 65: rs_text = "偏强"
        elif rsi > 55: rs_text = "中性偏强"
        elif rsi < 30: rs_text = "超卖"
        elif rsi < 40: rs_text = "偏弱"
        else: rs_text = "中性"
        
        # 模拟资金流向（粗略估算）
        if chg >= 0:
            flow = [round(chg * 0.5, 2), round(chg * 0.3, 2), round(chg * 0.15, 2), round(-chg * 0.3, 2)]
        else:
            flow = [round(chg * 0.3, 2), round(chg * 0.15, 2), round(chg * 0.1, 2), round(-chg * 0.2, 2)]
        
        stock = {
            "n": n,
            "c": c,
            "e": exch,
            "ec": ec,
            "cur": currency,
            "pr": round(price, 2) if price else 0,
            "ch": round(chg, 2),
            "rt": rt,
            "md": macd,
            "kd": kd,
            "r6": round(rsi, 1),
            "rs": rs_text,
            "mf": flow
        }
        stocks.append(stock)
    
    result = {
        "time": time_str,
        "stocks": stocks
    }
    return result

def save_and_push(data):
    """保存 portfolio.json 并推送"""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(PORTFOLIO_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[OK] portfolio.json saved ({len(data['stocks'])} stocks)")
    
    # git commit & push
    try:
        subprocess.run(["git", "-C", REPO_DIR, "add", "data/portfolio.json"],
                       check=True, capture_output=True, timeout=10)
        result = subprocess.run(
            ["git", "-C", REPO_DIR, "diff", "--cached", "--quiet"],
            capture_output=True, timeout=10
        )
        if result.returncode == 0:
            print("  NO_CHANGE — nothing to commit")
            return True
        
        subprocess.run(
            ["git", "-C", REPO_DIR, "commit", "-m", f"auto: portfolio refresh {data['time']}"],
            check=True, capture_output=True, timeout=10
        )
        push_url = REPO_URL if REPO_URL else "origin"
        subprocess.run(
            ["git", "-C", REPO_DIR, "push", push_url, "main"],
            check=True, capture_output=True, timeout=30
        )
        print(f"  PUSHED: portfolio data {data['time']}")
        return True
    except subprocess.CalledProcessError as e:
        stderr = e.stderr.decode() if e.stderr else ""
        if "nothing to commit" in stderr:
            print("  nothing to commit")
            return True
        print(f"  GIT_ERR: {stderr[:200]}")
        return False

def main():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 刷新持仓数据...")
    data = generate_portfolio_data()
    save_and_push(data)

if __name__ == "__main__":
    # 也支持schedule模式（后台定时运行）
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--schedule":
        print("=" * 50)
        print("📊 持仓数据定时刷新")
        print("  09:30 开盘 · 11:30 午间 · 15:05 收盘 · 17:00 晚盘")
        print("=" * 50)
        # 等待到下一个整点或半点的5分钟后执行
        while True:
            now = datetime.now()
            h, m = now.hour, now.minute
            
            # 只在交易相关时间执行
            target_times = [(9, 30), (11, 35), (15, 10), (17, 5), (20, 10)]
            for th, tm in target_times:
                if h == th and m == tm:
                    main()
                    break
            
            time.sleep(60)  # 每分钟检查一次
    else:
        main()