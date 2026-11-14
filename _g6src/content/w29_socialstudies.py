EXCHANGE = ('<svg viewBox="0 0 660 280" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="The Columbian Exchange: plants, animals and diseases moving between the Americas and Europe, Africa and Asia after 1492">'
  '<rect width="660" height="280" fill="#cfe3f3"/>'
  '<text x="330" y="22" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The Columbian Exchange after 1492</text>'
  '<rect x="20" y="40" width="190" height="220" rx="12" fill="#f3ead6" stroke="#b9a77a"/><text x="115" y="64" text-anchor="middle" fill="#8a6d1f" font-weight="bold">THE AMERICAS</text>'
  '<rect x="450" y="40" width="190" height="220" rx="12" fill="#f3ead6" stroke="#b9a77a"/><text x="545" y="64" text-anchor="middle" fill="#8a6d1f" font-weight="bold">EUROPE, AFRICA, ASIA</text>'
  + ''.join(f'<text x="115" y="{90+i*18}" text-anchor="middle" fill="#2c6e22" font-size="11">{t}</text>' for i, t in enumerate(["maize (corn)", "potatoes", "tomatoes", "cacao (chocolate)", "peanuts, squash, beans", "chili peppers", "turkeys", "rubber, tobacco"])) +
  ''.join(f'<text x="545" y="{90+i*18}" text-anchor="middle" fill="#0047BA" font-size="11">{t}</text>' for i, t in enumerate(["wheat, rice, sugarcane", "oranges, bananas, coffee", "horses, cattle, pigs", "chickens, sheep, goats", "smallpox, measles, flu", "iron tools, guns", "enslaved Africans", "(forced, not exchanged)"])) +
  '<defs><marker id="ce" viewBox="0 0 10 10" markerWidth="8" markerHeight="8" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="#0A1F3D"/></marker></defs>'
  '<path d="M215 120 C300 90 360 90 445 120" fill="none" stroke="#2c6e22" stroke-width="3" marker-end="url(#ce)"/><text x="330" y="88" text-anchor="middle" fill="#2c6e22" font-weight="bold">to the Eastern Hemisphere</text>'
  '<path d="M445 190 C360 220 300 220 215 190" fill="none" stroke="#0047BA" stroke-width="3" marker-end="url(#ce)"/><text x="330" y="236" text-anchor="middle" fill="#0047BA" font-weight="bold">to the Americas</text>'
  '<text x="330" y="160" text-anchor="middle" fill="#DB2F30" font-weight="bold" font-size="13">Atlantic Ocean</text></svg>')

LESSON = {
 "unit": "Unit 6: The Americas and the Meeting of Worlds",
 "title": "1492, the Taíno and the Columbian Exchange",
 "subtitle": "In October 1492, Christopher Columbus's ships reached an island the Lucayan people called Guanahani. The meeting of two worlds that followed changed what people eat on every continent, spread diseases that killed millions, and began centuries of conquest and slavery. This week you meet the Taíno, read Columbus's own words critically, and trace the Columbian Exchange.",
 "objectives": [
  "Describe the Taíno and their Caribbean societies before 1492.",
  "Analyze Columbus's journal as a primary source, identifying his goals and assumptions.",
  "Explain the causes and catastrophic effects of disease, forced labor and conquest on the Taíno.",
  "Trace the plants, animals, diseases and people that crossed the Atlantic in the Columbian Exchange.",
  "Evaluate the long-term effects of 1492, including the Atlantic slave trade, and recognize Taíno descendants today."],
 "vocab": [
  ["Taíno", "Indigenous Arawakan-speaking peoples of the Greater Antilles and the Bahamas (Lucayans) when Columbus arrived."],
  ["cacique", "A Taíno chief."],
  ["Columbian Exchange", "The transfer of plants, animals, diseases, people and ideas between the Eastern and Western Hemispheres after 1492."],
  ["encomienda", "A Spanish system that granted colonists the labor of Indigenous people, which in practice was a form of forced labor."],
  ["epidemic", "A disease that spreads quickly and affects many people in an area."],
  ["Atlantic slave trade", "The forced transport of millions of Africans across the Atlantic to be enslaved in the Americas."]],
 "reconnect": {
  "title": "Week 28: Indigenous Peoples of Florida",
  "intro": "Florida's nations met Spanish ships soon after 1492. Start with last week.",
  "items": [
   {"t":"text","q":"Last week you learned that Spain tried to convert the Timucua and Apalachee. What kind of religious settlements did Spain build among them?","a":[{"all":[["mission"]],"none":["not"]}],"show":"missions","pts":2,"why":"Spain used the same approach across its American colonies, starting in the Caribbean."},
   {"t":"text","q":"Which Florida nation built a powerful chiefdom without farming?","a":[{"all":[["calusa"]],"none":["not"]}],"show":"the Calusa","pts":2,"why":"Estuaries fed them."},
   {"t":"num","q":"Juan Ponce de León reached Florida in 1513. How many years after 1492 was that?","a":21,"unit":"years","pts":2,"why":"1513 − 1492 = 21."},
   {"t":"open","key":"rc_disease","q":"Last week you learned that European diseases devastated Florida's nations, often before people even met Europeans. How could a disease travel ahead of the people who brought it?","min":15,"rows":2,"rubric":["Explains spread through trade and contact between Native communities"],"model":"Native traders and travelers who met Europeans could carry the disease home and pass it along trade routes to towns that had never seen a European."}]},
 "hook": {
  "title": "Two Worlds Meet",
  "visual": EXCHANGE,
  "html": "<p>On October 12, 1492, the Lucayan people of Guanahani, in today's Bahamas, saw three strange ships. Columbus was searching for a sea route to Asia and believed he had reached the Indies, which is why he called the people \"Indians.\" He wrote about them in his journal. In Clements Markham's 1893 English translation:</p><blockquote>\"They neither carry nor know anything of arms, for I showed them swords, and they took them by the blade and cut themselves through ignorance.\"</blockquote><blockquote>\"They should be good servants and intelligent, for I observed that they quickly took in what was said to them, and I believe that they would easily be made Christians, as it appeared to me that they had no religion.\"</blockquote><p class='small'>Columbus's original journal is lost; this text comes from a summary copied by the priest Bartolomé de las Casas.</p><p>Notice what Columbus noticed, what he assumed and what he planned on his very first day.</p><div class='callout'><b>Big question:</b> How did the meeting of two worlds after 1492 change both, and who paid the price?</div>"},
 "learn": [
  {"title": "The Taíno World",
   "html": "<p>The <b>Taíno</b> lived on the islands now called Cuba, Hispaniola (Haiti and the Dominican Republic), Puerto Rico and Jamaica; the Lucayans of the Bahamas were a Taíno people. Estimates range from about 100,000 to several million people living on Hispaniola alone in 1492.</p><ul><li>Villages were led by <b>caciques</b>, chiefs who could be men or women. Anacaona, a cacique of Hispaniola, was famous as a poet and leader.</li><li>Farmers grew cassava (yuca) and sweet potatoes in raised mounds called <i>conucos</i>, and fished from dugout canoes holding up to 40 or more people.</li><li>Ball courts called <i>bateyes</i> hosted ceremonies and games played with rubber balls.</li><li>The Taíno practiced their own religion, honoring spirits called <i>zemí</i>, carved in stone and wood. Columbus's claim that they \"had no religion\" was wrong.</li><li>Taíno words entered English: hammock, canoe, hurricane, barbecue and probably tobacco.</li></ul>",
   "checks": [
    {"t":"text","q":"What was a Taíno chief called?","a":[{"all":[["cacique"]],"none":["not"]}],"show":"a cacique","pts":2,"why":"Caciques could be men or women."},
    {"t":"open","key":"tainowords","q":"Hurricane, hammock and canoe come from Taíno words. What does this tell historians about how Europeans encountered the Caribbean?","min":20,"rows":2,"rubric":["Europeans learned about new things from the Taíno","Borrowing words shows Taíno knowledge and cultural influence"],"model":"Europeans had no words for hurricanes, hammocks or canoes, so they learned them from the Taíno along with the things themselves. It shows that Europeans depended on Taíno knowledge of the Caribbean."}]},
  {"title": "Reading Columbus Critically",
   "html": "<p>Columbus's journal is a valuable <b>primary source</b>: an eyewitness account from the first day. But reading it critically means asking about its author and purpose:</p><ul><li>Columbus was writing for the king and queen of Spain, who paid for the voyage and wanted gold, land and converts.</li><li>He judged the Taíno by his own culture: no swords and no churches meant \"no arms\" and \"no religion\" to him, but the Taíno had spears and darts and their own beliefs.</li><li>His first thoughts included making them \"servants.\" Within days he seized several Taíno to take to Spain, and by 1495 he was shipping hundreds of enslaved Taíno there.</li></ul><p>Like Leo Africanus in Week 23 and Bernal Díaz in Week 27, Columbus shows both what he saw and what he wanted to see.</p>",
   "checks": [
    {"t":"open","key":"columbuspurpose","q":"Columbus wrote that the Taíno \"should be good servants.\" What does this reveal about his goals, and how does knowing his audience (the Spanish monarchs) help explain it?","min":30,"rows":3,"rubric":["Explains the goal the quotation reveals", "Connects to the audience who funded the voyage"],"model":"It shows that from the first day Columbus thought of the Taíno as people to use for labor, not as equals. He was writing to the Spanish monarchs who paid for his voyage, so he wanted to show that the islands could bring them workers, wealth and converts."},
    {"t":"open","key":"norelgion","q":"Columbus said the Taíno \"had no religion.\" Use evidence from the lesson to explain why he was wrong, and why he might have thought so.","min":25,"rows":3,"rubric":["Evidence of Taíno religion from the lesson", "Explains the assumption behind his claim"],"model":"The Taíno honored spirits called zemí and held ceremonies, so they did have a religion. Columbus had only been there one day and didn't see churches or anything he recognized from Christianity, so he assumed they had none."}]},
  {"title": "Catastrophe for the Taíno",
   "html": "<p>Columbus returned in 1493 with 17 ships and about 1,200 men to build a colony on Hispaniola. What followed was a catastrophe:</p><ul><li><b>Forced labor:</b> under the <b>encomienda</b> system, Spanish colonists were granted the labor of Taíno people, forcing them to mine gold and farm. Many died from overwork, hunger and violence.</li><li><b>Disease:</b> smallpox reached Hispaniola by 1518, along with measles and influenza. The Taíno had no immunity.</li><li><b>Violence and resistance:</b> caciques such as Hatuey, who fled Hispaniola to Cuba to warn others, and Enriquillo, who led a successful 14-year rebellion that won his people a free town, fought back.</li></ul><p>Within about 50 years, the Taíno population of Hispaniola had collapsed by more than 90 percent. The priest <b>Bartolomé de las Casas</b>, who had once held encomienda workers himself, became a fierce critic and wrote about the cruelty he witnessed.</p>",
   "checks": [
    {"t":"open","key":"collapsecauses","q":"Explain how forced labor and disease worked together to cause the collapse of the Taíno population.","min":30,"rows":3,"rubric":["Describes forced labor's effects","Describes disease's effects","Explains how they made each other worse"],"model":"Forced labor in mines and fields left the Taíno exhausted and hungry, and families couldn't farm their own food. When smallpox and measles arrived, weakened people had no immunity and many died. With so many dead, survivors were forced to work even harder, and more died."},
    {"t":"open","key":"resistance","q":"Many textbooks describe the Taíno only as victims. Why is it important to also learn about resisters like Hatuey and Enriquillo?","min":25,"rows":3,"rubric":["Explains that the Taíno acted and fought back","Explains why a complete, truthful history matters"],"model":"Hatuey and Enriquillo show that the Taíno fought for their freedom, and Enriquillo even won a free town. Telling only the story of victims makes them seem helpless, which isn't true, and a complete history respects their courage."}]},
  {"title": "The Columbian Exchange and Its Legacy",
   "html": "<p>Historian Alfred Crosby named the <b>Columbian Exchange</b>: the transfer of living things between hemispheres that had been separated for thousands of years.</p><ul><li>From the Americas: maize, potatoes, tomatoes, cacao, peanuts and chili peppers transformed diets worldwide. Potatoes fed Europe's growing population; chili peppers became central to Indian and Thai cooking.</li><li>To the Americas: wheat, sugarcane, coffee, oranges and bananas, plus horses, cattle and pigs. Horses transformed life for Plains nations such as the Comanche and Lakota. Florida's famous oranges arrived with the Spanish in the 1500s.</li><li>Disease: epidemics killed a large share of the Americas' Indigenous population, possibly most of it.</li><li>Forced migration: as Indigenous laborers died, colonists turned to the <b>Atlantic slave trade</b>, forcing about 12.5 million Africans onto ships to the Americas between the 1500s and 1800s, largely to grow sugar.</li></ul><p>The Taíno did not disappear: Taíno words, foods and traditions survive, many Puerto Ricans, Dominicans and Cubans have Taíno ancestry confirmed by DNA studies, and Taíno communities today are reviving their heritage.</p>",
   "checks": [
    {"t":"open","key":"exchangeboth","q":"Give one example of a positive effect and one example of a devastating effect of the Columbian Exchange, and explain who benefited or suffered in each.","min":27,"rows":3,"rubric":["One positive effect with who benefited","One devastating effect with who suffered"],"model":"Potatoes from the Andes fed millions of people in Europe, helping its population grow. But smallpox brought by Europeans killed huge numbers of Indigenous people in the Americas, who had no immunity."},
    {"t":"open","key":"sugarslavery","q":"Explain the connection between sugarcane, the collapse of Indigenous populations and the Atlantic slave trade.","min":30,"rows":3,"rubric":["Sugarcane plantations needed huge labor","As Indigenous people died, colonists forced enslaved Africans to work"],"model":"Europeans planted sugarcane in the Caribbean, which required brutal, nonstop labor. As forced labor and disease killed most of the Indigenous workers, colonists turned to kidnapping and enslaving millions of Africans, beginning the Atlantic slave trade."}]}],
 "handson": {
  "title": "Columbian Exchange Kitchen Audit",
  "intro": "Find the Columbian Exchange in your own kitchen, then map where your foods came from.",
  "materials": ["Your kitchen pantry and refrigerator (with permission)", "Paper and pencil", "A world map or atlas (printed or online)", "Colored pencils or two colors of sticky dots", "A family member"],
  "steps": [
   "Make a two-column chart: \"From the Americas\" and \"To the Americas.\"",
   "Search your kitchen for at least 15 foods or ingredients. Use the lesson's list (and a parent's help to look up others) to sort each one, including foods made from them (ketchup = tomatoes; bread = wheat; chocolate = cacao).",
   "On a world map, mark where each food was first grown with one color for Americas foods and another for Eastern Hemisphere foods.",
   "Plan a family meal that would have been impossible anywhere in the world before 1492 because it combines foods from both hemispheres (for example, tomato sauce on wheat pasta).",
   "Ask permission before opening packages, and check for food allergies before tasting anything."],
  "record": [
   {"t":"open","key":"kitchenrec","q":"List your foods in the two columns. Which column was longer, and which food surprised you most?","min":40,"rows":4,"rubric":["At least 15 foods sorted correctly","Compares the columns","Names a surprising food with a reason"],"model":"From the Americas: corn flakes, potatoes, tomato sauce, peanut butter, chocolate chips, salsa, vanilla, pumpkin seeds. To the Americas: rice, wheat bread, sugar, coffee, oranges, bananas, milk, eggs, cinnamon. The \"to the Americas\" column was longer, but I was surprised that chocolate and vanilla both came from the Americas."},
   {"t":"open","key":"mealrec","q":"Describe your before-1492-impossible meal and explain which ingredients came from each hemisphere.","min":30,"rows":3,"rubric":["A meal combining both hemispheres","Correctly identifies each ingredient's origin"],"model":"Chicken tacos with salsa and rice: corn tortillas, tomatoes, peppers and avocados came from the Americas, while chicken, rice, onions and lime came from the Eastern Hemisphere. Nobody anywhere could have made this meal before 1492."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"discoverword","q":"In Week 1 you questioned the word \"discovered.\" Some people now say Columbus \"encountered\" or \"invaded\" the Americas instead of \"discovered\" them. Which word do you think is most accurate? Support your choice with evidence from this week.","min":50,"rows":6,"rubric":["Chooses a word and makes a clear claim","At least two pieces of evidence from the lesson","Addresses why the other words are less accurate"],"model":"Encountered is most accurate for October 1492 because millions of people already lived in the Americas, so nothing was discovered; two peoples met. But what followed was an invasion: Columbus came back with 1,200 men, forced the Taíno into labor and took their land. I'd say Columbus encountered the Americas in 1492, and Spain invaded in the years after."},
   {"t":"open","key":"worldchanged","q":"Choose one food from the Columbian Exchange and trace how it changed life in at least two parts of the world. Then explain whether the Columbian Exchange should be remembered mostly for its benefits or its harms.","min":53,"rows":6,"rubric":["Traces one food's effects in two regions","A reasoned judgment about benefits and harms"],"model":"The potato, first grown in the Andes, became a staple in Ireland and across Europe, feeding growing populations, and later spread to China. But I think the Columbian Exchange should be remembered mostly for its harms, because the same contact that spread potatoes also spread smallpox that killed millions and launched the Atlantic slave trade. The benefits came at a terrible human cost."}]},
 "exit": [
  {"t":"text","q":"What were Taíno chiefs called?","a":[{"all":[["cacique"]],"none":["not"]}],"show":"caciques","pts":2,"why":"Including women such as Anacaona."},
  {"t":"text","q":"Name one food that traveled from the Americas to the rest of the world.","a":[{"all":[["maize","corn","potato","tomato","cacao","chocolate","peanut","chili","chile","bell pepper","jalapeno","squash","bean","pumpkin","vanilla","avocado","turkey","cassava"]],"none":["not","black pepper","peppercorn","coffee","soy","fava"]}],"show":"potatoes (also maize, tomatoes, cacao, peanuts, chili peppers)","pts":2,"why":"They transformed diets worldwide."},
  {"t":"open","key":"exit_source","q":"Name one thing a historian should keep in mind when reading Columbus's journal.","min":8,"rows":2,"rubric":["A valid consideration about author, audience, assumptions or the copied text"],"model":"He was writing for the Spanish monarchs who paid for his voyage, so he described the islands in ways that would please them."}],
 "next": "Week 30: end-of-year review, the Atlantic world begins."
}

TEACHER = {
 "standards": [
  "SS.6.W.1.3: Interpret primary and secondary sources.",
  "SS.6.W.1.5: Describe the roles of historians and recognize varying historical interpretations (historiography).",
  "SS.6.G.2.6: Explain the concept of cultural diffusion, and identify the influences of different ancient cultures on one another.",
  "SS.6.E.3.4: Describe the relationship among civilizations that engage in trade, including the benefits and drawbacks of voluntary trade."],
 "materials": ["The interactive lesson", "Kitchen access (with permission), paper and pencil, a world map or atlas, colored pencils or sticky dots", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 28 warm-up questions."],
  [5, "Hook", "Columbus's journal; the exchange diagram."],
  [10, "The Taíno world", "Caciques, conucos, zemí; Taíno words."],
  [11, "Reading Columbus critically", "Purpose, audience, assumptions."],
  [11, "Catastrophe", "Encomienda, disease, resistance; Las Casas."],
  [11, "The Columbian Exchange", "Both directions; sugar and slavery; Taíno descendants."],
  [6, "Assign", "Set up the kitchen audit; assign Think Deeper and the Exit Check."]],
 "key_questions": ["What did Columbus notice, assume and want?", "Who benefited and who suffered from the exchange?", "How did disease and forced labor work together?", "How do Taíno people and cultures continue today?"],
 "misconceptions": ["Columbus discovered an empty land.", "The Taíno had no religion or government.", "The Taíno simply vanished.", "The Columbian Exchange was an equal, voluntary trade."],
 "support": ["Read the journal excerpts aloud together and underline assumptions.", "Provide a two-column exchange chart.", "Pre-teach encomienda and epidemic."],
 "challenge": ["Read a short excerpt from Bartolomé de las Casas and compare his view with Columbus's.", "Research how horses transformed life for the Comanche or Lakota."],
 "background": "<p>Columbus's journal survives only in Las Casas's abstract; the excerpts are from Clements R. Markham's 1893 Hakluyt Society translation (entry for October 11 to 12), checked against the scanned text. Guanahani's location in the Bahamas is debated (San Salvador is the most common identification). Estimates of Hispaniola's 1492 population range from about 100,000 to several million. Smallpox reached Hispaniola by about 1518 to 1519. Enriquillo's rebellion lasted from about 1519 to 1533. The figure of about 12.5 million Africans embarked comes from the Trans-Atlantic Slave Trade Database (SlaveVoyages). Genetic studies (for example, Schroeder and others, 2018, PNAS) find Indigenous Caribbean ancestry in many Puerto Ricans and other Caribbean people today. Florida's Grade 6 NGSSS world history range ends before 1492; the standards above cover the skills taught.</p>",
 "sources": ["Columbus, Christopher, The Journal of Christopher Columbus, trans. Clements R. Markham (Hakluyt Society, 1893).", "Crosby, Alfred W., The Columbian Exchange (1972).", "Smithsonian National Museum of the American Indian, Taíno: Native Heritage and Identity in the Caribbean (2018 exhibition).", "SlaveVoyages, Trans-Atlantic Slave Trade Database."]
}

PRINT = {
 "directions": "Answer in complete sentences.",
 "items": [
  {"q":"Describe three features of Taíno life before 1492.","a":"Caciques led villages; farming cassava in conucos; ball courts; zemí spirits; dugout canoes.","lines":3},
  {"q":"What do Columbus's journal entries reveal about his goals and assumptions?","a":"He wanted servants, converts and gold; he assumed the Taíno had no weapons or religion.","lines":3},
  {"q":"Name two causes of the Taíno population collapse.","a":"Forced labor under the encomienda, European diseases, violence.","lines":2},
  {"q":"Give two items that traveled each way in the Columbian Exchange.","a":"To the Eastern Hemisphere: potatoes, maize; to the Americas: horses, wheat (and diseases).","lines":2},
  {"q":"How did the Columbian Exchange lead to the Atlantic slave trade?","a":"Sugar plantations needed labor; as Indigenous workers died, colonists enslaved millions of Africans.","lines":2}]
}
