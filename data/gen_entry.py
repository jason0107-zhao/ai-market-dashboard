#!/usr/bin/env python3
import json

with open('monitors.json', 'r') as f:
    data = json.load(f)

entry_id = "mon-20260603-1400"
data = [e for e in data if e['id'] != entry_id]

html = '<div class="metric-row">'
html += '<div class="metric-box"><div class="num">~4090</div><div class="lbs">上证指数</div></div>'
html += '<div class="metric-box"><div class="num">~15400</div><div class="lbs">深证成指</div></div>'
html += '<div class="metric-box"><div class="num">~4200</div><div class="lbs">创业板指</div></div>'
html += '<div class="metric-box"><div class="num">~1.9万亿</div><div class="lbs">半日成交</div></div>'
html += '<div class="metric-box"><div class="num">~76.7</div><div class="lbs">白银$</div></div>'
html += '</div>'

html += '<h1>AI板块盘中速览 · CPO/算力全面暴走 中际旭创超茅台 白银76震荡</h1>'
html += '<p><strong>时间：</strong>2026-06-03 14:00（A股交易中 · 午后盘）</p>'
html += '<div class="tagline">📌 <strong>核心基调：</strong>今日A股三大指数全面大涨，创业板指半日涨近4%站上4200点，科创50涨约4.8%。AI硬件（CPO/光模块/算力/半导体）全线暴走。中际旭创盘中股价超越贵州茅台，市值突破1.4万亿。英伟达Spectrum-X硅光以太网技术正式量产，COMPUTEX 2026多重催化持续发酵。COMEX白银期货报76.73美元/盎司，日内涨约2.1%。</div><hr>'

html += '<h2>📊 零、COMEX白银期货播报</h2>'
html += '<div class="info-grid">'
html += '<div class="info-item"><div class="il">COMEX白银期货</div><div class="iv"><strong>约76.73美元/盎司</strong> <span class="pill pill-up">日内+2.11%</span></div></div>'
html += '<div class="info-item"><div class="il">现货白银</div><div class="iv"><strong>约75.5-76.5美元</strong> <span class="pill pill-up">日内+约1%</span></div></div>'
html += '<div class="info-item"><div class="il">沪银主力</div><div class="iv"><strong>约18,330元/千克</strong> <span class="pill pill-up">小幅上涨</span></div></div>'
html += '<div class="info-item"><div class="il">美元指数</div><div class="iv"><strong>约99.2</strong> <span class="pill pill-down">低位运行</span></div></div>'
html += '<div class="info-item"><div class="il">COMEX黄金</div><div class="iv"><strong>约4,506美元</strong> <span class="pill pill-down">日内-0.31%</span></div></div>'
html += '<div class="info-item"><div class="il">美伊冲突</div><div class="iv" style="color:#f59e0b">今日凌晨伊朗袭击美军基地</div></div>'
html += '</div>'
html += '<p><strong>近期趋势判断：</strong>COMEX白银期货今日表现强劲，日内涨约2.11%至76.73美元，盘中最高触及77.23美元。白银近期在75-77美元区间<strong>震荡偏强</strong>运行，从5月中旬低点73美元区域逐步修复。但仍未突破80美元重要心理关口，整体处于<strong>宽幅震荡格局</strong>。</p>'
html += '<p><strong>驱动因素简析：</strong></p><ul>'
html += '<li><strong>中东地缘冲突：</strong>今日凌晨伊朗革命卫队宣布对美军基地发动报复性打击，推升避险情绪</li>'
html += '<li><strong>美元低位运行：</strong>美元指数99.2附近窄幅震荡，为贵金属提供计价支撑</li>'
html += '<li><strong>库存数据：</strong>美国6月1日COMEX白银库存变动14772.99百盎司，库存增加</li>'
html += '<li><strong>工业需求：</strong>光伏+AI数据中心建设维持白银需求高位</li>'
html += '<li><strong>机构观点：</strong>美银看多（Q4冲击100美元），瑞银偏谨慎（80美元目标）</li>'
html += '</ul><blockquote>💡 白银75-77美元区间震荡偏强，短线关注77美元能否站稳突破。</blockquote><hr>'

html += '<h2>一、大盘解读（午后盘）</h2>'
html += '<div class="info-grid">'
html += '<div class="info-item"><div class="il">上证指数</div><div class="iv">约4,090 <span class="pill pill-up">+0.56%</span></div></div>'
html += '<div class="info-item"><div class="il">深证成指</div><div class="iv">约15,400 <span class="pill pill-up">+2.31%</span></div></div>'
html += '<div class="info-item"><div class="il">创业板指</div><div class="iv">约4,200 <span class="pill pill-up"><strong>+3.97%</strong></span></div></div>'
html += '<div class="info-item"><div class="il">科创50</div><div class="iv"><span class="pill pill-up"><strong>+4.78%</strong></span></div></div>'
html += '<div class="info-item"><div class="il">半日成交</div><div class="iv"><strong>约1.89万亿元</strong></div></div>'
html += '<div class="info-item"><div class="il">上涨家数</div><div class="iv" style="color:#22c55e">超3300只</div></div>'
html += '</div>'
html += '<p>今日A股三大指数全面大涨，创业板指半日涨近4%站上4200点，科创50涨约4.8%。AI算力硬件成为全市场最强主线。<strong>芯片概念</strong>获主力净流入<strong>415.56亿元</strong>居板块第一，CPO获主力净流入<strong>300.04亿元</strong>居第二，数据中心(AIDC)<strong>298.32亿元</strong>居第三。培育钻石、光纤、CPO、半导体涨幅居前；影视院线、白酒、养鸡、房地产、零售板块跌幅居前。</p>'
html += '<p><strong>今日核心催化：</strong></p><ul>'
html += '<li>🔥 <strong>英伟达Spectrum-X硅光以太网技术正式量产</strong>——能效提升5倍</li>'
html += '<li>🔥 <strong>COMPUTEX 2026：黄仁勋公开表态Marvell有望冲击万亿市值</strong></li>'
html += '<li>🔥 <strong>中际旭创盘中超越贵州茅台</strong>市值突破1.4万亿</li>'
html += '<li>🔥 <strong>美股Marvell暴涨23.43%</strong>、Coherent涨15.16%</li>'
html += '<li>🔥 <strong>Lightcounting预测2026年以太网光模块市场增长65%</strong></li>'
html += '</ul><hr>'

html += '<h2>二、AI板块整体市场概览</h2>'
html += '<p>今日AI板块<strong>全面爆发</strong>。中证人工智能产业指数半日大涨<strong>3.28%</strong>。AI算力硬件（光模块/CPO/AI服务器/芯片）成为全市场最强主线。</p><ul>'
html += '<li><strong>光模块"易中天"齐创新高：</strong>中际旭创涨超10%超越茅台，天孚通信涨超14%突破500元，新易盛涨近9%突破800元</li>'
html += '<li><strong>光纤概念全面爆发：</strong>亨通光电、长飞光纤涨停</li>'
html += '<li><strong>芯片概念：</strong>半导体板块大涨4.18%</li>'
html += '</ul><hr>'

html += '<h2>三、细分领域动态</h2>'

html += '<div class="sect-card"><div class="sh">🔷 算力板块 <span class="pill pill-up">主力净流入415亿+</span> <span class="pill pill-up">情绪 极度乐观</span></div>'
html += '<p class="sn"><strong>资金面：</strong>算力板块（芯片概念）今日获主力资金净流入<strong>415.56亿元</strong>，位居全市场板块第一！板块内30股涨停，632股上涨。半导体板块半日主力净流入<strong>110.95亿元</strong>，板块大涨4.18%。工业富联获主力净流入7.22亿元，华工科技6.64亿元，长川科技6.61亿元。算力方向全面获得资金追捧。</p>'
html += '<p class="sn"><strong>政策面：</strong>上海发布全球资管中心建设新政，明确引导长线资金入局科技赛道，做好算力期货研发准备。国家能源局、工信部联合发文加快数据中心审批建设。</p>'
html += '<p class="sn"><strong>基本面：</strong>英伟达Spectrum-X硅光正式量产；Marvell CEO在COMPUTEX受黄仁勋盛赞；美股光通信全线暴涨；2027年光模块需求预期加速明朗。</p>'
html += '<p class="sn"><strong>情绪面：</strong>算力板块全面暴走，市场情绪极为乐观。中际旭创超越茅台标志科技股正式接过A股第一权重。</p></div>'

html += '<div class="sect-card"><div class="sh">🔷 存储板块 <span class="pill pill-up">跟随大涨</span> <span class="pill pill-up">情绪 乐观</span></div>'
html += '<p class="sn"><strong>资金面：</strong>兆易创新半日获主力净流入<strong>14.89亿元</strong>居前。澜起科技涨超8.5%。HBM概念同步走强。</p>'
html += '<p class="sn"><strong>政策面：</strong>长鑫科技科创板IPO过会后提交注册，拟募资295亿元。</p>'
html += '<p class="sn"><strong>基本面：</strong>美银发布半导体展望：AI投资持续扩张，存储周期逻辑或被改写。高盛和瑞银此前双重确认供不应求至2028年。</p>'
html += '<p class="sn"><strong>情绪面：</strong>存储板块受益于算力硬件整体爆发，HBM/DDR5涨价预期持续强化。</p></div>'

html += '<div class="sect-card"><div class="sh">🔷 机器人板块 <span class="pill pill-up">随大盘走强</span> <span class="pill pill-up">情绪 偏正面</span></div>'
html += '<p class="sn"><strong>资金面：</strong>奥比中光涨超9.5%领涨，宇树IPO过会积极影响仍在。</p>'
html += '<p class="sn"><strong>政策面：</strong>宇树科技6月1日已正式科创板IPO过会（73天），特斯拉Optimus Gen-3量产倒计时7-8月启动。</p>'
html += '<p class="sn"><strong>基本面：</strong>产业加速推进——Optimus量产按计划推进，宇树2025年人形出货超5500台全球第一。</p>'
html += '<p class="sn"><strong>情绪面：</strong>非今日主线，但中长期确定性支撑充分。浙商证券认为6月是配置好时机。</p></div>'

html += '<div class="sect-card"><div class="sh">🔷 CPO板块 <span class="pill pill-up">今日最强🔥</span> <span class="pill pill-up">情绪 极度乐观</span></div>'
html += '<p class="sn"><strong>资金面：</strong>CPO获主力净流入<strong>300.04亿元</strong>居板块第二！板块内16股涨停。通信设备主力净流入<strong>109.45亿元</strong>。通信ETF国泰飙涨<strong>8%</strong>，近20日流入超45亿元。CPO板块共诞生15只翻倍股。</p>'
html += '<p class="sn"><strong>资金面个股详情：</strong></p><ul>'
html += '<li><strong>天孚通信</strong> 主力净流入<strong>19.46亿</strong>（全市场第一）涨超14%破500元</li>'
html += '<li><strong>TCL科技</strong> 15.45亿 | <strong>通富微电</strong> 15.13亿 | <strong>兆易创新</strong> 14.89亿</li>'
html += '<li><strong>中际旭创</strong> 13.70亿 涨超10%超越茅台 | <strong>新易盛</strong> 12.46亿 涨近9%破800元</li>'
html += '<li><strong>立讯精密</strong> 8.40亿 | <strong>蓝思科技</strong> 8.26亿 | <strong>仕佳光子</strong> 7.51亿 | <strong>工业富联</strong> 7.22亿</li>'
html += '<li><strong>光迅科技</strong> 7.11亿 | <strong>华工科技</strong> 6.64亿 | <strong>亨通光电</strong> 5.77亿（涨停）</li>'
html += '</ul>'
html += '<p class="sn"><strong>政策面：</strong>英伟达Spectrum-X硅光以太网正式全面量产——新一代交换机基于CPO构建，能效提升5倍。2026年定义为<strong>CPO产业化元年</strong>。</p>'
html += '<p class="sn"><strong>基本面：</strong>中金研报指出全球光模块市场规模2027年将增至480亿美元以上；高盛预测2026年达285-480亿美元；1.6T商业化元年开启；源杰科技涨超17%创新高；<strong>金信诺</strong>高速光模块PCB已通过头部客户认证。</p>'
html += '<p class="sn"><strong>情绪面：</strong>CPO方向情绪达到<strong>极度乐观</strong>。中际旭创超越茅台是标志性事件。国盛证券建议"重回大光"关注光模块龙头。</p></div><hr>'

html += '<h2>四、主流净流入板块监控（午盘TOP10）</h2>'
html += '<table><tr><th>#</th><th>板块</th><th>净流入</th><th>核心驱动</th><th>类型</th></tr>'
html += '<tr><td><strong>1</strong></td><td><strong>芯片概念</strong></td><td><span class="green"><strong>+415.56亿</strong></span></td><td>AI算力爆发+硅光量产+半导体涨价</td><td><span class="pill pill-up">产业+业绩</span></td></tr>'
html += '<tr><td><strong>2</strong></td><td><strong>CPO</strong></td><td><span class="green"><strong>+300.04亿</strong></span></td><td>英伟达硅光量产+1.6T元年+Marvell暴涨</td><td><span class="pill pill-up">事件+产业</span></td></tr>'
html += '<tr><td><strong>3</strong></td><td><strong>数据中心(AIDC)</strong></td><td><span class="green"><strong>+298.32亿</strong></span></td><td>AI基建加码+算力需求爆发</td><td><span class="pill pill-up">产业驱动</span></td></tr>'
html += '<tr><td><strong>4</strong></td><td><strong>半导体</strong></td><td><span class="green"><strong>+110.95亿</strong></span></td><td>算力链传导+存储超级周期</td><td><span class="pill pill-up">产业驱动</span></td></tr>'
html += '<tr><td><strong>5</strong></td><td><strong>通信设备</strong></td><td><span class="green"><strong>+109.45亿</strong></span></td><td>光通信爆发+硅光量产+光纤需求</td><td><span class="pill pill-up">事件+产业</span></td></tr>'
html += '<tr><td><strong>6</strong></td><td>电子板块</td><td><span class="green">+109亿+</span></td><td>AI算力硬件全面爆发</td><td><span class="pill pill-up">产业驱动</span></td></tr>'
html += '<tr><td><strong>7</strong></td><td>光学光电子</td><td><span class="green">+32.65亿</span></td><td>TCL科技+蓝思科技领涨</td><td><span class="pill pill-mid">产业驱动</span></td></tr>'
html += '<tr><td><strong>8</strong></td><td>小金属</td><td><span class="green">+30.07亿</span></td><td>培育钻石+稀土轮动</td><td><span class="pill pill-mid">板块轮动</span></td></tr>'
html += '<tr><td><strong>9</strong></td><td>光纤概念</td><td><span class="green">涨停潮</span></td><td>中国移动三波段多芯光缆</td><td><span class="pill pill-mid">事件驱动</span></td></tr>'
html += '<tr><td><strong>10</strong></td><td>培育钻石</td><td><span class="green">板块走强</span></td><td>消费+工业双需求驱动</td><td><span class="pill pill-mid">板块轮动</span></td></tr>'
html += '</table>'
html += '<p><strong>资金流向核心发现：</strong></p><ul>'
html += '<li><strong>AI三条主线（芯片+CPO+AIDC）</strong>合计主力净流入超<strong>1,013亿元</strong>，占绝对主导！</li>'
html += '<li><strong>半导体+通信设备</strong>双双获百亿级加仓，是资金最密集方向</li>'
html += '<li><strong>净流出方向：</strong>电新行业、电网设备、医药、白酒——资金从消费防御全面回流科技</li>'
html += '<li><strong>AI板块相对热度：极高🔥</strong>——三条主线合计超1000亿净流入，碾压级热度</li>'
html += '<li><strong>南向资金：</strong>半日净买入超60亿港元</li>'
html += '<li><strong>新基金发行：</strong>6月191只新发基金，科技方向（科创板/芯片/AI）是主要方向</li>'
html += '</ul><hr>'

html += '<h2>五、关键异动个股</h2>'
html += '<table><tr><th>个股</th><th>异动</th><th>逻辑</th></tr>'
html += '<tr><td><strong>中际旭创</strong></td><td><span class="pill pill-up"><strong>涨超10%超越茅台！</strong></span><br>净流入13.70亿</td><td>CPO/光模块全球龙头，英伟达硅光量产+1.6T批量出货+2027年需求明朗</td></tr>'
html += '<tr><td><strong>天孚通信</strong></td><td><span class="pill pill-up"><strong>涨超14%破500元</strong></span><br>净流入19.46亿（全市场第一）</td><td>光模块龙头，深度受益英伟达硅光量产+CPO元年</td></tr>'
html += '<tr><td><strong>源杰科技</strong></td><td><span class="pill pill-up"><strong>涨超17%创新高</strong></span></td><td>光芯片龙头，硅光技术路线核心受益标的</td></tr>'
html += '<tr><td><strong>新易盛</strong></td><td><span class="pill pill-up"><strong>涨近9%破800元</strong></span><br>净流入12.46亿</td><td>1.6T光模块批量出货+COMPUTEX+英伟达双催化</td></tr>'
html += '<tr><td><strong>金信诺</strong></td><td><span class="pill pill-up"><strong>涨12%</strong></span></td><td>高速光模块PCB通过头部客户认证，下半年批量供应</td></tr>'
html += '</table><hr>'

html += '<h2>六、特斯拉机器人概念股解析</h2>'
html += '<p><strong>最新产业进展：</strong></p><ul>'
html += '<li>特斯拉Optimus Gen-3量产倒计时：<strong>2026年7-8月启动量产</strong>，加州工厂年产能100万台</li>'
html += '<li>宇树科技6月1日已正式科创板IPO过会（73天），拟募资42亿元</li>'
html += '<li>COMPUTEX 2026首次设立机器人专区</li>'
html += '<li>特斯拉弗里蒙特工厂Model S/X产线已全面改造为Optimus专用线</li>'
html += '</ul>'
html += '<table><tr><th>环节</th><th>核心公司</th><th>代码</th><th>受益逻辑</th><th>优先级</th></tr>'
html += '<tr><td><strong>执行器/总成</strong></td><td>三花智控、拓普集团</td><td>002050/601689</td><td>线性/旋转执行器核心供应商</td><td>⭐⭐⭐</td></tr>'
html += '<tr><td><strong>精密减速器</strong></td><td>绿的谐波、双环传动</td><td>688017/002472</td><td>谐波减速器/RV减速器</td><td>⭐⭐⭐</td></tr>'
html += '<tr><td><strong>伺服电机</strong></td><td>汇川技术、卧龙电驱</td><td>300124/600580</td><td>驱控一体方案</td><td>⭐⭐</td></tr>'
html += '<tr><td><strong>传感器</strong></td><td>柯力传感、奥比中光</td><td>603662/688322</td><td>力矩/3D视觉传感器</td><td>⭐⭐</td></tr>'
html += '<tr><td><strong>灵巧手</strong></td><td>峰岹科技</td><td>688279</td><td>电机驱动芯片</td><td>⭐⭐</td></tr>'
html += '<tr><td><strong>结构件/代工</strong></td><td>工业富联、长盈精密</td><td>601138/300115</td><td>整机代工+轻量化结构件</td><td>⭐⭐</td></tr>'
html += '<tr><td><strong>电池/电源</strong></td><td>珠海冠宇</td><td>688772</td><td>机器人电池方案</td><td>⭐</td></tr>'
html += '</table><hr>'

html += '<h2>七、总结与展望</h2>'
html += '<div class="info-grid">'
html += '<div class="info-item"><div class="il">📌 当前特征</div><div class="iv" style="font-size:14px">AI板块今日<strong>全面爆发</strong>，CPO/光模块/算力全线暴走。中际旭创超越茅台是历史性时刻。创业板涨近4%站上4200点。英伟达硅光量产是最核催化。</div></div>'
html += '<div class="info-item"><div class="il">🔥 今日核心事件</div><div class="iv" style="font-size:14px"><strong>1) 英伟达Spectrum-X硅光量产</strong>——CPO产业化元年正式确立<br><strong>2) 中际旭创超越茅台</strong>——科技股正式接过A股第一权重<br><strong>3) Marvell暴涨23%</strong>——COHERENT+15%，全球光通信狂潮</div></div>'
html += '<div class="info-item"><div class="il">💡 午后关注</div><div class="iv" style="font-size:14px">1) 午后AI板块能否守住涨幅，创业板能否站稳4200<br>2) CPO板块在连续大涨后是否出现冲高回落<br>3) 存储芯片方向是否接力轮动（龙头涨势已启动）<br>4) 关注港股南向资金下午是否持续加码</div></div>'
html += '<div class="info-item"><div class="il">⚠️ 风险提示</div><div class="iv" style="font-size:14px;color:#f59e0b">① CPO板块年内诞生15只翻倍股，短期涨幅巨大需警惕获利回吐；② 科创50在连续大涨后筹码结构可能恶化；③ 中际旭创突破万亿后机构分歧加大；④ 以上分析基于公开数据整理，<strong>不构成投资建议</strong></div></div>'
html += '</div>'
html += '<blockquote>⚠️ 以上分析基于公开数据和搜索结果整理，不构成投资建议。股市有风险，投资需谨慎。<br>📝 报告生成时间：2026-06-03 14:00 | 数据来源：公开市场信息 | 监测周期：1小时</blockquote>'

entry = {
    "id": entry_id,
    "date": "2026-06-03 14:00",
    "title": "AI板块盘中速览 · CPO/算力全面暴走 中际旭创超茅台 白银76震荡 · 英伟达硅光量产",
    "tags": ["盘中", "CPO", "算力", "硅光量产", "中际旭创", "白银", "COMPUTEX", "机器人"],
    "summary": "AI硬件全面暴走CPO/光模块领涨，中际旭创超越茅台创历史，英伟达Spectrum-X硅光量产点燃产业预期。创业板涨近4%，COMEX白银76.7美元。",
    "html": html
}

data.append(entry)

with open('monitors.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Entry {entry_id} added successfully. Total entries: {len(data)}")

# Verify
with open('monitors.json', 'r') as f:
    check = json.load(f)
last = check[-1]
print(f"Verified last entry: {last['id']} - {last['title'][:50]}")
print(f"HTML length: {len(last['html'])} chars")