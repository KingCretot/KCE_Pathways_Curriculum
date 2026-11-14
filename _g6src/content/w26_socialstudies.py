MAP = ('<svg viewBox="0 0 660 280" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Map of Mesoamerica showing the Olmec heartland on the Gulf Coast and Maya city-states in the Yucatan Peninsula, Guatemala and Belize">'
  '<rect width="660" height="280" fill="#cfe3f3"/>'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Mesoamerica: the Olmec and the Maya</text>'
  '<path d="M20 40 L250 40 L300 110 L340 150 L400 160 L420 110 L470 90 L540 95 L560 150 L540 200 L500 220 L470 260 L420 270 L380 240 L330 230 L250 210 L160 160 L80 110 L30 80Z" fill="#f3ead6" stroke="#b9a77a"/>'
  '<text x="120" y="80" fill="#8a6d1f" font-weight="bold">MEXICO</text><text x="320" y="70" fill="#0047BA" font-weight="bold">Gulf of Mexico</text><text x="150" y="255" fill="#0047BA" font-weight="bold">Pacific Ocean</text><text x="580" y="200" fill="#0047BA" font-weight="bold">Caribbean</text>'
  '<ellipse cx="320" cy="170" rx="42" ry="20" fill="#C9A84C" fill-opacity="0.45" stroke="#8a6d1f" stroke-dasharray="5 3"/><text x="275" y="200" fill="#8a6d1f" font-weight="bold">Olmec heartland</text><text x="270" y="213" fill="#8a6d1f" font-size="10">about 1200 to 400 BCE</text>'
  '<path d="M420 110 L470 90 L540 95 L560 150 L540 200 L500 220 L470 230 L430 210 L410 170Z" fill="#DB2F30" fill-opacity="0.15" stroke="#DB2F30"/><text x="470" y="125" fill="#DB2F30" font-weight="bold">Maya region</text><text x="458" y="138" fill="#DB2F30" font-size="10">Classic period 250 to 900 CE</text>'
  + ''.join(f'<circle cx="{x}" cy="{y}" r="4.5" fill="{c}"/><text x="{x+dx}" y="{y+dy}" fill="#0A1F3D" font-weight="bold" font-size="10">{n}</text>' for x, y, n, dx, dy, c in [
    (305, 165, "San Lorenzo", -58, -6, "#8a6d1f"), (340, 162, "La Venta", 6, -6, "#8a6d1f"), (420, 175, "Palenque", -50, 4, "#DB2F30"), (480, 190, "Tikal", 7, 4, "#DB2F30"), (462, 178, "Calakmul", -16, -8, "#DB2F30"), (495, 222, "Copán", 7, 6, "#DB2F30"), (500, 115, "Chichén Itzá", 7, -4, "#DB2F30")]) +
  '<text x="20" y="274" fill="#5b6676" font-size="10">Borders are approximate. Millions of Maya people live in this region today.</text></svg>')

LONGCOUNT = ('<svg viewBox="0 0 660 200" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Maya bar-and-dot numerals for 0 to 13 and a place-value example showing a shell for zero">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Maya numbers: dots are 1, bars are 5, a shell is 0</text>'
  + ''.join(
    f'<g transform="translate({30+i*44},40)"><rect width="38" height="80" rx="6" fill="#faf8f2" stroke="#e6dfcc"/>'
    + (f'<ellipse cx="19" cy="40" rx="13" ry="7" fill="none" stroke="#0A1F3D" stroke-width="2"/><path d="M8 40 h22 M12 36 v8 M19 34 v12 M26 36 v8" stroke="#0A1F3D" stroke-width="1.2"/>' if n == 0 else
       ''.join(f'<rect x="5" y="{66-b*10}" width="28" height="6" fill="#0A1F3D"/>' for b in range(n // 5)) +
       ''.join(f'<circle cx="{19-(n%5-1)*4.5+d*9}" cy="{58-(n//5)*10}" r="3.3" fill="#0A1F3D"/>' for d in range(n % 5)))
    + f'<text x="19" y="98" text-anchor="middle" fill="#0A1F3D" font-weight="bold">{n}</text></g>'
    for i, n in enumerate(range(14))) +
  '<text x="330" y="160" text-anchor="middle" fill="#0047BA">Maya numbers are base 20 and stack from bottom to top: a shell on the bottom and one dot above it means 1 × 20 + 0 = 20.</text>'
  '<text x="330" y="182" text-anchor="middle" fill="#5b6676" font-size="11">The Maya used a zero symbol by the 300s CE, one of the earliest in the world.</text></svg>')

LESSON = {
 "unit": "Unit 6: The Americas and the Meeting of Worlds",
 "title": "The Olmec and the Maya",
 "subtitle": "Long before Europeans crossed the Atlantic, the peoples of Mesoamerica built cities, wrote books, tracked the stars and invented a zero. This week you meet the Olmec, who carved giant stone heads, and the Maya, whose city-states, writing and mathematics still amaze scholars and whose descendants live in the region today.",
 "objectives": [
  "Locate Mesoamerica and explain how its geography supported farming and cities.",
  "Describe Olmec achievements and why historians call their culture a foundation for later Mesoamerica.",
  "Explain how Maya city-states were governed and how they used writing, astronomy and mathematics.",
  "Read Maya bar-and-dot numbers and explain the importance of zero.",
  "Evaluate causes of the Classic Maya decline and recognize that Maya people and cultures continue today."],
 "vocab": [
  ["Mesoamerica", "The region of southern Mexico and Central America where the Olmec, Maya, Mexica and other civilizations developed."],
  ["maize", "Corn, first domesticated in Mexico thousands of years ago; the most important food in Mesoamerica."],
  ["city-state", "An independent city that rules itself and the land around it."],
  ["glyph", "A symbol that stands for a word, sound or idea in a writing system."],
  ["codex", "A folded book; Maya codices were painted on bark paper (plural: codices)."],
  ["stela", "A tall carved stone monument, often recording a ruler's deeds and dates (plural: stelae)."]],
 "reconnect": {
  "title": "Week 25: Africa's trade networks",
  "intro": "Unit 5 showed how African empires connected the world. Now cross the Atlantic to civilizations that developed on their own.",
  "items": [
   {"t":"text","q":"What seasonal winds carried ships across the Indian Ocean?","a":[{"all":[["monsoon"]],"none":["not"]}],"show":"the monsoon winds","pts":2,"why":"They reverse about every six months."},
   {"t":"text","q":"Which people's ancestors built Great Zimbabwe?","a":[{"all":[["shona"]],"none":["not"]}],"show":"the Shona","pts":2,"why":"Colonial myths denied it; archaeology proved it."},
   {"t":"text","q":"Which city on the Niger became a world center of learning?","a":[{"all":[["timbuktu","tombouctou"]],"none":["not"]}],"show":"Timbuktu","pts":2,"why":"Books sold for more than any other goods."},
   {"t":"open","key":"rc_isolated","q":"The civilizations of Unit 5 traded with distant lands. Mesoamerica had no contact with Africa, Europe or Asia before 1492. Predict one way developing in isolation might make its civilizations different.","min":15,"rows":2,"rubric":["A reasonable prediction about crops, animals, technology or ideas developing independently"],"model":"They would develop their own crops, writing and calendars without borrowing from other continents, and they would have no horses or iron from the Old World."}]},
 "hook": {
  "title": "Heads of Stone",
  "visual": MAP,
  "html": "<p>In the 1860s, a farmworker in Veracruz, Mexico, found what he thought was an upside-down iron pot in the ground. It was the top of a colossal stone head nearly 5 feet tall. Since then, archaeologists have found 17 of these heads, some about 10 feet tall and weighing up to 40 tons, each with a different face and headdress. They were carved by the <b>Olmec</b> about 3,000 years ago from basalt hauled from mountains about 50 miles away, without wheels, iron tools or draft animals.</p><p>How did they do it, and who were they? This week you explore two of the Americas' great civilizations.</p><div class='callout'><b>Big question:</b> What did the Olmec and Maya achieve, and how do we know?</div>"},
 "learn": [
  {"title": "Mesoamerica and the Olmec",
   "html": "<p><b>Mesoamerica</b> stretches from central Mexico through Guatemala, Belize and Honduras. Its rainforests, highlands and rivers supported farming of the \"three sisters\" (<b>maize</b>, beans and squash), plus chocolate (cacao), chili peppers and avocados, all first grown here.</p><p>The <b>Olmec</b> lived along the Gulf Coast of Mexico from about 1200 to 400 BCE, at centers such as San Lorenzo and La Venta. (We don't know what they called themselves; Olmec is a later name meaning \"rubber people\" in Nahuatl, the Mexica language.) They:</p><ul><li>Carved colossal heads, probably portraits of rulers, and fine jade figures.</li><li>Built earthen platforms and plazas and organized large labor forces.</li><li>Played a ballgame with solid rubber balls, made from latex of the rubber tree, centuries before Europeans had rubber.</li><li>Traded jade, obsidian and shells across Mexico, spreading symbols and ideas later used by the Maya and others.</li></ul><p>Because so many later cultures used Olmec ideas, some historians have called them a \"mother culture.\" Others argue several Mesoamerican peoples developed together and influenced one another. Historians still debate it.</p>",
   "checks": [
    {"t":"text","q":"What are the \"three sisters\" crops of Mesoamerica? Name all three.","a":[{"all":[["maize","corn"],["bean"],["squash"]],"none":["not"]}],"show":"maize, beans and squash","pts":2,"why":"They grow well together and feed people well."},
    {"t":"open","key":"olmecheads","q":"The basalt for the colossal heads came from mountains about 50 miles away, and the heads weigh up to 40 tons. What does moving and carving them tell historians about Olmec society?","min":30,"rows":3,"rubric":["Explains what the effort shows about organization and leadership","Explains what it shows about skill, labor or resources"],"model":"Moving 40-ton stones 50 miles without wheels or draft animals needed hundreds of workers, careful planning and leaders powerful enough to organize and feed them. It shows the Olmec had skilled stone carvers, a strong government and enough food surplus to free people from farming."},
    {"t":"open","key":"mothersister","q":"Some historians call the Olmec a \"mother culture\"; others say Mesoamerican cultures were \"sister cultures\" that grew up together. What evidence would help decide between these views?","min":25,"rows":3,"rubric":["Explains the difference between the two views","Names a kind of evidence that would help (dates of artifacts, where symbols appear first, trade goods)"],"model":"If Olmec symbols and styles appear earlier than anywhere else and then spread outward, that supports \"mother culture.\" If similar symbols appear in several regions at the same time, with trade going both ways, that supports \"sister cultures.\" Careful dating of artifacts would help decide."}]},
  {"title": "Maya City-States",
   "html": "<p>The <b>Maya</b> built cities in southern Mexico, Guatemala, Belize and Honduras, flourishing especially in the <b>Classic period</b> (about 250 to 900 CE). There was never one Maya empire. Instead, dozens of <b>city-states</b>, including Tikal, Calakmul, Palenque and Copán, each had a ruler called a <i>k'uhul ajaw</i>, or holy lord. City-states traded, married into one another's royal families and fought wars, much like the Greek city-states you studied in Week 17.</p><p>Maya cities had stone pyramid temples, palaces, ball courts and plazas. Farmers fed huge populations by building raised fields, terraces and reservoirs. <b>K'inich Janaab' Pakal</b> became ruler of Palenque at age 12 in 615 CE and ruled for 68 years; his tomb, found deep inside the Temple of the Inscriptions in 1952, held a jade mosaic mask.</p>",
   "checks": [
    {"t":"num","q":"Pakal became ruler of Palenque in 615 CE and ruled for 68 years. In what year did his rule end?","a":683,"pts":2,"why":"615 + 68 = 683."},
    {"t":"open","key":"greekmaya","q":"Compare Maya city-states with the Greek city-states from Week 17. Give one similarity and one difference.","min":25,"rows":3,"rubric":["One accurate similarity","One accurate difference"],"model":"Like the Greeks, the Maya had independent city-states that shared a culture and religion but often fought each other. Unlike Athens, which developed democracy, Maya city-states were ruled by holy lords who claimed a connection to the gods."}]},
  {"title": "Writing, Mathematics and the Calendar",
   "visual": LONGCOUNT,
   "html": "<p>The Maya developed the most complete writing system in the ancient Americas, using about 800 <b>glyphs</b> that stand for whole words or syllables. They carved texts on <b>stelae</b> and buildings and painted <b>codices</b> on bark paper. Scholars could not read most Maya writing until the 1950s to 1980s, when researchers including Yuri Knorozov, Tatiana Proskouriakoff and Linda Schele, working with Maya speakers, cracked the code. Now we can read rulers' names, battles and dates.</p><p>Maya mathematics used three symbols, a dot for 1, a bar for 5 and a shell for zero, in a base-20 place-value system. Using zero, Maya astronomers built calendars of great accuracy, including a 365-day solar calendar, a 260-day ritual calendar and the <b>Long Count</b>, which counted days from a starting date in 3114 BCE.</p><p>In 1562, the Spanish friar Diego de Landa ordered Maya books burned at Maní, believing they were works of the devil. Only four Maya codices are known to survive today.</p>",
   "checks": [
    {"t":"num","q":"Using bars (5) and dots (1), what number is shown by 2 bars and 3 dots?","a":13,"pts":2,"why":"5 + 5 + 3 = 13."},
    {"t":"text","q":"How would you write 17 in Maya numbers? Tell how many bars and how many dots.","a":[{"all":[["3 bar","three bar"],["2 dot","two dot"]],"none":["not"]}],"show":"3 bars and 2 dots","pts":2,"why":"5 + 5 + 5 + 2 = 17."},
    {"t":"open","key":"zerovalue","q":"Why was having a symbol for zero such an important invention for Maya mathematicians and astronomers?","min":25,"rows":3,"rubric":["Explains that zero lets place value work (an empty place)","Connects to counting large numbers of days or tracking astronomy"],"model":"Zero lets a place-value system show an empty place, so the Maya could write very large numbers clearly, like the number of days since the Long Count began. That made it possible to track the movements of the sun, moon and Venus over centuries."},
    {"t":"open","key":"landa","q":"Diego de Landa ordered Maya books burned in 1562, and only four codices survive. What was lost, and how have historians and Maya communities worked to recover Maya history?","min":30,"rows":3,"rubric":["Explains what kind of knowledge was in the books","Names ways history has been recovered (reading stelae and buildings, archaeology, Maya languages and oral tradition)"],"model":"The books held Maya history, astronomy, religion and calendars, so centuries of knowledge were destroyed. Scholars recovered much of it by deciphering the inscriptions on stelae and buildings, working with Maya speakers, studying archaeology and listening to stories and traditions Maya communities kept alive."}]},
  {"title": "Decline and Continuity",
   "html": "<p>Between about 800 and 900 CE, many Classic Maya cities in the southern lowlands were abandoned. Scientists studying lake mud and cave formations have found evidence of severe droughts at that time. Historians think several causes worked together: drought, growing populations that strained farmland, constant warfare between city-states and loss of faith in rulers who could not bring rain.</p><p>But the Maya did not disappear. Cities in the north, such as Chichén Itzá, flourished afterward, and Maya kingdoms resisted Spanish conquest for nearly two centuries; the last independent Maya city, Nojpetén, fell in 1697. Today more than six million Maya people, including the K'iche', Yucatec, Q'eqchi', Mam and Kaqchikel, speak about 30 Mayan languages in Mexico, Guatemala and Belize. The K'iche' Maya preserved the <i>Popol Vuh</i>, their book of creation and history, written down in the 1500s.</p>",
   "checks": [
    {"t":"open","key":"declinecauses","q":"Explain how two causes of the Classic Maya decline could have worked together to make each other worse.","min":30,"rows":3,"rubric":["Names two causes","Explains how one made the other worse"],"model":"Drought reduced harvests just as populations were at their largest, so there wasn't enough food. Hungry city-states then fought more wars over farmland and water, which destroyed fields and drove people away, making the food shortage even worse."},
    {"t":"open","key":"stillhere","q":"Why is it inaccurate to say the Maya \"mysteriously vanished\"? Use evidence from the lesson.","min":25,"rows":3,"rubric":["States that Maya people and cultures continue","Uses at least two pieces of evidence"],"model":"Only some southern cities were abandoned; northern cities like Chichén Itzá kept going, Maya kingdoms resisted the Spanish until 1697, and more than six million Maya people speak Mayan languages today. The cities changed, but the people never vanished."}]}],
 "handson": {
  "title": "Maya Math Stela and the Glyph Name Card",
  "intro": "Carve a stela of your own in clay or foam, then compute with Maya numbers.",
  "materials": ["Air-dry clay, salt dough or a new craft foam sheet", "A pencil or craft stick for carving", "Dried beans (dots), craft sticks or pretzel sticks (bars), and small shells or paper circles (zero)", "Paper and pencil", "A family member"],
  "steps": [
   "Use beans for dots, craft sticks for bars and shells or paper circles for zero. Build the numbers 0 to 19.",
   "Build two-place numbers stacking upward: the bottom place counts ones, the place above counts twenties. Build 20, 45 and 100, then have a family member build a number for you to read.",
   "Add two Maya numbers by combining their dots and bars: five dots become a bar, and four bars in one place become one dot in the place above.",
   "Carve a stela: on clay, salt dough or foam, carve your name as your own glyph design, your birth year in Maya numbers and one achievement you are proud of.",
   "Keep beans, shells and small sticks away from young children (choking hazard) and pets; wash hands after using clay or dough."],
  "record": [
   {"t":"open","key":"stelarec","q":"Describe your stela: your glyph design, your birth year in Maya numbers (show the places) and your achievement. What was hardest about writing a large number in base 20?","min":40,"rows":4,"rubric":["Describes the glyph and achievement","Shows the birth year correctly in base-20 places","Reflects on what was hard"],"model":"My name glyph is a sun with a book, because I love reading outside. For 2014, I used three places: 5 × 400 = 2,000 on top (one bar), 0 × 20 in the middle (a shell), and 14 ones on the bottom (two bars and four dots). The hardest part was remembering that the third place counts 400s, not 100s."},
   {"t":"open","key":"addrec","q":"Show one addition problem you did with Maya numbers, including a regroup (five dots to a bar, or twenty in one place to one dot above).","min":25,"rows":3,"rubric":["A correct addition problem","Shows a regroup correctly"],"model":"I added 14 (two bars, four dots) and 9 (one bar, four dots). That made three bars and eight dots; five dots became one more bar, so four bars and three dots, or 23. Four bars is 20, so it regrouped to one dot in the twenties place and three dots in the ones place: 20 + 3 = 23."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"achievement","q":"Which Olmec or Maya achievement do you think was most impressive: the colossal heads, writing, the zero, the calendars or the cities? Make a claim and support it with at least two facts, then explain what it shows about the people who created it.","min":45,"rows":6,"rubric":["A clear claim","At least two accurate supporting facts","Explains what the achievement shows about the civilization"],"model":"The Maya zero is most impressive. The Maya were using a zero symbol by the 300s CE, centuries before it reached Europe, and it let them build calendars that counted days back to 3114 BCE. It shows that Maya scholars were brilliant mathematicians and astronomers who developed powerful ideas entirely on their own."},
   {"t":"open","key":"eraseknowledge","q":"Compare the burning of Maya books in 1562 with the attacks on Timbuktu's manuscripts in 2012 (Week 23). What do these events show about the power of written knowledge, and why do people try to destroy it?","min":57,"rows":5,"rubric":["Accurate details of both events","A comparison","An explanation of why people target written knowledge"],"model":"In 1562 Landa burned Maya books he called works of the devil, and in 2012 armed groups occupied Timbuktu and later burned thousands of manuscripts. In both cases, outsiders who wanted to control people attacked their written history. Books hold a people's memory, beliefs and identity, so destroying them is a way of trying to erase a culture, which is why communities risk so much to protect them."}]},
 "exit": [
  {"t":"text","q":"Which civilization carved the colossal stone heads?","a":[{"all":[["olmec"]],"none":["not"]}],"show":"the Olmec","pts":2,"why":"About 1200 to 400 BCE on Mexico's Gulf Coast."},
  {"t":"num","q":"In Maya numbers, what is 3 bars and 4 dots?","a":19,"pts":2,"why":"15 + 4 = 19."},
  {"t":"text","q":"What is the K'iche' Maya book of creation and history called?","a":[{"all":[["popol vuh","popol wuj"]],"none":["not"]}],"show":"the Popol Vuh","pts":2,"why":"Written down in the 1500s."},
  {"t":"open","key":"exit_maya","q":"In one or two sentences, explain why the Maya were not one empire.","min":12,"rows":2,"rubric":["Explains the city-state system with independent rulers"],"model":"The Maya lived in many independent city-states, each with its own holy lord, that traded, intermarried and fought but were never united under one ruler."}],
 "next": "Week 27: the Mexica (Aztec), the Inca and Cahokia."
}

TEACHER = {
 "standards": [
  "SS.6.G.2.1: Explain how major physical characteristics, natural resources, climate, and absolute and relative locations have influenced settlement, interactions, and the economies of ancient civilizations of the world.",
  "SS.6.W.1.3: Interpret primary and secondary sources.",
  "SS.6.W.1.5: Describe the roles of historians and recognize varying historical interpretations (historiography).",
  "SS.6.W.1.6: Describe how history transmits culture and heritage and provides models of human character."],
 "materials": ["The interactive lesson", "Air-dry clay, salt dough or a new craft foam sheet; a pencil or craft stick", "Dried beans, craft or pretzel sticks, small shells or paper circles", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 25 warm-up questions."],
  [4, "Hook", "The colossal heads; read the map."],
  [12, "The Olmec", "Three sisters; colossal heads; mother or sister culture."],
  [10, "Maya city-states", "Holy lords; Pakal; compare with Greece."],
  [13, "Writing, math, calendar", "Read bar-and-dot numbers; zero; decipherment; Landa."],
  [10, "Decline and continuity", "Causes working together; the Maya today."],
  [5, "Assign", "Set up the stela and Maya math; assign Think Deeper and the Exit Check."]],
 "key_questions": ["How did geography and farming support cities?", "How do we know what the Olmec and Maya did?", "What did zero make possible?", "Who are the Maya today?"],
 "misconceptions": ["The Maya were one empire.", "The Maya mysteriously vanished.", "The Olmec and Maya lived at the same time in the same place.", "Maya writing was only pictures."],
 "support": ["Provide a bar-and-dot chart for 0 to 19.", "Use a two-column chart: Olmec and Maya.", "Pre-teach Mesoamerica, maize and glyph."],
 "challenge": ["Research one Maya language spoken today and learn five words.", "Convert today's date into a Long Count date using an online converter and explain each place."],
 "background": "<p>Dates: Olmec about 1200 to 400 BCE (San Lorenzo about 1200 to 900, La Venta about 900 to 400); 17 colossal heads are known, the largest about 3 m tall; basalt from the Tuxtla Mountains. Maya Classic period about 250 to 900 CE; Pakal ruled Palenque 615 to 683 and his tomb was found by Alberto Ruz Lhuillier in 1952. Landa's auto-da-fé at Maní was in July 1562; four codices survive (Dresden, Madrid, Paris and the Maya Codex of Mexico). Nojpetén (Tayasal) fell in 1697. Estimates of Mayan-language speakers today range from about 6 to 7 million in roughly 30 languages. The \"mother culture\" debate is ongoing among archaeologists. Ancient Mesoamerica is outside Florida's Grade 6 NGSSS world history range (which ends with Rome); the standards above cover the skills taught.</p>",
 "sources": ["National Museum of Anthropology (Mexico), Olmec and Maya halls.", "Metropolitan Museum of Art, Heilbrunn Timeline: Olmec Art; Maya Art and Architecture.", "Coe, Michael D., Breaking the Maya Code (3rd ed., 2012).", "Smithsonian National Museum of the American Indian, Living Maya Time."]
}

PRINT = {
 "directions": "Answer in complete sentences.",
 "items": [
  {"q":"Where and when did the Olmec live, and name two of their achievements.","a":"Gulf Coast of Mexico, about 1200 to 400 BCE; colossal heads, the rubber ballgame, jade carving, trade networks.","lines":3},
  {"q":"How were Maya city-states governed?","a":"Each was independent, ruled by a holy lord (k'uhul ajaw).","lines":2},
  {"q":"Write these in Maya numbers (bars and dots): 8, 15, 19.","a":"8: 1 bar, 3 dots; 15: 3 bars; 19: 3 bars, 4 dots.","lines":2},
  {"q":"Why was zero important to the Maya?","a":"It made place value work, so they could write large numbers and build accurate calendars.","lines":2},
  {"q":"Name two causes of the Classic Maya decline.","a":"Drought, overpopulation, warfare, loss of faith in rulers.","lines":2},
  {"q":"Name two Maya peoples who live today.","a":"K'iche', Yucatec, Q'eqchi', Mam, Kaqchikel.","lines":1}]
}
