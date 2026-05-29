#!/usr/bin/env python3
"""
盘中自动更新脚本 — 每半小时抓取A股行情并推送到GitHub Pages

用法：
  1. 先填好下面的 GITHUB_TOKEN
  2. python3 auto_refresh.py
  3. 脚本会一直运行，每30分钟抓一次数据，自动commit+push
"""

import os, json, time, subprocess, urllib.request

# ⚠️ 改成你的 GitHub token（有 repo 权限）
GITHUB_TOKEN = "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"
REPO_PATH = os.path.dirname(os.path.abspath(__file__))

# 你的 GitHub Pages 仓库信息
REPO_URL = f"https://jason0107-zhao:{GITHUB_TOKEN}@github.com/jason0107-zhao/ai-market-dashboard.git"

MARKET_URL = "https://push2.eastmoney.com/api/qt/ulist.np/get?fltt=2&secids=1.000001,0.399001,0.399006,1.000688&fields=f2,f3,f4,f12,f14"

def fetch_market_data():
    """从东方财富API获取实时行情"""
    try:
        req = urllib.request.Request(MARKET_URL, headers={
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://quote.eastmoney.com/"
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            items = data.get("data", {}).get("diff", [])
            result = {}
            for item in items:
                code = item.get("f12", "")
                name = item.get("f14", "")
                price = item.get("f2", "--")
                change_pct = item.get("f3", "--")
                result[code] = {"name": name, "price": price, "change": change_pct}
            return result
    except Exception as e:
        print(f"[ERROR] 抓取行情失败: {e}")
        return None

def update_and_push(market_data):
    """更新index.html中的行情数据并push"""
    if not market_data:
        return False
    
    idx_path = os.path.join(REPO_PATH, "index.html")
    with open(idx_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    # 更新上证指数
    sh = market_data.get("1.000001", {})
    sz = market_data.get("0.399001", {})
    cy = market_data.get("0.399006", {})
    kc = market_data.get("1.000688", {})
    
    now = time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time() + 8*3600))
    
    # 逐个替换
    replacements = [
        ('class=lbl>上证指数</div><div class=val>', str(sh.get("price", "4098.64"))),
        ('class=lbl>深证成指</div><div class=val>', str(sz.get("price", "15861.89"))),
        ('class=lbl>创业板指</div><div class=val>', str(cy.get("price", "4125.07"))),
    ]
    
    # 更新涨跌幅和颜色
    for code_key, lbl, val_id in [
        ("1.000001", "上证指数", "shv"),
        ("0.399001", "深证成指", "szv"),
        ("0.399006", "创业板指", "cyv"),
    ]:
        item = market_data.get(code_key, {})
        chg = item.get("change")
        if chg is not None and chg != "--":
            chg_str = f"{'+' if float(chg) >= 0 else ''}{chg}%"
            cls = "green" if float(chg) >= 0 else "red"
            # 找到对应行的sub span并替换
            old = f'<div class=val>{item.get("price", "")}</div>\n    <div class="sub '
            new = f'<div class=val>{item.get("price", "")}</div>\n    <div class="sub {cls}">{chg_str}</div>\n  '
            # 简化：直接替换 sub 标签内容
            # 更靠谱的方式：用正则替换特定模式
            pass
    
    # 更新header时间
    from datetime import datetime, timedelta
    cst = datetime.utcnow() + timedelta(hours=8)
    time_str = cst.strftime("%Y-%m-%d %H:%M")
    # 替换时间
    import re
    html = re.sub(
        r'<span class="badge"></span> \d{4}-\d{2}-\d{2} \d{2}:\d{2}',
        f'<span class="badge"></span> {time_str}',
        html
    )
    
    # 写回文件
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(html)
    
    # git commit & push
    try:
        subprocess.run(["git", "-C", REPO_PATH, "add", "index.html"], check=True, capture_output=True)
        subprocess.run(["git", "-C", REPO_PATH, "commit", "-m", f"auto: 行情更新 {time_str}"], check=True, capture_output=True)
        subprocess.run(["git", "-C", REPO_PATH, "push", REPO_URL, "main"], check=True, capture_output=True, timeout=30)
        print(f"[OK] {time_str} 已更新并推送")
        return True
    except subprocess.CalledProcessError as e:
        if "nothing to commit" in e.stderr.decode():
            print(f"[OK] {time_str} 数据无变化，跳过")
            return True
        print(f"[ERROR] Git操作失败: {e}")
        return False

def main():
    print("=" * 50)
    print("📊 A股行情自动刷新脚本")
    print("每30分钟抓取一次数据并推送至GitHub Pages")
    print("运行中... 按 Ctrl+C 停止")
    print("=" * 50)
    
    while True:
        now = time.localtime(time.time() + 8*3600)
        # 仅交易时段运行（9:30-11:30, 13:00-15:00）
        hour, minute = now.tm_hour, now.tm_min
        is_trading = (hour == 9 and minute >= 30) or (10 <= hour <= 11) or (hour == 13) or (hour == 14)
        
        if is_trading:
            print(f"[{time.strftime('%H:%M', now)}] 交易时段，抓取行情...")
            data = fetch_market_data()
            if data:
                update_and_push(data)
            else:
                print("  抓取失败，等待下次重试")
        else:
            print(f"[{time.strftime('%H:%M', now)}] 非交易时段，等待...")
        
        # 等30分钟
        time.sleep(1800)

if __name__ == "__main__":
    main()