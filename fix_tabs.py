#!/usr/bin/env python3
"""Insert tab/filter/report functions into index.html"""
import re, subprocess
from pathlib import Path

HTML = Path('/root/.joyclaw/workspace-er-ji-shi-chang-yan-jiu-yuan-vxu6-d552a7b0dc9d-81c90a43/site/index.html')

html = HTML.read_text(encoding='utf-8')
m = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
js = m.group(1)

# Find last IIFE (the dashboard render function)
iife_start = js.rindex('(function() {')
iife_end = js.rindex('})()') + len('})()')
iife_code = js[iife_start:iife_end]

insert_code = r"""
// --- Tab & Filter Functions -----------------
let monFilter = 'all';

function showTab(name, evt) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('show'));
  document.getElementById('page-' + name).classList.add('show');
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  evt.target.classList.add('active');
}

function filterMon(f, evt) {
  monFilter = f;
  document.querySelectorAll('#monFilter button').forEach(b => b.classList.remove('active'));
  evt.target.classList.add('active');
  renderMonitors();
}

function renderMonitors() {
  const list = monitors.filter(m => {
    if (monFilter === 'all') return true;
    return m.date.startsWith(monFilter);
  });
  const el = document.getElementById('monList');
  if (!el) return;
  el.innerHTML = list.length === 0
    ? '<div style="text-align:center;padding:40px;color:#64748b">\u{1f4ed} \u6682\u65e0\u76d1\u63a7\u6570\u636e</div>'
    : list.map(m =>
      '<div class="article" onclick="openMonitor(\'' + m.id + '\')">' +
        '<div class="meta"><span class="t mon">\u{1f4e1} \u76d1\u6d4b\u62a5\u544a</span><span>' + m.date + '</span></div>' +
        '<h3>' + m.title + '</h3>' +
        '<p>' + m.summary + '</p>' +
        '<div class="tags">' + m.tags.map(t => '<span>' + t + '</span>').join('') + '</div>' +
      '</div>'
    ).join('');
}

function openMonitor(id) {
  const m = monitors.find(x => x.id === id);
  if (!m) return;
  document.getElementById('mTitle').textContent = m.title;
  document.getElementById('mBody').innerHTML = m.html;
  document.getElementById('modal').classList.add('show');
  document.getElementById('ov').classList.add('show');
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  document.getElementById('modal').classList.remove('show');
  document.getElementById('ov').classList.remove('show');
  document.body.style.overflow = '';
}

// --- Reports ---------------------------------
function renderReports() {
  const el = document.getElementById('rptList');
  if (!el) return;
  el.innerHTML = reports.length === 0
    ? '<div style="text-align:center;padding:40px;color:#64748b">\u{1f4ed} \u6682\u65e0\u4e13\u9898\u62a5\u544a</div>'
    : reports.map(r =>
      '<div class="article" onclick="openReport(\'' + r.id + '\')">' +
        '<div class="meta"><span class="t rpt">\u{1f4cb} \u4e13\u9898\u62a5\u544a</span></div>' +
        '<h3>' + r.title + '</h3>' +
        '<p>' + r.desc + '</p>' +
        '<div class="tags">' + r.tags.map(t => '<span>' + t + '</span>').join('') + '</div>' +
      '</div>'
    ).join('');
}

function openReport(id) {
  const r = reports.find(x => x.id === id);
  if (!r) return;
  document.getElementById('mTitle').textContent = r.title;
  document.getElementById('mBody').innerHTML = r.html;
  document.getElementById('modal').classList.add('show');
  document.getElementById('ov').classList.add('show');
  document.body.style.overflow = 'hidden';
}
"""

new_js = js[:iife_start] + insert_code + '\n' + iife_code
new_html = html[:m.start()] + '<script>' + new_js + '</script>' + html[m.end():]
HTML.write_text(new_html, encoding='utf-8')

print(f"Inserted {len(insert_code)} chars of tab/report functions")
print(f"New JS length: {len(new_js)}")

# Validate
result = subprocess.run(['node', '-e', '''
const fs = require("fs");
const html = fs.readFileSync("index.html", "utf8");
const m = html.match(/<script>([\\s\\S]*?)<\\/script>/);
const js = m[1];
try {
  global.document = {
    getElementById: function(){ return {textContent:"", className:"", innerHTML:"", style:{}}; },
    querySelectorAll: function(){ return {forEach:function(){}}; },
    body: {style:{overflow:""}}
  };
  eval(js);
  console.log("JS EXECUTED OK!");
} catch(e) {
  console.log("JS ERROR:", e.message.substring(0, 300));
}
'''], capture_output=True, text=True, timeout=10, cwd='/root/.joyclaw/workspace-er-ji-shi-chang-yan-jiu-yuan-vxu6-d552a7b0dc9d-81c90a43/site')
print(result.stdout)
if result.stderr:
    print('STDERR:', result.stderr[:200])