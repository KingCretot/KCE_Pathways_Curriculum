TITLE = "Unit 2 Projects and Rubrics"
KICKER = "Grade 6 · Unit 2 · Projects due in Week 10"
LINK = "Unit 2 projects and rubrics"

LEVELS = ["4 Exceeds", "3 Meets", "2 Approaching", "1 Beginning"]

def rubric(traits):
    h = "<table class='t rub'><tr><th>Trait</th>" + "".join(f"<th>{l}</th>" for l in LEVELS) + "</tr>"
    for name, cells in traits:
        h += f"<tr><td><b>{name}</b></td>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>"
    return h + "</table>"

INTRO = """<h1>Unit 2 Projects and Rubrics</h1>
<p>Each project is scored with five traits worth up to 4 points each, for a total of 20. Multiply by 5 for a score out of 100. <b>Mastery is 85 (17 of 20).</b> A project below mastery is returned with feedback and revised once. Read the rubric before you start.</p>
<style>.rub td,.rub th{font-size:13px;vertical-align:top}.rub td:first-child{width:16%}.proj{page-break-before:always}.proj.first{page-break-before:auto}</style>"""

ELA = """<div class='proj first'><h2>ELA: Informational Article</h2>
<p><b>Task:</b> Research a question you care about and write an informational article of 400 to 700 words that teaches a reader something real. Research question and note cards in Week 9; outline, drafting, revision and publishing in Week 10.</p>
<p><b>Must include:</b> a title; an introduction with a hook and a central idea (thesis); two to four body sections, each with a heading and a T-E-E-C paragraph; facts from at least two reliable sources, in your own words, with in-text citations; varied transitions; one visual with a caption; a conclusion that restates the central idea and explains why it matters; an MLA works cited list in alphabetical order.</p>
<p><b>Turn in:</b> the final article in the Week 10 lesson (Hands-On), your note cards (photo), and your reflection.</p>""" + rubric([
 ("Central idea and focus", ["A clear, insightful central idea that every section develops.", "A clear central idea that the sections support.", "The central idea is vague, or some sections wander.", "No clear central idea; a list of facts."]),
 ("Research and citations", ["Facts from two or more reliable sources are combined smoothly; every borrowed fact is cited; the works cited list is complete and correct.", "Facts from two reliable sources; borrowed facts are cited; the works cited list is mostly correct.", "One source, missing citations, or several works cited errors.", "Sources unclear or not cited; possible copying."]),
 ("Organization and text features", ["Logical structure with a strong introduction and conclusion, useful headings and a visual whose caption adds meaning.", "Clear introduction, body sections with headings, conclusion and a captioned visual.", "Some parts or features are missing or out of order.", "Hard to follow; few or no features."]),
 ("Elaboration and language", ["Every fact is explained; precise vocabulary; varied transitions connect ideas smoothly.", "Most facts are explained; some precise vocabulary; varied transitions.", "Facts are listed with little explanation; repeated transitions.", "Little explanation; vague language."]),
 ("Conventions", ["Almost no errors in capitals, usage, punctuation or spelling.", "A few errors that do not get in the way.", "Errors sometimes make reading hard.", "Frequent errors make the article hard to read."])]) + "</div>"

SCI = """<div class='proj'><h2>Science: Cell Model Project</h2>
<p><b>Task:</b> Build a three-dimensional model of a plant cell or an animal cell that teaches how a cell works, then give a 2-minute tour. Planned and built in Week 10.</p>
<p><b>Must include:</b> at least 8 labeled parts (see the Week 10 list for each cell type); a key explaining each material and each part's job; an analogy card (\"A cell is like a ___ because...\") with at least five matched parts, not a city; one process shown with arrows or movable pieces (photosynthesis, active transport or osmosis); a limits note; a photo of the model; the tour.</p>
<p><b>Safety:</b> ask a parent before using hot glue, knives or anything that must be heated. Photograph edible models before eating. Never taste non-food materials; keep beans, buttons, clay and gel away from pets and young children; check food allergies before an edible model.</p>
<p><b>Turn in:</b> photos of the model, key and analogy card; the tour script (Week 10 Hands-On); and a short video of the tour (or a parent's three-line note: how long it ran, what the student explained best, one question asked).</p>""" + rubric([
 ("Accuracy of parts", ["Eight or more parts, all correct for the cell type, placed and sized sensibly.", "Eight parts, correct for the cell type.", "Fewer than eight parts, or one or two errors (for example, chloroplasts in an animal cell).", "Few parts or several errors."]),
 ("Key and functions", ["Every part's job is explained accurately and clearly in the key.", "Each part's job is explained, with minor gaps.", "Some jobs are missing or inaccurate.", "No key, or jobs mostly missing."]),
 ("Process shown", ["The process is shown clearly with arrows or moving pieces and explained step by step with correct vocabulary.", "The process is shown and explained correctly.", "The process is shown but the explanation is unclear or partly wrong.", "No process shown."]),
 ("Analogy and limits", ["An original analogy with five or more well-explained matches and a thoughtful limits note.", "An analogy with five matches and a limits note.", "Fewer matches, weak reasons, or no limits note.", "No analogy."]),
 ("Tour and communication", ["A confident, organized tour that uses Unit 2 vocabulary and answers questions well.", "A clear tour that names parts and jobs.", "The tour is hard to follow or skips parts.", "No tour or note."])]) + "</div>"

SS = """<div class='proj'><h2>Social Studies: Nile Valley Project</h2>
<p><b>Task:</b> Build an illustrated scale timeline and map of the Nile Valley, then give a 2- to 3-minute Historian's Talk answering: <i>Why must the story of the Nile Valley include both Kemet and Kush?</i> Planned and built in Week 10.</p>
<p><b>Must include:</b> a timeline from about 5000 BCE to 940 CE drawn to a stated scale, with rows for Kemet, Nubia/Kush and Aksum; at least 12 events from Weeks 6 to 10, each with a date, a one-sentence explanation and a drawing; a map with at least eight labeled places; a talk with a claim, three pieces of evidence and one named source; photos and the talk.</p>
<p><b>Turn in:</b> photos of the timeline and map; the talk script (Week 10 Hands-On); and a recording of the talk (or a parent's three-line note: how long it ran, the strongest evidence, one question asked).</p>""" + rubric([
 ("Timeline accuracy and scale", ["Twelve or more accurate events placed precisely to a consistent scale, in clearly separated rows.", "Twelve accurate events placed to scale.", "Fewer events, some errors, or uneven spacing.", "Few events, many errors, no scale."]),
 ("Explanations and visuals", ["Every event has a clear explanation and a drawing that adds meaning.", "Each event has an explanation and a drawing.", "Some explanations or drawings are missing or unclear.", "Mostly dates only."]),
 ("Map", ["Eight or more places, accurately placed, with the Nile, cataracts and seas clearly shown.", "Eight places, mostly accurate.", "Fewer places or several errors.", "Map missing or mostly inaccurate."]),
 ("Claim and evidence", ["A strong claim supported by three specific, accurate pieces of evidence from different weeks and a named source, each clearly explained.", "A clear claim with three accurate pieces of evidence and a source.", "A weak claim, or evidence that is vague or not explained.", "No clear claim or evidence."]),
 ("Delivery", ["Confident, organized and within time; uses the timeline and map to support points; answers questions well.", "Clear and within time; refers to the timeline.", "Hard to follow, too short or too long.", "No talk or note."])]) + "</div>"

HTML = INTRO + ELA + SCI + SS
