OUTLINE = ('<svg viewBox="0 0 660 250" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Sub-questions become report sections: introduction with the research question, three body sections each answering a sub-question with evidence from two sources, and a conclusion">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">From sub-questions to sections: the report blueprint</text>'
  '<rect x="30" y="36" width="600" height="34" rx="8" fill="#0A1F3D"/><text x="330" y="58" text-anchor="middle" fill="#fff" font-weight="bold">Introduction: hook, background, research question, preview of answer</text>'
  + ''.join(f'<rect x="{30+i*204}" y="84" width="192" height="104" rx="8" fill="{c}"/><text x="{126+i*204}" y="104" text-anchor="middle" fill="#fff" font-weight="bold">Section {i+1}</text><text x="{126+i*204}" y="122" text-anchor="middle" fill="#fff" font-size="11">answers sub-question {i+1}</text><text x="{126+i*204}" y="142" text-anchor="middle" fill="#fff" font-size="11">topic sentence</text><text x="{126+i*204}" y="158" text-anchor="middle" fill="#fff" font-size="11">evidence from 2+ sources</text><text x="{126+i*204}" y="174" text-anchor="middle" fill="#fff" font-size="11">explanation and citation</text>'
            for i, c in enumerate(["#0047BA", "#2c6e22", "#8a6d1f"])) +
  '<rect x="30" y="202" width="600" height="34" rx="8" fill="#DB2F30"/><text x="330" y="224" text-anchor="middle" fill="#fff" font-weight="bold">Conclusion: answer the question, why it matters, what\'s still unknown</text></svg>')

LESSON = {
 "unit": "Unit 6: Research and Presentation",
 "title": "Organizing and Drafting a Report",
 "subtitle": "You have a question and reliable sources. Now you turn a pile of notes into a clear report. This week you sort notes into sections, synthesize sources that agree and disagree, write introductions and conclusions that hook and land, and draft your research report with accurate citations, ready to become next week's presentation.",
 "objectives": [
  "Organize research notes into an outline built from sub-questions.",
  "Synthesize information from several sources, including sources that disagree.",
  "Paraphrase and quote correctly with in-text citations and a works-cited list.",
  "Write an introduction that hooks readers and states the research question, and a conclusion that answers it.",
  "Draft a research report using varied transitions and precise vocabulary."],
 "vocab": [
  ["outline", "A plan that organizes the main ideas and supporting details of a piece of writing."],
  ["synthesize", "To combine information from several sources into a new understanding."],
  ["in-text citation", "A short note in the text, such as the author or organization, showing where information came from."],
  ["works cited", "A list at the end of a report of every source used."],
  ["transition", "A word or phrase that connects ideas, such as however, as a result or in contrast."],
  ["draft", "An early version of writing that will be revised."]],
 "reconnect": {
  "title": "Week 27: Judging sources",
  "intro": "Only reliable sources make it into your report.",
  "items": [
   {"t":"text","q":"What do the letters in SIFT stand for? Type the four words in order.","a":[{"all":[["stop"],["investigate"],["find"],["trace"]],"none":["not"]}],"show":"Stop, Investigate, Find, Trace","pts":2,"why":"The fact-checker's four moves."},
   {"t":"text","q":"What is false information spread on purpose to deceive called?","a":[{"all":[["disinformation"]],"none":["not"]}],"show":"disinformation","pts":2,"why":"Misinformation is shared by mistake."},
   {"t":"open","key":"rc_score","q":"Name your strongest research source and its scorecard total from last week. Why is it your strongest?","min":15,"rows":2,"rubric":["Names a source and score","Explains why it is strongest"],"model":"The South Florida Water Management District site scored 14 of 15. It's strongest because the agency collects the lake data itself and updates it often."}]},
 "hook": {
  "title": "From Pile to Plan",
  "visual": OUTLINE,
  "html": "<p>Imagine 30 note cards scattered across a table: facts, numbers, quotations, ideas. Writing a report straight from that pile is like building a house without a blueprint. Professional writers organize first.</p><p>The good news: you already have your blueprint. Your research question becomes your introduction's focus, and your sub-questions from Week 26 become your report's sections.</p><div class='callout'><b>Big question:</b> How do you turn research into a report that's clear, accurate and worth reading?</div>"},
 "learn": [
  {"title": "Sorting Notes into an Outline",
   "html": "<p>In Week 9 you took note cards. Now sort them:</p><ol><li>Label each card with the sub-question it helps answer (1, 2 or 3).</li><li>Make a pile for each sub-question. Cards that don't fit any pile may not belong in this report, even if they're interesting.</li><li>Within each pile, put the cards in a logical order: background first, then evidence, then effects or solutions.</li><li>Write a <b>topic sentence</b> for each section that answers its sub-question.</li></ol><p>If one pile is tiny, you need more research for that sub-question, or your question needs refocusing (Week 26).</p>",
   "checks": [
    {"t":"open","key":"sortcards","q":"A student researching \"Why do algae blooms spread from Lake Okeechobee, and what could stop them?\" has these notes. Sort them into three sections and name each: (a) farm fertilizer runoff adds phosphorus; (b) water released east and west carries algae to the coasts; (c) blooms can make people and pets sick; (d) a reservoir south of the lake will clean water; (e) warm summer water helps algae grow; (f) Everglades restoration sends water south instead.","min":11,"rows":4,"rubric":["Three sensible sections with names","Each note placed logically"],"model":"Causes: (a) and (e). Spread and effects: (b) and (c). Solutions: (d) and (f)."},
    {"t":"open","key":"topicsent","q":"Write a topic sentence for the \"Solutions\" section of that report.","min":12,"rows":2,"rubric":["A sentence that states the section's main idea and answers its sub-question"],"model":"Scientists and engineers are working on two big solutions: cleaning the water before it leaves the lake and sending more of it south to the Everglades."}]},
  {"title": "Synthesizing Sources",
   "html": "<p>A report doesn't just list what each source says. It <b>synthesizes</b>: combines sources into one explanation. Use transitions that show how sources relate:</p><ul><li>When sources agree: <i>Both the water district and University of Florida scientists report that...</i></li><li>When one adds to another: <i>The Department of Health adds that...</i></li><li>When sources disagree: <i>However, farm groups argue that... while environmental groups say...</i></li></ul><p>When reliable sources disagree, don't hide it: explain both sides and what the evidence shows. That's what historians did with Sunni Ali in Week 23.</p>",
   "checks": [
    {"t":"open","key":"synthpair","q":"Combine these two notes into one synthesized sentence with a transition: Source A (U.S. Geological Survey): Silver Springs' flow has dropped about 30 percent since the 1930s. Source B (St. Johns River Water Management District): reduced rainfall and groundwater pumping both lower spring flow.","min":20,"rows":2,"rubric":["One or two sentences combining both sources","A transition showing their relationship","Credits both sources"],"model":"According to the U.S. Geological Survey, Silver Springs' flow has dropped about 30 percent since the 1930s, and the St. Johns River Water Management District explains that both less rainfall and groundwater pumping are causes."},
    {"t":"open","key":"disagree","q":"Two reliable sources disagree about how much farms cause Lake Okeechobee's pollution compared with cities and septic tanks. How should a report handle this?","min":25,"rows":3,"rubric":["Presents both views fairly with citations","Explains what evidence supports each or what is still unknown"],"model":"The report should explain both views and name the sources, then describe what the evidence shows, such as measurements of where phosphorus enters the lake, and say clearly if scientists are still studying it, instead of picking one side and hiding the other."}]},
  {"title": "Paraphrasing, Quoting and Citing",
   "html": "<p>In Week 8 you learned to paraphrase without patchwriting, and in Week 9 to cite. In a report:</p><ul><li><b>Paraphrase</b> most information, in your own words and sentence structure.</li><li><b>Quote</b> only when the exact words matter: a powerful statement, a definition or an expert's opinion. Keep quotes short.</li><li>Give an <b>in-text citation</b> every time you use a source: <i>(U.S. Geological Survey)</i> or <i>According to NOAA,...</i></li><li>List every source in a <b>works-cited</b> list: author or organization, title, website or publisher, date, and the web address.</li></ul><p>Using someone's words or ideas without credit is plagiarism, even by accident.</p>",
   "checks": [
    {"t":"open","key":"paraphraseit","q":"Paraphrase this sentence and add an in-text citation: \"Blue-green algae blooms can produce toxins that harm people, pets and wildlife\" (Florida Department of Health).","min":15,"rows":2,"rubric":["Own words and structure","Keeps the meaning","Includes an in-text citation"],"model":"The Florida Department of Health warns that some algae blooms release poisons dangerous to humans, animals and pets."},
    {"t":"open","key":"whencite","q":"Do you need a citation for each of these? Explain briefly: (a) Florida is a state in the southeastern United States. (b) Lake Okeechobee covers about 730 square miles. (c) Your own opinion that the state should act faster.","min":25,"rows":3,"rubric":["(a) no, common knowledge","(b) yes, a specific fact","(c) no, but it should be clearly marked as opinion"],"model":"(a) No, that's common knowledge. (b) Yes, it's a specific figure someone measured, so cite where you found it. (c) No citation, because it's my opinion, but I should make clear it's my view."}]},
  {"title": "Introductions and Conclusions",
   "html": "<p>An <b>introduction</b> has four jobs: hook the reader (a surprising fact, a short scene or a question), give background, state your research question and preview your answer.</p><p>A <b>conclusion</b> answers the research question in a sentence or two, explains why it matters, and notes what's still unknown or what readers could do. Don't just repeat the introduction.</p><p>Example hook: <i>In the summer of 2018, families on Florida's coasts couldn't swim at their beaches: thick green algae covered the water.</i></p>",
   "checks": [
    {"t":"open","key":"writehook","q":"Write a hook for a report on your own research question. Label which kind of hook it is (surprising fact, short scene or question).","min":15,"rows":2,"rubric":["A hook connected to the student's question","Labeled correctly"],"model":"Short scene: The water in Silver Springs used to be so clear that glass-bottom boat riders could see fish 30 feet down; today, on some days, they can barely see the bottom."}]}],
 "handson": {
  "title": "Floor Outline and First Draft",
  "intro": "Physically build your report's structure, then draft it.",
  "materials": ["Your research note cards or notes (rewrite onto index cards if needed)", "About 10 extra index cards and a marker", "Painter's tape or string", "Paper and pencil, or a computer for typing", "A family member"],
  "steps": [
   "Make labels on index cards: Introduction, Section 1, Section 2, Section 3, Conclusion. Lay them in a row on the floor or a table.",
   "Place each note card under the section it supports. Put any card that doesn't fit in a \"parking lot\" pile.",
   "Walk the outline and explain your report aloud to a family member, section by section. Where they look confused, rearrange or add a card.",
   "Write a topic sentence card for each section. Then draft your report (about 400 to 700 words) from the outline, citing sources in the text.",
   "Write your works-cited list, checking each source's author, title, date and web address.",
   "Peel up tape when you're done so no one slips."],
  "record": [
   {"t":"open","key":"outlinerec","q":"Write your outline: your research question, each section's topic sentence, and which sources support each section. What went into the parking lot, and why?","min":50,"rows":5,"rubric":["Research question and topic sentences","Sources named for each section","Explains the parking lot choices"],"model":"Question: Why do algae blooms spread from Lake Okeechobee, and what could stop them? Section 1: Fertilizer runoff and warm water feed the blooms (SFWMD, UF/IFAS). Section 2: Water releases carry algae to both coasts, harming people and pets (Florida Department of Health, news). Section 3: A new reservoir and Everglades restoration could help (Army Corps of Engineers, SFWMD). Parking lot: a fact about the lake's fish, which is interesting but doesn't answer my question."},
   {"t":"open","key":"draftrec","q":"Paste or copy your introduction and one body paragraph from your draft, with in-text citations.","min":89,"rows":8,"rubric":["An introduction with a hook, background, question and preview","A body paragraph with a topic sentence, synthesized evidence and citations","Paraphrased in the student's own words"],"model":"In the summer of 2018, families on Florida's coasts couldn't swim at their beaches: thick green algae covered the water. The algae came from Lake Okeechobee, Florida's largest lake. Why do these blooms keep spreading, and what could stop them? Fertilizer, warm water and water releases are to blame, but new projects offer hope. Fertilizer from farms and lawns washes into the lake, adding phosphorus that feeds algae (South Florida Water Management District). University of Florida scientists add that summer heat speeds the algae's growth, so blooms explode in July and August (UF/IFAS). Together, extra nutrients and heat turn the lake into an algae factory."}]},
 "think": {
  "intro": "Your teacher scores these.",
  "items": [
   {"t":"open","key":"synthvslist","q":"Explain the difference between a report that lists sources (\"Source A says... Source B says...\") and one that synthesizes them. Why do readers prefer synthesis? Use an example from your research.","min":49,"rows":5,"rubric":["Explains listing versus synthesizing","Explains why synthesis helps readers","An example from the student's research"],"model":"A list report makes readers do the thinking, jumping from source to source. A synthesized report connects them into one explanation, showing where they agree and how they add to each other. For example, instead of listing what the water district and UF said separately, I combined them to show that nutrients and heat together cause the blooms."},
   {"t":"open","key":"plagiarismwhy","q":"Why is citing sources important beyond avoiding trouble? Give at least two reasons, connecting to what you learned in Week 27.","min":38,"rows":4,"rubric":["At least two reasons","A connection to judging sources or trust"],"model":"Citations let readers check your facts, just as we checked sources with SIFT in Week 27, so they make your report trustworthy. They also give credit to the scientists and writers who did the work, like the credit Rosalind Franklin deserved for her DNA photograph."}]},
 "exit": [
  {"t":"text","q":"What do we call combining information from several sources into one new understanding?","a":[{"all":[["synthes"]],"none":["not"]}],"show":"synthesizing","pts":2,"why":"Not just listing sources."},
  {"t":"open","key":"exit_intro","q":"Name two jobs of a report's introduction.","min":6,"rows":2,"rubric":["Two correct jobs"],"model":"Hook the reader and state the research question."},
  {"t":"open","key":"exit_quote","q":"When should you quote a source instead of paraphrasing?","min":8,"rows":2,"rubric":["A reason from the lesson for keeping exact words"],"model":"When the exact words matter, such as a powerful statement or an expert's opinion."}],
 "next": "Week 29: speaking and presenting."
}

TEACHER = {
 "standards": [
  "ELA.6.C.1.4: Write expository texts to explain and/or analyze information from multiple sources, using a logical organizational structure, relevant elaboration, and varied transitions.",
  "ELA.6.C.4.1: Conduct research to answer a question, drawing on multiple reliable and valid sources, and refocusing the inquiry when appropriate.",
  "ELA.K12.EE.1.1: Cite evidence to explain and justify reasoning."],
 "materials": ["The interactive lesson", "The student's research notes, about 10 extra index cards, a marker, painter's tape or string", "Paper and pencil or a computer", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 27 warm-up questions."],
  [4, "Hook", "From a pile of notes to a blueprint."],
  [12, "Outlining", "Sort the algae notes; write a topic sentence."],
  [12, "Synthesizing", "Combine two sources; handle disagreement."],
  [11, "Paraphrasing and citing", "Paraphrase with a citation; when to cite."],
  [9, "Introductions and conclusions", "Write a hook for your own report."],
  [6, "Assign", "Set up the floor outline; assign the draft, Think Deeper and the Exit Check."]],
 "key_questions": ["Which sub-question does this note answer?", "How do these sources connect?", "Is this in your own words, and is it cited?", "Does your conclusion answer the question?"],
 "misconceptions": ["A report is a list of facts.", "Changing a few words makes a paraphrase.", "Only quotations need citations.", "The conclusion should repeat the introduction."],
 "support": ["Provide an outline template with three sections.", "Offer transition word banks for agreeing and disagreeing sources.", "Let the student dictate the first draft."],
 "challenge": ["Add a section comparing two possible solutions with evidence for each.", "Add a chart or map with a caption and citation."],
 "background": "<p>The research report drafted this week becomes the script for Week 29's presentation and the final research presentation in Week 30 (see the Unit 6 projects page). Lake Okeechobee and Silver Springs examples use practice figures drawn from public sources and should be checked by students in their own research.</p>",
 "sources": ["Florida Department of Education, B.E.S.T. Standards for English Language Arts (2020).", "Purdue Online Writing Lab, MLA Formatting and Style Guide."]
}

PRINT = {
 "directions": "Answer in complete sentences.",
 "items": [
  {"q":"How do sub-questions help you organize a report?","a":"Each sub-question becomes a body section.","lines":2},
  {"q":"Combine into one sentence with a transition: Source A says manatees gather at warm springs in winter. Source B says power plant outflows also draw manatees.","a":"Model: Manatees gather at warm springs in winter (Source A), and power plant warm-water outflows also attract them (Source B).","lines":2},
  {"q":"Paraphrase with a citation: \"Sea turtles nest on Florida beaches from March through October\" (FWC).","a":"Model: From spring through mid-fall, sea turtles lay eggs on Florida's beaches (FWC).","lines":2},
  {"q":"List the four jobs of an introduction.","a":"Hook, background, research question, preview of the answer.","lines":2},
  {"q":"What should a conclusion do?","a":"Answer the question, explain why it matters, note what's unknown or what readers can do.","lines":2}]
}
