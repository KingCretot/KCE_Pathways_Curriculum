TITLE = "Unit 1 Projects and Rubrics"
KICKER = "Grade 6 · Unit 1 · Projects due in Week 5"
LINK = "Unit 1 projects and rubrics"

LEVELS = ["4 Exceeds", "3 Meets", "2 Approaching", "1 Beginning"]

def rubric(traits):
    h = "<table class='t rub'><tr><th>Trait</th>" + "".join(f"<th>{l}</th>" for l in LEVELS) + "</tr>"
    for name, cells in traits:
        h += f"<tr><td><b>{name}</b></td>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>"
    return h + "</table>"

INTRO = """<h1>Unit 1 Projects and Rubrics</h1>
<p>Each project is scored with five traits worth up to 4 points each, for a total of 20. Multiply by 5 for a score out of 100. <b>Mastery is 85 (17 of 20).</b> A project below mastery is returned with feedback and revised once. Students should read the rubric before they start, as they learned in ELA Week 1.</p>
<style>.rub td,.rub th{font-size:13px;vertical-align:top}.rub td:first-child{width:16%}.proj{page-break-before:always}.proj.first{page-break-before:auto}</style>"""

ELA = """<div class='proj first'><h2>ELA: Personal Narrative</h2>
<p><b>Task:</b> Write a true story about a moment that changed you, 400 to 800 words, told in first person. Started in Week 1 (story mountain and opening), drafted in Week 4, revised and published in Week 5.</p>
<p><b>Must include:</b> a title; an opening that drops the reader into the scene; at least three lines of correctly punctuated dialogue; sensory details and strong verbs; a slowed-down climax; transitions; an ending that reflects on how you changed; the Week 5 reflection.</p>
<p><b>Turn in:</b> the final story in the Week 5 lesson (Think Deeper), the reflection, and the Author's Chair feedback.</p>""" + rubric([
 ("Ideas and focus", ["A true, focused story with a clear problem, a powerful climax and a meaningful change.", "A true story with a clear problem, climax and change.", "The problem or change is unclear, or the story wanders.", "No clear problem or change; a list of events."]),
 ("Organization", ["Chronological order with varied transitions; the opening hooks and the ending reflects thoughtfully.", "Clear order with transitions; a real opening and ending.", "Order is sometimes confusing; the opening or ending is weak.", "Hard to follow; no real opening or ending."]),
 ("Narrative craft", ["Dialogue, sensory details, strong verbs and figurative language bring every scene to life; the climax is clearly slowed down.", "Uses dialogue, sensory details and strong verbs; the climax gets the most words.", "Some craft, but the climax is rushed or details are general.", "Little dialogue or detail; tells instead of shows."]),
 ("Voice and point of view", ["Consistent first person in a voice that clearly sounds like the writer.", "Consistent first person with some personal voice.", "Point of view slips, or the voice is flat.", "Point of view shifts often; no personal voice."]),
 ("Conventions", ["Almost no errors in capitals, usage, punctuation (including dialogue) or spelling.", "A few errors that do not get in the way.", "Errors sometimes make reading hard; dialogue punctuation is inconsistent.", "Frequent errors make the story hard to read."])]) + "</div>"

SCI = """<div class='proj'><h2>Science: Investigation Project</h2>
<p><b>Task:</b> Plan and carry out your own fair test at home, then report it like a scientist. Started with testable questions in Week 4; planned and run in Week 5.</p>
<p><b>Must include:</b> a testable question; a hypothesis (If... then... because...); independent, dependent and three controlled variables; a numbered, repeatable procedure and materials list; a data table with units and three trials; averages; the correct graph with TAILS; a CER conclusion; two limits and a next question; a photo of the setup.</p>
<p><b>Safety:</b> get a parent's permission for anything with heat, sharp tools, chemicals or the outdoors. Never taste materials.</p>
<p><b>Turn in:</b> the Week 5 Hands-On records, plus the graph (photo or drawing) and the setup photo emailed to your teacher or uploaded where your teacher directs.</p>""" + rubric([
 ("Question and hypothesis", ["Testable, original question; hypothesis gives a clear prediction and a scientific reason.", "Testable question; hypothesis in If-then-because form.", "Question is hard to test, or the hypothesis lacks a reason.", "Question cannot be tested; no hypothesis."]),
 ("Fair test design", ["One independent variable, a measurable dependent variable, three or more well-chosen controls; procedure could be repeated exactly.", "Variables correctly identified; three controls; procedure is clear.", "Variables partly confused, or the procedure skips steps.", "More than one variable changed; no procedure."]),
 ("Data and measurement", ["Three or more trials per condition, metric units in every heading, accurate averages and careful measurement.", "Three trials, units shown, averages correct.", "Fewer than three trials, or missing units or averages.", "Little or no data recorded."]),
 ("Graph", ["Correct graph type with every TAILS element and an easy-to-read scale.", "Correct graph type with most TAILS elements.", "Wrong graph type, or several TAILS elements missing.", "No graph, or the graph does not match the data."]),
 ("Conclusion (CER)", ["Claim answers the question; evidence uses specific averages with units; reasoning uses a science idea; limits and a next question are thoughtful.", "Claim, evidence with numbers, reasoning, two limits and a next question.", "Claim with weak evidence or no reasoning; limits missing.", "No real conclusion."])]) + "</div>"

SS = """<div class='proj'><h2>Social Studies: Museum Exhibit Project</h2>
<p><b>Task:</b> Become a curator. Build a home museum exhibit that answers one big question about Unit 1, then give a 3-minute tour. Planned and built in Week 5.</p>
<p><b>Must include:</b> a big question; an introduction panel (3 to 5 sentences); at least five objects (real items, replicas, drawings or printed images) from at least three weeks of Unit 1; a label for each object with title, place and date, material, story and a visitor question; a map or timeline; photos of the exhibit and each label; the tour and visitor feedback.</p>
<p><b>Ideas for objects:</b> Week 1 family interview or timeline; Week 2 true-size map; Week 3 dig box artifacts or a replica Lomekwi tool; Week 4 hand-ground flour or a clay Çatalhöyük house.</p>
<p><b>Turn in:</b> the Week 5 Hands-On records; photos of the exhibit and each label, emailed to your teacher or uploaded where your teacher directs; and a short video of the tour (or a parent's three-line tour note: how long it ran, what the student explained best, one visitor question).</p>""" + rubric([
 ("Big question and focus", ["A thoughtful question that the whole exhibit clearly answers.", "A clear question that the exhibit answers.", "The question is vague, or some objects do not connect.", "No clear question; a collection of facts."]),
 ("Evidence and accuracy", ["Five or more objects from three or more weeks; every fact is accurate and specific.", "Five objects from three weeks; facts are accurate.", "Fewer objects or weeks; some facts are vague or inaccurate.", "Few objects; many inaccurate facts."]),
 ("Labels", ["Every label has all five parts, is short, vivid and written for visitors.", "Every label has all five parts.", "Some labels are missing parts or are too long.", "Labels are missing or incomplete."]),
 ("Map or timeline", ["Accurate and clearly connected to the objects, with a title and labels.", "Accurate, with a title and labels.", "Present but incomplete or partly inaccurate.", "Missing."]),
 ("Tour and perspective", ["A confident tour; reflects on whose stories are included and uses visitor feedback well.", "A clear tour; records visitor feedback.", "A short or unclear tour; little feedback.", "No tour."])]) + "</div>"

HTML = INTRO + ELA + SCI + SS
