YEAR = ('<svg viewBox="0 0 660 210" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Six units of Grade 6 ELA as a path: stories, informational writing, poetry, argument, the novel, research and presentation">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Your Grade 6 ELA year</text>'
  '<path d="M60 110 H600" stroke="#C9A84C" stroke-width="6" stroke-dasharray="2 10" stroke-linecap="round"/>'
  + ''.join(f'<circle cx="{60+i*108}" cy="110" r="34" fill="{c}"/><text x="{60+i*108}" y="106" text-anchor="middle" fill="#fff" font-weight="bold" font-size="12">Unit {i+1}</text><text x="{60+i*108}" y="122" text-anchor="middle" fill="#fff" font-size="10">{w}</text><text x="{60+i*108}" y="{166 + (i%2)*16}" text-anchor="middle" fill="#0A1F3D" font-size="11">{t}</text>'
            for i, (w, t, c) in enumerate([("Wk 1-5", "personal narrative", "#0A1F3D"), ("Wk 6-10", "informational article", "#0047BA"), ("Wk 11-15", "poetry analysis", "#8a6d1f"),
                                            ("Wk 16-20", "argument speech", "#DB2F30"), ("Wk 21-25", "The Call of the Wild", "#2c6e22"), ("Wk 26-30", "research presentation", "#0A1F3D")])) +
  '</svg>')

SOURCE = ("<div class='callout'><b>Practice source (invented for this checkpoint):</b><br><i>\"SPRINGS ARE FINE, SAYS LOCAL EXPERT\"</i>, posted on <b>FloridaFunTubing.biz</b>, no date. "
          "\"Our springs are as clear as ever! Some so-called scientists claim flow is down, but I've been tubing here for 20 years and I haven't noticed a thing. Book your tube rental today and see for yourself! Use code CLEAR for 10% off.\" "
          "Author: \"Big Jim,\" owner.</div>")

LESSON = {
 "unit": "Unit 6: Research and Presentation",
 "title": "End-of-Year Review and Research Presentation",
 "subtitle": "This is the week you've been building toward. You deliver your research presentation, look back at how your reading and writing grew across six units, and show your mastery of research skills on the Unit 6 checkpoint.",
 "objectives": [
  "Deliver a 4- to 6-minute research presentation with visuals, oral citations and a Q&A.",
  "Evaluate a source for reliability using SIFT and the source questions from Week 27.",
  "Synthesize two sources in a paragraph with in-text citations.",
  "Connect the skills from all six units of the year.",
  "Demonstrate mastery of Unit 6 on the checkpoint (85 or higher)."],
 "vocab": [
  ["research question", "An open, focused question that can be answered with evidence from several sources."],
  ["reliable source", "A source with expert authors, clear evidence and an honest purpose."],
  ["synthesis", "Combining information from several sources into one new understanding."],
  ["in-text citation", "A short credit in your writing, such as (Florida Department of Health), that points to your works-cited list."],
  ["oral citation", "Naming a source aloud while you speak."],
  ["reflection", "Thinking back on your work to see how you grew and what you'll do next."]],
 "reconnect": {
  "title": "Unit 6, one question from each week",
  "intro": "Warm up with one question from each week of the unit.",
  "items": [
   {"t":"open","key":"rc_rq","q":"Week 26: Rewrite \"What is a manatee?\" as a strong research question.","min":8,"rows":2,"rubric":["An open, focused question that needs several sources"],"model":"How do warm-water springs help Florida manatees survive cold winters?"},
   {"t":"text","q":"Week 27: In SIFT, which move means leaving the page to see what other sources say about the website or author?","a":[{"all":[["investigate"]],"none":["not"]}],"show":"Investigate the source","pts":2,"why":"Read laterally."},
   {"t":"text","q":"Week 28: What do we call your list of every source used, at the end of a report?","a":[{"all":[["works cited","bibliography","reference"]],"none":["not"]}],"show":"the works-cited list","pts":2,"why":"In-text citations point to it."},
   {"t":"open","key":"rc_signpost","q":"Week 29: Write the signpost you'll use to begin your conclusion.","min":4,"rows":1,"rubric":["A phrase that signals the conclusion"],"model":"So, what's the answer to my question?"}]},
 "hook": {
  "title": "Look How Far You've Come",
  "visual": YEAR,
  "html": "<p>In Week 1 you studied story elements and how rubrics work. Since then you've written a personal narrative, an informational article, a poetry analysis, an argument speech and a literary analysis of a novel, and now you'll present original research. Each unit built a skill the next one needed: narrative taught you detail, informational writing taught you to cite, poetry taught you to read closely, argument taught you to use evidence and answer counterclaims, the novel taught you to analyze, and research put it all together.</p><div class='callout'><b>Big question:</b> What kind of reader, writer and speaker have you become this year?</div>"},
 "learn": [
  {"title": "Review: Research Questions and Sources",
   "html": "<p>Strong research starts with an open, focused question and its sub-questions (Week 26). Every source is checked before you use it (Week 27): <b>S</b>top, <b>I</b>nvestigate the source, <b>F</b>ind better coverage, <b>T</b>race claims to the original. Ask who made it, why, what evidence it gives and when. Primary sources, government agencies, universities and expert organizations usually beat anonymous posts and ads.</p>",
   "checks": [
    {"t":"open","key":"rvsource","q":"Rank these three sources from most to least reliable for a report on Florida springs, and explain your top and bottom choices: a tube-rental company's blog, a U.S. Geological Survey report, a classmate's social media post.","min":30,"rows":3,"rubric":["A sensible ranking","Explains the most reliable choice","Explains the least reliable choice"],"model":"1. The USGS report, because government scientists collect data and show their methods. 2. The tube-rental blog, which may have some local facts but wants to sell rentals. 3. The classmate's post, because there's no evidence or expert author."}]},
  {"title": "Review: Synthesizing and Citing",
   "html": "<p>A strong paragraph has a topic sentence, evidence from more than one source joined with transitions (also, however, similarly, as a result), commentary explaining what the evidence means, and an in-text citation for every borrowed fact, paraphrase or quotation (Week 28). Paraphrase in your own words and structure; quote only when the exact wording matters.</p>",
   "checks": [
    {"t":"open","key":"rvsynth","q":"Join these into one sentence with a transition and two citations: Source A (Florida Fish and Wildlife Conservation Commission) says manatees need water warmer than about 68°F in winter. Source B (Save the Manatee Club) says many manatees gather at power plant outflows.","min":20,"rows":2,"rubric":["One sentence combining both sources","A transition","Credits both sources"],"model":"Manatees need water warmer than about 68°F in winter (Florida Fish and Wildlife Conservation Commission), so many of them gather at the warm outflows of power plants (Save the Manatee Club)."}]},
  {"title": "The Year in Review: Skills That Connect",
   "html": "<p>Your research presentation uses skills from every unit:</p><ul><li><b>Unit 1 (narrative):</b> a vivid story or scene to hook the audience.</li><li><b>Unit 2 (informational):</b> central idea, text structure and citations.</li><li><b>Unit 3 (poetry):</b> precise, vivid word choice.</li><li><b>Unit 4 (argument):</b> evidence for every claim and answers to opposing views.</li><li><b>Unit 5 (novel):</b> close reading and commentary that explains how evidence works.</li><li><b>Unit 6 (research):</b> questions, reliable sources, synthesis and presentation.</li></ul>",
   "checks": [
    {"t":"open","key":"rvconnect","q":"Choose two earlier units and explain exactly how a skill from each one appears in your research presentation.","min":30,"rows":3,"rubric":["Two earlier units named","A specific skill from each","Shows where it appears in the presentation"],"model":"From Unit 1, I open with a short scene of my family seeing green water at the beach, using sensory details. From Unit 4, I answer the counterclaim that blooms are natural by showing the data on fertilizer runoff."}]}],
 "handson": {
  "title": "Deliver Your Research Presentation",
  "intro": "Present your research to a live audience, answer questions and reflect on your growth.",
  "materials": ["Your slides or poster from Week 29", "Your note cards", "A computer or tablet to show slides (if using slides)", "A timer", "A phone or tablet to record (optional)", "An audience of at least two people (family, co-op friends or grandparents on a video call)", "The Unit 6 project rubric"],
  "steps": [
   "Set up your space so the audience can see your visuals. Do one last quick run-through of your opening.",
   "Give the audience the Unit 6 project rubric so they know what to watch for.",
   "Present for 4 to 6 minutes, with a timer running where you can't see it. Record if you can.",
   "Hold a Q&A of at least 3 minutes. Repeat each question before answering.",
   "Ask each audience member for one specific strength and one specific suggestion, then watch your recording if you have one.",
   "If you present on a video call, use a call your parent sets up, and share only your first name."],
  "record": [
   {"t":"open","key":"deliverrec","q":"How long did you present? What questions were you asked, and what feedback did you receive?","min":40,"rows":4,"rubric":["Time reported","Questions listed","Specific feedback listed"],"model":"I presented for 5 minutes 20 seconds. Grandma asked whether the blooms hurt fish, and my uncle asked who pays for the reservoir; I said I'd need to research the second one. Feedback: my map was very clear and I spoke slowly, but I looked at the screen too much during the second finding."},
   {"t":"open","key":"growthrec","q":"Compare this presentation with your Week 20 argument speech. Name one way you improved and one goal for next year.","min":30,"rows":3,"rubric":["A specific improvement with evidence","A specific goal"],"model":"In Week 20 I rushed and said \"um\" a lot; this time I paused after key facts and used note cards with key words, so I hardly said \"um.\" Next year I want to look at my audience more instead of the screen."}]},
 "think": {
  "intro": "Your teacher scores this.",
  "items": [
   {"t":"open","key":"yearreflect","q":"Choose the piece of writing you're proudest of this year (narrative, article, poetry analysis, argument, literary analysis or research). Explain why, using specific details, and describe how one skill you learned in it showed up again later in the year.","min":67,"rows":6,"rubric":["Names a piece and explains why with specific details","Traces one skill into a later unit","Reflects honestly on growth"],"model":"I'm proudest of my argument essay about adding more water fountains to parks, because I answered the counterclaim about cost with real numbers from our city budget. That same skill, using evidence and answering the other side, showed up in my research report when I explained why some people say algae blooms are natural and showed the data that runoff makes them worse. I used to only list facts, but now I explain how the evidence proves my point."}]},
 "checkpoint": {
  "title": "Unit 6 Checkpoint: Research and Presentation",
  "intro": "This checkpoint covers Weeks 26 to 29. Part A uses an invented practice source; reread it as often as you like. You may not use notes. Mastery is 85 or higher. If you score below 85, your teacher will review with you, then you will retake it.",
  "parts": [
   {"title": "Part A: Evaluate a source", "items": [
    {"t":"open","key":"cpeval","q":SOURCE + "<p>Evaluate this source's reliability for a research report on spring flow. Use at least three specific clues from the source.</p>","min":40,"rows":4,"pts":6,"rubric":["A clear judgment of reliability","Three specific clues from the source","Explains how each clue affects reliability"],"model":"It's not reliable. The author is \"Big Jim,\" the owner of a tube-rental business, so he wants people to keep buying rentals. His only evidence is that he hasn't noticed a change, which is personal opinion, not data. There's no date, and the post ends with a discount code, which shows its purpose is to sell."},
    {"t":"open","key":"cpsift","q":"Name the SIFT move you would use next with this source, and describe exactly what you would do.","min":20,"rows":2,"pts":4,"rubric":["Names a SIFT move","Describes a specific action that fits the move"],"model":"Find better coverage: I'd search for spring-flow data from the St. Johns River Water Management District or the U.S. Geological Survey to see what measurements show."},
    {"t":"open","key":"cpclaim","q":"The source says \"so-called scientists claim flow is down.\" Explain how a reader can check whether that claim is true.","min":20,"rows":2,"pts":4,"rubric":["Describes tracing the claim to original data or experts","Names a type of reliable source"],"model":"I'd trace the claim to the original studies by looking for reports from the water management district or university scientists, then read their actual flow measurements instead of trusting the tube company's summary."}]},
   {"title": "Part B: Research skills", "items": [
    {"t":"open","key":"cprq","q":"\"Florida\" is a topic, not a research question. Write a strong research question about Florida and two sub-questions that would help answer it.","min":20,"rows":3,"pts":4,"rubric":["An open, focused research question","Two sub-questions that each help answer it"],"model":"How have invasive Burmese pythons changed the Everglades? Sub-questions: How did pythons get into the Everglades? Which native animals have declined since pythons spread?"},
    {"t":"text","q":"What do we call using someone else's words or ideas without giving credit, even by accident?","a":[{"all":[["plagiari"]],"none":["not"]}],"show":"plagiarism","pts":3,"why":"Cite every borrowed idea."},
    {"t":"open","key":"cpparaphrase","q":"Paraphrase this practice statement and add an in-text citation: \"Burmese pythons have spread across thousands of square miles of South Florida, where they eat native mammals and birds\" (U.S. Geological Survey).","min":15,"rows":2,"pts":4,"rubric":["Own words and sentence structure","Keeps the meaning","Includes an in-text citation"],"model":"Across a huge area of South Florida, invasive pythons are eating native birds and mammals (U.S. Geological Survey)."},
    {"t":"open","key":"cppresent","q":"Name two things a presenter can do to help an audience understand and trust numbers from research.","min":15,"rows":2,"pts":4,"rubric":["Two specific, valid techniques"],"model":"Round and compare the number, like \"about one-third,\" and name the source aloud, like \"according to the U.S. Geological Survey.\""}]},
   {"title": "Part C: Write a synthesized paragraph", "items": [
    {"t":"open","key":"cpparagraph","q":"<p>Write one paragraph (5 to 7 sentences) that answers this question: <b>Why are Florida's springs worth protecting?</b> Use both practice sources below, connect them with transitions, cite each one, and add your own commentary.</p><div class='callout'><b>Source 1 (practice, adapted from Florida State Parks):</b> Florida's springs stay about 68 to 72°F all year, giving manatees warm water in winter.<br><b>Source 2 (practice, adapted from the Florida Geological Survey):</b> Springs are windows into the Floridan aquifer, which supplies most of the state's drinking water.</div>","min":70,"rows":7,"pts":8,"rubric":["A topic sentence that answers the question","Accurate evidence from both sources with citations","Transitions that connect the sources","Commentary that explains why the evidence matters","Correct conventions"],"model":"Florida's springs are worth protecting because they support both wildlife and people. Springs stay about 68 to 72°F all year, so they give manatees a warm place to survive cold winters (Florida State Parks). In addition, springs are windows into the Floridan aquifer, the source of most of the state's drinking water (Florida Geological Survey). This means that when a spring is polluted or loses flow, it's a warning sign about the water families drink every day. Protecting springs protects manatees, the aquifer and Floridians themselves."}]}]},
 "next": "Congratulations on finishing Grade 6! Next: the end-of-year comprehensive mastery test."
}

TEACHER = {
 "standards": [
  "ELA.6.C.2.1: Present information orally, in a logical sequence, using nonverbal cues, appropriate volume, clear pronunciation, and appropriate pacing.",
  "ELA.6.C.4.1: Conduct research to answer a question, drawing on multiple reliable and valid sources, and refocusing the inquiry when appropriate.",
  "ELA.6.C.5.1: Integrate diverse digital media to enhance audience engagement in oral or written tasks.",
  "ELA.6.C.1.4: Write expository texts to explain and/or analyze information from multiple sources, using relevant supporting details and a logical organizational pattern.",
  "ELA.K12.EE.1.1: Cite evidence to explain and justify reasoning."],
 "materials": ["The interactive lesson", "The student's slides or poster and note cards, a device to show slides, a timer, optional recording device, an audience", "The Unit 6 project rubric", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run one question from each week of the unit."],
  [4, "Hook", "The year's path: six units, six products."],
  [8, "Sources", "Rank three sources."],
  [8, "Synthesis and citation", "Join two manatee sources."],
  [8, "The year in review", "Trace two earlier skills into the presentation."],
  [16, "Presentation", "The student delivers the research presentation (or schedules it this week) and holds the Q&A; score with the Unit 6 rubric."],
  [10, "Checkpoint preview", "Explain that the checkpoint is completed after class, independently, one try per item, with no answers shown until you review it. Notes may not be used. Mastery is 85; below 85 means a review lesson and a retake."]],
 "key_questions": ["Who made this source, and why?", "Where does each borrowed fact come from?", "How did a skill from an earlier unit help you here?", "What will you do differently next year?"],
 "misconceptions": ["A personal experience is the same as data.", "Paraphrasing means changing a few words.", "A source with a professional-looking design is reliable.", "A presentation is the report read aloud."],
 "support": ["Allow the presentation to be delivered to a small audience first, then repeated.", "Provide a paragraph frame for Part C.", "Review the SIFT bookmark before the checkpoint."],
 "challenge": ["Present to an audience outside the family, such as a library group or co-op class.", "Turn the research into a letter to a local official or newspaper."],
 "background": "<p>The Part A source and the Part C sources are invented or adapted for practice and are labeled that way for students. Florida State Parks describes spring temperatures of about 68 to 72°F (verify before release); the Floridan aquifer supplies drinking water to most Floridians. The research presentation is scored with the Unit 6 project rubric. Verify standard wording against CPALMS before release.</p>",
 "sources": ["Florida Department of Education, B.E.S.T. Standards for English Language Arts (2020).", "Caulfield, Mike, and Sam Wineburg, Verified (2023).", "Florida State Parks, Florida Springs."]
}

PRINT = {
 "directions": "Answer in complete sentences.",
 "items": [
  {"q":"List the four SIFT moves.","a":"Stop; investigate the source; find better coverage; trace claims to the original.","lines":2},
  {"q":"Name three clues that a source may not be reliable.","a":"No author or expert; selling something; no date; no evidence; opinion presented as fact.","lines":2},
  {"q":"Paraphrase with a citation: \"Gopher tortoise burrows shelter more than 350 other species\" (practice statement, adapted from FWC).","a":"Model: Hundreds of other kinds of animals use gopher tortoise burrows for shelter (FWC).","lines":2},
  {"q":"What is the difference between a topic and a research question? Give an example.","a":"A topic is a subject; a research question is an open, focused question, such as How do springs help manatees survive winter?","lines":2},
  {"q":"Write one specific strength and one specific suggestion for a presentation you watched this week.","a":"Model: Your map made the spread easy to see; next time, face the audience instead of the screen.","lines":2}]
}
