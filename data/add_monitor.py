#!/usr/bin/env python3
import json, sys, os, re
from datetime import datetime

# Read existing monitors
data_path = os.path.join(os.path.dirname(__file__), "monitors.json")
with open(data_path, "r", encoding="utf-8") as f:
    monitors = json.load(f)

# Report content
report_html = """
<h1>AI板块实时监控报告 &amp; COMEX白银期货播报</h1>
<p><strong>报告时间：2026-06-10 12:52</strong></p>
<p>⚠️ 当前为A股午间休盘时段（11:30-13:00），上午盘已结束，下午盘13:00开市。以下为上午盘回顾及下午展望。</p>
<hr />

<h2>零、COMEX白银期货播报</h2>
<ul>
  <li><strong>最新价格：</strong>COMEX白银期货最新报约 <strong>68.65美元/盎司</strong>，日内涨+0.48%。6月9日纽约尾盘报68.585美元（昨结68.585美元）。盘中最高68.985美元，最低67.535美元。</li>
  <li><strong>日内涨跌幅：</strong>日内上涨约+0.48%，小幅反弹。此前自5月中旬近90美元高位持续回调，6月5日一度跌破71美元。</li>
  <li><strong>近期趋势判断：</strong>白银自5月近90美元高位回调后在<strong>67-72美元区间低位震荡</strong>。68美元为近期支撑，70美元为短期阻力。整体偏弱但下行速度放缓。</li>
  <li><strong>驱动因素简析：</strong>
    <ul>
      <li><strong>美元指数：</strong>交投于99附近，对贵金属形成压制</li>
      <li><strong>美联储政策：</strong>市场预期6月FOMC按兵不动，但就业数据强劲推迟降息预期</li>
      <li><strong>工业需求：</strong>光伏/新能源/AI硬件用银维持高位，世界白银协会预计2026年供需缺口约6316吨</li>
      <li><strong>库存支撑：</strong>COMEX白银库存处近十年低位提供中期支撑</li>
      <li>美国银行看年底冲击100美元，瑞银/汇丰目标75-80美元区间</li>
    </ul>
  </li>
</ul>
<hr />

<h2>一、大盘解读（6月10日午间回顾）</h2>
<ul>
  <li><strong>昨日（6月9日）回顾：</strong>A股三大指数强势反弹——沪指涨1.28%重返4000点，深证成指大涨3.02%，创业板指大涨3.93%。两市成交约2.64万亿元。通信设备、半导体、电子元器件涨幅居前。</li>
  <li><strong>今日早盘主力资金：</strong>主力资金净流入<strong>银行、能源金属、出版</strong>等板块。净流出<strong>电子、电新行业、通信</strong>等板块，其中<strong>电子板块净流出超212亿元</strong>。</li>
  <li><strong>个股方面：</strong><strong>海光信息大涨</strong>，主力资金净买入超13.64亿元位居首位。拓维信息、宗申动力、中微公司获主力净流入居前。<strong>沪电股份遭净卖出超19亿元</strong>，京东方A、中天科技、天孚通信资金净流出额居前。</li>
</ul>
<hr />

<h2>二、AI板块整体市场概览</h2>
<blockquote>今日AI板块上午盘呈现<strong>缩量分化调整</strong>态势。继6月9日AI板块大涨（人工智能ETF华富涨3.58%、科创人工智能ETF涨3.04%）后，今日AI板块整体高位整理<strong>，电子板块资金净流出超212亿元居全市场首位</strong>。CPO/光模块方向经历前期大涨后获利了结，存储芯片延续活跃。AI板块处于\"大涨后的技术性休整\"阶段。</blockquote>
<hr />

<h2>三、细分领域动态</h2>

<h3>算力板块</h3>
<ul>
  <li><strong>资金面：</strong>电子板块早盘主力资金净流出超212亿元居全市场首位。但<strong>海光信息逆势大涨，主力净买入超13.64亿元位居全市场首位</strong>，中微公司同步获净流入。</li>
  <li><strong>政策面：</strong>发改委/工信部联合发布AI新规划，2030年AI核心产业规模超5万亿元。大基金二期重点投资AI芯片/高端GPU/光芯片。</li>
  <li><strong>基本面：</strong>博通2026财年AI芯片销售额560亿美元，已向OpenAI交付芯片。英伟达GTC Taipei 2026全面布局AI全栈。中芯国际对2026年全年运营持乐观态度。6月9日科创芯片ETF国泰收涨5.48%，沪硅产业涨20%。</li>
  <li><strong>情绪面：</strong>中性偏谨慎。昨日大涨后今日获利了结压力较大，电子板块净流出212亿元显示短期资金趋向谨慎。但国产替代逻辑中期不变。</li>
</ul>

<h3>存储板块</h3>
<ul>
  <li><strong>资金面：</strong>存储芯片概念持续活跃。6月9日德明利、江波龙、大为股份、神工股份等同步上行。<strong>金太阳（GSUN.US）涨超12%</strong>。今日早盘兆易创新、澜起科技等延续活跃。</li>
  <li><strong>政策面：</strong>SK集团会长崔泰源称先进制程、HBM堆叠及高端封装设备存在严重供给约束，扩产周期长，未来数年供需紧平衡。黄仁勋指出Vera Rubin AI服务器显著提升单台HBM用量。</li>
  <li><strong>基本面：</strong><strong>黄仁勋：SK海力士到2030年将晶圆产能翻倍的计划还不够。</strong> 三大存储芯片制造商已通过认证，为英伟达Vera Rubin平台供应HBM4芯片。<strong>三星展示全球首款HBM5内存</strong>（2nm基础裸片+1c nm DRAM，预计2029-2031年推出）。HBM4E带宽突破4.0TB/s。</li>
  <li><strong>情绪面：</strong>偏积极。英伟达加持+黄仁勋对HBM产能缺口的高度评价，HBM高景气周期有望延续至2030年以后。存储从周期股向成长股切换预期强化。</li>
</ul>

<h3>机器人板块</h3>
<ul>
  <li><strong>资金面：</strong>6月9日机器人概念反复活跃。<strong>埃斯顿2连板</strong>，晋拓股份涨停，景业智能、腾亚精工、丰光精密涨超10%。6月10日早盘板块有所分化，但整体维持热度。</li>
  <li><strong>政策面：</strong><strong>工信部、国务院国资委联合启动2026年度人形机器人与具身智能实景实训专项行动。</strong> 到2026年底，人形机器人等重点产品在一批代表性场景中完成应用验证和常态部署，开启\"作业模式\"。推动人形机器人在<strong>医疗康养、安全生产、应急救援</strong>等场景常态化部署。至年底形成万台级规模落地能力。</li>
  <li><strong>基本面：</strong><strong>天工3.0将于2026年下半年开启规模化量产</strong>。搭载地瓜机器人旭日S600具身智能大算力芯片。比亚迪计划部署超2万台自研\"尧舜禹\"人形机器人。特斯拉Optimus V3预计7-8月量产，弗里蒙特厂年产100万台。</li>
  <li><strong>情绪面：</strong>乐观。两部门联合政策推动+天工3.0量产落地+特斯拉Optimus量产在即，三重催化。2026年为人形机器人量产元年共识强化。</li>
</ul>

<h3>CPO板块</h3>
<ul>
  <li><strong>资金面：</strong>今日CPO/光模块方向资金<strong>净流出明显</strong>。<strong>天孚通信资金净流出居前</strong>，与沪电股份、京东方A、中天科技等一起位列净流出前列。经历了6月3日板块暴涨（亨通光电两连板、长飞光纤/剑桥科技/中际旭创涨停）后，获利了结压力较大。</li>
  <li><strong>政策面：</strong>英伟达官宣Spectrum-X硅光CPO交换机全面量产，2026年Q4实现CPO规模化商用。2026年定义为CPO产业化元年。</li>
  <li><strong>基本面：</strong>Lightcounting报告指出<strong>2026年硅光模块市场份额将首次超过50%</strong>。2026年光模块进入1.6T大规模交付元年，出货量相较2025年增长约10倍，毛利率45%-60%。中际旭创800G全球市占率超42%，1.6T全球唯一批量供货。CPO市场规模2026年预计达80亿美元（同比增长430%）。富士康旗下讯芯投资5.68亿元在越南扩充CPO产能，年产能450万片。</li>
  <li><strong>情绪面：</strong>短期回调偏谨慎，但中长期极度乐观。硅光/CPO方向产业趋势确定性强。短期光模块龙头需消化获利盘，光纤/DCI方向仍有性价比。</li>
</ul>
<hr />

<h2>四、主流净流入板块监控</h2>
<h3>今日（6月10日）早盘主力资金净流入排行</h3>
<ol>
  <li><strong>银行</strong>——主力净流入居前（防御性配置+高股息逻辑）</li>
  <li><strong>能源金属</strong>——主力净流入居前（锂矿/有色资源反弹）</li>
  <li><strong>出版</strong>——主力净流入居前（AI+文化数字化）</li>
</ol>
<p><strong>主力资金净流出板块：</strong></p>
<ol>
  <li><strong>电子板块</strong>——净流出超<strong>212亿元</strong>居全市场首位</li>
  <li><strong>电新行业</strong>——净流出居前</li>
  <li><strong>通信</strong>——净流出居前（CPO/光纤获利了结）</li>
</ol>
<p><strong>AI板块相对热度：</strong> 🔴 <strong>短期降温明显</strong>。电子板块净流出212亿元居全市场首位，通信板块同样净流出，显示AI板块经历6月初强势上涨后进入技术性整理。但海光信息获主力净买入13.64亿元居个股首位，说明AI板块并非全面退潮，而是<strong>从全面普涨转向精选核心标的</strong>。</p>
<hr />

<h2>五、关键异动个股</h2>
<ol>
  <li><strong>海光信息（688041）⬆ 大涨，主力净买入13.64亿元居全市场首位</strong>——国产算力芯片龙头，受益于国产替代逻辑持续强化。博通560亿AI芯片指引+中芯国际乐观经营展望为板块提供支撑。</li>
  <li><strong>沪电股份（002463）⬇ 遭净卖出超19亿元，居两市净流出首位</strong>——PCB概念股高位获利了结。昨日（6月9日）AI概念股普涨后今日获利回吐压力显著。</li>
  <li><strong>中天科技（600522）⬆ 6月8日涨停，今日资金净流出</strong>——中天科技战略布局AI算力+海上风电+特高压，6月8日涨停后今日资金获利了结。公司攻克空芯光纤等卡脖子技术，AI配套光纤产品已批量供货头部客户。</li>
</ol>
<hr />

<h2>六、特斯拉机器人概念股解析</h2>
<p><strong>Optimus量产进展：</strong> V3设计接近定型，预计<strong>2026年7-8月启动规模化量产</strong>。弗里蒙特工厂设计年产能<strong>100万台</strong>。</p>

<p><strong>A股产业链受益标的：</strong></p>
<ul>
  <li><strong>减速器：</strong>绿的谐波（谐波减速器龙头）、中大力德（已批量供货人形机器人客户）、双环传动</li>
  <li><strong>执行器：</strong>拓普集团（直线/旋转执行器）、三花智控（机电执行器）、肇民科技</li>
  <li><strong>电机：</strong>汇川技术（伺服电机）、鸣志电器、兆威机电</li>
  <li><strong>传感器：</strong>奥比中光（3D视觉传感器）、禾川科技</li>
  <li><strong>灵巧手/结构件：</strong>斯菱智驱、北特科技、丰光精密</li>
  <li><strong>整机/集成：</strong>埃斯顿、中控技术、昊志机电</li>
</ul>

<p><strong>最新催化：</strong></p>
<ul>
  <li>两部门联合启动2026年度人形机器人与具身智能实景实训专项行动</li>
  <li>天工3.0将于2026年下半年开启规模化量产交付</li>
  <li>比亚迪计划部署超2万台自研\"尧舜禹\"人形机器人</li>
  <li>特斯拉Optimus V3预计7-8月启动量产</li>
  <li>万元级消费机器人\"小布米\"定价9998元</li>
</ul>

<p>国金证券指出，2026年是人形机器人产业从概念走向现实的关键时期。两部门政策明确提出带动形成<strong>万台级规模落地能力</strong>。</p>
<hr />

<h2>七、总结与展望</h2>

<h3>当前市场总结</h3>
<ol>
  <li><strong>AI板块短期高位整理：</strong>昨日大涨后今日早盘电子板块资金净流出212亿元，CPO/通信方向获利了结，属于正常技术性调整。</li>
  <li><strong>存储/机器人维持热度：</strong>存储芯片受黄仁勋HBM产能紧缺表态持续受益；机器人受两部门联合政策+天工3.0量产落地双重催化。</li>
  <li><strong>海光信息逆势吸金13.64亿元：</strong>显示市场对国产算力龙头的稀缺性高度认可，核心标的不缺买盘。</li>
  <li><strong>白银低位震荡：</strong>68-69美元区间窄幅整理，关注本周CPI/PPI数据对降息预期的引导。</li>
  <li><strong>资金向防御板块轮动：</strong>银行/能源金属等板块获主力净流入，市场整体风险偏好略有降低。</li>
</ol>

<h3>下午盘展望</h3>
<ul>
  <li><strong>AI板块：</strong>下午关注电子板块资金流出是否收窄。海光信息能否持续领涨有望带动算力方向情绪修复。CPO/光模块方向短期获利盘消化后或迎反弹。</li>
  <li><strong>机器人：</strong>两部门政策催化+天工3.0量化消息持续发酵，下午机器人概念有望维持活跃。</li>
  <li><strong>存储：</strong>HBM4E→HBM5技术路线清晰，存储芯片板块中期趋势向好。</li>
  <li><strong>白银：</strong>关注美元指数走势及本周美国通胀数据。68美元为短期支撑，若跌破则看67美元。</li>
  <li><strong>宏观：</strong>关注下午是否有重要政策或消息面催化。</li>
</ol>

<blockquote>⚠️ <strong>风险提示：</strong>以上内容为市场信息汇总，不构成投资建议。AI板块短期涨幅较大面临获利了结压力。CPO/通信方向需注意高位品种调整风险。投资有风险，决策需谨慎。</blockquote>
<hr />
<p><em>数据来源：Wind、东方财富、同花顺、证券时报、财联社、IT之家、Lightcounting、腾讯新闻、证券之星</em></p>
"""

new_entry = {
    "id": "mon-20260610-1252",
    "date": "2026-06-10 12:52",
    "title": "AI板块午间监控 & COMEX白银播报 — 电子板块净流出212亿 海光信息逆势吸金13.64亿",
    "tags": ["AI板块", "白银", "午间监控", "算力", "存储", "机器人", "CPO", "海光信息"],
    "summary": "AI板块高位整理获利了结，电子板块净流出212亿；海光信息逆势大涨吸金13.64亿居首；两部门启动人形机器人实训专项行动",
    "html": report_html
}

# Check for duplicate id
existing_ids = set(m.get("id") for m in monitors)
if new_entry["id"] in existing_ids:
    print(f"ERROR: Duplicate id {new_entry['id']} found!")
    sys.exit(1)

monitors.append(new_entry)

with open(data_path, "w", encoding="utf-8") as f:
    json.dump(monitors, f, ensure_ascii=False, indent=2)

print(f"Successfully added entry {new_entry['id']}")
print(f"Total entries: {len(monitors)}")