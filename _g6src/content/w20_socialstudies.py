TL = ('<svg viewBox="0 0 680 200" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Timeline of the Mediterranean world from 814 BCE to 193 CE">'
  '<text x="340" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The Mediterranean world, 814 BCE to 193 CE</text>'
  '<line x1="30" y1="100" x2="650" y2="100" stroke="#0A1F3D" stroke-width="3"/>'
  + ''.join(f'<line x1="{x}" y1="92" x2="{x}" y2="108" stroke="#0A1F3D" stroke-width="2"/><text x="{x}" y="{y}" text-anchor="middle" font-size="10" fill="{c}" font-weight="bold">{d}</text><text x="{x}" y="{y+13}" text-anchor="middle" font-size="10" fill="{c}">{e}</text>'
            for x, y, d, e, c in [
              (30 + (814-814)*0.6, 70, "814 BCE", "Carthage founded", "#0A1F3D"),
              (30 + (814-550)*0.6, 130, "550 BCE", "Persian Empire", "#8a6d1f"),
              (30 + (814-509)*0.6, 70, "509 BCE", "Roman Republic", "#DB2F30"),
              (30 + (814-490)*0.6, 40, "490 BCE", "Marathon", "#0047BA"),
              (30 + (814-218)*0.6, 70, "218 BCE", "Second Punic War", "#0A1F3D"),
              (30 + (814-146)*0.6, 130, "146 BCE", "Carthage destroyed", "#0A1F3D"),
              (30 + (814-27)*0.6, 70, "27 BCE", "Augustus", "#DB2F30"),
              (30 + (814+193)*0.6, 130, "193 CE", "an African-born emperor", "#2c6e22")]) +
  '<text x="340" y="190" text-anchor="middle" font-size="9" fill="#5b6676">Drawn to scale: each 100 years is 60 pixels.</text></svg>')

LESSON = {
 "unit": "Unit 4: The Mediterranean World",
 "title": "Unit 4 Checkpoint and Mediterranean Project",
 "subtitle": "Persia, Greece, Rome and Carthage shared one sea and constantly shaped one another through trade, war and ideas. This week you connect the four civilizations, finish your Mediterranean project and show your mastery on the Unit 4 checkpoint.",
 "objectives": [
  "Compare how Persia, Athens, Sparta, Rome and Carthage were governed.",
  "Explain the causes and effects of the Persian Wars and the Punic Wars.",
  "Trace cultural diffusion around the Mediterranean, including ideas from Africa and Asia.",
  "Analyze primary sources by asking who wrote them, when and why.",
  "Demonstrate mastery of Unit 4 on the checkpoint (85 or higher)."],
 "vocab": [
  ["empire", "Many lands and peoples ruled by one government."],
  ["republic", "A government in which citizens elect leaders."],
  ["democracy", "Government by the people."],
  ["cultural diffusion", "The spread of ideas, goods and customs between cultures."],
  ["primary source", "A source created at the time or by people who were there."],
  ["bias", "A one-sided point of view."]],
 "reconnect": {
  "title": "Unit 4, one question from each week",
  "intro": "Warm up with one question from each week of the unit.",
  "items": [
   {"t":"text","q":"Week 16: What was the title of a Persian provincial governor?","a":[{"all":[["satrap"]],"none":["not"]}],"show":"satrap","pts":2,"why":"Under Darius."},
   {"t":"text","q":"Week 17: Which Athenian leader's Funeral Oration praised democracy?","a":[{"all":[["pericles"]],"none":["not"]}],"show":"Pericles","pts":2,"why":"Recorded by Thucydides."},
   {"t":"text","q":"Week 18: What were Rome's first written laws, displayed in the Forum, called?","a":[{"all":[["twelve tables","12 tables"]],"none":["not"]}],"show":"the Twelve Tables","pts":2,"why":"About 450 BCE."},
   {"t":"text","q":"Week 19: Which Numidian king helped Rome win at Zama?","a":[{"all":[["masinissa","massinissa"]],"none":["not"]}],"show":"Masinissa","pts":2,"why":"202 BCE."}]},
 "hook": {
  "title": "One Sea, Many Peoples",
  "visual": TL,
  "html": "<p>Romans called the Mediterranean <i>Mare Nostrum</i>, \"Our Sea.\" But for more than a thousand years before Rome ruled all its shores, the sea was shared by Phoenicians, Carthaginians, Egyptians, Amazigh (Berber) peoples such as the Numidians, Greeks, Persians and many other peoples. Ships carried grain, olive oil, purple dye and silver, and also alphabets, gods, laws and ideas about government.</p><p>This week you connect Persia, Greece, Rome and Carthage into one story.</p><div class='callout'><b>Big question:</b> How did the civilizations of the Mediterranean shape one another, and us?</div>"},
 "learn": [
  {"title": "Review: Four Ways to Govern",
   "html": "<ul><li><b>Persia:</b> an empire ruled by a Great King through satraps, with roads, coins, a shared official language and tolerance for local customs.</li><li><b>Athens:</b> a direct democracy for adult citizen men, with an Assembly, lotteries and juries; women, enslaved people and foreigners excluded.</li><li><b>Sparta:</b> two kings, a council of elders and a citizen assembly; a military society built on the labor of enslaved helots.</li><li><b>Rome:</b> a republic of consuls, Senate, assemblies and tribunes that became an empire under Augustus.</li><li><b>Carthage:</b> a trading republic in North Africa, led by elected officials and a council of elders, with a powerful navy.</li></ul>",
   "checks": [
    {"t":"blanks","q":"Name the government.","sent":"Citizens vote directly on laws: ___ &nbsp; Citizens elect leaders such as consuls: ___ &nbsp; A Great King rules many peoples through satraps: ___","blanks":[[{"all":[["democracy","direct"]],"none":["not"]}],[{"all":[["republic"]],"none":["not"]}],[{"all":[["empire"]],"none":["not"]}]],"show":"direct democracy (Athens); republic (Rome); empire (Persia)","pts":3,"why":"Unit 4 governments."},
    {"t":"open","key":"revexclude","q":"Compare who was left out of power in Sparta and Carthage, then explain which exclusion you think most weakened its society.","min":25,"rows":3,"rubric":["Sparta: helots (enslaved), women, foreigners excluded","Carthage: power held mainly by wealthy families; women and enslaved people excluded","A reasoned judgment"],"model":"In Sparta, the enslaved helots, who outnumbered citizens, had no rights, and women could not vote. In Carthage, power was held mostly by wealthy families through elected officials and a council, and women and enslaved people had no voice. I think Sparta's exclusion weakened it most, because fear of a helot revolt forced every citizen to live as a soldier."}]},
  {"title": "Review: Wars and Their Effects",
   "html": "<p>The <b>Persian Wars</b> (499 to 479 BCE) began when Greek cities in Ionia revolted and Athens helped them; Greek victories at Marathon, Salamis and Plataea kept Greece independent and made Athens a sea power. The <b>Punic Wars</b> (264 to 146 BCE) between Rome and Carthage ended with Carthage destroyed, Rome master of the western Mediterranean, and Roman wealth and inequality growing, which helped turn the Republic into an empire.</p>",
   "checks": [
    {"t":"open","key":"revwars","q":"Compare one effect of the Persian Wars with one effect of the Punic Wars.","min":25,"rows":3,"rubric":["A correct effect of each war","A comparison (both made a winner the leading sea power; both changed the balance of power)"],"model":"The Persian Wars kept Greece independent and made Athens a powerful sea power. The Punic Wars made Rome the strongest power in the western Mediterranean. In both, the winner became the leading naval power in its region."}]},
  {"title": "Review: Ideas That Traveled",
   "html": "<p>Ideas moved around the sea. The alphabet traveled from Egypt to the Phoenicians, Greeks and Romans. Greeks credited Egypt with the 365-day calendar and studied in Egypt; later, Alexandria in Egypt became the center of Hellenistic learning. Persian roads and messengers inspired admiration from Greek writers. Rome borrowed Greek gods, architecture and ideas about citizenship, and North Africans like Terence, Septimius Severus and Augustine shaped Roman culture. The United States later borrowed the Senate, the veto and the idea of a republic.</p>",
   "checks": [
    {"t":"open","key":"revdiffuse","q":"Trace one idea or invention as it traveled between at least three Unit 4 civilizations.","min":30,"rows":3,"rubric":["An accurate idea (alphabet, calendar, republic, roads)","At least three civilizations in correct order"],"model":"The alphabet began with Semitic-speaking workers in Egypt adapting hieroglyphs. The Phoenicians, including the people of Carthage, carried it around the Mediterranean, the Greeks added vowels, and the Romans adapted it into the Latin alphabet we use today."}]}],
 "handson": {
  "title": "Mediterranean Market Day",
  "intro": "Recreate a Mediterranean trading port at home, then turn it into the presentation for your Mediterranean project.",
  "materials": ["Index cards or paper slips", "Markers or colored pencils", "Small household items to stand for trade goods (a spoon of rice for grain, a small bottle for olive oil, a purple cloth for dye, a coin for silver)", "A world map, atlas or globe", "Family members (2 or more)", "Your notes from Weeks 16 to 19"],
  "steps": [
   "Each person chooses a civilization (Persia, Athens, Rome or Carthage) and makes a \"trader card\": three goods it could offer, one thing it needed, and one idea it could share.",
   "Set up a market on a table. Trade goods and ideas: each trade must include one good and one idea (for example, Carthaginian purple dye and the alphabet for Athenian olive oil and the idea of a jury).",
   "Track every trade on the map with a line between the two places.",
   "Afterward, list which ideas spread farthest and why.",
   "Keep small items away from young children and pets, and don't eat any food items used as trade goods."],
  "record": [
   {"t":"open","key":"marketrec","q":"List three trades you made (goods and ideas), and explain which idea you think spread farthest in real history and why.","min":40,"rows":5,"rubric":["Three trades with goods and ideas, historically reasonable","A real-history judgment with a reason"],"model":"1. My Carthage purple dye and the alphabet for Athens' olive oil and jury trials. 2. Persia's road-and-relay-messenger idea for Rome's bronze tools. 3. Persia's dates and woven textiles for Carthage's grain. In real history, the alphabet spread farthest, because it was easy to learn and traders carried it to every port, and we still use a version of it."}]},
 "think": {
  "intro": "Use evidence from the whole unit. Your teacher scores this.",
  "items": [
   {"t":"open","key":"bestgov","q":"If you could live in Persia under Darius, Athens under Pericles, the Roman Republic or Carthage, which would you choose? Defend your choice with evidence about government, rights and daily life, and acknowledge one drawback.","min":66,"rows":8,"rubric":["A clear choice","Evidence about government and rights","Evidence about daily life or economy","An honest drawback","Considers who you would be (citizen, woman, enslaved person, foreigner)"],"model":"I would choose the Roman Republic. Citizens elected consuls each year, tribunes could veto unfair laws, and the Twelve Tables let everyone know the laws. Roman roads and trade made goods available across the Mediterranean. The drawback is that if I were a woman or enslaved person, I would have had no vote, and over time generals like Caesar took power away from citizens. Still, the Republic's idea of elected leaders checking each other inspired the United States."}]},
 "checkpoint": {
  "title": "Unit 4 Checkpoint: The Mediterranean World",
  "intro": "This checkpoint covers Weeks 16 to 19. Answer every question; use evidence and specific names and dates where you can. Mastery is 85 or higher. If you score below 85, your teacher will review with you, then you will retake it.",
  "parts": [
   {"title": "Part A: Persia and Greece", "items": [
    {"t":"open","q":"Name the founder of the Persian Empire and explain one policy that helped him hold it together.","key":"cpcyrus","min":16,"rows":2,"pts":3,"rubric":["Cyrus the Great","A policy: letting conquered peoples keep religions, customs or local leaders (tolerance) if they paid tribute"],"model":"Cyrus the Great founded it. He let conquered peoples keep their religions and customs as long as they paid tribute and stayed loyal, which reduced rebellions."},
    {"t":"text","q":"Which road about 1,600 miles long linked Sardis to Susa?","a":[{"all":[["royal"]],"none":["not"]}],"show":"the Royal Road","pts":3,"why":"Relay messengers used it."},
    {"t":"open","q":"Compare how Sparta and Athens trained boys, and say what each choice shows about what the city valued.","key":"cpboys","min":18,"rows":2,"pts":3,"rubric":["Sparta: army training from age 7, valuing military strength (to control helots)","Athens: reading, music, sport and public speaking, valuing citizenship and debate"],"model":"Spartan boys began army training at age 7, which shows Sparta valued military strength above all. Athenian boys studied reading, music, sport and speaking, which shows Athens valued thinking and taking part as citizens."},
    {"t":"open","q":"Explain why Greece's geography led to many independent city-states instead of one united country.","key":"cpgeo","min":17,"rows":2,"pts":4,"rubric":["Mountains separated valleys/communities","Each grew its own government (polis)"],"model":"Mountains divided Greece into separate valleys, so communities grew up apart and each became its own city-state with its own government."}]},
   {"title": "Part B: Rome and Carthage", "items": [
    {"t":"open","q":"Explain why plebeians demanded tribunes and what power tribunes gained.","key":"cptrib","min":16,"rows":2,"pts":3,"rubric":["Patricians held most power; plebeians walked out in 494 BCE","Tribunes, elected by plebeians, could veto laws that harmed plebeians"],"model":"Wealthy patricians held almost all the power, so plebeians walked out of Rome in 494 BCE. To bring them back, patricians agreed to tribunes, elected by plebeians, who could veto laws that harmed them."},
    {"t":"open","q":"Hannibal won at Cannae but lost the Second Punic War. Give one reason why.","key":"cphann","min":12,"rows":2,"pts":3,"rubric":["A valid reason (far from home with few supplies; Rome's Italian allies stayed loyal; Scipio attacked Africa; Masinissa's cavalry at Zama)"],"model":"Most of Rome's allies in Italy stayed loyal, so Rome kept raising new armies, while Hannibal got few soldiers or supplies from home. Then Scipio attacked Africa and won at Zama."},
    {"t":"text","q":"Name the Roman emperor born in North Africa whose reign began in 193 CE.","a":[{"all":[["severus","septimius"]],"none":["not"]}],"show":"Septimius Severus","pts":3,"why":"Born in Leptis Magna, in modern Libya."},
    {"t":"open","q":"Give two causes that turned the Roman Republic into an empire.","key":"cpfall","min":20,"rows":2,"pts":4,"rubric":["Two valid causes (armies loyal to generals; civil wars; wealth gap after conquests such as the Punic Wars; Caesar's seizure of power; Augustus)"],"model":"Conquests like the Punic Wars made the rich richer and hurt small farmers, which caused unrest, and generals like Julius Caesar had armies loyal to them instead of to Rome, which let them seize power."}]},
   {"title": "Part C: Sources and connections", "items": [
    {"t":"open","q":"Herodotus (a Greek) wrote about Persia, and Livy (a Roman) wrote about Hannibal. What do these two sources have in common that a historian should keep in mind? Give one way to check them.","key":"cpsources","min":30,"rows":3,"pts":5,"rubric":["Both were written by enemies or outsiders of the people they describe, and often long after the events","Check against other evidence (archaeology, inscriptions, tablets, other writers)"],"model":"Both men were outsiders writing about their own side's enemies, Herodotus about 50 years after the Persian Wars and Livy nearly 200 years after Hannibal, so they might be biased or repeat stories they couldn't check. A historian can compare them with archaeology, inscriptions like the Persepolis tablets, or other writers."},
    {"t":"open","q":"Name two ideas from ancient Rome or Greece that influenced the government of the United States, and explain one of them.","key":"cpusa","min":25,"rows":3,"pts":5,"rubric":["Two valid ideas (republic, senate, veto, checks and balances, written laws/rule of law, democracy, civic virtue like Cincinnatus)","An accurate explanation of one"],"model":"The Senate and the veto both came from Rome. The U.S. president can veto laws passed by Congress, just as Roman consuls and tribunes could block decisions, so no one part of the government has all the power."},
    {"t":"open","q":"Explain one way Africa shaped the Mediterranean world in Unit 4.","key":"cpafrica","min":19,"rows":2,"pts":4,"rubric":["A valid example (alphabet from Egypt; Carthage as a great power; Alexandria's learning; North Africa as Rome's breadbasket; Terence, Severus, Augustine; Masinissa)"],"model":"North Africa, including Egypt, grew much of the grain that fed the city of Rome, so the empire depended on Africa to survive."}]}]},
 "next": "Unit 5: empires and global trade, starting with Ghana and the trans-Saharan trade."
}

TEACHER = {
 "standards": [
  "SS.6.W.3.1: Analyze the cultural impact the ancient Phoenicians had on the Mediterranean world with regard to colonization (Carthage), exploration, maritime commerce (purple dye, tin), and written communication (alphabet).",
  "SS.6.W.3.2: Explain the democratic concepts (polis, civic participation and voting rights, legislative bodies, written constitutions, rule of law) developed in ancient Greece.",
  "SS.6.W.3.4: Explain the causes and effects of the Persian and Peloponnesian Wars.",
  "SS.6.W.3.9: Explain the impact of the Punic Wars on the development of the Roman Empire.",
  "SS.6.W.3.11: Explain the transition from Roman Republic to empire and Imperial Rome, and compare Roman life and culture under each one.",
  "SS.6.CG.1.2: Analyze the influence of ancient Rome on the United States' constitutional republic.",
  "SS.6.G.2.6: Explain the concept of cultural diffusion, and identify the influences of different ancient cultures on one another.",
  "SS.6.W.1.3: Interpret primary and secondary sources."],
 "materials": ["The interactive lesson", "Index cards, markers, small household items as trade goods", "A world map, atlas or globe", "Notes from Weeks 16 to 19", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run one question from each week of the unit."],
  [4, "Hook", "Mare Nostrum and the scaled timeline."],
  [10, "Four ways to govern", "Compare Persia, Athens, Sparta, Rome and Carthage; who was excluded."],
  [9, "Wars and effects", "Persian Wars and Punic Wars side by side."],
  [9, "Ideas that traveled", "Trace the alphabet and other ideas."],
  [12, "Assign", "Set up the market; review the project rubric; assign Think Deeper."],
  [10, "Checkpoint preview", "Explain that the checkpoint is completed after class, independently, one try per item, with no answers shown until you review it. Mastery is 85; below 85 means a review lesson and a retake."]],
 "key_questions": ["Who held power, and who was left out?", "What caused this war, and what changed because of it?", "Where did this idea come from?", "Who wrote this source, and why?"],
 "misconceptions": ["Greece and Rome invented civilization on their own.", "Carthage was not an African city.", "All Athenians could vote.", "Julius Caesar was the first emperor."],
 "support": ["Use a four-column organizer (Persia, Greece, Rome, Carthage).", "Keep the scaled timeline visible during review (not during the checkpoint).", "Read checkpoint questions aloud if reading is a barrier."],
 "challenge": ["Add Egypt (Kemet) and Kush as a fifth and sixth column in the organizer, using Unit 2.", "Research the Library of Alexandria and what may have caused its decline."],
 "background": "<p>The checkpoint is scored out of 40 points: Part A 13, Part B 13, Part C 14. A score of 85 percent is 34 of 40 points. Open items are scored with the rubric after submission. Carthage's government included two annually elected chief magistrates (suffetes), a council of elders and a popular assembly (Aristotle, Politics 2.11).</p>",
 "sources": ["Herodotus, Thucydides, Livy (Project Gutenberg translations used in Weeks 16 to 19).", "British Museum, Persia, Greece, Rome and Carthage collections.", "Miles, Richard, Carthage Must Be Destroyed (2010)."]
}

PRINT = {
 "directions": "Answer in complete sentences. This is review practice, not the checkpoint.",
 "items": [
  {"q":"Describe the government of Persia, Athens, Sparta, Rome and Carthage in one sentence each.","a":"Persia: Great King with satraps. Athens: direct democracy for citizen men. Sparta: two kings, council, military assembly. Rome: republic of consuls, Senate, assemblies and tribunes, later an empire. Carthage: trading republic with elected officials and a council.","lines":5},
  {"q":"Explain a cause and an effect of the Persian Wars.","a":"Cause: Athens helped the Ionian Revolt. Effect: Greek independence and Athens' rise as a sea power.","lines":2},
  {"q":"Explain a cause and an effect of the Punic Wars.","a":"Cause: rivalry over Sicily and the western Mediterranean. Effect: Carthage destroyed; Rome dominant and wealthier.","lines":2},
  {"q":"Trace the alphabet from Egypt to Rome.","a":"Semitic-speaking workers in Egypt adapted hieroglyphs; Phoenicians spread it; Greeks added vowels; Romans adapted it into Latin letters.","lines":2},
  {"q":"Name three North Africans who shaped the Roman world.","a":"Terence, Septimius Severus, Augustine (also Masinissa).","lines":1},
  {"q":"Why should historians read Herodotus and Livy carefully?","a":"They wrote about enemies, sometimes long after the events, and repeated stories they could not check.","lines":2}]
}
