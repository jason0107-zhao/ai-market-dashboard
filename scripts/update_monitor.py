#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

html_content = """<div class="metric-row">
  <div class="metric-box"><div class="num">74.38</div><div class="lbs">COMEX白银</div></div>
  <div class="metric-box"><div class="num">-1.56%</div><div class="lbs">日内跌幅</div></div>
  <div class="metric-box"><div class="num">74.105</div><div class="lbs">日内最低</div></div>
  <div class="metric-box"><div class="num">75.625</div><div class="lbs">日内最高</div></div>
  <div class="metric-box"><div class="num">75.44</div><div class="lbs">昨收</div></div>
  <div class="metric-box"><div class="num">6.76</div><div class="lbs">美元/人民币</div></div>
</div>

<h1>AI板块盘前复盘 &middot; A股昨日已收盘 聚焦CPO爆发+英伟达量产 COMPUTEX 2026进行中</h1>
<p><strong>时间：</strong>2026-06-04 06:29（北京时间 盘前）</p>

<div class="tagline"><p><strong>核心基调：</strong>A股昨日（6月3日）已收盘&mdash;&mdash;三大指数收涨但近4000只个股下跌，呈现极度结构性行情。光模块CPO产业链全面爆发，<strong>英伟达Spectrum-X硅光CPO交换机量产</strong>催化，中际旭创盘中股价超越贵州茅台（A股第四高价股）。半导体+通信设备双百亿净流入领跑全场。晚间COMEX白银期货跌至74.38美元/盎司（-1.56%）。今日关注COMPUTEX 2026后续消息及美国ADP就业数据。</p></div>

<hr>

<h2>📊 零、COMEX白银期货播报</h2>
<div class="info-grid">
  <div class="info-item"><div class="il">COMEX白银期货（最新）</div><div class="iv"><strong>74.38 美元/盎司</strong> <span class="pill pill-down">日内-1.56%</span></div></div>
  <div class="info-item"><div class="il">现货白银（伦敦银）</div><div class="iv"><strong>约74.3 美元</strong> <span class="pill pill-down">日内-0.96%</span></div></div>
  <div class="info-item"><div class="il">沪银主力（昨日日盘）</div><div class="iv"><strong>约18,522元/千克</strong> <span class="pill pill-up">+1.42%</span></div></div>
  <div class="info-item"><div class="il">日内最低/最高</div><div class="iv">74.105 / 75.625</div></div>
  <div class="info-item"><div class="il">美元指数</div><div class="iv"><strong>约99.0</strong> <span class="pill pill-down">低位运行</span></div></div>
</div>

<p><strong>近期趋势判断：</strong>白银隔夜跌至74.38美元，日内最低探至74.10美元。从5月中旬的90美元高位回落以来，白银已在此位置盘整多日。自2025年10月以来，COMEX白银库存已腰斩，实物层面存在结构性供需矛盾。当前74美元附近为关键支撑位，若能站稳则有望反弹，若跌破则下看72-73美元。</p>

<p><strong>驱动因素简析：</strong></p>
<ul>
  <li><strong>美元指数低位运行：</strong>美元指数徘徊于99附近低位，对贵金属计价端形成支撑</li>
  <li><strong>美联储政策预期：</strong>市场关注本周五非农就业数据，鲍威尔言论显示6月维持利率不变概率达98.3%</li>
  <li><strong>工业需求支撑：</strong>光伏+AI数据中心建设对白银需求维持高位，全球白银已连续五年供给缺口</li>
  <li><strong>机构观点分歧：</strong>美国银行看多（Q4冲击100美元）；瑞银下调目标至80美元，关注&quot;去银化&quot;风险</li>
</ul>

<blockquote><p><strong>白银整体偏弱</strong>，但74美元下方有较强的工业需求支撑，预计短期内维持74-77美元区间震荡。中长期看，全球白银供需缺口和AI数据中心工业需求逻辑不变。</p></blockquote>

<hr>

<h2>一、AI板块整体市场概览</h2>

<p>昨日（6月3日）A股已收盘。三大指数集体收涨但结构性极度分化&mdash;&mdash;<strong>上涨个股不足1600家，超3700只下跌</strong>，呈&quot;指数强、个股弱&quot;格局。AI板块方面，<strong>科技硬件全面回归</strong>，与6月1日的&quot;硬切软&quot;形成鲜明对比。<strong>半导体+通信设备双百亿净流入</strong>领跑全市场。核心催化来自英伟达Spectrum-X硅光CPO交换机全面量产，叠加1.6T光模块需求预期加速明朗，CPO/光模块产业链成为当日最强主线。</p>

<p><strong>昨日AI板块关键数据：</strong></p>
<ul>
  <li><strong>上证指数</strong> 4083.97点 <span class="pill pill-up">+0.22%</span>，深证成指 +0.73%，创业板指 <strong>+1.65%</strong> 创历史新高</li>
  <li><strong>两市成交</strong> 3.13万亿元，较前日小幅放量</li>
  <li><strong>光模块(CPO)指数</strong>涨超5%，&quot;易中天&quot;三剑客齐创历史新高</li>
  <li><strong>半导体板块</strong>主力净流入<strong>87.18亿元（全行业第一）</strong>，通信设备+67.72亿（第二）</li>
  <li><strong>北向资金</strong> 成交4147.48亿元（占两市13.25%），中际旭创深股通成交83.32亿居首</li>
</ul>

<hr>

<h2>二、细分领域动态</h2>

<div class="sect-card">
<div class="sh">🔷 算力板块 <span class="pill pill-up">全面走强</span> <span class="pill pill-up">半导体获87亿净流入</span></div>
<p class="sn"><strong>资金面：</strong>半导体板块全天主力净流入<strong>87.18亿元</strong>（居全行业第一），通信设备净流入67.72亿元（居第二）。个股方面：<strong>通富微电</strong>净流入30.01亿（全市场个股第一）、<strong>寒武纪</strong>净流入14.09亿。</p>
<p class="sn"><strong>政策面：</strong>国家发改委、工信部联合发布《新一代人工智能发展规划(2026-2030)》，提出2030年AI核心产业规模超5万亿元。算力自主可控为重点方向，AI芯片、服务器、光模块等给予专项补贴，单项目最高5000万元。</p>
<p class="sn"><strong>基本面：</strong>英伟达Vera Rubin平台全面量产，生成token速度大幅提升。英伟达RTX Spark超级芯片发布。东山精密2026Q1归母净利润增143.47%，光模块业务收入翻倍。</p>
<p class="sn"><strong>情绪面：</strong>算力方向情绪全线回暖。COMPUTEX 2026开幕后产业催化剂密集，市场开始转向&quot;2027年光模块需求预期加速明朗&quot;的远期叙事，情绪积极偏乐观。</p>
</div>

<div class="sect-card">
<div class="sh">🔷 存储板块 <span class="pill pill-up">HBM4E全球首发</span> <span class="pill pill-up">超级周期持续</span></div>
<p class="sn"><strong>资金面：</strong>存储板块延续活跃。<strong>兆易创新</strong>主力净流入11.09亿元。北向资金在存储龙头上交投活跃。</p>
<p class="sn"><strong>基本面（重大里程碑）：</strong>三星电子6月2日向核心客户交付全球首批<strong>HBM4E</strong>高带宽内存样品，单堆叠容量16GB，数据带宽超1.5TB/s（较HBM3E提升约50%）。三星同时全球首秀<strong>HBM5原型</strong>。SK海力士计划五年内将晶圆产能翻番，存储芯片产能瓶颈持续至2030年。</p>
<p class="sn"><strong>情绪面：</strong>HBM4E全球首发+SK海力士扩产+三星HBM5原型展示三重催化，存储&quot;超级周期&quot;情绪强化。机构普遍看好HBM从HBM3向HBM4切换为国产HBM产业链提供的国产替代机遇。</p>
</div>

<div class="sect-card">
<div class="sh">🔷 机器人板块 <span class="pill pill-up">震荡整理</span> <span class="pill pill-mid">高位整固</span></div>
<p class="sn"><strong>资金面：</strong>人形机器人板块昨日小幅波动，主力资金净流出约10.64亿元，呈高位整理态势。</p>
<p class="sn"><strong>政策面：</strong>宇树科技科创板IPO于6月1日闪电过会（73天创新纪录），&quot;人形机器人第一股&quot;即将登陆A股。国家发改委等四部门印发《2026年提升全民数字素养与技能工作要点》。</p>
<p class="sn"><strong>基本面：</strong>宇树科技2025年营收16.99亿、净利2.78亿，人形机器人出货超5600台（全球第一）。特斯拉Optimus Gen3量产节点明确：7-8月正式量产。COMPUTEX 2026首次设立机器人专区。</p>
<p class="sn"><strong>情绪面：</strong>机器人板块昨日情绪偏中性。宇树IPO过会余热尚在，但短线缺乏新催化剂。中长期看，特斯拉Optimus量产在即、宇树上市在即，6月仍是机器人板块的关注窗口。</p>
</div>

<div class="sect-card">
<div class="sh">🔷 CPO板块 <span class="pill pill-up"><strong>昨日最强主线</strong></span> <span class="pill pill-up">全面爆发</span></div>
<p class="sn"><strong>资金面：</strong>CPO板块昨日<strong>全线暴涨</strong>，为全天最强主线。<strong>通信设备板块</strong>主力净流入<strong>67.72亿元</strong>（全行业第二）。个股：<strong>天孚通信</strong>净流入17.19亿、<strong>亨通光电</strong>净流入7.83亿。中际旭创成交量超263亿居A股前列。</p>
<p class="sn"><strong>基本面（最强催化）：</strong></p>
<ul>
  <li><strong>&#x1f525; 英伟达宣布Spectrum-X硅光CPO交换机全面量产</strong>&mdash;&mdash;全球首款基于光电一体封装技术(CPO)的以太网交换机。能效较传统方案提升<strong>5倍</strong>，AI部署效率提高130%，明确2026年Q4启动CPO规模化商用。</li>
  <li><strong>&#x1f525; 中际旭创盘中股价超越贵州茅台</strong>&mdash;&mdash;股价站上1320元/股，1.6T光模块全球唯一批量供货，订单排期覆盖至2028年</li>
  <li>Lightcounting预测2026年以太网光模块市场增长65%，1.6T产品进入大规模交付期</li>
  <li><strong>亨通光电两连板</strong>、长飞光纤涨停、源杰科技涨18%</li>
</ul>
<p class="sn"><strong>情绪面：</strong>CPO板块情绪极度乐观。英伟达CPO量产是行业重大里程碑，标志CPO从概念走向AI数据中心标配。&quot;易中天&quot;（中际旭创、天孚通信、新易盛）三剑客齐创历史新高。但需注意短线涨幅过大后的获利回吐压力。</p>
</div>

<hr>

<h2>三、主流净流入板块监控（昨日收盘TOP10）</h2>

<table>
  <tr><th>#</th><th>板块/行业</th><th>主力净流入</th><th>核心驱动</th><th>驱动类型</th></tr>
  <tr><td><strong>1</strong></td><td><strong>半导体</strong></td><td><span class="green"><strong>+87.18亿</strong></span></td><td>英伟达CPO量产+AI算力需求+涨价周期</td><td><span class="pill pill-up">产业+事件驱动</span></td></tr>
  <tr><td><strong>2</strong></td><td><strong>通信设备</strong></td><td><span class="green"><strong>+67.72亿</strong></span></td><td>CPO全面量产+1.6T光模块爆发</td><td><span class="pill pill-up">事件驱动</span></td></tr>
  <tr><td><strong>3</strong></td><td><strong>电子</strong></td><td><span class="green"><strong>+67.00亿</strong></span></td><td>AI硬件产业链全面走强</td><td><span class="pill pill-up">产业驱动</span></td></tr>
  <tr><td><strong>4</strong></td><td><strong>有色金属</strong></td><td><span class="green"><strong>+22.81亿</strong></span></td><td>稀土/小金属涨价</td><td><span class="pill pill-mid">涨价驱动</span></td></tr>
  <tr><td><strong>5</strong></td><td>煤炭</td><td><span class="green">净流入</span></td><td>夏季用电高峰+防御配置</td><td><span class="pill pill-mid">防御+预期</span></td></tr>
  <tr><td><strong>6</strong></td><td>小金属</td><td><span class="green">净流入</span></td><td>稀土管理条例预期</td><td><span class="pill pill-mid">政策驱动</span></td></tr>
  <tr><td><strong>7</strong></td><td>光纤光缆</td><td><span class="green">净流入</span></td><td>CPO光纤需求爆发</td><td><span class="pill pill-up">事件驱动</span></td></tr>
  <tr><td><strong>8</strong></td><td>消费电子</td><td><span class="green">获资金增配</span></td><td>AI PC+苹果产业链复苏</td><td><span class="pill pill-mid">产业驱动</span></td></tr>
  <tr><td><strong>9</strong></td><td>电力</td><td><span class="green">小幅流入</span></td><td>AI用电+防御配置</td><td><span class="pill pill-mid">防御配置</span></td></tr>
  <tr><td><strong>10</strong></td><td>银行</td><td><span class="green">小幅流入</span></td><td>高股息防御配置</td><td><span class="pill pill-mid">防御配置</span></td></tr>
</table>

<p><strong>资金流出TOP板块：</strong></p>
<ul>
  <li>电力设备（全天净流出<strong>-92.41亿</strong>，全市场第一失血行业）</li>
  <li>医药生物（净流出<strong>-39.70亿</strong>）</li>
  <li>计算机（净流出<strong>-27.10亿</strong>，AI应用资金回吐）</li>
</ul>

<p><strong>资金流向核心发现：</strong></p>
<ul>
  <li><strong>半导体+通信设备+电子</strong>三大科技硬件板块合计净流入超<strong>221亿元</strong>，&quot;科技硬件回归&quot;特征极其鲜明</li>
  <li><strong>AI板块相对热度：极高</strong>&mdash;&mdash;半导体获87亿净流入（全行业第一），通信设备获68亿净流入（第二），AI硬件方向在全市场资金占比接近<strong>70%</strong></li>
  <li><strong>北向资金</strong>延续净流入，外资持续加仓科技主线标的（中际旭创深股通成交83.32亿居首）</li>
  <li>全市场净流出114亿背景下，科技硬件逆势大幅吸金，显示场内资金在高度聚焦AI硬件主线</li>
</ul>

<hr>

<h2>四、关键异动个股</h2>

<table>
  <tr><th>个股</th><th>代码</th><th>异动</th><th>逻辑</th><th>关注度</th></tr>
  <tr><td><strong>中际旭创</strong></td><td>300308</td><td><span class="pill pill-up">涨超10%</span><br>盘中股价<strong>首超茅台</strong>（1320元/股）</td><td>英伟达CPO量产核心受益+1.6T全球唯一批量供货+订单排期至2028年</td><td>&#x2b50;&#x2b50;&#x2b50;</td></tr>
  <tr><td><strong>通富微电</strong></td><td>002156</td><td><span class="pill pill-up">涨停</span><br>主力净流入<strong>30.01亿</strong></td><td>先进封装龙头+AMD供应链+受益AI芯片封装需求爆发</td><td>&#x2b50;&#x2b50;&#x2b50;</td></tr>
  <tr><td><strong>天孚通信</strong></td><td>300394</td><td><span class="pill pill-up">涨超14%</span><br>主力净流入17.19亿</td><td>光模块核心器件龙头+CPO产业链+英伟达Spectrum-X量产直接受益</td><td>&#x2b50;&#x2b50;&#x2b50;</td></tr>
</table>

<hr>

<h2>五、特斯拉机器人概念股解析</h2>

<p><strong>最新产业进展：</strong></p>
<ul>
  <li>特斯拉Optimus Gen3量产时间表：2026年Q2产线改造，<strong>7-8月正式启动量产</strong>，加州工厂年产能规划100万台</li>
  <li>宇树科技科创板6月1日过会，拟募资42亿元，冲击&quot;人形机器人第一股&quot;</li>
  <li>COMPUTEX 2026首次设立机器人专区，AI服务机器人/具身智能集中展示</li>
</ul>

<table>
  <tr><th>环节</th><th>核心公司</th><th>代码</th><th>受益逻辑</th><th>优先级</th></tr>
  <tr><td><strong>执行器/总成</strong></td><td>三花智控、拓普集团</td><td>002050/601689</td><td>线性/旋转执行器核心供应商，特斯拉验证推进</td><td>&#x2b50;&#x2b50;&#x2b50;</td></tr>
  <tr><td><strong>精密减速器</strong></td><td>绿的谐波、双环传动</td><td>688017/002472</td><td>谐波减速器/RV减速器，最高壁垒环节</td><td>&#x2b50;&#x2b50;&#x2b50;</td></tr>
  <tr><td><strong>伺服电机</strong></td><td>汇川技术、卧龙电驱</td><td>300124/600580</td><td>驱控一体方案，国产电机龙头</td><td>&#x2b50;&#x2b50;</td></tr>
  <tr><td><strong>传感器</strong></td><td>柯力传感、奥比中光</td><td>603662/688322</td><td>力矩传感器/3D视觉传感器</td><td>&#x2b50;&#x2b50;</td></tr>
  <tr><td><strong>灵巧手</strong></td><td>峰岹科技</td><td>688279</td><td>电机驱动芯片，WIPO特斯拉灵巧手专利催化</td><td>&#x2b50;&#x2b50;</td></tr>
  <tr><td><strong>结构件/代工</strong></td><td>工业富联、长盈精密</td><td>601138/300115</td><td>整机代工+轻量化结构件</td><td>&#x2b50;&#x2b50;</td></tr>
  <tr><td><strong>电池/电源</strong></td><td>珠海冠宇</td><td>688772</td><td>机器人电池方案</td><td>&#x2b50;</td></tr>
</table>

<hr>

<h2>六、总结与展望</h2>

<div class="info-grid">
  <div class="info-item"><div class="il">&#x1f4cc; 昨日定性</div><div class="iv"><strong>A股昨日已收盘</strong>（06:29盘前）。三大指数集体收涨，结构性行情极致&mdash;&mdash;上涨不足1600家，下跌超3700家。科技硬件全面爆发：半导体+87亿、通信设备+68亿净流入领跑。CPO/光模块最强&mdash;&mdash;英伟达Spectrum-X硅光CPO交换机量产催化+中际旭创股价首超茅台（历史性时刻）。HBM4E全球首发。夜间COMEX白银跌至74.38美元（-1.56%）。</div></div>
  <div class="info-item"><div class="il">&#x1f440; 今日关注</div><div class="iv">
  <strong>1) &#x1f319; 美股AI板块走势</strong>&mdash;&mdash;今晚关注COMPUTEX 2026后续发酵<br>
  <strong>2) &#x1f1fa;&#x1f1f8; 美国就业数据</strong>&mdash;&mdash;ADP数据（周三20:15）及周五非农<br>
  <strong>3) COMPUTEX 2026后续（6/2-6/5）</strong>&mdash;&mdash;英特尔CEO陈立武演讲、AMD新产品发布<br>
  <strong>4) 今日CPO/光模块方向</strong>&mdash;&mdash;昨日全面爆发后，关注获利回吐与持续性博弈
  </div></div>
  <div class="info-item"><div class="il">&#x1f4a1; 今日展望</div><div class="iv">
  <strong>1) CPO方向：</strong>短线超买严重，注意获利回吐风险，但产业逻辑是近十年最强光通信趋势<br>
  <strong>2) 半导体方向：</strong>算力+存储双轮驱动，HBM4E时代开启+国产替代加速<br>
  <strong>3) 存储方向：</strong>HBM4E+SK海力士扩产+超级周期确认，逢低关注<br>
  <strong>4) 机器人方向：</strong>宇树IPO+特斯拉量产将至，6月配置窗口延续<br>
  <strong>5) 白银：</strong>74美元附近盘整，关注美国经济数据
  </div></div>
  <div class="info-item"><div class="il">&#x26a0;&#xfe0f; 风险提示</div><div class="iv">
  ① CPO/光模块方向昨日全面爆发，短线涨幅过大，今日可能出现获利回吐<br>
  ② A股&quot;涨指数跌个股&quot;结构性分化极致，超3700只下跌<br>
  ③ 美国ADP若强劲可能强化加息预期<br>
  ④ COMPUTEX 2026进入中期，催化剂边际效应递减<br>
  ⑤ 以上分析基于公开数据整理，<strong>不构成投资建议</strong>
  </div></div>
</div>

<hr>

<blockquote>&#x26a0;&#xfe0f; 以上分析基于公开数据和搜索结果整理，不构成投资建议。股市有风险，投资需谨慎。<br>
&#x1f4dd; 报告生成时间：2026-06-04 06:29 | 数据来源：公开市场信息 | 监测周期：盘前（A股已收盘）</blockquote>"""

# Read existing monitors
with open('site/data/monitors.json', 'r', encoding='utf-8') as f:
    monitors = json.load(f)

new_entry = {
    "id": "mon-20260604-0629",
    "date": "2026-06-04 06:29",
    "title": "AI板块盘前复盘 · 昨日CPO全线爆发 中际旭创股价超茅台 英伟达CPO量产持续发酵 白银74美元震荡",
    "tags": [
        "盘前",
        "A股收盘",
        "CPO爆发",
        "中际旭创超茅台",
        "英伟达量产",
        "HBM4E",
        "存储",
        "白银",
        "COMPUTEX2026"
    ],
    "summary": "A股昨日收盘三大指数收涨但近4000只下跌。CPO全线爆发中际旭创股价首超茅台。英伟达Spectrum-X硅光CPO交换机全面量产。HBM4E全球首发。COMEX白银跌至74.38美元。",
    "html": html_content
}

monitors.append(new_entry)

with open('site/data/monitors.json', 'w', encoding='utf-8') as f:
    json.dump(monitors, f, ensure_ascii=False, indent=2)

print(f'Appended entry {new_entry["id"]}')
print(f'Total entries: {len(monitors)}')