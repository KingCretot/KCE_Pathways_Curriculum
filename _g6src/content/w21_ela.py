ROUTE = ('<svg viewBox="0 0 640 300" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Map of Buck&apos;s journey from the Santa Clara Valley, California, to the Klondike in the Yukon">'
  '<rect width="640" height="300" fill="#eaf2fb"/>'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Buck\'s journey north, fall 1897</text>'
  '<path d="M300 40 L640 40 L640 300 L420 300 L380 260 L340 220 L320 180 L300 140 L280 110 L250 80 L230 60Z" fill="#f4ecd8" stroke="#b9a77a"/>'
  '<path d="M60 40 L230 40 L200 70 L150 80 L100 70 L60 60Z" fill="#f4ecd8" stroke="#b9a77a"/><text x="100" y="58" font-size="10" fill="#5b6676">Alaska</text>'
  '<text x="500" y="90" font-size="12" fill="#5b6676" font-weight="bold">CANADA</text><text x="500" y="250" font-size="12" fill="#5b6676" font-weight="bold">UNITED STATES</text>'
  '<path d="M330 150 L640 150" stroke="#b9a77a" stroke-dasharray="4 3"/>'
  '<path d="M405 280 Q390 230 360 190 Q330 150 300 130 Q270 105 250 82 Q262 68 285 58" fill="none" stroke="#DB2F30" stroke-width="3" stroke-dasharray="7 4"/>'
  + ''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="#0A1F3D"/><text x="{x+tx}" y="{y+ty}" font-weight="bold" fill="#0A1F3D">{n}</text>' for x, y, n, tx, ty in [
    (405, 280, "Santa Clara Valley (Judge Miller\'s place)", -230, 4), (380, 236, "San Francisco", 8, 4), (310, 140, "Seattle", 8, 4), (250, 82, "Skagway and Dyea", -110, 4), (285, 58, "Dawson, Klondike (Yukon)", 8, 4)]) +
  '<text x="190" y="190" font-size="12" fill="#0047BA" font-style="italic">Pacific Ocean</text>'
  '<text x="210" y="110" font-size="10" fill="#5b6676">by steamship</text><text x="300" y="74" font-size="10" fill="#5b6676">over the passes</text>'
  '<text x="630" y="294" text-anchor="end" font-size="9" fill="#5b6676">Schematic map, not to scale.</text></svg>')

OPEN = ("<div class='card' style='border-left-color:#C9A84C'><h3 style='margin-top:0'>From The Call of the Wild, Chapter I: \"Into the Primitive\"</h3><p class='muted' style='margin-top:-6px'>Jack London, 1903 (Project Gutenberg text). ... marks words left out. Read the whole chapter with your family; the full novel is free online.</p>"
        "<p style='font-family:Georgia,serif'>Buck did not read the newspapers, or he would have known that trouble was brewing, not alone for himself, but for every tide-water dog, strong of muscle and with warm, long hair, from Puget Sound to San Diego. Because men, groping in the Arctic darkness, had found a yellow metal, and because steamship and transportation companies were booming the find, thousands of men were rushing into the Northland. These men wanted dogs, and the dogs they wanted were heavy dogs, with strong muscles by which to toil, and furry coats to protect them from the frost.</p>"
        "<p style='font-family:Georgia,serif'>Buck lived at a big house in the sun-kissed Santa Clara Valley. Judge Miller's place, it was called. It stood back from the road, half hidden among the trees, through which glimpses could be caught of the wide cool veranda that ran around its four sides. The house was approached by gravelled driveways which wound about through wide-spreading lawns and under the interlacing boughs of tall poplars. ...</p>"
        "<p style='font-family:Georgia,serif'>And over this great demesne Buck ruled. ... for he was king,—king over all creeping, crawling, flying things of Judge Miller's place, humans included.</p>"
        "<p class='muted' style='font-size:12px'>tide-water: living near the coast. booming: loudly advertising. toil: hard work. veranda: a porch. gravelled: the printed spelling of graveled (both are used). demesne (deh-MAIN): an estate, land belonging to a large house.</p></div>")

CLUB = ("<div class='card' style='border-left-color:#DB2F30'><h3 style='margin-top:0'>Later in Chapter I</h3><p class='muted' style='margin-top:-6px'>After Buck is stolen and shipped north, a man in a red sweater beats him with a club. Parents: the full chapter describes this beating in detail; preview it first.</p>"
        "<p style='font-family:Georgia,serif'>He had learned the lesson, and in all his after life he never forgot it. That club was a revelation. It was his introduction to the reign of primitive law, and he met the introduction halfway. ... the lesson was driven home to Buck: a man with a club was a lawgiver, a master to be obeyed, though not necessarily conciliated.</p>"
        "<p class='muted' style='font-size:12px'>revelation: a surprising discovery. primitive: early, basic, wild. conciliated: won over, made friendly.</p></div>")

LESSON = {
 "unit": "Unit 5: Novel Study",
 "title": "Launching the Novel: Setting and Context",
 "subtitle": "For the next five weeks you will read a complete novel, Jack London's The Call of the Wild (1903), about a dog stolen from a California estate and thrown into the brutal world of the Klondike Gold Rush. This week you explore its setting and the real history behind it.",
 "objectives": [
  "Explain how setting (time, place and social conditions) shapes a story's characters and conflicts.",
  "Describe the historical context of the Klondike Gold Rush, including the Indigenous people who made the first strike.",
  "Analyze how the opening chapter establishes Buck's character through setting and contrast.",
  "Identify point of view and how the narrator gives us Buck's perspective.",
  "Use context clues and the roots prim and civ to understand challenging words."],
 "vocab": [
  ["setting", "When and where a story happens, including its social conditions."],
  ["historical context", "The real events and conditions of the time a story is set or written."],
  ["contrast", "A strong difference between two things placed side by side."],
  ["third-person narrator", "A storyteller outside the story who uses he, she, it and they."],
  ["primitive", "Early, basic or wild; the opposite of civilized in London's novel."],
  ["foreshadowing", "Hints about what will happen later in a story."],
  ["stampede", "In gold-rush history, a sudden rush of people to a new gold strike."]],
 "reconnect": {
  "title": "Unit 4: Argument",
  "intro": "Unit 5 turns from writing arguments to reading a novel, but you'll still use evidence for every claim you make.",
  "items": [
   {"t":"text","q":"In an argumentative essay, the sentence that states the claim is called the ___.","a":[{"all":[["thesis"]],"none":["not"]}],"show":"thesis","pts":2,"why":"Week 19."},
   {"t":"text","q":"Douglass used painful contrasts and irony. What device points out a painful contradiction to make a point?","a":[{"all":[["irony","ironic"]],"none":["not"]}],"show":"irony","pts":2,"why":"Week 17."},
   {"t":"text","q":"Paine compared America to a growing child. What is that kind of comparison called?","a":[{"all":[["analogy"]],"none":["not"]}],"show":"an analogy","pts":2,"why":"Week 18."},
   {"t":"open","key":"rc_evidence","q":"In Unit 4 every claim needed evidence. How might that habit help you when you write about a novel?","min":15,"rows":2,"rubric":["Claims about a novel (character, theme) need quotations or details from the text as evidence"],"model":"When I say something about a character or a theme, I'll need to back it up with a quotation or detail from the novel, just like evidence in an argument."}]},
 "hook": {
  "title": "Gold!",
  "visual": ROUTE,
  "html": "<p>In August 1896, on a creek off the Klondike River in the Yukon, northwestern Canada, three men found gold: <b>Keish (Skookum Jim Mason)</b>, a Tagish man; his nephew <b>Káa Goox (Dawson Charlie)</b>; and his brother-in-law <b>George Carmack</b>, an American married to Keish's sister <b>Shaaw Tláa (Kate Carmack)</b>. When ships carrying miners and their gold reached Seattle and San Francisco in July 1897, newspapers went wild. About 100,000 people set out for the Klondike; only about 30,000 to 40,000 made it.</p><p>Gold seekers needed dogs to haul sleds over snow and ice, and dogs were stolen from all over the West Coast to be sold north. One of those dogs, in a story, was Buck.</p><div class='callout'><b>Big question:</b> How does a setting shape a character?</div>"},
 "learn": [
  {"title": "Meet the Novel and Its Setting",
   "html": "<p><b>Jack London</b> (1876 to 1916) grew up poor in Oakland, California, and worked from childhood: in a cannery, on ships and as an oyster pirate. In 1897, at age 21, he joined the Klondike Gold Rush. He found almost no gold, but he gathered the experiences that made him one of the most famous American writers of his time. <i>The Call of the Wild</i>, published in 1903, became a bestseller.</p><p>The novel's <b>setting</b> changes dramatically: from the warm, comfortable Santa Clara Valley in California to the frozen Yukon in the fall and winter of 1897. As you read, notice how each new setting forces Buck to change.</p><p><b>Point of view:</b> the story has a <b>third-person narrator</b> who can tell us what Buck sees, feels and \"thinks,\" even though he is a dog. London uses this to let readers experience the Klondike through animal eyes.</p>",
   "checks": [
    {"t":"text","q":"In what year does the story begin?","a":["1897"],"show":"1897 (the fall)","pts":2,"why":"\"in the fall of 1897, when the Klondike strike dragged men from all the world into the frozen North.\""},
    {"t":"text","q":"The narrator uses he and Buck, not I. What point of view is this?","a":[{"all":[["third"]],"none":["not","first"]}],"show":"third person","pts":2,"why":"A narrator outside the story."},
    {"t":"open","key":"londonlife","q":"How might Jack London's own life have helped him write this novel? Give two connections.","min":25,"rows":3,"rubric":["He went to the Klondike in 1897 and saw the setting firsthand","His hard, working childhood may connect to struggle and survival"],"model":"London went to the Klondike in 1897 himself, so he knew the cold, the trails and the sled dogs firsthand. He also grew up poor and worked hard jobs as a child, so he understood what it's like to struggle to survive."}]},
  {"title": "Reading Chapter I: Buck the King",
   "html": OPEN + "<p>Notice how London builds Buck's character through his setting. The estate is huge, sunny and orderly. Buck is not a pampered house-dog or a kennel-dog: he swims, hunts, guards the Judge's grandchildren and \"rules\" the whole place. The very first sentence uses <b>foreshadowing</b>: \"trouble was brewing.\"</p><p><b>Roots:</b> <i>prim</i> means first (primitive, primary, prime). <i>Civ</i> means citizen or city (civilized, civic, civilian). The tension between the primitive and the civilized drives the whole novel.</p>",
   "checks": [
    {"t":"open","key":"kingbuck","q":"Find two details from the excerpt that show Buck thinks of himself as a king. Explain what they suggest about his character.","min":30,"rows":3,"rubric":["Two accurate details (\"over this great demesne Buck ruled\"; \"king over all creeping, crawling, flying things ... humans included\"; free to roam the whole estate)","Explains: proud, confident, used to comfort and respect"],"model":"London writes that \"over this great demesne Buck ruled\" and that he was \"king over all creeping, crawling, flying things of Judge Miller's place, humans included.\" These details show Buck is proud and confident, and used to comfort and respect. He has never had to struggle."},
    {"t":"text","q":"The first sentence says \"trouble was brewing.\" Hints like this about what will happen later are called ___.","a":[{"all":[["foreshadow"]],"none":["not"]}],"show":"foreshadowing","pts":2,"why":"It prepares readers for Buck's kidnapping."},
    {"t":"blanks","q":"Use the roots.","sent":"The most important, first-ranked thing is the ___ concern (prim). A person who is not in the military is a ___ (civ).","blanks":[[{"all":[["primary","prime"]],"none":["not"]}],[{"all":[["civilian"]],"none":["not"]}]],"show":"primary; civilian","pts":2,"why":"prim = first; civ = citizen."}]},
  {"title": "The Real Klondike",
   "html": "<p>The <b>historical context</b> explains why Buck is stolen. Stampeders who reached Skagway or Dyea, Alaska, had to haul their supplies over the steep <b>Chilkoot</b> or <b>White Pass</b> trails into Canada. The North-West Mounted Police required each person to bring about a year's worth of supplies, roughly a ton, so many people made dozens of trips up the passes. Dogs that could pull sleds were worth a fortune; a strong dog could sell for hundreds of dollars.</p><p>The Klondike was not empty land. It was the homeland of the <b>Tr'ondëk Hwëch'in</b>, a Hän-speaking First Nation, whose fishing camp at the mouth of the Klondike River was overrun by the rush. Their leader, Chief Isaac, moved his people downriver and worked to protect their culture, songs and traditions. Tlingit packers carried goods over the Chilkoot Pass for pay, and Indigenous guides, packers and suppliers made the stampede possible.</p>",
   "checks": [
    {"t":"text","q":"Which First Nation's homeland was the Klondike?","a":[{"all":[["tr'ondek","trondek","hwech","han"]],"none":["not"]}],"show":"the Tr'ondëk Hwëch'in (Hän-speaking First Nation)","pts":2,"why":"Chief Isaac led them during the rush."},
    {"t":"open","key":"whydogs","q":"Using the historical context, explain why dogs like Buck were stolen and sold north in 1897.","min":25,"rows":3,"rubric":["Thousands of stampeders needed strong dogs to haul heavy supplies over snow","Dogs were worth a lot of money, so people stole and sold them"],"model":"Thousands of gold seekers had to haul a ton of supplies over snow and ice, so they desperately needed big, strong dogs. Dogs sold for hundreds of dollars, so people like Manuel stole dogs and sold them north for profit."},
    {"t":"open","key":"emptyland","q":"Many gold-rush stories describe the Yukon as an empty wilderness. Why is that description inaccurate, and why does it matter?","min":25,"rows":3,"rubric":["It was the homeland of the Tr'ondëk Hwëch'in and other First Nations; Indigenous people made the first strike","Matters: erasing Indigenous people hides their history and the harm the rush caused"],"model":"The Yukon was the homeland of the Tr'ondëk Hwëch'in and other First Nations, and a Tagish man, Keish, was one of the people who made the first strike. Calling it empty erases the people who lived there and hides how the rush took over their fishing camp and land."}]},
  {"title": "Setting Shapes Character",
   "html": CLUB + "<p>In just one chapter, Buck's world changes completely: from king of a sunny estate to a crate on a train, then to a yard where a man with a club teaches him a brutal lesson. London calls it Buck's \"introduction to the reign of primitive law.\" This is the first of many changes in Buck. Watch how each new setting teaches him something new about survival.</p>",
   "checks": [
    {"t":"open","key":"clublesson","q":"What lesson does Buck learn from the man in the red sweater? Quote a phrase, and explain how this lesson is the opposite of Buck's life at Judge Miller's.","min":35,"rows":3,"rubric":["Lesson: a man with a club must be obeyed; might makes right (primitive law)","Quoted phrase","Contrast: at Judge Miller's he ruled and was respected; now he is ruled by force"],"model":"Buck learns that \"a man with a club was a lawgiver, a master to be obeyed.\" At Judge Miller's place, Buck was a king who ruled freely and was respected. Now he must obey whoever holds power, which is the opposite of the comfortable, orderly world he came from."},
    {"t":"open","key":"predict","q":"Based on Chapter I, predict how Buck might change as the story continues. Use one detail from the text to support your prediction.","min":25,"rows":3,"rubric":["A reasonable prediction about change","Supported by a detail (he met the lesson \"halfway,\" \"latent cunning ... aroused,\" foreshadowing)"],"model":"I predict Buck will become tougher and more cunning. The text says he met the lesson \"halfway\" and that \"all the latent cunning of his nature\" was \"aroused,\" which suggests wild instincts are waking up inside him."}]}],
 "handson": {
  "title": "Gold Rush Packing Challenge and Setting Map",
  "intro": "Find out what a stampeder had to carry, then build a setting map you will add to all unit long.",
  "materials": ["A large sheet of paper or poster board", "Markers or colored pencils", "A bathroom scale", "Household items to pack (canned food, a bag of rice or flour, blankets, a pot)", "A backpack or box", "Paper and pencil", "A copy of The Call of the Wild (free online or from the library)"],
  "steps": [
   "Packing challenge: the Mounted Police required about a year's supplies, roughly 1,000 pounds of food plus gear, about a ton in all. Pack a backpack or box with household items until it weighs about 25 pounds. Carry it up and down a flight of stairs or across a room 5 times.",
   "Calculate: if a stampeder could carry about 50 pounds per trip, how many trips would it take to move 2,000 pounds over the pass?",
   "Setting map: draw a large map of Buck's journey: Santa Clara Valley, San Francisco, Seattle, Skagway and Dyea, the passes and Dawson. Leave space to add places as you read.",
   "Add three quotations from Chapter I that describe the California setting.",
   "Lift with your legs, keep loads light enough to carry safely, and take breaks."],
  "record": [
   {"t":"open","key":"packrec","q":"How did carrying 25 pounds feel after 5 trips? Show your calculation for moving 2,000 pounds at 50 pounds per trip. How does this help explain why dogs were so valuable?","min":40,"rows":4,"rubric":["Describes the experience","2,000 ÷ 50 = 40 trips","Connects to dogs' value: dogs could haul heavy loads, saving many trips"],"model":"By the fifth trip my legs were burning and I was breathing hard. 2,000 ÷ 50 = 40 trips over the pass, and each trip was miles of steep, icy trail. A team of dogs could pull hundreds of pounds on a sled, saving dozens of trips, so dogs were worth a fortune."},
   {"t":"open","key":"maprec","q":"List the places on your setting map and the three California quotations you added. Which quotation best shows the contrast with the North?","min":30,"rows":4,"rubric":["Places listed","Three accurate quotations","A choice with reasoning about contrast"],"model":"Places: Santa Clara Valley, San Francisco, Seattle, Skagway, Dyea, Chilkoot Pass, Dawson. Quotations: \"sun-kissed Santa Clara Valley,\" \"wide cool veranda,\" \"wide-spreading lawns.\" \"Sun-kissed\" shows the contrast best, because the North is described as \"Arctic darkness\" and \"frost.\""}]},
 "think": {
  "intro": "Use evidence from the text. Your teacher scores these.",
  "items": [
   {"t":"open","key":"settingessay","q":"Explain how Jack London uses setting in Chapter I to show who Buck is at the start of the novel and to prepare readers for change. Use at least two quotations.","min":96,"rows":8,"rubric":["A clear claim about setting and character","Two accurate quotations","Explains the contrast between California and the club yard or the North","Mentions foreshadowing or the coming change"],"model":"London uses the California setting to show Buck as a comfortable, proud ruler, and then breaks that setting apart to show that Buck's life is about to change. Buck lives in the \"sun-kissed Santa Clara Valley\" on a huge estate where \"over this great demesne Buck ruled.\" The warm, orderly place matches his confident, royal personality. But from the first sentence London warns that \"trouble was brewing,\" and by the end of the chapter, the man in the red sweater has taught Buck that \"a man with a club was a lawgiver.\" The shift from sunlit lawns to a brutal yard shows that Buck will have to become a very different dog to survive."},
   {"t":"open","key":"indigenousview","q":"Imagine you are a member of the Tr'ondëk Hwëch'in in 1898, watching tens of thousands of stampeders arrive at your fishing camp. Write a short journal entry (in your own words) about what you see and how it affects your community. Base it on facts from the lesson.","min":80,"rows":6,"rubric":["Accurate facts (fishing camp overrun, Chief Isaac moving the people downriver, thousands of newcomers)","A thoughtful, respectful perspective","Clear writing"],"model":"Summer, 1898. Boats and rafts keep coming down the river, more people than I can count. They have built tents and shacks all over the place where we dried our salmon every summer. Chief Isaac says we will move our camp downriver to Moosehide, where we can keep our families together. The newcomers only talk about gold. They don't know this land or the songs our grandparents taught us here. I worry about the animals and the fish with so many people. But we will keep our songs and our ways, and we will remember."}]},
 "exit": [
  {"t":"text","q":"Where does Buck live at the start of the novel? (Name the valley.)","a":[{"all":[["santa clara"]],"none":["not"]}],"show":"the Santa Clara Valley, California","pts":2,"why":"At Judge Miller's place."},
  {"t":"text","q":"What metal causes the rush to the Northland?","a":[{"all":[["gold"]],"none":["not"]}],"show":"gold","pts":2,"why":"\"a yellow metal.\""},
  {"t":"text","q":"The root prim means ___.","a":[{"all":[["first"]],"none":["not"]}],"show":"first","pts":2,"why":"primitive, primary."},
  {"t":"open","key":"exit_setting","q":"Why does a writer's choice of setting matter? Use Buck as an example.","min":15,"rows":2,"rubric":["Setting shapes what characters must face and how they change","Buck's change from California comfort to the brutal North"],"model":"The setting decides what problems a character faces. Buck was a proud king in sunny California, but in the harsh North he will have to change to survive."}],
 "next": "Week 22: conflict and character change as Buck learns the law of club and fang."
}

TEACHER = {
 "standards": [
  "ELA.6.R.1.1: Explain how the setting impacts conflict and characterization in a literary text.",
  "ELA.6.R.1.2: Analyze the development of stated or implied theme(s) throughout a literary text.",
  "ELA.6.R.1.3: Explain the influence of narrator(s) and point of view on a literary text.",
  "ELA.6.V.1.3: Apply knowledge of context clues, figurative language, word relationships, reference materials, and/or background knowledge to determine and clarify the meaning of multiple-meaning and unknown words and phrases, appropriate to grade level.",
  "ELA.6.V.1.2: Apply knowledge of Greek and Latin roots and affixes to determine meanings of words and phrases in grade-level content.",
  "ELA.K12.EE.1.1: Cite evidence to explain and justify reasoning."],
 "materials": ["The interactive lesson", "The Call of the Wild (Project Gutenberg or library)", "Poster board, markers, a bathroom scale, household items, a backpack or box", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Unit 4 warm-up questions."],
  [6, "Hook", "The Klondike strike: Keish, Káa Goox, Shaaw Tláa and George Carmack; trace the route map."],
  [9, "Meet the novel", "Jack London's life; setting and point of view."],
  [12, "Chapter I", "Read the opening aloud; find details of Buck as king; foreshadowing; roots."],
  [10, "Real Klondike", "Chilkoot Pass, the ton of goods, the Tr'ondëk Hwëch'in and Chief Isaac."],
  [11, "Setting shapes character", "Read the club passage; discuss the lesson and the contrast."],
  [6, "Assign", "Assign Chapter I reading, the packing challenge and map, Think Deeper and the Exit Check."]],
 "key_questions": ["How does this setting shape what Buck feels and does?", "What does the narrator let us know that a dog couldn't say?", "Whose land was the Klondike?", "What clues hint at what will happen next?"],
 "misconceptions": ["Setting is just background.", "The Yukon was empty land.", "Only white miners found and dug gold.", "A dog story is a simple children's story."],
 "support": ["Read Chapter I aloud together, or use a free audiobook (LibriVox).", "Keep a character chart for Buck and a setting map.", "Pre-teach demesne, veranda, primitive."],
 "challenge": ["Read the Tr'ondëk Hwëch'in's own account of the gold rush on their First Nation's website (with a parent).", "Compare London's description of Buck with a photo of a St. Bernard and a Scotch shepherd (collie)."],
 "background": "<p><b>Content note:</b> The Call of the Wild contains frequent violence against dogs (beatings, dogfights, deaths), period racial and ethnic labels, and a stereotyped portrayal of an Indigenous people (the fictional \"Yeehats\") in Chapter VII. KCE chose the novel for its strong setting, character change and themes, and will teach the portrayal critically in Week 24. Parents should preview chapters. The lesson's discovery details follow Yukon government and Parks Canada sources: gold was found on Rabbit (later Bonanza) Creek on August 16 or 17, 1896, by Keish (Skookum Jim Mason), Káa Goox (Dawson Charlie) and George Carmack, with Shaaw Tláa (Kate Carmack) present; accounts differ on who found the first gold. The ships Excelsior and Portland reached San Francisco and Seattle in July 1897. Estimates: about 100,000 set out, about 30,000 to 40,000 reached Dawson. The North-West Mounted Police \"ton of goods\" rule was in force from 1898. Chief Isaac moved the Tr'ondëk Hwëch'in to Moosehide in 1897. The Gutenberg text spells \"gravelled\"; it is kept as printed.</p>",
 "sources": ["Jack London, The Call of the Wild (1903), Project Gutenberg.", "Parks Canada, Chilkoot Trail National Historic Site and Dawson Historical Complex.", "Tr'ondëk Hwëch'in First Nation, history.", "National Park Service, Klondike Gold Rush National Historical Park."]
}

PRINT = {
 "directions": "Answer in complete sentences, citing the novel where asked.",
 "items": [
  {"q":"Describe the setting at the start of the novel: time, place and Buck's life.","a":"Fall 1897, Judge Miller's estate in the Santa Clara Valley, California; Buck rules the estate as a proud, respected dog.","lines":3},
  {"q":"Who made the first Klondike gold strike in 1896?","a":"Keish (Skookum Jim Mason), Káa Goox (Dawson Charlie) and George Carmack, with Shaaw Tláa (Kate Carmack).","lines":2},
  {"q":"Why were dogs like Buck stolen and sold north?","a":"Stampeders needed strong dogs to haul supplies over snow; dogs were worth a lot of money.","lines":2},
  {"q":"Quote and explain the lesson Buck learns from the man in the red sweater.","a":"\"A man with a club was a lawgiver, a master to be obeyed\": force rules in this new world.","lines":3},
  {"q":"What is foreshadowing? Give the example from the first sentence.","a":"Hints about later events; \"trouble was brewing.\"","lines":2},
  {"q":"Use the roots: what do primitive and civilized have to do with prim and civ?","a":"Primitive: early, first, wild (prim = first); civilized: of cities and citizens (civ).","lines":2}]
}
