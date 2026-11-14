SIFT = ('<svg viewBox="0 0 660 220" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="The four SIFT moves: Stop, Investigate the source, Find better coverage, Trace claims to the original">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Four moves before you trust or share: SIFT</text>'
  + ''.join(f'<g transform="translate({16+i*160},36)"><rect width="150" height="170" rx="12" fill="{c}"/><text x="75" y="44" text-anchor="middle" fill="#fff" font-weight="bold" font-size="34" font-family="Georgia">{l}</text><text x="75" y="72" text-anchor="middle" fill="#fff" font-weight="bold" font-size="14">{a}</text>'
            + ''.join(f'<text x="75" y="{96+j*16}" text-anchor="middle" fill="#fff" font-size="11">{t}</text>' for j, t in enumerate(lines)) + '</g>'
            for i, (l, a, c, lines) in enumerate([("S", "Stop", "#0A1F3D", ["Notice strong feelings.", "Do you know this", "source? Pause before", "you share."]),
                                                 ("I", "Investigate", "#0047BA", ["Who made this?", "Leave the page and", "search the author or", "site (read laterally)."]),
                                                 ("F", "Find better", "#2c6e22", ["What do other", "trusted sources say?", "Look for agreement", "across several."]),
                                                 ("T", "Trace", "#DB2F30", ["Follow quotes, data", "and images back to", "the original: who", "said it first?"])])) +
  '</svg>')

POST = ("<div class='card' style='border-left-color:#DB2F30'><p class='small muted' style='margin:0'>A practice social media post written by KingCretot Experience for this lesson. It is not real.</p>"
        "<p style='font-size:17px;margin:8px 0'><b>@FloridaNatureFacts2026</b> &middot; 2h</p>"
        "<p style='font-size:16px'>SHOCKING!!! Scientists CONFIRM Florida's springs will be completely DRY by 2030!!! The government doesn't want you to know. One study proves it. SHARE before this gets deleted!!! #SaveOurSprings</p>"
        "<p class='small muted'>[photo of a cracked, dry lakebed] &middot; 48,000 shares</p></div>")

LESSON = {
 "unit": "Unit 6: Research and Presentation",
 "title": "Judging Sources and Spotting Misinformation",
 "subtitle": "Your research question is only as good as the sources you use to answer it. This week you learn the moves professional fact-checkers use: stopping before you share, investigating who made a source, finding better coverage, tracing claims to their origin, and spotting the tricks of misinformation, including fake images and AI-written text.",
 "objectives": [
  "Evaluate a source's reliability using its author, purpose, evidence, date and publisher.",
  "Use lateral reading and the SIFT moves to check a source or claim.",
  "Distinguish misinformation from disinformation and identify common persuasion tricks.",
  "Check images and AI-generated content before trusting them.",
  "Choose and justify reliable sources for your research question."],
 "vocab": [
  ["reliable", "Trustworthy because it is accurate, well supported and from a knowledgeable source."],
  ["misinformation", "False or misleading information shared without the intent to deceive."],
  ["disinformation", "False information spread on purpose to deceive."],
  ["lateral reading", "Checking a source by leaving it and searching what other sources say about it."],
  ["bias", "A one-sided point of view that can affect how information is presented."],
  ["primary source", "An original source created at the time, such as data, a speech or an eyewitness account."]],
 "reconnect": {
  "title": "Week 26: Asking research questions",
  "intro": "Your research question tells you what to look for. Now decide what to trust.",
  "items": [
   {"t":"open","key":"rc_myq","q":"Write your Unit 6 research question from last week.","min":6,"rows":2,"rubric":["A focused, open research question"],"model":"Why do algae blooms keep spreading from Lake Okeechobee, and what could stop them?"},
   {"t":"text","q":"What do we call smaller questions that help answer your main research question?","a":[{"all":[["sub-question","subquestion","sub question"]],"none":["not"]}],"show":"sub-questions","pts":2,"why":"Plan three to five."},
   {"t":"open","key":"rc_trust","q":"Name one source you already found for your question. What makes you think it is trustworthy, or what makes you unsure?","min":15,"rows":2,"rubric":["Names a source","Gives a reason for trust or doubt"],"model":"I found a page from the South Florida Water Management District. I trust it because it's a government agency that measures the lake, but I'm not sure how it handles blame for pollution."}]},
 "hook": {
  "title": "Share or Stop?",
  "visual": SIFT,
  "html": POST + "<p>This post has 48,000 shares. Does that make it true? Notice the all-caps words, the many exclamation points, the claim that \"the government doesn't want you to know,\" the pressure to share before it's deleted, and a single unnamed study. And is that photo even a Florida spring?</p><p>False information spreads fast online because it's designed to make us feel shocked, angry or afraid, and to share before we think. This week you learn to check before you trust.</p><div class='callout'><b>Big question:</b> How do you know what to trust when anyone can publish anything?</div>"},
 "learn": [
  {"title": "What Makes a Source Reliable",
   "html": "<p>In Week 9 you found two sources and took notes. Now judge them. Ask five questions:</p><ul><li><b>Who</b> made it? An expert, a scientist, a journalist, a government agency, or someone anonymous?</li><li><b>Why</b> was it made? To inform, to persuade, to sell or to entertain?</li><li><b>What evidence</b> does it give? Data, named sources and links you can check, or just opinions?</li><li><b>When</b> was it published or updated? For science and news, newer is usually better.</li><li><b>Where</b> is it published? A peer-reviewed journal, a government (.gov) or university (.edu) site, an established news outlet with corrections policies, or a random post?</li></ul><p>No clue alone is enough: a .org site can be excellent or biased, and a .com site can be a respected newspaper.</p>",
   "checks": [
    {"t":"open","key":"rankfour","q":"Rank these sources for the question \"How many manatees live in Florida?\" from most to least reliable, and explain your top and bottom choices: (a) a fan video titled \"I swam with 1,000 manatees!\", (b) the Florida Fish and Wildlife Conservation Commission's manatee survey, (c) a 2009 encyclopedia, (d) a news article quoting the survey.","min":39,"rows":4,"rubric":["A sensible ranking","Explains the top choice with reliability criteria","Explains the bottom choice"],"model":"Most to least: (b), (d), (c), (a). The FWC survey is the original data from scientists who count manatees. The news article is good but secondhand. The encyclopedia is reliable but out of date. The fan video is entertainment with an exaggerated title and no method."},
    {"t":"open","key":"purposecheck","q":"A website about the health benefits of orange juice is run by an orange juice company. Does that make it false? How should a researcher use it?","min":25,"rows":3,"rubric":["Recognizes the bias or purpose without assuming it's false","Explains checking its claims against independent sources"],"model":"It isn't automatically false, but the company wants to sell juice, so it might leave out downsides like sugar. A researcher should check its claims against independent sources, like a university nutrition department or government health site."}]},
  {"title": "Reading Laterally: How Fact-Checkers Work",
   "html": "<p>When researchers at Stanford tested how people judge websites, professional fact-checkers beat even history professors. Their secret was <b>lateral reading</b>: instead of reading a site from top to bottom, they opened new tabs right away and searched what other sources said about the site and its author.</p><p>The four <b>SIFT</b> moves, developed by researcher Mike Caulfield, put this into practice: <b>Stop</b>, <b>Investigate</b> the source, <b>Find</b> better coverage and <b>Trace</b> claims, quotes and images to their original context.</p>",
   "checks": [
    {"t":"order","q":"Put the SIFT moves in order.","items":["Stop","Investigate the source","Find better coverage","Trace claims to the original"],"pts":2,"why":"Stop first, then check outward."},
    {"t":"open","key":"lateralpost","q":"Use the SIFT moves to describe exactly what you would do to check the springs post in the hook. Name a real kind of source you'd use for the \"Find\" step.","min":45,"rows":4,"rubric":["Applies all four moves to the post","Names a reliable kind of source for checking springs"],"model":"Stop: the caps and \"share before it's deleted\" are warning signs, so I won't share. Investigate: search the account name to see who runs it. Find: check what the Florida Department of Environmental Protection and university scientists say about spring flow. Trace: look for the \"one study\" and see what it actually said, and do a reverse image search on the photo to see where it really came from."}]},
  {"title": "Misinformation Tricks",
   "html": "<p><b>Misinformation</b> is false information shared by mistake; <b>disinformation</b> is spread on purpose. Both use the same tricks:</p><ul><li><b>Emotional hooks:</b> all caps, \"SHOCKING,\" outrage or fear.</li><li><b>Urgency:</b> \"share before it's deleted.\"</li><li><b>Fake authority:</b> \"scientists confirm\" with no names; \"one study proves\" (one study rarely proves anything).</li><li><b>Exaggeration:</b> a real fact stretched, like a spring with lower flow becoming \"completely dry.\"</li><li><b>Out-of-context images:</b> a real photo from somewhere else.</li><li><b>Us-versus-them claims:</b> \"they don't want you to know.\"</li></ul><p>Remember the Week 24 lesson about Great Zimbabwe: false stories can spread for a century when they serve someone's interests.</p>",
   "checks": [
    {"t":"open","key":"findtricks","q":"Name three misinformation tricks used in the springs post, quoting the words that show each one.","min":17,"rows":3,"rubric":["Three different tricks named","A quotation from the post for each"],"model":"Emotional hook: \"SHOCKING!!!\" Fake authority: \"Scientists CONFIRM\" and \"One study proves it\" with no names. Urgency: \"SHARE before this gets deleted!!!\""},
    {"t":"open","key":"misdis","q":"Your grandmother shares the springs post because she's worried about the springs. The account that created it makes money from clicks. Which person is spreading misinformation and which is spreading disinformation? Explain.","min":25,"rows":3,"rubric":["Correctly labels both","Explains the difference as intent"],"model":"Grandma is spreading misinformation, because she believes it and means well. The account is spreading disinformation if it knows the claim is exaggerated and posts it to get clicks and money. The difference is whether they intend to deceive."}]},
  {"title": "Images and AI-Generated Content",
   "html": "<p>Photos can be real but taken somewhere else, edited, or completely generated by AI. AI tools can also write convincing articles that contain made-up facts and even fake citations.</p><ul><li><b>Reverse image search</b> (with a parent's help) shows where else a picture appears and when it first appeared.</li><li>Look for clues of AI images: warped hands or text, strange backgrounds, too-perfect lighting. Clues aren't proof; check the source.</li><li>Never cite a source you haven't opened yourself. If a chatbot or website gives you a quotation or study, find the original before you use it.</li></ul>",
   "checks": [
    {"t":"open","key":"aicheck","q":"An AI chatbot tells you, \"A 2021 University of Florida study found that springs lose 2 inches of water a year,\" with a link. What should you do before using this in your research, and why?","min":30,"rows":3,"rubric":["Says to open and read the original study","Explains that AI can invent facts or citations","Mentions checking that the number matches"],"model":"I should click the link and find the actual study to make sure it exists, that the University of Florida really published it, and that it says exactly that. AI tools sometimes invent studies and numbers that sound real, so I can't cite something I haven't checked."}]}],
 "handson": {
  "title": "Fact-Check Challenge",
  "intro": "Investigate practice claims like a professional fact-checker, then evaluate the sources for your own research.",
  "materials": ["A computer or tablet with internet access (with a parent nearby)", "Paper and pencil", "A timer", "A family member", "Your research question and sources from last week"],
  "steps": [
   "With a parent, check each practice claim using SIFT, spending no more than 5 minutes per claim: (1) \"Manatees are no longer listed as a threatened species.\" (2) \"Lightning strikes Florida more than any other state.\" (3) \"The Great Wall of China is visible from the Moon with the naked eye.\" (4) \"Honey never spoils.\"",
   "For each claim, record your verdict (true, false, partly true or can't tell), the best source you found and why you trust it.",
   "Source scorecard: for two sources you plan to use for your research question, rate each on who, why, evidence, when and where (1 to 3 points each).",
   "Replace any source that scores below 10 out of 15 with a better one.",
   "Stay on sites your parent approves, and never share personal information while researching."],
  "record": [
   {"t":"open","key":"factrec","q":"Report your verdict and best source for each of the four practice claims. Which claim surprised you, and which SIFT move helped most?","min":50,"rows":5,"rubric":["Four verdicts with sources","Reliable sources chosen","Reflects on a surprise and the most useful move"],"model":"1. False: the U.S. Fish and Wildlife Service reclassified manatees from endangered to threatened in 2017, so they are still listed as threatened. 2. Mostly true: Florida usually leads in lightning density (National Weather Service). 3. False: NASA says you can't see the Great Wall from the Moon. 4. Mostly true: archaeologists found edible honey in ancient Egyptian tombs, though it can spoil if water gets in. The manatee claim surprised me; \"Find better coverage\" helped most."},
   {"t":"open","key":"scorecardrec","q":"Share your source scorecard for two research sources, with the score for each criterion. Did you replace a source? Explain why or why not.","min":40,"rows":4,"rubric":["Two sources scored on all five criteria","Totals calculated","A justified decision about keeping or replacing"],"model":"Source 1, South Florida Water Management District: who 3, why 2, evidence 3, when 3, where 3 = 14. Source 2, a blog called Florida Fishing Fun: who 1, why 1, evidence 1, when 2, where 1 = 6. I replaced the blog with a Florida Sea Grant fact sheet from the University of Florida, which scored 14."}]},
 "think": {
  "intro": "Your teacher scores these.",
  "items": [
   {"t":"open","key":"whyspread","q":"Research shows false news often spreads faster online than true news. Explain at least two reasons why, and describe what you personally will do differently before sharing something.","min":50,"rows":5,"rubric":["Two reasonable explanations","A specific personal plan"],"model":"False stories are often more shocking and emotional than the truth, so people share them before thinking, and they're designed to spread, with urgency like \"share before it's deleted.\" Also, people tend to share things that match what they already believe. Before I share anything, I'll stop, search the source and see whether at least two reliable sources agree."},
   {"t":"open","key":"historytrust","q":"Historians in Units 4 and 5 had to judge sources too: Herodotus, al-Bakri, Ibn Battuta, Leo Africanus. Choose one and explain how the questions about who, why, evidence, when and where would apply to it.","min":54,"rows":5,"rubric":["Accurate details about the chosen source","Applies at least four of the five questions"],"model":"Leo Africanus: who, a well-traveled scholar from North Africa; why, to describe Africa for European readers; evidence, his own visit to Timbuktu about 1510, so firsthand but from memory; when, written years after the visit; where, published in Italian and later translated into English in 1600, so some words may have changed. Like a modern website, it's useful but needs checking against other sources."}]},
 "exit": [
  {"t":"text","q":"What is the name for checking a source by leaving it and searching what others say about it?","a":[{"all":[["lateral"]],"none":["not"]}],"show":"lateral reading","pts":2,"why":"Fact-checkers do it first."},
  {"t":"open","key":"exit_misdis","q":"What is the difference between misinformation and disinformation?","min":10,"rows":2,"rubric":["Explains the difference in intent"],"model":"Misinformation is false information shared by mistake; disinformation is false information spread on purpose to deceive."},
  {"t":"open","key":"exit_redflag","q":"Name two red flags that a post might be misinformation.","min":6,"rows":2,"rubric":["Two valid red flags"],"model":"All-caps emotional words and pressure to share right away."}],
 "next": "Week 28: organizing and drafting a report."
}

TEACHER = {
 "standards": [
  "ELA.6.C.4.1: Conduct research to answer a question, drawing on multiple reliable and valid sources, and refocusing the inquiry when appropriate.",
  "ELA.K12.EE.1.1: Cite evidence to explain and justify reasoning."],
 "materials": ["The interactive lesson", "A computer or tablet with internet access (parent supervision)", "A timer", "The student's research question and sources", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 26 warm-up questions."],
  [5, "Hook", "The springs post: share or stop?"],
  [12, "Reliable sources", "Five questions; rank the manatee sources."],
  [11, "Lateral reading", "SIFT; apply it to the post."],
  [11, "Misinformation tricks", "Find the tricks; misinformation versus disinformation."],
  [9, "Images and AI", "Reverse image search; check AI citations."],
  [6, "Assign", "Set up the fact-check challenge and scorecard; assign Think Deeper and the Exit Check."]],
 "key_questions": ["Who made this, and why?", "What do other sources say about it?", "Where did this claim, quote or image first appear?", "How does this post want me to feel?"],
 "misconceptions": ["Lots of shares means it's true.", "A professional-looking site must be reliable.", ".org sites are always trustworthy.", "If an AI tool says it, it must have a source."],
 "support": ["Provide the five-question checklist as a bookmark.", "Model one lateral search aloud.", "Pair the student with a parent for the online challenge."],
 "challenge": ["Find a real correction published by a news outlet and explain what it shows about reliability.", "Compare how two news outlets with different viewpoints cover the same Florida story."],
 "background": "<p>Practice claim answers: (1) false, since manatees were reclassified from endangered to threatened in 2017 and remain federally threatened; (2) Florida generally has the highest lightning density among U.S. states, though a given year can vary; (3) false, per NASA; (4) mostly true, since properly sealed honey keeps for very long periods. The springs post is invented for the lesson. The Stanford History Education Group study (Wineburg and McGrew, 2017) compared fact-checkers, historians and students. SIFT was developed by Mike Caulfield.</p>",
 "sources": ["Caulfield, Mike, and Sam Wineburg, Verified: How to Think Straight, Get Duped Less, and Make Better Decisions about What to Believe Online (2023).", "Wineburg, Sam, and Sarah McGrew, \"Lateral Reading,\" Stanford History Education Group working paper (2017).", "News Literacy Project, Checkology resources."]
}

PRINT = {
 "directions": "Answer in complete sentences.",
 "items": [
  {"q":"List the five questions for judging a source.","a":"Who made it? Why? What evidence? When? Where is it published?","lines":2},
  {"q":"What do the letters in SIFT stand for?","a":"Stop, Investigate the source, Find better coverage, Trace claims to the original.","lines":2},
  {"q":"Name three misinformation tricks.","a":"Emotional hooks, urgency, fake authority, exaggeration, out-of-context images, us-versus-them.","lines":2},
  {"q":"Why should you never cite a source you haven't opened yourself?","a":"It might not exist, might say something different, or might be invented by AI.","lines":2},
  {"q":"Rate one of your research sources on the five questions and decide whether to keep it.","a":"Answers will vary.","lines":3}]
}
