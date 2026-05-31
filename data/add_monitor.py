#!/usr/bin/env python3
import json, sys
from datetime import datetime

now = datetime.now()
ts = now.strftime("%Y%m%d-%H%M")
date_str = now.strftime("%Y-%m-%d %H:%M")

# Report HTML content
html = """<div class=\"metric-row\">
  <div class=\"metric-box\"><div class=\"num\">75.2</div><div class=\"lbs\">COMEX白银(美元)</div></div>
  <div class=\"metric-box\"><div class=\"num\">99.03</div><div class=\"lbs\">美元指数</div></div>
  <div class=\"metric-box\"><div class=\"num\">4068.57</div><div class=\"lbs\">上周五上证</div></div>
  <div class=\"metric-box\"><div class=\"num\">-5.04%</div><div class=\"lbs\">科创50</div></div>
</div>

<h1>AI板块周日夜盘复盘 · 白银窄幅震荡 关注下周超级催化</h1>
<p><strong>时间：</strong>2026-05-31 22:00（A股非交易时段 &#8226; 周日）</p>

<div class=\"tagline\">📌 <strong>核心基调：</strong>当前为A股非交易时段（周日夜晚）。上周五科技全线退潮情绪尚待修复，周末消息面相对平静。COMEX白银在75-76美元区间窄幅震荡。下周迎接超级催化周——6/1宇树科技IPO上会 + 6/2-6/5 Computex大会，将决定AI板块短期方向。</div>

<hr>

<h2>📊 零、COMEX白银期货播报</h2>
<div class=\"info-grid\">
  <div class=\"info-item\"><div class=\"il\">COMEX白银期货</div><div class=\"iv\"><strong>~75.2美元/盎司</strong> <span class=\"pill pill-mid\">日内 窄幅震荡</span></div></div>
  <div class=\"info-item\"><div class=\"il\">现货白银</div><div class=\"iv\"><strong>~74.98-75.25美元/盎司</strong> <span class=\"pill pill-mid\">窄幅波动</span></div></div>
  <div class=\"info-item\"><div class=\"il\">沪银TD</div><div class=\"iv\"><strong>~18,280元/千克</strong></div></div>
  <div class=\"info-item\"><div class=\"il\">美元指数</div><div class=\"iv\"><strong>~99.03</strong> <span class=\"pill pill-down\">近期低位</span></div></div>
  <div class=\"info-item\"><div class=\"il\">COMEX黄金</div><div class=\"iv\"><strong>~4,538美元/盎司</strong></div></div>
</div>
<p><strong>近期趋势判断：</strong>COMEX白银自上周五金价的强力反弹(+3.81%)后，周末进入了<strong>窄幅震荡整固</strong>阶段，现货价格在75美元附近整理。周线来看本周COMEX白银<strong>下跌约0.93%</strong>，市场多空分歧仍然激烈。整体处于<strong>72-80美元宽幅震荡区间</strong>的中枢位。</p>
<p><strong>驱动因素简析：</strong></p>
<ul>
  <li><strong>✅ 美元走弱提供支撑：</strong>美元指数报99.03，处于近期低位，对贵金属形成基础支撑</li>
  <li><strong>⚠️ 美联储紧缩预期：</strong>新任主席沃什表态优先控制通胀，市场对降息的预期迅速冷却，甚至开始讨论加息可能性</li>
  <li><strong>⚠️ 4月CPI超预期：</strong>美国4月CPI同比+3.8%，远超预期，强化了紧缩预期，压制白银上行空间</li>
  <li><strong>✅ 供需缺口持续：</strong>全球白银供应已连续第六年短缺，2026年缺口预计约4630万盎司，库存处于低位</li>
  <li><strong>✅ 工业需求故事：</strong>光伏+AI数据中心建设对白银工业需求维持高位，但高价正在侵蚀部分工业需求</li>
  <li><strong>⚠️ 印度提高白银进口关税：</strong>从6%大幅提高至15%，可能抑制来自印度的边际需求</li>
  <li><strong>机构观点严重分歧：</strong>美国银行看年内100美元（但称\"昙花一现\"）、瑞银下调目标至80美元、汇丰认为\"基本面明显高估\"</li>
</ul>
<blockquote>💡 白银当前处于72-80美元宽幅震荡区间中枢位（75美元）。短线支撑72美元，压力80美元。下周关注6/5美国非农数据对贵金属方向的指引。</blockquote>

<hr>

<h2>一、AI板块整体市场概览</h2>
<p>当前为A股非交易时段（周日22:00）。上周五（5月29日）A股三大指数全线收跌——上证指数-0.73%报4068.57，深证成指-1.81%报15575.13，<strong>科创50暴跌5.04%</strong>领跌全场。</p>
<p>上周五市场呈现极端\"高切低\"格局——科技板块全面退潮，AI/半导体高位股集体回调，主力资金单日净流出831亿元，<strong>电子行业净流出372亿元居首</strong>。电力/公用事业/消费等防御板块逆势吸金。</p>
<p>但产业基本面并未恶化——调整属于<strong>交易层面的筹码消化</strong>，而非产业逻辑破坏。下周迎来两大关键催化：</p>

<hr>

<h2>二、细分领域动态</h2>

<div class=\"sect-card\">
<div class=\"sh\">🔷 算力板块 <span class=\"pill pill-mid\">调整消化中</span></div>
<p class=\"sn\"><strong>资金面：</strong>上周五电子行业净流出372亿元居全行业首位。算力ETF全线收跌，中芯国际主力净流出31.4亿居全市场第一。资金短期从高位科技品种系统出逃。</p>
<p class=\"sn\"><strong>政策面：</strong>工信部十部门联合印发《人工智能科技伦理审查与服务办法(试行)》。国家网信办/发改委/工信部联合发布《智能体规范应用与创新发展实施意见》，为AI产业发展提供政策框架。下周<strong>6/2-6/5 Computex大会</strong>以\"AI Together\"为主题，是最重要的催化窗口。</p>
<p class=\"sn\"><strong>基本面：</strong>Cerebras在美上市首日暴涨89%市值达750亿美元，验证AI算力赛道高景气。戴尔AI服务器营收161亿美元同比+757%。四大云厂商2026年合计资本支出7250亿美元(+77%)，AI基建投资持续超预期。华为发布韬(τ)定律，为国产算力提供理论框架。</p>
<p class=\"sn\"><strong>情绪面：</strong>短线情绪偏谨慎，高位筹码需消化。但美股AI热度不减（纳指创新高），调整更多是A股内部资金博弈——\"高切低\"。待Computex催化释放后企稳概率大。</p>
</div>

<div class=\"sect-card\">
<div class=\"sh\">🔷 存储板块 <span class=\"pill pill-mid\">情绪中期乐观</span></div>
<p class=\"sn\"><strong>资金面：</strong>上周五跟随半导体整体回调。北向资金在存储龙头上交投活跃——澜起科技沪股通成交42亿、兆易创新33.86亿，但方向偏流出。佰维存储盘中逆势上涨0.94%。</p>
<p class=\"sn\"><strong>基本面：</strong>HBM景气度持续超预期——HBM3E现货价半年暴涨超300%。三星率先交付首批12层48GB HBM4E样品，传输速度14-16Gbps，带宽达3.6TB/s。美光警告内存短缺将持续至2026年后。HBM在AI芯片成本占比已升至63%。全球DRAM营收2026Q1逼近970亿美元（环比+80%，同比+260%），创历史新高。</p>
<p class=\"sn\"><strong>情绪面：</strong>产业数据极为强势，但短期股价已充分反映涨价预期。中长期来看，HBM是AI产业链中<strong>供需格局最紧张</strong>的环节之一，涨价至少持续到2027年。</p>
</div>

<div class=\"sect-card\">
<div class=\"sh\">🔷 机器人板块 <span class=\"pill pill-up\">关注明日IPO上会</span></div>
<p class=\"sn\"><strong>资金面：</strong>上周五延续回调态势，5月27日单日净流出143亿元后尚未企稳。</p>
<p class=\"sn\"><strong>基本面：</strong><strong>重大催化：明日（6月1日）宇树科技科创板IPO上会</strong>，冲刺A股\"人形机器人第一股\"，拟募资42.02亿元。2026年为规模化验证关键期。海关数据4月工业机器人出口量突破2.5万台（同比+90%）。特斯拉Optimus Gen-3已下线投入内部测试，Q2启动量产。小鹏宣布2026年完成Robotaxi和人形机器人量产。</p>
<p class=\"sn\"><strong>情绪面：</strong>市场对宇树IPO高度关注——成功过会将为整个机器人板块注入强心剂，是短期最重要的情绪催化剂。</p>
</div>

<div class=\"sect-card\">
<div class=\"sh\">🔷 CPO板块 <span class=\"pill pill-up\">通信线缆方向持续关注</span></div>
<p class=\"sn\"><strong>资金面：</strong>CPO板块内部分化——光模块龙头高位震荡，但<strong>通信线缆及配套</strong>方向逆势净流入39.83亿元。亨通光电主力净流入39.76亿居全市场第一，剑桥科技净流入11.73亿。</p>
<p class=\"sn\"><strong>基本面：</strong>2026年定义<strong>CPO产业化元年</strong>。英伟达明确Q4启动CPO量产，鸿海CPO全光交换机出货目标上调至5万台以上。LightCounting预测2030年CPO市场规模达100亿美元。中际旭创2026Q1营收194.96亿元（+192%），净利润57.35亿元（+262%）。</p>
<p class=\"sn\"><strong>情绪面：</strong>光模块龙头短期调整属获利回吐。通信线缆作为CPO新延伸方向获资金持续关注。下周Computex上英伟达Vera Rubin架构相关展示可能进一步催化CPO方向。</p>
</div>

<hr>

<h2>三、主流净流入板块监控（基于5月29日数据）</h2>
<table>
  <tr><th>#</th><th>板块</th><th>净流入(亿元)</th><th>驱动原因</th><th>类型</th></tr>
  <tr><td><strong>1</strong></td><td>电力</td><td><span class=\"green\">+43.08</span></td><td>防御属性+夏季用电高峰预期</td><td><span class=\"pill pill-mid\">防御配置</span></td></tr>
  <tr><td><strong>2</strong></td><td>公用事业</td><td><span class=\"green\">+41.74</span></td><td>科技→防御资金大迁徙</td><td><span class=\"pill pill-mid\">防御配置</span></td></tr>
  <tr><td><strong>3</strong></td><td>通信线缆及配套</td><td><span class=\"green\">+39.83</span></td><td>CPO/算力互联延伸，亨通光电领涨</td><td><span class=\"pill pill-up\">产业驱动</span></td></tr>
  <tr><td><strong>4</strong></td><td>印制电路板</td><td><span class=\"green\">+28.51</span></td><td>AI服务器PCB需求放量</td><td><span class=\"pill pill-up\">业绩驱动</span></td></tr>
  <tr><td><strong>5</strong></td><td>火力发电</td><td><span class=\"green\">+24.79</span></td><td>防御+高分红+估值洼地</td><td><span class=\"pill pill-mid\">防御配置</span></td></tr>
  <tr><td><strong>6</strong></td><td>食品饮料</td><td><span class=\"green\">+21.60</span></td><td>消费复苏+618大促预期</td><td><span class=\"pill pill-mid\">防御配置</span></td></tr>
  <tr><td><strong>7</strong></td><td>商贸零售</td><td><span class=\"green\">+20.22</span></td><td>端午消费旺季预期</td><td><span class=\"pill pill-mid\">事件驱动</span></td></tr>
  <tr><td><strong>8</strong></td><td>白酒</td><td><span class=\"green\">+18.43</span></td><td>贵州茅台主力净流入9.19亿</td><td><span class=\"pill pill-mid\">防御配置</span></td></tr>
  <tr><td><strong>9</strong></td><td>通信设备</td><td><span class=\"green\">+13.13</span></td><td>CPO/5G/光通信产业链</td><td><span class=\"pill pill-up\">产业驱动</span></td></tr>
  <tr><td><strong>10</strong></td><td>免税店概念</td><td><span class=\"green\">+18.59</span></td><td>端午消费旺季+政策利好</td><td><span class=\"pill pill-mid\">事件驱动</span></td></tr>
</table>
<p><strong>资金流向核心发现：</strong></p>
<ul>
  <li>上周五全市场主力净流出831.55亿元，连续多日净流出</li>
  <li><strong>电力+公用事业</strong>合计净流入~85亿元；<strong>电子行业</strong>净流出372亿元居首</li>
  <li>AI相关板块（电子+计算机+通信）合计净流出超过400亿元，相对热度降至冰点</li>
  <li>通信线缆是AI板块中<strong>唯一的逆势吸金方向</strong>——CPO产业链资金持续活跃</li>
  <li>北向资金成交4734亿但整体呈净流出态势，外资同步\"高切低\"</li>
</ul>

<hr>

<h2>四、关键异动个股</h2>
<table>
  <tr><th>个股</th><th>代码</th><th>异动</th><th>逻辑</th></tr>
  <tr><td><strong>亨通光电</strong></td><td>600487</td><td><span class=\"pill pill-up\">主力净流入39.76亿 全市场第一</span></td><td>通信线缆龙头，CPO/算力互联概念延伸受益，获主力资金集中追捧</td></tr>
  <tr><td><strong>中芯国际</strong></td><td>688981</td><td><span class=\"pill pill-down\">主力净流出31.4亿 全市场第一</span></td><td>半导体龙头获利回吐，高开低走拖累板块</td></tr>
  <tr><td><strong>博杰股份</strong></td><td>002975</td><td><span class=\"pill pill-up\">涨停</span></td><td>AI算力+业绩爆发(净利增557%)，切入英伟达供应链</td></tr>
</table>

<hr>

<h2>五、特斯拉机器人概念股解析</h2>
<table>
  <tr><th>环节</th><th>核心公司</th><th>代码</th><th>受益逻辑</th><th>进度</th></tr>
  <tr><td><strong>执行器</strong></td><td>三花智控</td><td>002050</td><td>线性/旋转执行器，已进入Optimus验证环节</td><td><span class=\"pill pill-up\">验证中</span></td></tr>
  <tr><td><strong>减速器</strong></td><td>绿的谐波</td><td>688017</td><td>谐波减速器国产龙头，机器人关节核心零部件</td><td><span class=\"pill pill-up\">批量供应</span></td></tr>
  <tr><td><strong>传感器</strong></td><td>柯力传感</td><td>603662</td><td>力矩传感器潜在供应商，国产替代空间大</td><td><span class=\"pill pill-mid\">送样阶段</span></td></tr>
  <tr><td><strong>电机</strong></td><td>汇川技术</td><td>300124</td><td>伺服电机/驱动龙头，延伸至机器人领域</td><td><span class=\"pill pill-up\">研发中</span></td></tr>
  <tr><td><strong>结构件</strong></td><td>拓普集团</td><td>601689</td><td>一体化压铸+机器人结构件，平台型扩张</td><td><span class=\"pill pill-mid\">送样阶段</span></td></tr>
</table>
<p>特斯拉于5月初宣布Optimus Gen-3已下线投入内部测试，Q2正式启动量产，弗里蒙特汽车产线已开启换产，目标年产能100万台。这将带动国内供应链进入放量验证期。A股核心受益标的中，<strong>三花智控</strong>（执行器）和<strong>绿的谐波</strong>（减速器）确定性最强。</p>

<hr>

<h2>六、总结与展望</h2>
<div class=\"info-grid\">
  <div class=\"info-item\"><div class=\"il\">📌 当前状态</div><div class=\"iv\" style=\"font-size:14px\">A股非交易时段（周日22:00）。上周五科技全面退潮情绪尚待修复，周末消息面平静。白银窄幅震荡于75美元附近。</div></div>
  <div class=\"info-item\"><div class=\"il\">👀 下周超级催化</div><div class=\"iv\" style=\"font-size:14px\"><strong>1) 6/1 宇树科技科创板IPO上会</strong> — 人形机器人第一股，过会将注入强心剂<br><strong>2) 6/2-6/5 Computex大会</strong> — AI年度最强催化窗口，英伟达/AMD最新产品方案<br><strong>3) 6/5 美国非农数据</strong> — 影响美联储加息节奏和贵金属方向</div></div>
  <div class=\"info-item\"><div class=\"il\">💡 美股指引</div><div class=\"iv\" style=\"font-size:14px\">上周美股三大指数齐创新高（纳指六连涨+0.91%），AI产业热度不减。A股的调整更多是<strong>内部资金博弈的高切低</strong>。若下周Computex催化落地，科技板块企稳概率大。</div></div>
  <div class=\"info-item\"><div class=\"il\">💡 白银展望</div><div class=\"iv\" style=\"font-size:14px\">COMEX白银在72-80美元区间宽幅震荡，75美元中枢位。下周关注非农数据对美联储降息预期的指引。美元指数若继续走弱将支撑白银向上测试80美元。</div></div>
  <div class=\"info-item\"><div class=\"il\">⚠️ 风险提示</div><div class=\"iv\" style=\"font-size:14px;color:#f59e0b\">主力资金连续多日大额净流出，若下周Computex/宇树IPO催化不及预期，AI板块调整时间和幅度可能超出预期。仓位管理是第一要务。</div></div>
  <div class=\"info-item\"><div class=\"il\">🧭 策略建议</div><div class=\"iv\" style=\"font-size:14px\">保持核心仓位不动，利用调整<strong>逢低分批布局</strong>算力/光模块龙头。重点关注Computex大会英伟达Vera Rubin架构细节和CPO产业化时间表。CPO产业链通信线缆方向值得持续跟踪。</div></div>
</div>
<blockquote>⚠️ 以上分析基于公开数据整理，不构成投资建议。股市有风险，投资需谨慎。</blockquote>"""

entry = {
    "id": f"mon-{ts}",
    "date": date_str,
    "title": "AI板块周日夜盘复盘 · 白银窄幅震荡 聚焦下周宇树IPO/Computex超级催化",
    "tags": ["周日夜盘", "白银", "等待催化", "宇树IPO", "Computex", "CPO", "高切低"],
    "summary": "A股非交易时段，白银75美元窄幅震荡。关注明日宇树科技IPO上会和Computex大会催化。",
    "html": html
}

with open("/root/.joyclaw/workspace-er-ji-shi-chang-yan-jiu-yuan-vxu6-d552a7b0dc9d-81c90a43/site/data/monitors.json", "r") as f:
    data = json.load(f)

# Check for duplicate id
ids = {item["id"] for item in data}
if entry["id"] not in ids:
    data.append(entry)
    with open("/root/.joyclaw/workspace-er-ji-shi-chang-yan-jiu-yuan-vxu6-d552a7b0dc9d-81c90a43/site/data/monitors.json", "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Added entry {entry['id']}")
else:
    print(f"Duplicate id {entry['id']}, skipping")