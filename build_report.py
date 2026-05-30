#!/usr/bin/env python3
"""Build and append monitor entry to monitors.json."""
import json, os

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
MONITORS_PATH = os.path.join(DATA_DIR, "monitors.json")

MONITOR_ID = "mon-20260530-1307"
REPORT_DATE = "2026-05-30 13:07"
TITLE = "AI板块周末午间复盘 · 周末休市 聚焦下周Computex/宇树IPO双重催化"

TAGS = ["周末复盘", "休市", "Computex", "宇树IPO", "白银", "COMEX白银"]

SUMMARY = "周六A股休市。本周科技高切低，科创50周跌超5%。COMEX白银周末震荡。下周Computex大会和宇树IPO是AI板块双重催化。"

HTML = """<div class="metric-row">
  <div class="metric-box"><div class="num">休市</div><div class="lbs">A股状态</div></div>
  <div class="metric-box"><div class="num">4068.57</div><div class="lbs">上证周收</div></div>
  <div class="metric-box"><div class="num">-5.04%</div><div class="lbs">科创50周跌</div></div>
  <div class="metric-box"><div class="num">$75.58</div><div class="lbs">COMEX白银</div></div>
</div>

<h1>AI板块周末午间复盘</h1>
<p><strong>时间：</strong>2026-05-30 13:07（A股今日休市 — 周六）</p>

<div class="tagline">📌 <strong>周末核心看点：</strong>A股本周经历了\"高切低\"的剧烈切换——周五科技全面退潮、科创50暴跌5.04%，而电力/公用事业等防御板块逆势吸金。周末消息面整体平静，市场目光聚焦下周两件大事：<strong>① 6/1 宇树科技IPO上会</strong>（人形机器人第一股）；<strong>② 6/2-6/5 Computex大会</strong>（全球AI年度催化窗口）。COMEX白银本周收报75.58美元/盎司，较前一交易日微跌。</div>

<hr>

<h2>📊 零、COMEX白银期货播报</h2>
<div class="info-grid">
  <div class="info-item"><div class="il">COMEX白银期货</div><div class="iv"><strong>75.58 美元/盎司</strong> <span class="pill pill-down">周跌 -0.81%</span></div></div>
  <div class="info-item"><div class="il">现货白银</div><div class="iv"><strong>75.47 美元/盎司</strong> <span class="pill pill-mid">5月累涨 +2.1%</span></div></div>
  <div class="info-item"><div class="il">COMEX黄金期货</div><div class="iv"><strong>4,569.90 美元/盎司</strong> <span class="pill pill-up">周涨 +0.28%</span></div></div>
  <div class="info-item"><div class="il">美元指数</div><div class="iv"><strong>约99.33</strong> <span class="pill pill-down">近期走弱</span></div></div>
  <div class="info-item"><div class="il">沪银主力</div><div class="iv"><strong>17,790元/千克</strong> <span class="pill pill-down">沪银 -4.31%</span></div></div>
  <div class="info-item"><div class="il">白银月线</div><div class="iv"><strong>5月累涨 +2.1%</strong></div></div>
</div>

<p><strong>近期趋势判断：</strong>白银经历了极为剧烈的5月行情——5月上旬从70美元快速拉升至89.3美元（5月13日年内高点），随后因美国CPI数据超预期引发恐慌性抛售，单日暴跌超9%，一路回撤至73美元附近。近期在74-78美元区间震荡筑底。周末报75.58美元，处于<strong>宽幅震荡下的低位整固</strong>阶段。</p>

<p><strong>驱动因素简析：</strong></p>
<ul>
  <li><strong>美元弱势提供支撑：</strong>美元指数持续走弱至99.33附近，对贵金属整体形成支撑</li>
  <li><strong>美联储降息预期反复：</strong>美国4月PCE物价指数同比+3.8%创三年新高，通胀粘性超预期，市场对降息节奏的预期出现明显摇摆</li>
  <li><strong>工业需求持续定价：</strong>光伏+AI数据中心+新能源汽车对白银工业需求维持高位，为银价提供中长期底部支撑</li>
  <li><strong>美伊和谈进展：</strong>周末美伊谈判接近达成的消息主导市场情绪，地缘风险溢价有所下降</li>
  <li><strong>机构观点分化：</strong>美银看多（预测Q4触及100美元），瑞银偏谨慎（下调目标至85美元），两机构分歧反映市场对后市研判的不确定性</li>
  <li><strong>CFTC持仓：</strong>截至5月26日一周，COMEX白银投机净多头减少1517手至10244手，投机热情降温</li>
</ul>

<blockquote>💡 白银当前处于72-80美元震荡区间，短线关键支撑72-75美元，上方压力80美元。5月振幅达18.81%，波动极为剧烈。操作上建议控制仓位，避免追涨杀跌。</blockquote>

<hr>

<h2>一、大盘解读（本周五收盘数据）</h2>
<p>本周五（5月29日）A股三大指数高开低走，全线收跌：</p>
<div class="info-grid">
  <div class="info-item"><div class="il">上证指数</div><div class="iv">4068.57 <span class="pill pill-down">-0.73%</span></div></div>
  <div class="info-item"><div class="il">深证成指</div><div class="iv">15575.13 <span class="pill pill-down">-1.81%</span></div></div>
  <div class="info-item"><div class="il">创业板指</div><div class="iv">约4038 <span class="pill pill-down">-2.11%</span></div></div>
  <div class="info-item"><div class="il">科创50</div><div class="iv">1751.32 <span class="pill pill-down">-5.04% 💥</span></div></div>
  <div class="info-item"><div class="il">两市成交</div><div class="iv"><strong>3.32万亿元</strong>（放量+3500亿）</div></div>
</div>

<p>全市场仅1565只上涨，3867只下跌，涨跌比约3:7。主力资金净流出<strong>831.55亿元</strong>，其中电子行业净流出<strong>372.05亿元</strong>居全行业第一。</p>

<p><strong>5月整体回顾：</strong></p>
<ul>
  <li>沪指先扬后抑，<strong>月线收阴</strong>；但科创50本月累计涨超<strong>11%</strong>，突破2020年7月以来高点</li>
  <li>创业板指涨近<strong>10%</strong>站稳4000点</li>
  <li>芯片产业链为5月绝对主线——中芯国际、寒武纪、北方华创等多只龙头股价迭创历史新高</li>
  <li>AI算力硬件（\"易中天\"光模块、PCB等）持续走出趋势行情</li>
</ul>

<hr>

<h2>二、AI板块整体市场概览</h2>
<p>本周AI板块经历<strong>先扬后抑、高切低剧烈切换</strong>：</p>
<ul>
  <li><strong>周初：</strong>\"易中天\"齐创历史新高，半导体全面爆发，创业板首超沪指</li>
  <li><strong>周中：</strong>半导体制裁传闻催化国产替代，算力链延续强势</li>
  <li><strong>周五：</strong>科技全线退潮，科创50暴跌5.04%，电子行业主力净流出372亿元</li>
</ul>
<p>核心判断：<strong>这轮调整是交易层面的\"高切低\"，而非产业逻辑破坏</strong>。AI算力/半导体的基本面——资本开支高增长、HBM供不应求、光模块订单饱满——均未改变。</p>

<hr>

<h2>三、细分领域动态</h2>

<div class="sect-card">
<div class="sh">🔷 算力板块 <span class="pill pill-down">周五净流出显著</span></div>
<p class="sn"><strong>资金面：</strong>电子行业周五主力净流出372亿元居首。中芯国际主力净流出31.4亿居全市场第一。算力ETF全线下跌。</p>
<p class="sn"><strong>政策面：</strong>下周<strong>6/2-6/5 Computex大会</strong>以\"AI Together\"为主题，英伟达CEO黄仁勋将发布最新Vera Rubin架构AI芯片，是全球AI算力最强催化窗口。市场监管总局&发改委联合发布《人工智能计量体系建设指引》。</p>
<p class="sn"><strong>基本面：</strong>Cerebras在美上市首日暴涨89%市值达750亿美元，验证AI算力赛道高景气。戴尔AI服务器营收161亿美元同比+757%。四大云厂商2026年资本支出7250亿美元（+77%）。</p>
<p class="sn"><strong>情绪面：</strong>A股算力板块高位回调明显，但美股AI板块仍在创新高（纳指六连涨）。A股调整本质是<strong>内部筹码博弈和\"高切低\"</strong>的体现。</p>
</div>

<div class="sect-card">
<div class="sh">🔷 存储板块 <span class="pill pill-mid">情绪中性</span></div>
<p class="sn"><strong>资金面：</strong>周五跟随半导体整体回调。北向资金在存储龙头交投活跃（澜起科技沪股通成交42亿、兆易创新33.86亿）。佰维存储逆势上涨0.94%成为存储中少有的红盘。</p>
<p class="sn"><strong>基本面：</strong>HBM景气度持续超预期——HBM3E现货价半年暴涨超300%。三星率先交付首批12层48GB HBM4E样品，全球领先。美光警告内存短缺将持续至2026年后。全球DRAM营收Q1逼近970亿美元（+260%）。</p>
<p class="sn"><strong>情绪面：</strong>产业数据极为强劲但股价已充分反映涨价预期。中长期看HBM仍是AI产业链中<strong>供需格局最紧张</strong>的环节之一。</p>
</div>

<div class="sect-card">
<div class="sh">🔷 机器人板块 <span class="pill pill-mid">等待催化剂</span></div>
<p class="sn"><strong>资金面：</strong>延续周初的抛压态势。人形机器人板块5月虽整体反弹，但年内行情分化明显。</p>
<p class="sn"><strong>基本面：</strong>产业趋势加速——<strong>宇树科技科创板IPO于6月1日上会</strong>，冲刺A股\"人形机器人第一股\"，拟募资42.02亿元。海关数据4月工业机器人出口量突破2.5万台（同比+90%）。特斯拉Optimus Gen-3 Q2启动量产，首代目标年产能100万台。</p>
<p class="sn"><strong>情绪面：</strong>市场短期聚焦宇树科技上会结果。如果顺利过会将为板块注入强心剂。当前属于<strong>等待催化剂真空期</strong>的调整。</p>
</div>

<div class="sect-card">
<div class="sh">🔷 CPO板块 <span class="pill pill-up">通信线缆逆势走强</span></div>
<p class="sn"><strong>资金面：</strong>板块内部分化明显。光模块龙头高位震荡，但<strong>通信线缆及配套</strong>板块周五逆势净流入<strong>39.83亿元</strong>。亨通光电主力净流入<strong>39.76亿</strong>居全市场第一，剑桥科技净流入11.73亿。</p>
<p class="sn"><strong>基本面：</strong>2026年机构定义为<strong>CPO产业化元年</strong>。英伟达Q4启动CPO量产，鸿海CPO全光交换机出货目标上调至5万台以上。LightCounting预测2030年CPO市场规模达100亿美元。中际旭创Q1营收194.96亿元（+192%），净利润57.35亿元（+262%）。</p>
<p class="sn"><strong>情绪面：</strong>资金正在寻找CPO产业链的\"新面孔\"——通信线缆方向获得集中配置。下周Computex大会可能发布CPO新标准/应用方案，有望进一步提振板块情绪。</p>
</div>

<hr>

<h2>四、主流净流入板块监控（周五数据）</h2>
<table>
  <tr><th>#</th><th>板块</th><th>净流入(亿)</th><th>驱动原因</th><th>类型</th></tr>
  <tr><td><strong>1</strong></td><td>电力</td><td><span class="green">+43.08</span></td><td>防御+夏季用电高峰预期</td><td><span class="pill pill-mid">防御配置</span></td></tr>
  <tr><td><strong>2</strong></td><td>公用事业</td><td><span class="green">+41.74</span></td><td>资金从科技向防御大迁徙</td><td><span class="pill pill-mid">防御配置</span></td></tr>
  <tr><td><strong>3</strong></td><td>通信线缆及配套</td><td><span class="green">+39.83</span></td><td>CPO/算力互联延伸</td><td><span class="pill pill-up">产业驱动</span></td></tr>
  <tr><td><strong>4</strong></td><td>印制电路板</td><td><span class="green">+28.51</span></td><td>AI服务器PCB需求放量</td><td><span class="pill pill-up">业绩驱动</span></td></tr>
  <tr><td><strong>5</strong></td><td>火力发电</td><td><span class="green">+24.79</span></td><td>防御+高分红</td><td><span class="pill pill-mid">防御配置</span></td></tr>
  <tr><td><strong>6</strong></td><td>食品饮料</td><td><span class="green">+21.60</span></td><td>消费复苏+618大促预期</td><td><span class="pill pill-mid">防御配置</span></td></tr>
  <tr><td><strong>7</strong></td><td>商贸零售</td><td><span class="green">+20.22</span></td><td>端午消费旺季预期</td><td><span class="pill pill-mid">事件驱动</span></td></tr>
  <tr><td><strong>8</strong></td><td>白酒Ⅲ</td><td><span class="green">+18.43</span></td><td>贵州茅台净流入9.19亿</td><td><span class="pill pill-mid">防御配置</span></td></tr>
  <tr><td><strong>9</strong></td><td>白酒Ⅱ</td><td><span class="green">+18.43</span></td><td>消费板块资金集中涌入</td><td><span class="pill pill-mid">防御配置</span></td></tr>
  <tr><td><strong>10</strong></td><td>通信设备</td><td><span class="green">+13.13</span></td><td>CPO/5G/光通信</td><td><span class="pill pill-up">产业驱动</span></td></tr>
</table>
<p><strong>资金流向核心结论：</strong></p>
<ul>
  <li>周五全市场主力净流出<strong>831.55亿元</strong>，连续多日净流出</li>
  <li>电子行业净流出<strong>372.05亿</strong>居全行业第一</li>
  <li><strong>电力+公用事业</strong>合计净流入约85亿——资金从科技全面撤退至防御方向</li>
  <li>通信线缆是AI板块中<strong>唯一逆势吸金方向</strong>——亨通光电全市场净流入第一</li>
  <li><strong>AI板块相对热度降至冰点</strong>，但产业逻辑未变，调整后是逢低布局的机会</li>
</ul>

<hr>

<h2>五、关键异动个股</h2>
<table>
  <tr><th>个股</th><th>代码</th><th>异动</th><th>逻辑</th></tr>
  <tr><td><strong>亨通光电</strong></td><td>600487</td><td><span class="pill pill-up">主力净流入39.76亿<br>全市场第一</span></td><td>通信线缆龙头，CPO/算力互联概念延伸受益</td></tr>
  <tr><td><strong>中芯国际</strong></td><td>688981</td><td><span class="pill pill-down">主力净流出31.4亿</span></td><td>半导体龙头获利回吐，昨日创新高后周五大幅回调</td></tr>
  <tr><td><strong>博杰股份</strong></td><td>002975</td><td><span class="pill pill-up">涨停</span></td><td>切入英伟达供应链，液冷测试设备小批量发货，业绩爆发</td></tr>
  <tr><td><strong>联想集团</strong></td><td>HK.0992</td><td><span class="pill pill-up">港股暴涨22.46%</span></td><td>AI服务器财报超预期，验证全球AI硬件景气度</td></tr>
</table>

<hr>

<h2>六、特斯拉机器人概念股解析</h2>
<p>特斯拉Optimus V3于2026年Q2启动量产，核心受益标的如下：</p>

<table>
  <tr><th>环节</th><th>核心公司</th><th>代码</th><th>受益逻辑</th><th>优先级</th></tr>
  <tr><td><strong>执行器（线性）</strong></td><td>拓普集团</td><td>601689</td><td>Optimus V3线性执行器独家供应商（腿/腰大关节），单机价值约1.5万元，已签40亿+订单</td><td>⭐⭐⭐</td></tr>
  <tr><td><strong>执行器（旋转）</strong></td><td>三花智控</td><td>002050</td><td>旋转关节总成独家（14个上肢关节）+全套液冷，单机约3万元，锁定54亿订单</td><td>⭐⭐⭐</td></tr>
  <tr><td><strong>减速器</strong></td><td>绿的谐波</td><td>688017</td><td>谐波减速器国产龙头，V3单台用14-20个，唯一规模化进入特斯拉供应链</td><td>⭐⭐⭐</td></tr>
  <tr><td><strong>滚柱丝杠</strong></td><td>五洲新春</td><td>603667</td><td>行星滚柱丝杠核心供应商，V3单机34根，腿部关键传动</td><td>⭐⭐</td></tr>
  <tr><td><strong>电机（灵巧手）</strong></td><td>鸣志电器</td><td>603728</td><td>空心杯电机独家供应商，用于V3灵巧手，高功率密度</td><td>⭐⭐</td></tr>
  <tr><td><strong>伺服系统</strong></td><td>汇川技术</td><td>300124</td><td>伺服系统+运动控制方案，工业自动化延伸至机器人</td><td>⭐⭐</td></tr>
  <tr><td><strong>传感器</strong></td><td>柯力传感</td><td>603662</td><td>力矩传感器潜在供应商，国产替代空间大</td><td>⭐⭐</td></tr>
  <tr><td><strong>滚柱丝杠</strong></td><td>恒立液压</td><td>601100</td><td>滚柱丝杠供应商，V3线性关节核心部件</td><td>⭐⭐</td></tr>
</table>

<p><strong>量产进展：</strong>特斯拉加州弗里蒙特工厂已将原Model S/X生产线全面改造为Optimus专属产线，计划4个月内完成产线切换与调试，设计年产能达100万台。德州超级工厂第二代机器人产线也在规划中，预计2027年投产，长期目标年产能高达1000万台。</p>

<p><strong>操作思路：</strong>机器人板块目前处于\"产业趋势确定但业绩尚未大规模兑现\"的阶段。核心仓位建议配置<strong>执行器（拓普/三花）+减速器（绿的谐波）</strong>，卫星仓位关注传感器/电机等方向。<strong>宇树科技6/1上会</strong>若顺利过会，将为板块注入强心剂。</p>

<hr>

<h2>七、总结与展望</h2>
<div class="info-grid">
  <div class="info-item"><div class="il">📌 本周回顾</div><div class="iv" style="font-size:14px">A股先扬后抑，\"高切低\"剧烈切换。科技板块周五全面退潮，但5月全月看科创50+11%、创业板+10%，AI仍是核心主线。</div></div>
  <div class="info-item"><div class="il">👀 下周一关键催化</div><div class="iv" style="font-size:14px"><strong>1) 6/1 宇树科技上会</strong>（\"人形机器人第一股\"）<br><strong>2) 6/2-6/5 Computex大会</strong>（英伟达Vera Rubin发布、CPO/液冷等前沿方案展示）</div></div>
  <div class="info-item"><div class="il">💡 美股指引</div><div class="iv" style="font-size:14px">美股三大指数齐创新高，纳指六连涨。费城半导体+1%。Snowflake暴涨36%，英伟达/微软/亚马逊上涨。A股调整更多是<strong>内部资金博弈</strong>问题。</div></div>
  <div class="info-item"><div class="il">💡 白银展望</div><div class="iv" style="font-size:14px">COMEX白银周末报75.58美元，5月累涨2.1%。短线在72-78美元区间震荡。下周关注非农数据和美联储官员讲话。</div></div>
  <div class="info-item"><div class="il">⚠️ 风险提示</div><div class="iv" style="font-size:14px;color:#f59e0b">主力资金连续多日净流出，若Computex大会催化效果不及预期，AI板块调整时间可能延长。仓位管理是第一要务。</div></div>
  <div class="info-item"><div class="il">🧭 策略建议</div><div class="iv" style="font-size:14px">调整中<strong>逢低分批布局</strong>算力/光模块龙头。关注Computex大会英伟达Vera Rubin架构及CPO最新进展。通信线缆方向（亨通光电等）值得重点跟踪新机会。</div></div>
</div>
<blockquote>⚠️ 以上分析基于公开数据整理，不构成投资建议。股市有风险，投资需谨慎。</blockquote>
"""

entry = {
    "id": MONITOR_ID,
    "date": REPORT_DATE,
    "title": TITLE,
    "tags": TAGS,
    "summary": SUMMARY,
    "html": HTML,
}

# Read existing data
with open(MONITORS_PATH, "r", encoding="utf-8") as f:
    monitors = json.load(f)

# Append
monitors.append(entry)

# Write back
with open(MONITORS_PATH, "w", encoding="utf-8") as f:
    json.dump(monitors, f, ensure_ascii=False, indent=2)

print(f"✅ Appended entry {MONITOR_ID} to {MONITORS_PATH}")
print(f"   Total entries: {len(monitors)}")