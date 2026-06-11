#!/usr/bin/env python3
"""Add monitor entry to monitors.json"""
import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "monitors.json")

# Read
with open(DATA_FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Remove if exists
new_id = "mon-20260611-1129"
data = [e for e in data if e['id'] != new_id]

new_entry = {
    "id": new_id,
    "date": "2026-06-11 11:29",
    "title": "AI板块实时监控 & COMEX白银播报 — 午前CPO反弹延续 半导体材料活跃 工信部政策持续发酵",
    "tags": ["AI板块", "白银", "实时监控", "CPO", "算力", "存储", "机器人", "工信部", "HBM"],
    "summary": "A股低开震荡超4000股下跌；CPO延续反弹炬光科技20cm涨停；半导体材料走强；白银64美元企稳",
    "html": ""
}

# Read the HTML from file
html_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "report_html_final.txt")
with open(html_file, 'r', encoding='utf-8') as f:
    new_entry["html"] = f.read()

data.append(new_entry)

with open(DATA_FILE, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Entry {new_id} added. Total: {len(data)} entries")