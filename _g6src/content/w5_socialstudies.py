from geo import africa_map

LABEL = ('<svg viewBox="0 0 560 220" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Parts of a museum label">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Anatomy of a museum label</text>'
  '<rect x="30" y="34" width="320" height="170" fill="#fff" stroke="#0A1F3D" stroke-width="2"/>'
  '<text x="46" y="62" font-family="Georgia" font-size="17" font-weight="bold" fill="#0A1F3D">Carved Ochre</text>'
  '<text x="46" y="82" font-size="11" fill="#5b6676">Blombos Cave, South Africa · about 75,000 years ago</text>'
  '<text x="46" y="98" font-size="11" fill="#5b6676">Red ochre (iron-rich stone) · replica</text>'
  '<text x="46" y="122" font-size="12">Someone scratched a crosshatch pattern into</text><text x="46" y="138" font-size="12">this piece of red ochre on purpose. It is one of</text>'
  '<text x="46" y="154" font-size="12">the oldest known designs made by people, and it</text><text x="46" y="170" font-size="12">shows our ancestors thought in symbols.</text>'
  '<text x="46" y="192" font-size="12" font-style="italic" fill="#0047BA">Look closely: how many lines can you count?</text>'
  + ''.join(f'<line x1="352" y1="{y}" x2="380" y2="{y}" stroke="#DB2F30"/><text x="386" y="{y+4}" fill="#DB2F30" font-weight="bold">{t}</text>' for y, t in [(58, "Title"), (80, "Place and date"), (96, "Material"), (146, "The story: why it matters"), (188, "A question for the visitor")]) +
  '</svg>')

UNITMAP = africa_map([(-8.9, 31.9, 'Jebel Irhoud', 6, -4), (30.7, 22.5, 'Nabta Playa', 6, -4), (40.5, 11.1, 'Hadar (Lucy)', 6, 0), (36.0, 3.0, 'Lomekwi', 6, 4),
                      (21.2, -34.4, 'Blombos Cave', -6, 14), (-3.0, 16.8, 'Timbuktu', -6, -6), (36.4, 15.5, 'Sudan: sorghum', 6, 8)],
                     'Unit 1 places to remember', rivers=True)

LESSON = {
 "unit": "Unit 1: How We Know the Past",
 "title": "Unit 1 Checkpoint and Museum Exhibit Project",
 "subtitle": "Museums do more than display objects. They decide which stories get told. This week you become the curator.",
 "objectives": [
  "Explain how museums choose, interpret and display evidence about the past.",
  "Write clear museum labels with a title, place, date, material and story.",
  "Discuss who owns the past and why some museums are returning objects to the countries they came from.",
  "Plan and build a museum exhibit that answers a big question about Unit 1.",
  "Show mastery of Unit 1 on the checkpoint (85 or higher)."],
 "vocab": [
  ["curator", "A person who chooses, researches and arranges the objects in a museum exhibit."],
  ["exhibit", "A collection of objects, images and labels arranged to tell a story or answer a question."],
  ["artifact", "An object made or used by people in the past."],
  ["replica", "An exact copy of an object, often used when the original is too fragile or valuable to display."],
  ["interpretation", "An explanation of what evidence means. Different people may interpret the same evidence differently."],
  ["repatriation", "Returning objects or remains to the country or community they were taken from."]],
 "reconnect": {
  "title": "Weeks 1 to 4: how we know the past",
  "intro": "Your exhibit will draw on every week of this unit. Check your memory first.",
  "items": [
   {"t":"text","q":"A diary written by a soldier during a war is what kind of source?","a":["primary","primary source","a primary source","^primary"],"show":"a primary source","pts":2,"why":"It was created at the time by someone who was there."},
   {"t":"text","q":"Which map projection keeps the true sizes of land areas but stretches their shapes?","a":["gall-peters","gall peters","peters","equal area","equal-area"],"show":"Gall-Peters (an equal-area projection)","pts":2,"why":"Equal-area maps like Gall-Peters show true size; Mercator keeps shapes for navigation but enlarges lands near the poles."},
   {"t":"text","q":"Name the site in Morocco where the oldest known Homo sapiens fossils were found.","a":["jebel irhoud"],"show":"Jebel Irhoud","pts":2,"why":"About 300,000 years old."},
   {"t":"text","q":"What word means extra food that can be stored or traded?","a":["surplus","a surplus"],"pts":2,"why":"A surplus made specialists possible."},
   {"t":"text","q":"Name one crop first domesticated in Africa.","a":["sorghum","pearl millet","african rice","yams","yam","okra","watermelon","teff","enset","finger millet","coffee"],"show":"sorghum (or pearl millet, African rice, yams, okra, teff)","pts":2,"why":"African farmers gave the world sorghum, pearl millet, African rice, yams, okra, watermelon and teff."},
   {"t":"open","key":"rc_unit","q":"Pick one thing you learned this unit that changed how you think about the past. Explain the change.","min":20,"rows":3,"rubric":["Names a specific idea from Unit 1","Explains what they thought before and after"],"model":"I used to think farming was invented in one place and spread. Now I know people on several continents, including Africa and the Americas, started farming on their own, which shows people everywhere were inventive."}]},
 "hook": {
  "title": "Who Tells the Story?",
  "html": "<p>In 1897, British soldiers attacked Benin City in what is now Nigeria and carried away thousands of bronze and ivory sculptures, now called the Benin Bronzes. For more than a century, many were displayed in museums in Europe and the United States with labels that said little about how they were taken.</p><p>In 2022, the Smithsonian's National Museum of African Art in Washington, D.C., returned 29 Benin Bronzes to Nigeria. Museums around the world are now asking hard questions: Who should own these objects? Who should tell their story?</p><div class='callout'><b>Big idea:</b> Every exhibit is an interpretation. A good curator uses evidence, names its sources, and thinks about whose voices are included.</div>"},
 "learn": [
  {"title": "How Museums Tell Stories",
   "visual": LABEL,
   "html": "<p>A curator starts with a <b>big question</b>, chooses objects that help answer it, and writes labels that explain why each object matters. Every label has the same parts: title, place and date, material, the story, and often a question to make the visitor look closer.</p><p>Labels must be short. Most visitors read a label for less than a minute, so curators choose every word carefully, just like the pacing choices you made in ELA.</p>",
   "checks": [
    {"t":"text","q":"What is the job title of the person who chooses and arranges the objects in an exhibit?","a":["curator","a curator","the curator"],"pts":2,"why":"A curator researches, chooses and arranges an exhibit."},
    {"t":"text","q":"The Blombos label says <i>replica</i>. What does that tell the visitor?","a":[{"all":[["copy","not the real","not real","not original","model","fake","reproduction"]]}],"show":"the object is an exact copy, not the original","pts":2,"why":"A replica is an exact copy, used when the original is too fragile or valuable."},
    {"t":"open","key":"writelabel","q":"Write a museum label (title, place and date, material, story in 2 to 3 sentences, and a question) for the 3.3-million-year-old Lomekwi stone tools.","min":40,"rows":5,"rubric":["Title","Place and date (Lomekwi, Kenya; about 3.3 million years ago)","Material (stone)","Story explains why it matters","A question for the visitor"],"model":"Lomekwi Stone Tools. Lomekwi, near Lake Turkana, Kenya, about 3.3 million years ago. Stone. These are the oldest stone tools ever found, made before our own species existed. Someone struck these rocks on purpose to make sharp edges, which shows early hominins planned and solved problems. Question: what do you think these tools were used to cut?"}]},
  {"title": "Who Owns the Past?",
   "html": "<p>Many famous artifacts in European and American museums were taken during colonial rule or war, often without the permission of the people who made them. Communities in Africa, the Americas, Asia and the Pacific have asked for these objects to be returned. This is called <b>repatriation</b>.</p><p>Some museums argue they protect objects and share them with millions of visitors. Others say objects belong with the people whose ancestors made them, and that those communities should tell their own history. In 2022, the Smithsonian returned 29 Benin Bronzes to Nigeria, and other museums in Germany and the United Kingdom have returned objects as well.</p>",
   "checks": [
    {"t":"text","q":"What is the word for returning objects to the country or community they were taken from?","a":["repatriation","repatriate"],"show":"repatriation","pts":2,"why":"Repatriation means returning objects or remains home."},
    {"t":"num","q":"How many Benin Bronzes did the Smithsonian return to Nigeria in 2022?","a":29,"pts":2,"why":"The National Museum of African Art returned 29 Benin Bronzes in October 2022."},
    {"t":"open","key":"owns","q":"Give one argument for keeping an artifact in a museum far from where it was made and one argument for returning it. Which argument do you find stronger, and why?","min":45,"rows":5,"rubric":["One fair argument for keeping","One fair argument for returning","States a position with a reason","Respectful of both sides"],"model":"Some say a big museum can protect the object and let millions of visitors from around the world learn from it. Others say it was taken by force, so it belongs to the community whose ancestors made it, and they should tell its story. I think the argument for returning is stronger when the object was stolen, because a museum should not profit from a theft, but museums can still borrow objects or make replicas."}]},
  {"title": "Planning Your Museum Exhibit",
   "visual": UNITMAP,
   "html": "<p>Your exhibit answers one big question about Unit 1, such as:</p><ul><li>How do we know what happened before writing?</li><li>Why do scientists say all humans share African roots?</li><li>Was farming a good trade for the first farmers?</li><li>How do maps shape the way we see the world?</li></ul><p>Your exhibit needs at least <b>five objects</b> (real items, replicas you make, drawings or printed images), each with a label; an introduction panel; and a map or timeline. Use the flour you ground in Week 4, your dig box artifacts from Week 3 or your family history interview from Week 1. Full directions and the rubric are on the Unit 1 Projects page.</p>",
   "checks": [
    {"t":"open","key":"exhibitplan","q":"Write your big question, the five objects you plan to include, and one sentence about why each object helps answer the question.","min":60,"rows":7,"rubric":["A clear big question","Five objects listed","Each object connected to the question","Uses evidence from at least three different weeks"],"model":"Big question: Was farming a good trade for the first farmers? 1. My jar of hand-ground flour: shows how much daily work grinding took. 2. A drawing of a saddle quern: the tool women used for hours each day. 3. A printed photo of an ear of maize beside teosinte: shows how farmers changed plants. 4. A clay model of a Çatalhöyük house: shows crowded village life. 5. A chart comparing forager and farmer heights: evidence that early farmers were often less healthy."}]}],
 "handson": {
  "title": "Build Your Museum Exhibit",
  "intro": "Turn a table, shelf or trifold board into a museum. Then give a tour.",
  "materials": ["A table, shelf or trifold board", "Five or more objects: real items, replicas you make (clay, cardboard, paper), drawings or printed images", "Index cards or card stock for labels", "Markers or a printer", "Your Unit 1 work: Week 4 flour, Week 3 dig box artifacts, Week 1 interview or timeline, Week 2 maps", "A phone to take photos"],
  "steps": [
   "Write an introduction panel with your big question and a short answer (3 to 5 sentences).",
   "Arrange your objects in an order that tells a story.",
   "Write a label for each object with a title, place and date, material, story and a question.",
   "Add a map or timeline that shows where and when your objects come from.",
   "Give a 3-minute tour to your family. Ask each visitor which object they will remember and why.",
   "Photograph the whole exhibit and each label."],
  "record": [
   {"t":"open","key":"intropanel","q":"Type your introduction panel and all five object labels.","min":150,"rows":14,"rubric":["Introduction panel states the big question and answer","Five labels, each with title, place and date, material, story and question","Facts are accurate and drawn from Unit 1","Clear, short writing for visitors"],"model":"Was Farming a Good Trade? About 11,000 years ago, people in at least seven regions of the world began to farm. Farming gave villages extra food and let towns grow, but the first farmers worked harder and were often less healthy than the foragers before them. Explore the evidence and decide for yourself.\nLabel 1: Hand-Ground Flour. Made in my kitchen, 2026, recreating a method from about 10,000 years ago. Wheat berries. It took me 10 minutes to grind 2 tablespoons. One loaf would take about 4 hours. Question: who do you think did this work every day? (Labels 2 to 5 follow the same pattern.)"},
   {"t":"open","key":"tour","q":"After your tour, what did your visitors remember most, and what would you change if you built the exhibit again?","min":30,"rows":3,"rubric":["Reports visitor feedback","Names a specific improvement"],"model":"My grandmother remembered the flour jar most because she could not believe one loaf took four hours. My brother said the labels were too long, so next time I would cut each story to two sentences."}]},
 "think": {
  "intro": "Explain your reasoning. Your teacher scores this.",
  "items": [
   {"t":"open","key":"curatorchoice","q":"A curator has space for only one of two objects in an exhibit about early farming: a beautiful gold necklace from a ruler's tomb, or a worn grinding stone used by an ordinary woman. Which should the curator choose, and what does the choice say about whose history matters? Use evidence from Unit 1.","min":70,"rubric":["Makes a clear choice","Explains what each object reveals about the past","Discusses whose stories museums tell","Uses Unit 1 evidence (grinding, skeletons, specialists, inequality)"],"model":"I would choose the grinding stone. The gold necklace shows that some people had great wealth, which connects to the inequality that grew after farming created surpluses. But the grinding stone tells the story of most people's lives. Skeletons from early farming villages show worn toes, knees and backs from hours of grinding each day. Museums have often shown the treasures of rulers, so choosing the grinding stone tells visitors that ordinary people's work is history too."}]},
 "checkpoint": {
  "title": "Unit 1 Checkpoint: How We Know the Past",
  "intro": "This checkpoint covers Weeks 1 to 5. Mastery is 85 or higher. If you score below 85, your teacher will review with you, then you will retake it.",
  "parts": [
   {"title": "Part A: Historians and sources", "items": [
    {"t":"text","q":"A modern textbook chapter about ancient Kemet is what kind of source?","a":["secondary","secondary source","a secondary source","^secondary"],"show":"a secondary source","pts":2,"why":"It was written long afterward by someone who studied primary sources."},
    {"t":"num","q":"How many years apart are 800 BCE and 200 CE?","a":[1000,999],"unit":"years","show":"1,000 (999 if you account for there being no year 0)","pts":3,"why":"About 800 years from 800 BCE to 1 CE, plus 200 = 1,000 years. Because there is no year 0, the exact count is 999; both are accepted."},
    {"t":"open","key":"cp_bias","q":"Why should a historian compare more than one source about the same event? Give an example.","min":20,"rows":3,"rubric":["Sources can be biased, incomplete or from one point of view","Example comparing two perspectives"],"model":"One source may tell only one side or leave things out. For example, a British soldier's account of the 1897 attack on Benin City would describe it very differently from the memories of people in Benin."}]},
   {"title": "Part B: Maps and geography", "items": [
    {"t":"text","q":"On a Mercator map, Greenland looks about the same size as Africa. Which is really much larger?","a":["africa"],"pts":2,"why":"Africa is about 14 times larger than Greenland."},
    {"t":"text","q":"Timbuktu is at about 17°N, 3°W. Which two hemispheres is it in?","a":[{"all":[["north"],["west"]]}],"show":"Northern and Western","pts":2,"why":"North of the equator and west of the prime meridian."}]},
   {"title": "Part C: Human beginnings", "items": [
    {"t":"num","q":"About how many years old are the Lomekwi stone tools, the oldest known?","a":3300000,"tol":100000,"unit":"years","show":"about 3.3 million (3,300,000)","pts":2,"why":"About 3.3 million years, older than our own species."},
    {"t":"open","key":"cp_oneafrica","q":"Use two pieces of evidence from Week 3 to explain why scientists say all living humans share African roots.","min":25,"rows":3,"rubric":["Oldest Homo sapiens fossils found in Africa (Jebel Irhoud, Omo Kibish, Florisbad)","Genetic evidence: Africa has the greatest human genetic diversity, or all humans share about 99.9% of DNA"],"model":"The oldest Homo sapiens fossils, about 300,000 years old, come from Jebel Irhoud in Morocco and other African sites. DNA also shows that Africa has the greatest human genetic diversity, which means humans have lived there the longest before groups spread to other continents."}]},
   {"title": "Part D: The first farmers", "items": [
    {"t":"text","q":"In which region of Africa was sorghum first domesticated?","a":["sudan","eastern sudan","eastern sahel","sahel","sudan and the eastern sahel","northeast africa"],"show":"Sudan and the eastern Sahel","pts":2,"why":"Evidence from eastern Sudan dates to about 5,000 years ago."},
    {"t":"open","key":"cp_trade","q":"Explain one way farming helped early communities and one way it made life harder, with evidence.","min":25,"rows":3,"rubric":["A benefit with evidence (surplus, specialists, towns)","A cost with evidence (shorter stature, tooth decay, hard labor, disease)"],"model":"Farming created a surplus of stored grain, which let towns like Çatalhöyük grow and let some people become potters and builders. But skeletons show many early farmers were shorter and had more tooth decay than foragers, because they ate only a few crops."}]}]},
 "next": "Unit 2: The Nile Valley and Ancient Africa. You will travel down the Nile to Kemet, Nubia and the Kingdom of Kush."
}

TEACHER = {
 "standards": [
  "SS.6.W.1.3: Interpret primary and secondary sources.",
  "SS.6.W.1.4: Describe the methods of historical inquiry and how history relates to the other social sciences.",
  "SS.6.W.1.5: Describe the roles of historians and recognize varying historical interpretations (historiography).",
  "SS.6.W.1.6: Describe how history transmits culture and heritage and provides models of human character.",
  "C3 Framework D4.2.6-8: Construct explanations using reasoning, correct sequence, examples, and details with relevant information and data."],
 "materials": ["The interactive lesson", "Index cards or card stock for labels", "A table, shelf or trifold board", "The student's Unit 1 work and artifacts", "The Unit 1 Projects page with the exhibit rubric", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Reconnect questions."],
  [6, "Hook", "Tell the story of the Benin Bronzes and their 2022 return. Ask: who should tell an object's story?"],
  [12, "Museum labels", "Study the label anatomy. Write the Lomekwi label together."],
  [10, "Who owns the past?", "Discuss both sides of repatriation respectfully. Have the student state and defend a position."],
  [16, "Plan the exhibit", "Choose the big question and five objects. Check that the plan uses at least three weeks of Unit 1."],
  [5, "Due dates", "Set dates for the exhibit, the family tour and the checkpoint (all after class)."],
  [5, "Close", "Review the exhibit rubric."]],
 "key_questions": ["What is your exhibit's big question?", "Why did you choose this object over another?", "Whose stories are told in your exhibit, and whose are missing?", "What evidence supports each label?"],
 "misconceptions": ["Thinking museum labels are simply facts with no interpretation.", "Believing every museum object was obtained fairly.", "Making an exhibit that lists facts instead of answering a question."],
 "support": ["Provide a label template with blanks for each part.", "Limit the exhibit to five objects with short labels.", "Let the student dictate labels before typing."],
 "challenge": ["Add a section showing two different interpretations of the same evidence.", "Research one artifact that has been repatriated and add a label about its journey home."],
 "background": "<p>British forces attacked Benin City in February 1897 and removed thousands of objects. The Smithsonian's National Museum of African Art transferred ownership of 29 Benin Bronzes to Nigeria's National Commission for Museums and Monuments in October 2022. Germany began returning Benin Bronzes to Nigeria in 2022 as well. The checkpoint BCE/CE item accepts both 1,000 and 999, because there is no year 0. The Museum Exhibit Project is scored with the five-trait rubric on the Unit 1 Projects page (20 points; multiply by 5 for a score out of 100; mastery 85).</p>",
 "sources": ["Smithsonian National Museum of African Art: Benin Bronzes return (October 2022).", "British Museum: Benin Bronzes collection history.", "CPALMS: SS.6.W.1.3 to SS.6.W.1.6."]
}

PRINT = {
 "directions": "Use complete sentences and evidence from Unit 1.",
 "items": [
  {"q":"Name the five parts of a museum label.","a":"Title; place and date; material; story; question for the visitor","lines":2},
  {"q":"Write a label for an object from your own home that tells something about your family's history.","a":"Answers vary; must include all five parts.","lines":5},
  {"q":"Define repatriation and give one example.","a":"Returning objects to the country or community they were taken from; for example, the Smithsonian returned 29 Benin Bronzes to Nigeria in 2022.","lines":2},
  {"q":"What is the difference between a primary and a secondary source? Give an example of each from Unit 1.","a":"Primary: made at the time (a stone tool, a griot's account); secondary: made later by someone studying it (a textbook).","lines":3},
  {"q":"Write the big question for your exhibit and list your five objects.","a":"Answers vary.","lines":4},
  {"q":"Explain one way a museum can show more than one point of view.","a":"For example: include labels written with the community the object came from, or show two interpretations side by side.","lines":2}]
}
