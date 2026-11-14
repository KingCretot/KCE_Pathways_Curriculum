WEB = ('<svg viewBox="0 0 660 330" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="An Everglades food web with arrows showing the direction energy flows">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">An Everglades food web (arrows point the way energy flows)</text>'
  '<defs><marker id="fw" viewBox="0 0 10 10" markerWidth="6" markerHeight="6" refX="9" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="#5b6676"/></marker></defs>'
  + ''.join(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#8a95a5" stroke-width="1.6" marker-end="url(#fw)"/>' for x1, y1, x2, y2 in [
    (110, 285, 140, 215), (110, 285, 260, 225), (250, 285, 260, 225), (250, 285, 390, 225), (400, 285, 390, 225), (400, 285, 520, 220),
    (150, 200, 210, 140), (270, 210, 220, 140), (270, 210, 340, 140), (390, 210, 340, 140), (520, 205, 470, 140), (390, 210, 470, 140),
    (220, 125, 280, 70), (340, 125, 300, 70), (470, 125, 420, 70), (150, 185, 395, 70)]) +
  ''.join(f'<rect x="{x-55}" y="{y-15}" width="110" height="30" rx="8" fill="{c}"/><text x="{x}" y="{y+4}" text-anchor="middle" fill="#fff" font-weight="bold" font-size="11">{n}</text>' for x, y, n, c in [
    (110, 300, "sawgrass", "#2c6e22"), (250, 300, "algae", "#2c6e22"), (400, 300, "periphyton", "#2c6e22"),
    (140, 200, "marsh rabbit", "#8a6d1f"), (270, 210, "apple snail", "#8a6d1f"), (390, 210, "mosquitofish", "#8a6d1f"), (520, 205, "crayfish", "#8a6d1f"),
    (220, 125, "snail kite", "#0047BA"), (340, 125, "largemouth bass", "#0047BA"), (470, 125, "great egret", "#0047BA"),
    (290, 55, "alligator", "#DB2F30"), (410, 55, "Florida panther", "#DB2F30")]) +
  '<text x="600" y="300" font-size="10" fill="#2c6e22" font-weight="bold">producers</text><text x="600" y="210" font-size="10" fill="#8a6d1f" font-weight="bold">primary</text><text x="600" y="222" font-size="10" fill="#8a6d1f" font-weight="bold">consumers</text><text x="585" y="122" font-size="10" fill="#0047BA" font-weight="bold">secondary</text><text x="585" y="134" font-size="10" fill="#0047BA" font-weight="bold">consumers</text><text x="510" y="58" font-size="10" fill="#DB2F30" font-weight="bold">top predators</text>'
  '<text x="330" y="326" text-anchor="middle" font-size="10" fill="#5b6676">Simplified. Decomposers (bacteria, fungi) break down every organism here when it dies. Panthers eat marsh rabbits and many other animals.</text></svg>')

PYR = ('<svg viewBox="0 0 660 260" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Energy pyramid showing that only about 10 percent of energy passes to each higher level">'
  '<text x="280" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The energy pyramid: about 10% moves up each level</text>'
  '<path d="M60 230 L500 230 L440 180 L120 180Z" fill="#2c6e22"/><text x="280" y="210" text-anchor="middle" fill="#fff" font-weight="bold">producers: 10,000 units of energy</text>'
  '<path d="M120 178 L440 178 L380 128 L180 128Z" fill="#8a6d1f"/><text x="280" y="158" text-anchor="middle" fill="#fff" font-weight="bold">primary consumers: 1,000</text>'
  '<path d="M180 126 L380 126 L330 80 L230 80Z" fill="#0047BA"/><text x="280" y="108" text-anchor="middle" fill="#fff" font-weight="bold">secondary: 100</text>'
  '<path d="M230 78 L330 78 L280 36Z" fill="#DB2F30"/><text x="280" y="68" text-anchor="middle" fill="#fff" font-weight="bold" font-size="11">top: 10</text>'
  '<text x="510" y="140" font-size="11" fill="#5b6676">The other 90%</text><text x="510" y="154" font-size="11" fill="#5b6676">at each level</text><text x="510" y="168" font-size="11" fill="#5b6676">is used for life</text><text x="510" y="182" font-size="11" fill="#5b6676">or lost as heat.</text>'
  '<text x="280" y="252" text-anchor="middle" font-size="10" fill="#5b6676">The 10% figure is an average rule of thumb; real transfers range from about 5 to 20 percent.</text></svg>')

LESSON = {
 "unit": "Unit 5: Ecosystems",
 "title": "Food Chains, Food Webs and Energy",
 "subtitle": "Almost every living thing on Earth runs on sunlight, captured by plants and passed along through who eats whom. This week you trace energy through an Everglades food web, discover why there are so few top predators, and see how a poison can build up from the bottom of the web to the top.",
 "objectives": [
  "Classify organisms as producers, consumers (herbivores, carnivores, omnivores) and decomposers.",
  "Construct food chains and food webs that show the direction of energy flow.",
  "Explain why only about 10 percent of energy passes from one level to the next, using an energy pyramid.",
  "Predict how removing or adding a species affects a food web.",
  "Explain biomagnification using the example of mercury in the Everglades."],
 "vocab": [
  ["producer", "An organism that makes its own food, usually by photosynthesis."],
  ["consumer", "An organism that gets energy by eating other organisms."],
  ["decomposer", "An organism, such as a fungus or bacterium, that breaks down dead matter and returns nutrients to the soil and water."],
  ["food chain", "A single path showing how energy passes from one organism to another."],
  ["food web", "Many connected food chains in an ecosystem."],
  ["trophic level", "A feeding level in a food chain, such as producers or primary consumers."],
  ["biomagnification", "The buildup of a toxin in organisms at higher levels of a food chain."]],
 "reconnect": {
  "title": "Week 21: Living and nonliving parts of an ecosystem",
  "intro": "Last week you met the parts of an ecosystem. This week they start eating each other.",
  "items": [
   {"t":"text","q":"Is sunlight a biotic or abiotic factor?","a":[{"all":[["abiotic"]],"none":["not abiotic"]}],"show":"abiotic","pts":2,"why":"Today: the energy source for almost every food web."},
   {"t":"text","q":"All the populations living together in an area form a ___.","a":[{"all":[["community"]],"none":["not","population"]}],"show":"community","pts":2,"why":"A food web maps the feeding links in a community."},
   {"t":"text","q":"In Unit 2 you learned the process plants use to make sugar from sunlight, water and carbon dioxide. What is it called?","a":[{"all":[["photosynthes"]],"none":["not"]}],"show":"photosynthesis","pts":2,"why":"It starts every food chain in this lesson."},
   {"t":"open","key":"rc_limit","q":"Last week you learned about limiting factors. How could food act as a limiting factor for alligators in the Everglades?","min":12,"rows":2,"rubric":["If prey (fish, turtles, birds) is scarce, alligators can't all get enough to eat, so their population can't grow"],"model":"If there aren't enough fish, turtles and birds to eat, not all alligators can get enough food, so their population stops growing."}]},
 "hook": {
  "title": "The Poisoned Panther",
  "visual": WEB,
  "html": "<p>In 1989, scientists found a dead Florida panther in the Everglades with extremely high levels of <b>mercury</b>, a toxic metal, in its body. The panther hadn't eaten anything poisonous on purpose. The mercury had started out in tiny amounts in the water, from sources such as burning trash and coal, and was taken up by algae and tiny organisms. Fish ate those, raccoons and alligators ate the fish, and panthers ate the raccoons. At every step, the mercury became more concentrated.</p><p>To understand how a poison can climb a food web, you first need to understand how <b>energy</b> moves through it.</p><div class='callout'><b>Big question:</b> How does energy move through an ecosystem, and what else moves with it?</div>"},
 "learn": [
  {"title": "Producers, Consumers and Decomposers",
   "html": "<ul><li><b>Producers</b> make their own food. Sawgrass, cypress trees, algae and periphyton (the spongy mats of algae and microbes in Everglades water) capture sunlight through photosynthesis.</li><li><b>Consumers</b> eat other organisms. <i>Herbivores</i> eat plants (marsh rabbits, apple snails). <i>Carnivores</i> eat animals (snail kites, bass, panthers). <i>Omnivores</i> eat both (raccoons, many turtles, humans).</li><li><b>Decomposers</b> such as bacteria and fungi break down dead organisms and wastes, returning nutrients to the soil and water so producers can use them again.</li></ul><p>The <b>snail kite</b>, an endangered Everglades hawk, eats almost nothing but apple snails. Its curved beak is shaped to pull snails out of their shells, a great example of structure fitting function.</p>",
   "checks": [
    {"t":"blanks","q":"Classify each organism.","sent":"Sawgrass: ___ &nbsp; Marsh rabbit (eats plants): ___ &nbsp; Raccoon (eats crayfish and berries): ___ &nbsp; Mushroom on a rotting log: ___","blanks":[[{"all":[["producer"]],"none":["not"]}],[{"all":[["herbivore","primary consumer","consumer"]],"none":["not"]}],[{"all":[["omnivore"]],"none":["not"]}],[{"all":[["decomposer"]],"none":["not"]}]],"show":"producer; herbivore; omnivore; decomposer","pts":4,"why":"Mushrooms are fungi that break down dead matter."},
    {"t":"open","key":"nodecomposers","q":"Predict what would happen to an ecosystem if all its decomposers disappeared.","min":25,"rows":3,"rubric":["Dead organisms and waste would pile up","Nutrients would stay locked up, so producers couldn't get them; eventually the whole web would suffer"],"model":"Dead plants and animals would pile up without rotting. The nutrients in them would stay locked away instead of returning to the soil and water, so producers couldn't grow well, and everything that depends on producers would suffer too."}]},
  {"title": "Food Chains and Food Webs",
   "html": "<p>A <b>food chain</b> shows one path energy takes: <i>algae → mosquitofish → largemouth bass → alligator</i>. The arrows point from the food to the eater, the direction <b>energy flows</b>.</p><p>Real ecosystems are <b>food webs</b>: many chains linked together, because most animals eat more than one thing and are eaten by more than one predator. Each feeding step is a <b>trophic level</b>: producers, primary consumers, secondary consumers, tertiary consumers.</p>",
   "checks": [
    {"t":"order","q":"Put this Everglades food chain in order, starting with the producer.","items":["periphyton","apple snail","snail kite"],"pts":2,"why":"Energy flows from the producer to the herbivore to the carnivore."},
    {"t":"text","q":"In a food chain diagram, the arrow points from the food toward the ___.","a":[{"all":[["eater","consumer","predator","organism that eats"]],"none":["not"]}],"show":"the eater (the consumer)","pts":2,"why":"Arrows show the direction energy flows."},
    {"t":"open","key":"snailkite","q":"Use the food web. Snail kites eat almost only apple snails. Why is the snail kite more at risk than the great egret if a drought dries up the marsh?","min":29,"rows":3,"rubric":["Drought reduces apple snails","Snail kites depend on one food source; egrets eat many kinds of prey, so they can switch"],"model":"A drought would kill off many apple snails. Since snail kites eat almost nothing else, they would starve. Great egrets eat many kinds of fish, crayfish and frogs, so they can switch to other food."}]},
  {"title": "Energy Pyramids: The 10 Percent Rule",
   "visual": PYR,
   "html": "<p>At each step in a food chain, only about <b>10 percent</b> of the energy is passed on. The rest is used by the organism to live, move and grow, or lost as heat. (You saw this in Unit 4: your body burns food energy to keep warm and move.)</p><p>That's why an energy pyramid gets narrower at the top, and why ecosystems have many more producers than herbivores, and only a few top predators. A Florida panther needs a home range of roughly 200 square miles for a male to find enough prey.</p>",
   "checks": [
    {"t":"num","q":"Producers in a pond capture 50,000 units of energy. Using the 10% rule, about how many units reach the secondary consumers?","a":500,"unit":"units","pts":2,"why":"50,000 → 5,000 (primary) → 500 (secondary)."},
    {"t":"open","key":"fewpredators","q":"Explain, using the energy pyramid, why there are far fewer alligators than mosquitofish in the Everglades.","min":25,"rows":3,"rubric":["Only about 10% of energy passes to each higher level","Less energy at the top supports fewer organisms; alligators are several levels above mosquitofish"],"model":"Only about 10 percent of the energy at each level moves up to the next. Alligators are higher up the pyramid than mosquitofish, so much less energy reaches them, and that smaller amount can only support a few alligators."}]},
  {"title": "Changes in the Web and Biomagnification",
   "html": "<p>Because everything is connected, a change to one species ripples through the web. When <b>Burmese pythons</b>, released pets from Asia, spread through the Everglades, surveys in some areas found raccoon, opossum and marsh rabbit sightings dropped by about 90 percent or more. Predators that ate those mammals lost food, and plants and insects those mammals ate changed too.</p><p><b>Biomagnification</b> works the opposite way from energy. A toxin like mercury is not used up or lost as heat; it stays stored in the body. Each predator eats many prey, collecting all their mercury, so concentrations grow at each level, and top predators like panthers, alligators and large fish carry the most. That is why Florida issues fish-eating advisories for some large fish in some lakes.</p>",
   "checks": [
    {"t":"open","key":"pythonripple","q":"Burmese pythons eat marsh rabbits and raccoons. Use the food web to predict two ripple effects of pythons spreading through the Everglades.","min":28,"rows":3,"rubric":["Prey mammals decline","Two ripple effects (native predators like panthers lose food; plants or prey that mammals ate could increase or change; competition with alligators)"],"model":"With fewer marsh rabbits and raccoons, Florida panthers would have less food and might struggle. Also, the things raccoons eat, like crayfish and turtle eggs, might increase because fewer raccoons are eating them."},
    {"t":"open","key":"biomagwhy","q":"Why does mercury become more concentrated at higher levels of a food chain, while energy becomes less?","min":30,"rows":3,"rubric":["Explains what happens to energy at each level","Explains why mercury builds up instead"],"model":"Energy gets used up and lost as heat at each step, so less moves up. Mercury isn't used up; it stays stored in the body. Each predator eats many prey and keeps all of their mercury, so it piles up higher in the chain."}]}],
 "handson": {
  "title": "Yarn Food Web and Energy Cups",
  "intro": "Build a living food web with family and yarn, then model the 10 percent rule with water.",
  "materials": ["A ball of yarn or string", "Index cards and a marker", "Tape or safety pins", "5 clear cups of the same size", "A measuring cup and water", "A dropper or teaspoon", "Family members (3 or more is best)", "Paper and pencil"],
  "steps": [
   "Write one Everglades organism on each card (sun, sawgrass, algae, apple snail, mosquitofish, marsh rabbit, snail kite, bass, egret, alligator, panther, decomposers). Each person wears one or more cards.",
   "Start with the sun holding the yarn. Pass the ball to an organism that gets energy from the sun, holding on to your end. Keep passing along feeding links until everyone is connected in a web.",
   "Have one organism (say, the apple snail) tug its strings. Everyone who feels the tug is affected. Then have the apple snail drop its strings (it disappears). Who loses a connection?",
   "Energy cups: fill cup 1 with 1,000 mL of water (or as much as your cup holds) as the producers. Pour 10% into cup 2 (100 mL), then 10% of that into cup 3 (10 mL), then 10% into cup 4 (1 mL, a dropper or a few drops). Compare the cups.",
   "Wipe up spills right away so no one slips."],
  "record": [
   {"t":"open","key":"yarnrec","q":"Describe your yarn web. When one organism disappeared, which organisms lost connections, and what does that show about food webs?","min":40,"rows":4,"rubric":["Describes the web and the removed organism","Names affected organisms correctly","Explains interdependence: one change affects many"],"model":"The sun connected to sawgrass and algae, which connected to snails, rabbits and fish, then up to kites, egrets, alligators and the panther. When the apple snail dropped out, the snail kite lost its only connection, and the algae lost an eater. It showed that one missing species can affect many others."},
   {"t":"open","key":"cuprec","q":"Record how much water was in each cup. How does the model show the 10 percent rule, and why would a food chain rarely have more than four or five levels?","min":30,"rows":3,"rubric":["Amounts: 1,000, 100, 10, 1 mL (or proportional)","Explains that energy shrinks quickly, so there isn't enough left to support more levels"],"model":"Cup 1 had 1,000 mL, cup 2 had 100, cup 3 had 10 and cup 4 had just 1 mL, a few drops. The energy shrinks so fast that by the fifth level there would be almost nothing left, so there isn't enough energy to support many levels."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"eatlower","q":"Some people say that eating lower on the food chain (more plants, less meat) uses less of the Earth's energy and land. Use the 10 percent rule to explain the reasoning behind this claim. Then name one thing the rule alone doesn't tell us about people's food choices.","min":68,"rows":6,"rubric":["Explains: about 90% of energy is lost at each level, so feeding animals plants to eat the animals uses more plant energy and land than eating plants directly","Names a limit (nutrition needs, culture and tradition, land not suited to crops, health, cost, personal choice)","Even-handed tone"],"model":"Each step up the food chain loses about 90 percent of the energy. So if cows eat 100 units of plant energy, people who eat the beef get only about 10 units. Eating plants directly gets much more of the original energy, so it can take less land to feed people. But the rule doesn't tell us everything: people need certain nutrients, some land can only grow grass for grazing, and food is tied to culture, health and family traditions."},
   {"t":"open","key":"mercuryadvice","q":"Florida advises people to limit how often they eat some large fish, like largemouth bass from certain lakes, but not small fish like sunfish. Explain why, using biomagnification.","min":46,"rows":5,"rubric":["Bass are higher in the food chain (they eat smaller fish)","Mercury builds up at each level, so bass carry more mercury than small fish","Eating fish high in mercury too often could harm health"],"model":"Largemouth bass are predators that eat many smaller fish, which ate even smaller organisms. Mercury builds up at every level, so a big bass can carry much more mercury than a small sunfish lower in the chain. Eating high-mercury fish too often could harm a person's health, so the advice is to eat them less."}]},
 "exit": [
  {"t":"text","q":"What do we call an organism that makes its own food?","a":[{"all":[["producer"]],"none":["not"]}],"show":"a producer","pts":2,"why":"Usually by photosynthesis."},
  {"t":"num","q":"If producers have 20,000 units of energy, about how many reach primary consumers?","a":2000,"unit":"units","pts":2,"why":"10% of 20,000."},
  {"t":"text","q":"What is the buildup of a toxin at higher levels of a food chain called?","a":[{"all":[["biomagnif","bioaccumul"]],"none":["not"]}],"show":"biomagnification","pts":2,"why":"Like mercury in Everglades panthers."},
  {"t":"open","key":"exit_web","q":"Why is a food web a better model of an ecosystem than a single food chain?","min":12,"rows":2,"rubric":["Most organisms eat and are eaten by more than one thing; a web shows all those connections"],"model":"Most animals eat several kinds of food and are eaten by several predators, so a web shows all those connections, while a chain shows only one."}],
 "next": "Week 23: cycles of matter, water and carbon."
}

TEACHER = {
 "standards": [
  "SC.7.L.17.1: Explain and illustrate the roles of and relationships among producers, consumers, and decomposers in the process of energy transfer in a food web.",
  "SC.7.L.17.3: Describe and investigate various limiting factors in the local ecosystem and their impact on native populations, including food, shelter, water, space, disease, parasitism, predation, and nesting sites.",
  "SC.8.L.18.4: Cite evidence that living systems follow the Laws of Conservation of Mass and Energy (preview).",
  "NGSS MS-LS2-3: Develop a model to describe the cycling of matter and flow of energy among living and nonliving parts of an ecosystem."],
 "materials": ["The interactive lesson", "A ball of yarn, index cards, a marker, tape or safety pins", "5 clear cups, a measuring cup, water, a dropper", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 21 warm-up questions."],
  [5, "Hook", "The 1989 mercury panther."],
  [10, "Producers, consumers, decomposers", "Classify organisms; the snail kite's beak."],
  [11, "Food chains and webs", "Trace arrows on the Everglades web; trophic levels."],
  [11, "Energy pyramid", "The 10% rule; why few top predators; panther home ranges."],
  [11, "Changes and biomagnification", "Burmese pythons; mercury and fish advisories."],
  [6, "Assign", "Build the yarn web; assign the energy cups, Think Deeper and the Exit Check."]],
 "key_questions": ["Where does this organism get its energy?", "Which way does the arrow point, and why?", "Where did the other 90 percent go?", "What happens if this species disappears?"],
 "misconceptions": ["Arrows point from the eater to the food.", "Energy is recycled like matter.", "Top predators have the most energy.", "Decomposers aren't important."],
 "support": ["Color-code trophic levels on the food web.", "Use the phrase \"arrow means 'is eaten by' / 'gives energy to.'\"", "Pre-fill some yarn-web cards."],
 "challenge": ["Research the snail kite's recovery and how it has adapted to eating invasive island apple snails.", "Calculate how much producer energy is needed to support one panther, using the 10% rule over four levels."],
 "background": "<p>Florida NGSSS places food webs in Grade 7 (SC.7.L.17.1); KCE teaches them here per the Grade 6 scope. The first Florida panther documented to have died of mercury poisoning was found in 1989 in the Everglades (Florida Fish and Wildlife Conservation Commission; Roelke and others). Dorcas and colleagues (2012, PNAS) reported declines of 99 percent in raccoon sightings, 98 percent in opossums and 87 percent in bobcats in road surveys in Everglades National Park, with marsh rabbits and foxes effectively disappearing from surveys; the lesson rounds to \"about 90 percent or more.\" Male panther home ranges average roughly 200 square miles. The 10 percent figure is a commonly used average (Lindeman, 1942); real ecological efficiencies vary. Fish consumption advisories: Florida Department of Health.</p>",
 "sources": ["Florida Fish and Wildlife Conservation Commission, Florida Panther and Burmese Python pages.", "Dorcas, M. E., et al. (2012), Severe mammal declines coincide with proliferation of invasive Burmese pythons in Everglades National Park, PNAS 109(7).", "Florida Department of Health, Fish Consumption Advisories.", "National Park Service, Everglades food web resources."]
}

PRINT = {
 "directions": "Answer in complete sentences.",
 "items": [
  {"q":"Define producer, consumer and decomposer, with an Everglades example of each.","a":"Producer: makes food (sawgrass). Consumer: eats others (alligator). Decomposer: breaks down dead matter (fungi, bacteria).","lines":3},
  {"q":"Write a four-step Everglades food chain with arrows.","a":"algae → mosquitofish → largemouth bass → alligator.","lines":1},
  {"q":"Producers capture 30,000 units of energy. How much reaches the tertiary consumers?","a":"30,000 → 3,000 → 300 → 30 units.","lines":2},
  {"q":"Why do food chains rarely have more than four or five levels?","a":"Only about 10% of energy moves up each level, so too little remains to support more levels.","lines":2},
  {"q":"Explain biomagnification using mercury and panthers.","a":"Mercury is stored, not used; each predator collects mercury from many prey; it builds up to high levels in panthers.","lines":3},
  {"q":"Predict one effect of Burmese pythons on the Everglades food web.","a":"Fewer raccoons and marsh rabbits; panthers lose food; prey of those mammals may increase.","lines":2}]
}
