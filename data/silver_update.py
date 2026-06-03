#!/usr/bin/env python3
"""Update monitors.json with new AI market monitor entry"""
import json
import os
from datetime import datetime

data_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(data_dir, "monitors.json")

with open(json_path, "r", encoding="utf-8") as f:
    monitors = json.load(f)

# Report content
report_html = """<div class="metric-row">
  <div class="metric-box"><div class="num">4097.94</div><div class="lbs">上证午盘</div></div>
  <div class="metric-box"><div class="num">+0.56%</div><div class="lbs">上证涨幅</div></div>
  <div class="metric-box"><div class="num">+2.31%</div><div class="lbs">深成指</div></div>
  <div class="metric-box"><div class="num">+3.97%</div><div class="lbs">创业板指🚀</div></div>
  <div class="metric-box"><div class="num">+4.78%</div><div class="lbs">科创50</div></div>
  <div class="metric-box"><div class="num">1.89万亿</div><div class="lbs">半日成交</div></div>
  <div class="metric-box"><div class="num">74.67</div><div class="lbs">白银$</div></div>
</div>

<h1>AI板块盘中速览 · 科大讯飞/ComputeX双催化 创业板大涨近4% 算力/AI芯片全线爆发</h1>
<p><strong>时间：</strong>2026-06-03 13:00（A股交易中）</p>

<div class="tagline">📌 <strong>核心基调：</strong>今日A股科技股全面爆发，创业板指半日大涨3.97%站上4200点，科创50涨4.78%。ComputeX 2026持续催化叠加微软Build大会AI大模型发布，算力硬件、CPO、半导体全线井喷。AI板块主力资金疯狂涌入，半导体获超110亿净流入，通信设备近109亿。COMEX白银受美元走弱和中东局势影响，日内震荡偏弱报74.67美元/盎司。</div>

<hr>

<h2>📊 零、COMEX白银期货播报</h2>
<div class="info-grid">
  <div class="info-item"><div class="il">COMEX白银期货</div><div class="iv"><strong>约74.67美元/盎司</strong> <span class="pill pill-down">日内-1.17%</span></div></div>
  <div class="info-item"><div class="il">现货白银（伦敦银）</div><div class="iv"><strong>约74.38美元/盎司</strong> <span class="pill pill-down">日内-1.01%</span></div></div>
  <div class="info-item"><div class="il">美股前一晚收盘</div><div class="iv"><strong>75.44美元/盎司</strong> <span class="pill pill-up">+0.25%</span></div></div>
  <div class="info-item"><div class="il">美元指数</div><div class="iv"><strong>约99.26</strong> <span class="pill pill-mid">小幅走强</span></div></div>
  <div class="info-item"><div class="il">伦银现货</div><div class="iv"><strong>约74.76美元/盎司</strong> <span class="pill pill-down">日内-0.40%</span></div></div>
  <div class="info-item"><div class="il">沪银主力</div><div class="iv"><strong>约18,300元/千克</strong> <span class="pill pill-mid">窄幅震荡</span></div></div>
</div>

<p><strong>近期趋势判断：</strong>白银今日亚盘偏弱运行，COMEX期货从隔夜收盘的75.44美元回落至74.67美元附近，跌幅超1%。自5月中旬从接近90美元高位回落后，白银已在75美元附近盘整多日。关键技术位方面，<strong>74.63美元（61.8%回撤位）</strong>为短期关键支撑，若跌破可能加速下行。</p>

<p><strong>驱动因素简析：</strong></p>
<ul>
  <li><strong>美伊局势反复：</strong>伊朗革命卫队3日凌晨声明称，美军对伊朗支持的胡塞武装发动空袭，伊朗随即袭击美海军第五舰队总部。霍尔木兹海峡通行许可虽恢复申请，但实际航运仍低迷，地缘溢价支撑贵金属</li>
  <li><strong>美元指数小幅反弹：</strong>美元指数报99.26，日内小幅走强，对贵金属形成短线压制</li>
  <li><strong>美国就业数据强势：</strong>4月美国职位空缺跃升至762万创近两年新高，劳动力市场韧性超出预期，为美联储保持鹰派立场提供依据，压制银价</li>
  <li><strong>美联储鹰派升温：</strong>克利夫兰联储主席哈马克表示需更多证据确认通胀回归目标，市场对6月降息的概率预期不足2%</li>
  <li><strong>工业属性支撑：</strong>COMEX白银库存自2025年10月以来腰斩，2026年Q1交割量同比增加72%，实物供需偏紧</li>
  <li><strong>机构观点分化：</strong>美银看多Q4冲击100美元，瑞银偏谨慎下调年底目标至80美元</li>
</ul>

<hr>

<h2>一、大盘解读（午盘13:00数据）</h2>

<div class="info-grid">
  <div class="info-item"><div class="il">上证指数</div><div class="iv"><strong>4097.94</strong> <span class="pill pill-up">+0.56%</span></div></div>
  <div class="info-item"><div class="il">深证成指</div><div class="iv"><strong>15951.08</strong> <span class="pill pill-up">+2.31%</span></div></div>
  <div class="info-item"><div class="il">创业板指</div><div class="iv" style="color:#22c55e"><strong>4216.74 +3.97% 🚀 站上4200点</strong></div></div>
  <div class="info-item"><div class="il">科创50</div><div class="iv" style="color:#22c55e"><strong>+4.78% 💥 领涨全场</strong></div></div>
  <div class="info-item"><div class="il">半日成交额</div><div class="iv"><strong>1.89万亿元</strong> <span class="pill pill-up">放量789亿</span></div></div>
  <div class="info-item"><div class="il">上涨/下跌</div><div class="iv"><span style="color:#22c55e">上涨超1900只</span> / 跌多涨少（权重股带动指数）</div></div>
</div>

<p><strong>市场特征：</strong>三大指数早盘低开高走，创业板指半日大涨<strong>3.97%</strong>站上4200点，科创50暴涨<strong>4.78%</strong>领涨市场。两市半日成交额1.89万亿，较周二放量789亿元。半导体芯片、CPO、光纤概念成为最强主线。这是继6月1日科创50暴跌5%后，科技股全面强势修复。</p>

<p><strong>今日核心催化事件：</strong></p>
<ul>
  <li>🔥 <strong>微软Build 2026大会连发七款自研AI模型</strong>：MAI-Thinking-1旗舰推理模型+六款编码/图像/语音/多模态模型，全部从零训练、无第三方蒸馏，标志微软AI自研战略正式落地</li>
  <li>🔥 <strong>ComputeX 2026展会进行中（6/2-6/5）</strong>：英伟达AI工厂全栈路线+三星HBM4E样品交付+英特尔AI芯片进展</li>
  <li>🔥 <strong>英伟达Spectrum-X以太网硅光技术正式量产</strong>：基于CPO技术，能效比传统方案提升5倍</li>
  <li>🔥 <strong>美银研报：AI产业链核心正从算力转向存储</strong>，HBM4E交付催化存储板块大涨</li>
  <li>🔥 <strong>腾讯市值单日暴增3000亿</strong>：微信内嵌AI智能体传闻引爆港股</li>
</ul>

<hr>

<h2>二、AI板块整体市场概览</h2>

<p>今日AI板块<strong>全面爆发</strong>，半导体芯片、CPO通信、算力硬件三大方向集体井喷，与6月1日的\"硬切软\"格局形成鲜明对比。AI ETF全线大涨——人工智能ETF易方达(159819)涨幅近5%，科创芯片ETF(588290)涨5.75%。市场情绪从前期的获利了结模式快速切换回AI主线进攻模式。</p>

<p><strong>AI核心ETF表现：</strong></p>
<ul>
  <li><strong>人工智能ETF易方达(159819)</strong> 涨<strong>4.72%</strong>，成交5.33亿元</li>
  <li><strong>科创芯片ETF(588290)</strong> 涨<strong>5.75%</strong>，全市场同指数最低费率</li>
  <li><strong>创业板人工智能ETF大成(159242)</strong> 涨<strong>4.72%</strong>，连续6日获资金净流入合计3.59亿元</li>
  <li><strong>通信ETF广发(159507)</strong> 涨近<strong>6%</strong></li>
</ul>

<p><strong>半导体芯片全面走强：</strong>寒武纪+6.15%、海光信息+4.06%、中芯国际+3.74%，科创芯片指数30日累计涨幅27.69%，动能强劲。</p>

<p><strong>培育钻石/超硬材料板块延续强势：</strong>培育钻石作为AI芯片散热材料获市场追捧，楚江新材、国机精工涨停。</p>

<hr>

<h2>三、细分领域动态</h2>

<div class="sect-card">
<div class="sh">🔷 算力板块 <span class="pill pill-up">全面爆发</span> <span class="pill pill-up">主力超百亿流入</span></div>
<p class="sn"><strong>资金面（半日）：</strong>算力/半导体板块今日成为主力资金<strong>最疯狂涌入</strong>的方向。半导体板块半日主力净流入<strong>110.95亿元</strong>居所有板块首位，板块大涨4.18%；通信设备板块主力净流入<strong>109.45亿元</strong>（板块涨3.87%）。电子板块半日净流入<strong>超109亿元</strong>。个股方面，中际旭创获净流入51.87亿、长电科技33.61亿、TCL科技24.31亿。资金从前期防御板块（银行/电力/食品饮料）大规模回流科技。</p>
<p class="sn"><strong>政策面：</strong>工信部等四部门此前联合印发《2026年提升全民数字素养与技能工作要点》，强调AI素养提升。英伟达ComputeX上宣布Spectrum-X硅光技术量产，CPO成为AI数据中心标配。华为\"韬定律\"继发布后持续发酵——从晶体管时代进入系统级优化时代，利好国产算力生态。</p>
<p class="sn"><strong>基本面：</strong>微软Build 2026发布七款全自研AI模型是今日<strong>最强催化</strong>。MAI系列覆盖推理/编码/图像/语音/多模态，核心旗舰MAI-Thinking-1实测对标海外头部推理产品。微软从\"AI平台使用者\"向\"AI模型开发者\"身份转变，利好算力基础设施需求。英伟达ComputeX展示AI工厂全栈硬件路线：Rubin GPU、GB300、RTX Spark等。慧与（HPE）财报强劲、股价创纪录大涨。</p>
<p class="sn"><strong>情绪面：</strong>6月1日算力硬件大幅回调后市场情绪<strong>快速修复</strong>，\"AI主线未变\"的观点得到验证。ComputeX+微软Build双催化极大提振了多头信心。科创50大涨4.78%显示科技股人气重聚。算力不再只是\"硬件涨价\"逻辑，AI应用规模化带来的算力需求正加速落地。</p>
</div>

<div class="sect-card">
<div class="sh">🔷 存储板块 <span class="pill pill-up">HBM4E催化大涨</span> <span class="pill pill-up">超级周期确认</span></div>
<p class="sn"><strong>资金面：</strong>存储板块跟随半导体整体大涨。兆易创新延续强势。<strong>佰维存储</strong>涨超<strong>8%</strong>领涨存储方向。北向资金持续在存储龙头上活跃，佰维存储获北向增持显著。</p>
<p class="sn"><strong>政策面：</strong>中国信息安全测评中心发布AI训练推理芯片安全可靠测评结果，9款芯片通过评测，利好国产存储生态。长鑫科技科创板IPO过会后持续推进。</p>
<p class="sn"><strong>基本面（今日最强催化）：</strong></p>
<ul>
  <li><strong>三星电子ComputeX 2026全球首发HBM4E内存样品</strong>：单堆叠16GB，带宽突破1.5TB/s（较HBM3E提升50%），已交付主流AI芯片厂商验证。同时展示全球首款<strong>HBM5原型</strong>（预计2029-2031年推出，带宽目标4TB/s）</li>
  <li><strong>三星已5月交付12层HBM4E样品</strong>，领先竞争对手</li>
  <li><strong>美银最新研报：AI产业链核心瓶颈正从算力转向存储</strong>。在长上下文、高并发AgenticAI场景中，内存容量与带宽的重要性快速提升</li>
  <li><strong>黄仁勋与SK集团会长崔泰源6月1日台北会谈</strong>（今年第三次会面），聚焦AI存储合作前景</li>
  <li>高盛+瑞银此前双确认DRAM缺货至2028年，存储超级周期逻辑持续强化</li>
</ul>
<p class="sn"><strong>情绪面：</strong>存储板块今日情绪<strong>极度亢奋</strong>。HBM4E样品交付标志着存储技术迭代进入新阶段，HBM5概念预演也激发了产业想象力。AI产业链核心从\"算力为王\"向\"存储为王\"转变的观点被更多机构接受。美银指出\"东算+西存\"协同格局形成。</p>
</div>

<div class="sect-card">
<div class="sh">🔷 机器人板块 <span class="pill pill-up">板块活跃</span> <span class="pill pill-mid">跟随大盘反弹</span></div>
<p class="sn"><strong>资金面：</strong>机器人板块今日表现活跃，浙江荣泰涨停，奥比中光涨超10%，绿的谐波涨6.6%，德马科技、五洲新春、晋拓股份跟涨。机器人板块今日随科技大盘反弹，但并非今日最强势细分方向。</p>
<p class="sn"><strong>政策面：</strong>宇树科技科创板IPO 6月1日已顺利过会（73天创科创板最快纪录），今日处于持续发酵阶段。中信建投研报指出Optimus量产渐行渐近，供应链量产量纲逐步清晰，V3产品发布仍值得期待。ICRA 2026上，中科院自动化所联合团队获图像质量、动作跟随两大核心指标全球第一。</p>
<p class="sn"><strong>基本面：</strong>特斯拉Optimus Gen3预计2026年7-8月启动量产。中信证券判断V3版本设计接近定型。宇树科技作为\"A股人形机器人第一股\"估值约420亿元，为产业链提供估值锚。智元机器人自研世界模型GE 2.0获World Arena冠军。</p>
<p class="sn"><strong>情绪面：</strong>宇树IPO过会后市场对板块信心增强，但机器人板块今日表现相对温和。此前\"硬切软\"轮动中机器人也未充分受益，现在随科技股整体估值修复。中长期催化剂明确（特斯拉量产+宇树上市+国产机器人IPO推进），情绪稳中向好。</p>
</div>

<div class="sect-card">
<div class="sh">🔷 CPO板块 <span class="pill pill-up">今日涨幅最大方向之一</span> <span class="pill pill-up">情绪高涨</span></div>
<p class="sn"><strong>资金面：</strong>CPO/光模块板块今日<strong>强势领涨全场</strong>，是AI板块中涨幅最大的细分方向。<strong>源杰科技涨超18%</strong>股价再创新高，金信诺涨12%，依米康涨超10%，天孚通信、光库科技、锐捷网络涨超8%，中际旭创、新易盛、太辰光等多股领涨。中际旭创突破1.4万亿市值超越茅台和宁德时代成为沪深300权重股榜首。通信设备板块半日资金净流入109.45亿。</p>
<p class="sn"><strong>政策面：</strong>英伟达ComputeX 2026官宣Spectrum-X以太网硅光技术<strong>全面量产</strong>——基于CPO+光电一体封装，服务于Vera Rubin平台数据中心扩展。能效比传统方案提升5倍，AI正常运行时间提升5倍，部署速度快1.3倍。英伟达已与Coherent、Corning、Lumentum签署多年战略协议锁定关键产能。工信部要求新建智算中心CPO适配≥60%。</p>
<p class="sn"><strong>基本面（最强劲产业数据）：</strong></p>
<ul>
  <li><strong>LightCounting预测</strong>：2026年全球以太网光模块市场增长<strong>65%</strong>，1.6T产品大规模交付</li>
  <li><strong>高盛预测</strong>：2026年全球光模块市场规模有望达<strong>285-480亿美元</strong>，AI需求占比超60%</li>
  <li>中际旭创800G全球市占率>42%，1.6T产品全球唯一批量供货厂商，订单排期至<strong>2028年</strong></li>
  <li>CPO能将800G端口功耗从14-16W降至5.2-5.6W（降幅60-68%），十万卡集群建设至关重要</li>
  <li>2026年被机构定义为<strong>CPO产业化元年</strong></li>
  <li>外资（QFII）重仓天孚通信、中际旭创、源杰科技等24家CPO公司</li>
</ul>
<p class="sn"><strong>情绪面：</strong>CPO板块情绪今日<strong>极度高涨</strong>。英伟达官宣CPO量产+中际旭创市值突破1.4万亿双双成为最核心的情绪催化剂。\"易中天\"（新易盛/中际旭创/天孚通信）齐创新高。媒体和投资者高度关注CPO产业逻辑，2026年作为CPO元年的市场共识进一步增强。北向资金今日积极配置CPO龙头。LightCounting乐观预测提振了板块整体估值空间信心。</p>
</div>

<hr>

<h2>四、主流净流入板块监控（半日数据）</h2>

<table>
  <tr><th>#</th><th>板块/行业</th><th>净流入参考</th><th>核心驱动</th><th>驱动类型</th></tr>
  <tr><td><strong>1</strong></td><td><strong>半导体</strong></td><td><span class="green"><strong>+110.95亿</strong></span></td><td>微软七款自研AI模型+ComputeX+英伟达CPO量产三催化叠加</td><td><span class="pill pill-up">产业密集催化</span></td></tr>
  <tr><td><strong>2</strong></td><td><strong>通信设备</strong></td><td><span class="green"><strong>+109.45亿</strong></span></td><td>英伟达Spectrum-X CPO硅光量产+光模块市场增65%</td><td><span class="pill pill-up">产业+事件</span></td></tr>
  <tr><td><strong>3</strong></td><td><strong>电子</strong></td><td><span class="green"><strong>+109亿</strong></span></td><td>电子板块昨日下午盘全面发力，中际旭创+TCL科技领涨</td><td><span class="pill pill-up">产业驱动</span></td></tr>
  <tr><td><strong>4</strong></td><td><strong>机械设备</strong></td><td><span class="green">获主力流入</span></td><td>培育钻石/AI芯片散热+工业机器人预期</td><td><span class="pill pill-mid">产业+材料</span></td></tr>
  <tr><td><strong>5</strong></td><td>小金属</td><td><span class="green">板块涨3%+</span></td><td>培育钻石/超硬材料持续走强，芯片散热概念扩散</td><td><span class="pill pill-mid">材料替代</span></td></tr>
  <tr><td><strong>6</strong></td><td>光纤/铜缆连接</td><td><span class="green"><strong>板块大涨</strong></span></td><td>世嘉科技/长飞光纤/亨通光电涨停，英伟达CPO催化</td><td><span class="pill pill-mid">产业催化</span></td></tr>
  <tr><td><strong>7</strong></td><td>PCB概念</td><td><span class="green"><strong>板块走强</strong></span></td><td>迅捷兴/一博科技/东材科技涨停，CPO量产带动</td><td><span class="pill pill-mid">产业传导</span></td></tr>
  <tr><td><strong>8</strong></td><td>CPO概念</td><td><span class="green"><strong>板块领涨全线</strong></span></td><td>光模块/光芯片全线爆发，产业化元年确认</td><td><span class="pill pill-up">产业确立</span></td></tr>
</table>

<p><strong>资金流出方向：</strong>电力设备（-56.43亿）、医药生物（-26.85亿）、电网设备（-26.41亿）、食品饮料（-15.72亿）、白酒（持续走低）。</p>

<p><strong>资金流向核心发现：</strong></p>
<ul>
  <li><strong>AI板块今日绝对主导全市场</strong>——半导体+通信设备合计流入约<strong>220亿元</strong>，占全市场净流入的绝大部分，为近几个月罕见的高集中度</li>
  <li>资金从<strong>防御板块（电力设备/医药生物/白酒）大幅回流科技股</strong>，风格重归\"进攻模式\"</li>
  <li><strong>AI板块相对热度判断：🔥🔥🔥 极高</strong>——今日AI板块是全市场唯一的资金主攻方向，半导体和通信设备两个板块的合计净流入即超过大部分交易日所有板块总和</li>
  <li>北向资金方面，今日积极加仓CPO/算力/光模块方向，中际旭创/新易盛/天孚通信持续获北向买入</li>
</ul>

<hr>

<h2>五、关键异动个股</h2>

<table>
  <tr><th>个股</th><th>代码</th><th>异动</th><th>逻辑</th><th>关注度</th></tr>
  <tr><td><strong>中际旭创</strong></td><td>300308</td><td><span class="pill pill-up"><strong>大涨创新高</strong></span><br>主力净流入51.87亿</td><td>CPO光模块绝对龙头，英伟达CPO量产直接受益，市值突破1.4万亿超越茅台/宁德，跻身沪深300权重第一</td><td>⭐⭐⭐</td></tr>
  <tr><td><strong>源杰科技</strong></td><td>688498</td><td><span class="pill pill-up"><strong>涨超18%创新高</strong></span></td><td>光芯片龙头，英伟达Spectrum-X CPO硅光量产催化+1.6T光芯片需求激增</td><td>⭐⭐⭐</td></tr>
  <tr><td><strong>天孚通信</strong></td><td>300394</td><td><span class="pill pill-up"><strong>涨超10%创新高</strong></span><br>主力净买入超17.93亿</td><td>CPO龙头三剑客之一（\"易中天\"），外资QFII重仓+英伟达CPO产业链核心受益</td><td>⭐⭐⭐</td></tr>
  <tr><td><strong>长电科技</strong></td><td>600584</td><td><span class="pill pill-up">主力净流入33.61亿</span></td><td>半导体封装测试龙头，先进封装受益AI芯片需求爆发+英伟达供应链概念</td><td>⭐⭐⭐</td></tr>
  <tr><td><strong>和林微纳</strong></td><td>688661</td><td><span class="pill pill-up"><strong>涨停+20%</strong></span></td><td>精密微纳零部件龙头，AI算力散热+芯片测试探针概念，当日主力净流入9435万</td><td>⭐⭐</td></tr>
  <tr><td><strong>长飞光纤</strong></td><td>601869</td><td><span class="pill pill-up"><strong>涨停+10%</strong></span></td><td>光纤龙头，全球首条三波段超低损多芯光缆上周在青岛开通，CPO+AI算力互连核心</td><td>⭐⭐</td></tr>
</table>

<hr>

<h2>六、特斯拉机器人概念股解析</h2>

<p><strong>最新产业进展：</strong>特斯拉Optimus量产时间表锁定——<strong>2026年7-8月启动规模化量产</strong>，目前处于量产前密集准备阶段。MS马斯克价值1万亿美元薪酬方案与\"生产100万台机器人\"目标直接挂钩。中信证券最新研报判断V3版设计接近定型，灵巧手是最新核心升级点。</p>

<p><strong>近期催化：</strong></p>
<ul>
  <li>宇树科技科创板IPO 6月1日顺利过会（73天闪电速度），冲击\"人形机器人第一股\"</li>
  <li>特斯拉弗里蒙特工厂Model S/X产线全面改造为机器人专用产线</li>
  <li>得州超级工厂同步筹备二期产线</li>
  <li>中信建投：Optimus量产渐行渐近，放量节奏逐步验证</li>
</ul>

<table>
  <tr><th>环节</th><th>核心公司</th><th>代码</th><th>受益逻辑</th><th>优先级</th></tr>
  <tr><td><strong>执行器/总成</strong></td><td>三花智控、拓普集团</td><td>002050/601689</td><td>线性/旋转执行器核心供应商，特斯拉验证推进</td><td>⭐⭐⭐</td></tr>
  <tr><td><strong>精密减速器</strong></td><td>绿的谐波、双环传动</td><td>688017/002472</td><td>谐波减速器/RV减速器，机器人最高壁垒环节</td><td>⭐⭐⭐</td></tr>
  <tr><td><strong>伺服电机</strong></td><td>汇川技术、卧龙电驱</td><td>300124/600580</td><td>驱控一体方案，国产电机龙头，ODM模式切入</td><td>⭐⭐</td></tr>
  <tr><td><strong>传感器</strong></td><td>柯力传感、奥比中光</td><td>603662/688322</td><td>力矩传感器/3D视觉传感器</td><td>⭐⭐</td></tr>
  <tr><td><strong>灵巧手</strong></td><td>峰岹科技</td><td>688279</td><td>电机驱动芯片，WIPO特斯拉灵巧手专利催化，核心执行单元</td><td>⭐⭐</td></tr>
  <tr><td><strong>结构件/代工</strong></td><td>工业富联、长盈精密</td><td>601138/300115</td><td>整机代工+轻量化结构件</td><td>⭐⭐</td></tr>
  <tr><td><strong>电池/电源</strong></td><td>珠海冠宇</td><td>688772</td><td>机器人电池方案，低波动电源技术</td><td>⭐</td></tr>
</table>

<p><strong>机构观点：</strong>中信证券坚定看好特斯拉机器人及供应链企业。浙商证券指出6月是配置机器人板块好时机。中信建投强调机器人板块波动中聚焦优质环节。</p>

<hr>

<h2>七、总结与展望</h2>

<div class="info-grid">
  <div class="info-item"><div class="il">📌 13:00盘中定性</div><div class="iv" style="font-size:14px"><strong>A股交易中</strong>（13:00午盘）。AI板块全面爆发——创业板指大涨3.97%站上4200点，科创50暴涨4.78%。半导体+通信设备合计获主力净流入超220亿元。微软Build七款自研AI模型+英伟达Spectrum-X CPO量产+三星HBM4E样品交付三大催化共振。CPO/算力芯片/存储全面开花。</div></div>
  <div class="info-item"><div class="il">👀 下午关注</div><div class="iv" style="font-size:14px">
  <strong>1) 收盘前资金是否会持续涌入</strong>——若下午量能维持，今日有望冲击更高涨幅<br>
  <strong>2) 算力/CPO龙头能否涨停</strong>——多只标的正逼近涨停板<br>
  <strong>3) 北向资金今日净流入规模</strong><br>
  <strong>4) 白银关注76美元能否收复</strong>
  </div></div>
  <div class="info-item"><div class="il">💡 午后展望</div><div class="iv" style="font-size:14px">
  <strong>1) AI硬件持续领跑</strong>——ComputeX+微软Build双催化明确了AI硬件需求趋势，预计下午板块维持强势<br>
  <strong>2) CPO概念有望继续扩散</strong>——英伟达CPO量产确认后，上游光芯片/光器件/PCB方向逻辑强化<br>
  <strong>3) 存储板块关注HBM4E供应链</strong>——三星交付样品后，国产化替代链有望受益<br>
  <strong>4) 机器人板块温和跟涨</strong>——宇树IPO发酵+特斯拉量产预期支撑
  </div></div>
  <div class="info-item"><div class="il">⚠️ 风险提示</div><div class="iv" style="font-size:14px;color:#f59e0b">
  ① 今日AI板块成交占比偏高，已进入\"极度拥挤\"区间，警惕尾盘资金回吐压力<br>
  ② 6月1日科创50单日暴跌5%的经验表明科技股短期波动剧烈<br>
  ③ 6月进入财报真空期+美国通胀数据超预期风险<br>
  ④ 白银短线受强势就业数据压制，74.63美元支撑若破将加速回调<br>
  ⑤ <strong>以上分析基于公开数据整理，不构成投资建议</strong>
  </div></div>
</div>

<hr>

<blockquote>⚠️ 以上分析基于公开数据和搜索结果整理，不构成投资建议。股市有风险，投资需谨慎。<br>
📝 报告生成时间：2026-06-03 13:00 | 数据来源：公开市场信息 | 监测周期：1小时</blockquote>"""

new_entry = {
    "id": "mon-20260603-1300",
    "date": "2026-06-03 13:00",
    "title": "AI板块盘中速览 · 微软Build七款AI模型+ComputeX双催化 创业板大涨4% 算力/CPO全线井喷",
    "tags": ["盘中", "微软Build", "ComputeX2026", "CPO量产", "HBM4E", "半导体", "算力", "机器人", "白银"],
    "summary": "AI板块全面爆发：创业板大涨4%站上4200点，科创50涨4.78%。半导体+通信设备合计净流入超220亿。中际旭创市值破1.4万亿。",
    "html": report_html
}

# Check for duplicate ids
existing_ids = [m["id"] for m in monitors]
if new_entry["id"] not in existing_ids:
    monitors.append(new_entry)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(monitors, f, ensure_ascii=False, indent=2)
    print(f"✅ Added new entry: {new_entry['id']}")
else:
    print(f"⚠️ Duplicate ID {new_entry['id']} found, replacing...")
    for i, m in enumerate(monitors):
        if m["id"] == new_entry["id"]:
            monitors[i] = new_entry
            break
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(monitors, f, ensure_ascii=False, indent=2)
    print(f"✅ Replaced entry: {new_entry['id']}")