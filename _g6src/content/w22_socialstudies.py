MALI = ('<svg viewBox="0 0 680 320" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Map of the Mali Empire around 1330 and Mansa Musa&apos;s route to Mecca through Cairo">'
  '<rect width="680" height="320" fill="#eaf2fb"/>'
  '<text x="340" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The Mali Empire and Mansa Musa\'s journey, 1324 to 1325</text>'
  '<path d="M20 40 L600 40 L640 110 L620 180 L600 300 L20 300Z" fill="#f4ecd8" stroke="#b9a77a"/>'
  '<path d="M612 40 L680 40 L680 240 L642 178 L648 118Z" fill="#f4ecd8" stroke="#b9a77a"/><text x="635" y="80" font-size="10" fill="#5b6676">Arabia</text>'
  '<path d="M600 60 L640 120 L630 170" fill="none" stroke="#9fc6e8" stroke-width="8"/><text x="582" y="190" font-size="9" fill="#0047BA">Red Sea</text>'
  '<rect x="20" y="40" width="580" height="120" fill="#f1d9a0" opacity="0.6"/><text x="300" y="80" font-size="14" fill="#8a6d1f" font-weight="bold">SAHARA</text>'
  '<path d="M30 200 Q90 175 140 190 Q200 215 260 215 Q320 210 360 200 Q400 190 430 175" fill="#C9A84C" fill-opacity="0.45" stroke="#8a6d1f" stroke-width="2"/>'
  '<path d="M30 200 Q40 250 80 260 Q160 270 240 255 Q320 245 380 230 Q420 210 430 175" fill="#C9A84C" fill-opacity="0.45" stroke="none"/><text x="236" y="262" font-weight="bold" fill="#0A1F3D" font-size="13">MALI EMPIRE</text>'
  '<path d="M90 230 Q160 210 220 205 Q280 200 320 215 Q350 230 380 260" fill="none" stroke="#0047BA" stroke-width="3"/><text x="320" y="270" font-size="10" fill="#0047BA">Niger River</text>'
  + ''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="{c}"/><text x="{x+tx}" y="{y+ty}" font-weight="bold" fill="{c}">{n}</text>' for x, y, n, tx, ty, c in [
    (120, 245, "Niani", -40, 16, "#0A1F3D"), (240, 200, "Timbuktu", -20, -10, "#DB2F30"), (200, 225, "Djenné", -30, 18, "#0A1F3D"), (320, 210, "Gao", 6, -6, "#0A1F3D"), (560, 95, "Cairo", -40, -8, "#0A1F3D"), (662, 145, "Mecca", -14, 20, "#0A1F3D")]) +
  '<path d="M120 245 Q260 200 360 150 Q470 100 560 95 Q610 105 662 145" fill="none" stroke="#DB2F30" stroke-width="3" stroke-dasharray="8 4"/>'
  '<text x="400" y="128" font-size="11" fill="#DB2F30" font-weight="bold">Mansa Musa\'s hajj</text>'
  '<text x="20" y="314" font-size="9" fill="#5b6676">Schematic map, not to scale; empire borders approximate and changed over time.</text></svg>')

LESSON = {
 "unit": "Unit 5: Empires and Global Trade",
 "title": "Mali and Mansa Musa",
 "subtitle": "After Ghana, a new West African empire rose: Mali, founded by the hero Sundiata and made famous by Mansa Musa, whose journey to Mecca in 1324 put Mali on the maps of Europe. This week you compare how we know about Mali, through the voices of griots and the writings of travelers.",
 "objectives": [
  "Explain how Sundiata Keita founded the Mali Empire and how the epic of Sundiata is preserved by griots.",
  "Describe how Mali grew rich and powerful through gold, salt and trade, and how it was governed.",
  "Explain the causes and effects of Mansa Musa's hajj to Mecca.",
  "Explain how Mali's rulers supported Islam and learning.",
  "Compare oral tradition and written accounts as historical sources."],
 "vocab": [
  ["mansa", "The title of the emperor of Mali, meaning king or emperor."],
  ["griot", "A West African oral historian, storyteller and musician who preserves a people's history."],
  ["oral tradition", "History, stories and knowledge passed down by speaking and memory."],
  ["hajj", "The pilgrimage to Mecca that Muslims who are able are expected to make at least once in their lives."],
  ["pilgrimage", "A journey to a sacred place for religious reasons."],
  ["inflation", "A general rise in prices, often caused when a currency or money becomes less scarce."],
  ["epic", "A long story about a hero's deeds, important to a people's history."]],
 "reconnect": {
  "title": "Week 21: Ghana and the trans-Saharan trade",
  "intro": "Mali rose in the same lands, on the same trade.",
  "items": [
   {"t":"text","q":"What two goods were the heart of the trans-Saharan trade?","a":[{"all":[["gold"],["salt"]],"none":["not"]}],"show":"gold and salt","pts":2,"why":"Gold north, salt south."},
   {"t":"text","q":"What did the Soninke people call the kingdom of Ghana?","a":[{"all":[["wagadu"]],"none":["not"]}],"show":"Wagadu","pts":2,"why":"Week 21."},
   {"t":"text","q":"Why did Ghana's king keep all gold nuggets? Finish: to keep gold ___.","a":[{"all":[["scarce","rare","valuable","value high","price high"]],"none":["not"]}],"show":"scarce (and valuable)","pts":2,"why":"Today: what happened when a lot of gold arrived at once."},
   {"t":"open","key":"rc_bakri","q":"Al-Bakri never visited Ghana. What other kinds of sources could historians use to learn about West African kingdoms?","min":12,"rows":2,"rubric":["Archaeology, oral traditions (griots), travelers who did visit, maps, objects"],"model":"Historians can use archaeology at places like Koumbi Saleh, the oral histories kept by griots, and accounts by travelers who actually visited."}]},
 "hook": {
  "title": "The King Who Changed Cairo's Prices",
  "visual": MALI,
  "html": "<p>In 1324, Mansa Musa, emperor of Mali, set out on the hajj, the pilgrimage to Mecca. Reports say thousands of people traveled with him, and that he carried enormous amounts of gold. When he stopped in Cairo, Egypt, he and his followers spent and gave away so much gold that, according to the Arab historian al-Umari, the value of gold in Cairo fell and had still not recovered twelve years later.</p><p>About fifty years later, in 1375, a mapmaker on the Mediterranean island of Majorca drew Mansa Musa on the Catalan Atlas, seated on a throne, wearing a crown and holding a large gold nugget. Mali had become famous across three continents.</p><div class='callout'><b>Big question:</b> How did Mali become one of the richest and most respected empires in the world, and how do we know?</div>"},
 "learn": [
  {"title": "Sundiata and the Griots",
   "html": "<p>After Ghana weakened, the Sosso king <b>Sumanguru</b> (Soumaoro Kanté) conquered much of the region. According to the <b>Epic of Sundiata</b>, a prince of the Mandinka (Maninka) people named <b>Sundiata Keita</b> overcame great hardship: as a child he could not walk, and he was mocked and exiled. He grew strong, gathered allies and defeated Sumanguru at the <b>Battle of Kirina</b>, around 1235. He became the first mansa of Mali.</p><p>We know Sundiata's story mainly through <b>griots</b> (in Mande languages, jeli), hereditary oral historians who memorize and perform the history of families and kingdoms, often with music on the kora or balafon. Both men and women are griots; women griots (jelimusow) are celebrated singers of history. Griot families have passed down the epic for nearly 800 years. According to tradition, Sundiata proclaimed the <b>Manden Charter</b> (Kouroukan Fouga), an oral constitution that includes principles about the value of human life, and which UNESCO recognized as part of humanity's cultural heritage in 2009. Historians debate how much of today's text dates to the 1200s.</p>",
   "checks": [
    {"t":"text","q":"Who founded the Mali Empire after the Battle of Kirina?","a":[{"all":[["sundiata","sunjata","soundiata"]],"none":["not"]}],"show":"Sundiata Keita","pts":2,"why":"Around 1235."},
    {"t":"open","key":"griotvalue","q":"Griot families served royal families. How might that shape the way the epic portrays Sundiata and Sumanguru, and how could a historian check it?","min":30,"rows":3,"rubric":["Explains how serving a royal family could shape the story (hero made greater, enemy made worse)","A way to check (other griot versions, Arabic written sources, archaeology)"],"model":"Griots who served the Keita family had reasons to make Sundiata a great hero and Sumanguru a cruel sorcerer-king. A historian could compare versions from different griot families, check Arabic writers like Ibn Khaldun, and look at archaeology from the period."}]},
  {"title": "How Mali Grew Rich and Was Governed",
   "html": "<p>Mali was larger than Ghana, stretching from the Atlantic coast deep into the interior along the Niger River. Unlike Ghana, Mali controlled the <b>gold fields</b> themselves (Bambuk and Bure) as well as the trade routes, and it taxed salt, copper and other goods. Fertile land along the Niger grew rice, millet and sorghum, and the river carried boats of goods between cities like <b>Djenné</b>, <b>Timbuktu</b> and <b>Gao</b>.</p><p>The mansa ruled with governors over provinces and a strong army, and many local rulers kept power if they paid tribute and stayed loyal. Many mansas and merchants were Muslims, and Islam spread through trade, while many farmers and villagers kept traditional beliefs; rulers often respected both.</p>",
   "checks": [
    {"t":"open","key":"maliVsGhana","q":"Give one way Mali was similar to Ghana and one way it was different.","min":25,"rows":3,"rubric":["Similar: grew rich from the gold-salt trade, taxes, tribute; based in the Sahel near the Niger","Different: Mali controlled the gold fields themselves, was larger, and had stronger ties to Islam and Islamic learning"],"model":"Like Ghana, Mali grew rich from the gold and salt trade and from taxing traders. But Mali was much larger and controlled the gold fields themselves, not just the trade routes."},
    {"t":"text","q":"Which river was Mali's main highway for boats and trade?","a":[{"all":[["niger"]],"none":["not"]}],"show":"the Niger River","pts":2,"why":"It linked Djenné, Timbuktu and Gao."}]},
  {"title": "Mansa Musa's Hajj",
   "html": "<p><b>Mansa Musa</b> ruled from about 1312 to 1337. As a devout Muslim, he made the hajj in 1324 to 1325. Arabic sources describe a huge caravan, often said to include thousands of people and camels loaded with gold; the exact numbers are uncertain and may be exaggerated.</p><p><b>Effects of the hajj:</b></p><ul><li><b>Fame:</b> Mali appeared on European and North African maps; merchants and scholars across the Mediterranean heard of its wealth.</li><li><b>Inflation in Cairo:</b> so much gold flooded the city that its value fell, so prices measured in gold rose.</li><li><b>Learning and architecture:</b> Musa brought back scholars, including the Andalusian poet and scholar <b>Abu Ishaq al-Sahili</b>, whom tradition credits with designing the <b>Djinguereber Mosque</b> in Timbuktu, made of mud brick and still standing today, rebuilt and repaired many times.</li><li><b>Trade connections:</b> stronger ties between Mali and the Islamic world.</li></ul>",
   "checks": [
    {"t":"text","q":"In what year did Mansa Musa begin his hajj?","a":["1324"],"show":"1324","pts":2,"why":"He reached Cairo that year."},
    {"t":"open","key":"inflationwhy","q":"Explain, using what you learned about Ghana's nugget rule, why Mansa Musa's gold made the value of gold fall in Cairo.","min":30,"rows":3,"rubric":["Gold's value depends on scarcity","Flooding Cairo with gold made it much less scarce, so each piece was worth less (prices rose)","Connects to Ghana keeping gold scarce"],"model":"Ghana's kings kept gold scarce so it stayed valuable. Mansa Musa did the opposite in Cairo: he spent and gave away so much gold that it was no longer scarce there, so each piece of gold was worth less and prices went up."},
    {"t":"num","q":"Mansa Musa ruled from about 1312 to 1337. About how many years did he rule?","a":25,"tol":1,"unit":"years","pts":2,"why":"1337 − 1312 = 25."}]},
  {"title": "Ibn Battuta's Visit",
   "html": "<p>Under Mali, <b>Timbuktu</b> grew as a trading city on the Niger, and Mansa Musa's Djinguereber Mosque made it a place of prayer and study. Next week you will see how it became one of the world's great centers of learning under Songhai.</p><p>In 1352 to 1353, the Moroccan traveler <b>Ibn Battuta</b> visited Mali during the reign of Mansa Sulayman, Musa's brother. He praised the people's justice and the safety of travel. In H. A. R. Gibb's 1929 English translation:</p><blockquote>\"They are seldom unjust, and have a greater abhorrence of injustice than any other people. Their sultan shows no mercy to anyone who is guilty of the least act of it. There is complete security in their country. Neither traveller nor inhabitant in it has anything to fear from robbers or men of violence.\"</blockquote><p class='small'><i>abhorrence</i> = strong hatred; <i>traveller</i> = British spelling of traveler; <i>sultan</i> = ruler (here, Mansa Sulayman).</p><p>He also praised their faithfulness to prayer. He also criticized some customs that differed from those in his homeland, such as how women dressed and mixed freely in public. His account shows both what impressed an outsider and the judgments he brought with him.</p>",
   "checks": [
    {"t":"text","q":"Which Moroccan traveler visited Mali in 1352 to 1353?","a":[{"all":[["battuta"]],"none":["not"]}],"show":"Ibn Battuta","pts":2,"why":"He visited during Mansa Sulayman's reign."},
    {"t":"open","key":"battutaquote","q":"Reread the excerpt. Name two things Ibn Battuta says made Mali safe and just, and explain why a traveler's safety mattered so much to a trading empire.","min":30,"rows":3,"rubric":["Two details from the excerpt (people seldom unjust and hate injustice; the ruler punishes any injustice; no fear of robbers or violent men)","Connects safe roads to merchants, caravans and trade wealth"],"model":"He says the people hate injustice and the ruler punishes even small acts of it, so no one has to fear robbers. Safety mattered because merchants with gold and salt would only travel and trade where their goods and lives were safe, and that trade made Mali rich."},
    {"t":"open","key":"battutabias","q":"Ibn Battuta praised Mali's safety and justice but criticized some customs. What does this tell you about using his account as a source?","min":30,"rows":3,"rubric":["He saw Mali firsthand, so his praise is valuable evidence","His criticism reflects his own culture's expectations (bias), so historians separate what he observed from his judgments"],"model":"Because he actually traveled there, his praise of Mali's safety and justice is strong evidence. But his criticism shows he judged Mali by the customs of his own homeland, so historians have to separate what he saw from his opinions about it."}]}],
 "handson": {
  "title": "Be a Griot and the Gold Flood Market",
  "intro": "Preserve your own family's history the way griots do, then simulate what happened to prices in Cairo.",
  "materials": ["A family elder or any trusted adult (parent, family friend, neighbor, co-op mentor), in person or by phone, or your Week 1 interview notes", "Paper and pencil", "A phone or tablet to record (optional)", "A simple drum, pot and spoon, or table to tap a rhythm (optional)", "About 40 pennies (13 per buyer) or yellow paper squares for gold", "About 10 small household items to be \"market goods\""],
  "steps": [
   "In Week 1 you interviewed a family member. Without looking at your notes, retell one story from that interview as a griot would, 2 to 3 minutes long, with a repeating line or a rhythm you tap. (If you are new or can't find your notes, interview any trusted adult now: Where did you grow up? What is one challenge you are proud of getting through? What lesson do you want to pass on? The person can choose any story they want to share and may skip any question.)",
   "Perform the story without reading it. If you can, perform it for the person who told it to you and ask what you got right and what changed.",
   "Compare your retelling with your Week 1 notes: what stayed, what changed, what grew?",
   "Gold flood market: one person sells 10 goods. The buyers start with 3 gold each and bid. Record the price of each item. Then \"Mansa Musa arrives\" and gives every buyer 10 more gold. Put the same 10 goods up for sale again and record the new prices. Keep pennies and small items away from young children and pets.",
   "Compare the prices before and after."],
  "record": [
   {"t":"open","key":"griotrec","q":"Summarize the story you retold. What changed between your Week 1 notes and your retelling, and what does that show about how oral tradition can stay true, or change, over 800 years?","min":50,"rows":5,"rubric":["A summary of the family story","Honest reflection on what changed in retelling","Connects to the strengths and limits of oral tradition"],"model":"My grandmother grew up on a farm in Georgia and moved to Jacksonville at 17 to work in a shipyard during the war; her lesson was \"education is the one thing no one can take from you.\" When I told it from memory, I mixed up the year she moved and said Savannah instead of Jacksonville. It showed me that oral history keeps the meaning and lessons strong, but details can change, which is why griots train for years and historians compare their stories with other evidence."},
   {"t":"open","key":"marketrec","q":"Record the prices before and after the gold arrived. What happened, and how does this model what happened in Cairo in 1324?","min":30,"rows":4,"rubric":["Prices recorded","Prices rose after more gold arrived","Explains: more gold chasing the same goods made gold worth less (inflation), like Cairo"],"model":"Before: items sold for 1 to 3 gold. After Mansa Musa gave everyone 10 more gold, the same kinds of items sold for 6 to 9 gold. With more gold but the same number of goods, each piece of gold bought less, just like in Cairo when Mansa Musa's gold made prices rise."}]},
 "think": {
  "intro": "Use evidence. Your teacher scores these.",
  "items": [
   {"t":"open","key":"musalegacy","q":"Was Mansa Musa's hajj good for Mali? Weigh at least two positive effects and one possible negative effect, and give your judgment.","min":76,"rows":6,"rubric":["Two positive effects (fame, trade ties, scholars and architects, mosques and learning in Timbuktu)","One possible negative (spending vast wealth; attracting attention from outsiders, including Europeans seeking African gold; inflation hurt Cairo)","A supported judgment"],"model":"The hajj helped Mali in many ways: it made Mali famous across Africa, Asia and Europe, strengthened trade with the Islamic world, and brought scholars and the architect al-Sahili, who helped build mosques and make Timbuktu a center of learning. But it cost an enormous amount of gold, and the fame drew the attention of outsiders, including European explorers who later sailed down Africa's coast looking for the source of that gold. Overall, I think it was good for Mali, because the learning and connections it brought lasted for centuries."},
   {"t":"open","key":"oralwritten","q":"Compare the griots' Epic of Sundiata with Ibn Battuta's written account as sources. What can each tell historians that the other cannot?","min":64,"rows":6,"rubric":["Griots: Mande people's own view of their history, values, heroes, genealogies; but legend and changes over time","Ibn Battuta: a dated, eyewitness description of daily life and government in 1352 to 1353; but an outsider's judgments","A thoughtful comparison"],"model":"The Epic of Sundiata tells us how the Mande people themselves remember their founding, their heroes and their values, which no outsider could provide, though it mixes history and legend and has changed over 800 years. Ibn Battuta gives a dated eyewitness description of daily life, safety and government in 1352 to 1353, details the epic doesn't include, but he judged Mali by his own customs. Together they give a much fuller picture than either alone."}]},
 "exit": [
  {"t":"text","q":"What is a West African oral historian and storyteller called?","a":[{"all":[["griot","jeli","jali"]],"none":["not"]}],"show":"a griot (jeli)","pts":2,"why":"They preserved the Epic of Sundiata."},
  {"t":"text","q":"What title did Mali's emperors hold?","a":[{"all":[["mansa"]],"none":["not"]}],"show":"mansa","pts":2,"why":"Mansa Musa is the most famous."},
  {"t":"open","key":"exit_gold","q":"What happened to the value of gold in Cairo after Mansa Musa's visit, and why?","min":8,"rows":2,"rubric":["Gold lost value","Because so much arrived that it was no longer scarce"],"model":"It fell, because so much gold arrived that it was no longer scarce."},
  {"t":"open","key":"exit_hajj","q":"Name one lasting effect of Mansa Musa's hajj.","min":10,"rows":2,"rubric":["A valid effect (fame on maps, scholars and architects, Djinguereber Mosque, Timbuktu learning, trade ties)"],"model":"He brought back scholars and an architect who helped build the Djinguereber Mosque in Timbuktu, which still stands."}],
 "next": "Week 23: Songhai, Timbuktu and centers of learning."
}

TEACHER = {
 "standards": [
  "SS.6.G.2.1: Explain how major physical characteristics, natural resources, climate, and absolute and relative locations have influenced settlement, interactions, and the economies of ancient civilizations of the world.",
  "SS.6.E.3.4: Describe the relationship among civilizations that engage in trade, including the benefits and drawbacks of voluntary trade.",
  "SS.6.W.1.3: Interpret primary and secondary sources.",
  "SS.6.W.1.5: Describe the roles of historians and recognize varying historical interpretations (historiography).",
  "SS.6.W.1.6: Describe how history transmits culture and heritage and provides models of human character."],
 "materials": ["The interactive lesson", "Week 1 interview notes or a trusted adult to interview, paper and pencil, optional recorder and drum", "About 40 pennies or yellow paper squares, about 10 household items", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 21 warm-up questions."],
  [5, "Hook", "Gold in Cairo and the Catalan Atlas."],
  [11, "Sundiata and the griots", "The epic, the Battle of Kirina, the Manden Charter; oral tradition."],
  [9, "Mali's wealth and government", "Gold fields, the Niger, governors and tribute; Islam and traditional beliefs."],
  [11, "Mansa Musa's hajj", "Causes and effects; inflation; al-Sahili and the Djinguereber Mosque."],
  [11, "Ibn Battuta", "Read the Gibb excerpt; an outsider's praise and judgments."],
  [7, "Assign", "Plan the elder interview; assign the gold flood market, Think Deeper and the Exit Check."]],
 "key_questions": ["How do we know what we know about Mali?", "What made Mali richer than Ghana?", "Why did gold lose value in Cairo?", "What does an outsider's account reveal, and what does it hide?"],
 "misconceptions": ["Africa had no written history (Arabic-script manuscripts were written and collected in Mali's cities; Week 23 explores Timbuktu's libraries).", "Oral history is just made-up stories.", "Mansa Musa was the first ruler of Mali.", "All of Mali's people were Muslim."],
 "support": ["Use a Ghana-and-Mali comparison chart.", "Listen to a griot performance with kora music (with a parent).", "Pre-teach mansa, griot and hajj."],
 "challenge": ["Read a young readers' version of the Epic of Sundiata and compare it with this lesson.", "Compare Ibn Battuta's praise of Mali's justice with the Manden Charter's principles."],
 "background": "<p>Dates: the Battle of Kirina is traditionally dated about 1235; Mansa Musa's reign is usually given as about 1312 to 1337; his hajj began in 1324, and al-Umari, writing in Cairo about twelve years later, reported that the value of gold there had not recovered. Caravan figures (often 60,000 people, 12,000 enslaved servants, 80 to 100 camel loads of gold) come from later Arabic writers and should be treated as uncertain. The Catalan Atlas (1375) is attributed to Abraham Cresques of Majorca. Ibn Battuta visited Mali in 1352 to 1353; the excerpt is from H. A. R. Gibb, Ibn Battuta: Travels in Asia and Africa 1325-1354 (Broadway Travellers, 1929), checked against the scanned text; the sentence just before it uses a term for Black Africans common in 1929 and is omitted. The architect role of al-Sahili is traditional and debated. The Manden Charter was inscribed on UNESCO's Representative List of the Intangible Cultural Heritage of Humanity in 2009. Medieval West Africa is outside Florida's Grade 6 NGSSS world history range; the standards above cover the skills taught.</p>",
 "sources": ["UNESCO, Manden Charter, proclaimed in Kurukan Fuga; Timbuktu World Heritage site.", "Metropolitan Museum of Art, Heilbrunn Timeline: The Empire of Mali.", "Conrad, David C., Sunjata: A New Prose Version (2016).", "Gomez, Michael A., African Dominion: A New History of Empire in Early and Medieval West Africa (2018)."]
}

PRINT = {
 "directions": "Answer in complete sentences.",
 "items": [
  {"q":"Who was Sundiata Keita, and how do we know his story?","a":"Founder of Mali after defeating Sumanguru at Kirina about 1235; his story is preserved by griots in the Epic of Sundiata.","lines":3},
  {"q":"How was Mali's wealth different from Ghana's?","a":"Mali controlled the gold fields themselves as well as the trade routes, and was larger.","lines":2},
  {"q":"List three effects of Mansa Musa's hajj.","a":"Fame on maps; inflation in Cairo; scholars such as al-Sahili; the Djinguereber Mosque in Timbuktu; stronger trade ties.","lines":3},
  {"q":"Why did gold lose value in Cairo?","a":"So much gold arrived at once that it was no longer scarce.","lines":2},
  {"q":"What made Timbuktu important?","a":"A center of trade and Islamic learning with scholars, mosques and many manuscripts.","lines":2},
  {"q":"Compare oral tradition and written accounts as sources.","a":"Oral: insiders' memory and values, may change; written: dated and detailed, but may reflect the writer's bias.","lines":3}]
}
