#!/usr/bin/env python3
"""盘中自动更新：每30分钟抓新浪行情 → 更新index.html → push GitHub Pages"""
import re, subprocess, os, sys
from urllib.request import Request, urlopen
from datetime import datetime, timedelta

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
TOKEN = "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"
REPO_URL = f"https://jason0107-zhao:{TOKEN}@github.com/jason0107-zhao/ai-market-dashboard.git"

# 新浪行情接口：sh=上海  sz=深圳 后缀0=指数
CODES = "sh000001,sz399001,sz399006,sh000688"
URL = f"http://hq.sinajs.cn/list={CODES}"

def fetch():
    req = Request(URL, headers={"Referer":"https://finance.sina.com.cn"})
    with urlopen(req, timeout=10) as r:
        raw = r.read().decode("gbk")
    results = {}
    for line in raw.strip().split("\n"):
        if not line.strip():
            continue
        # 解析格式: var hq_str_sh000001="上证指数,open,昨收,现价,最高,最低,...";
        m = re.match(r'var hq_str_\w+="([^"]+)"', line)
        if not m:
            continue
        fields = m.group(1).split(",")
        results[fields[0]] = {
            "price": fields[3],   # 当前价
            "open": fields[1],
            "yclose": fields[2],
            "high": fields[4],
            "low": fields[5],
        }
    return results

def update_and_push(data):
    path = os.path.join(REPO_DIR, "index.html")
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    now = (datetime.utcnow() + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M")

    # 更新header时间
    html = re.sub(
        r'<span class="badge"></span> \d{4}-\d{2}-\d{2} \d{2}:\d{2}',
        f'<span class="badge"></span> {now}',
        html
    )

    # 指数映射
    index_config = [
        ("上证指数", "4098.64", "0.12"),
        ("深证成指", "15861.89", "0.80"),
        ("创业板指", "4125.07", "1.96"),
        ("科创50", "1844.25", "1.59"),
    ]

    for name, default_price, default_chg in index_config:
        entry = data.get(name)
        if not entry:
            price, yclose = default_price, default_price
            chg_pct = float(default_chg)
        else:
            price = entry["price"]
            yclose = entry.get("yclose", price)
            try:
                p = float(price)
                yc = float(yclose)
                chg_pct = round((p - yc) / yc * 100, 2)
            except:
                chg_pct = 0.0

        cls = "green" if chg_pct >= 0 else "red"
        sign = "+" if chg_pct >= 0 else ""
        chg_str = f"{sign}{chg_pct:.2f}%"

        # 找到该指数card
        idx = html.find(f"class=lbl>{name}")
        if idx < 0:
            print(f"WARN: 未找到 {name}")
            continue

        card_end = html.find("</div>", idx + 50)
        card_section = html[idx:card_end] if card_end > 0 else html[idx:idx+300]

        # 替换价格
        price_old = re.search(r'<div class=val>[^<]+</div>', card_section)
        if price_old:
            html = html[:idx + price_old.start()] + f'<div class=val>{price}</div>' + html[idx + price_old.end():]
            # 重新定位
            idx = html.find(f"class=lbl>{name}")
            card_end = html.find("</div>", idx + 50)
            card_section = html[idx:card_end] if card_end > 0 else html[idx:idx+300]

        # 替换涨跌幅
        sub_old = re.search(r'<div class="sub [^"]*">[^<]+%</div>', card_section)
        if sub_old:
            local_idx = idx + sub_old.start()
            local_end = idx + sub_old.end()
            html = html[:local_idx] + f'<div class="sub {cls}">{chg_str}</div>' + html[local_end:]

    # Git push
    try:
        subprocess.run(["git", "-C", REPO_DIR, "add", "index.html"],
                       check=True, capture_output=True, timeout=10)
        result = subprocess.run(
            ["git", "-C", REPO_DIR, "diff", "--cached", "--quiet"],
            capture_output=True, timeout=10
        )
        if result.returncode == 0:
            print("NO_CHANGE")
            return

        ts = now.replace(" ", "_").replace(":", "-")
        subprocess.run(
            ["git", "-C", REPO_DIR, "commit", "-m", f"auto: 行情 {ts}"],
            check=True, capture_output=True, timeout=10
        )
        subprocess.run(
            ["git", "-C", REPO_DIR, "push", REPO_URL, "main"],
            check=True, capture_output=True, timeout=30
        )
        print(f"PUSHED {now}")
    except subprocess.CalledProcessError as e:
        stderr = e.stderr.decode() if e.stderr else ""
        print(f"GIT_ERR: {stderr[:200]}")

if __name__ == "__main__":
    try:
        data = fetch()
        print(f"Got data: {list(data.keys())}")
        update_and_push(data)
    except Exception as e:
        print(f"FAIL: {e}")
        sys.exit(1)