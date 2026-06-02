#!/usr/bin/env python3
"""Add a new monitor entry to monitors.json and rebuild site."""
import json

MONITORS_PATH = "/root/.joyclaw/workspace-er-ji-shi-chang-yan-jiu-yuan-vxu6-d552a7b0dc9d-81c90a43/site/data/monitors.json"

html = open("/root/.joyclaw/workspace-er-ji-shi-chang-yan-jiu-yuan-vxu6-d552a7b0dc9d-81c90a43/site/scripts/report_html.txt", "r", encoding="utf-8").read()

new_entry = {
    'id': 'mon-20260602-1647',
    'date': '2026-06-02 16:47',
    'title': 'AI板块收盘复盘 · A股收盘 三大指数集体收涨 CPO暴涨 机器人爆发 白银震荡上行',
    'tags': [
        '收盘复盘',
        'A股收盘',
        'CPO暴涨',
        '算力',
        '机器人',
        '宇树IPO过会',
        'MLCC',
        '白银'
    ],
    'summary': 'A股收盘三大指数集体收涨，创业板指+2.66%领涨。CPO概念暴涨东山精密涨停，机器人板块宇树IPO过会持续催化。通信设备主力净流入155亿。COMEX白银76美元震荡走强。',
    'html': html
}

with open(MONITORS_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# Check for duplicate
ids = [d['id'] for d in data]
if new_entry['id'] in ids:
    print(f"Duplicate ID {new_entry['id']} found, skipping")
    sys.exit(1)

data.append(new_entry)
print(f"Added entry {new_entry['id']}, total entries: {len(data)}")

with open(MONITORS_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Done!")