ROUTES = ('<svg viewBox="0 0 660 260" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Unit 5 review map of Africa&apos;s trade networks: trans-Saharan routes to Ghana, Mali and Songhai, and Indian Ocean routes to the Swahili Coast and Great Zimbabwe">'
  '<rect width="660" height="260" fill="#f3ead6"/>'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Unit 5 review: two great African trade networks</text>'
  '<path d="M60 40 L420 40 L470 90 L520 150 L480 250 L380 250 L330 200 L200 190 L90 170 L50 110Z" fill="#efdcae" stroke="#b9a77a"/>'
  '<text x="230" y="70" fill="#8a6d1f" font-weight="bold" letter-spacing="3">SAHARA</text>'
  '<path d="M520 150 L560 140 L640 140 L640 250 L480 250Z" fill="#cfe3f3"/><text x="580" y="200" fill="#0047BA" font-weight="bold">Indian Ocean</text>'
  + ''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="{c}"/><text x="{x+dx}" y="{y+dy}" fill="#0A1F3D" font-weight="bold" font-size="10">{n}</text>' for x, y, n, dx, dy, c in [
    (130, 150, "Koumbi Saleh (Ghana)", -40, 18, "#8a6d1f"), (190, 160, "Niani (Mali)", 6, 16, "#C9A84C"), (230, 140, "Timbuktu", -20, -8, "#DB2F30"), (290, 150, "Gao (Songhai)", 6, -6, "#DB2F30"),
    (505, 175, "Malindi", 8, 4, "#0047BA"), (495, 205, "Kilwa", 8, 4, "#0047BA"), (480, 235, "Sofala", 8, 4, "#0047BA"), (420, 235, "Great Zimbabwe", -95, 4, "#0A1F3D")]) +
  '<path d="M160 40 Q170 100 135 145" fill="none" stroke="#8a6d1f" stroke-width="2.5" stroke-dasharray="6 4"/><path d="M250 40 Q250 90 232 135" fill="none" stroke="#8a6d1f" stroke-width="2.5" stroke-dasharray="6 4"/>'
  '<text x="70" y="56" fill="#8a6d1f" font-size="10">camel caravans: salt south, gold north</text>'
  '<path d="M425 235 L475 235" stroke="#C9A84C" stroke-width="3"/><path d="M640 160 Q580 165 510 178" fill="none" stroke="#0047BA" stroke-width="2.5" stroke-dasharray="6 4"/>'
  '<text x="545" y="155" fill="#0047BA" font-size="10">dhows on the monsoon</text></svg>')

LESSON = {
 "unit": "Unit 5: Empires and Global Trade",
 "title": "Unit 5 Checkpoint and Trade Route Project",
 "subtitle": "Ghana, Mali, Songhai, the Swahili city-states and Great Zimbabwe: this week you connect the African empires and trading cities of Unit 5, finish your trade route project, and show your mastery on the Unit 5 checkpoint.",
 "objectives": [
  "Compare the trans-Saharan and Indian Ocean trade networks.",
  "Explain how geography and trade shaped Ghana, Mali, Songhai, the Swahili Coast and Great Zimbabwe.",
  "Analyze primary sources and archaeology about African history.",
  "Explain how historians corrected myths that denied African achievement.",
  "Demonstrate mastery of Unit 5 on the checkpoint (85 or higher)."],
 "vocab": [
  ["trade network", "A system of routes, cities and merchants that moves goods over long distances."],
  ["primary source", "A source created by someone who was there at the time, such as a traveler's account."],
  ["archaeology", "The study of the past through objects, buildings and other remains."],
  ["cultural diffusion", "The spread of ideas, beliefs and customs from one group to another."]],
 "reconnect": {
  "title": "Unit 5, one question from each week",
  "intro": "Warm up with one question from each week of the unit.",
  "items": [
   {"t":"text","q":"Week 21: Which animal made it possible to cross the Sahara with heavy loads?","a":[{"all":[["camel"]],"none":["not"]}],"show":"the camel","pts":2,"why":"Camels can go many days without water."},
   {"t":"text","q":"Week 22: Which ruler of Mali made a famous hajj to Mecca in 1324?","a":[{"all":[["musa"]],"none":["not"]}],"show":"Mansa Musa","pts":2,"why":"His gold lowered its value in Cairo."},
   {"t":"text","q":"Week 23: Which Songhai ruler divided the empire into provinces?","a":[{"all":[["askia","muham","moham"]],"none":["not","sunni"]}],"show":"Askia Muhammad","pts":2,"why":"He ruled from 1493 to 1528."},
   {"t":"text","q":"Week 24: Which people's ancestors built Great Zimbabwe?","a":[{"all":[["shona"]],"none":["not"]}],"show":"the Shona","pts":2,"why":"A Bantu-speaking people of Zimbabwe."}]},
 "hook": {
  "title": "Gold That Crossed Deserts and Oceans",
  "visual": ROUTES,
  "html": "<p>In the 1300s, gold from West Africa paid for goods in Cairo and Europe, and gold from Great Zimbabwe reached Arabia, India and China. Two great trade networks, one across the sand and one across the sea, made African kingdoms and cities rich and connected them to the wider world, carrying Islam, scholarship and ideas along with goods.</p><div class='callout'><b>Big question:</b> How did trade shape Africa's empires and cities, and how do we know?</div>"},
 "learn": [
  {"title": "Review: West African Empires",
   "html": "<p><b>Ghana</b> (Week 21) grew rich by taxing the gold-salt trade. <b>Mali</b> (Week 22), founded by Sundiata and made famous by Mansa Musa, controlled more gold and grew larger. <b>Songhai</b> (Week 23), built by Sunni Ali and organized by Askia Muhammad, became the largest, until Moroccan guns defeated it at Tondibi in 1591. Each empire relied on the Niger River and on trade across the Sahara, and Timbuktu became a world center of learning.</p>",
   "checks": [
    {"t":"order","q":"Put these events in order.","items":["Ghana taxes the gold-salt trade","Sundiata founds Mali","Mansa Musa's hajj","Askia Muhammad organizes Songhai","Battle of Tondibi"],"pts":2,"why":"Ghana, then Mali, then Songhai."},
    {"t":"open","key":"empirecompare","q":"Choose two of the West African empires and compare how each gained and kept its wealth.","min":30,"rows":3,"rubric":["Two empires named","How each gained wealth, with specifics","One similarity or difference"],"model":"Ghana grew rich by taxing the gold and salt that passed through its lands, without controlling the gold mines themselves. Mali controlled the gold fields and the trade cities directly, so it grew even richer, as Mansa Musa's hajj showed. Both depended on the trans-Saharan trade."}]},
  {"title": "Review: East Africa and the Indian Ocean",
   "html": "<p>On the east coast (Week 24), Swahili city-states such as Kilwa, Mombasa and Malindi grew rich trading gold, ivory and iron for cloth, beads and porcelain, sailing with the monsoon winds. Inland, the ancestors of the Shona built Great Zimbabwe, whose rulers controlled the plateau's gold. Swahili culture blended a Bantu language and African traditions with Islam and Arabic words.</p>",
   "checks": [
    {"t":"open","key":"diffusion","q":"Give one example of cultural diffusion from the trans-Saharan trade and one from the Indian Ocean trade.","min":25,"rows":3,"rubric":["A correct example from each network","Explains what spread and how"],"model":"Across the Sahara, Islam and Arabic writing spread to West Africa with Muslim traders and scholars, helping Timbuktu become a center of learning. On the Indian Ocean, Arabic words entered the Swahili language, and Chinese porcelain became a prized decoration in Swahili homes."}]},
  {"title": "Review: How We Know",
   "html": "<p>Historians use many kinds of evidence: travelers' accounts (al-Bakri, Ibn Battuta, Leo Africanus), African sources (griots, Timbuktu's manuscripts, Ahmad Baba's books) and archaeology (Kilwa's stone mosque, Great Zimbabwe's walls and imported goods). They compare sources, ask who wrote each one and why, and check them against physical evidence. That method exposed the myth that Africans could not have built Great Zimbabwe.</p>",
   "checks": [
    {"t":"open","key":"evidencetype","q":"Choose one written source and one piece of archaeological evidence from Unit 5. Explain what each tells historians and one limit of each.","min":35,"rows":4,"rubric":["One written source with what it shows and one limit","One archaeological find with what it shows and one limit"],"model":"Ibn Battuta's account of Mali tells us how safe and just the empire seemed to a visitor, but he judged some customs by his own culture. Great Zimbabwe's walls show the builders' skill and wealth, but stones can't tell us the rulers' names or what people believed."}]}],
 "handson": {
  "title": "Trade Route Board Game Playtest",
  "intro": "Test the board game you built for your trade route project with a family member.",
  "materials": ["Your trade route project game board, map or pieces", "Index cards and a marker", "A die", "Small household items or paper squares as goods and coins", "A family member", "Paper and pencil"],
  "steps": [
   "Set up the game board you made for the project (see the Unit 5 projects page).",
   "Write 10 event cards based on real history (for example, \"Sandstorm: lose a turn,\" \"Monsoon reverses: sail home,\" \"Mansa Musa's gold floods Cairo: gold is worth half\").",
   "Play one full game with a family member. Record every rule that was unclear and every time history and the game didn't match.",
   "Revise your rules and one event card based on the playtest.",
   "Keep small pieces and the die away from young children (choking hazard) and pets."],
  "record": [
   {"t":"open","key":"playtestrec","q":"Describe your playtest. Which event card taught the most history, which rule did you revise and why, and what did your family member learn?","min":45,"rows":4,"rubric":["Names an event card and the history it teaches","Describes a rule revision and the reason","Reports what the player learned"],"model":"The best card was \"Monsoon reverses: you must wait in port until April,\" because it showed why merchants stayed for months. My sister found that the camel route was too easy, so I added a water rule: caravans must stop at an oasis every three spaces. She said she never knew African cities traded with China."}]},
 "think": {
  "intro": "Your teacher scores this.",
  "items": [
   {"t":"open","key":"unitreflect","q":"Many history books once left Africa out of world history before 1500. Using at least three examples from Unit 5, explain why that was a serious mistake.","min":56,"rows":6,"rubric":["A clear claim","At least three accurate examples from Unit 5","Explains what is lost when Africa is left out"],"model":"Leaving Africa out was a serious mistake because African empires were at the center of world trade. Mali's gold was so plentiful that Mansa Musa's visit changed prices in Cairo. Timbuktu was a world center of learning with scholars and libraries. Kilwa and Great Zimbabwe traded with Arabia, India and China. Without Africa, the story of medieval gold, Islam and the Indian Ocean makes no sense."}]},
 "checkpoint": {
  "title": "Unit 5 Checkpoint: Empires and Global Trade",
  "intro": "This checkpoint covers Weeks 21 to 24. Answer every question; use evidence and specific names and dates where you can. Mastery is 85 or higher. If you score below 85, your teacher will review with you, then you will retake it.",
  "parts": [
   {"title": "Part A: West African empires", "items": [
    {"t":"text","q":"Which two goods were traded for each other across the Sahara?","a":[{"all":[["gold"],["salt"]],"none":["not gold","not salt"]}],"show":"gold and salt","pts":3,"why":"Gold came from the south; salt from Saharan mines."},
    {"t":"text","q":"Who founded the Mali Empire, according to the epic preserved by griots?","a":[{"all":[["sundiata","sunjata","sondiata"]],"none":["not"]}],"show":"Sundiata Keita","pts":3,"why":"He defeated Sumanguru at Kirina."},
    {"t":"open","key":"cpmusa","q":"Explain one cause and two effects of Mansa Musa's hajj.","min":25,"rows":3,"pts":4,"rubric":["A correct cause","Two correct effects"],"model":"He made the hajj because he was a devout Muslim and the pilgrimage is a duty for those able to go. His gold made its value fall in Cairo, and the journey put Mali on European maps like the Catalan Atlas."},
    {"t":"open","key":"cptondibi","q":"Explain two causes of Songhai's fall in 1591.","min":20,"rows":3,"pts":4,"rubric":["Two correct causes, explained"],"model":"Morocco's army had guns and cannons that Songhai's spears and bows could not match, and Songhai had been weakened by a civil war between rival princes in the late 1580s."}]},
   {"title": "Part B: Timbuktu and learning", "items": [
    {"t":"open","key":"cpleo","q":"Leo Africanus wrote that in Timbuktu, written books \"are sold for more money than any other merchandize.\" What does this tell historians about Timbuktu, and why should they be careful with this source?","min":25,"rows":3,"pts":4,"rubric":["What the quotation shows about Timbuktu","A reason for caution about the source"],"model":"It shows that learning was so valued in Timbuktu that books were the most profitable goods. Historians should be careful because Leo was a visitor writing years later, and we read him through translations."},
    {"t":"open","key":"cpahmad","q":"Who was Ahmad Baba, and why is he remembered?","min":20,"rows":3,"pts":4,"rubric":["Identifies him as a Timbuktu scholar exiled by Morocco","Explains his argument about race and slavery or his scholarship"],"model":"Ahmad Baba was a famous Timbuktu scholar whom the Moroccans exiled to Marrakesh after 1591. He is remembered for his books and for arguing in 1615 that skin color was no reason for slavery."},
    {"t":"open","key":"cpmanuscripts","q":"Explain how Timbuktu's manuscripts have been protected, from the 1500s to 2013.","min":20,"rows":3,"pts":4,"rubric":["Protection in earlier centuries","The 2012 to 2013 rescue"],"model":"Families kept manuscripts in private libraries, hiding them in chests and even burying them after 1591. In 2012, librarians smuggled more than 350,000 manuscripts to Bamako to save them from armed groups."}]},
   {"title": "Part C: The Indian Ocean world", "items": [
    {"t":"text","q":"What seasonal winds carried ships between East Africa and Arabia and India?","a":[{"all":[["monsoon"]],"none":["not"]}],"show":"the monsoon winds","pts":3,"why":"They reverse about every six months."},
    {"t":"open","key":"cpswahili","q":"Describe Swahili culture, explaining what was African and what came from contact with traders.","min":25,"rows":3,"pts":4,"rubric":["African roots (Bantu language, African people)","Influences from contact (Islam, Arabic words, imported goods)"],"model":"Swahili people were African and spoke a Bantu language, but centuries of trade added Arabic words, Islam as the main religion, and imported goods like Chinese porcelain set into their homes and tombs."},
    {"t":"open","key":"cpzimbabwe","q":"Explain how Great Zimbabwe was connected to the Indian Ocean trade, and what evidence proves it.","min":25,"rows":3,"pts":4,"rubric":["Explains the gold route to the coast","Names archaeological evidence of the connection"],"model":"Great Zimbabwe's rulers controlled gold that was carried to Sofala and Kilwa and shipped across the Indian Ocean. Archaeologists found Chinese porcelain, Persian pottery, Indian glass beads and a coin from Kilwa at the site."}]},
   {"title": "Part D: Myth and evidence", "items": [
    {"t":"open","key":"cpmyth","q":"Explain the colonial myth about who built Great Zimbabwe, why it was spread, and how archaeologists disproved it.","min":35,"rows":4,"pts":5,"rubric":["Describes the myth","Explains the motive","Names evidence or archaeologists who disproved it"],"model":"Colonizers claimed that outsiders such as Phoenicians or the Queen of Sheba built Great Zimbabwe, because admitting Africans built it would undercut their claim to be bringing civilization. Archaeologists David Randall-MacIver in 1905 and Gertrude Caton-Thompson in 1929 showed it was built by the ancestors of the Shona."},
    {"t":"open","key":"cpcompare","q":"Compare the trans-Saharan and Indian Ocean trade networks: give one similarity and two differences.","min":30,"rows":4,"pts":5,"rubric":["One correct similarity","Two correct differences, with specifics"],"model":"Both carried African gold to distant markets and spread Islam. But trans-Saharan trade used camels across a desert while Indian Ocean trade used dhows on monsoon winds, and the Sahara trade exchanged gold for salt while the Indian Ocean trade brought cloth and porcelain from India and China."}]}]},
 "next": "Unit 6: the Americas and the meeting of worlds, starting with the Olmec and the Maya."
}

TEACHER = {
 "standards": [
  "SS.6.G.2.1: Explain how major physical characteristics, natural resources, climate, and absolute and relative locations have influenced settlement, interactions, and the economies of ancient civilizations of the world.",
  "SS.6.G.2.6: Explain the concept of cultural diffusion, and identify the influences of different ancient cultures on one another.",
  "SS.6.E.3.4: Describe the relationship among civilizations that engage in trade, including the benefits and drawbacks of voluntary trade.",
  "SS.6.W.1.3: Interpret primary and secondary sources.",
  "SS.6.W.1.5: Describe the roles of historians and recognize varying historical interpretations (historiography)."],
 "materials": ["The interactive lesson", "The student's trade route game or project", "Index cards, a marker, a die, small items as goods", "The Unit 5 projects page and rubric", "The Unit 5 checkpoint"],
 "flow": [
  [6, "Reconnect", "Run one question from each week of the unit."],
  [4, "Hook", "Two trade networks on one map."],
  [10, "West African empires", "Order the empires; compare their wealth."],
  [10, "East Africa", "Cultural diffusion on both networks."],
  [10, "How we know", "Written sources versus archaeology."],
  [10, "Assign", "Set up the playtest; review the project rubric; assign Think Deeper."],
  [10, "Checkpoint preview", "Explain that the checkpoint is completed after class, independently, one try per item, with no answers shown until you review it. Mastery is 85; below 85 means a review lesson and a retake."]],
 "key_questions": ["How did geography shape this empire or city?", "What moved along this route besides goods?", "Who wrote this source, and what can archaeology add?", "Who benefited from leaving Africa out of history?"],
 "misconceptions": ["Africa was isolated before Europeans arrived.", "Africa had no written history.", "Outsiders built Africa's great monuments.", "The empires existed at the same time (they followed one another)."],
 "support": ["Keep the review map visible during review (not during the checkpoint).", "Provide a timeline card from Ghana to Great Zimbabwe.", "Let the student answer one item aloud before writing."],
 "challenge": ["Compare the trade networks of Unit 5 with the Silk Road.", "Research the Kilwa coins found in northern Australia and what historians think they show."],
 "background": "<p>Checkpoint totals: Part A 14, Part B 12, Part C 11, Part D 10, total 47. Medieval Africa is outside Florida's Grade 6 NGSSS world history range; the standards above cover the skills taught.</p>",
 "sources": ["UNESCO, Timbuktu; Great Zimbabwe National Monument; Ruins of Kilwa Kisiwani.", "Metropolitan Museum of Art, Heilbrunn Timeline of Art History (Ghana, Mali, Songhai, Great Zimbabwe, the Swahili Coast).", "Gomez, Michael A., African Dominion (2018)."]
}

PRINT = {
 "directions": "Answer in complete sentences. This page reviews the whole unit.",
 "items": [
  {"q":"Put in order and describe in one sentence each: Ghana, Mali, Songhai.","a":"Ghana taxed the gold-salt trade; Mali controlled gold and grew under Sundiata and Mansa Musa; Songhai became largest under Askia Muhammad.","lines":4},
  {"q":"Why was Timbuktu important?","a":"A center of trade and Islamic learning with scholars, mosques and manuscripts.","lines":2},
  {"q":"How did the monsoon winds shape Swahili trade?","a":"Ships sailed to Africa November to March and back April to September.","lines":2},
  {"q":"Who built Great Zimbabwe, and how was the colonial myth disproved?","a":"Ancestors of the Shona; archaeologists Randall-MacIver and Caton-Thompson.","lines":3},
  {"q":"Name one written source and one archaeological find from Unit 5.","a":"Ibn Battuta's account; Kilwa's Great Mosque (or Great Zimbabwe's walls).","lines":2}]
}
