SRC_A = ("<div class='card'><p style='font-size:12px;color:#5b6676;margin:0 0 6px'>Practice Source A. Written for this lesson; the author's name is invented. The facts are real.</p>"
 "<h3 style='margin-top:0'>Rainforests of the Sea: Florida's Coral Reef</h3><p style='margin-top:-6px'><i>by Grace Okafor · KCE Practice Reader · 2026</i></p>"
 "<p><b>[1]</b> Off the coast of South Florida lies a living wonder. Florida's Coral Reef stretches about 350 miles, from the Dry Tortugas west of Key West to St. Lucie Inlet in Martin County. It is the only coral barrier reef in the continental United States and one of the largest barrier reef systems in the world.</p>"
 "<p><b>[2]</b> Although corals can look like rocks or plants, they are animals. Each coral is a colony of tiny animals called polyps. Inside their bodies live microscopic algae. The algae use sunlight to make food through photosynthesis and share it with the coral. In return, the coral gives the algae shelter. The algae also give corals much of their color.</p>"
 "<p><b>[3]</b> Reefs are called the rainforests of the sea because so many living things depend on them. Fish, lobsters, sea turtles and sponges find food and shelter among the corals. Reefs also protect people. A 2014 study found that coral reefs can reduce the energy of waves by up to 97 percent before they reach the shore, which helps protect coasts from storms.</p>"
 "<p><b>[4]</b> But Florida's reef is in trouble. When the water stays too hot for too long, corals push out their algae and turn white. This is called coral bleaching. Without their algae, corals begin to starve. In the summer of 2023, a record marine heat wave struck the Florida Keys. A water sensor in Manatee Bay recorded about 101°F, and corals across the reef bleached.</p></div>")

SRC_B = ("<div class='card'><p style='font-size:12px;color:#5b6676;margin:0 0 6px'>Practice Source B. Written for this lesson; the organization's name is invented. The facts are real.</p>"
 "<h3 style='margin-top:0'>Fact Sheet: Saving Florida's Reef</h3><p style='margin-top:-6px'><i>Sunshine Ocean Alliance · Updated 2026 · no author listed</i></p>"
 "<ul><li><b>Disease:</b> Stony coral tissue loss disease was first seen near Miami in 2014. It has spread along most of Florida's reef and attacks more than 20 kinds of coral.</li>"
 "<li><b>Coral nurseries:</b> Groups such as the Coral Restoration Foundation in Key Largo grow young corals on underwater \"trees\" made of pipe, then plant them back on the reef.</li>"
 "<li><b>Mission: Iconic Reefs:</b> In 2019, the National Oceanic and Atmospheric Administration (NOAA) launched a plan to restore seven important reef sites in the Florida Keys.</li>"
 "<li><b>During the 2023 heat wave:</b> Some scientists moved nursery corals to deeper, cooler water or to tanks on land to save them.</li>"
 "<li><b>What you can do:</b> Use less fertilizer, which can wash into the ocean and feed harmful algae; never touch or stand on coral; and choose reef-safe sunscreen.</li></ul></div>")

CARD = ('<svg viewBox="0 0 620 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="A sample research note card">'
  '<text x="310" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Anatomy of a research note card</text>'
  '<rect x="120" y="36" width="380" height="180" rx="6" fill="#fffef5" stroke="#C9A84C" stroke-width="2"/>'
  + ''.join(f'<line x1="130" y1="{y}" x2="490" y2="{y}" stroke="#d8e6f3"/>' for y in range(100, 210, 22)) +
  '<line x1="120" y1="80" x2="500" y2="80" stroke="#DB2F30"/>'
  '<text x="135" y="62" font-weight="bold">Threats: bleaching</text><text x="485" y="62" text-anchor="end" font-weight="bold" fill="#0047BA">Source A</text>'
  '<text x="135" y="104">- Hot water for a long time makes corals push out</text><text x="135" y="126">  their algae, so they turn white and starve.</text>'
  '<text x="135" y="148">- Summer 2023: record heat wave in the Keys.</text>'
  '<text x="135" y="170">- Quote: water reached \"about 101°F\" (para. 4)</text>'
  '<text x="485" y="206" text-anchor="end" font-size="11" fill="#5b6676">card 3</text>'
  '<path d="M118 58 H60" stroke="#0A1F3D"/><text x="56" y="54" text-anchor="end" font-size="11">subtopic</text><text x="56" y="67" text-anchor="end" font-size="11">heading</text>'
  '<path d="M502 58 H550" stroke="#0A1F3D"/><text x="554" y="54" font-size="11">which</text><text x="554" y="67" font-size="11">source</text>'
  '<path d="M118 115 H60" stroke="#0A1F3D"/><text x="56" y="112" text-anchor="end" font-size="11">notes in</text><text x="56" y="125" text-anchor="end" font-size="11">your words</text>'
  '<path d="M502 170 H550" stroke="#0A1F3D"/><text x="554" y="166" font-size="11">exact words</text><text x="554" y="179" font-size="11">in quotes</text></svg>')

LESSON = {
 "unit": "Unit 2: Explaining the World (Informational)",
 "title": "Writing to Inform: Research Notes and Citations",
 "subtitle": "Researchers gather facts from more than one source, take notes in their own words, and give credit to every source they use.",
 "objectives": [
  "Write a focused research question.",
  "Take note cards that are organized by subtopic, labeled by source and written in your own words.",
  "Use quotation marks for exact words and record where they came from.",
  "Combine information from two sources on the same subtopic.",
  "Write MLA-style works cited entries and in-text citations."],
 "vocab": [
  ["research question", "A focused question that guides what information you look for."],
  ["source", "A book, article, website, interview or other place information comes from."],
  ["note card", "A card with notes on one subtopic from one source."],
  ["quotation", "An author's exact words, shown with quotation marks and credited."],
  ["citation", "Information that tells readers exactly where an idea or quote came from."],
  ["works cited", "The list of sources at the end of a piece of writing, in alphabetical order."],
  ["in-text citation", "A short note in parentheses, such as (Okafor), that points to a works cited entry."],
  ["synthesize", "To combine information from more than one source into one idea."]],
 "reconnect": {
  "title": "Week 8: Summarizing without copying",
  "intro": "Good notes are tiny summaries. Review first.",
  "items": [
   {"t":"text","q":"What is the word for presenting someone else's words or ideas as your own?","a":["plagiarism","plagiarizing"],"show":"plagiarism","pts":2,"why":"Plagiarism. Today you learn how to avoid it with citations."},
   {"t":"num","q":"Under last week's warning rule, if this many words in a row match the original, you should rewrite them or use quotation marks. What is the number?","a":4,"unit":"words","pts":2,"why":"The 4-word check."},
   {"t":"open","key":"rc_para","q":"Paraphrase this sentence from Source A in today's lesson: \"Reefs are called the rainforests of the sea because so many living things depend on them.\"","min":12,"rows":2,"rubric":["Same meaning; new wording and structure; no 4 or more words in a row copied"],"model":"Because they support such a huge variety of life, coral reefs are often compared to rainforests."},
   {"t":"text","q":"Which root, taught last week, means \"sailor\" and appears in astronaut?","a":["naut"],"show":"naut","pts":2,"why":"naut = sailor: astronaut, nautical, aeronautics."}]},
 "hook": {
  "title": "Who Said That?",
  "html": "<p>Imagine you read online that coral reefs block almost all of the force of ocean waves. Is it true? Who found that out, and how? If you write it in a report, how will your reader know you did not just make it up?</p><p>Real researchers answer these questions with <b>notes</b> and <b>citations</b>. A citation is like a trail of breadcrumbs: it lets any reader follow you back to the exact place you found a fact. It also gives credit to the people who did the work, which is the honest thing to do.</p><div class='callout'><b>This week:</b> you will research Florida's Coral Reef using two practice sources, and then start research for your own informational article, the Unit 2 project.</div>"},
 "learn": [
  {"title": "Start with a Research Question",
   "html": "<p>Research begins with a <b>focused question</b>. A question that is too broad (\"What about the ocean?\") leads to too much information. One that is too narrow (\"How hot was Manatee Bay on July 24, 2023?\") can be answered in one sentence.</p><div class='callout'><b>Too broad:</b> What about coral reefs?<br><b>Too narrow:</b> What year was stony coral tissue loss disease found?<br><b>Just right:</b> What is threatening Florida's Coral Reef, and what are people doing to save it?</div><p>A good research question cannot be answered with yes or no, needs more than one source, and fits the length of what you are writing.</p>",
   "checks": [
    {"t":"open","key":"rq","q":"Label each research question too broad, too narrow or just right, and explain one: (1) How do sea turtles find their way across the ocean? (2) What is a turtle? (3) How many eggs did one turtle lay on Juno Beach in 2024?","min":25,"rows":3,"rubric":["1 just right; 2 too broad (and simple); 3 too narrow","Explanation tied to scope (one-sentence answer, or too much information)"],"model":"(1) Just right, (2) too broad, (3) too narrow. Question 3 is too narrow because one number answers it, so there is nothing to research or explain."},
    {"t":"open","key":"rqmine","q":"Write a just-right research question about a topic you care about that you could research for your Unit 2 informational article.","min":10,"rows":2,"rubric":["Open-ended (not yes/no)","Focused enough for a short article","Needs more than one source"],"model":"How do hurricanes form, and how do scientists predict where they will go?"}]},
  {"title": "Read Two Sources",
   "html": SRC_A + SRC_B + "<p>Read both sources once for meaning. Notice how they are different: Source A is an article by an author, written in paragraphs. Source B is a fact sheet from an organization, written in bullet points, with no author listed.</p>",
   "checks": [
    {"t":"open","key":"diffsrc","q":"Name one subtopic both sources cover, and one piece of information that appears in only one source.","min":20,"rows":2,"rubric":["Shared subtopic: the 2023 heat wave or bleaching (or threats to the reef)","A fact found in only one source (disease, nurseries, wave protection, Mission: Iconic Reefs, what you can do)"],"model":"Both sources cover the 2023 heat wave. Only Source B tells about stony coral tissue loss disease."},
    {"t":"text","q":"In Source A, paragraph 2, what living things inside coral make food through photosynthesis?","a":[{"all":[["algae","alga"]],"none":["not"]}],"show":"algae","pts":2,"why":"Microscopic algae live inside the polyps and share the food they make. You learned about photosynthesis in Science last week."},
    {"t":"open","key":"reliable","q":"Source B lists no author. What else could you check to decide whether a fact sheet like this is reliable?","min":20,"rows":2,"rubric":["Who published it (a known science or government organization); date updated; whether facts match other trusted sources; whether it names its sources"],"model":"I could check who published it and whether it is a trusted science group, how recently it was updated, and whether its facts match other reliable sources, like NOAA."}]},
  {"title": "Take Note Cards",
   "visual": CARD,
   "html": "<p>A note card holds notes on <b>one subtopic</b> from <b>one source</b>. Each card has:</p><ul><li>A <b>subtopic heading</b> at the top (Threats: bleaching).</li><li>The <b>source</b> label (Source A).</li><li>Short notes in <b>your own words</b>. Phrases are fine; you do not need full sentences.</li><li>Any <b>exact words</b> inside quotation marks, with the paragraph or page.</li></ul><p>Why one subtopic per card? Because later you can sort the cards into the order of your article. Why label the source? So you never forget where a fact came from, which is how accidental plagiarism happens.</p><p>Copy a quotation only when the exact words matter: a striking phrase, a number or a definition. Everything else, put in your own words, as you practiced last week.</p>",
   "checks": [
    {"t":"open","key":"card1","q":"Make a note card from Source A, paragraph 3. Write a subtopic heading, the source label and two or three notes in your own words.","min":25,"rows":4,"rubric":["Heading names a subtopic (Why reefs matter)","Labeled Source A","Notes in own words: home and food for many animals; protect coasts by reducing wave energy up to 97 percent (2014 study)","No 4 or more words in a row copied without quotation marks"],"model":"Heading: Why reefs matter. Source A. Notes: Fish, lobsters, turtles and sponges live and eat there. Reefs shield coasts from storms. 2014 study: they cut wave energy by as much as 97 percent before waves hit land."},
    {"t":"open","key":"quotecheck","q":"A student's note card says: Corals push out their algae and turn white. It is labeled Source A but has no quotation marks. What is the problem, and how should the student fix it?","min":20,"rows":2,"rubric":["Copied 6 words in a row (\"push out their algae and turn white\") without quotation marks, which could become plagiarism","Fix: put the exact words in quotation marks with para. 4, or paraphrase"],"model":"\"Push out their algae and turn white\" is copied word for word without quotation marks, so it could end up as plagiarism. The student should put those words in quotation marks and add para. 4, or rewrite them, such as: corals lose their algae and go pale."},
    {"t":"open","key":"card2","q":"Make a note card from Source B on the subtopic \"Ways people are helping.\" Include at least three notes in your own words.","min":25,"rows":4,"rubric":["Heading and Source B label","Three accurate notes: nurseries grow corals on underwater trees and replant them; Mission: Iconic Reefs (NOAA, 2019) restoring seven sites; moving corals to cooler water or land tanks in 2023; individual actions","Own words"],"model":"Heading: Ways people are helping. Source B. Notes: Groups grow baby corals on pipe frames underwater and replant them. NOAA's 2019 Mission: Iconic Reefs plan aims to fix 7 sites in the Keys. In the 2023 heat wave, scientists rescued nursery corals by moving them deeper or onto land."}]},
  {"title": "Combine Sources and Give Credit",
   "html": "<p>When two sources speak about the same subtopic, put their notes together to write one stronger paragraph. This is called <b>synthesizing</b>.</p><div class='callout'><b>Synthesized sentence:</b> During the record 2023 heat wave, water in Manatee Bay reached about 101°F and corals across the reef bleached (Okafor), so some scientists moved nursery corals to deeper water or tanks on land to protect them (Sunshine Ocean Alliance).</div><p>The words in parentheses are <b>in-text citations</b>. They point to full entries in the <b>works cited</b> list at the end. This course uses MLA style, which most middle schools use. A basic entry lists:</p><div class='callout'>Author's Last Name, First Name. \"Title of Article.\" <i>Name of Website or Publication</i>, Date, URL.<br><br>Okafor, Grace. \"Rainforests of the Sea: Florida's Coral Reef.\" <i>KCE Practice Reader</i>, 2026.<br>Sunshine Ocean Alliance. \"Fact Sheet: Saving Florida's Reef.\" 2026.</div><p>When there is no author, the entry starts with the title or the organization, and the in-text citation uses that. Entries go in alphabetical order. For a real website, add the full URL at the end.</p>",
   "checks": [
    {"t":"blanks","q":"Complete the MLA entry for this book: Author Mary Ellen Tanaka; title Coral Kingdoms; publisher Pineapple Press; year 2021.","sent":"___, Mary Ellen. Coral Kingdoms. Pineapple Press, ___.","blanks":[["tanaka"],["2021"]],"show":"Tanaka; 2021","pts":2,"why":"The author's last name comes first, then the first name. The year comes after the publisher. (Book titles go in italics.)"},
    {"t":"text","q":"Write the in-text citation for a fact from Source A. Include the parentheses.","a":[{"all":[["okafor"]],"none":["grace"]}],"show":"(Okafor)","pts":2,"why":"An MLA in-text citation uses the author's last name: (Okafor). Add a page number if there is one."},
    {"t":"open","key":"synth","q":"Write two sentences that synthesize both sources on the subtopic \"Threats to Florida's reef.\" Include an in-text citation after each fact.","min":30,"rows":4,"rubric":["Combines a fact from Source A (bleaching from hot water, 2023 heat wave) and Source B (stony coral tissue loss disease)","An in-text citation after each fact: (Okafor) and (Sunshine Ocean Alliance)","Own words"],"model":"Florida's reef faces more than one threat. Water that stays too hot causes corals to lose their algae and bleach, as happened across the reef in 2023 (Okafor), and a disease first found near Miami in 2014 now attacks more than 20 kinds of coral (Sunshine Ocean Alliance)."},
    {"t":"open","key":"order","q":"Which entry comes first in a works cited list, Okafor or Sunshine Ocean Alliance? Explain the rule.","min":10,"rows":2,"rubric":["Okafor","Entries are listed alphabetically by the first word of each entry"],"model":"Okafor comes first, because works cited entries are in alphabetical order, and O comes before S."}]}],
 "handson": {
  "title": "Research Note Card Sort",
  "intro": "Start research for your Unit 2 informational article. You will physically sort your notes into the shape of an article.",
  "materials": ["Index cards (at least 12) or paper cut into cards", "Highlighters or markers in two colors (one for each source)", "Two sources on your topic from the library or a trusted website (encyclopedia, museum, government, science organization)", "Paper clips or envelopes", "A table or the floor for sorting"],
  "steps": [
   "Write your research question from Learn 1 at the top of a sheet of paper.",
   "Find two sources. On one card for each, write the information you need for its works cited entry: author, title, publisher or website, date and URL.",
   "Take at least six note cards (at least two from each source). Mark each card with that source's color. One subtopic per card.",
   "Spread the cards out on a table. Group cards with the same subtopic, even if they come from different sources. Give each group a heading.",
   "Arrange the groups in the order you would write about them. Clip each group together. This is the skeleton of your article."],
  "record": [
   {"t":"open","key":"sortlist","q":"List your research question, your subtopic groups in order, and how many cards are in each group. Which group came from both sources?","min":40,"rows":5,"rubric":["Research question","Two to four subtopic groups in a logical order","Card counts","Identifies at least one group combining both sources"],"model":"Question: How do hurricanes form, and how do scientists predict their paths? Groups: 1. Warm water and wind (3 cards, both sources). 2. How a hurricane grows (2 cards). 3. Hurricane hunters and satellites (2 cards). 4. Staying safe (1 card). Group 1 combines both sources."},
   {"t":"open","key":"workscited","q":"Write the works cited list for your two sources in MLA style, in alphabetical order.","min":20,"rows":4,"rubric":["Two entries with author (or title/organization), title in quotation marks, publication or website, date, URL","Alphabetical order","Correct punctuation"],"model":"National Weather Service. \"Hurricane Safety Tips and Resources.\" National Oceanic and Atmospheric Administration, www.weather.gov/safety/hurricane. Simon, Seymour. Hurricanes. HarperCollins, 2007."}]},
 "think": {
  "intro": "Write in complete sentences. Your teacher scores these.",
  "items": [
   {"t":"open","key":"paragraph","q":"Using your note cards from this lesson, write a short informational paragraph (5 to 7 sentences) answering: What is threatening Florida's Coral Reef, and what are people doing to save it? Begin with a topic sentence, use facts from both sources with in-text citations, and end with a concluding sentence. Then write the works cited list.","min":110,"rows":10,"rubric":["Topic sentence answers the question","Facts from both sources, accurate and in own words","In-text citations after borrowed facts","Concluding sentence","Correct works cited list in alphabetical order"],"model":"Florida's Coral Reef, the only coral barrier reef in the continental United States, faces serious threats, but people are fighting to save it. When ocean water stays too hot, corals lose the algae that feed them and turn white, which happened across the reef during the record heat wave of 2023 (Okafor). A disease first found near Miami in 2014 has also spread along most of the reef (Sunshine Ocean Alliance). To help, groups grow young corals on underwater frames and plant them back on the reef, and NOAA has a plan to restore seven key sites in the Keys (Sunshine Ocean Alliance). Ordinary people can help, too, by using less fertilizer and never touching coral. With science and care, the reef may still have a future.\n\nWorks Cited\nOkafor, Grace. \"Rainforests of the Sea: Florida's Coral Reef.\" KCE Practice Reader, 2026.\nSunshine Ocean Alliance. \"Fact Sheet: Saving Florida's Reef.\" 2026."},
   {"t":"open","key":"whycite","q":"Bessie Coleman's story (Week 8) was written using books and museum websites. Explain two reasons writers cite their sources, even when they put everything in their own words.","min":45,"rows":4,"rubric":["Gives credit for others' ideas and research, even when paraphrased (avoids plagiarism)","Lets readers check facts and learn more; builds trust"],"model":"First, ideas belong to the people who discovered or wrote them, so even a paraphrase needs credit, or it is still plagiarism. Second, citations let readers check the facts and find more information, which makes the writing more trustworthy."}]},
 "exit": [
  {"t":"open","key":"exit_card","q":"Name the four parts of a research note card.","min":10,"rows":2,"rubric":["Subtopic heading, source label, notes in own words, quotations in quotation marks with location"],"model":"A subtopic heading, the source label, notes in my own words, and any exact words in quotation marks with the paragraph or page."},
  {"t":"text","q":"What is the name of the list of sources at the end of an MLA paper?","a":[{"all":[["works cited"]],"none":["not"]},"bibliography"],"show":"works cited","pts":2,"why":"In MLA style, the list is called Works Cited. Some styles call it a bibliography."},
  {"t":"open","key":"exit_synth","q":"What does it mean to synthesize sources?","min":10,"rows":2,"rubric":["Combine information from more than one source on the same idea"],"model":"To combine information from two or more sources into one idea or paragraph."},
  {"t":"text","q":"A source has no author. What does its works cited entry begin with: the title, the date or the URL?","a":[{"all":[["title"]],"none":["not","date","url"]}],"show":"the title (or the organization that wrote it)","pts":2,"why":"With no author, start with the title (or the organization that wrote it, if it is the author)."}],
 "next": "Week 10: the Unit 2 checkpoint and writing your informational article."
}

TEACHER = {
 "standards": [
  "ELA.6.C.4.1: Conduct research to answer a question, drawing on multiple reliable and valid sources, and refocusing the inquiry when appropriate.",
  "ELA.6.C.1.4: Write expository texts to explain and/or analyze information from multiple sources, using a logical organizational structure, relevant elaboration, and varied transitions.",
  "ELA.6.R.3.2: Paraphrase content from grade-level texts.",
  "ELA.K12.EE.1.1: Cite evidence to explain and justify reasoning.",
  "ELA.6.V.1.2: Apply knowledge of Greek and Latin roots and affixes to determine meanings of words and phrases in grade-level content (reconnect)."],
 "materials": ["The interactive lesson", "Index cards (at least 12), two highlighters or markers in different colors, paper clips", "A library visit or access to trusted websites for the student's own topic", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 8 Reconnect questions."],
  [4, "Hook", "Ask where the 97 percent figure came from and how a reader could check it."],
  [8, "Research questions", "Sort questions into too broad, too narrow and just right. The student drafts a project question."],
  [10, "Read sources", "Read Sources A and B. Compare the two kinds of sources and discuss reliability."],
  [14, "Note cards", "Model one card, then the student makes two. Hunt for copied strings without quotation marks."],
  [12, "Synthesize and cite", "Write the synthesized sentence together. Build both works cited entries."],
  [6, "Assign", "Assign the note card sort (library or online), Think Deeper and the Exit Check."]],
 "key_questions": ["Can this question be answered in one sentence? Is it too big?", "Which source is this card from?", "Are these your words or the author's?", "Where would a reader go to check this fact?"],
 "misconceptions": ["Only direct quotations need citations.", "Notes should be copied sentences.", "Any website is a reliable source.", "A works cited list is in the order sources were used."],
 "support": ["Provide note card templates with labeled spaces.", "Give a works cited frame with blanks for each element.", "Limit the project search to two pre-selected sources."],
 "challenge": ["Find a third source and add it to your synthesis.", "Compare MLA and APA citation styles for one source."],
 "background": "<p>Sources A and B are practice sources written for this lesson; the author name (Grace Okafor) and the organization (Sunshine Ocean Alliance) are invented and labeled as such on the page. Their facts are real: Florida's Coral Reef runs about 350 miles from the Dry Tortugas to St. Lucie Inlet (Florida Department of Environmental Protection); the 97 percent wave-energy figure is from Ferrario et al. (2014), Nature Communications; the Manatee Bay buoy recorded about 101°F (38.4°C) on July 24, 2023 (NOAA); stony coral tissue loss disease was first reported off Miami-Dade County in 2014 and affects more than 20 stony coral species; NOAA launched Mission: Iconic Reefs in 2019 for seven Keys sites; the Coral Restoration Foundation in Key Largo uses coral tree nurseries. Citation format follows MLA 9th edition, simplified for Grade 6. When students use real websites, require the URL and teach them to prefer .gov, .edu, museum and established science organization sites.</p>",
 "sources": ["Florida Department of Environmental Protection, Florida's Coral Reef.", "Ferrario, F. et al. (2014), The effectiveness of coral reefs for coastal hazard risk reduction and adaptation, Nature Communications 5.", "NOAA, Mission: Iconic Reefs.", "Modern Language Association (2021), MLA Handbook, 9th ed.", "Purdue Online Writing Lab, MLA Formatting and Style Guide."]
}

PRINT = {
 "directions": "Write in complete sentences.",
 "items": [
  {"q":"Rewrite this as a just-right research question: \"What about hurricanes?\"","a":"How do hurricanes form, and how do scientists predict their paths?","lines":2},
  {"q":"Name the four parts of a note card.","a":"Subtopic heading, source label, notes in your own words, exact quotes in quotation marks with location.","lines":2},
  {"q":"Make a note card on why reefs matter, from Source A.","a":"Heading: Why reefs matter. Source A. Home and food for fish, lobsters, turtles; cut wave energy up to 97 percent (2014 study).","lines":3},
  {"q":"Write an MLA works cited entry for an article by Luis Ortega called \"Manatees in Winter\" in the magazine Florida Wildlife, 2025.","a":"Ortega, Luis. \"Manatees in Winter.\" Florida Wildlife, 2025.","lines":2},
  {"q":"What does synthesize mean? Give an example from the coral sources.","a":"Combine information from two sources; e.g. the 2023 heat wave bleached corals (Okafor), so scientists moved nursery corals (Sunshine Ocean Alliance).","lines":2},
  {"q":"Why do writers cite paraphrased information?","a":"The ideas still belong to someone else; citing gives credit and lets readers check.","lines":2}]
}
