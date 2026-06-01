#!/usr/bin/env python3
"""Generate the 16:00 monitor entry JSON and pass to append script."""

import json, sys

entry = {
  "id": "mon-20260601-1615",
  "date": "2026-06-01 16:15",
  "title": "AI板块收盘复盘 · A股收盘 硬切软 科创50重挫5% 煤炭逆势爆发 存储超级周期获双确认",
  "tags": ["收盘复盘", "A股收盘", "高低切换", "AI应用", "存储", "CPO回调", "机器人", "白银", "煤炭"],
  "summary": "A股收盘三大指数收跌，科创50暴跌5%。AI硬件重挫CPO/算力领跌，AI应用软件接棒爆发。存储超级周期获高盛+瑞银双确认。COMEX白银75美元附近窄幅震荡。",
  "html": """<div class=\"metric-row\">
  <div class=\"metric-box\"><div class=\"num\">4057.74</div><div class=\"lbs\">上证收盘</div></div>
  <div class=\"metric-box\"><div class=\"num\">-0.27%</div><div class=\"lbs\">上证跌幅</div></div>
  <div class=\"metric-box\"><div class=\"num\">-2.15%</div><div class=\"lbs\">创业板指</div></div>
  <div class=\"metric-box\"><div class=\"num\">-5.00%</div><div class=\"lbs\">科创50💥</div></div>
  <div class=\"metric-box\"><div class=\"num\">2.89万亿</div><div class=\"lbs\">全日成交</div></div>
  <div class=\"metric-box\"><div class=\"num\">3700+</div><div class=\"lbs\">个股上涨</div></div>
</div>

<h1>AI板块收盘复盘 · A股收盘 沪指微跌 科创50暴跌5% 硬切软延续 煤炭逆势爆发</h1>
<p><strong>时间：</strong>2026-06-01 16:15（A股今日已收盘）</p>

<div class=\"tagline\">📌 <strong>核心基调：</strong>今日A股三大指数集体收跌，但全市场<strong>超3700只个股上涨</strong>，呈现典型的\"指数弱、个股强\"分化格局。科创50暴跌5%，AI硬件（CPO/PCB/半导体）大幅回调，AI应用/软件板块逆势爆发成为今日最强主线。煤炭板块因夏季用电高峰+印尼煤炭出口新政逆市大涨。宇树科技科创板IPO今日上会，冲击A股\"人形机器人第一股\"。COMPUTEX 2026开幕，黄仁勋发表主题演讲。美元指数99附近低位运行，COMEX白银在75美元附近窄幅震荡。</div>

<hr>

<h2>📊 零、COMEX白银期货播报</h2>
<div class=\"info-grid\">
  <div class=\"info-item\"><div class=\"il\">COMEX白银期货</div><div class=\"iv\"><strong>约75.2 美元/盎司</strong> <span class=\"pill pill-mid\">日内小幅震荡</span></div></div>
  <div class=\"info-item\"><div class=\"il\">伦敦银现货</div><div class=\"iv\"><strong>约74.8 美元/盎司</strong> <span class=\"pill pill-mid\">窄幅波动</span></div></div>
  <div class=\"info-item\"><div class=\"il\">沪银主力</div><div class=\"iv\"><strong>18,226 元/千克</strong> <span class=\"pill pill-up\">+0.11%</span></div></div>
  <div class=\"info-item\"><div class=\"il\">白银T+D</div><div class=\"iv\"><strong>18.28 元/克</strong> <span class=\"pill pill-mid\">窄幅波动</span></div></div>
  <div class=\"info-item\"><div class=\"il\">美元指数</div><div class=\"iv\"><strong>约99.0</strong> <span class=\"pill pill-down\">低位运行</span></div></div>
  <div class=\"info-item\"><div class=\"il\">伦敦金现货</div><div class=\"iv\"><strong>约4,539 美元/盎司</strong> <span class=\"pill pill-mid\">高位震荡</span></div></div>
</div>

<p><strong>近期趋势判断：</strong>白银当前处于<strong>74-76美元窄幅震荡</strong>区间，日内波动较小。5月白银月线连续第三个月收阴，从年初逾百美元高位持续回落。短期呈现<strong>低位筑底</strong>特征，方向选择在即。</p>

<p><strong>驱动因素简析：</strong></p>
<ul>
  <li><strong>美元指数低位运行：</strong>美元指数徘徊在99附近，贵金属计价端获得支撑</li>
  <li><strong>美联储政策预期：</strong>市场对6月降息概率不足2%，高利率环境压制无息资产配置意愿</li>
  <li><strong>工业需求支撑：</strong>光伏+AI数据中心建设对白银需求维持高位，全球白银已连续五年供给缺口</li>
  <li><strong>机构观点分歧：</strong>美国银行看多（预测Q4冲击100美元），瑞银偏谨慎（下调年底目标至80美元，关注\"去银化\"风险）</li>
  <li><strong>地缘因素：</strong>美伊战火未停但和谈进展反复，避险情绪边际降温</li>
</ul>

<hr>

<h2>一、大盘解读</h2>

<div class=\"info-grid\">
  <div class=\"info-item\"><div class=\"il\">上证指数</div><div class=\"iv\">4057.74 <span class=\"pill pill-down\">-0.27%</span></div></div>
  <div class=\"info-item\"><div class=\"il\">深证成指</div><div class=\"iv\">15340.36 <span class=\"pill pill-down\">-1.51%</span></div></div>
  <div class=\"info-item\"><div class=\"il\">创业板指</div><div class=\"iv\">3950.94 <span class=\"pill pill-down\">-2.15%</span></div></div>
  <div class=\"info-item\"><div class=\"il\">科创50</div><div class=\"iv\" style=\"color:#ef4444\"><strong>-5.00% 💥 领跌全场</strong></div></div>
  <div class=\"info-item\"><div class=\"il\">北证50</div><div class=\"iv\" style=\"color:#22c55e\"><strong>逆势上涨</strong></div></div>
  <div class=\"info-item\"><div class=\"il\">全日成交</div><div class=\"iv\"><strong>约2.89万亿元</strong></div></div>
  <div class=\"info-item\"><div class=\"il\">涨跌家数</div><div class=\"iv\" style=\"color:#22c55e\"><strong>超3700只上涨</strong> / 近1700只下跌</div></div>
</div>

<p><strong>市场特征：</strong>今日A股冲高回落，呈现经典的\"指数弱、个股强\"格局。科创50暴跌5%领跌全场，但全市场超3700只个股上涨，说明调整高度集中在权重大盘科技股（半导体/PCB/CPO等AI硬件）。中小盘股和AI应用方向表现活跃。</p>

<p><strong>成交额：</strong>全市场成交约2.89万亿元，量能保持高位。中际旭创以<strong>309.68亿元</strong>成交额居A股第一。</p>

<p><strong>今日关键催化事件：</strong></p>
<ul>
  <li>🔥 <strong>COMPUTEX 2026/GTC Taipei开幕</strong>：黄仁勋发表主题演讲，发布N1X AI PC芯片和Vera Rubin架构细节</li>
  <li>🔥 <strong>宇树科技科创板IPO今日上会</strong>：冲刺A股\"人形机器人第一股\"，拟募资42亿元</li>
  <li>🔥 <strong>英伟达发布RTX Spark超级芯片</strong>：面向Windows PC，最高1 petaflop AI算力，支持128GB统一内存</li>
  <li>🔥 <strong>四部门联合印发AI素养提升政策</strong>：网信办、教育部、工信部、人社部联合发文</li>
  <li>🔥 <strong>煤炭板块逆市爆发</strong>：夏季用电高峰+印尼煤炭出口新政策催化</li>
</ul>

<hr>

<h2>二、AI板块整体市场概览</h2>

<p>今日AI板块呈现<strong>严重的内部轮动分化</strong>——AI应用/软件方向大幅上涨接棒领涨，而AI算力硬件（PCB/CPO/光模块/半导体设备）普遍重挫。市场将这一现象归纳为\"<strong>硬切软</strong>\"逻辑延续。此前的午盘报告中已明确指出这一趋势，午后至收盘跌幅进一步加深。</p>

<p><strong>AI应用/软件方向强势：</strong></p>
<ul>
  <li><strong>软通动力</strong> 涨停 +20.01%（AI全链条战略转型，AI营收占比超50%）</li>
  <li><strong>星环科技-U</strong> 领涨超16%</li>
  <li><strong>深信服</strong> 涨超13%（AI+安全融合逻辑）</li>
  <li>软件开发行业获主力净流入超<strong>47亿元</strong>，位居申万二级行业第一</li>
  <li>天地在线3连板，掌阅科技4天2板，视觉中国、税友股份涨停</li>
</ul>

<p><strong>AI硬件/算力方向重挫：</strong></p>
<ul>
  <li><strong>东山精密</strong> 触及跌停（主力净卖出超33亿元居首）</li>
  <li><strong>澜起科技</strong> 跌7.59%，寒武纪跌4.73%</li>
  <li>CPO概念中：<strong>东田微</strong>跌14.9%，<strong>蘅东光</strong>跌13.87%，<strong>长光华芯</strong>跌13.87%</li>
  <li><strong>赛微电子</strong>跌逾11%，<strong>芯原股份</strong>跌7.22%</li>
</ul>

<hr>

<h2>三、细分领域动态</h2>

<div class=\"sect-card\">
<div class=\"sh\">🔷 算力板块 <span class=\"pill pill-down\">大幅回调</span> <span class=\"pill pill-mid\">应用/软件接棒</span></div>
<p class=\"sn\"><strong>资金面：</strong>算力硬件方向遭遇主力大幅抛售。AI芯片/PCB/半导体设备板块全天主力净流出规模巨大。东山精密遭净卖出超33亿元居全市场第一；寒武纪(-15.07亿)、澜起科技(-14.81亿)、海光信息(-12.19亿)、中芯国际(-9.73亿)净流出居前。但算力内部并非全线溃败——<strong>兆易创新</strong>获主力净买入7.88亿元居前，<strong>太极实业</strong>（+7.25亿）、<strong>华勤技术</strong>（+6.03亿）等AI服务器/存储方向仍有资金流入。AI应用方向软件开发行业主力净流入超47亿元居首，\"硬切软\"资金再平衡特征显著。</p>
<p class=\"sn\"><strong>政策面：</strong>网信办、教育部、工信部、人社部四部门联合印发《2026年提升全民数字素养与技能工作要点》，\"提升全民人工智能素养\"被列为独立重点任务，直接催化AI应用/软件方向。工信部\"人工智能+软件\"专项行动稳步推进。华为\"韬(τ)定律\"发布，提出通过先进封装、内存带宽等技术创新绕开\"卡脖子\"问题。</p>
<p class=\"sn\"><strong>基本面：</strong>产业趋势仍在加速——2026年全球半导体销售额预计超<strong>1.3万亿美元</strong>（同比+64%），北美四大云厂商资本支出合计逾<strong>7000亿美元</strong>。英伟达GTC发布N1X AI PC芯片（1 Petaflop算力），RTX Spark面向个人AI智能体时代。联想、戴尔最新财报均大超预期，AI订单储备均超200亿元。但A股高位筹码松动，市场对利好出现\"利多出尽\"反应模式。</p>
<p class=\"sn\"><strong>情绪面：</strong>算力硬件方向短期追高意愿明显下降，获利了结压力集中释放。但中长期看，AI算力资本开支高增长趋势未变。中信建投呼吁关注COMPUTEX 2026带来的产业催化。机构普遍认为调整是<strong>筹码消化而非逻辑破坏</strong>。</p>
</div>

<div class=\"sect-card\">
<div class=\"sh\">🔷 存储板块 <span class=\"pill pill-up\">超级周期获双确认</span> <span class=\"pill pill-up\">中长期最确定</span></div>
<p class=\"sn\"><strong>资金面：</strong>存储板块整体跟随大盘回调，但龙头有资金逆势布局。<strong>兆易创新</strong>主力净流入7.88亿元，成交活跃。北向资金在存储龙头上交投活跃。但板块整体受科创50暴跌拖累，澜起科技跌7.59%。</p>
<p class=\"sn\"><strong>政策面：</strong>中国信息安全测评中心与国家保密科技测评中心联合发布安全可靠测评结果公告(2026年第2号)，9款AI训练推理芯片通过评测。长鑫科技科创板IPO过会后提交注册，拟募资295亿元。</p>
<p class=\"sn\"><strong>基本面（今日最强基本面催化）：</strong>存储超级周期获<strong>高盛</strong>和<strong>瑞银</strong>双重确认——这是全市场最明确的产业信号。</p>
<ul>
  <li><strong>高盛重磅报告：</strong>由AI驱动的存储周期比市场预期更强且更持久，2027年供需紧张将比2026年更严重，供不应求持续到2028年</li>
  <li><strong>瑞银深度报告：</strong>市场严重低估智能体AI对存储产业链的拉动。存储需求从HBM扩散到DDR5、LPDDR5、SSD及NAND Flash等几乎所有品类。DRAM缺货至2028年Q2，NAND至2027年Q4</li>
  <li>三星、美光、SK海力士三家存储巨头市值均突破<strong>万亿美元</strong>大关</li>
  <li>万联证券指出，华为\"韬定律\"有望推动我国AI芯片、高带宽内存实现技术突破</li>
</ul>
<p class=\"sn\"><strong>情绪面：</strong>存储产业链景气确定性极高，市场共识持续强化。\"存储芯片产业价值已超越传统石油资源\"的观点引发广泛讨论。短期股价调整不改变中长期超级周期逻辑。瑞银强调智能体AI将成为比训练/推理更大级别的存储需求催化剂。</p>
</div>

<div class=\"sect-card\">
<div class=\"sh\">🔷 机器人板块 <span class=\"pill pill-up\">今日重大催化</span> <span class=\"pill pill-up\">情绪积极</span></div>
<p class=\"sn\"><strong>资金面：</strong>机器人ETF华夏(562500)今日成交<strong>9.03亿元</strong>，收盘报1.1元。成分股涨跌互现——<strong>新时达涨停+10.04%</strong>（领涨），派斯林+6.91%，石头科技+5.31%；奥比中光领跌。板块整体随大盘冲高回落，但宇树IPO上会提供了较强的底部支撑。</p>
<p class=\"sn\"><strong>政策面（今日最大催化）：</strong><strong>宇树科技科创板IPO今日正式上会</strong>——73天闪电过会速度，拟募资42亿元，冲击A股\"人形机器人第一股\"。宇树科技全球人形机器人累计销售超5600台。COMPUTEX 2026首次设立机器人专区。MWC上海6月24-25日将举办\"人形机器人点球大战\"赛事。</p>
<p class=\"sn\"><strong>基本面：</strong>产业面上多重催化共振——① 宇树科技具身智能体验馆亚洲首店5月31日登陆上海久光百货；② 智元机器人自研世界模型GE 2.0获World Arena冠军；③ 特斯拉Optimus Gen3将于7-8月启动量产，加州工厂规划年产100万台；④ 中信证券判断V3版设计接近定型，量产在即；⑤ 小鹏IRON机器人目标2026年底量产。浙商证券：<strong>6月是配置机器人板块好时机</strong>。</p>
<p class=\"sn\"><strong>情绪面：</strong>宇树IPO上会是今日机器人板块最大情绪催化剂。73天闪电过会体现监管对硬科技IPO的大力支持。市场对\"人形机器人第一股\"加冕预期较高。特斯拉Optimus量产预期及得州工厂动工为板块提供中长期信心。</p>
</div>

<div class=\"sect-card\">
<div class=\"sh\">🔷 CPO板块 <span class=\"pill pill-down\">今日跌幅最大</span> <span class=\"pill pill-down\">获利回吐</span></div>
<p class=\"sn\"><strong>资金面：</strong>CPO概念今日遭遇<strong>集体暴跌</strong>，为AI板块中跌幅最大的细分方向。CPO板块指数收跌<strong>4.03%</strong>。<strong>东山精密</strong>触及跌停（主力净卖出超33亿元）；<strong>东田微</strong>-14.9%，<strong>蘅东光</strong>-13.87%，<strong>长光华芯</strong>-13.87%；<strong>剑桥科技</strong>一度触及跌停。前期CPO板块5月涨幅巨大（月涨17%+），获利回吐压力集中释放。</p>
<p class=\"sn\"><strong>政策面：</strong>\"xPO赋能AI数据中心光互连论坛\"5月28日在上海举行（CPO/NPO/LPO/XPO多元路线）。台积电COUPE on Substrate（基板级CPO）5月官宣量产，CPO产业化元年正式开启。工信部此前要求新建智算中心CPO适配比例≥60%。</p>
<p class=\"sn\"><strong>基本面（产业逻辑未变）：</strong>2026年全球1.6T光模块需求约<strong>2700万只</strong>，硅光路线占比80%，硅光芯片年需求超5500万只。800G硅光方案较EML方案成本降低21%。英伟达明确2026年Q4启动CPO量产，鸿海CPO全光交换机出货目标上调至5万台以上。LightCounting预测2030年CPO市场规模达100亿美元。<strong>产业基本面未变，今日回调纯属交易层面</strong>。</p>
<p class=\"sn\"><strong>情绪面：</strong>今日CPO板块暴跌属于<strong>技术性获利回吐</strong>，产业逻辑和业绩确定性均未受损伤。此前CPO/光模块龙头股价持续创新高（中际旭创突破千元、市值超1.2万亿），短期积累了较多获利盘。值得注意的是，虽然板块暴跌，但<strong>中际旭创</strong>仍以<strong>309.68亿元</strong>成交额位居A股第一，表明市场关注度极高。回调后性价比有所改善，机构普遍认为CPO作为AI算力互联核心环节，中长期确定性最强。</p>
</div>

<hr>

<h2>四、主流净流入板块监控（收盘TOP10）</h2>

<table>
  <tr><th>#</th><th>板块/行业</th><th>净流入参考</th><th>核心驱动</th><th>驱动类型</th></tr>
  <tr><td><strong>1</strong></td><td><strong>软件开发</strong></td><td><span class=\"green\"><strong>+47亿+</strong></span></td><td>AI应用爆发+四部门AI素养政策催化+信创主线</td><td><span class=\"pill pill-up\">政策+产业</span></td></tr>
  <tr><td><strong>2</strong></td><td><strong>煤炭</strong></td><td><span class=\"green\"><strong>逆市爆发</strong></span></td><td>夏季用电高峰+印尼煤炭出口新政+防御配置</td><td><span class=\"pill pill-mid\">事件+防御</span></td></tr>
  <tr><td><strong>3</strong></td><td>AI应用/智能体</td><td><span class=\"green\"><strong>+70亿+</strong></span></td><td>AI智能体概念13股涨停+369只上涨</td><td><span class=\"pill pill-up\">产业驱动</span></td></tr>
  <tr><td><strong>4</strong></td><td>文化传媒</td><td><span class=\"green\">净流入居前</span></td><td>AI+传媒/游戏概念活跃</td><td><span class=\"pill pill-mid\">产业驱动</span></td></tr>
  <tr><td><strong>5</strong></td><td>华为概念</td><td><span class=\"green\"><strong>+76亿+</strong></span></td><td>29只涨停/678只上涨，AI PC+鸿蒙催化</td><td><span class=\"pill pill-up\">事件驱动</span></td></tr>
  <tr><td><strong>6</strong></td><td>IT服务</td><td><span class=\"green\">净流入</span></td><td>AI应用商用化提速</td><td><span class=\"pill pill-up\">产业驱动</span></td></tr>
  <tr><td><strong>7</strong></td><td>鸡肉/养殖</td><td><span class=\"green\">晓鸣+17%</span></td><td>消费板块轮动+涨价预期</td><td><span class=\"pill pill-mid\">板块轮动</span></td></tr>
  <tr><td><strong>8</strong></td><td>氟化工</td><td><span class=\"green\">巨化涨停</span></td><td>制冷剂旺季+涨价逻辑</td><td><span class=\"pill pill-mid\">产业驱动</span></td></tr>
  <tr><td><strong>9</strong></td><td>电力/绿电</td><td><span class=\"green\">盘初走强</span></td><td>AI用电+夏季用电+防御配置</td><td><span class=\"pill pill-mid\">防御+预期</span></td></tr>
  <tr><td><strong>10</strong></td><td>燃气</td><td><span class=\"green\">小幅流入</span></td><td>夏季能源需求+防御切换</td><td><span class=\"pill pill-mid\">防御配置</span></td></tr>
</table>

<p><strong>资金流向核心发现：</strong></p>
<ul>
  <li><strong>软件开发</strong>行业主力净流入超47亿元，位居申万二级行业<strong>第一</strong>，与AI硬件（电子/半导体/CPO）形成鲜明\"硬切软\"对比</li>
  <li>AI三板块（AI应用+华为+软件开发）合计净流入近<strong>200亿元</strong>，在全市场中仍占主导</li>
  <li><strong>煤炭板块</strong>今日逆市爆发——大有能源、郑州煤电、新集能源、辽宁能源等多股涨停，是今日最抢眼的非AI方向</li>
  <li><strong>电子/半导体</strong>板块主力净流出居前，成为资金\"失血\"重灾区</li>
  <li><strong>AI板块整体相对热度：中等偏高</strong>——AI应用方向充分吸金，但硬件方向大幅失血，内部分化加剧。AI板块整体在全市场中仍是核心关注方向，但\"硬件→应用\"的内部轮动十分剧烈</li>
</ul>

<hr>

<h2>五、关键异动个股</h2>

<table>
  <tr><th>个股</th><th>代码</th><th>异动</th><th>逻辑</th><th>关注度</th></tr>
  <tr><td><strong>软通动力</strong></td><td>301236</td><td><span class=\"pill pill-up\"><strong>涨停+20.01%</strong></span></td><td>AI应用龙头，AI全链条战略转型+AI营收占比超50%+定增33亿落地</td><td>⭐⭐⭐</td></tr>
  <tr><td><strong>兆易创新</strong></td><td>603986</td><td><span class=\"pill pill-up\">主力净买入+7.88亿</span><br>资金流入居前</td><td>存储芯片龙头，受益HBM超级周期+DRAM涨价+高盛/瑞银确认存储超级周期</td><td>⭐⭐⭐</td></tr>
  <tr><td><strong>东山精密</strong></td><td>002384</td><td><span class=\"pill pill-down\">触及跌停</span><br><span class=\"coral\">主力净卖出-33亿</span></td><td>CPO/PCB概念前期涨幅巨大+获利兑现+板块系统性回调，主力大幅出逃</td><td>⭐⭐⭐</td></tr>
  <tr><td><strong>新时达</strong></td><td>002527</td><td><span class=\"pill pill-up\"><strong>涨停+10.04%</strong></span></td><td>机器人概念龙头，宇树科技IPO上会催化+特斯拉Optimus量产预期</td><td>⭐⭐</td></tr>
  <tr><td><strong>风华高科</strong></td><td>000636</td><td><span class=\"pill pill-up\">主力净流入8.64亿</span><br>全市场第一</td><td>MLCC涨价周期+电子元器件景气复苏，逆势获资金大举配置</td><td>⭐⭐⭐</td></tr>
</table>

<hr>

<h2>六、特斯拉机器人概念股解析</h2>

<p><strong>最新产业进展：</strong>特斯拉Optimus Gen3量产时间表明确——2026年Q2启动产线改造，<strong>7-8月启动量产</strong>，年底前投产。加州弗里蒙特工厂Model S/X产线全面改造，规划年产能<strong>100万台</strong>。</p>

<p><strong>今日催化：</strong>宇树科技科创板IPO上会（6月1日）+ COMPUTEX 2026首次设立机器人专区 + 英伟达RTX Spark芯片发布利好AI边缘/机器人计算。</p>

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

<p><strong>机构策略观点：</strong>浙商证券指出三季度特斯拉量产前，<strong>6月是配置机器人板块好时机</strong>，建议精选特斯拉机器人供应链核心标的。中信证券认为随着机器人外观、专利等细节公开，V3版本设计接近定型。中国供应链在规模化制造上具备优势，在机器人产业化浪潮中扮演重要角色。</p>

<hr>

<h2>七、总结与展望</h2>

<div class=\"info-grid\">
  <div class=\"info-item\"><div class=\"il\">📌 今日定性</div><div class=\"iv\" style=\"font-size:14px\"><strong>A股今日已收盘</strong>（16:15）。三大指数集体收跌，科创50暴跌5%领跌全场。AI\"硬切软\"逻辑持续演绎——AI应用/软件接棒领涨（软件开发+47亿），算力硬件（CPO/PCB/半导体）大幅回调。煤炭板块逆市爆发。全市场超3700只个股上涨，呈\"指数弱、个股强\"格局。</div></div>
  <div class=\"info-item\"><div class=\"il\">👀 今日关键事件</div><div class=\"iv\" style=\"font-size:14px\">
  <strong>1) COMPUTEX 2026/GTC Taipei开幕</strong>：黄仁勋演讲发布N1X AI PC芯片<br>
  <strong>2) 宇树科技IPO上会</strong>：冲击A股\"人形机器人第一股\"<br>
  <strong>3) 高盛+瑞银双确认存储超级周期</strong>：DRAM缺货至2028年<br>
  <strong>4) 四部门印发全民AI素养政策</strong>：直催化AI应用/软件方向<br>
  <strong>5) 科创50暴跌5%</strong>：CPO/半导体/PCB大幅回调
  </div></div>
  <div class=\"info-item\"><div class=\"il\">💡 次日展望</div><div class=\"iv\" style=\"font-size:14px\">
  <strong>1) 美股映射关注</strong>：隔夜美股AI/半导体方向表现将影响A股次日情绪<br>
  <strong>2) 硬件方向可能技术性修复</strong>：今日CPO/算力跌幅较大，短线或有反弹<br>
  <strong>3) AI应用持续性考量</strong>：明日关注AI应用/软件方向能否延续强势<br>
  <strong>4) COMPUTEX后续催化</strong>：6/2-6/5展会尚在进行中，更多细节披露有望提振硬件方向<br>
  <strong>5) 存储板块中长期逻辑最强</strong>：超级周期获双确认，可逢低关注
  </div></div>
  <div class=\"info-item\"><div class=\"il\">⚠️ 风险提示</div><div class=\"iv\" style=\"font-size:14px;color:#f59e0b\">
  ① CPO/算力硬件方向主力资金大幅流出，若明日未企稳则调整可能延长<br>
  ② A股\"硬切软\"轮动速度过快，AI应用方向的持续性仍需验证<br>
  ③ 科创50暴跌5%后，科技板块整体情绪修复需要时间<br>
  ④ 6月进入财报真空期+美国通胀数据超预期风险，短期市场波动可能加大<br>
  ⑤ 以上分析基于公开数据整理，<strong>不构成投资建议</strong>
  </div></div>
</div>

<hr>

<blockquote>⚠️ 以上分析基于公开数据和搜索结果整理，不构成投资建议。股市有风险，投资需谨慎。<br>
📝 报告生成时间：2026-06-01 16:15 | 数据来源：公开市场信息 | 监测周期：1小时</blockquote>"""
}

print(json.dumps(entry, ensure_ascii=False))