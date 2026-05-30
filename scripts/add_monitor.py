#!/usr/bin/env python3
"""Append a monitor entry to monitors.json"""
import json, sys

entry = json.loads(sys.stdin.read())
path = "/root/.joyclaw/workspace-er-ji-shi-chang-yan-jiu-yuan-vxu6-d552a7b0dc9d-81c90a43/site/data/monitors.json"
with open(path, 'r') as f:
    data = json.load(f)
data.append(entry)
with open(path, 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("OK")