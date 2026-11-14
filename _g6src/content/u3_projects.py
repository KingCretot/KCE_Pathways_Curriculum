TITLE = "Unit 3 Projects and Rubrics"
KICKER = "Grade 6 · Unit 3 · Projects due in Week 15"
LINK = "Unit 3 projects and rubrics"

LEVELS = ["4 Exceeds", "3 Meets", "2 Approaching", "1 Beginning"]

def rubric(traits):
    h = "<table class='t rub'><tr><th>Trait</th>" + "".join(f"<th>{l}</th>" for l in LEVELS) + "</tr>"
    for name, cells in traits:
        h += f"<tr><td><b>{name}</b></td>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>"
    return h + "</table>"

INTRO = """<h1>Unit 3 Projects and Rubrics</h1>
<p>Each project is scored with five traits worth up to 4 points each, for a total of 20. Multiply by 5 for a score out of 100. <b>Mastery is 85 (17 of 20).</b> A project below mastery is returned with feedback and revised once. Read the rubric before you start.</p>
<style>.rub td,.rub th{font-size:13px;vertical-align:top}.rub td:first-child{width:16%}.proj{page-break-before:always}.proj.first{page-break-before:auto}</style>"""

ELA = """<div class='proj first'><h2>ELA: Poetry Analysis Project</h2>
<p><b>Task:</b> Choose one poem from Unit 3 (Weeks 11 to 14), or two poems in conversation, and (1) write an analysis of 400 to 600 words explaining how the poet creates meaning, and (2) recite the poem from memory and record it. Planning in Week 14 if you like; writing, memorizing and recording in Week 15.</p>
<p><b>Must include:</b> a title; an introduction that names the poem and poet and ends with a thesis naming at least two techniques; three body paragraphs in T-E-E-C form, each with a short, accurate quotation (line breaks shown with a slash); analysis of the poem's form and at least two devices, explaining their effect; a conclusion; an MLA citation of the poem. Recitation: the whole poem, or at least 14 lines of a longer one, from memory, with clear voice and pauses at punctuation.</p>
<p><b>Turn in:</b> the analysis in the Week 15 lesson (Hands-On), the recording, and your reflection.</p>""" + rubric([
 ("Thesis and focus", ["An insightful thesis about how the poem creates meaning, naming techniques that every paragraph develops.", "A clear thesis naming two techniques; paragraphs support it.", "The thesis is vague, or some paragraphs wander or retell.", "No clear thesis; mostly retelling."]),
 ("Evidence", ["Three or more short, precise quotations, accurately copied with slashes, each perfectly chosen.", "Three accurate quotations that support the points.", "Quotations are too long, inaccurate or weakly chosen.", "Few or no quotations."]),
 ("Analysis of form and devices", ["Explains clearly and originally how the form and at least two devices create meaning and feeling.", "Explains how the form and two devices create meaning.", "Names devices but explains little about their effect.", "Devices missing or misidentified."]),
 ("Organization and conventions", ["Smooth T-E-E-C paragraphs, varied transitions, an MLA citation, and almost no errors.", "Organized paragraphs, a citation and few errors.", "Some disorganization or errors that distract.", "Hard to follow; many errors; no citation."]),
 ("Recitation", ["Fully memorized; confident voice, varied pace and pauses that bring out meaning; eye contact.", "Memorized with few slips; clear voice; pauses at punctuation.", "Several slips or reading; rushed or too quiet.", "Not memorized or not recorded."])]) + "</div>"

SCI = """<div class='proj'><h2>Science: Field Guide Project</h2>
<p><b>Task:</b> Create a field guide to at least 6 living things near your home, at least 5 of them observed in person and at least 1 of them a fungus (such as a mushroom or a bracket fungus on a log), plus 1 microorganism page. Fieldwork and drafting in Week 15.</p>
<p><b>Must include:</b> a cover and a table of contents; one page per organism with a labeled drawing or your own photo, the common name, the scientific name written correctly, classification as far as you can find it (domain to genus), at least two observable identifying traits, where and when you saw it, one fact about how it lives, and whether it is native to Florida or invasive; a microorganism page (for example, the mold from your bread test or Karenia brevis); a tested dichotomous key to all of your organisms; a sources page.</p>
<p><b>Safety:</b> observe with an adult; look but don't touch unknown plants and animals; no collecting in state parks; wash hands after fieldwork.</p>
<p><b>Turn in:</b> the field guide (paper, photos of the pages, or a slide file), your Week 15 field notes and your key-test notes.</p>""" + rubric([
 ("Accuracy of identification and names", ["Every organism correctly identified; scientific names perfectly written; full classification where available.", "Organisms correctly identified; scientific names correct; classification mostly complete.", "Some identifications or names are wrong or missing.", "Many organisms unidentified or misnamed."]),
 ("Observations", ["Detailed, dated, first-hand observations with measurements and behavior for every organism seen in person.", "Dated observations with identifying traits for each organism.", "Some observations are vague, missing or copied.", "Few or no real observations."]),
 ("Dichotomous key", ["A key with one fewer couplet than organisms, true opposites and observable traits, tested and revised, that anyone can use.", "A working key with opposite couplets that identifies every organism.", "The key has errors: couplets not opposite, uses color or opinions, or misses organisms.", "No key, or it does not work."]),
 ("Science connections", ["Explains native versus invasive status, the microorganism's role, and connects traits to classification with insight.", "Includes native or invasive status, a microorganism page and traits linked to classification.", "Connections are thin or partly inaccurate.", "Few connections to Unit 3 ideas."]),
 ("Design and sources", ["Clear, attractive and well organized; every borrowed fact sourced from a reliable source.", "Clear and organized; sources listed.", "Hard to use in places; sources incomplete.", "Disorganized; no sources."])]) + "</div>"

SS = """<div class='proj'><h2>Social Studies: Ancient Asia Project (Silk Roads Travel Journal)</h2>
<p><b>Task:</b> Invent a traveler around 100 CE (a Sogdian merchant's apprentice, a Han envoy, a Buddhist monk or an Aksumite sailor) and write a historically accurate travel journal of a journey on the land Silk Roads, the Indian Ocean sea roads, or both. Planned and written in Week 15.</p>
<p><b>Must include:</b> at least five dated journal entries of 100 to 200 words; a hand-drawn route map with at least six real, labeled stops and the deserts, mountains, rivers and seas crossed; real goods, foods, animals, money, dangers and beliefs of the time; at least two civilizations from Unit 3 visited or discussed (for example, the ruins of Babylon or a conversation about Confucius); at least one primary source quoted or described (such as the Periplus or the Analects); no anachronisms; a Historian's Note that separates real facts from invented details, with at least three sources.</p>
<p><b>Turn in:</b> the journal and map (or photos), and the Historian's Note.</p>""" + rubric([
 ("Historical accuracy", ["Every detail fits 100 CE and the places described; rich, specific facts; no anachronisms.", "Details are accurate for the time and place; no anachronisms.", "Some inaccurate or vague details, or one anachronism.", "Many errors or anachronisms."]),
 ("Use of Unit 3 learning", ["Connects two or more Unit 3 civilizations and the trade routes with insight; explains relay trade, monsoons or cultural diffusion through the story.", "Includes two Unit 3 civilizations and accurate trade-route ideas.", "Only one civilization, or the connections are thin.", "Few connections to Unit 3."]),
 ("Map", ["Six or more stops accurately placed in order, with geography clearly shown and labeled.", "Six stops in order, mostly accurate.", "Fewer stops or several errors.", "Map missing or mostly inaccurate."]),
 ("Writing and voice", ["Vivid, believable first-person entries with sensory detail and a consistent voice; almost no errors.", "Clear first-person entries with detail; few errors.", "Entries are short, flat or hard to follow.", "Fewer than five entries or very hard to follow."]),
 ("Historian's Note and sources", ["Clearly separates fact from fiction for every major detail; three or more reliable sources including a primary source, correctly cited.", "Separates fact from fiction; three sources including a primary source.", "The note is incomplete or sources are weak.", "No note or sources."])]) + "</div>"

HTML = INTRO + ELA + SCI + SS
