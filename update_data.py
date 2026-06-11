#!/usr/bin/env python3
import json
import os
import subprocess
import sys

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SITE_DIR, "data", "monitors.json")

# Read existing data
with open(DATA_FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Check for duplicate
new_id = "mon-20260611-1129"
data = [e for e in data if e['id'] != new_id]

new_entry = {
    "id": new_id,
    "date": "2026-06-11 11:29",
    "title": "AI板块实时监控 & COMEX白银播报 — 午前CPO反弹延续 半导体材料活跃 工信部政策持续发酵",
    "tags": ["AI板块", "白银", "实时监控", "CPO", "算力", "存储", "机器人", "工信部", "HBM"],
    "summary": "A股低开震荡超4000股下跌；CPO延续反弹炬光科技20cm涨停；半导体材料走强；白银64美元企稳",
    "html": (
        '<h1>AI板块实时监控报告 &amp; COMEX白银期货播报</h1>\n'
        '<p><strong>【2026-06-11 11:29】</strong></p>\n'
        '<p><strong>\u26a1 A\u80a1\u6b63\u5728\u4ea4\u6613\u4e2d\uff08\u5348\u524d\u76d8\uff09</strong> \u2014 \u4ee5\u4e0b\u4e3a\u5b9e\u65f6\u76d8\u4e2d\u76d1\u63a7</p>\n'
        '<hr />\n'
        '<h2>\u96f6\u3001COMEX\u767d\u94f6\u671f\u8d27\u64ad\u62a5</h2>\n'
        '<ul>\n'
        '  <li><strong>\u6700\u65b0\u4ef7\u683c\uff1a</strong>COMEX\u767d\u94f6\u671f\u8d27\u4e3b\u529b\u6700\u65b0\u62a5\u7ea6 <strong>64.24\u7f8e\u5143/\u76ce\u53f8</strong>\uff0c\u65e5\u5185\u6da8<strong>+1.2%</strong>\u3002\u73b0\u8d27\u767d\u94f6\u65e5\u5185\u6da8<strong>1%</strong>\u62a5<strong>64.03\u7f8e\u5143/\u76ce\u53f8</strong>\u3002</li>\n'
        '  <li><strong>\u65e5\u5185\u6da8\u8dcc\u5e45\uff1a</strong>\u6628\u65e5\uff086\u670810\u65e5\uff09COMEX\u767d\u94f6\u8d85\u0031%\u6536\u62a564.58\u7f8e\u5143\uff0c\u4eca\u65e5\u4e9a\u76d8\u5c0f\u5e45\u53cd\u5f39\u81f364\u7f8e\u5143\u4e0a\u65b9\u3002\u6caa\u94f6\u4e3b\u529b\u5f00\u76d8\u62a515,266\u5143/\u5343\u514b\u3002</li>\n'
        '  <li><strong>\u8fd1\u671f\u8d8b\u52bf\u5224\u65ad\uff1a</strong>\u767d\u94f6\u81ea5\u670813\u65e5\u8fd1<strong>90\u7f8e\u5143/\u76ce\u53f8</strong>\u5386\u53f2\u9ad8\u4f4d\u6301\u7eed\u56de\u8c03\u81f3\u4eca\uff0c\u7d2f\u8ba1\u8dcc\u5e45\u8d8528%\uff0c\u76ee\u524d\u5728<strong>63-67\u7f8e\u5143\u533a\u95f4\u9707\u8361\u6574\u7406</strong>\u3002<br />\n'
    )
}

data.append(new_entry)

with open(DATA_FILE, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Entry {new_id} added successfully.")
print(f"Total entries: {len(data)}")