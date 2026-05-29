#!/usr/bin/env python3
"""
Build site: monitors data from site/data/monitors.json, reports from site/data/reports.json
Usage:
  python3 build_site.py          # just build index.html
  python3 build_site.py --push   # build + git commit + push to GitHub Pages
"""
import json, os, sys, subprocess, re
from datetime import datetime

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(REPO_DIR, "data")
INDEX   = os.path.join(REPO_DIR, "index.html")
TOKEN   = "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"
REPO_URL = f"https://jason0107-zhao:{TOKEN}@github.com/jason0107-zhao/ai-market-dashboard.git"

os.makedirs(DATA_DIR, exist_ok=True)

def load_json(name):
    path = os.path.join(DATA_DIR, name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def dump_monitors(monitors):
    path = os.path.join(DATA_DIR, "monitors.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(monitors, f, ensure_ascii=False, indent=2)

def dump_reports(reports):
    path = os.path.join(DATA_DIR, "reports.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(reports, f, ensure_ascii=False, indent=2)

def append_monitor(new_entry):
    """Append a single new monitor entry, dedup by id."""
    monitors = load_json("monitors.json")
    # Check for duplicate id
    existing_ids = {m["id"] for m in monitors}
    if new_entry["id"] in existing_ids:
        print(f"  ⏭  skip duplicate id={new_entry['id']}")
        return monitors
    monitors.append(new_entry)
    dump_monitors(monitors)
    print(f"  ✅ appended monitor {new_entry['id']}  (total {len(monitors)})")
    return monitors

def build():
    """Read JSON data, write into index.html, return True on success."""
    monitors = load_json("monitors.json")
    reports  = load_json("reports.json")

    if not os.path.exists(INDEX):
        print(f"ERROR: {INDEX} not found")
        return False

    with open(INDEX, "r", encoding="utf-8") as f:
        html = f.read()

    # Replace monitors array
    monitors_json = json.dumps(monitors, ensure_ascii=False)
    html = re.sub(
        r'const monitors = \[.*?\];',
        f'const monitors = {monitors_json};',
        html,
        flags=re.DOTALL
    )

    # Replace reports array
    reports_json = json.dumps(reports, ensure_ascii=False)
    html = re.sub(
        r'const reports = \[.*?\];',
        f'const reports = {reports_json};',
        html,
        flags=re.DOTALL
    )

    with open(INDEX, "w", encoding="utf-8") as f:
        f.write(html)

    # Also update filter buttons — find dates present in monitors
    dates_present = sorted(set(m["date"][:10] for m in monitors), reverse=True)

    print(f"  Monitors: {len(monitors)}, Reports: {len(reports)}, Dates: {dates_present[:5]}...")
    return True

def git_push(msg=None):
    """Git add, commit, push."""
    if msg is None:
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        msg = f"auto: site build {now}"

    try:
        subprocess.run(["git", "-C", REPO_DIR, "add", "-A"],
                       check=True, capture_output=True, timeout=10)

        result = subprocess.run(
            ["git", "-C", REPO_DIR, "diff", "--cached", "--quiet"],
            capture_output=True, timeout=10
        )
        if result.returncode == 0:
            print("  NO_CHANGE — nothing to commit")
            return True

        subprocess.run(
            ["git", "-C", REPO_DIR, "commit", "-m", msg],
            check=True, capture_output=True, timeout=10
        )
        subprocess.run(
            ["git", "-C", REPO_DIR, "push", REPO_URL, "main"],
            check=True, capture_output=True, timeout=30
        )
        print(f"  PUSHED: {msg}")
        return True
    except subprocess.CalledProcessError as e:
        stderr = e.stderr.decode() if e.stderr else ""
        print(f"  GIT_ERR: {stderr[:200]}")
        return False

# ─── CLI ────────────────────────────────────────
if __name__ == "__main__":
    do_push = "--push" in sys.argv

    if "append" in sys.argv:
        # Usage: python3 build_site.py append '<json_string>'
        # Where json_string = {"id":"mon-...","date":"...","title":"...","tags":[...],"summary":"...","html":"..."}
        try:
            entry = json.loads(sys.argv[sys.argv.index("append") + 1])
        except (IndexError, json.JSONDecodeError):
            print("ERROR: append needs a JSON string argument")
            sys.exit(1)
        append_monitor(entry)

    ok = build()

    if do_push:
        git_push()

    if not ok:
        sys.exit(1)