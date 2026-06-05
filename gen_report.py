#!/usr/bin/env python3
import json, datetime, os, subprocess, sys

now = datetime.datetime(2026, 6, 5, 16, 12)
ts = now.strftime("%Y-%m-%d %H:%M")
id_str = now.strftime("mon-%Y%m%d-%H%M")

html_content = """<h1>AI板块收盘监控报告 &amp; COMEX白银期货播报</h1>
<p><strong>【""" + ts + """】</strong></p>
<p>⚠️ <strong>A股今日（6月5日，周五）已收盘。</strong> 以下为全天盘面回顾、盘后消息及下周展望。</p>
<hr />

<h2>零、COMEX白银期货播报</h2>
<ul>
  <li><strong>最新价格：</strong>COMEX白银期货报约 <strong>71.75美元/盎司</strong>，日内跌 <strong>超3%</strong>。周四纽约尾盘报74.16美元（涨1.69%），今日亚盘失守73美元关口后加速下跌。现货白银同步跌超2%报72.29美元/盎司。</li>
  <li><strong>日内涨跌幅：</strong>自74.16美元开盘持续下挫，跌破73美元后加速至71.75美元附近，日内跌幅超3%。</li>
  <li><strong>近期趋势：</strong>白银自5月中旬近90美元/盎司高位持续回调，跌破73美元关键支撑位后加速下行，目前在<strong>71-75美元区间震荡偏弱</strong>。72美元支撑已失守，下一关键支撑在70美元整数关口。</li>
  <li><strong>驱动因素：</strong>美元指数企稳于99.2附近压制贵金属；今晚<strong>20:30美国5月非农数据</strong>公布前市场偏谨慎；ADP就业超预期强化鹰派预期；光伏/AI用银需求维持高位（供需缺口6316吨）；COMEX库存处近十年低位提供中期支撑；机构观点分化（美国银行看100美元，瑞银看75-80美元）。</li>
</ul>
<hr />

<h2>一、大盘解读（6月5日收盘回顾）</h2>
<ul>
  <li><strong>三大指数集体收跌，指数与个股背离：</strong>今日A股冲高回落。全市场成交<strong>3.10万亿元</strong>，较上日放量3216亿元。<strong>超3200只个股上涨</strong>，结构性行情延续——指数跌但个股涨多跌少。</li>
  <li><strong>收盘数据：</strong><strong>上证指数</strong>报4027.74点（跌0.74%）；<strong>深证成指</strong>跌2.21%；<strong>创业板指</strong>跌3.20%；<strong>北证50</strong>涨5.59%（逆市大涨）；<strong>科创50</strong>跌4.01%（半导体/算力大幅回调）。</li>
  <li><strong>外围冲击：</strong>博通Q3指引低于预期，股价暴跌12.59%。韩国综指跌超6%触发熔断。A股半导体/算力板块受情绪传导。</li>
  <li><strong>盘面特征：</strong><strong>机器人/玻璃基板/光纤三大赛道逆势走强</strong>。电力、半导体、贵金属、存储芯片领跌。资金从大盘权重涌向科技小盘和高端制造。</li>
</ul>
<hr />

<h2>二、AI板块整体市场概览</h2>
<blockquote>今日AI板块呈现<strong>极端结构性分化</strong>。机器人板块全线爆发（绿的谐波20CM涨停），CPO/DCI光纤方向大单持续（烽火通信净买入21.89亿居首），但算力芯片/存储/半导体<strong>集体深度回调</strong>。整体来看，<strong>AI板块"算力硬件→机器人/应用"的轮动正在加速</strong>。</blockquote>
<hr />

<h2>三、细分领域动态</h2>

<h3>算力板块</h3>
<ul>
  <li><strong>资金面：</strong>电子板块主力净流出<strong>323.22亿元</strong>居全市场首位。<strong>中际旭创遭净卖出46.38亿元</strong>居两市个股净流出第一；胜宏科技、工业富联、兆易创新跟跌。</li>
  <li><strong>政策面：</strong>发改委/工信部发布《新一代人工智能发展规划(2026-2030)》，2030年AI核心产业规模超5万亿。"东数西算"2026年投资超2000亿元。</li>
  <li><strong>基本面：</strong><strong>博通利空</strong>——2026财年AI芯片总销售额560亿美元，但Q3指引160亿远低于172亿预期。英伟达发布Cosmos 3全模态物理AI模型。意法半导体6月28日涨价。</li>
  <li><strong>情绪面：</strong>偏谨慎。博通利空+美股回调双重压制，科创50暴跌4%。"国产替代加速"叙事仍获部分资金认可。</li>
</ul>

<h3>存储板块</h3>
<ul>
  <li><strong>资金面：</strong>存储芯片板块跌幅居前。兆易创新遭净卖出，江波龙、德明利跟跌。受SK海力士暴跌超8%情绪拖累。</li>
  <li><strong>政策面：</strong>SK海力士计划五年内晶圆产能翻番，产能瓶颈持续到2030年。</li>
  <li><strong>基本面：</strong><strong>三星交付全球首批HBM4E样品</strong>（带宽1.5TB/s，12层堆叠），展示<strong>HBM5原型</strong>。TrendForce预计Q2 DRAM合约价环比增长45%-50%。</li>
  <li><strong>情绪面：</strong>短期偏弱，但HBM技术迭代加速。回调或为中长线布局窗口。</li>
</ul>

<h3>机器人板块【今日全市场最强主线】</h3>
<ul>
  <li><strong>资金面：</strong><strong>逆势爆发！</strong>机器人ETF景顺涨<strong>5.47%</strong>领涨全市场ETF，富国涨5.38%，易方达涨5.36%。主力净流入<strong>12.63亿元</strong>。北证50涨5.59%（大量机器人标的集中在此）。</li>
  <li><strong>政策面：</strong><strong>华为云发布"具身智能专区"+CloudRobo平台</strong>月内公测。机器人高峰论坛今明举办。宇树科技73天闪电过会。</li>
  <li><strong>基本面：</strong><strong>绿的谐波20CM涨停创新高！</strong>中大力德4天2板，丰光精密30CM涨停。比亚迪"尧舜禹"部署2万台。特斯拉Optimus V3 7-8月量产。万元消费机器人定价9998元。</li>
  <li><strong>情绪面：</strong><strong>极度乐观！</strong>华为+宇树+比亚迪+特斯拉+消费机器人+论坛六重催化共振。2026年确认为人形机器人量产元年。</li>
</ul>

<h3>CPO板块</h3>
<ul>
  <li><strong>资金面：</strong>板块内分化剧烈。<strong>烽火通信净买入21.89亿元居两市首位</strong>，中兴通讯净买入居前。但<strong>中际旭创遭净卖出46.38亿元</strong>居两市净流出首位。</li>
  <li><strong>政策面：</strong>英伟达Spectrum-X硅光CPO交换机全面量产，2026年Q4规模化商用。</li>
  <li><strong>基本面：</strong>中际旭创800G全球市占率超42%，1.6T全球唯一批量供货，订单覆盖至2028年。今日跌超7%，成交额破580亿元。</li>
  <li><strong>情绪面：</strong>中性。光纤/DCI方向持续获资金买入，但光模块龙头短线获利了结。中长期趋势确定性强。</li>
</ul>
<hr />

<h2>四、主流净流入板块监控（6月5日）</h2>
<p><strong>主力资金净流入板块TOP10：</strong></p>
<ol>
  <li><strong>机械设备</strong> —— 净流入26.47亿元（机器人/自动化催化）</li>
  <li><strong>国防军工</strong> —— 净流入23.00亿元（商业航天利好）</li>
  <li><strong>航天装备</strong> —— 净流入13.84亿元（商业航天政策催化）</li>
  <li><strong>自动化设备</strong> —— 净流入13.63亿元（机器人/工业自动化）</li>
  <li><strong>商贸零售</strong> —— 净流入13.56亿元（消费政策预期）</li>
  <li><strong>机器人</strong> —— 净流入12.63亿元（华为+高峰论坛+特斯拉量产）</li>
  <li><strong>被动元件</strong> —— 净流入12.32亿元（AI硬件需求驱动）</li>
  <li><strong>通用设备</strong> —— 净流入11.39亿元（机器人产业链扩散）</li>
  <li><strong>一般零售</strong> —— 净流入10.71亿元（消费政策预期）</li>
  <li><strong>通信/DCI</strong> —— 烽火通信21.89亿净买入居个股首位</li>
</ol>
<p><strong>AI板块相对热度：</strong> 🟢 <strong>极高但方向切换剧烈</strong>。大盘主力整体净流出486亿元，但有限资金高度集中在机器人/高端制造方向。<strong>机械设备+机器人+自动化设备+通用设备合计净流入超64亿元</strong>。但<strong>电子板块净流出323.22亿元</strong>（半导体/CPO龙头获利了结），显示AI板块内部从算力硬件向机器人方向大迁徙。</p>
<hr />

<h2>五、关键异动个股</h2>
<ol>
  <li><strong>绿的谐波（688017）20CM涨停创历史新高</strong>——华为具身智能+高峰论坛+消费机器人+特斯拉Quantus量产四重催化，减速器龙头。</li>
  <li><strong>烽火通信（600498）净买入21.89亿元居两市首位</strong>——DCI+光纤通信龙头，英伟达CPO量产直接催化。</li>
  <li><strong>中际旭创（300308）遭净卖出46.38亿元居两市净流出首位，跌超7%</strong>——CPO龙头短线获利了结压力集中释放，成交破580亿元。1.6T全球独占供货地位不变，中长期无忧。</li>
</ol>
<hr />

<h2>六、特斯拉机器人概念股解析</h2>
<p><strong>Optimus量产进展：</strong> V3设计接近定型，预计7-8月启动规模化量产。弗里蒙特工厂年产100万台。</p>
<p><strong>A股产业链受益标的：</strong></p>
<ul>
  <li><strong>减速器：</strong><strong>绿的谐波</strong>（20CM涨停创新高）、中大力德（4天2板）、双环传动</li>
  <li><strong>执行器：</strong>拓普集团、三花智控、肇民科技</li>
  <li><strong>电机：</strong>汇川技术、鸣志电器、兆威机电</li>
  <li><strong>传感器：</strong>奥比中光、禾川科技</li>
  <li><strong>灵巧手：</strong>斯菱智驱、北特科技、丰光精密（30CM涨停）</li>
  <li><strong>整机：</strong>埃斯顿、科力尔（涨停）、光洋股份（涨停）</li>
</ul>
<p><strong>六重催化：</strong>华为入局具身智能+宇树过会+比亚迪部署2万台+特斯拉量产+万元机器人+机器人论坛。2026年为人形机器人量产元年。</p>
<hr />

<h2>七、总结与展望</h2>
<h3>当前市场总结</h3>
<ol>
  <li><strong>🔥 机器人板块今日全面爆发：</strong>绿的谐波20CM涨停，ETF批量涨超5%，六重催化共振</li>
  <li><strong>⚠️ 算力芯片/存储集体回调：</strong>博通利空持续发酵，中际旭创遭净卖出46亿，电子板块净流出323亿元</li>
  <li><strong>🔄 AI内部极致轮动：</strong>"算力硬件→机器人/应用"格局清晰，光纤/DCI方向持续获资金买入</li>
  <li><strong>💵 白银深度回调破73美元：</strong>关注今晚20:30非农数据</li>
</ol>
<h3>下周展望（6月8日-12日）</h3>
<ul>
  <li><strong>机器人：</strong>短期情绪极强，下周初有望延续。关注华为具身智能公测时间表+论坛成果</li>
  <li><strong>算力芯片/CPO：</strong>中际旭创调整压力需消化，但基本面不变。光纤/DCI方向性价比更高</li>
  <li><strong>存储：</strong>回调为中长期布局窗口。HBM4E/HBM5技术迭代确定</li>
  <li><strong>白银：</strong>非农若超预期或下探70美元，不及预期则反弹73美元上方</li>
</ul>
<blockquote>⚠️ <strong>风险提示：</strong>以上为市场信息汇总，不构成投资建议。机器人板块涨幅极大需防回调。CPO龙头巨额资金出逃需警惕连锁反应。投资有风险，决策需谨慎。</blockquote>
<p><em>数据来源：Wind、东方财富、同花顺、证券时报、财联社、Lightcounting、高盛、中信证券</em></p>"""

entry = {
    "id": id_str,
    "date": ts,
    "title": "AI板块收盘监控 & COMEX白银播报 — 机器人爆发领涨 A股独立行情 收盘解析",
    "tags": ["AI板块", "白银", "收盘回顾", "机器人", "CPO", "算力", "存储", "博通", "非农"],
    "summary": "机器人全线爆发！绿的谐波20CM涨停，北证50涨5.59%；算力/存储大幅回调；白银跌破73美元",
    "html": html_content
}

# Read existing data
data_path = "/root/.joyclaw/workspace-er-ji-shi-chang-yan-jiu-yuan-vxu6-d552a7b0dc9d-81c90a43/site/data/monitors.json"
with open(data_path, 'r', encoding='utf-8') as f:
    monitors = json.load(f)

# Check for duplicates
existing_ids = [m["id"] for m in monitors]
if id_str not in existing_ids:
    monitors.append(entry)
    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(monitors, f, ensure_ascii=False, indent=2)
    print(f"Added entry {id_str}")
else:
    print(f"Entry {id_str} already exists, skipping")

# Build and push
os.chdir("/root/.joyclaw/workspace-er-ji-shi-chang-yan-jiu-yuan-vxu6-d552a7b0dc9d-81c90a43/site")
result = subprocess.run(["python3", "build_site.py", "--push"], capture_output=True, text=True)
print(result.stdout[-2000:] if len(result.stdout) > 2000 else result.stdout)
if result.stderr[-2000:] if len(result.stderr) > 2000 else result.stderr:
    print("STDERR:", result.stderr[-2000:])