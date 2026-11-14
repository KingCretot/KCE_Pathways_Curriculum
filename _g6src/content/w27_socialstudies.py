AMERICAS = ('<svg viewBox="0 0 660 330" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Map of the Americas showing Cahokia on the Mississippi River, the Mexica Empire around Tenochtitlan in central Mexico, and the Inca Empire along the Andes in South America">'
  '<rect width="660" height="330" fill="#cfe3f3"/>'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Three great societies of the Americas before 1492</text>'
  '<path d="M60 30 L330 30 L360 70 L340 110 L300 130 L270 150 L240 160 L220 175 L250 190 L285 200 L300 215 L280 220 L250 212 L215 200 L190 175 L160 150 L120 120 L80 80Z" fill="#f3ead6" stroke="#b9a77a"/>'
  '<path d="M300 220 L340 225 L390 240 L430 260 L440 290 L420 320 L360 330 L330 300 L320 260Z" fill="#f3ead6" stroke="#b9a77a"/>'
  '<text x="150" y="60" fill="#8a6d1f" font-weight="bold">NORTH AMERICA</text><text x="360" y="300" fill="#8a6d1f" font-weight="bold">SOUTH AMERICA</text>'
  '<path d="M250 40 Q245 80 255 120" fill="none" stroke="#0047BA" stroke-width="3"/><text x="262" y="80" fill="#0047BA" font-size="10">Mississippi River</text>'
  '<circle cx="252" cy="95" r="6" fill="#2c6e22"/><text x="244" y="108" text-anchor="end" fill="#2c6e22" font-weight="bold">Cahokia</text><text x="244" y="121" text-anchor="end" fill="#2c6e22" font-size="10">about 1050 to 1200 CE</text>'
  '<ellipse cx="205" cy="180" rx="34" ry="16" fill="#DB2F30" fill-opacity="0.25" stroke="#DB2F30"/><circle cx="205" cy="180" r="5" fill="#DB2F30"/><text x="168" y="168" text-anchor="end" fill="#DB2F30" font-weight="bold">Mexica Empire</text><text x="168" y="181" text-anchor="end" fill="#DB2F30" font-size="10">Tenochtitlan, 1325 to 1521</text>'
  '<path d="M320 235 Q328 270 345 315" fill="none" stroke="#C9A84C" stroke-width="16" stroke-opacity="0.55"/><circle cx="330" cy="262" r="5" fill="#8a6d1f"/><text x="460" y="250" fill="#8a6d1f" font-weight="bold">Inca Empire</text><text x="460" y="263" fill="#8a6d1f" font-size="10">along the Andes; Cusco,</text><text x="460" y="276" fill="#8a6d1f" font-size="10">about 1438 to 1533</text><path d="M456 256 L336 262" stroke="#8a6d1f" stroke-dasharray="3 3"/>'
  '<text x="20" y="322" fill="#5b6676" font-size="10">Simplified, not to scale.</text></svg>')

QUIPU = ('<svg viewBox="0 0 660 220" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="A quipu: a main cord with hanging cords; knots in the hundreds, tens and ones positions record 242, 103 and 330">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Reading a quipu: knots on cords record numbers in base 10</text>'
  '<path d="M80 40 H580" stroke="#8a6d1f" stroke-width="6"/>'
  + ''.join(f'<path d="M{x} 40 V200" stroke="{c}" stroke-width="3"/>' for x, c in [(200, "#DB2F30"), (330, "#0047BA"), (460, "#2c6e22")]) +
  ''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="#0A1F3D"/>' for x, ys in [(200, [62, 72]), (330, [62]), (460, [62, 72, 82])] for y in ys) +
  ''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="#0A1F3D"/>' for x, ys in [(200, [110, 120, 130, 140]), (460, [110, 120, 130])] for y in ys) +
  ''.join(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="6" fill="#0A1F3D"/>' for x, ys in [(200, [166, 182]), (330, [160, 175, 190])] for y in ys) +
  '<text x="70" y="72" fill="#5b6676" text-anchor="end" font-size="11">hundreds</text><text x="70" y="128" fill="#5b6676" text-anchor="end" font-size="11">tens</text><text x="70" y="182" fill="#5b6676" text-anchor="end" font-size="11">ones</text>'
  '<text x="200" y="214" text-anchor="middle" fill="#DB2F30" font-weight="bold">242</text><text x="330" y="214" text-anchor="middle" fill="#0047BA" font-weight="bold">103</text><text x="460" y="214" text-anchor="middle" fill="#2c6e22" font-weight="bold">330</text>'
  '<text x="600" y="128" fill="#5b6676" font-size="11">no knots</text><text x="600" y="142" fill="#5b6676" font-size="11">= zero</text></svg>')

LESSON = {
 "unit": "Unit 6: The Americas and the Meeting of Worlds",
 "title": "The Mexica (Aztec), the Inca and Cahokia",
 "subtitle": "In 1491, one of the world's largest cities stood on an island in a Mexican lake, the largest empire on Earth's longest mountain range ran on roads and knotted cords, and a great city of earthen mounds had already risen and fallen beside the Mississippi. This week you meet the Mexica, the Inca and the people of Cahokia.",
 "objectives": [
  "Explain how the Mexica built Tenochtitlan and governed through tribute.",
  "Explain how the Inca organized a huge empire using roads, the mit'a labor system and quipus.",
  "Describe Cahokia and the Mississippian culture of North America.",
  "Analyze a primary source describing Tenochtitlan, considering its author's point of view.",
  "Compare how the three societies adapted to their environments and organized power."],
 "vocab": [
  ["Mexica", "The people, often called Aztecs, who founded Tenochtitlan and led the Triple Alliance in central Mexico."],
  ["chinampa", "A raised farm field built in shallow lake water from mud and plants."],
  ["tribute", "Payments of goods or labor that conquered peoples must give to a ruling power."],
  ["Inca", "The rulers of Tawantinsuyu, an empire along the Andes Mountains of South America."],
  ["quipu", "An Inca recording device of knotted cords used to track numbers and possibly other information."],
  ["Mississippian culture", "Farming societies along the Mississippi and its rivers that built large earthen mounds, about 800 to 1600 CE."]],
 "reconnect": {
  "title": "Week 26: The Olmec and the Maya",
  "intro": "The Mexica and Inca built on ideas older Mesoamerican and Andean peoples developed. Start with last week.",
  "items": [
   {"t":"text","q":"What are the \"three sisters\" crops? Name all three.","a":[{"all":[["maize","corn"],["bean"],["squash"]],"none":["not"]}],"show":"maize, beans and squash","pts":2,"why":"They fed the Maya and the Mexica; maize also fed Cahokia."},
   {"t":"num","q":"In Maya numbers, what is 2 bars and 4 dots?","a":14,"pts":2,"why":"10 + 4 = 14."},
   {"t":"text","q":"What were the Maya rulers of each city-state called (in English)?","a":[{"all":[["holy lord","k'uhul ajaw","kuhul ajaw","ajaw"]],"none":["not"]}],"show":"holy lords (k'uhul ajaw)","pts":2,"why":"Each city-state had its own."},
   {"t":"open","key":"rc_empire","q":"The Maya never united into one empire. Predict one advantage an empire might have over separate city-states, and one challenge it would face.","min":15,"rows":2,"rubric":["One advantage","One challenge"],"model":"An empire could gather resources and soldiers from a huge area, but it would be hard to control distant peoples who resented paying it."}]},
 "hook": {
  "title": "A City Like a Dream",
  "visual": AMERICAS,
  "html": "<p>In November 1519, Spanish soldiers and their Indigenous allies stood on a causeway and saw Tenochtitlan for the first time. Decades later one of the soldiers, Bernal Díaz del Castillo, remembered the moment. In John Ingram Lockhart's 1844 English translation:</p><blockquote>\"Our astonishment was indeed raised to the highest pitch, and we could not help remarking to each other, that all these buildings resembled the fairy castles we read of in Amadis de Gaul; so high, majestic, and splendid did the temples, towers, and houses of the town, all built of massive stone and lime, rise up out of the midst of the lake. Indeed, many of our men believed what they saw was a mere dream.\"</blockquote><p class='small'><i>Amadis de Gaul</i> = a popular Spanish fantasy novel of knights and castles. Díaz is describing the towns built in the lake, with Tenochtitlan (which the Spanish called Mexico) at their center.</p><p>Tenochtitlan was larger than any city in Spain. Who built it, and how?</p><div class='callout'><b>Big question:</b> How did the Mexica, Inca and Cahokians build great societies, and how did their environments shape them?</div>"},
 "learn": [
  {"title": "The Mexica and Tenochtitlan",
   "html": "<p>According to their history, the <b>Mexica</b> migrated south and founded <b>Tenochtitlan</b> in 1325 on an island in Lake Texcoco, where they saw an eagle on a cactus, the image on Mexico's flag today. They turned a swampy island into a city of perhaps 200,000 people, one of the largest in the world:</p><ul><li>Three <b>causeways</b> linked the island to the shore, and an aqueduct brought fresh water.</li><li><b>Chinampas</b>, raised fields built from lake mud, produced several harvests a year.</li><li>The great market at Tlatelolco drew tens of thousands of people a day.</li></ul><p>In 1428 Tenochtitlan formed the <b>Triple Alliance</b> with Texcoco and Tlacopan and conquered much of central Mexico. Conquered peoples kept their own rulers but paid <b>tribute</b> in cotton cloth, cacao, feathers, gold and captives. The Mexica language, <b>Nahuatl</b>, gave English words such as chocolate, tomato and avocado, and about 1.7 million people speak it today.</p>",
   "checks": [
    {"t":"text","q":"What were the raised farm fields built in Lake Texcoco called?","a":[{"all":[["chinampa"]],"none":["not"]}],"show":"chinampas","pts":2,"why":"They allowed several harvests a year."},
    {"t":"open","key":"tribute","q":"The Mexica let conquered peoples keep their rulers but demanded tribute. Give one advantage and one danger of this system for the Mexica.","min":25,"rows":3,"rubric":["One advantage","One danger"],"model":"An advantage was that the Mexica didn't need to govern every town directly, yet they received huge wealth. The danger was that heavy tribute made conquered peoples such as the Totonacs of Cempoala resent them, so they joined the Spanish, along with the Tlaxcalans, longtime enemies the Mexica had never conquered."},
    {"t":"open","key":"diazsource","q":"Reread Bernal Díaz's description. What does it tell us about Tenochtitlan, and what should a historian remember about who wrote it and when?","min":30,"rows":3,"rubric":["What the source shows about the city","A consideration about the author's point of view or timing"],"model":"It shows Tenochtitlan was enormous and grand, with tall stone temples rising from the lake, so impressive the Spanish thought it was a dream. A historian should remember Díaz was a conquistador writing decades later, so his memory may have changed, and he wrote partly to defend the conquest."}]},
  {"title": "The Inca: An Empire on the Mountains",
   "visual": QUIPU,
   "html": "<p>The <b>Inca</b> called their empire <b>Tawantinsuyu</b>, \"the four parts together.\" Starting in 1438 under the ruler <b>Pachacuti</b>, they expanded from Cusco until they ruled about 10 million people along 2,500 miles of the Andes, the largest empire in the Americas.</p><ul><li><b>Roads:</b> about 25,000 miles of roads, the Qhapaq Ñan, with stone steps, rope suspension bridges and rest houses. Relay runners called chasquis carried messages up to about 150 miles a day.</li><li><b>Mit'a:</b> instead of money taxes, families owed labor: building roads and terraces, farming state lands or serving in the army.</li><li><b>Farming:</b> terraces turned steep slopes into fields, and Andean farmers grew hundreds of kinds of potatoes, freeze-drying them into chuño that kept for years.</li><li><b>Quipus:</b> the Inca had no writing system as we know it, but officials recorded numbers on knotted cords, using a base-10 place-value system.</li></ul><p>Machu Picchu, a royal estate built in the 1400s, is the empire's most famous site. Inca resistance continued at Vilcabamba until 1572. About 8 to 10 million people speak Quechua, the Inca language, today.</p>",
   "checks": [
    {"t":"num","q":"Read the blue quipu cord: 1 knot in the hundreds place, none in the tens and 3 in the ones place. What number is it?","a":103,"pts":2,"why":"100 + 0 + 3 = 103."},
    {"t":"open","key":"roadsrule","q":"Explain how the Inca road system helped them rule such a large, mountainous empire. Give two ways.","min":25,"rows":3,"rubric":["Two specific ways the roads helped govern"],"model":"The roads let armies move quickly to put down rebellions, and chasqui runners carried messages and quipu records so rulers in Cusco knew what was happening across the empire. They also moved food from storehouses to places with bad harvests."},
    {"t":"open","key":"mita","q":"Compare the Inca mit'a labor system with paying taxes in money. Why might the Inca have used labor instead of coins?","min":25,"rows":3,"rubric":["Explains what mit'a was","A reasonable reason for labor instead of money"],"model":"In mit'a, families paid the state with work, like building roads, instead of money. The Inca didn't use coins or markets the way Europeans did, and they needed huge amounts of labor for roads, terraces and storehouses, so work was the most useful payment."}]},
  {"title": "Cahokia: A City of Mounds",
   "html": "<p>North America had cities too. Near present-day St. Louis, the Mississippian city of <b>Cahokia</b> reached its peak about 1050 to 1200 CE, with perhaps 10,000 to 20,000 people, possibly larger than London at the time.</p><ul><li><b>Monks Mound</b>, about 100 feet tall with a base covering about 14 acres, is the largest earthen mound in the Americas. It was built by hand, basket by basket, from millions of loads of soil.</li><li>Cahokians built more than 100 mounds, a grand plaza and circles of wooden posts (archaeologists call them \"Woodhenge\") that marked sunrise on the solstices and equinoxes.</li><li>They farmed maize and traded for copper from the Great Lakes, shells from the Gulf of Mexico and mica from the Appalachians.</li></ul><p>Cahokia was largely abandoned by about 1350, possibly because of flooding, drought, environmental strain or conflict. Many Native nations, including the Osage Nation (in Oklahoma today), have traditions connected to Mississippian peoples, and Mississippian mound towns once stood in Florida too, such as at Lake Jackson near Tallahassee.</p>",
   "checks": [
    {"t":"text","q":"What is the name of the largest earthen mound in the Americas, at Cahokia?","a":[{"all":[["monks"]],"none":["not"]}],"show":"Monks Mound","pts":2,"why":"About 100 feet tall."},
    {"t":"open","key":"cahokiatrade","q":"Archaeologists found Great Lakes copper, Gulf of Mexico shells and Appalachian mica at Cahokia. What does this evidence show?","min":20,"rows":2,"rubric":["Concludes there were long-distance trade networks","Connects to Cahokia's importance or wealth"],"model":"It shows Cahokia was the center of a trade network reaching across much of North America, so it was a wealthy, important city that people traveled long distances to trade with."}]},
  {"title": "Three Societies, Three Environments",
   "html": "<p>Each society adapted to its environment:</p><ul><li>The Mexica turned a lake into farmland with chinampas and built a city on water.</li><li>The Inca turned mountains into farmland with terraces and connected them with roads.</li><li>Cahokians used the rich river floodplain for maize and the river for trade.</li></ul><p>The Mexica and Inca empires fell to Spanish invaders and their Indigenous allies in 1521 and 1533, aided by smallpox and other diseases that killed huge numbers of people, and in the Inca case by a civil war between the brothers Atahualpa and Huáscar. In Week 29 you'll study how contact after 1492 changed both sides of the Atlantic.</p>",
   "checks": [
    {"t":"open","key":"envadapt","q":"Choose two of the three societies and compare how each changed its environment to grow food.","min":29,"rows":3,"rubric":["Two societies with accurate farming methods","A comparison"],"model":"The Mexica built chinampas, piling lake mud into raised fields in shallow water, while the Inca carved terraces into steep mountainsides. Both turned land that seemed useless for farming into fields that fed huge populations."}]}],
 "handson": {
  "title": "Make a Quipu",
  "intro": "Record real data from your home on a quipu, then challenge a family member to read it.",
  "materials": ["A thick piece of yarn or string about 2 feet long (the main cord)", "6 to 8 pieces of yarn about 1 foot long, in two or three colors", "Scissors and a ruler", "Paper and pencil", "A family member"],
  "steps": [
   "Choose data to record from your home or homeschool: for example, pages read each day this week, minutes of practice, or the number of birds seen at a feeder.",
   "Tie each short cord to the main cord. Use colors to stand for categories (for example, red for reading and blue for math).",
   "Tie knots to record each number: a cluster of single knots near the top for hundreds, a cluster in the middle for tens and a cluster near the bottom for ones. Leave a space with no knots for zero.",
   "Give your quipu to a family member without telling them the numbers. Explain only the color code and place values, and see whether they can read your data.",
   "Keep yarn away from toddlers and pets."],
  "record": [
   {"t":"open","key":"quipurec","q":"What data did you record, what did each color stand for, and could your family member read it correctly? What would make a quipu hard to read without the person who made it?","min":40,"rows":4,"rubric":["Describes the data and color code","Reports whether it was read correctly","Explains a challenge of reading a quipu without its maker"],"model":"I recorded pages read (red) and minutes of piano practice (blue) for four days. My dad read the numbers correctly once I told him the color code, but he couldn't have known what the colors meant without me. Inca quipu-keepers trained for years, so today many quipus are hard to read because the meanings of colors and patterns were lost."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"greatestfeat","q":"Which achievement do you think was most impressive: Tenochtitlan's chinampas and causeways, the Inca road system, or Monks Mound? Make a claim and support it with at least two facts.","min":45,"rows":5,"rubric":["A clear claim","At least two accurate facts","Explains why it is most impressive"],"model":"The Inca road system was most impressive. The Inca built about 25,000 miles of roads across the Andes, with rope bridges over canyons, and relay runners carried messages up to 150 miles a day. Building that across the world's longest mountain range without iron tools or wheeled carts shows incredible engineering and organization."},
   {"t":"open","key":"compareworld","q":"Compare the Inca roads with Persia's Royal Road (Week 16) or Rome's roads (Week 18). How did each empire use roads to hold power?","min":43,"rows":5,"rubric":["Accurate details about both road systems","At least one similarity","At least one difference"],"model":"Like Persia's Royal Road with its relay riders, the Inca had chasqui runners carrying messages quickly, and both empires used roads to move armies and govern distant lands. But Persian riders used horses on mostly flatter ground, while Inca runners carried messages on foot over steep mountain steps and rope bridges."}]},
 "exit": [
  {"t":"text","q":"On what lake did the Mexica build Tenochtitlan?","a":[{"all":[["texcoco"]],"none":["not"]}],"show":"Lake Texcoco","pts":2,"why":"Founded in 1325."},
  {"t":"text","q":"What knotted-cord device did the Inca use to keep records?","a":[{"all":[["quipu","khipu"]],"none":["not"]}],"show":"the quipu (khipu)","pts":2,"why":"Base-10 knots."},
  {"t":"text","q":"Near which present-day U.S. city are the Cahokia mounds?","a":[{"all":[["st. louis","st louis","saint louis","collinsville"]],"none":["not"]}],"show":"St. Louis (Collinsville, Illinois)","pts":2,"why":"Beside the Mississippi River."},
  {"t":"open","key":"exit_tribute","q":"In one or two sentences, explain what tribute was in the Mexica Empire.","min":12,"rows":2,"rubric":["Defines tribute as goods or labor paid by conquered peoples to the Mexica"],"model":"Tribute was the goods, like cloth, cacao and feathers, that conquered peoples had to send to the Mexica as payment for being ruled."}],
 "next": "Week 28: Indigenous Peoples of Florida."
}

TEACHER = {
 "standards": [
  "SS.6.G.2.1: Explain how major physical characteristics, natural resources, climate, and absolute and relative locations have influenced settlement, interactions, and the economies of ancient civilizations of the world.",
  "SS.6.E.3.4: Describe the relationship among civilizations that engage in trade, including the benefits and drawbacks of voluntary trade.",
  "SS.6.W.1.3: Interpret primary and secondary sources.",
  "SS.6.W.1.6: Describe how history transmits culture and heritage and provides models of human character."],
 "materials": ["The interactive lesson", "Yarn or string: one 2-foot main cord and 6 to 8 one-foot cords in two or three colors; scissors and a ruler", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 26 warm-up questions."],
  [5, "Hook", "Bernal Díaz's description; read the map."],
  [13, "The Mexica", "Chinampas, causeways, tribute; analyze the source."],
  [13, "The Inca", "Roads, mit'a, terraces; read a quipu."],
  [9, "Cahokia", "Monks Mound, Woodhenge, trade."],
  [8, "Three environments", "Compare adaptations; preview Week 29."],
  [6, "Assign", "Set up the quipu; assign Think Deeper and the Exit Check."]],
 "key_questions": ["How did geography shape this society?", "How did rulers hold such large territories?", "Who wrote this source, and when?", "What evidence shows these were connected, complex societies?"],
 "misconceptions": ["The Americas had no cities before Europeans arrived.", "Aztec is what the Mexica called themselves.", "The Inca had no way to keep records.", "A small number of Spanish soldiers conquered empires alone (they had many Indigenous allies, and disease devastated the population)."],
 "support": ["Use a three-column chart: Mexica, Inca, Cahokia.", "Practice reading the quipu diagram together.", "Pre-teach chinampa, tribute and quipu."],
 "challenge": ["Research the Codex Mendoza's tribute pages and what they show about Mexica tribute.", "Find out how researchers are trying to decode non-number information in quipus."],
 "background": "<p>Dates and figures: Tenochtitlan founded 1325 (traditional date); Triple Alliance 1428; population estimates range from about 150,000 to 300,000; fall of Tenochtitlan August 13, 1521. Pachacuti's expansion began about 1438; estimates of the Inca population range from about 6 to 14 million; road network estimates about 40,000 km (25,000 mi); the Qhapaq Ñan became a UNESCO World Heritage Site in 2014; Atahualpa was captured in 1532 and executed in 1533. Cahokia's population estimates range from about 10,000 to 20,000 at the core (some estimates higher); Monks Mound is about 30 m tall; UNESCO 1982. Nahuatl speakers about 1.7 million (INEGI); Quechua speakers estimates vary widely (about 8 to 10 million). The Bernal Díaz quotation is from the 1844 Lockhart translation (Project Gutenberg eBook #32474), checked against the text. The Americas before 1492 are outside Florida's Grade 6 NGSSS world history range; the standards above cover the skills taught.</p>",
 "sources": ["Díaz del Castillo, Bernal, The Memoirs of the Conquistador Bernal Diaz del Castillo, trans. John Ingram Lockhart (1844), Project Gutenberg eBook #32474.", "UNESCO, Qhapaq Ñan, Andean Road System; Cahokia Mounds State Historic Site.", "Smithsonian National Museum of the American Indian, The Great Inka Road.", "Mann, Charles C., 1491: New Revelations of the Americas Before Columbus (2005)."]
}

PRINT = {
 "directions": "Answer in complete sentences.",
 "items": [
  {"q":"How did the Mexica build a city in a lake and feed its people?","a":"Causeways and an aqueduct; chinampas, raised fields of lake mud with several harvests a year.","lines":3},
  {"q":"What was tribute?","a":"Goods or labor that conquered peoples paid to the Mexica.","lines":2},
  {"q":"Name three ways the Inca held their empire together.","a":"Roads and chasqui runners, the mit'a labor system, quipu records, storehouses.","lines":2},
  {"q":"Read this quipu cord: 3 knots (hundreds), 0 (tens), 7 (ones).","a":"307.","lines":1},
  {"q":"Describe Cahokia and Monks Mound.","a":"A Mississippian city near St. Louis, peak about 1050 to 1200; Monks Mound is the largest earthen mound in the Americas.","lines":3},
  {"q":"What should a historian keep in mind when reading Bernal Díaz?","a":"He was a conquistador writing decades later, partly to defend the conquest.","lines":2}]
}
