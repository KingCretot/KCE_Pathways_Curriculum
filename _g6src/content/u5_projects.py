TITLE = "Unit 5 Projects and Rubrics"
KICKER = "Grade 6 · Unit 5 · Projects due in Week 25"
LINK = "Unit 5 projects and rubrics"

LEVELS = ["4 Exceeds", "3 Meets", "2 Approaching", "1 Beginning"]

def rubric(traits):
    h = "<table class='t rub'><tr><th>Trait</th>" + "".join(f"<th>{l}</th>" for l in LEVELS) + "</tr>"
    for name, cells in traits:
        h += f"<tr><td><b>{name}</b></td>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>"
    return h + "</table>"

INTRO = """<h1>Unit 5 Projects and Rubrics</h1>
<p>Each project is scored with five traits worth up to 4 points each, for a total of 20. Multiply by 5 for a score out of 100. <b>Mastery is 85 (17 of 20).</b> A project below mastery is returned with feedback and revised once. Read the rubric before you start.</p>
<style>.rub td,.rub th{font-size:13px;vertical-align:top}.rub td:first-child{width:16%}.proj{page-break-before:always}.proj.first{page-break-before:auto}</style>"""

ELA = """<div class='proj first'><h2>ELA: Literary Response Project</h2>
<p><b>Task:</b> (1) Write a literary analysis essay of 500 to 800 words about <i>The Call of the Wild</i>, and (2) create a creative response that shows the same idea in another form. Plan in Week 24 if you like; draft, revise and finish in Week 25.</p>
<p><b>Choose an essay question</b> (or propose your own to a parent): How does London use a symbol (the club, the fire, the trail or the call) to develop a theme? Is Buck's ending a triumph, a loss or both? How do foils reveal what London believes about survival? How does the Klondike setting drive Buck's change? How should a reader today respond to London's portrayal of the Yeehats?</p>
<p><b>Essay must include:</b> a title; an introduction with a hook, brief context (title, author, 1903, the Klondike) and a clear thesis; at least three body paragraphs, each with a claim, at least one exact quotation with its chapter, and commentary longer than the quotation; evidence from at least three different chapters; a conclusion that explains why the idea matters; correct quotation punctuation.</p>
<p><b>Creative response</b> (choose one): a one-page illustrated map of Buck's journey with a quotation at each stop; a poem of at least 16 lines in Buck's voice; a scene of 400 to 600 words from Thornton's or another character's point of view (not a Yeehat point of view unless it follows the Week 24 guidelines: only what the novel says and ordinary human feelings, no invented customs, clothing or speech); or a 2-minute recorded reading of a chosen passage with an introduction explaining why you chose it.</p>
<p><b>Turn in:</b> the essay, the creative response (or a photo or recording of it), and the record in the Week 25 lesson.</p>""" + rubric([
 ("Thesis and organization", ["A precise, arguable thesis about how the novel works; every paragraph supports it; smooth, varied transitions.", "A clear thesis; introduction, three body paragraphs and conclusion; transitions present.", "Thesis is vague or summary-like; organization uneven.", "No clear thesis or organization."]),
 ("Evidence", ["Well-chosen, exact quotations from three or more chapters, each introduced with context.", "Exact quotations from three chapters.", "Few quotations, inexact, or from only one or two chapters.", "Little or no textual evidence."]),
 ("Commentary and analysis", ["Insightful commentary that explains how each quotation proves the claim, with attention to craft.", "Clear commentary that connects evidence to claims.", "Commentary mostly retells the plot.", "No commentary."]),
 ("Creative response", ["Original and polished; clearly expresses the essay's idea with accurate details from the novel.", "Complete and connected to the essay's idea.", "Incomplete or loosely connected.", "Missing."]),
 ("Conventions", ["Nearly error-free; quotations punctuated correctly; precise word choice.", "Few errors that don't affect meaning.", "Several errors that distract.", "Many errors that make it hard to read."])]) + "</div>"

SCI = """<div class='proj'><h2>Science: Ecosystem Study Project</h2>
<p><b>Task:</b> Study a real ecosystem near you (a park, pond, beach, spring, wooded lot or backyard) on at least three visits, then present a field guide as a poster or a slideshow of 6 to 10 slides.</p>
<p><b>Must include:</b> the site's name and a simple map; a data table from three visits (date, time, weather, temperature and counts from a 1-meter quadrat or a 15-minute observation); at least five biotic and three abiotic factors; a food web of at least eight organisms with arrows showing energy flow; one matter cycle (water or carbon) drawn for your site; at least three relationships (predation, competition, mutualism, commensalism or parasitism) you observed or researched for your site; one human impact on the site and a realistic solution; a short list of sources, including any field guide or app used.</p>
<p><b>Safety:</b> visit only with an adult; keep well back from water where alligators may live; do not touch or feed wildlife; follow park rules about collecting.</p>
<p><b>Turn in:</b> the poster or slideshow (or photos of it), your data table, and the record in the Week 25 lesson.</p>""" + rubric([
 ("Field data", ["Specific, well-organized data from three or more visits, with units and patterns noted.", "Data from three visits in a clear table.", "Data incomplete or vague.", "Little or no data."]),
 ("Energy and matter", ["Accurate food web of eight or more organisms and a matter cycle clearly tied to your site.", "Accurate food web and matter cycle.", "Errors in arrows or the cycle, or few organisms.", "Missing or inaccurate."]),
 ("Interactions and factors", ["Three or more relationships correctly classified and explained, plus five biotic and three abiotic factors.", "Three relationships and the required factors.", "Fewer relationships or factors, or some misclassified.", "Few or none."]),
 ("Human impact and solution", ["A specific, evidence-based impact with a realistic, well-explained solution.", "A clear impact and a reasonable solution.", "Impact or solution is vague.", "Missing."]),
 ("Presentation and sources", ["Clear, attractive and easy to follow; sources listed correctly.", "Readable and organized; sources listed.", "Hard to follow in places; sources incomplete.", "Messy or incomplete; no sources."])]) + "</div>"

SS = """<div class='proj'><h2>Social Studies: Trade Route Project</h2>
<p><b>Task:</b> Design and build a board game about one of Unit 5's trade networks (trans-Saharan or Indian Ocean), with a one-page rule sheet and a \"history behind the game\" guide, then playtest it with your family.</p>
<p><b>Must include:</b> a game board with an accurate map showing at least five real places (cities, deserts, rivers, ports); at least ten event cards based on real history (such as sandstorms, monsoon seasons, Mansa Musa's gold, the Portuguese attack on Kilwa); trade goods that match the real network; one rule that depends on geography (oases, the Niger's flood, monsoon direction); a history guide of 300 to 500 words explaining what the game teaches and citing at least one primary source from Unit 5 (al-Bakri, Ibn Battuta or Leo Africanus); a fair, respectful portrayal of African peoples and cultures, with no stereotypes; a list of at least three sources.</p>
<p><b>Turn in:</b> photos of the game, the rule sheet, the history guide, and the playtest record in the Week 25 lesson.</p>""" + rubric([
 ("Historical accuracy", ["Rich, accurate places, goods and events with no errors.", "Accurate places, goods and events.", "Some errors or thin history.", "Many errors."]),
 ("Geography in play", ["Geography shapes the strategy in several clever, accurate ways.", "At least one rule depends on real geography.", "Geography appears on the board but doesn't affect play.", "No real geography."]),
 ("Primary source and history guide", ["Clear, engaging guide with an accurate primary source and sharp analysis of its author and limits.", "Complete guide with an accurate primary source.", "Guide is short or the source is not analyzed.", "No guide or source."]),
 ("Game design", ["Clear rules, balanced play and a satisfying goal; revised after playtesting.", "Rules are clear and the game can be finished.", "Rules are confusing or the game stalls.", "Not playable."]),
 ("Respect and sources", ["Thoughtful, respectful portrayal of African peoples; three or more reliable sources listed.", "Respectful portrayal; three sources listed.", "Some careless portrayals or sources incomplete.", "Stereotypes or no sources."])]) + "</div>"

HTML = INTRO + ELA + SCI + SS
