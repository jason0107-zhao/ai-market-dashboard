#!/usr/bin/env python3
"""Generate and push AI monitor report - 2026-06-05 03:21"""

import json, os, sys, subprocess

SITE_DIR = "/root/.joyclaw/workspace-er-ji-shi-chang-yan-jiu-yuan-vxu6-d552a7b0dc9d-81c90a43/site"
DATA_FILE = os.path.join(SITE_DIR, "data", "monitors.json")

report_date = "2026-06-05 03:21"
report_id = "mon-20260605-0321"
# Add before e4 creation
_ = report_id
report_title = "AI板块凌晨监控 & COMEX白银播报 — A股6/4收盘回顾与盘后展望"
report_summary = "A股6/4三大指数收跌芯片逆势走强；白银日内涨1.6%后亚盘回落；聚焦美股隔夜动态"
report_tags = ["AI板块", "白银", "盘后回顾", "CPO", "算力", "存储", "机器人"]

html_content = """
<h1>COMEX白银期货播报 &amp; AI板块盘后监控报告</h1>
<p><strong>报告时间：2026-06-05 03:21（北京时间，凌晨）</strong></p>

<h2>零、COMEX白银期货播报</h2>
<ul>
<li><strong>最新价格：</strong>COMEX白银期货周四（6月4日）纽约尾盘报 <strong>74.16美元/盎司</strong>，日内涨 <strong>+1.69%</strong>。现货白银报 <strong>73.90美元/盎司</strong>，日内涨 <strong>+1.62%</strong>。</li>
<li><strong>今日亚盘动态（6月5日）：</strong>现货白银亚盘早间一度突破 <strong>74.92美元/盎司</strong>（日内涨3%），但随后快速回落，最新失守 <strong>73美元/盎司</strong>，日内跌 <strong>-1.29%</strong>。高波动特征显著。</li>
<li><strong>近期趋势判断：</strong>白银自5月中旬近90美元/盎司高位持续回调后，目前在 <strong>72-76美元区间剧烈震荡</strong>。短期多空博弈激烈，72美元为关键支撑位，76美元为短期阻力。</li>
<li><strong>驱动因素简析：</strong>
<ul>
<li><strong>美元指数：</strong>美伊谈判本周末或重启，特朗普称协议签署后霍尔木兹海峡将重新开放，油价回落支撑贵金属但走势反复</li>
<li><strong>美联储政策：</strong>美国5月ADP就业超预期强化鹰派预期，市场等待今晚非农数据（北京时间20:30）</li>
<li><strong>工业需求：</strong>光伏、电子等工业用银需求维持高位，但瑞银将2026年底白银预测下调至80美元/盎司</li>
<li><strong>库存面：</strong>COMEX白银库存持续下降，实物供需偏紧提供中期底部支撑</li>
</ul></li>
<li><strong>黄金同步波动：</strong>现货黄金周四纽约尾盘报4471美元/盎司附近，日内震荡加剧。（数据来源：每经AI快讯、界面新闻、中金在线）</li>
</ul>

<h2>一、大盘解读（回顾昨日6月4日A股）</h2>
<p><strong>⚠️ A股今日已收盘——以下为6月4日（周四）收盘回顾</strong></p>
<ul>
<li><strong>上证指数：</strong>报收 <strong>4057.78点</strong>，跌 <strong>0.64%</strong></li>
<li><strong>深证成指：</strong>报收 <strong>15661.57点</strong>，跌 <strong>0.27%</strong></li>
<li><strong>创业板指：</strong>跌 <strong>0.83%</strong></li>
<li><strong>科创综指：</strong>逆势 <strong>涨0.69%</strong> —— 芯片半导体方向强势</li>
<li><strong>两市成交额：</strong> <strong>2.78万亿元</strong>，较6月3日缩量3740亿元</li>
<li><strong>市场特征：</strong>超4100只个股下跌，仅不到1000只上涨。结构性分化极致——资金极度集中流向芯片产业链相关方向。</li>
</ul>

<h2>二、AI板块整体市场概览</h2>
<blockquote>6月4日AI板块 <strong>内部分化剧烈</strong>。CPO方向经历6月3日集体暴涨后进入技术性回调，芯片半导体方向接棒上涨。科创综指逆势收红，半导体/芯片产业链逆势走强。整体表现为 <strong>"指数普跌但结构性热点延续"</strong>。隔夜美股三大指数收跌（道指-1.21%、标普-0.73%、纳指-0.89%），但费城半导体指数逆市创历史新高。Computex 2026大会进入尾声，但CPO量产、博通560亿AI芯片指引等核心事件影响力持续发酵。</blockquote>

<h2>三、细分领域动态</h2>

<h3>算力板块</h3>
<ul>
<li><strong>资金面</strong> 💰：6月4日主力资金净流入TOP10个股中，AI/科技方向占比极高。京东方A净流入 <strong>34.81亿元</strong>居首，三安光电净流入14.54亿元，沪电股份14.13亿元，兆易创新13.61亿元，中兴通讯12.18亿元，德明利11.73亿元，大族激光11.49亿元，通鼎互联9.13亿元。博通预测2026财年AI芯片销售额达560亿美元。</li>
<li><strong>政策面</strong> 📋：发改委/工信部联合发布《新一代人工智能发展规划(2026-2030)》，算力基础设施列为第一重点，<strong>2030年AI核心产业规模超5万亿元</strong>。"东数西算"2026年投资超2000亿元，大基金二期重点投向AI硬件。工信部发布"模数共振"行动面向20个重点行业推动制造业AI规模化落地。</li>
<li><strong>基本面</strong> 🔬：英伟达在Computex 2026宣布Vera CPU全面投产，RTX Spark PC芯片正式发布进军消费级市场。微软Build大会发布马约拉纳2代量子芯片（量子比特存续时长突破20秒）。博通已向OpenAI交付芯片并将于2027年部署1.3吉瓦算力基础设施。华为"韬定律"推动系统级优化，六年量产381款芯片。</li>
<li><strong>情绪面</strong> 😊：偏积极但内部轮动明显。CPO高位回调、芯片半导体接力，资金在AI产业各细分方向间轮动。中际旭创等高位标的需警惕短期获利了结压力。</li>
</ul>

<h3>存储板块</h3>
<ul>
<li><strong>资金面</strong> 💰：6月4日兆易创新主力净流入 <strong>13.61亿元</strong>（TOP5）。存储方向持续吸金。隔夜美股费城半导体指数逆市创历史新高，存储方向贡献显著。</li>
<li><strong>政策面</strong> 📋：SK集团会长崔泰源称SK海力士<strong>计划五年内晶圆产能翻番</strong>，产能瓶颈或持续到2030年。SK海力士扩产利好国内半导体设备和材料供应商。</li>
<li><strong>基本面</strong> 🔬：<strong>三星交付全球首批HBM4E样品</strong>（带宽超1.5TB/s），并在Computex 2026展示全球首款<strong>HBM5原型</strong>（带宽4TB/s目标）。英伟达向供应商探询2026年Q4交付16层堆叠HBM的可行性。HBM4E单堆叠48GB容量、带宽4.0TB/s。华特气体（电子特气）触及涨停。</li>
<li><strong>情绪面</strong> 😊：存储赛道持续高景气。HBM技术迭代加速（HBM3E→HBM4E→HBM5路线清晰），存储从周期股向高成长股切换的预期进一步强化。</li>
</ul>

<h3>机器人板块</h3>
<ul>
<li><strong>资金面</strong> 💰：6月4日机器人概念表现活跃，<strong>日盈电子、锋龙股份、日发精机</strong>涨停。但板块整体受大盘拖累表现分化。创业板人工智能ETF华宝(159363)主力资金净流入1.02亿元居可比基金首位。</li>
<li><strong>政策面</strong> 📋：工信部/国家数据局联合启动"模数共振"行动，面向钢铁、汽车、航空航天等20个重点行业推动AI+机器人应用。广州、深圳等"十五五"规划明确支持具身智能产业发展。</li>
<li><strong>基本面</strong> 🔬：<strong>宇树科技科创板73天闪电过会</strong>，估值420亿元成为"人形机器人第一股"。市场讨论正从可行性转向规模化——2028年人形机器人市场规模预计超138亿美元，2035年有望达2000亿美元。特斯拉Optimus预计2026年更广泛推广。小鹏新一代IRON机器人预计2026年底量产。</li>
<li><strong>情绪面</strong> 😊：概念向量产切换预期强烈。宇树IPO过会提振板块情绪，但需警惕"利好兑现"后的短期回调风险。板块PE 34.6倍处于近5年14%分位，估值相对合理，中长线逻辑清晰。</li>
</ul>

<h3>CPO板块</h3>
<ul>
<li><strong>资金面</strong> 💰：6月4日CPO板块经历6月3日集体大涨后进入<strong>技术性回调</strong>，跌幅居前。此前（6月2-3日）通信板块连续两日主力净流入居全行业首位（148-168亿元级别）。中际旭创市值突破1.4万亿元超越茅台后进入调整。</li>
<li><strong>政策面</strong> 📋：<strong>英伟达6月2日官宣Spectrum-X硅光CPO交换机全面量产</strong>，能效较传统方案提升5倍，明确2026年Q4实现CPO规模化商用。2026年被机构定义为<strong>CPO产业化元年</strong>。英伟达与Coherent、Corning、Lumentum签署多年战略协议锁定关键产能。</li>
<li><strong>基本面</strong> 🔬：中际旭创800G全球市占率超42%，1.6T全球唯一批量供货厂商，订单排期已覆盖至2028年。高盛预测2026年全球光模块市场规模达285-480亿美元，AI需求占比超六成。Lightcounting预测2026年以太网光模块市场增长65%。（数据来源：东方财富、高盛、Lightcounting）</li>
<li><strong>情绪面</strong> 😊：短期回调属于大涨后正常技术性调整，中长期逻辑不变。CPO方向仍是AI硬件中确定性最强的环节之一，英伟达量产+中际旭创独占供应两大支撑坚实。回调后关注资金是否回流。</li>
</ul>

<h2>四、主流净流入板块监控（6月4日）</h2>
<h3>沪深A股主力资金净流入TOP10个股</h3>
<ol>
<li><strong>京东方A</strong> —— 净流入 <strong>34.81亿元</strong>（面板/LED，涨停创近五年新高）</li>
<li><strong>三安光电</strong> —— 净流入 <strong>14.54亿元</strong>（化合物半导体）</li>
<li><strong>沪电股份</strong> —— 净流入 <strong>14.13亿元</strong>（PCB/AI服务器）</li>
<li><strong>兆易创新</strong> —— 净流入 <strong>13.61亿元</strong>（存储芯片）</li>
<li><strong>中兴通讯</strong> —— 净流入 <strong>12.18亿元</strong>（通信设备）</li>
<li><strong>德明利</strong> —— 净流入 <strong>11.73亿元</strong>（存储芯片）</li>
<li><strong>大族激光</strong> —— 净流入 <strong>11.49亿元</strong>（激光/半导体设备）</li>
<li><strong>通鼎互联</strong> —— 净流入 <strong>9.13亿元</strong>（光纤通信）</li>
<li><strong>厦门钨业</strong> —— 净流入 <strong>8.73亿元</strong>（有色金属）</li>
<li><strong>胜宏科技</strong> —— 净流入 <strong>7.72亿元</strong>（PCB）</li>
</ol>
<h3>行业板块净流入</h3>
<ul>
<li><strong>半导体/芯片</strong> —— 逆势领涨，主力净流入居行业首位</li>
<li><strong>煤炭板块</strong> —— 反复活跃，安泰集团、平煤股份双双涨停（资金防御性偏好）</li>
<li><strong>通信设备</strong> —— 6月3日净流入155亿后6月4日回调，资金阶段性获利了结</li>
<li><strong>电子元器件</strong> —— 资金持续流入，PCB、面板等细分方向受关注</li>
</ul>
<p><strong>AI板块相对热度判断：</strong> 🟡 <strong>中等偏上</strong>。6月4日市场普跌（超4100只下跌），但芯片/半导体方向逆势走强，表明AI产业链仍是存量资金最偏好的方向。CPO虽回调但属于大涨后的正常调整。AI板块在全市场中的资金热度排名靠前，但整体交投较6月3日明显缩量（两市缩量3740亿）。需关注今日（6月5日晚间）美股科技股表现对6月5日A股交易的影响。</p>

<h2>五、关键异动个股</h2>
<ol>
<li><strong>京东方A（000725）⬆ 涨停</strong> —— 百万股东迎涨停，股价创近五年来新高。面板行业景气度回升+AI PC需求预期+LED显示技术升级三重驱动。主力净流入34.81亿元居两市首位。</li>
<li><strong>中船特气（688146）⬆ 20CM涨停</strong> —— 半导体电子特气龙头，直接受益于HBM/先进封装产能扩张。存储芯片扩产驱动上游材料和设备需求爆发。</li>
<li><strong>太极实业（600667）⬆ 3天2板</strong> —— 半导体封测概念持续发酵，AI芯片封装需求旺盛带动板块活跃。</li>
</ol>

<h2>六、特斯拉机器人概念股解析</h2>
<ul>
<li><strong>Optimus量产进展：</strong> 中信证券研报显示特斯拉人形机器人V3版本设计接近定型，预计2026年7-8月启动规模化量产。宇树科技（A股"人形机器人第一股"）科创板73天闪电过会，拟募资42亿元。小鹏新一代IRON机器人预计2026年底量产，广州量产基地已动工建设。</li>
<li><strong>A股受益标的梳理：</strong>
<ul>
<li><strong>执行器/关节：</strong> 拓普集团、三花智控、肇民科技</li>
<li><strong>减速器：</strong> 绿的谐波、中大力德、双环传动</li>
<li><strong>电机：</strong> 汇川技术、鸣志电器、兆威机电</li>
<li><strong>传感器：</strong> 奥比中光（涨9.75%）、禾川科技</li>
<li><strong>灵巧手：</strong> 斯菱智驱、北特科技</li>
</ul></li>
<li><strong>行业数据：</strong> 宇树科技2025年人形机器人出货量全球首位，营收从2023年1.59亿飙升至2025年16.99亿元（复合增长率226%），毛利率60.13%。2026年Q1营收同比增长68.5%。摩根士丹利预计2025年全球出货约1.3万台（中国企业占近80%），执行器成本已降90%。（数据来源：宇树科技招股书、中信证券、摩根士丹利）</li>
</ul>

<h2>七、总结与展望</h2>
<h3>当前市场总结</h3>
<ol>
<li><strong>A股6月4日普跌调整：</strong> 三大指数集体下挫，超4100只个股下跌，但芯片半导体逆势走强，科创综指收红。CPO方向技术性回调，芯片接棒反映AI产业内部轮动健康。</li>
<li><strong>资金极度聚焦AI/科技方向：</strong> 主力资金净流入TOP10几乎全部为科技/半导体标的，AI产业链仍是市场最核心主线。</li>
<li><strong>白银波动加剧：</strong> 美伊局势反复 + 美联储鹰派预期 + 非农数据今晚出炉，多空博弈激烈。短期关注73美元支撑位是否有效。</li>
<li><strong>博通/英伟达指引强化算力主线：</strong> 博通560亿美元AI芯片销售额预测、英伟达CPO量产、三星HBM4E/HBM5技术迭代——AI算力上游硬件景气度持续升温。</li>
</ol>
<h3>下一交易日（6月5日）展望</h3>
<ul>
<li><strong>A股方向（今日9:30开盘）：</strong> 关注科创板/半导体能否延续强势。CPO方向经历两日回调后或迎技术性反弹。大盘若继续缩量则注意震荡风险。今晚美国5月非农数据（北京时间20:30）将影响全球市场情绪。</li>
<li><strong>美股隔夜：</strong> 关注费城半导体指数能否延续创历史新高的强势，中际旭创、新易盛等映射标的若企稳将提振CPO方向信心。</li>
<li><strong>白银：</strong> 今晚非农数据公布前后波动将加剧。若数据偏弱（提振降息预期），白银有望反弹至75美元上方；若数据偏强，可能再次考验72美元支撑。</li>
<li><strong>长期逻辑不变：</strong> 2026年为CPO产业化元年、AI算力资本开支持续高增（2030年全球或达1.5万亿美元）、人形机器人商业化拐点临近——三大产业趋势不变，回调即布局机会。</li>
</ul>
<hr />
<p><em>⚠️ 风险提示：以上内容为市场信息汇总，不构成投资建议。AI板块短期涨幅较大，需关注高位震荡和获利了结风险。投资有风险，决策需谨慎。</em></p>
<p><em>数据来源：东方财富、证券时报、Wind、Lightcounting、高盛、中信证券、中泰证券、每经AI快讯</em></p>
"""

# Read existing monitors.json
with open(DATA_FILE, 'r', encoding='utf-8') as f:
    monitors = json.load(f)

# Check for duplicate id
existing_ids = [m.get('id') for m in monitors]
if report_id in existing_ids:
    print(f"⚠️ Duplicate ID: {report_id}, will still add but check manually")
else:
    print(f"✅ No duplicate for {report_id}")

# Create new entry
new_entry = {
    "id": report_id,
    "date": report_date,
    "title": report_title,
    "tags": report_tags,
    "summary": report_summary,
    "html": html_content.strip()
}

# Append
monitors.append(new_entry)

# Write back
with open(DATA_FILE, 'w', encoding='utf-8') as f:
    json.dump(monitors, f, ensure_ascii=False, indent=2)

print(f"✅ Added entry: {report_id}")
print(f"📊 Total monitors: {len(monitors)}")

# Step: build and push
os.chdir(SITE_DIR)
result = subprocess.run(
    ["python3", "build_site.py", "--push"],
    capture_output=True, text=True, timeout=120
)
print(f"🔨 Build output: {result.stdout[-2000:]}")
if result.stderr:
    print(f"⚠️ Build stderr: {result.stderr[-1000:]}")
print(f"✅ Build return code: {result.returncode}")