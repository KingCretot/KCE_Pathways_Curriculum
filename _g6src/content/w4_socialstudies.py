from geo import world_map

CENTERS = world_map([(40, 36, 'Fertile Crescent', 6, -4), (112, 34, 'China', 6, -9), (144, -6, 'New Guinea', -6, 14), (-98, 19, 'Mesoamerica', -6, -4),
                     (-72, -13, 'Andes', 6, 4), (-86, 37, 'Eastern N. America', -6, -8), (-2, 14, 'West African Sahel', -6, 12), (32, 14, 'Sudan', -8, -8),
                     (39, 9, 'Ethiopian Highlands', 6, 14), (68, 29, 'Indus (Mehrgarh)', 6, 12)],
                    'Where people began farming, independently or early')

HOUSE = ('<svg viewBox="0 0 560 240" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Cutaway drawing of a Catalhoyuk house">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Çatalhöyük: houses packed wall to wall, entered through the roof</text>'
  '<rect x="20" y="80" width="520" height="140" fill="#e8d3a8" stroke="#8a6d1f"/>'
  + ''.join(f'<rect x="{x}" y="80" width="130" height="140" fill="{c}" stroke="#8a6d1f" stroke-width="3"/>' for x, c in [(20, '#e8d3a8'), (150, '#f1e0bd'), (280, '#e8d3a8'), (410, '#f1e0bd')]) +
  '<rect x="150" y="70" width="130" height="12" fill="#a9824a"/><rect x="195" y="70" width="30" height="12" fill="#3b2a12"/>'
  '<line x1="205" y1="75" x2="185" y2="215" stroke="#5b3a12" stroke-width="3"/><line x1="220" y1="75" x2="200" y2="215" stroke="#5b3a12" stroke-width="3"/>'
  + ''.join(f'<line x1="{205-i*3}" y1="{95+i*20}" x2="{220-i*3}" y2="{95+i*20}" stroke="#5b3a12" stroke-width="2"/>' for i in range(6)) +
  '<rect x="240" y="180" width="30" height="34" fill="#c45c2a"/><text x="255" y="232" text-anchor="middle" font-size="10">oven</text>'
  '<rect x="160" y="196" width="28" height="18" fill="#cdb48a" stroke="#8a6d1f"/><text x="174" y="232" text-anchor="middle" font-size="10">platform</text>'
  '<path d="M290 120 q10 -20 20 0 q10 20 20 0" fill="none" stroke="#DB2F30" stroke-width="2"/><text x="345" y="112" font-size="10">wall paintings</text>'
  '<text x="85" y="60" text-anchor="middle" font-size="11">no streets: people walked</text><text x="85" y="74" text-anchor="middle" font-size="11">across the rooftops</text>'
  '<path d="M140 64 L190 72" stroke="#0A1F3D"/><text x="420" y="60" text-anchor="middle" font-size="11">ladder through a roof hole</text><path d="M360 62 L226 76" stroke="#0A1F3D"/></svg>')

FLOW = ('<svg viewBox="0 0 560 180" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Chain of effects from farming">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">One change leads to another</text>'
  + ''.join(f'<rect x="{10+i*110}" y="50" width="100" height="70" rx="10" fill="{c}"/><text x="{60+i*110}" y="80" text-anchor="middle" fill="#fff" font-weight="bold">{a}</text><text x="{60+i*110}" y="98" text-anchor="middle" fill="#fff" font-size="11">{b}</text>'
            + (f'<path d="M{110+i*110} 85 h10" stroke="#0A1F3D" stroke-width="2"/><path d="M{120+i*110} 85 l-5 -4 v8z" fill="#0A1F3D"/>' if i < 4 else '')
            for i, (a, b, c) in enumerate([("Farming", "planting, herding", "#0A1F3D"), ("Surplus", "extra food stored", "#0047BA"), ("More people", "villages grow", "#2f5a91"), ("Specialists", "potters, builders", "#C9A84C"), ("Trade and rules", "towns, leaders", "#DB2F30")])) +
  '<text x="280" y="150" text-anchor="middle" font-size="12">Every arrow is a cause and an effect. Historians ask which links were strongest, and who gained or lost.</text></svg>')

LESSON = {
 "unit": "Unit 1: Beginnings",
 "title": "Farming, Villages and the First Towns",
 "subtitle": "For most of human history, people gathered and hunted their food. Then, in at least ten places on Earth, people began to farm.",
 "objectives": [
  "Explain what domestication is and how it differs from gathering and hunting.",
  "Locate the places where farming began and recognize that it started independently on several continents, including Africa.",
  "Compare the lifestyles of hunter-gatherers and early farmers.",
  "Describe early towns such as Jericho and Çatalhöyük and the evidence historians use to study them.",
  "Analyze the chain of effects of farming, including its costs, and argue whether it was a good trade."],
 "vocab": [
  ["domestication", "Changing plants or animals over many generations, by choosing which ones to grow or breed, so they become more useful to people."],
  ["agriculture", "Growing crops and raising animals for food and other products."],
  ["Neolithic", "The New Stone Age, when many people began farming and living in permanent villages."],
  ["surplus", "More than is needed right away; extra food that can be stored or traded."],
  ["specialization", "When people do one kind of work, such as making pottery, instead of all producing their own food."],
  ["pastoralist", "A person who raises herds of animals, often moving with them to find grass and water."],
  ["settlement", "A place where people live permanently."],
  ["independent invention", "When different groups develop the same idea on their own, without learning it from each other."]],
 "reconnect": {
  "title": "Week 3: human beginnings in Africa",
  "intro": "This week's farmers were the descendants of the people you studied last week, so start by reviewing what you learned.",
  "items": [
   {"t":"text","q":"On which continent did <i>Homo sapiens</i> first appear?","a":["africa"],"pts":2,"why":"The oldest known Homo sapiens fossils, from Jebel Irhoud in Morocco, are about 300,000 years old."},
   {"t":"num","q":"About how many years old are the Jebel Irhoud fossils?","a":300000,"unit":"years","pts":2,"why":"About 300,000 years."},
   {"t":"text","q":"In undisturbed layers of earth, are deeper layers usually older or younger?","a":["older","older layers"],"pts":2,"why":"Layers pile up over time, so deeper usually means older (the law of superposition)."},
   {"t":"num","q":"All humans share about what percent of their DNA?","a":99.9,"unit":"%","pts":2,"why":"About 99.9%, which is why races are not separate biological groups."},
   {"t":"open","key":"rc_hunter","q":"Describe how people got food for almost all of human history before farming. Give two specific examples.","min":15,"rows":2,"rubric":["Gathering and hunting (or fishing)","Two concrete examples"],"model":"They gathered and hunted. For example, they collected wild seeds, fruits and shellfish, and hunted animals like antelope or fished in rivers and lakes."},
   {"t":"open","key":"rc_evidence","q":"Name one kind of evidence from Week 3 that tells us early humans planned and made art, and explain what it shows.","min":15,"rows":2,"rubric":["Names real evidence (Blombos ochre or beads, tools)","Explains what it shows about thinking"],"model":"At Blombos Cave in South Africa, people carved patterns into ochre about 75,000 years ago, which shows they used symbols and planned ahead."}]},
 "hook": {
  "title": "One Day in Two Worlds",
  "html": "<p>Imagine two families 10,000 years ago. The first family moves with the seasons, gathering wild grains, fruits and roots, hunting, and fishing. They carry everything they own. The second family has stayed in one valley for years. They plant seeds, weed fields, guard their goats, and store grain in clay jars.</p><p>Which family works harder? Which eats better? Which is healthier? The answers surprised historians and archaeologists, and they are still debated.</p><div class='callout'><b>Big idea:</b> Farming changed almost everything about human life, but it was a trade, with real gains and real costs.</div>"},
 "learn": [
  {"title": "Domestication: Changing Plants and Animals",
   "html": "<p>Wild wheat drops its seeds to the ground when ripe, which is perfect for the plant and terrible for a harvester. Over many generations, people kept replanting seeds from plants whose seeds stayed on the stalk. Slowly, the plants changed. That is <b>domestication</b>.</p><p>The same happened with animals. People kept and bred the calmest goats, sheep and cattle. In northeast Africa, some researchers argue that people were managing cattle at sites like Nabta Playa (from Week 1) as early as about 9,000 years ago, though scientists still debate when those cattle became fully domesticated.</p><p>Wild teosinte in Mexico had tiny ears with a handful of hard kernels. Thousands of years of selection by farmers in Mesoamerica turned it into maize (corn).</p>",
   "checks": [
    {"t":"open","key":"select","q":"Explain in your own words how farmers changed wild wheat without any modern science. Use the word <b>generations</b>.","min":20,"rows":3,"rubric":["Farmers chose seeds from useful plants","Replanted those seeds again and again","The plant changed over many generations"],"model":"Farmers kept seeds from the wheat plants that held on to their seeds and planted them the next year. They did this again and again for many generations, so the wheat slowly changed into a plant that keeps its seeds until harvest."},
    {"t":"text","q":"What wild plant in Mexico did farmers turn into maize?","a":["teosinte"],"pts":2,"why":"Teosinte, a wild grass with tiny ears."},
    {"t":"open","key":"calm","q":"Why would early herders breed the calmest animals instead of the biggest or strongest? Give one reason.","min":12,"rows":2,"rubric":["Calm animals are safer and easier to manage, gather and keep"],"model":"Calm animals are easier and safer to keep in a pen and lead to water, so they are less likely to run away or hurt someone."}]},
  {"title": "Farming Began in Many Places",
   "visual": CENTERS,
   "html": "<p>Farming was not invented once and spread from one place. Scientists have found that people in at least ten regions began farming on their own, with different crops. Dates are approximate and are revised as new evidence is found.</p><table class='t'><tr><th>Region</th><th>Early crops or animals</th><th>About how long ago</th></tr><tr><td>Fertile Crescent (Southwest Asia)</td><td>wheat, barley, goats, sheep</td><td>11,000 years</td></tr><tr><td>China</td><td>millet (north), rice (south)</td><td>9,000 to 10,000 years</td></tr><tr><td>Mesoamerica</td><td>squash, then maize, beans</td><td>9,000 to 10,000 years</td></tr><tr><td>Andes (South America)</td><td>potatoes, quinoa, llamas</td><td>about 8,000 years</td></tr><tr><td>New Guinea</td><td>taro, bananas</td><td>about 7,000 years or more</td></tr><tr><td>Sudan and the eastern Sahel (Africa)</td><td>sorghum</td><td>about 5,000 years</td></tr><tr><td>West African Sahel</td><td>pearl millet, later African rice and yams</td><td>about 4,500 years</td></tr><tr><td>Ethiopian Highlands (Africa)</td><td>teff, enset, coffee</td><td>debated; thousands of years</td></tr><tr><td>Eastern North America</td><td>sunflower, squash</td><td>about 5,000 years</td></tr></table><p>African farmers domesticated crops the world still eats: sorghum, pearl millet, African rice, yams, coffee, okra and watermelon.</p>",
   "checks": [
    {"t":"num","q":"About how many years ago did farming begin in the Fertile Crescent?","a":11000,"unit":"years","pts":2,"why":"About 11,000 years ago."},
    {"t":"blanks","q":"Name the region where each crop was first domesticated.","sent":"Potatoes: ___. Sorghum: ___ (in Africa). Rice: ___.","blanks":[["andes","the andes","south america","peru"],["sudan","eastern sahel","sahel","sudan and the eastern sahel"],["china","southern china"]],"show":"Andes; Sudan (eastern Sahel); China","pts":3,"why":"Potatoes in the Andes, sorghum in Sudan and the eastern Sahel, rice in southern China."},
    {"t":"open","key":"independent","q":"Why is it important that farming began independently in many places, instead of being invented once and spread? What does this tell us about people around the world?","min":25,"rows":3,"rubric":["Explains independent invention","Concludes that people everywhere were inventive and solved problems","Avoids the idea that one group taught everyone"],"model":"It shows that people in Africa, Asia, the Americas and New Guinea all figured out farming on their own, using the plants around them. No single group was the only inventor; people everywhere were smart problem solvers."},
    {"t":"blanks","q":"Name two different crops first domesticated in Africa.","sent":"Crop 1: ___   Crop 2: ___","blanks":[["sorghum","pearl millet","millet","african rice","yams","yam","coffee","okra","watermelon","watermelons","teff","enset"],["sorghum","pearl millet","millet","african rice","yams","yam","coffee","okra","watermelon","watermelons","teff","enset"]],"distinct":True,"show":"For example: sorghum and coffee","pts":2,"why":"Sorghum, pearl millet, African rice, yams, coffee, okra, watermelon and teff all come from Africa."}]},
  {"title": "The First Towns",
   "visual": HOUSE,
   "html": "<p><b>Göbekli Tepe</b> (southeastern Türkiye), built beginning about 11,500 years ago, has huge carved stone pillars arranged in circles. It was built by people who still mostly gathered and hunted their food, which surprised archaeologists: big shared projects may have come <i>before</i> farming, not only after.</p><p><b>Jericho</b> (in the West Bank, near the Jordan River) had a stone wall and a tall stone tower about 10,000 years ago, built on a spring that still flows today.</p><p><b>Çatalhöyük</b> (central Türkiye), lived in from about 9,100 to 8,000 years ago, may have held several thousand people. Its mud-brick houses were packed together with no streets. People walked across the roofs and climbed down ladders into their homes, which had ovens, platforms for sleeping and working, and wall paintings.</p>",
   "checks": [
    {"t":"text","q":"How did people get into their homes at Çatalhöyük?","a":[{"all":[["roof","ladder","top"]]}],"show":"through a hole in the roof, by ladder","pts":2,"why":"Houses had no front doors on streets; people climbed down ladders through roof openings."},
    {"t":"open","key":"gobekli","q":"Göbekli Tepe was built by people who mostly gathered and hunted. Why did this surprise archaeologists, and what new question did it raise?","min":25,"rows":3,"rubric":["Archaeologists expected big building only after farming","New question: did gathering for building or ceremonies help lead to farming?"],"model":"Archaeologists thought people needed farming and stored food before they could build huge stone monuments. Göbekli Tepe raised a new question: maybe gathering in large groups to build and hold ceremonies helped lead people toward farming."},
    {"t":"open","key":"nostreet","q":"Look at the drawing of Çatalhöyük. Give one advantage and one disadvantage of building houses wall to wall with roof entrances.","min":20,"rows":3,"rubric":["A reasonable advantage (protection, warmth, shared walls save material)","A reasonable disadvantage (fire spreads, hard to carry things, crowded, disease)"],"model":"An advantage is protection: with no doors at ground level, animals and raiders could not easily get in, and shared walls saved mud bricks. A disadvantage is that carrying heavy loads up and down ladders would be hard, and a fire or disease could spread quickly."}]},
  {"title": "Was Farming a Good Trade?",
   "visual": FLOW,
   "html": "<p>Farming produced a <b>surplus</b>. Stored food let more people live in one place, and not everyone had to farm. Some became <b>specialists</b>: potters, toolmakers, builders, traders, religious leaders. Over time this led to towns, trade networks and, eventually, cities and governments.</p><p>But there were costs. Skeletons from many early farming villages show people who were shorter than earlier foragers, with more tooth decay and signs of poor nutrition, because they ate a few crops instead of many wild foods. Living close to animals and to one another spread disease. A single drought or crop disease could cause famine. Some people stored more than others, so differences between rich and poor began to grow.</p>",
   "checks": [
    {"t":"text","q":"What is the word for extra food that can be stored or traded?","a":["surplus","a surplus"],"pts":2,"why":"A surplus made specialization possible."},
    {"t":"open","key":"specialist","q":"Explain why a surplus made it possible for some people to become potters or builders.","min":15,"rows":2,"rubric":["Others produced enough food for them","So they could spend time on other work"],"model":"If farmers grew more food than their families needed, they could trade some to the potter, so the potter did not have to grow food and could spend the day making pots."},
    {"t":"open","key":"health","q":"Give two pieces of evidence that early farmers were sometimes less healthy than foragers, and explain why.","min":25,"rows":3,"rubric":["Two pieces of skeletal or other evidence (height, teeth, disease)","Explains the cause (less varied diet, crowding, animals)"],"model":"Skeletons show many early farmers were shorter and had more tooth decay than foragers. They ate mostly a few starchy crops instead of many wild foods, and living crowded together with animals spread disease."}]}],
 "handson": {
  "title": "Grind It Like the First Farmers",
  "intro": "Early farmers ground grain into flour by hand between two stones. Feel the work for yourself, then do the math.",
  "materials": ["A flat stone or a sturdy cutting board, plus a smooth fist-sized stone (washed) or a mortar and pestle", "1/4 cup of dry whole grain (wheat berries, uncooked rice, popcorn kernels or dried corn, or oats)", "A timer", "A measuring spoon", "A clean towel underneath to catch spills"],
  "steps": [
   "Spread a spoonful of grain on the flat stone. Kneel and push the hand stone back and forth over it, the way people used a grinding stone, called a saddle quern.",
   "Set a timer for 5 minutes and grind. Sift out what is fine enough to call flour and measure it.",
   "Repeat once more and record your total.",
   "Calculate: a family loaf of bread needs about 3 cups of flour. At your rate, how long would it take to grind enough flour for one loaf?",
   "Talk with a parent: who in an early village probably did this work every day, and how might it have shaped their life?"],
  "record": [
   {"t":"open","key":"grind","q":"Record how much flour you made in 10 minutes, then calculate how long it would take to grind 3 cups (48 tablespoons). Show your math.","min":25,"rows":4,"rubric":["Records the amount ground with units","Correctly sets up the rate calculation","Gives an answer in minutes or hours"],"model":"I made 2 tablespoons in 10 minutes, which is 5 minutes per tablespoon. 48 tablespoons × 5 minutes = 240 minutes, or 4 hours for one loaf."},
   {"t":"open","key":"grind2","q":"Archaeologists have found skeletons of early farming women with worn toes, knees and lower backs. Using your experience, explain what might have caused this.","min":25,"rows":3,"rubric":["Connects kneeling and pushing to the injuries","Notes the daily hours of grinding","Uses the skeleton as evidence about daily life"],"model":"Grinding meant kneeling with toes bent and pushing forward with the back and arms for hours every day. After years, this would wear down the toes, knees and lower back, so the skeletons are evidence of how hard daily grinding was."}]},
 "think": {
  "intro": "Make an argument and support it with evidence. Your teacher scores these.",
  "items": [
   {"t":"open","key":"argue","q":"Was the switch to farming a good trade for ordinary people in the first villages? Take a side. Give at least two pieces of evidence for your side and answer one argument from the other side.","min":90,"rows":10,"rubric":["Clear claim","Two pieces of accurate evidence","Responds to a counterargument","Organized paragraph with a conclusion"],"model":"For ordinary people in the first villages, farming was not a good trade at first. Skeletons show farmers were often shorter and had more tooth decay than foragers, because they ate a few crops instead of many wild foods. Farming also meant hours of hard work, like grinding grain on knees every day, and one drought could cause hunger. Some people argue farming was worth it because a surplus let villages grow and specialists like potters appear. That is true for society over thousands of years, but the first farmers paid the cost in their health and work. So farming helped humanity in the long run, but it was a hard deal for the first people who made it."},
   {"t":"open","key":"compare","q":"Compare a day in the life of a forager family and an early farming family. Write at least two similarities and three differences.","min":60,"rows":7,"rubric":["Two accurate similarities","Three accurate differences (food, housing, possessions, work, group size)","Specific details"],"model":"Both families needed water, made stone tools and shared food with their group. Foragers moved with the seasons and carried few belongings, while farmers lived in one place in mud-brick houses with stored grain. Foragers ate many kinds of wild food, but farmers ate mostly a few crops. Farmers worked long hours weeding and grinding, and they lived in larger groups with more chance of disease."}]},
 "exit": [
  {"t":"text","q":"What does domestication mean?","a":[{"all":[["chang","breed","select","choos","tame"],["plant","animal","crop","seed"]]}],"show":"changing plants or animals over generations to be more useful to people","pts":2,"why":"Domestication is changing plants or animals over generations by choosing which to grow or breed."},
  {"t":"num","q":"About how many regions of the world began farming independently, according to this lesson? Type the number.","a":10,"pts":2,"why":"At least ten regions."},
  {"t":"text","q":"Name one crop first domesticated in Africa.","a":["sorghum","pearl millet","millet","african rice","yams","yam","coffee","okra","watermelon","teff","enset"],"show":"sorghum (or pearl millet, coffee, yams, okra, teff)","pts":2,"why":"Africa gave the world sorghum, pearl millet, African rice, yams, coffee, okra, watermelon and teff."},
  {"t":"text","q":"Which early town had houses with no streets, entered through the roof?","a":["catalhoyuk","çatalhöyük","catal huyuk","catalhuyuk","çatalhöyuk"],"show":"Çatalhöyük","pts":2,"why":"Çatalhöyük, in central Türkiye."},
  {"t":"open","key":"exit_cost","q":"Name one benefit and one cost of farming for early villages.","min":12,"rows":2,"rubric":["A real benefit (surplus, specialists, larger groups)","A real cost (poorer diet, disease, hard labor, famine risk, inequality)"],"model":"A benefit was a surplus of stored food that let villages grow. A cost was a less varied diet that made many people shorter and less healthy."}],
 "next": "Week 5: the Unit 1 checkpoint and your museum exhibit project. Then Unit 2 travels to the Nile Valley: Kemet, Nubia and Kush."
}

TEACHER = {
 "standards": [
  "SS.6.W.2.1: Compare the lifestyles of hunter-gatherers with those of settlers of early agricultural communities.",
  "SS.6.W.2.2: Describe how the developments of agriculture and metallurgy related to settlement, population growth, and the emergence of civilization.",
  "SS.6.W.2.3 (preview): Identify the characteristics of civilization.",
  "SS.6.G.2.4 (preview): Explain how the geographical location of ancient civilizations contributed to the culture and politics of those societies.",
  "C3 Framework D2.His.14.6-8: Explain multiple causes and effects of events and developments in the past."],
 "materials": ["The interactive lesson", "A world map or globe", "A flat stone or cutting board, a smooth stone or mortar and pestle, and 1/4 cup of dry grain", "A timer", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 3 Reconnect questions."],
  [5, "Hook", "Read the two families. Ask the student to predict which family was healthier before teaching."],
  [10, "Domestication", "Explain seed selection with wheat and teosinte. If possible, show a picture of teosinte beside an ear of corn."],
  [12, "Many centers", "Find each center on the map. Emphasize independent invention and the African crops the student eats today."],
  [10, "First towns", "Study the Çatalhöyük drawing. Discuss why Göbekli Tepe changed archaeologists' thinking."],
  [12, "Costs and benefits", "Trace the chain of effects. Present the skeletal evidence. Ask the student to take a side and defend it."],
  [5, "Assign", "Assign the grinding activity, Think Deeper and the Exit Check."]],
 "key_questions": ["What evidence do we have for this, and how sure are scientists?", "Who gained from farming, and who paid the costs?", "Why did farming start in so many places at roughly the same era?", "What foods on your table today came from Africa, the Americas or Asia?"],
 "misconceptions": ["Farming was invented once in the Middle East and spread everywhere.", "Farming was an obvious improvement that made everyone healthier.", "Early towns looked like modern towns with streets and stores.", "Africa had no role in early agriculture."],
 "support": ["Provide the crop table as a printed card.", "Give sentence starters for the argument: I believe... One piece of evidence is... Some people argue... However...", "Let the student talk through the argument aloud before writing."],
 "challenge": ["Research the Green Sahara: how did people in the Sahara live when it was grassland about 10,000 to 5,000 years ago, and what happened when it dried?", "Investigate one crop's journey, such as coffee from Ethiopia, and map how it spread around the world."],
 "background": "<p>Archaeologists generally recognize somewhere between about seven and more than a dozen independent or early centers of plant domestication, depending on definitions. The dates in the table are rounded and represent current estimates. Early dates for cattle management at Nabta Playa and Bir Kiseiba (around 9,000 or more years ago) are argued by Fred Wendorf and colleagues and remain debated. Sorghum domestication in eastern Sudan is supported by finds at Adam-Butana sites around 5,000 years ago. Pearl millet domestication in the West African Sahel is dated to about 4,500 years ago. Göbekli Tepe's earliest construction is about 9500 BCE; recent work has found evidence of more permanent occupation than first thought, but its builders did not yet rely on domesticated crops. Çatalhöyük was occupied roughly 7100 to 5950 BCE. The evidence that early farming populations often show reduced stature and increased dental disease comes from bioarchaeological studies across several regions, though patterns vary.</p>",
 "sources": ["Smithsonian National Museum of Natural History: The Origins of Agriculture.", "Çatalhöyük Research Project (catalhoyuk.com).", "German Archaeological Institute (DAI): Göbekli Tepe project.", "Winchell, F. et al. (2017), sorghum domestication evidence from eastern Sudan, African Archaeological Review.", "Manning, K. et al. (2011), 4500-year-old domesticated pearl millet from Mali, Journal of Archaeological Science.", "Larsen, C.S. (2006), The agricultural revolution as environmental catastrophe, Quaternary International."]
}

PRINT = {
 "directions": "Use complete sentences and evidence from the lesson.",
 "items": [
  {"q":"Define domestication and give one plant and one animal example.","a":"Changing plants or animals over generations by choosing which to grow or breed. Examples: wheat, maize; goats, cattle.","lines":2},
  {"q":"List four regions where farming began independently and one crop from each.","a":"For example: Fertile Crescent, wheat; China, rice; Andes, potatoes; Sudan, sorghum.","lines":3},
  {"q":"Name three crops first domesticated in Africa.","a":"For example: sorghum, pearl millet, coffee (also yams, okra, watermelon, teff, African rice).","lines":1},
  {"q":"Describe one feature of Çatalhöyük and one of Göbekli Tepe.","a":"Çatalhöyük: houses packed together, entered through the roof. Göbekli Tepe: huge carved stone pillars built by people who mostly foraged.","lines":2},
  {"q":"Fill in the chain: Farming → ________ → More people → ________ → Trade and rules","a":"Surplus; Specialists","lines":1},
  {"q":"Give two costs of early farming and explain one.","a":"For example: poorer diet (fewer kinds of food), more disease (crowding and animals), hard labor, famine risk, inequality.","lines":3}]
}
