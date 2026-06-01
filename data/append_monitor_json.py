#!/usr/bin/env python3
"""Append a new monitor entry to monitors.json then build."""

import json, sys, os

MONITORS_FILE = "/root/.joyclaw/workspace-er-ji-shi-chang-yan-jiu-yuan-vxu6-d552a7b0dc9d-81c90a43/site/data/monitors.json"
SITE_DIR = "/root/.joyclaw/workspace-er-ji-shi-chang-yan-jiu-yuan-vxu6-d552a7b0dc9d-81c90a43/site"

new_entry = json.loads(sys.argv[1])

# Read existing
with open(MONITORS_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# Check for duplicate ids
existing_ids = {e["id"] for e in data}
if new_entry["id"] in existing_ids:
    print(f"WARNING: duplicate id {new_entry['id']}, skipping")
    sys.exit(0)

# Prepend (newest first)
data.insert(0, new_entry)

# Write back
with open(MONITORS_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Appended {new_entry['id']} to monitors.json ({len(data)} entries total)")

# Build and push
ret = os.system(f"cd {SITE_DIR} && python3 build_site.py --push")
if ret != 0:
    print(f"⚠️  Build/push exited with code {ret}")
    sys.exit(ret)
print("✅ Site build and push complete")