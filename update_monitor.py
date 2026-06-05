#!/usr/bin/env python3
"""Update monitors.json with new entry and rebuild site."""
import json, os, sys

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
MONITORS_FILE = os.path.join(DATA_DIR, "monitors.json")

# New monitor entry - read HTML from external file to avoid encoding issues
entry = {
    "id": "mon-20260604-2054",
    "date": "2026-06-04 20:54",
    "title": "AI板块盘后总结 & COMEX白银期货播报 — A股收盘后聚焦美股与次日展望",
    "tags": ["AI板块", "白银", "盘后", "CPO", "算力", "存储", "机器人"],
    "summary": "A股今日低开高走收跌但芯片/电子逆市吸金535亿元；白银73美元震荡",
    "html": ""
}

html_content = """<h1>AI板块盘后总结报告 & COMEX白银期货播报</h1>
<p><strong>【2026-06-04 20:54 北京时间】</strong></p>
<p style="color:#ff6600;font-weight:bold;">&#x26A0;&#xFE0F; A股今日已收盘（15:00），本报告聚焦盘后消息、美股预判和次日展望。</p>
<hr/>

<h2>&#x96F6;&#x3001;COMEX白银期货播报</h2>
<ul>
<li><strong>最新价格：</strong> COMEX白银期货主力合约最新报约 <strong>73.00-73.50美元/盎司</strong>，日内小幅震荡。现货白银交投于73美元/盎司附近。</li>
<li><strong>日内涨跌幅：</strong> 今日亚盘现货白银一度触及73.72美元/盎司（涨超1%），随后回落，欧盘时段维持窄幅震荡。</li>
<li><strong>近期趋势判断：</strong> 白银自5月中旬近<strong>89美元/盎司</strong>高位持续回调后，目前在<strong>72-76美元区间震荡整理</strong>。中期关注COMEX库存持续下降（Q1已腰斩）带来的供给支撑，短期受美元指数和美伊局势反复压制。</li>
<li><strong>驱动因素简析：</strong>
<ul>
<li>美伊谈判本周末或重启，特朗普称协议签署后霍尔木兹海峡将重新开放，油价回落带动贵金属企稳</li>
<li>美国5月ADP就业数据超预期强化鹰派预期，但市场已逐步消化</li>
<li>COMEX白银库存2026年Q1腰斩，实物供需偏紧提供中期底部支撑</li>
<li>光伏/电子等工业需求维持高位，美国银行预测白银Q4有望冲击100美元/盎司</li>
<li>瑞银将2026年底白银预测下调至80美元/盎司，多空分歧加大</li>
</ul></li>
<li><strong>关联品种：</strong> 现货黄金今日企稳于4470美元/盎司附近，日内涨近1%。</li>
</ul>

<h2>&#x4E00;&#x3001;大盘回顾</h2>
<p><strong>今日（6月4日月，周四）A股三大指数低开分化震荡，尾盘集体收跌：</strong></p>
<ul>
<li><strong>>上证指数：</strong> 收跌<strong>0.64%</strong>，报4058点附近</li>
<li><strong>深证成指：</strong> 收跌<strong>0.27%</strong></li>
<li><strong>创业板指：</strong> 收跌<strong>0.83%</strong></li>
<li><strong>>盘面特征：</strong>> 三大指数集体低开（受隔夜美股回调影响），盘中深成指一度翻红，但尾盘承压回落。全市场约3700只个股下跌，涨停56股，封板率81%。</li>
<li><strong>成交额：</strong> 沪深两市全天成交额约<strong>2.76万亿元</strong>（较昨日3.13万亿元缩量），但仍维持较高水平。</li>
<li><strong>>隔夜美股参考：</strong>> 6月3日美股三大指数收跌（道指-1.21%、标普-0.73%、纳指-0.89%），但<strong>费城半导体指数逆市涨1.39%创历史新高</strong>，年初至今累涨96.48%。</li>
</ul>

<h2>&#x4E8C;&#x3001;AI板块整体市场概览</h2>
<blockquote>今日AI板块 <strong>低开后分化轮动</strong>：CPO经历昨日的集体大涨后今日进入<strong>技术性回调</strong>，芯片半导体接力上涨，AI产业内部轮动健康。资金面电子板块逆市净流入<strong>535亿元</strong>高居全行业首位。北向资金全天成交3651.69亿元，占两市成交额13.24%。博通560亿美元AI芯片销售额预测+英伟达CPO量产两大事件持续为板块提供产业逻辑支撑。</blockquote>

<h2>&#x4E09;&#x3001;细分领域动态</h2>

<h3>算力板块</h3>
<ul>
<li><strong>资金面：</strong> &#x1F4B0; <strong>半导体/芯片板块今日主力资金净流入居前</strong>。芯片产业链早盘主力资金净流入一度高达<strong>106.6亿元</strong>。科创芯片ETF南方(588890)收涨超2%冲击3连胜，半导体ETF国联安(512480)涨2.56%。<strong>电子板块全天主力资金净流入535亿元</strong>，高居31个申万一级行业首位。</li>
<li><strong>政策面：</strong> &#x1F4;&#x1F4F3; 发改委/工信部联合发布布新一代人工智能发展规划(2026-2030)》，算算基础设施列为第一重点点，<strong>2030年AI核心产业规模超5万亿元</strong>。东数西算2026年投资超2000亿元。大基金二期重点投向AI硬件。</li>
<li><strong>基本面：</strong> &#x1F1C; 博通预测<strong>2026财年AI芯片销售额达560亿美元</strong>，已向OpenAI交付芯片。台积电总裁魏哲家表示全球芯片供应未来几年都无法满足AI带动需求。英伟达在Computex 2026发布Vera CPU全面投产。招商证券看好半导体产业持续受益AI需求增长。</li>
<li><strong>情绪面：</strong> &#x1F60A; 偏积极。算力需求从训练端向推理端延伸的长逻辑清晰，博通/英伟达引引强劲。但A股收盘后关注美股盘前NVDA动向。</li>
</ul>

<h33>存储板块</h3>
<ul>
<li><strong>资金面：</strong> &#x1F4B0; <strong>存储芯片概念今日收涨2.42%</strong>，获主力资金净流入<strong>92.02亿元</strong>。其其中111股获主力资金净流入，42股净流入超亿元。兆易创新主力净流入<strong>18.71亿元</strong>居首，德明利13.01亿元、大族激光10.39亿元紧紧跟。</li>
<li><strong>政策面：</strong> &#x1F4DB; SK海力士计划五五年内晶晶圆产能翻番，Arm CEO表示存储芯片供应体仍吃紧，HBM/DRAM/NAND供需平衡均紧张张。</li>
<li><strong>基本面：</strong> &#x1F52C; <strong>三星交付全球首批HBM4E样品</strong>（带宽超1.5TB/s），并在Computex 2026展示全球首款<strong>HBM5原型</strong>（带宽目标4TB/s）。HBM4E带宽突破4TB/s成讨论焦点，业内认为虽阶段缓解了存储墙瓶颈但并未彻底解决。中国银河证券指出AI服务器正成为拉动MLCC需求的核心场景。</li>
<li><strong>情绪面：</strong> &#x1F60A; 持续高热。HBM技术迭代加速，存储从周期股向成长股切换预期强化。沪硅产业涨超14%%，兆易创新涨超7%成为今日存储方向领涨标的。</li>
</ul>

<h33>机器人板块</h3>
<ul>
<li><strong>资金面：</strong>> &#x1F4B0; 今日机器人板块小幅震荡，未出现明显异动。回顾6月2 –板块涨1.12%但主力净流出10.64亿元，近期资金面偏中性。</li>
<li><strong>政策面：</strong> &#x1F4DB; 四部门联合印发《2026年提升全民数字素养与技能工作要点》，将AI素养提升单独列为重点任务。外交部部长助理率37国驻华使节参访深圳具身智能企业，显示外交层面对机器人产业的重视。</li>
<li><strong>基本面：</strong> &#x1F52C; <strong>比亚迪正式官宣自研人形机器人&quot;尧舜禹&quot;</strong>，2026年计划内部部署2万台，已组建约4000人核心研发团队（博士占比超30%），原型机迭代至第七代。宇树科技科创板73天闪电过会。特斯拉Optimus预计2026年更广泛推广。2028年人形机器人市场规模有望超138亿美元、2035年达2000亿美元。</li>
<li><strong>情绪面：</strong> &#x1F60A; 概念向量产切换预期强烈。摩根士丹利将2026年称为&quot;首个真正的重新定价窗口&quot;，执行器成本已降90%。但电池续航仍是制约因素。</li>
</ul>

<h33>CPO板块</h3>
<ul>
<li><strong>资金面：</strong> &#x1F4B0; 今日CPO板块开盘跌幅居前，为昨日大涨后的<strong>技术性回调</strong>。但昨日（6月3日）通信板块主力净流入36.33亿元。中际旭创昨日大涨后今日回调，但创业板人工智能ETF华宝(159363)昨日大涨超5%成交11亿元。今日通信板块整体净流出。</li>
<li><strong>政策面：</strong> &#x1F4DB; <strong>英伟达6月2日官宣Spectrum-X硅光CPO交换机全面量产</strong>，能效较传统方案提升5倍、AI部署效率提高130%。明确2026年四季实现CPO规模化商用。2026年被机构定义为<strong>CPO产业化元年</strong>。</li>
<li><strong>基本面：</strong>> &#x1F52C; <strong>中际旭创昨日股价超越贵州茅台</strong>（最高1290元），800G全球市占率超42%，1.6T全球唯一批量供货厂商，订单排期覆盖至2028年。高盛预测2026年全球光模块市场规模达285-480亿美元，AI需求占比超六成。英伟达在Computex指出AI发展瓶颈正从算力/存储转向高速连接，光互连技术有望迈入产业景气周期。</li>
<li><strong>情绪面：</strong>> &#x1F60A;&#x1F628; 持续亢奋但已现分化。昨日易中天（中际旭创、新易盛、天孚通信）批量创历史新高后今日正常回调，获利资金兑现现象明显。但黄仁勋点名Marvell为&quot;下一家万亿美元公司&quot;的言论持续发酵，Marvell隔夜暴涨32%。</li>
</ul>

<h2>&#x56DB;&#x3001;主流净流入板块监控</h2>
<h3>6月4日行业板块主力资金流向TOP10</h3>
<tabble border=&quot;1&quot; cellpaddding=&quot;6&quot; cellspacing=&quot;0&quot; style=&quot;border-collapse:collapse;width:100%;&quot;>
<trr style=&quot;background:#4a90d9;color:white;&quot;><th>排名</th><th>行业板块</th><th>主力净流入</th><th>驱动逻辑</th></tr>
<tr><td>1</td><td>>strong>电子</strong></td><td><strong>+535亿元<</strong></td><td>>AI算力+消费电子+存储三线共振，京东方A涨停</td></tr>
<tr><td>2</td><td>>strong>>元件</strong></td><td><strong>大幅净流入</strong></td><td>PCB/AI服务器零部件需求爆发，沪电股份涨超8%创新高</td></tr>
<tr><td>3</td><td>>strong>>光学光电子</strong></td><td><strong>>大幅净流入</strong></td><td>>京东方A活力净买入34亿元居A股首位，三安光电涨停</td></tr>
<tr><td>4</td><td><strong>>半导体/芯片</strong></td><td><strong>净流入106.6亿+</strong></td><td>>存储芯片概念净流入92亿，国家大基金概念涨3.24%</td></tr>
<tr><td>5</td><td>>国家大基金持股</td>>td>大幅净流入</td>>td>华虹公司净流入4.96亿</td></tr>
<tr><td>6</td><td>>机械/工程</td>>td>净流入</td>>td>工程机械ETF表现亮眼</td></tr>
<tr><td>7</td><td>>消费电子</td>>td>净流入</td><td>>苹果链/安卓链备货旺季启动</td></tr>
<tr><td>8</td><td>>氢能源</td><td>>小幅流入</td><td>>政策驱动，清洁能源规划</td></tr>
<tr><td>9</td><td>>算力设备</td>>td>小幅流入</td><td>>AI服务器/液冷设备需求持续</td></tr>
<tr><td>10</td><td>>证券</td><td>>小幅流入流出</td><td>>护盘资金维稳</td></tr>
</table>
<p><strong>净流出方向：</strong>> 电新行业净流出148.18亿元（居首），有色金属、通信（CPO获利了结）等板块净流出居前。</p>
<p><strong>AI板块相对热度判断：</strong> &#x1F7E2; <strong>AI产业链（电子/半导体/存储）热度极高</strong>。电子板块以535亿元净流入高居全行业首位，存储芯片概念92亿元净流入，算力产业链106亿元净流入。AI方向在全市场中占据绝对资金主导地位。但CPO板块今日回调（资金流出通信板块），显示板块内部轮动特征明显，算力/存储接棒CPO成为日内最强主线。</p>

<h2>&#x4E94;&#x3001;关键异动个股</h2>
<ol>
<li><strong>京东方A（000725）&#x2EB06; 涨停</strong> —— 光学光电子龙头获主力资金净买入<strong>34.03亿元</strong>居A股首位。驱动因素：AI算力需求拉动高端显示面板，叠加消费电子备货旺季启动。带动整个光学光电子板块大涨。</li>
<li><strong>兆易创新（603986）&#x2EB06; 涨7.53%</strong>》 —— 存储芯片龙头获主力资金净流入<strong>>18.71亿元</strong>。驱动因素：三星HBM4E/HBM5技术突破引爆存储赛道情绪，公司作为国内存储芯片设计龙头直接受益HBM技术扩散效应。</li>
<li><strong>沪硅产业（688126）&#x2EB06; 涨14.12%</strong>> —— 半导体硅片材料龙头。驱动因素：存储芯片扩产带动上游硅片需求激增，国家大基金持股概念涨3.24%，公司作为大硅片国产替代核心标的受益明显。</li>
</ol>

<h2>&#x516D;&#x3001;特斯拉机器人概念股解析</h2>
<p><strong>Optimus量产进展更新：</strong> 特斯拉Optimus V3设计接近定型，预计<strong>2026年月-8月启动规模化量产</strong>，弗里蒙特工厂年产能目标100万台。比亚迪&quot;尧舜禹&quot;人形机器人2026年计划内部部署2万台，进一步验证了产业落地趋势。</p>
<p><strong>A股受益标的梳理：</strong></p>
<ul>
<li><strong>执行器总成：</strong> 拓普集团（直线/旋转执行器）、三花智控（机电执行器）</li>
<li><strong>减速器：</strong> 绿的谐波（谐波减速器龙头）、中大力德、双环传动</li>
<li><strong>电机：</strong> 汇川技术（伺服电机）、鸣志电器（空心杯电机）、兆威机电（微型传动）</li>
<li><strong>传感器：</strong> 奥比中光（3D视觉）、禾川科技（编码器）</li>
<li><strong>灵巧手：</strong> 斯菱智驱、北特科技</li>
<li><strong>结构件/外壳：</strong> 模塑科技（近期涨停，切入机器人外覆盖件业务）</li>
</ul>
<p><strong>最新催化：</strong> 比亚迪正式下场造人形机器人（代号&quot;尧舜禹&quot;），2026年部署2万台，成为继特斯拉之后又一重磅产业催化。日本航空在羽田机场试验人形机器人，摩根士丹利将2026年定义为行业&quot;首个真正的重新定价窗口&quot;。</p>

<h2>&#x4E03;&#x3001;总结与展望</h2>
<h3>今日市场总结</h3>
<ol>
<li><strong>A股低开收跌但结构性机会突出：</strong> 三大指数集体收跌但电子板块逆市净流入535亿元，AI方向内部轮动健康（CPO&#x2192;芯片存储），资金仍在积极寻找AI产业链机会。</li>
<li><strong>CPO技术性回调不改中长期逻辑：</strong> 英伟达CPO量产、1.6T光模块需求确定性极强强，回调是布局机会。</li>
<li><strong>存储芯片接棒成最强主线：</strong> HBM4E/HBM5技术突破+万亿美元市场空间间，兆易创新/沪硅产业等核心标的获资金追捧</li>
<li><strong>白银短期震荡中期看多：</strong> 贵金属受美元和地缘政治反复扰动，但工业需求和库存下降提供中长期支撑</li>
</ol>

<h3>盘后及次日（6月5日）展望</h3>
<ul>
<li><strong>美股今晚关注点：</strong> 盘前关注NVDA动向（昨日跌3%后能否企稳）和费城半导体指数走势。留意美伊谈判进展及美国初请失业金数据。</li>
<li><strong>A股明日（6月5日）展望：</strong>
<ul>
<li>CPO板块预计震荡企稳，关注获利回吐压力释放程度。英伟达CPO量产逻辑不变，短线回调或是中长期布局机会</li>
<li>芯片半导体有望延续强势，存储芯片主线+国产替代双重逻辑仍是重点</li>
<li>机器人板块关注比亚迪&quot;尧舜禹&quot;供应链新催化</li>
<li>AI板块整体大概率维持热点轮动格局，算力/芯片是短期最强方向，CPO中期布局窗口</li>
</ul></li>
<li><strong>贵金属：</strong> 关注今晚美国就业数据和地缘事件，白银72美元支撑位牢固，若美伊局势恶化可能触发避险反弹。</li>
</ul>

<hr/>
<p style="color:#999;font-size:13px;"><em>&#x26A0;&#xFE0F; 以上内容为市场信息汇总，仅供参考，不构成投资建议。AI板块部分个股近期涨幅巨大（中际旭创年内翻倍有余、京东方A今日涨停等），需关注高位震荡和获利了结风险。投资有风险，决策需谨慎。数据来源：Wind、财联社、东方财富、界面新闻等公开信息。</em></p>"""

entry["html"] = html_content

# Read existing monitors
with open(MONITORS_FILE, 'r', encoding='utf-8') as f:
    monitors = json.load(f)

# Check for duplicate id
existing_ids = [m["id"] for m in monitors]
if entry["id"] in existing_ids:
    print(f"Warning: duplicate id {entry['id']}, skipping")
    sys.exit(0)

# Append
monitors.append(entry)

# Write back
with open(MONITORS_FILE, 'w', encoding='utf-8') as f:
    json.dump(monitors, f, ensure_ascii=False, indent=2)

print(f"✅ Added entry {entry['id']} to monitors.json")
print(f"   Total monitors: {len(monitors)}")