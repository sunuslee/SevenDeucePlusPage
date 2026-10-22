from pathlib import Path
from html import escape
import json
import xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1]/'build'/'production'
BASE='https://72plus.pro/'
GUIDES={
'session-tracking':{
'zh':('德州扑克盈亏怎么记录？牌局记录与收益复盘指南','德州扑克盈亏记录：从单场结果到长期复盘','每场牌局先把买入、追加买入和带出金额记清楚，再看长期变化。',[
('先统一记录口径','每次坐下前建立一场记录，保存日期、场地、级别和货币。追加买入也计入本场总买入，离桌时再填写带出金额。现金局与锦标赛最好分开查看；不同货币不要未经换算直接相加。'),
('单场盈亏怎么算？','单场盈亏 = 带出金额 − 总买入。例如先买入 1,000，追加 500，最后带出 1,800，本场盈利就是 300。交通、小费等额外费用是否计入，要保持一致；如果单独记录，回顾净收益时再扣除，避免重复计算。'),
('收益曲线能告诉你什么？','按时间累加每场盈亏，可以看到累计结果的变化。短期输赢受波动影响，不能仅凭几场盈利判断技术进步。结合牌局环境、级别和记录完整性一起看，不要把收益曲线当成未来收益承诺。'),
('把结果与决策分开复盘','输钱的牌不一定打错，赢钱的牌也不一定打得好。挑出让你犹豫的手牌，记下位置、有效筹码、行动和当时对对手的判断。先按当时掌握的信息分析，再回看最终结果。'),
('在德益记里怎么做？','使用盈利记录保存买入、带出与结果，通过历史记录和收益曲线回顾。值得研究的手牌可用 Insights 录入并辅助复盘；AI 反馈可能有误，应核对其假设。PRO PLAY 则帮助你查看真实选手在具体牌局中的行动。')]),
'en':('How to Track Poker Session Results | SevenDeucePlus','How to track poker session results','Start with consistent records. Use the bigger picture to ask better questions about your game.',[
('Record the same things every session','Keep the date, venue, stakes and currency with each session. Include every rebuy in total buy-ins, then record the amount you leave with. Separate cash games from tournaments when comparing results. Do not add different currencies together without a consistent conversion method.'),
('Calculate session profit correctly','Session profit equals cash-out minus total buy-ins. If you buy in for 1,000, add another 500 and cash out for 1,800, your result is +300. Decide how to treat tips, travel and other expenses. If tracked separately, account for them when calculating net profit without counting them twice.'),
('Read the graph with context','A cumulative profit graph adds each session’s result to the previous total. It shows what happened, not what you are guaranteed to win next. A short winning stretch is not proof of an edge. Consider the sample, stakes and game conditions before drawing conclusions.'),
('Separate decisions from outcomes','A losing hand can be well played; a winning hand can contain mistakes. Save the hands that left you uncertain, including positions, effective stacks, action and your reads at the time. Review the decision using what was known then, before considering the final outcome.'),
('Use SevenDeucePlus to keep the records together','Log buy-ins, cash-outs and results, then revisit your session history and profit charts. Enter individual hands in Insights for AI-assisted review, checking its assumptions and calculations. PRO PLAY lets you explore actions from real player samples, with links back to the source video.')])},
'home-game-settlement':{
'zh':('德州扑克朋友局如何结算？买入、带出与记分板指南','朋友局结算：先对平，再转账','把每个人的买入和带出放在同一张表里，结束时逐项核对。',[
('开始前统一单位与记录人','先约定筹码对应的金额或积分单位，并确定谁负责记录。每位玩家每次买入都当场登记，不要依赖散场时的记忆。追加买入、提前离场也应及时更新。'),
('逐个计算净结果','每位玩家的净结果 = 带出 − 累计买入。例如小李买入 1,000、带出 1,400，结果为 +400；小王买入 1,000、带出 600，结果为 −400。这两个结果正好抵消。这里的结果是账目记录，不代表已经发生了转账。'),
('先检查整桌是否平衡','在没有抽水或其他扣款的封闭筹码账目中，总买入应等于总带出，所有人的净结果之和应为零。如果不一致，先查漏记的追加买入、提前离场、筹码清点或单位错误。有明确费用时，先记录费用并说明由谁承担。'),
('确认后分享，再执行结算','把最终表发给同桌玩家确认，区分账面净结果与实际已支付金额。转账由玩家自行完成，并在需要时另外保存支付记录，避免重复付款。不要在金额尚未对平时猜测差额归属。'),
('用德益记减少重复录入','记分板集中展示每位玩家的买入、带出和净结果，帮助核对并分享结算。常见牌友可以提前保存到 Friends，留下头像、标签与备注，下次组局时直接加入记分板。App 不代收、保管或转移玩家资金。')]),
'en':('How to Settle a Home Poker Game | SevenDeucePlus','How to settle a home poker game','Keep one clear record of buy-ins and cash-outs, then reconcile the table before anyone pays.',[
('Agree on units and keep one record','Decide what each chip or point represents and who records the table. Enter each buy-in when it happens, including rebuys. Record players who leave early immediately instead of trying to reconstruct their numbers at the end of the night.'),
('Calculate each player’s net result','Net result equals cash-out minus total buy-ins. A player who buys in for 1,000 and leaves with 1,400 is +400. Another who buys in for 1,000 and leaves with 600 is −400. Those results balance. A net result is an accounting entry, not evidence that a payment has been made.'),
('Reconcile the whole table first','For a closed chip ledger with no deductions, total buy-ins should equal total cash-outs and player net results should sum to zero. If they do not, check missing rebuys, early departures, chip counts and inconsistent units. Account for any agreed expenses explicitly rather than hiding them in a player’s result.'),
('Confirm, share and settle','Share the final scoreboard so everyone can check their numbers. Keep the final net result separate from payments already made. Players handle payments themselves; retain payment records where needed to avoid paying twice. Resolve an imbalance before deciding who owes the difference.'),
('Keep the table organized with SevenDeucePlus','The scoreboard brings buy-ins, cash-outs and net results together for checking and sharing. Friends stores regular players’ profiles, tags and notes so you can add them to the next game without repeated typing. The app does not collect, hold or transfer player funds.')])}}

from feature_content import FEATURES, SCREENSHOTS
GUIDES.update(FEATURES)
GUIDES['session-tracking']['zh'][3].append(('可以用表格记录吗？', '可以。记录日期、总买入、带出和净结果就能开始；每次都使用同一套口径。需要在手机上持续保存牌局、浏览收益曲线并把手牌复盘放在一起时，再使用德益记这样的记录工具。'))
GUIDES['session-tracking']['en'][3].append(('Can I start with a spreadsheet?', 'Yes. Start with date, total buy-ins, cash-out and net result, using consistent definitions. A session tracker such as SevenDeucePlus is useful when you want to keep records on your phone, browse profit charts and revisit hands alongside your results.'))
GUIDES['home-game-settlement']['zh'][3].append(('多人局怎么算谁付给谁？', '例如三位玩家的净结果为 +300、−100、−200，后两位分别向第一位支付 100 和 200 即可对平。这只是账目示例；先确认是否有人已提前支付，避免重复结算。'))
GUIDES['home-game-settlement']['en'][3].append(('Who pays whom in a three-player example?', 'If the net results are +300, −100 and −200, the two losing players can pay 100 and 200 respectively to the winning player. First check whether anyone has already paid part of their balance so you do not settle the same amount twice.'))


def enhance():
 urls=[BASE,BASE+'en/']
 for lang,path in [('zh',R/'index.html'),('en',R/'en/index.html')]:
  en=lang=='en';pre='../' if en else '';s=path.read_text()
  title='Poker Session Tracker & Home Game Scoreboard | SevenDeucePlus' if en else '德益记 SevenDeucePlus｜德州扑克盈亏记录、记分板结算与复盘 App'
  desc='Track poker session results, settle home games and review hands on iPhone and iPad. Explore real pro hands with PRO PLAY and AI-assisted review with Insights.' if en else '德益记是支持中文和英文的德州扑克记录 App，提供盈亏曲线、朋友局记分板与结算、PRO PLAY 职业选手真实手牌、Insights AI 辅助复盘和牌友管理。适用于 iPhone 与 iPad。'
  import re
  s=re.sub(r'<title>.*?</title>',f'<title>{escape(title)}</title>',s)
  s=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{escape(desc)}">',s)
  s=re.sub(r'<meta property="og:description" content="[^"]*">',f'<meta property="og:description" content="{escape(desc)}">',s)
  if not en:
   s=re.sub(r'assets/([\w-]+)\.webp',r'assets/zh/\1.webp',s)
   s=s.replace('页面使用当前客户端真实截图与示例数据；截图为英文界面，App 支持中文和英文。','页面使用当前中文客户端的真实截图与示例数据，App 同时支持中文和英文。')
   s=s.replace('Profit tracking in SevenDeucePlus','德益记德州扑克盈亏记录与收益曲线').replace('PRO PLAY range matrix','PRO PLAY 职业选手起手牌范围矩阵').replace('Insights action entry','Insights 手动录入行动')
  else:s=s.replace('Actual current-client screenshots with sample data. Screens shown in English; the app supports English and Chinese.','Actual English app screenshots with sample data. The app supports English and Chinese.')
  schema={'@context':'https://schema.org','@graph':[{'@type':'SoftwareApplication','@id':BASE+'#app','name':'SevenDeucePlus','alternateName':'德益记','url':BASE+('en/' if en else ''),'applicationCategory':'SportsApplication','operatingSystem':'iOS, iPadOS','inLanguage':['en','zh-Hans'],'description':desc,'downloadUrl':'https://apps.apple.com/app/id6460033253','image':BASE+'img/appIcon.png','offers':{'@type':'Offer','price':'0','priceCurrency':'USD','description':'Free download with optional in-app purchases' if en else '免费下载，含可选 App 内购买'}},{'@type':'WebPage','@id':BASE+('en/' if en else '')+'#webpage','url':BASE+('en/' if en else ''),'name':title,'inLanguage':'en' if en else 'zh-Hans','about':{'@id':BASE+'#app'}}]}
  # No invented ratings/reviews; schema describes the app, not guaranteed rich-result eligibility.
  extra=f'<meta name="robots" content="index,follow,max-image-preview:large"><meta name="apple-itunes-app" content="app-id=6460033253"><meta property="og:locale" content="{"en_US" if en else "zh_CN"}"><meta property="og:locale:alternate" content="{"zh_CN" if en else "en_US"}"><meta name="twitter:card" content="summary"><meta name="twitter:title" content="{escape(title)}"><meta name="twitter:description" content="{escape(desc)}"><meta name="twitter:image" content="{BASE}img/appIcon.png"><link rel="sitemap" type="application/xml" href="{pre}sitemap.xml"><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script>'
  s=s.replace('</head>',extra+'<meta name="google-site-verification" content="q2xwd1uOt4LnEns07kvi5OlC2WJ-DHVE-IfghfIUI70"><meta name="google-site-verification" content="YgwjKXx70NA7AdtpxjcjWVmbbYKTZO_Q79WKJ7KUul0">'+'</head>')
  cards=''.join(f'<a class="guide-card" href="guides/{slug}/"><h3>{escape(data[lang][1])}</h3><p>{escape(data[lang][2])}</p><span>{"Read the guide" if en else "阅读指南"} ↗</span></a>' for slug,data in GUIDES.items())
  section=f'<section class="guides" id="guides"><p class="eyebrow">{"POKER RECORDS & HOME GAMES" if en else "牌局记录与朋友局指南"}</p><h2>{"Practical guides for your next game" if en else "从记录方法开始，让每次结算更清楚"}</h2><div class="guide-grid">{cards}</div></section>'
  s=s.replace('<section id="pricing"',section+'<section id="pricing"')
  path.write_text(s)
  for slug,data in GUIDES.items():
   title,heading,summary,blocks=data[lang];rel=('en/' if en else '')+'guides/'+slug+'/'
   url=BASE+rel;urls.append(url);back='../../';asset='../../../' if en else '../../';other=BASE+('guides/' if en else 'en/guides/')+slug+'/'
   content=''.join(f'<section><h2>{escape(h)}</h2><p>{escape(b)}</p></section>' for h,b in blocks)
   shots=''.join(f'<figure><img src="{asset}assets/{"" if en else "zh/"}{name}.webp" alt="{escape(alt_en if en else alt_zh)}" width="603" height="1311" loading="lazy" decoding="async"><figcaption>{escape(alt_en if en else alt_zh)}</figcaption></figure>' for name,alt_zh,alt_en in SCREENSHOTS[slug])
   content=f'<div class="guide-screens">{shots}</div>'+content
   related_links=''.join(f'<li><a class="text-link" href="../{key}/">{escape(value[lang][1])} →</a></li>' for key,value in GUIDES.items() if key!=slug)
   related_html=f'<section><h2>{"Related guides" if en else "继续阅读"}</h2><ul>{related_links}</ul></section>'
   html=f'''<!doctype html><html lang="{'en' if en else 'zh-Hans'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)}</title><meta name="description" content="{escape(summary)}"><meta name="robots" content="index,follow"><link rel="canonical" href="{url}"><link rel="alternate" hreflang="zh-Hans" href="{BASE}guides/{slug}/"><link rel="alternate" hreflang="en" href="{BASE}en/guides/{slug}/"><link rel="alternate" hreflang="x-default" href="{BASE}en/guides/{slug}/"><link rel="stylesheet" href="{asset}assets/site.css"><meta property="og:title" content="{escape(title)}"><meta property="og:description" content="{escape(summary)}"><meta property="og:url" content="{url}"><meta property="og:type" content="article"></head><body><header><a class="brand" href="{back}">SevenDeucePlus · 德益记</a><nav><a href="{back}">{'App homepage' if en else 'App 主页'}</a><a href="{other}" class="language">{'简体中文' if en else 'English'} ↗</a></nav></header><main class="guide-body"><p class="eyebrow">{'PRACTICAL POKER GUIDE' if en else '实用牌局指南'}</p><h1>{escape(heading)}</h1><p class="intro">{escape(summary)}</p>{content}<aside class="guide-next"><h2>{'Keep your next game organized' if en else '把下一场牌局记录清楚'}</h2><p><a class="text-link" href="{back}">{'Explore SevenDeucePlus' if en else '了解德益记的功能'} ↗</a></p><a href="https://apps.apple.com/app/id6460033253" class="button">{'Get it on the App Store' if en else '前往 App Store'} ↗</a><p class="small">{'Free download · In-app purchases' if en else '免费下载 · 含 App 内购买'}</p></aside>{related_html}</main><footer><span>© 2026 SevenDeucePlus</span><a href="mailto:dmoment+sdp@gmail.com">{'Support & feedback' if en else '支持与反馈'}</a></footer></body></html>'''
   dest=R/rel;dest.mkdir(parents=True,exist_ok=True);(dest/'index.html').write_text(html)
 ns='http://www.sitemaps.org/schemas/sitemap/0.9';ET.register_namespace('',ns);root=ET.Element('{'+ns+'}urlset')
 for url in urls:
  node=ET.SubElement(root,'{'+ns+'}url');ET.SubElement(node,'{'+ns+'}loc').text=url;ET.SubElement(node,'{'+ns+'}lastmod').text='2026-10-22'
 ET.ElementTree(root).write(R/'sitemap.xml',encoding='utf-8',xml_declaration=True)
 # Plain-text alternative supported by Google; generated from the same canonical URLs.
 (R/'sitemap.txt').write_text('\n'.join(urls)+'\n',encoding='utf-8')
 (R/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: '+BASE+'sitemap.xml\n',encoding='utf-8')
if __name__=='__main__':enhance()
