#!/usr/bin/env python3
"""Add a new monitor entry to monitors.json and build site."""
import json
import os
import subprocess
import sys

SITE_DIR = "/root/.joyclaw/workspace-er-ji-shi-chang-yan-jiu-yuan-vxu6-d552a7b0dc9d-81c90a43/site"
DATA_FILE = os.path.join(SITE_DIR, "data", "monitors.json")

new_entry = {
    "id": "mon-20260611-1129",
    "date": "2026-06-11 11:29",
    "title": "AI板块实时监控 & COMEX白银播报 — 午前CPO反弹延续 半导体材料活跃 工信部政策持续发酵",
    "tags": [
        "AI板块",
        "白银",
        "实时监控",
        "CPO",
        "算力",
        "存储",
        "机器人",
        "工信部",
        "HBM"
    ],
    "summary": "A股低开震荡超4000股下跌；CPO延续反弹炬光科技20cm涨停；半导体材料走强；白银64美元企稳",
    "html": """<h1>AI板块实时监控报告 &amp; COMEX白银期货播报</h1>
<p><strong>【2026-06-11 11:29】</strong></p>
<p><strong>⚡ A股正在交易中（午前盘）</strong> — 以下为实时盘中监控</p>
<hr />

<h2>零、COMEX白银期货播报</h2>
<ul>
  <li><strong>最新价格：</strong>COMEX白银期货主力最新报约 <strong>64.24美元/盎司</strong>，日内涨<strong>+1.2%</strong>。现货白银日内涨<strong>1%</strong>报<strong>64.03美元/盎司</strong>，盘中最高触及64.35美元。现货黄金同步涨0.59%报4095.72美元/盎司。</li>
  <li><strong>日内涨跌幅：</strong>昨日（6月10日）COMEX白银跌超1%收报64.58美元，今日亚盘小幅反弹至64美元上方。沪银主力开盘报<strong>15,266元/千克</strong>（昨收15,622元），日内低开低走最低15,179元。</li>
  <li><strong>近期趋势判断：</strong>白银自5月13日近<strong>90美元/盎司</strong>历史高位持续回调至今，累计跌幅超28%，目前在<strong>63-67美元区间震荡整理</strong>。63美元为近期关键支撑，67美元为短期阻力。分析师普遍认为短期在63-67美元来回磨，中期有望回弹至70美元上方。</li>
  <li><strong>驱动因素简析：</strong>
    <ul>
      <li><strong>美元指数：</strong>重新站上100大关，对贵金属形成明显压制</li>
      <li><strong>美联储政策：</strong>美国CPI年率4.2%符合预期但核心CPI小幅回落，通胀仍偏高。市场对美联储维持高利率预期升温</li>
      <li><strong>工业需求：</strong>光伏/AI硬件用银需求维持高位，全球白银连续多年供不应求，供需缺口约<strong>6,316吨</strong></li>
      <li><strong>库存支撑：</strong>COMEX白银库存持续下降，全球主要交易所库存处于近十年低位</li>
      <li><strong>机构观点：</strong>短期震荡偏弱，但中长期受益于工业需求和供给缺口，63美元附近具有较好性价比</li>
    </ul>
  </li>
</ul>
<hr />

<h2>一、大盘解读</h2>
<ul>
  <li><strong>今日A股三大指数集体低开，盘中震荡回升：</strong>
    <ul>
      <li><strong>上证指数：</strong>开盘<strong>3979.71点</strong>（跌0.34%），盘中一度翻红现报<strong>3982.62点</strong>（跌约0.27%）</li>
      <li><strong>深证成指：</strong>开盘报<strong>14889.57点</strong>（跌0.43%）</li>
      <li><strong>创业板指：</strong>开盘报<strong>3839.19点</strong>（跌0.40%）</li>
      <li><strong>北证50：</strong>跌1.02%</li>
    </ul>
  </li>
  <li><strong>盘面特征：</strong>两市呈<strong>普跌态势</strong>，下跌个股超4000只。石油、环氧丙烷、磷化工、化肥等周期板块走强；物理AI、边缘计算、空间计算等科技概念走弱。</li>
  <li><strong>前日回顾（6月10日）：</strong>A股三大指数集体下跌——沪指跌0.74%报4027.74点，深成指跌2.21%，创业板指跌3.20%。两市成交3.10万亿元缩量。北向资金共成交4047.71亿元。隔夜美股纳指暴跌<strong>4.18%</strong>，费城半导体指数跌1.26%。</li>
  <li><strong>板块分化：</strong><strong>半导体材料板块短线冲高</strong>（康强电子涨停、江丰电子涨超16%）；有色·钨概念异动（翔鹭钨业、章源钨业涨停）；<strong>CPO板块延续反弹</strong>（炬光科技20cm涨停、烽火通信涨停）。AI应用方向继续回调（凡拓数创跌超15%）。</li>
</ul>
<hr />

<h2>二、AI板块整体市场概览</h2>
<blockquote>今日AI板块<strong>整体偏弱但结构性亮点突出</strong>。受前日美股AI板块大幅下挫（纳指跌4.18%）拖累，A股AI板块开盘承压。但<strong>CPO方向强势反弹延续</strong>（炬光科技20cm涨停，烽火通信涨停），<strong>半导体材料</strong>方向（江丰电子涨16%）同样活跃。AI应用方向继续回调。整体呈现<strong>\"硬件分化、应用回调、CPO领涨\"</strong>的格局。工信部《\"人工智能+信息通信\"创新发展实施意见》政策持续发酵，支撑AI算力基础设施中长期逻辑。</blockquote>
<hr />

<h2>三、细分领域动态</h2>

<h3>算力板块</h3>
<ul>
  <li><strong>资金面</strong> 💰：今日算力板块整体承压。前日（6月10日）芯片ETF华夏(588170)跌3.66%。但<strong>半导体材料方向逆势获资金关注</strong>（康强电子涨停、江丰电子涨16%）。科创芯片ETF南方(588890)前日获净流入<strong>4699万元</strong>，连续2天资金净流入，居同类基金首位。</li>
  <li><strong>政策面</strong> 📋：昨日（6月10日）<strong>工信部重磅发布《\"人工智能+信息通信\"创新发展实施意见（2026—2028年）》</strong>。核心内容：到2028年形成30个以上高价值典型场景，城域算力1毫秒时延圈覆盖率不低于75%。建立\"算力+数据+模型+AI应用\"一体化服务生态。加强高端光电芯片和器件研发。5月份CPI同比上涨1.2%，PPI同比上涨3.9%创2022年8月以来新高。</li>
  <li><strong>基本面</strong> 🔬：隔夜美股三大指数重挫——<strong>纳指跌4.18%</strong>。美光科技跌13.25%，ARM跌12.84%，应用材料跌9.71%。但AI产业利好不断：英伟达与SK海力士宣布建立<strong>多年期技术合作伙伴关系</strong>，联合研发下一代AI内存技术。三大存储巨头HBM4已通过英伟达认证。博通预测2026财年AI芯片销售额达560亿美元。</li>
  <li><strong>情绪面</strong> 😟：偏谨慎。隔夜美股芯片惨跌严重打击短期情绪，但<strong>工信部重磅政策</strong>为AI算力长期发展提供确定性，国产替代逻辑获持续强化。</li>
</ul>

<h3>存储板块</h3>
<ul>
  <li><strong>资金面</strong> 💰：前日（6月10日）存储芯片概念延续活跃——<strong>金太阳（GSUN.US）涨超12%</strong>，德明利、江波龙、大为股份同步上行。今日受外围美光暴跌13.25%拖累，板块短线承压。但HBM产业链整体供需格局仍然强劲。</li>
  <li><strong>政策面</strong> 📋：SK集团会长崔泰源表示先进制程、HBM堆叠及高端封装设备供给约束严重，扩产周期长，未来数年供需将保持紧平衡。黄仁勋指出新一代Vera Rubin AI服务器显著提升单台HBM用量，<strong>HBM高景气周期有望延续至2030年以后</strong>。</li>
  <li><strong>基本面</strong> 🔬：
    <ul>
      <li><strong>HBM4量产进展顺利：</strong>三大存储巨头（三星、海力士、美光）均已通过英伟达认证并开始投产</li>
      <li><strong>HBM4E带宽突破4.0TB/s：</strong>三星率先出货12层HBM4E样品（带宽3.6TB/s），SK海力士展出同规格产品标定4.0TB/s</li>
      <li><strong>HBM5原型亮相：</strong>三星在Computex 2026展示全球首款HBM5（2nm基础裸片+1c nm DRAM），预计2029-2031年推出</li>
      <li><strong>2027年合约价格上涨预期：</strong>TrendForce预计HBM合同价格将大幅上涨，HBM盈利能力正在超越传统DRAM</li>
    </ul>
  </li>
  <li><strong>情绪面</strong> 😐：中长期极度乐观，HBM从周期股向成长股切换逻辑持续强化。美光暴跌13.25%为短线情绪冲击，但不改产业趋势。回调或是中长期布局窗口。</li>
</ul>

<h3>机器人板块</h3>
<ul>
  <li><strong>资金面</strong> 💰：前日（6月9日）机器人概念反复活跃——<strong>埃斯顿2连板</strong>，晋拓股份涨停，景业智能、腾亚精工、丰光精密涨超10%。今日板块随大盘整体承压，但<strong>机器人ETF华夏(562500)</strong>近3日合计\"吸金\"<strong>7.30亿元</strong>，日均净流入2.43亿元，连续3天资金净流入。</li>
  <li><strong>政策面</strong> 📋：<strong>工信部与国资委联合印发《2026年度人形机器人与具身智能实景实训专项行动》</strong>。三大量化目标：人形机器人在代表性场景开启\"作业模式\"；凝练形成<strong>百个以上高价值应用场景</strong>；<strong>带动形成万台级规模落地能力</strong>。重点面向生产制造、医疗康养、应急救援等场景。</li>
  <li><strong>基本面</strong> 🔬：
    <ul>
      <li><strong>\"天工3.0\"量产时间表：</strong>北京人形机器人创新中心与地瓜机器人宣布，全尺寸通用人形机器人天工3.0搭载地瓜旭日S600芯片，确定<strong>2026年下半年开启规模化量产交付</strong></li>
      <li><strong>Anthropic发布Claude Fable 5：</strong>6月9日发布，被誉为\"神话级\"模型，在软件工程、视觉处理等领域创下新纪录。进一步推动AI Agent和机器人智能化应用</li>
      <li><strong>明略科技-W：</strong>今日港股明略科技-W领涨<strong>12.75%</strong>，AI+企业服务方向获资金关注</li>
    </ul>
  </li>
  <li><strong>情绪面</strong> 😊：中长期乐观。\"万台级\"量化目标+天工3.0量产时间表+机器人ETF连续3日吸金7.3亿，显示机构资金高度认可。2026年为人形机器人量产元年判断延续。</li>
</ul>

<h3>CPO板块</h3>
<ul>
  <li><strong>资金面</strong> 💰：今日<strong>CPO板块延续强势反弹！</strong><strong>炬光科技20cm涨停</strong>，烽火通信涨停，太辰光涨7.41%，光库科技涨4.91%。通信ETF华夏(515050)盘中换手3.67%，成交<strong>6.26亿元</strong>。近6天获得连续资金净流入，合计\"吸金\"<strong>18.96亿元</strong>，日均净流入3.16亿元。资金持续布局CPO/光通信方向。</li>
  <li><strong>政策面</strong> 📋：工信部《\"人工智能+信息通信\"创新发展实施意见》明确<strong>加强高速光电芯片、光电共封装（CPO）器件等技术和产品研发验证</strong>，开展光电混合组网技术试验。加强智算超节点光电互联技术攻关。政策层面强力支持CPO技术发展。</li>
  <li><strong>基本面</strong> 🔬：
    <ul>
      <li><strong>2026年CPO产业化元年确认：</strong>英伟达官宣Spectrum-X硅光CPO交换机全面量产，2026年Q4规模化商用</li>
      <li><strong>台积电COUPE平台：</strong>预计2026年正式量产，推动CPO从0到1</li>
      <li><strong>硅光模块市占率首超50%：</strong>LightCounting报告指出，2026年基于硅光的光模块销售额首次超过整体市场的50%</li>
      <li><strong>1.6T光模块放量元年：</strong>出货量较2025年约10倍增长，毛利率可达45%-60%</li>
      <li><strong>新易盛筹划港股上市：</strong>6月10日晚公告筹划发行H股并在港交所上市，进一步提升国际竞争力</li>
    </ul>
  </li>
  <li><strong>情绪面</strong> 😊：<strong>乐观</strong>。今日CPO延续反弹，炬光科技20cm涨停+烽火通信涨停显示资金认可度极高。2026年1.6T+CPO双轮驱动，产业趋势确定性极强。新易盛筹划H股上市进一步提振信心。</li>
</ul>
<hr />

<h2>四、主流净流入板块监控</h2>

<h3>今日盘中（6月11日午前）板块表现</h3>
<ul>
  <li><strong>领涨方向：</strong>
    <ol>
      <li><strong>⚡ 石油/油气开采</strong> — 科力股份涨超10%，通源石油、中曼石油跟涨。地缘政治（美伊局势）紧张推动油价上行，WTI原油维持92美元/桶附近</li>
      <li><strong>⚡ 环氧丙烷/磷化工</strong> — 中化国际一字涨停，红宝丽、滨化股份跟涨。化工周期板块受PPI同比+3.9%创新高催化</li>
      <li><strong>⚡ CPO/光模块</strong> — <strong>炬光科技20cm涨停</strong>，烽火通信涨停，太辰光涨7.41%。工信部政策+英伟达量产双重催化</li>
      <li><strong>⚡ 半导体材料</strong> — 康强电子涨停，江丰电子涨超16%。国产替代+半导体材料需求扩张</li>
      <li><strong>⚡ 有色·钨/小金属</strong> — 翔鹭钨业、章源钨业涨停。战略金属资源受关注</li>
    </ol>
  </li>
  <li><strong>前日（6月10日）主力资金净买入TOP10个股（10:40数据）：</strong>
    <ol>
      <li><strong>烽火通信</strong> — <strong>20.59亿元</strong>（DCI+CPO，通信龙头）</li>
      <li><strong>章源钨业</strong> — 9.61亿元（有色·钨）</li>
      <li><strong>云南锗业</strong> — 5.63亿元（小金属）</li>
      <li><strong>风华高科</strong> — 4.82亿元（被动元件）</li>
      <li><strong>太辰光</strong> — 4.40亿元（光模块/CPO）</li>
      <li><strong>天孚通信</strong> — 4.05亿元（光器件/OCS）</li>
      <li><strong>永鼎股份</strong> — 3.93亿元（光纤光缆）</li>
      <li><strong>北方华创</strong> — 3.82亿元（半导体设备）</li>
      <li><strong>南大光电</strong> — 3.66亿元（半导体材料）</li>
      <li><strong>翔鹭钨业</strong> — 3.63亿元（小金属）</li>
    </ol>
  </li>
  <li><strong>前日主力资金流出前列：</strong><strong>寒武纪</strong>（-9.52亿元）、<strong>亨通光电</strong>（-9.16亿元）、<strong>中际旭创</strong>（-8.27亿元）——CPO/算力龙头短线获利了结。</li>
</ul>

<p><strong>AI板块相对热度：</strong> 🟡 <strong>中等偏弱但结构性机会突出</strong>。今日大盘普跌超4000只，AI板块整体承压。但<strong>CPO方向延续强势反弹</strong>（炬光科技20cm涨停）和<strong>半导体材料</strong>的逆势上涨表明资金仍在AI产业链内部轮动。资金从前期涨幅大的AI应用（凡拓数创跌超15%）向前期调整充分的CPO/半导体材料方向流动，\"高切低\"特征明显。通信ETF华夏近6日净流入18.96亿元，CPO方向为近期资金持续布局的重点领域。</p>
<hr />

<h2>五、关键异动个股</h2>
<ol>
  <li><strong>炬光科技（688167）⬆ 20cm涨停</strong> — CPO板块强势反弹龙头。工信部政策明确支持光电共封装器件研发验证+英伟达CPO交换机量产，公司为CPO核心光芯片/器件供应商，今日获资金强力追捧。</li>
  <li><strong>烽火通信（600498）⬆ 涨停（获主力净流入20.59亿元居两市首位）</strong> — DCI+光纤通信龙头。CPO/光互连方向持续获资金关注，公司光纤通信产品线在AI数据中心互联需求爆发背景下订单饱满。</li>
  <li><strong>凡拓数创（301313）⬇ 跌超15%</strong> — AI应用板块龙头大幅回调。此前受英伟达Cosmos 3物理AI模型发布催化大涨，今日随板块整体回调，高位获利了结压力集中释放。AI应用方向短期情绪明显降温。</li>
</ol>
<hr />

<h2>六、特斯拉机器人概念股解析</h2>
<ul>
  <li><strong>Optimus量产进展：</strong> V3设计接近定型，预计<strong>2026年7-8月启动规模化量产</strong>。弗里蒙特工厂设计年产能<strong>100万台</strong>。工信部\"万台级\"量化目标与特斯拉量产时间线形成共振。</li>
  <li><strong>\"天工3.0\"量产：</strong> 北京人形机器人创新中心与地瓜机器人联合确定2026年下半年开启规模化量产交付。搭载国产地瓜旭日S600芯片，体现国产替代趋势。</li>
  <li><strong>A股受益标的（按环节）：</strong>
    <ul>
      <li><strong>减速器：</strong>绿的谐波（谐波减速器龙头，6月5日20CM涨停创新高）、中大力德、双环传动</li>
      <li><strong>执行器：</strong>拓普集团（中信重点推票）、三花智控、肇民科技</li>
      <li><strong>电机：</strong>汇川技术、鸣志电器（空心杯电机受益）、兆威机电</li>
      <li><strong>传感器：</strong>奥比中光（3D视觉传感器）、禾川科技</li>
      <li><strong>整机/集成：</strong>埃斯顿（6月9日2连板）、中控技术、昊志机电</li>
      <li><strong>灵巧手/结构件：</strong>斯菱智驱、北特科技、丰光精密</li>
    </ul>
  </li>
  <li><strong>近期催化密集：</strong> ①工信部/国资委\"万台级\"量化目标（6月8日）；②\"天工3.0\"量产时间表（6月8日）；③Anthropic发布Claude Fable 5（6月9日）；④机器人ETF连续3日净流入7.3亿元（截至6月10日）。2026年为人形机器人<strong>量产元年</strong>判断持续强化。</li>
</ul>
<hr />

<h2>七、总结与展望</h2>

<h3>当前市场总结</h3>
<ol>
  <li><strong>📉 A股低开震荡，超4000只个股下跌：</strong> 受隔夜美股纳指暴跌4.18%+费城半导体跌1.26%情绪传导，三大指数全线低开。沪指开3979点（跌0.34%），盘中震荡回升但做多情绪偏弱。</li>
  <li><strong>🟢 CPO延续强势反弹：</strong> 炬光科技20cm涨停+烽火通信涨停+通信ETF近6日净流入18.96亿元。工信部《AI+信息通信》政策明确支持CPO/光电互联技术，CPO方向为当前AI板块最强主线。</li>
  <li><strong>🧪 半导体材料获资金关注：</strong> 江丰电子涨16%+康强电子涨停。前期调整充分的半导体材料方向获\"高切低\"资金青睐。</li>
  <li><strong>🤖 机器人板块中长期逻辑持续强化：</strong> 机器人ETF近3日净流入7.3亿元+工信部/国资委万台级目标+\"天工3.0\"2026下半年量产。产业链进入订单兑现期。</li>
  <li><strong>💾 HBM产业链高景气延续：</strong> 三大巨头HBM4认证通过+HBM4E带宽突破4.0TB/s+新易盛筹划H股上市。存储/CPO/AI芯片三线并行。</li>
  <li><strong>🥈 白银64美元企稳：</strong> 经历5月以来超28%的回调后，白银在63美元附近获得支撑，短线64美元附近震荡整理。中长期供需缺口+工业需求提供支撑。</li>
</ol>

<h3>下午盘展望</h3>
<ul>
  <li><strong>CPO/光模块方向：</strong> 今日炬光科技20cm涨停+烽火通信涨停，预计下午有望继续扩散。关注太辰光、天孚通信、光库科技等能否跟涨。</li>
  <li><strong>算力芯片：</strong> 隔夜美股芯片大跌（美光-13.25%、ARM-12.84%），短期A股芯片承压。但<strong>国产替代+工信部政策双驱动</strong>提供韧性，\"外围跌=国产替代加速\"叙事获市场认同。</li>
  <li><strong>AI应用：</strong> 凡拓数创暴跌超15%，高位获利了结仍在继续。建议短期回避涨幅过大的AI应用标的。</li>
  <li><strong>机器人：</strong> 政策利好+ETF持续净流入，但短期涨幅已大，今日随大盘调整。关注下午是否企稳。</li>
  <li><strong>整体：</strong> 关注A股下午能否在低开后收窄跌幅。沪指3980点附近为短期支撑。若下午资金回流科技方向，有望形成\"低开震荡\"格局。</li>
</ul>

<blockquote>⚠️ <strong>风险提示：</strong> 以上内容为市场信息汇总整理，不构成任何投资建议。隔夜美股科技股暴跌影响可能持续发酵。AI应用方向\"高切低\"风险较大，追高需谨慎。CPO板块短期涨幅已大，注意高位震荡风险。投资有风险，决策需谨慎。</blockquote>

<p><strong>数据来源：