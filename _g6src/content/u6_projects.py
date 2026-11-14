TITLE = "Unit 6 Projects and Rubrics"
KICKER = "Grade 6 · Unit 6 · Projects due in Week 30"
LINK = "Unit 6 projects and rubrics"

LEVELS = ["4 Exceeds", "3 Meets", "2 Approaching", "1 Beginning"]

def rubric(traits):
    h = "<table class='t rub'><tr><th>Trait</th>" + "".join(f"<th>{l}</th>" for l in LEVELS) + "</tr>"
    for name, cells in traits:
        h += f"<tr><td><b>{name}</b></td>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>"
    return h + "</table>"

INTRO = """<h1>Unit 6 Projects and Rubrics</h1>
<p>Each project is scored with five traits worth up to 4 points each, for a total of 20. Multiply by 5 for a score out of 100. <b>Mastery is 85 (17 of 20).</b> A project below mastery is returned with feedback and revised once. Read the rubric before you start.</p>
<style>.rub td,.rub th{font-size:13px;vertical-align:top}.rub td:first-child{width:16%}.proj{page-break-before:always}.proj.first{page-break-before:auto}</style>"""

ELA = """<div class='proj first'><h2>ELA: Research Presentation</h2>
<p><b>Task:</b> Research an open question about Florida's environment, people or history, write a research report of 600 to 900 words, and deliver a 4- to 6-minute presentation with visuals and a Q&A. Plan in Week 26, judge sources in Week 27, draft in Week 28, build and rehearse in Week 29, and present in Week 30.</p>
<p><b>Report must include:</b> an open, focused research question and two or three sub-questions; at least four reliable sources, including at least one government, university or expert-organization source, each checked with SIFT; an introduction with a hook, background and the question; one body section per sub-question that synthesizes more than one source; in-text citations for every borrowed fact, paraphrase or quotation; a conclusion that answers the question and explains why it matters; and a works-cited list.</p>
<p><b>Presentation must include:</b> 6 to 8 slides or poster panels with one idea each; at least one chart, map or diagram with a source line; oral citations; signposts for each finding; and a Q&A of at least 3 minutes. Use only images you took, drew or have permission to use, with credit.</p>
<p><b>Turn in:</b> the report, the slides or poster (or photos), your note cards, a recording if you made one, and the records in the Week 30 lesson.</p>""" + rubric([
 ("Research question and sources", ["A sharp, open question; four or more reliable, varied sources, each clearly evaluated.", "An open question; four reliable sources.", "Question is too broad or narrow, or some sources are unreliable.", "No real question or few sources."]),
 ("Synthesis and citation", ["Sources are skillfully combined in every section; every borrowed idea is cited; works-cited list is complete and correct.", "Sources are combined in most sections; borrowed ideas are cited; works-cited list is present.", "Sources are listed one at a time, or some citations are missing.", "Little synthesis; citations missing."]),
 ("Organization and content", ["Clear introduction, sections by sub-question and a conclusion that answers the question with insight.", "Clear introduction, sections and conclusion.", "Organization is uneven or the conclusion doesn't answer the question.", "Hard to follow."]),
 ("Visuals", ["Clean, readable visuals with one idea each; data visuals are accurate, labeled and sourced.", "Readable visuals; at least one sourced data visual.", "Crowded or unsourced visuals.", "No useful visuals."]),
 ("Delivery and Q&A", ["Confident eye contact, volume and pacing; numbers explained clearly; questions answered thoughtfully and honestly.", "Generally clear delivery within 4 to 6 minutes; questions answered.", "Reads from slides or notes much of the time, or runs well over or under time.", "Delivery is hard to follow; no Q&A."])]) + "</div>"

SCI = """<div class='proj'><h2>Science: Capstone Investigation</h2>
<p><b>Task:</b> Design and carry out your own fair-test investigation on a life science question, then report it as a poster, slideshow or lab report.</p>
<p><b>Parent-approved question ideas:</b> Does the amount of light affect how fast bean seeds sprout or how tall seedlings grow? Does the amount of water affect radish seedling growth? Does salt water affect seed sprouting (a model of rising seas in coastal Florida)? Do seeds sprout faster in soil, sand or on a damp paper towel? Does temperature affect how fast yeast produces gas (measured by a balloon on a bottle)? Do pill bugs (roly-polies) choose damp or dry areas (observe gently and return them outdoors where you found them)? Propose your own to a parent.</p>
<p><b>Must include:</b> a testable question; background research from at least two reliable sources; a hypothesis with a reason; independent, dependent and controlled variables; a materials list and safety steps; at least three trials for each condition; a data table with units; a graph; a conclusion supported by data; a source of error; a new question; and a connection to a Grade 6 unit (cells, classification, body systems, ecosystems or heredity and adaptation).</p>
<p><b>Safety:</b> get a parent's approval before starting; wash hands after handling soil, seeds, yeast or animals; never taste materials; use warm (not hot) water for yeast; treat any animals gently and return them where you found them.</p>
<p><b>Turn in:</b> the poster, slideshow or report (or photos), your data table and the records in the Week 30 lesson.</p>""" + rubric([
 ("Question and design", ["A creative, testable question with one independent variable, a clear dependent variable and well-chosen controls.", "A testable question with correct variables.", "Variables are unclear or more than one thing changes.", "No testable question."]),
 ("Data", ["Three or more trials per condition, recorded carefully with units, and patterns noted.", "Three trials per condition with units.", "Fewer trials or missing units.", "Little or no data."]),
 ("Graph and analysis", ["An accurate, well-labeled graph; analysis uses averages and describes patterns.", "An accurate graph with labels.", "Graph has errors or missing labels.", "No graph."]),
 ("Conclusion and science connection", ["A conclusion fully supported by data, with a thoughtful source of error, new question and a clear connection to a unit.", "A supported conclusion, a source of error and a new question.", "Conclusion is not fully supported by the data.", "No conclusion."]),
 ("Presentation and sources", ["Clear, attractive and easy to follow; two or more sources listed correctly.", "Readable and organized; sources listed.", "Hard to follow in places; sources incomplete.", "Messy or incomplete; no sources."])]) + "</div>"

SS = """<div class='proj'><h2>Social Studies: Year-in-Review Timeline Museum</h2>
<p><b>Task:</b> Build a timeline museum of the year's history, from human origins in Africa to the founding of St. Augustine in 1565, and give a guided tour to your family. Write a one-page \"curator's guide\" explaining the big theme your tour follows.</p>
<p><b>Must include:</b> at least 20 cards in correct order, including at least two from each unit, each with a date, place, one accurate fact and a drawing or map; color-coding by region (Africa, Asia, Europe and the Americas); at least three primary sources from the year (quoted exactly or described, with the author and date); a big theme that connects at least five cards; and at least two places where you show more than one perspective, such as Columbus and the Taíno, or Rome and Carthage.</p>
<p><b>Turn in:</b> photos of the timeline, the curator's guide and the records in the Week 30 lesson.</p>""" + rubric([
 ("Historical accuracy and order", ["Rich, accurate cards in correct order with no errors.", "Accurate cards in correct order.", "Some errors in facts or order.", "Many errors."]),
 ("Coverage", ["Thoughtful selections from every unit that show the year's range.", "At least two cards from each unit.", "Some units missing or thin.", "Few units represented."]),
 ("Primary sources", ["Three or more primary sources, accurately quoted or described and connected to the cards.", "Three primary sources with authors and dates.", "Fewer sources or missing authors or dates.", "No primary sources."]),
 ("Theme and perspectives", ["An insightful theme traced across five or more cards, with two or more strong multiple-perspective comparisons.", "A clear theme across five cards and two perspective comparisons.", "Theme is vague or perspectives are missing.", "No theme."]),
 ("Tour and curator's guide", ["An engaging, organized tour and a clear, well-written guide.", "A complete tour and guide.", "Tour or guide is short or unclear.", "Missing."])]) + "</div>"

HTML = INTRO + ELA + SCI + SS
