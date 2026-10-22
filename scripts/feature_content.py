"""Bilingual product guides; claims match the published app homepage."""
FEATURES = {
'pro-play': {
'zh': ('PRO PLAY 职业选手手牌与范围查询｜德益记', '查看职业选手真实手牌：PRO PLAY', '在 iPhone 与 iPad 上查找 Tan Xuan、Wiktor 等选手的真实手牌，结合位置、范围矩阵和原视频研究行动。', [
('从一个具体问题开始', '想知道某位选手在某个位置如何处理一手牌？先选择选手，再按手牌和位置筛选。把问题缩小到具体场景，比只看最后谁赢了更有帮助。'),
('Tan Xuan 与 Wiktor 的手牌怎么查？', '在 PRO PLAY 中选择对应选手，查看符合筛选条件的样本，再进入手牌详情。可以收藏值得研究的牌，或打开原视频，结合前后行动理解当时的决定。可查询内容以 App 当前收录为准。'),
('范围矩阵表示什么？', '矩阵帮助你浏览收录样本中的起手牌分布。选手、位置与样本数量会影响你看到的结果；未出现的组合不意味着选手永远不会打。真实牌局样本不等同于 GTO 推荐范围。'),
('如何把职业选手手牌用于自己的复盘？', '对照位置、有效筹码、下注尺度和对手信息。先写下自己在这个场景会怎么做，再查看选手的行动与原视频。不要仅因为某位选手赢下底池就照搬其打法。'),
('PRO PLAY 免费吗？', 'PRO PLAY 提供总计 7 次免费查询。之后需要符合条件的订阅或 BB 点数，具体额度与当地价格以 App 内购买页面为准。'),
('支持哪些设备和语言？', '德益记支持 iPhone、iPad，以及中文和英文界面。PRO PLAY 用于研究已收录的真实牌局，不是在线扑克游戏平台。')]),
'en': ('Pro Poker Hands & Range Explorer for iPhone | SevenDeucePlus', 'Study real pro poker hands with PRO PLAY', 'Explore hands from Tan Xuan, Wiktor and other players on iPhone and iPad. Filter by position and cards, browse range matrices and revisit source videos.', [
('Start with a specific question', 'Choose a player, then filter by cards and position. Asking how a player handled a particular situation gives you a clearer study task than watching only who won the pot.'),
('How do I find Tan Xuan or Wiktor hands?', 'Select the player in PRO PLAY, browse matching samples and open a hand for details. Save hands to revisit or open the original video for the surrounding action. Availability depends on the hands currently included in the app.'),
('What does the range matrix show?', 'The matrix helps you explore starting hands in the recorded sample. Your player and position filters, and the sample size, affect what appears. A missing combination does not mean the player never plays it. Observed hands are not a GTO prescription.'),
('How can I use pro hands in my own review?', 'Compare position, effective stacks, bet sizes and opponent context. Write down your own decision before watching the action and source video. A winning outcome alone is not a reason to copy a play.'),
('Is PRO PLAY free?', 'PRO PLAY includes 7 free queries in total. Further use requires an eligible subscription or BB credits. Check the app for current allowances and prices in your region.'),
('Which devices and languages are supported?', 'SevenDeucePlus supports iPhone and iPad, with English and Chinese interfaces. PRO PLAY is for studying recorded hands; it is not an online poker game.')])},
'insights': {
'zh': ('德州扑克手牌复盘 App：Insights AI 辅助分析｜德益记', '把一手牌记完整，再用 Insights 辅助复盘', '逐步录入德州扑克手牌行动，补充对手风格与现场信息，在 iPhone 和 iPad 上回顾关键决策。', [
('复盘前需要准备什么？', '先整理手牌、公共牌、位置、有效筹码与逐街行动。尽量还原下注尺度和底池变化，不确定的内容要保留不确定性，避免凭记忆补出一个并未发生的行动。'),
('怎样使用 Insights？', '在 Insights 中逐步录入行动，补充对手风格与现场信息，检查记录后再请求分析。反馈用于帮助你回顾决策；如果输入遗漏了关键行动，应先修正记录，再判断分析是否适用。'),
('为什么要补充对手信息？', '同样的下注在不同对手与情境中可能有不同含义。将观察到的行为与个人猜测分开写，例如“这场两次在河牌大额下注”比直接认定“总在诈唬”更便于复盘。'),
('AI 分析能保证正确吗？', '不能。AI 可能误读行动、采用不合适的假设或算错数值。检查输入、底池与分析前提，并结合自己的判断。单手输赢也不能证明一个决策好坏。'),
('Insights 包含在订阅里吗？', 'Insights 分析单独消耗 BB 点数，订阅不等于无限 AI 分析。当前消耗、可用方案和当地价格请以 App 内显示为准。'),
('Insights 与 PRO PLAY 有什么区别？', 'Insights 用于录入并复盘你想研究的手牌；PRO PLAY 用于查找已收录的职业选手真实样本及原视频。两者分别帮助你回顾自己的问题和研究他人的行动。')]),
'en': ('Poker Hand Review App for iPhone: Insights | SevenDeucePlus', 'Review poker hands with Insights', 'Rebuild the action, add opponent context and use AI-assisted feedback to revisit poker decisions on iPhone and iPad.', [
('What should I record before reviewing a hand?', 'Gather hole cards, board cards, positions, effective stacks and the action on each street. Reconstruct bet sizes and pot changes as accurately as possible. Keep uncertain details marked as uncertain rather than inventing missing action.'),
('How do I use Insights?', 'Enter the action step by step, add opponent context and check the record before requesting analysis. Use the feedback to revisit your decisions. If you missed an important action, correct the record before deciding whether the analysis applies.'),
('Why include opponent context?', 'The same bet can mean different things against different opponents. Separate observations from guesses: “made two large river bets this session” is a more useful review note than assuming someone always bluffs.'),
('Is the AI analysis always correct?', 'No. AI can misread action, use unsuitable assumptions or make calculation errors. Check the input, pot sizes and reasoning against your own judgment. One hand’s outcome does not establish whether a decision was good.'),
('Does a subscription include Insights analysis?', 'Insights analysis uses BB credits separately. A subscription does not include unlimited AI analysis. Check the app for current credit costs, available plans and local prices.'),
('How is Insights different from PRO PLAY?', 'Insights helps you enter and review a hand you want to study. PRO PLAY lets you browse recorded pro hands and their source videos. Use one to revisit your decisions and the other to explore real player samples.')])}}

SCREENSHOTS = {
 'session-tracking': [('overview', '盈利记录与收益曲线', 'Session results and profit chart')],
 'home-game-settlement': [('scoreboard', '记分板：玩家买入与结算', 'Scoreboard with buy-ins and results')],
 'pro-play': [('proplay-tanxuan', 'Tan Xuan 真实手牌查询', 'Tan Xuan hand search'), ('proplay-wiktor-range', 'Wiktor 起手牌范围矩阵', 'Wiktor starting-hand range matrix')],
 'insights': [('manual-action', 'Insights 逐步录入行动', 'Enter hand actions in Insights'), ('manual-confirm', 'Insights 对手信息与确认', 'Opponent context and review in Insights')],
}
