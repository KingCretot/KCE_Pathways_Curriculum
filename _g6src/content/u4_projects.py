TITLE = "Unit 4 Projects and Rubrics"
KICKER = "Grade 6 · Unit 4 · Projects due in Week 20"
LINK = "Unit 4 projects and rubrics"

LEVELS = ["4 Exceeds", "3 Meets", "2 Approaching", "1 Beginning"]

def rubric(traits):
    h = "<table class='t rub'><tr><th>Trait</th>" + "".join(f"<th>{l}</th>" for l in LEVELS) + "</tr>"
    for name, cells in traits:
        h += f"<tr><td><b>{name}</b></td>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>"
    return h + "</table>"

INTRO = """<h1>Unit 4 Projects and Rubrics</h1>
<p>Each project is scored with five traits worth up to 4 points each, for a total of 20. Multiply by 5 for a score out of 100. <b>Mastery is 85 (17 of 20).</b> A project below mastery is returned with feedback and revised once. Read the rubric before you start.</p>
<style>.rub td,.rub th{font-size:13px;vertical-align:top}.rub td:first-child{width:16%}.proj{page-break-before:always}.proj.first{page-break-before:auto}</style>"""

ELA = """<div class='proj first'><h2>ELA: Argument Project (Essay and Speech)</h2>
<p><b>Task:</b> (1) Write a researched argumentative essay of 500 to 800 words, and (2) deliver it as a 2- to 3-minute speech to an audience and record it. Plan and research in Week 19; finish, rehearse and record in Week 20.</p>
<p><b>Choose a question</b> (or propose your own to a parent): Should our county add protected bike lanes on main roads? Should every Florida child learn to swim before age 7? Should homeschool students take part in community service each year? Should students still learn cursive? Should kids ages 11 to 13 have their own smartphones? Should our town build a splash pad or community garden?</p>
<p><b>Must include:</b> a title; an introduction with a hook, background and a clear, arguable thesis; at least two body paragraphs, each with a reason, evidence and explanation; a counterclaim paragraph with a fair counterclaim, a concession and a rebuttal; a conclusion with a call to action; at least three credible sources, cited in the essay and listed in a works-cited list; no fallacies. Speech: note cards (not a script), eye contact, clear voice and pauses.</p>
<p><b>Turn in:</b> the essay and works-cited list, the speech recording, and the reflection in the Week 20 lesson.</p>""" + rubric([
 ("Claim and organization", ["A precise, arguable thesis; every paragraph does its job; smooth, varied transitions.", "A clear thesis; introduction, body, counterclaim and conclusion all present; transitions used.", "The thesis is vague or a paragraph is missing or out of order.", "No clear thesis or organization."]),
 ("Evidence and sources", ["Three or more credible sources, honestly paraphrased or quoted, each with a clear explanation.", "Three credible sources cited accurately with explanation.", "Fewer than three sources, weak sources, or evidence without explanation.", "Little or no evidence; sources missing."]),
 ("Counterclaim and reasoning", ["The strongest objection stated fairly, a generous concession and a convincing rebuttal; no fallacies.", "A fair counterclaim, a concession and a rebuttal; no fallacies.", "The counterclaim is weak or a straw man, or the rebuttal is thin.", "No counterclaim, or the essay relies on fallacies."]),
 ("Language and conventions", ["Precise, varied language; almost no errors.", "Clear language; few errors that don't affect meaning.", "Several errors or vague wording.", "Many errors that make it hard to read."]),
 ("Speech delivery", ["Confident, from note cards, with strong eye contact, expression and pacing; 2 to 3 minutes.", "From note cards, clear and audible; 2 to 3 minutes.", "Mostly read aloud, rushed or too quiet, or outside the time range.", "Not delivered or very hard to follow."])]) + "</div>"

SCI = """<div class='proj'><h2>Science: Body Systems Project</h2>
<p><b>Task:</b> Build a life-size body map showing at least five organ systems, and write a 300- to 500-word \"Day in the Life\" explanation of how your body systems work together during one real activity you do (a swim, a dance class, a soccer game, a hike).</p>
<p><b>Must include:</b> your traced body outline; organs from at least five systems (skeletal, muscular, circulatory, respiratory, digestive, nervous) drawn about life size in the right places and labeled with their jobs; red and blue paths for oxygen-rich and oxygen-poor blood; at least three interaction arrows with explanations; the written explanation using at least eight Unit 4 vocabulary words and the idea of homeostasis; one piece of data you collected this unit (heart rate, breathing rate or reaction time) used in your explanation; a short list of sources.</p>
<p><b>Turn in:</b> a photo of the body map, the written explanation, and the record in the Week 20 lesson.</p>""" + rubric([
 ("Scientific accuracy", ["All organs correctly placed and labeled with accurate jobs; no errors.", "Organs mostly correctly placed; accurate jobs.", "Several organs misplaced or jobs inaccurate.", "Many errors."]),
 ("System interactions", ["Three or more insightful interactions clearly explained, including homeostasis.", "Three accurate interactions explained.", "Interactions are vague or only one or two.", "No interactions explained."]),
 ("Use of data", ["Your own data used to explain a body response, with units and a comparison.", "Your own data included and connected to the explanation.", "Data included but not connected.", "No data."]),
 ("Vocabulary and explanation", ["Eight or more Unit 4 terms used precisely in a clear, engaging explanation.", "Eight terms used correctly; clear explanation.", "Fewer terms or some misused.", "Few terms; hard to follow."]),
 ("Craftsmanship and sources", ["Neat, colorful, life-size and easy to read; sources listed correctly.", "Neat and readable; sources listed.", "Hard to read in places; sources incomplete.", "Messy or incomplete; no sources."])]) + "</div>"

SS = """<div class='proj'><h2>Social Studies: Mediterranean Project</h2>
<p><b>Task:</b> Create a museum exhibit of four panels (poster board, a folded display, or four slides) titled \"One Sea, Many Peoples,\" comparing Persia, Greece, Rome and Carthage, and give a 3- to 4-minute tour to your family as the museum guide.</p>
<p><b>Must include:</b> one panel per civilization with a hand-drawn map, its government, one major achievement, one war or conflict and who was left out of power; a fifth \"connections\" section showing at least three ideas or goods that traveled between civilizations (one must involve Africa); one short quotation from a primary source studied in Unit 4 (Herodotus, Ezra, Pericles or Livy) with a sentence on who wrote it, when and why; a timeline with at least eight dates; a list of at least three sources.</p>
<p><b>Turn in:</b> photos of the exhibit, a recording of the tour, and the record in the Week 20 lesson.</p>""" + rubric([
 ("Historical accuracy", ["Rich, accurate facts for all four civilizations; no errors.", "Accurate facts for all four.", "Some errors or one civilization thin.", "Many errors or missing civilizations."]),
 ("Comparison and connections", ["Insightful comparison of governments and exclusions; three or more well-explained connections, including Africa.", "Clear comparison; three connections including Africa.", "Comparison is thin or fewer connections.", "Little comparison."]),
 ("Primary source analysis", ["Accurate quotation with sharp analysis of author, date, purpose and bias.", "Accurate quotation with author, date and purpose.", "Quotation without much analysis.", "No primary source."]),
 ("Maps and timeline", ["Accurate, labeled maps and a timeline with eight or more correctly placed dates.", "Maps and timeline accurate with eight dates.", "Maps or timeline incomplete or with errors.", "Missing maps or timeline."]),
 ("Presentation and sources", ["Engaging, confident tour; three or more reliable sources correctly listed.", "Clear tour; three sources listed.", "Tour is hard to follow or sources incomplete.", "No tour or sources."])]) + "</div>"

HTML = INTRO + ELA + SCI + SS
