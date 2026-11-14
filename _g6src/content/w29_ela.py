SLIDES = ('<svg viewBox="0 0 660 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="A cluttered slide with paragraphs of text compared with a clear slide with one headline, one image and a source line">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Slides support your talk; they don\'t replace it</text>'
  '<rect x="30" y="36" width="280" height="160" rx="6" fill="#fff" stroke="#DB2F30" stroke-width="3"/><text x="170" y="56" text-anchor="middle" fill="#DB2F30" font-weight="bold">Hard to follow</text>'
  + ''.join(f'<rect x="44" y="{66+i*11}" width="{250 - (i%3)*30}" height="5" fill="#b9c3d0"/>' for i in range(10)) +
  '<text x="170" y="190" text-anchor="middle" fill="#5b6676" font-size="10">tiny text, full paragraphs, no source</text>'
  '<rect x="350" y="36" width="280" height="160" rx="6" fill="#fff" stroke="#2c6e22" stroke-width="3"/><text x="490" y="58" text-anchor="middle" fill="#0A1F3D" font-weight="bold" font-size="14">Algae blooms are growing</text>'
  '<rect x="380" y="70" width="220" height="86" rx="4" fill="#9fc6e8"/><path d="M390 140 Q450 100 510 120 T590 92" fill="none" stroke="#2c6e22" stroke-width="5"/><text x="490" y="150" text-anchor="middle" fill="#0A1F3D" font-size="10">chart: bloom size, 2015 to 2025</text>'
  '<text x="490" y="176" text-anchor="middle" fill="#5b6676" font-size="10">Source: SFWMD (practice chart)</text><text x="490" y="190" text-anchor="middle" fill="#2c6e22" font-size="10">one idea, one visual, a source</text></svg>')

LESSON = {
 "unit": "Unit 6: Research and Presentation",
 "title": "Speaking and Presenting",
 "subtitle": "Your research report is drafted. Now you turn it into a presentation that informs and holds an audience. In Week 20 you delivered an argument speech; this week you add what research presentations need: planning for your audience, designing clear visuals, explaining data aloud, citing sources while speaking, and handling questions you didn't expect.",
 "objectives": [
  "Adapt a written report into a 4- to 6-minute presentation for a specific audience.",
  "Design slides or posters that follow principles of clear visual design.",
  "Explain data and visuals aloud and cite sources while speaking.",
  "Use delivery skills (eye contact, volume, pace, gestures) and respond to audience questions.",
  "Give and use specific feedback to improve a presentation."],
 "vocab": [
  ["audience", "The people listening to or reading your work."],
  ["visual aid", "A slide, poster, chart, map or object that helps an audience understand your message."],
  ["oral citation", "Naming a source aloud, such as \"According to the U.S. Geological Survey...\""],
  ["pace", "How fast or slow you speak."],
  ["signpost", "A phrase that tells the audience where you are in a talk, such as \"My second finding is...\""],
  ["Q&A", "The question-and-answer time after a presentation."]],
 "reconnect": {
  "title": "Week 28: Drafting a report",
  "intro": "Your draft becomes your presentation plan.",
  "items": [
   {"t":"text","q":"What do we call combining information from several sources into one new understanding?","a":[{"all":[["synthes"]],"none":["not"]}],"show":"synthesizing","pts":2,"why":"Not just listing sources."},
   {"t":"open","key":"rc_mainpoints","q":"Write the three main points (section topic sentences) of your research report.","min":20,"rows":3,"rubric":["Three main points that answer the research question"],"model":"1. Fertilizer runoff and warm water feed the algae. 2. Water releases carry the algae to both coasts, harming people and pets. 3. A new reservoir and Everglades restoration could help stop the blooms."},
   {"t":"open","key":"rc_week20","q":"In Week 20 you delivered an argument speech. Name one delivery skill you did well and one you want to improve this time.","min":15,"rows":2,"rubric":["One strength","One goal"],"model":"I made good eye contact in Week 20, but I talked too fast when I got nervous, so this time I want to slow down and pause after key facts."}]},
 "hook": {
  "title": "Reports Are Read; Presentations Are Heard",
  "visual": SLIDES,
  "html": "<p>A reader can reread a confusing sentence; a listener can't. That's why the best presenters don't just read their reports aloud. They choose the three most important ideas, show one clear visual for each, tell the audience where they're going, and repeat the big answer at the end.</p><p>Compare the two slides. Which would you rather look at while someone talks?</p><div class='callout'><b>Big question:</b> How do you share research so an audience understands it, remembers it and trusts it?</div>"},
 "learn": [
  {"title": "From Report to Talk: Know Your Audience",
   "html": "<p>Start with your <b>audience</b>: Who will listen? What do they already know? What should they remember? A talk for your co-op's younger students needs simpler words and more pictures than one for adults.</p><p>Then plan a 4- to 6-minute talk:</p><ul><li><b>Opening (30 seconds):</b> your hook and research question.</li><li><b>Three findings (about 1 minute each):</b> one visual and one or two key facts for each. Use <b>signposts</b>: \"My first finding is...\", \"Next...\", \"Finally...\".</li><li><b>Closing (30 to 60 seconds):</b> your answer in one sentence, why it matters and what listeners can do.</li></ul><p>Write key words on note cards, not full sentences, so you speak instead of read.</p>",
   "checks": [
    {"t":"open","key":"audienceshift","q":"Explain two changes you would make to your presentation if your audience were 8-year-olds instead of adults.","min":25,"rows":3,"rubric":["Two specific changes","Each tied to what young listeners need"],"model":"I would replace words like phosphorus with \"fertilizer that feeds algae\" and use a picture of green water instead of a data chart, because younger kids need simpler words and pictures they can understand quickly."},
    {"t":"open","key":"signposts","q":"Write the three signpost sentences you'll use to introduce your three findings.","min":20,"rows":3,"rubric":["Three signposts that name each finding"],"model":"My first finding is what feeds the algae. Next, I'll show how the algae reach our beaches. Finally, I'll share what scientists are doing to stop it."}]},
  {"title": "Designing Clear Visuals",
   "html": "<p>Good visual aids follow a few rules:</p><ul><li><b>One idea per slide or panel,</b> with a short headline that states it.</li><li><b>Big, readable text</b> (no more than about 20 words per slide) and high contrast, like dark text on a light background.</li><li><b>Charts and maps</b> that show your data clearly, with labeled axes and units, like the displays you made in math in Weeks 28 and 29.</li><li><b>A source line</b> on every slide that uses someone else's data or image.</li><li>Images you have the right to use: your own photos and drawings, or public domain and openly licensed images, credited.</li></ul>",
   "checks": [
    {"t":"open","key":"fixslide","q":"A classmate's slide has the title \"Manatees,\" three paragraphs of small text and a photo copied from a news website with no credit. Give three specific fixes.","min":30,"rows":3,"rubric":["Three specific, correct fixes"],"model":"Change the title to a headline that states the idea, like \"Manatees need warm water to survive winter.\" Cut the paragraphs to a few key words and say the rest aloud. Replace the photo with one that's free to use, or credit it, and add a source line."},
    {"t":"open","key":"chartchoice","q":"Which kind of visual (photo, map, bar graph, line graph, dot plot or diagram) would best show each: (a) how Silver Springs' flow changed from 1940 to 2020, (b) where algae blooms spread, (c) how a spring is connected to the aquifer?","min":20,"rows":3,"rubric":["A sensible visual for each with a reason"],"model":"(a) A line graph, because it shows change over time. (b) A map, because it shows places. (c) A diagram, because it shows how parts connect underground."}]},
  {"title": "Speaking with Data and Sources",
   "html": "<p>Numbers are hard to remember when you only hear them. Make them land:</p><ul><li>Round and compare: \"about one-third less water\" is easier than \"32.4 percent.\"</li><li>Point to the visual: \"See how the line drops after 1970?\"</li><li>Explain what it means: \"That's like losing a whole swimming pool every few seconds.\"</li></ul><p>Use <b>oral citations</b> so listeners can trust you: \"According to the U.S. Geological Survey...\", \"A 2023 study from the University of Florida found...\". Include a final slide or handout listing all your sources.</p>",
   "checks": [
    {"t":"open","key":"speakdata","q":"Rewrite this sentence so it works better when spoken aloud, with an oral citation: \"Flow declined 32.4% from the 1933-2010 mean.\"","min":14,"rows":2,"rubric":["Rounds or simplifies the number","Adds an oral citation","Easy to understand when heard"],"model":"According to the St. Johns River Water Management District, Silver Springs now flows about one-third less than it used to."}]},
  {"title": "Delivery and Questions",
   "html": "<p>In Week 20 you practiced eye contact, voice and pauses. For a research talk, add:</p><ul><li><b>Face the audience, not the screen.</b> Glance at the visual, then turn back.</li><li><b>Pause after key facts</b> so they sink in.</li><li><b>Handle Q&A:</b> listen to the whole question, repeat or rephrase it, answer briefly, and if you don't know, say \"I didn't find that in my research, but I'd look in...\" Honesty builds trust.</li></ul><p>Practice with a timer at least twice, and ask a listener for specific feedback: one thing that worked and one thing to change.</p>",
   "checks": [
    {"t":"open","key":"hardq","q":"During your Q&A, someone asks a question you can't answer. Write exactly what you would say.","min":15,"rows":2,"rubric":["Honest about not knowing","Suggests where the answer might be found"],"model":"That's a great question. I didn't find that in my research, but I'd check the South Florida Water Management District's reports, and I can look it up after the presentation."},
    {"t":"open","key":"feedback","q":"Turn this vague feedback into specific feedback: \"It was good but kind of boring.\"","min":20,"rows":2,"rubric":["Names something specific that worked","Names a specific, actionable change"],"model":"Your map of where the algae spread was really clear. To make it more engaging, you could open with the story of the beach that closed instead of starting with numbers."}]}],
 "handson": {
  "title": "Build and Rehearse Your Presentation",
  "intro": "Create your visuals, rehearse with a timer and improve with feedback.",
  "materials": ["Your research report draft", "A computer or tablet with slide software, or poster board and markers", "5 to 8 index cards", "A timer", "A phone or tablet to record (optional)", "At least one family member as an audience"],
  "steps": [
   "Plan 6 to 8 slides or poster panels: title and question, three findings, conclusion, and sources. Use one idea and one visual per slide.",
   "Make at least one data visual (a chart, map or diagram) with a source line, using what you learned in math.",
   "Write key words, not sentences, on note cards.",
   "Rehearse with a timer. Aim for 4 to 6 minutes. Record yourself if you can and watch for pace, eye contact and filler words.",
   "Present to a family member, who asks at least two questions and gives one specific strength and one specific change. Revise and rehearse once more.",
   "Use only images you took, drew or have permission to use, with credit."],
  "record": [
   {"t":"open","key":"rehearsalrec","q":"How long was your first rehearsal and your last? List the feedback you received and the changes you made.","min":40,"rows":4,"rubric":["Both times reported","Specific feedback listed","Specific changes described"],"model":"My first rehearsal was 7 minutes 40 seconds and my last was 5 minutes 15 seconds. My mom said my map was clear but I read the slides word for word and said \"um\" a lot. I cut the slide text to five words each, practiced with note cards, and paused instead of saying \"um.\""},
   {"t":"open","key":"qarec","q":"What two questions did your audience ask, and how did you answer them? Was there one you couldn't answer, and what did you say?","min":35,"rows":3,"rubric":["Two questions with answers","Honest handling of a question that couldn't be answered, or a note that all were answered"],"model":"My dad asked whether the algae can hurt dogs; I said yes, and that the Department of Health warns pet owners. My sister asked whether it happens every year; I wasn't sure, so I said blooms happen most summers but I'd need to check the exact years."}]},
 "think": {
  "intro": "Your teacher scores these.",
  "items": [
   {"t":"open","key":"trustspeaker","q":"What makes an audience trust a speaker who is presenting research? Give at least three things, and explain which matters most.","min":39,"rows":5,"rubric":["Three things that build trust","Explains which matters most and why"],"model":"Citing reliable sources aloud, showing clear data with sources, and admitting what you don't know all build trust. I think citing sources matters most, because like we learned in Week 27, people should be able to check where information came from instead of just believing the speaker."},
   {"t":"open","key":"greatspeaker","q":"Think of a speaker you've heard (a pastor, a teacher, a museum guide, a documentary narrator, a family member). What did they do that kept you listening, and how will you use one of those techniques?","min":35,"rows":4,"rubric":["Names a speaker and specific techniques","Explains how the student will use one"],"model":"Our museum guide at the Florida Museum told a story about one fossil before giving facts, and she asked us questions. I'll open my presentation with the story of the beach closing and ask my audience whether they've ever seen green water."}]},
 "exit": [
  {"t":"open","key":"exit_signpost","q":"Write one signpost phrase you could use in a presentation.","min":3,"rows":1,"rubric":["A phrase that tells listeners where they are in the talk"],"model":"My second finding is..."},
  {"t":"open","key":"exit_slide","q":"Name two rules for a clear slide.","min":6,"rows":2,"rubric":["Two valid rules from the lesson"],"model":"One idea per slide, and big readable text with a source line."},
  {"t":"open","key":"exit_oral","q":"Write an oral citation for a fact from your research.","min":6,"rows":2,"rubric":["Names the source aloud with the fact"],"model":"According to the Florida Department of Health, algae blooms can make pets sick."}],
 "next": "Week 30: end-of-year review and research presentation."
}

TEACHER = {
 "standards": [
  "ELA.6.C.2.1: Present information orally, in a logical sequence, using nonverbal cues, appropriate volume, clear pronunciation, and appropriate pacing.",
  "ELA.6.C.5.1: Integrate diverse digital media to enhance audience engagement in oral or written tasks.",
  "ELA.6.C.4.1: Conduct research to answer a question, drawing on multiple reliable and valid sources, and refocusing the inquiry when appropriate.",
  "ELA.K12.EE.1.1: Cite evidence to explain and justify reasoning."],
 "materials": ["The interactive lesson", "The student's report draft", "Slide software or poster board and markers", "5 to 8 index cards, a timer, optional recording device", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 28 warm-up questions; recall Week 20."],
  [4, "Hook", "Read versus heard; compare two slides."],
  [11, "Audience and structure", "Adapt for 8-year-olds; write signposts."],
  [12, "Visual design", "Fix a slide; choose the right chart."],
  [10, "Data and sources aloud", "Round, compare, point; oral citations."],
  [11, "Delivery and Q&A", "The question you can't answer; specific feedback."],
  [6, "Assign", "Build and rehearse; assign Think Deeper and the Exit Check."]],
 "key_questions": ["Who is your audience, and what should they remember?", "Does each slide have one idea and a source?", "How will you make this number understandable?", "What will you say if you don't know an answer?"],
 "misconceptions": ["A presentation is the report read aloud.", "More text on slides is more helpful.", "Admitting you don't know looks bad.", "Any image online is free to use."],
 "support": ["Provide a slide template with headline, visual and source boxes.", "Let the student rehearse first to a pet or stuffed animal, then a person.", "Provide note-card frames for each section."],
 "challenge": ["Add a short demonstration or object to the presentation.", "Present to an audience outside the family, such as a co-op class or library group."],
 "background": "<p>The final research presentation is delivered in Week 30 and scored with the Unit 6 project rubric. Week 20 introduced speech delivery (eye contact, volume, pauses, note cards); this week builds research-presentation skills: audience analysis, visual design, speaking with data, oral citations and Q&A.</p>",
 "sources": ["Florida Department of Education, B.E.S.T. Standards for English Language Arts (2020).", "Duarte, Nancy, slide:ology (2008).", "Reynolds, Garr, Presentation Zen (3rd ed., 2019)."]
}

PRINT = {
 "directions": "Plan your presentation.",
 "items": [
  {"q":"Write your hook and research question as you'll say them.","a":"Model: In 2018, families couldn't swim at their beaches because of thick green algae. Why do these blooms keep spreading, and what could stop them?","lines":3},
  {"q":"List your three findings and the visual you'll use for each.","a":"Model: causes (diagram of runoff), spread (map of releases), solutions (photo of the reservoir site).","lines":3},
  {"q":"Write one sentence that explains a number from your research in a way listeners will remember.","a":"Model: Silver Springs now flows about one-third less than it did in the 1930s, according to the St. Johns River Water Management District.","lines":2},
  {"q":"List three rules for clear slides.","a":"One idea per slide; big readable text; a source line on every slide with outside data or images.","lines":2},
  {"q":"Write what you'll say if someone asks a question you can't answer.","a":"Model: I didn't find that in my research, but I'd look in the water district's reports.","lines":2}]
}
