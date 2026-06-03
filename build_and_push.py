#!/usr/bin/env python3
"""Add a new monitor entry and build+push the site."""
import json, sys, os, subprocess

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "monitors.json")

NEW_ENTRY = {
    "id": "mon-20260603-1929",
    "date": "2026-06-03 19:29",
    "title": "AI板块盘后复盘 · A股今日收盘 创业板突破4122 中际旭创超越茅台 CPO/光模块集体暴涨",
    "tags": [
        "收盘复盘",
        "A股收盘",
        "中际旭创超越茅台",
        "CPO",
        "光模块",
        "创业板新高",
        "宇树IPO过会",
        "英伟达CPO量产",
        "存储超级周期",
        "白银"
    ],
    "summary": "A股收盘三大指数齐涨，创业板+1.65%报4122点。中际旭创涨超10%超越茅台股价。CPO/光模块暴涨，天孚通信+14.5%。宇树IPO过会。HBM价格将暴涨。白银75.3美元震荡。",
    "html": """<div class="metric-row">
  <div class="metric-box"><div class="num">4083.97</div><div class="lbs">上证收盘</div></div>
  <div class="metric-box"><div class="num">+0.22%</div><div class="lbs">上证涨幅</div></div>
  <div class="metric-box"><div class="num">4122.99</div><div class="lbs">创业板指🚀</div></div>
  <div class="metric-box"><div class="num">+1.65%</div><div class="lbs">创业板涨幅</div></div>
  <div class="metric-box"><div class="num">3.13万亿</div><div class="lbs">成交额</div></div>
  <div class="metric-box"><div class="num">1600↑</div><div class="lbs">上涨家数</div></div>
  <div class="metric-box"><div class="num">75.31</div><div class="lbs">白银$</div></div>
</div>

<h1>AI板块盘后复盘 · A股收盘 创业板突破4122 CPO光模块集体暴涨</h1>
<p><strong>时间：</strong>2026-06-03 19:29（A股今日已收盘）</p>
<p><strong>⚠️ 数据口径说明：</strong>当前为A股收盘后19:29，以下为基于今日收盘数据及盘后事件的综合复盘。</p>

<div class="tagline">📌 <strong>核心基调：</strong>今日A股三大指数全线上涨，创业板指领涨+1.65%报4122.99点。AI板块核心逻辑"硬切硬"回归——算力硬件方向集体暴涨，CPO/光模块成为今日最强主线。<strong>中际旭创盘中最高1315.51元，超越贵州茅台股价</strong>，创历史性时刻！宇树科技IPO过会确认，"人形机器人第一股"正式加冕。英伟达官宣Spectrum-X硅光CPO全面量产，点燃光通信全产业链。白银回踩74美元后反弹至75.31美元。今日盘面呈极致结构性行情——AI硬件吸金超百亿，超3700只个股收跌。</div>

<hr>

<h2>📊 零、COMEX白银期货播报</h2>
<div class="info-grid">
  <div class="info-item"><div class="il">COMEX白银期货</div><div class="iv"><strong>约75.31美元/盎司</strong> <span class="pill pill-up">日内+0.07%</span></div></div>
  <div class="info-item"><div class="il">现货白银（伦敦银）</div><div class="iv"><strong>约74.98美元/盎司</strong> <span class="pill pill-up">日内+0.18%</span>（突破75关口）</div></div>
  <div class="info-item"><div class="il">沪银主力</div><div class="iv"><strong>约18,522元/千克</strong> <span class="pill pill-up">+1.42%</span></div></div>
  <div class="info-item"><div class="il">美元指数</div><div class="iv"><strong>约99.22</strong> <span class="pill pill-down">小幅走低</span></div></div>
  <div class="info-item"><div class="il">COMEX黄金期货</div><div class="iv"><strong>约4,519美元/盎司</strong> <span class="pill pill-up">+0.29%</span></div></div>
  <div class="info-item"><div class="il">美国10年期国债</div><div class="iv"><strong>4.429%</strong> <span class="pill pill-mid">高位运行</span></div></div>
</div>

<p><strong>近期趋势判断：</strong>白银今日亚盘回踩74美元后反弹，重新站稳75美元上方。日图级别延续<strong>74-76美元箱体震荡</strong>格局。COMEX白银期货收盘75.31美元，日内窄幅波动反映多空进入平衡区域。本周五美国非农数据将是短期方向催化剂，若数据弱于预期可能助推白银突破76美元。</p>

<p><strong>驱动因素简析：</strong></p>
<ul>
  <li><strong>美元指数小幅走低：</strong>美元指数报99.22，日内微跌，为以美元计价的白银提供支撑</li>
  <li><strong>中东局势升温：</strong>海湾地区局势再度紧张，科威特、巴林等地传出袭击消息，霍尔木兹海峡运输风险上升，避险情绪部分转移到贵金属</li>
  <li><strong>美联储政策博弈：</strong>美联储高利率预期升温，市场预期维持高利率更长时间，压制无息资产上方空间</li>
  <li><strong>机构预测白银缺口收窄：</strong>机构预计2026年白银市场缺口将从此前约3亿盎司大幅收窄至约6000-7000万盎司，主要因高银价导致光伏制造商削减银用量、银饰需求受抑，以及矿山供应略有增加，对银价形成一定压制</li>
  <li><strong>工业需求结构性变化：</strong>光伏"去银化"趋势初现，但AI数据中心建设维持白银工业需求，多空因素交织</li>
</ul>

<hr>

<h2>一、大盘解读</h2>

<div class="info-grid">
  <div class="info-item"><div class="il">上证指数</div><div class="iv">4083.97 <span class="pill pill-up">+0.22%</span></div></div>
  <div class="info-item"><div class="il">深证成指</div><div class="iv">15704.71 <span class="pill pill-up">+0.73%</span></div></div>
  <div class="info-item"><div class="il">创业板指</div><div class="iv"><strong>4122.99 <span class="pill pill-up">+1.65%</span> 🚀</strong></div></div>
  <div class="info-item"><div class="il">两市成交</div><div class="iv"><strong>3.13万亿元</strong>（环比小幅放量）</div></div>
  <div class="info-item"><div class="il">涨跌家数</div><div class="iv"><strong>近1600只上涨</strong> / 超3700只下跌</div></div>
  <div class="info-item"><div class="il">北向资金</div><div class="iv"><strong>延续净流入</strong>（成交4147亿，占13.25%）</div></div>
  <div class="info-item"><div class="il">主力资金</div><div class="iv"><span class="coral">净流出114.21亿元</span></div></div>
</div>

<p><strong>市场特征：</strong>今日A股呈现极致的<strong>结构性行情</strong>——指数全线收涨但超3700只个股收跌，典型"指数走强、个股普跌"格局。AI硬件产业链（CPO/光模块/算力）成为全市场唯一的核心吸金主线，资金虹吸效应显著。创业板指领涨+1.65%报4122.99点，延续强势。</p>

<p><strong>成交额：</strong>两市全天成交<strong>3.13万亿元</strong>，环比小幅放量，资金活跃度维持高位。北向资金成交4147.48亿元，占两市总成交额的13.25%，外资持续加仓科技主线标的。内资主力小幅净流出114.21亿元，呈现场内调仓特征。</p>

<p><strong>今日关键催化事件：</strong></p>
<ul>
  <li>🔥 <strong>中际旭创股价超越贵州茅台</strong>：中际旭创盘中最高达1315.51元，超越贵州茅台（1280.86元），创A股历史性里程碑</li>
  <li>🔥 <strong>英伟达宣Spectrum-X硅光CPO全面量产</strong>：6月2日官宣，专为NVIDIA Vera Rubin平台打造，能效提升5倍，AI部署效率提高130%</li>
  <li>🔥 <strong>宇树科技科创板IPO正式过会</strong>：6月1日上会，73天闪电过会，"人形机器人第一股"正式加冕</li>
  <li>🔥 <strong>TrendForce预估HBM合约价将暴涨</strong>：DRAM供应紧张持续，2027年HBM合约价有望大幅增长数倍</li>
  <li>🔥 <strong>创业板人工智能ETF创新高</strong>：创业板人工智能ETF大成(159242)盘中刷新历史新高</li>
</ul>

<hr>

<h2>二、AI板块整体市场概览</h2>

<p>今日AI板块呈现<strong>"硬切硬"强势回归</strong>——与此前两日的"硬切软"轮动截然相反，AI算力硬件（CPO/光模块/AI服务器/PCB）集体暴涨，成为全市场唯一的核心主线。天孚通信暴涨超14%，新易盛涨近9%，中际旭创涨超10%股价超越贵州茅台。</p>

<p><strong>领涨方向：算力硬件 > 光模块/CPO > 光纤光缆 > PCB > 半导体</strong></p>

<p><strong>走弱方向：</strong>AI应用/软件/传媒游戏今日回调，白酒医药震荡承压，冷门小票普遍阴跌。资金从前期爆炒的AI应用端兑现离场，重新回流硬件产业链。</p>

<p><strong>关键信号：</strong>今日的"硬切硬"行情受英伟达CPO量产+中际旭创超越茅台双重事件驱动，属于<strong>标志性事件驱动行情</strong>。中际旭创股价超越茅台在心理层面具有极强的市场象征意义——标志AI算力产业链在A股中的估值定位进入新阶段。</p>

<hr>

<h2>三、细分领域动态</h2>

<div class="sect-card">
<div class="sh">🔷 算力板块 <span class="pill pill-up">大幅上涨</span> <span class="pill pill-up">算力龙头集体爆发</span></div>
<p class="sn"><strong>资金面：</strong>算力硬件方向今日主力净流入居前。通富微电净流入<strong>30.01亿元</strong>位居全市场第一；天孚通信净流入17.19亿元；TCL科技13.62亿；豪威集团9.98亿；长川科技9.75亿；东材科技9.37亿。AI算力芯片板块全天强势，电子板块主力净流入<strong>67亿元</strong>，通信板块主力净流入<strong>64.57亿元</strong>，是今日资金流入最大的两个行业。</p>
<p class="sn"><strong>政策面：</strong>国家发改委、工信部联合发布《新一代人工智能发展规划(2026-2030)》，明确提出2030年AI核心产业规模超5万亿元，算力基础设施、大模型、AI应用为三大核心发展方向。政策重点强调算力自主可控，对AI芯片、服务器、光模块、液冷等核心硬件给予专项补贴、税收减免。政府采购优先采购国产AI芯片服务器，信创替换加速。</p>
<p class="sn"><strong>基本面：</strong>COMPUTEX 2026持续催化中——英伟达GTC台北发布RTX Spark超级芯片（面向PC，最高1 Petaflop AI算力）和Spectrum-X硅光CPO量产。全球四大云厂商资本支出合计超7000亿美元。海光信息CPU+DCU协同驱动2026Q1营收增长68%。博杰股份切入AI算力赛道绑定英伟达客户，AI服务器测试已量产。戴尔美股财报超预期，AI订单超200亿元。</p>
<p class="sn"><strong>情绪面：</strong>中际旭创超越茅台成为今日市场最大情绪引爆点，具有划时代意义。算力硬件方向资金回流强劲，市场共识高度集中。机构普遍看好6月算力产业链，国盛证券建议"重回大光"关注光模块龙头。</p>
</div>

<div class="sect-card">
<div class="sh">🔷 存储板块 <span class="pill pill-up">长期超级周期确认</span> <span class="pill pill-up">HBM合约价看好暴涨数倍</span></div>
<p class="sn"><strong>资金面：</strong>存储板块今日跟涨算力硬件方向。<strong>兆易创新</strong>获主力净流入居前；港股存储相关标的活跃。北向资金在澜起科技、兆易创新等存储龙头上交投活跃。整体存储板块今日非最核心主线，但中长期资金持续布局。</p>
<p class="sn"><strong>政策面：</strong>长鑫科技科创板IPO过会后提交注册，拟募资295亿元，国产存储扩产预期升温。国家集成电路大基金二期重点投向AI存储方向。</p>
<p class="sn"><strong>基本面（今日关键更新）：</strong><strong>TrendForce最新研究：</strong></p>
<ul>
  <li>DRAM持续供应紧张，HBM供应商议价能力增强，<strong>预计2027年HBM合约价格还将大幅上涨数倍</strong></li>
  <li>2026年HBM需求成长主力来自AI ASIC平台升级（Google TPU及各大云端业者自研芯片）</li>
  <li>单颗AI芯片搭载HBM容量将从96GB/192GB提升至216GB/288GB</li>
  <li>2027年NVIDIA Rubin Ultra平台推出，单颗GPU配置HBM容量将进一步提升至384GB</li>
  <li>HBM投片量占DRAM投片比重将由2025年的18%提升至2027年约30%</li>
  <li>HBM位供给占比将由8%提高至约13%</li>
  <li>AI相关存储需求同步增长——AI数据中心贡献2026年全球HDD出货量约18%，到2030年将超过50%</li>
  <li><strong>智能手机市场受存储挤兑：</strong>Counterpoint报告2026年全球智能手机出货量预计同比暴跌13.9%至约10.8亿部，因晶圆厂产能大规模向HBM倾斜</li>
</ul>
<p class="sn"><strong>情绪面：</strong>存储超级周期逻辑持续强化，TrendForce确认HBM4合约价将暴涨数倍，中长期确定性极高。智能手机存储短缺的"副作用"也从侧面印证了AI存储需求的极度旺盛。</p>
</div>

<div class="sect-card">
<div class="sh">🔷 机器人板块 <span class="pill pill-up">宇树IPO过会确认</span> <span class="pill pill-up">板块里程碑</span></div>
<p class="sn"><strong>资金面：</strong>机器人板块今日小幅上涨。人形机器人板块指数涨幅约0.5%。资金整体平稳，宇树IPO过会消息被市场逐步消化。阿莱德表现突出。整体板块主力净流出约10.64亿元（此数据为6月2日），今日资金面中性。</p>
<p class="sn"><strong>政策面：</strong><strong>宇树科技科创板IPO正式过会确认</strong>——6月1日上交所审议通过，73天闪电过会创科创板记录。拟募资42.02亿元，冲击A股"人形机器人第一股"。整体估值预计达420亿元。创始人王兴兴通过AB股设计合计拥有68.78%表决权。</p>
<p class="sn"><strong>基本面：</strong></p>
<ul>
  <li>宇树科技2025年全年营收16.99亿元，归母净利润2.78亿元；2026年Q1营收增速回落至68.49%，扣非净利润同比下滑52.55%（因研发与销售费用大幅攀升）</li>
  <li>宇树全球人形机器人累计销售超5600台（全球第一），四足机器人累计销超3.3万台</li>
  <li>特斯拉Optimus Gen3 7-8月启动量产，加州工厂规划年产100万台</li>
  <li>COMPUTEX 2026首次设立机器人专区</li>
  <li>MWC上海6月24-25日举办"人形机器人点球大战"赛事</li>
</ul>
<p class="sn"><strong>情绪面（分歧加大）：</strong>宇树IPO过会是里程碑事件，但市场对板块估值的分歧也在加大。有观点认为"人形机器人板块未来N年的估值大顶已经形成"——宇树上市是最后一个最大的利好，故事讲到了最高潮。浙商证券则认为<strong>6月仍是配置机器人板块好时机</strong>。板块情绪从中性偏多转向多空分歧。</p>
</div>

<div class="sect-card">
<div class="sh">🔷 CPO板块 <span class="pill pill-up"><strong>今日最强主线！</strong></span> <span class="pill pill-up">集体暴涨创历史新高</span></div>
<p class="sn"><strong>资金面：</strong>CPO/光模块今日为全市场最吸金方向。通信板块主力净流入<strong>64.57亿元</strong>（仅次于电子）。个股天孚通信主力净流入17.19亿元（全市场第二）；亨通光电7.83亿；仕佳光子7.06亿。通信ETF国泰(515880)大涨8.26%领跑全市场！"易中天"（中际旭创+新易盛+天孚通信）三剑客集体暴涨批量创历史新高。</p>
<p class="sn"><strong>政策面：</strong>工信部明确新建智算中心CPO适配比例≥60%。"xPO赋能AI数据中心光互连论坛"5月底刚在上海举行，产业共识高度统一。工信部此前已发文要求加快800G/1.6T光模块产业化进程。</p>
<p class="sn"><strong>基本面（今日最大产业催化）：</strong></p>
<ul>
  <li><strong>🔥 英伟达6月2日晚官宣：</strong>NVIDIA Spectrum-X以太网硅光技术正式全面量产。新一代交换机完全基于CPO光电一体封装构建，专门服务于NVIDIA Vera Rubin平台。能效比传统可插拔光模块网络提升5倍，AI正常运行时间提升5倍，部署速度快1.3倍</li>
  <li><strong>🔥 中际旭创：</strong>股价突破1315元超越贵州茅台！全球800G光模块市占率超42%，1.6T产品全球唯一批量供货厂商，订单排期已覆盖至2028年。自研硅光芯片良率达95%</li>
  <li><strong>🔥 行业数据：</strong>Lightcounting预测2026年以太网光模块市场增长65%。1.6T产品进入大规模交付期，订单逐季快速增长。出口均价同比增长23%，产业加速向高速率迭代</li>
  <li><strong>天孚通信</strong>暴涨14.56%创历史新高；<strong>新易盛</strong>涨8.94%；<strong>光库科技</strong>涨7.77%；<strong>联特科技</strong>涨超11%</li>
  <li><strong>长飞光纤、亨通光电</strong>等光纤光缆龙头10cm涨停，订单排至2027年</li>
  <li><strong>国盛证券：</strong>2027年光模块需求预期正加速明朗，上游缺料问题迎改善拐点，龙头产能与业绩弹性有望加速释放，建议"重回大光"</li>
</ul>
<p class="sn"><strong>情绪面：</strong>CPO板块今日情绪极度亢奋。英伟达CPO量产官宣是<strong>产业化元年最有力的催化剂</strong>。中际旭创超越茅台在心理层面极具冲击力，标志着A股"光模块信仰"达到新高度。短期需注意情绪过热后的波动风险，但产业逻辑和业绩确定性均为最强。</p>
</div>

<hr>

<h2>四、主流净流入板块监控（收盘TOP10）</h2>

<table>
  <tr><th>#</th><th>行业/板块</th><th>净流入参考</th><th>核心驱动</th><th>驱动类型</th></tr>
  <tr><td><strong>1</strong></td><td><strong>电子</strong></td><td><span class="green"><strong>+67.00亿</strong></span></td><td>AI算力/芯片/PCB全面爆发，英伟达CPO量产催化+中际旭创超越茅台</td><td><span class="pill pill-up">事件+产业</span></td></tr>
  <tr><td><strong>2</strong></td><td><strong>通信</strong></td><td><span class="green"><strong>+64.57亿</strong></span></td><td>CPO/光模块/光纤光缆暴涨，通信ETF涨超8%领跑全市场</td><td><span class="pill pill-up">事件+产业</span></td></tr>
  <tr><td><strong>3</strong></td><td><strong>有色金属</strong></td><td><span class="green"><strong>+22.81亿</strong></span></td><td>中钨高新净流入9.83亿领涨，铜锡等小金属紧跟大宗商品走高</td><td><span class="pill pill-mid">周期+涨价</span></td></tr>
  <tr><td><strong>4</strong></td><td><strong>煤炭</strong></td><td><span class="green">净流入</span></td><td>夏季用电高峰+防御配置+高分红逻辑，全天涨幅2.55%</td><td><span class="pill pill-mid">防御配置</span></td></tr>
  <tr><td><strong>5</strong></td><td>银行</td><td><span class="green">小幅流入</span></td><td>北向资金配置+高股息防御+6月调样预期</td><td><span class="pill pill-mid">防御配置</span></td></tr>
  <tr><td><strong>6</strong></td><td>半导体</td><td><span class="green">早盘净流入</span></td><td>AI算力需求拉动+国产替代</td><td><span class="pill pill-up">产业驱动</span></td></tr>
  <tr><td><strong>7</strong></td><td>电力/绿电</td><td><span class="green">小幅流入</span></td><td>AI算力用电预期+夏季用电高峰</td><td><span class="pill pill-mid">预期驱动</span></td></tr>
  <tr><td><strong>8</strong></td><td>钢铁</td><td><span class="green">小幅流入</span></td><td>顺周期+低估修复</td><td><span class="pill pill-mid">板块轮动</span></td></tr>
  <tr><td><strong>9</strong></td><td>特种线缆</td><td><span class="green">持续偏强</span></td><td>算力基建高速线缆需求+鑫宏业等震荡偏强</td><td><span class="pill pill-up">产业驱动</span></td></tr>
  <tr><td><strong>10</strong></td><td>石油石化</td><td><span class="green">小幅流入</span></td><td>能源价格高位+防御配置</td><td><span class="pill pill-mid">防御配置</span></td></tr>
</table>

<p><strong>净流出TOP：</strong><strong>电力设备</strong>主力净流出<strong>92.41亿元</strong>（全市场最大失血行业），医药生物净流出39.70亿元，计算机、传媒、建筑材料净流出居前。</p>

<p><strong>资金流向核心发现：</strong></p>
<ul>
  <li><strong>电子+通信</strong>两大行业合计净流入约<strong>130亿元</strong>，是全市场最核心的吸金方向，资金高度集中于AI硬件主线</li>
  <li><strong>AI板块在全市场中的相对热度：极高。</strong>电子和通信今日几乎吸收了所有净流入资金，AI硬件主线在全市场中的虹吸效应极为显著</li>
  <li><strong>有色金属</strong>板块受益铜锡等小金属涨价+中钨高新领涨，净流入22.81亿元，是今日第三大吸金行业</li>
  <li><strong>北向资金</strong>延续净流入，成交4147亿元占两市13.25%。沪股通TOP3：工业富联（50.22亿）、寒武纪（39.92亿）、兆易创新（36.09亿）；深股通TOP3：中际旭创（<strong>83.32亿</strong>）、立讯精密（72.05亿）、宁德时代（60.51亿）。中际旭创以83.32亿位居深股通成交第一</li>
  <li><strong>AI板块相对热度判断：🔥 极高</strong>——AI硬件方向（CPO/光模块/算力）是全市场唯一的核心主线，资金高度集中</li>
</ul>

<hr>

<h2>五、关键异动个股</h2>

<table>
  <tr><th>个股</th><th>代码</th><th>异动</th><th>逻辑</th><th>关注度</th></tr>
  <tr><td><strong>中际旭创</strong></td><td>300308</td><td><span class="pill pill-up"><strong>涨+10.38%</strong></span><br>最高1315.51元</td><td><strong>🔥 股价超越贵州茅台，历史性里程碑！</strong>全球光模块龙头，800G市占率42%，1.6T全球唯一批量供货，订单排至2028年。英伟达CPO量产核心受益</td><td>⭐⭐⭐</td></tr>
  <tr><td><strong>天孚通信</strong></td><td>300394</td><td><span class="pill pill-up"><strong>暴涨+14.56%</strong></span><br>主力净流入17.19亿</td><td>光模块/光器件龙头，CPO产业链最核心环节之一，英伟达CPO量产催化，创历史新高</td><td>⭐⭐⭐</td></tr>
  <tr><td><strong>通富微电</strong></td><td>002156</td><td><span class="pill pill-up"><strong>主力净流入30.01亿</strong></span><br>全市场第一</td><td>先进封装/半导体龙头，受益AI算力芯片封测需求暴增+国产替代加速</td><td>⭐⭐⭐</td></tr>
  <tr><td><strong>东山精密</strong></td><td>002384</td><td><span class="pill pill-up"><strong>涨停+10%（触及涨停）</strong></span><br>成交185亿</td><td>【昨日跌停→今日涨停】AI算力+业绩增长+光模块业务翻倍+全产业链布局（AI PCB+光芯片+光模块+新能源汽车），龙虎榜资金积极流入</td><td>⭐⭐⭐</td></tr>
  <tr><td><strong>长飞光纤</strong></td><td>601869</td><td><span class="pill pill-up"><strong>涨停+10%</strong></span></td><td>光纤光缆龙头，CPO/硅光技术对光纤连接需求暴增，订单排至2027年</td><td>⭐⭐</td></tr>
</table>

<hr>

<h2>六、特斯拉机器人概念股解析</h2>

<p><strong>最新进展：</strong></p>
<ul>
  <li><strong>宇树科技科创板IPO过会确认</strong>（6月1日），"人形机器人第一股"正式加冕，73天闪电过会创纪录</li>
  <li>特斯拉Optimus Gen3量产时间表明确——<strong>7-8月启动量产</strong>，加州工厂规划年产能100万台</li>
  <li>COMPUTEX 2026首次设立机器人专区，AI服务机器人/具身智能集中亮相</li>
  <li>英伟达RTX Spark芯片利好AI边缘计算/机器人控制</li>
</ul>

<table>
  <tr><th>环节</th><th>核心公司</th><th>代码</th><th>受益逻辑</th><th>优先级</th></tr>
  <tr><td><strong>执行器/总成</strong></td><td>三花智控、拓普集团</td><td>002050/601689</td><td>线性/旋转执行器核心供应商，特斯拉验证推进</td><td>⭐⭐⭐</td></tr>
  <tr><td><strong>精密减速器</strong></td><td>绿的谐波、双环传动</td><td>688017/002472</td><td>谐波减速器/RV减速器，最高壁垒环节</td><td>⭐⭐⭐</td></tr>
  <tr><td><strong>伺服电机</strong></td><td>汇川技术、卧龙电驱</td><td>300124/600580</td><td>驱控一体方案，国产电机龙头</td><td>⭐⭐</td></tr>
  <tr><td><strong>传感器</strong></td><td>柯力传感、奥比中光</td><td>603662/688322</td><td>力矩传感器/3D视觉传感器</td><td>⭐⭐</td></tr>
  <tr><td><strong>灵巧手</strong></td><td>峰岹科技</td><td>688279</td><td>电机驱动芯片，WIPO特斯拉灵巧手专利催化</td><td>⭐⭐</td></tr>
  <tr><td><strong>结构件/代工</strong></td><td>工业富联、长盈精密</td><td>601138/300115</td><td>整机代工+轻量化结构件</td><td>⭐⭐</td></tr>
  <tr><td><strong>电池/电源</strong></td><td>珠海冠宇</td><td>688772</td><td>机器人电池方案</td><td>⭐</td></tr>
</table>

<p><strong>机构策略：</strong>浙商证券指出三季度特斯拉量产前，6月是配置机器人板块好时机。但需注意市场对估值已出现分歧——有观点认为宇树上市是"人形机器人估值大顶"。宇树IPO过会为板块估值提供锚定，但2026Q1扣非净利润同比下滑52.55%需关注。</p>

<hr>

<h2>七、总结与展望</h2>

<div class="info-grid">
  <div class="info-item"><div class="il">📌 今日定性</div><div class="iv" style="font-size:14px"><strong>A股今日已收盘</strong>（19:29）。三大指数齐涨，创业板+1.65%报4122。AI板块"硬切硬"强势回归，CPO/光模块集体暴涨。<strong>中际旭创超越贵州茅台股价</strong>，创历史性里程碑。英伟达官宣CPO全面量产。宇树IPO过会。但结构性分化极致——超3700只个股收跌。</div></div>
  <div class="info-item"><div class="il">👀 今夜/明日关注</div><div class="iv" style="font-size:14px">
  <strong>1) 🌙 今夜美股AI板块表现</strong>——中际旭创超越茅台的故事能否在美股映射？英伟达/博通/AMD等走势<br>
  <strong>2) COMPUTEX 2026后续</strong>——6/2-6/5展会进行中，更多产业细节有望催化硬件方向<br>
  <strong>3) 存储板块TrendForce报告发酵</strong>——2027年HBM合约价暴涨数倍的预期可能驱动存储方向资金流入<br>
  <strong>4) 6月CPI/PPI及非农数据</strong>——本周五美国非农就业数据将是白银和黄金短期方向的重要催化剂
  </div></div>
  <div class="info-item"><div class="il">💡 次日展望</div><div class="iv" style="font-size:14px">
  <strong>1) 短期情绪大概率延续</strong>——中际旭创超越茅台的符号意义将吸引更多资金关注CPO/光模块产业链<br>
  <strong>2) 存储板块有望接力</strong>——TrendForce确认HBM合约价暴涨数倍，明日资金可能从CPO扩散至存储方向<br>
  <strong>3) 机器人板块短期催化兑现</strong>——宇树IPO过会已落地，短期需等待新的催化剂<br>
  <strong>4) 注意结构性分化风险</strong>——超3700只下跌意味着资金高度集中，一旦AI硬件方向回调，市场情绪可能迅速恶化
  </div></div>
  <div class="info-item"><div class="il">⚠️ 风险提示</div><div class="iv" style="font-size:14px;color:#f59e0b">
  ① CPO/光模块板块情绪极度亢奋，短期追高风险加大，中际旭创PE已较高；<br>
  ② A股结构性分化极致（仅AI硬件涨、其余均跌），一旦AI硬件回调可能引发连锁反应；<br>
  ③ 中际旭创超越茅台虽然振奋人心，但需注意股价不等于市值，两者市值仍有较大差距；<br>
  ④ 存储HBM合约价暴涨预期虽已明确，但实际执行存不确定性，需关注供需格局演变；<br>
  ⑤ <strong>以上分析基于公开数据整理，不构成投资建议</strong>
  </div></div>
</div>

<hr>

<blockquote>⚠️ 以上分析基于公开数据和搜索结果整理，不构成投资建议。股市有风险，投资需谨慎。<br>
📝 报告生成时间：2026-06-03 19:29 | 数据来源：公开市场信息 | 监测周期：1小时</blockquote>"""
}

# Read existing data
with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# Check for duplicate IDs
existing_ids = [entry["id"] for entry in data]
if NEW_ENTRY["id"] in existing_ids:
    print(f"ERROR: Duplicate ID {NEW_ENTRY['id']} found!")
    sys.exit(1)

# Append new entry
data.append(NEW_ENTRY)

# Write back
with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Added entry {NEW_ENTRY['id']} to monitors.json")
print(f"   Total entries: {len(data)}")

# Build and push
SITE_DIR = os.path.dirname(__file__)
result = subprocess.run(
    ["python3", "build_site.py", "--push"],
    cwd=SITE_DIR,
    capture_output=True,
    text=True,
    timeout=120
)

print(f"build_site.py return code: {result.returncode}")
if result.stdout:
    print(f"STDOUT: {result.stdout[-2000:]}")
if result.stderr:
    print(f"STDERR: {result.stderr[-2000:]}")