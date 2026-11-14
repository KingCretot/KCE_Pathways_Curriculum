MAP = ('<svg viewBox="0 0 660 240" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Unit 5 concept map: an ecosystem has biotic and abiotic parts; energy flows through food webs; matter cycles; organisms interact">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Unit 5 concept map: how an ecosystem works</text>'
  '<rect x="250" y="34" width="160" height="40" rx="10" fill="#0A1F3D"/><text x="330" y="58" text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">ECOSYSTEM</text>'
  + ''.join(f'<path d="M330 74 L{x+70} 120" stroke="#8a95a5" stroke-width="2"/><rect x="{x}" y="120" width="140" height="104" rx="10" fill="{c}"/><text x="{x+70}" y="140" text-anchor="middle" fill="#fff" font-weight="bold">{a}</text>'
            + ''.join(f'<text x="{x+70}" y="{160+j*15}" text-anchor="middle" fill="#fff" font-size="10">{t}</text>' for j, t in enumerate(lines))
            for x, a, c, lines in [(14, "Week 21: parts", "#8a6d1f", ["biotic and abiotic", "levels of ecology", "limiting factors", "carrying capacity"]),
                                   (176, "Week 22: energy", "#DB2F30", ["producers, consumers,", "decomposers", "about 10% per level", "biomagnification"]),
                                   (338, "Week 23: matter", "#0047BA", ["water cycle", "Floridan aquifer", "carbon cycle", "matter is conserved"]),
                                   (500, "Week 24: interactions", "#2c6e22", ["predation, competition", "mutualism, commensalism,", "parasitism", "predator-prey cycles"])]) +
  '</svg>')

LESSON = {
 "unit": "Unit 5: Ecosystems",
 "title": "Unit 5 Checkpoint and Ecosystem Study Project",
 "subtitle": "This week you put the whole ecosystem together, from the abiotic factors that decide who lives where to the relationships that link every organism, finish your ecosystem study project on a real place near you, and show your mastery on the Unit 5 checkpoint.",
 "objectives": [
  "Explain how biotic and abiotic factors, energy flow, matter cycles and interactions work together in one ecosystem.",
  "Use evidence to predict how a change ripples through an ecosystem.",
  "Interpret food webs, cycles and population graphs.",
  "Complete a field study of a local ecosystem.",
  "Demonstrate mastery of Unit 5 on the checkpoint (85 or higher)."],
 "vocab": [
  ["ecosystem", "All the living and nonliving things in an area and how they interact."],
  ["energy pyramid", "A model showing how energy decreases at each level of a food chain."],
  ["biomagnification", "The buildup of a toxin at higher levels of a food chain."],
  ["symbiosis", "A close, long-term relationship between two species."],
  ["field study", "Scientific observations made in a real natural setting."]],
 "reconnect": {
  "title": "Unit 5, one question from each week",
  "intro": "Warm up with one question from each week of the unit.",
  "items": [
   {"t":"text","q":"Week 21: Is sunlight a biotic or an abiotic factor?","a":["^abiotic",{"all":[["abiotic"]],"none":["not abiotic"]}],"show":"abiotic","pts":2,"why":"It is not alive."},
   {"t":"num","q":"Week 22: If producers capture 30,000 units of energy, about how many reach the primary consumers?","a":3000,"unit":"units","pts":2,"why":"About 10 percent."},
   {"t":"text","q":"Week 23: Which process releases carbon dioxide every time a living thing breaks down sugar for energy?","a":[{"all":[["respiration"]],"none":["not"]}],"show":"cellular respiration","pts":2,"why":"Plants do it too."},
   {"t":"text","q":"Week 24: A tick feeding on a deer is an example of which type of symbiosis?","a":[{"all":[["parasit"]],"none":["not"]}],"show":"parasitism","pts":2,"why":"The tick benefits; the deer is harmed."}]},
 "hook": {
  "title": "One Spring, Every Idea",
  "visual": MAP,
  "html": "<p>Picture a single Florida spring. The 72°F water and the sunlight are abiotic factors. Eelgrass and algae capture the sun's energy; snails, fish and manatees eat them; alligators eat the fish. The water itself came from rain that soaked through the Floridan aquifer years ago, and carbon moves in and out with every breath and every bite. Cleaning fish, competing turtles and parasites all play their parts.</p><p>Every idea from Unit 5 is happening at once, in one place. This week you show how they fit together.</p><div class='callout'><b>Big question:</b> How do all the parts of an ecosystem depend on one another?</div>"},
 "learn": [
  {"title": "Review: Parts and Energy",
   "html": "<p>An ecosystem has <b>biotic</b> (living) and <b>abiotic</b> (nonliving) factors. Abiotic factors such as temperature, water and soil decide which organisms can live there, and limiting factors set the carrying capacity. Energy enters as sunlight, is captured by producers and flows to consumers, with only about 10 percent passing to each level. Toxins such as mercury do the opposite: they build up at higher levels.</p>",
   "checks": [
    {"t":"num","q":"In a food chain of sawgrass → marsh rabbit → panther, the sawgrass captures 50,000 units of energy. About how many reach the panther?","a":500,"unit":"units","pts":2,"why":"50,000 → 5,000 → 500."},
    {"t":"open","key":"abioticwho","q":"Explain how one abiotic factor decides which organisms can live in a Florida spring but not in the Gulf of Mexico.","min":20,"rows":2,"rubric":["Names a specific abiotic factor","Explains how it affects which organisms can live there"],"model":"Salt is the key abiotic factor. Spring water is fresh, so freshwater plants like eelgrass and fish like bass live there, while ocean fish that need salt water can't survive."}]},
  {"title": "Review: Cycles and Interactions",
   "html": "<p>Matter cycles: water evaporates, condenses, falls and flows through the aquifer; carbon moves through photosynthesis, eating, respiration, decomposition and burning. Organisms interact through predation, competition, mutualism, commensalism and parasitism, and predator and prey populations rise and fall in cycles.</p>",
   "checks": [
    {"t":"open","key":"matterenergy","q":"A manatee eats eelgrass. Explain what happens to the energy and what happens to the carbon in the eelgrass.","min":25,"rows":3,"rubric":["Energy: most is used or lost as heat; little is stored","Carbon: becomes part of the manatee and returns to the air or water through respiration or decomposition","Contrasts flowing energy with cycling matter"],"model":"Most of the energy in the eelgrass is used by the manatee to live and is lost as heat; it doesn't come back. The carbon becomes part of the manatee's body and returns to the water and air when the manatee breathes out or when it dies and decomposes, so the carbon can be used again."},
    {"t":"open","key":"relationsort","q":"Give one Florida example each of mutualism, commensalism and parasitism from this unit, and explain who benefits in each.","min":30,"rows":3,"rubric":["A correct example of each type","Explains who benefits, who is harmed and who is unaffected"],"model":"Mutualism: the neon goby cleans a grouper; both benefit. Commensalism: Spanish moss on a live oak; the moss benefits and the oak is unaffected. Parasitism: a tick on a deer; the tick benefits and the deer is harmed."}]},
  {"title": "Finishing the Ecosystem Study Project",
   "html": "<p>Your project (see the Unit 5 projects page) is a field study of a real ecosystem near you: a park, a pond, a beach, a spring, a wooded lot or even your backyard. You collect data on at least three visits, then present a <b>field guide poster or slideshow</b> that shows its biotic and abiotic factors, a food web, one matter cycle, at least three relationships and one human impact with a solution.</p><p>Good field data are specific: \"7 fiddler crabs in a 1-meter quadrat at 10 a.m., 84°F, low tide,\" not \"some crabs.\"</p>",
   "checks": [
    {"t":"open","key":"fieldplan","q":"Name the place you are studying and describe how you will collect data on three visits: what you will measure, with what tools, and how you'll keep conditions fair.","min":35,"rows":3,"rubric":["Names a real study site","Specific measurements and tools","Explains how visits will be comparable"],"model":"I'm studying the retention pond behind our church. On three Saturday mornings at 9 a.m., I'll measure water temperature with a thermometer, count birds and turtles for 15 minutes, and survey a 1-meter quadrat at the edge for plants and insects. Going at the same time and spot each visit keeps it fair."}]}],
 "handson": {
  "title": "Ecosystem in a Shoebox: Ripple Test",
  "intro": "Build a model of your study ecosystem and test what happens when one piece changes.",
  "materials": ["A shoebox or box lid", "Index cards cut in half and a marker", "Yarn or string in 3 colors", "Tape", "Your field notes", "A family member", "Paper and pencil"],
  "steps": [
   "Write each organism and abiotic factor from your study site on a half card. Tape them inside the box: abiotic factors along the bottom, producers above, consumers higher, and decomposers along one side.",
   "Connect feeding links with one color of yarn (arrows drawn in the direction energy flows), relationships such as mutualism with a second color, and one matter cycle with a third.",
   "Ripple test: your family member names a change (a drought, a new invasive species, a fertilizer spill or the loss of one species). Pull or remove the affected card and trace every yarn connected to it.",
   "Predict and record how at least three other parts would change.",
   "Keep yarn and scissors away from young children and pets."],
  "record": [
   {"t":"open","key":"ripplerec","q":"Describe the change you tested and the ripple effects you predicted for at least three other parts of your ecosystem. Which connection surprised you?","min":45,"rows":4,"rubric":["Names the change tested","At least three ripple effects traced through the model","Reflects on a surprising connection"],"model":"We tested a fertilizer spill into our pond. Algae would grow quickly and block sunlight from underwater plants; when the algae died, decomposers would use up oxygen, so fish could die; then herons and turtles would lose food. The surprise was that more food for algae could end up meaning less food for everything else."}]},
 "think": {
  "intro": "Your teacher scores this.",
  "items": [
   {"t":"open","key":"unitreflect","q":"Write a short explanation for a younger child of why \"everything in an ecosystem is connected.\" Use at least one example from each week of the unit (parts, energy, matter and interactions).","min":70,"rows":6,"rubric":["Explains connection in kid-friendly language","An accurate example from each of the four weeks","Ties the examples together"],"model":"In nature, everything needs something else. Plants need sunlight and water, which are nonliving parts. Rabbits eat the plants to get energy, and panthers eat the rabbits, but most energy gets used up along the way, so there are only a few panthers. When animals breathe and when they die, their carbon goes back into the air and soil for new plants. And some animals help each other, like little fish that clean big fish. If one piece disappears, the others feel it."}]},
 "checkpoint": {
  "title": "Unit 5 Checkpoint: Ecosystems",
  "intro": "This checkpoint covers Weeks 21 to 24. Answer every question; for written answers, use science vocabulary. Mastery is 85 or higher. If you score below 85, your teacher will review with you, then you will retake it.",
  "parts": [
   {"title": "Part A: Parts of an ecosystem", "items": [
    {"t":"blanks","q":"Classify each factor in a Florida pine forest.","sent":"Longleaf pine: ___ &nbsp; Sandy soil: ___ &nbsp; Gopher tortoise: ___","blanks":[[{"all":[["biotic"]],"none":["abiotic","not"]}],[{"all":[["abiotic"]],"none":["not"]}],[{"all":[["biotic"]],"none":["abiotic","not"]}]],"show":"biotic; abiotic; biotic","pts":3,"why":"Living things are biotic; soil is abiotic."},
    {"t":"order","q":"Put the levels of ecology in order from smallest to largest.","items":["organism","population","community","ecosystem","biosphere"],"pts":3,"why":"Each level includes the one before it."},
    {"t":"open","key":"cplimit","q":"A pond's frog population grows for three years and then levels off. Explain why, using the terms limiting factor and carrying capacity.","min":20,"rows":3,"pts":4,"rubric":["Uses limiting factor correctly with an example","Uses carrying capacity correctly","Explains the leveling off"],"model":"The population levels off because it reached the pond's carrying capacity, the largest number of frogs the pond can support. Limiting factors such as the number of insects to eat and places to lay eggs keep the population from growing any larger."}]},
   {"title": "Part B: Energy in food webs", "items": [
    {"t":"text","q":"In a food web, what do the arrows show?","a":[{"all":[["energy"]],"none":["not energy"]}],"show":"the direction energy flows (from food to eater)","pts":3,"why":"Arrows point from the food to the organism that eats it."},
    {"t":"num","q":"Algae capture 80,000 units of energy. About how many reach a secondary consumer?","a":800,"unit":"units","pts":3,"why":"80,000 → 8,000 → 800."},
    {"t":"open","key":"cpmercury","q":"Explain why a largemouth bass from a polluted lake usually has much more mercury in its body than the small fish it eats.","min":20,"rows":3,"pts":4,"rubric":["Mercury is stored in the body, not used up","The bass eats many small fish, so mercury builds up at each level (biomagnification)"],"model":"Mercury isn't used up or lost; it is stored in the body. A bass eats many small fish over its life, collecting the mercury from each one, so the amount builds up at each level of the food chain. This is biomagnification."}]},
   {"title": "Part C: Cycles of matter", "items": [
    {"t":"order","q":"Put these steps of the water cycle in order, starting with water in a lake.","items":["evaporation","condensation","precipitation","infiltration into the aquifer"],"pts":3,"why":"Then groundwater can flow out at a spring."},
    {"t":"text","q":"Which process do producers use to remove carbon dioxide from the air?","a":[{"all":[["photosynth"]],"none":["not photosynth"]}],"show":"photosynthesis","pts":3,"why":"They make sugar from carbon dioxide and water."},
    {"t":"open","key":"cpfossil","q":"Explain why burning fossil fuels increases the carbon dioxide in the air even though that carbon was once part of living things.","min":20,"rows":3,"pts":4,"rubric":["The carbon was stored underground for millions of years, outside the active cycle","Burning releases it quickly, faster than plants and oceans can absorb it"],"model":"The carbon in coal, oil and gas was locked underground for millions of years, out of the active cycle. Burning releases all that stored carbon as carbon dioxide very quickly, faster than plants and the ocean can take it back in, so the amount in the air rises."}]},
   {"title": "Part D: Interactions", "items": [
    {"t":"blanks","q":"Classify each relationship.","sent":"Bees pollinating orange blossoms: ___ &nbsp; Cattle egrets catching insects stirred up by cows: ___ &nbsp; Two anole species wanting the same perch: ___","blanks":[[{"all":[["mutual"]],"none":["not"]}],[{"all":[["commensal"]],"none":["not"]}],[{"all":[["compet"]],"none":["not"]}]],"show":"mutualism; commensalism; competition","pts":3,"why":"+/+; +/0; −/−."},
    {"t":"open","key":"cpcycle","q":"In a forest, hare numbers peak in 2010 and lynx numbers peak in 2012. Explain why the lynx peak comes after the hare peak, and predict what happens to the hares after 2012.","min":25,"rows":3,"pts":4,"rubric":["Explains the time lag (more food lets lynx reproduce; kittens take time to grow)","Predicts the hares decline after 2012 because there are many predators"],"model":"With lots of hares, lynx have plenty of food and raise more kittens, but it takes time for the lynx population to grow, so it peaks two years later. After 2012 the many lynx eat so many hares that the hare population falls, and later the lynx will decline too."},
    {"t":"open","key":"cpinvasive","q":"Burmese pythons have spread through the Everglades. Use two relationship types and the idea of energy flow to predict two effects on the ecosystem.","min":30,"rows":4,"pts":4,"rubric":["Uses two relationship types correctly","Uses energy flow correctly","Two reasonable predicted effects"],"model":"Pythons are predators of raccoons and marsh rabbits, so those populations drop. They also compete with native predators like panthers and alligators for the same prey, so those predators have less energy flowing to them and may decline. Plants and animals the mammals once ate could increase."}]}]},
 "next": "Unit 6: heredity and adaptation, starting with traits and inheritance."
}

TEACHER = {
 "standards": [
  "SC.7.L.17.1: Explain and illustrate the roles of and relationships among producers, consumers, and decomposers in the process of energy transfer in a food web.",
  "SC.7.L.17.2: Compare and contrast the relationships among organisms such as mutualism, predation, parasitism, competition, and commensalism.",
  "SC.7.L.17.3: Describe and investigate various limiting factors in the local ecosystem and their impact on native populations, including food, shelter, water, space, disease, parasitism, predation, and nesting sites.",
  "SC.8.L.18.3: Construct a scientific model of the carbon cycle to show how matter and energy are continuously transferred within and between organisms and their physical environment.",
  "SC.6.N.1.1: Define a problem from the sixth grade curriculum, use appropriate reference materials to support scientific understanding, plan and carry out scientific investigation of various types, such as systematic observations or experiments, identify variables, collect and organize data, interpret data in charts, tables, and graphics, analyze information, make predictions, and defend conclusions."],
 "materials": ["The interactive lesson", "A shoebox or box lid, half index cards, a marker, yarn in 3 colors, tape", "The student's field notes", "The Unit 5 projects page and rubric", "The Unit 5 checkpoint"],
 "flow": [
  [6, "Reconnect", "Run one question from each week of the unit."],
  [4, "Hook", "One spring, every idea; the concept map."],
  [10, "Parts and energy", "Abiotic factors; the 10 percent rule."],
  [10, "Cycles and interactions", "Energy versus matter in one meal; sort relationships."],
  [12, "Project workshop", "Field data that are specific; plan the three visits."],
  [8, "Assign", "Set up the shoebox ripple test; review the project rubric; assign Think Deeper."],
  [10, "Checkpoint preview", "Explain that the checkpoint is completed after class, independently, one try per item, with no answers shown until you review it. Mastery is 85; below 85 means a review lesson and a retake."]],
 "key_questions": ["Is this energy or matter, and does it flow or cycle?", "What limits this population?", "Who benefits in this relationship?", "If one part changes, what else changes?"],
 "misconceptions": ["Energy is recycled in ecosystems.", "Food web arrows point from eater to food.", "Plants don't respire.", "Predators wipe out their prey."],
 "support": ["Keep the concept map visible during review (not during the checkpoint).", "Use the shoebox model to answer ripple questions aloud first.", "Provide a field data sheet with columns for date, time, weather, counts and notes."],
 "challenge": ["Compare your study site with a site in a different Florida ecosystem.", "Graph your three visits' data and explain any differences."],
 "background": "<p>Checkpoint totals: Part A 10, Part B 10, Part C 10, Part D 11, total 41. Florida places most of these benchmarks in Grades 7 and 8; KCE teaches them here per the Grade 6 scope. Field visits should be supervised; avoid touching wildlife, stay back from water where alligators may be present, and check public land rules before collecting anything.</p>",
 "sources": ["Florida Department of Education, Next Generation Sunshine State Standards for Science.", "Florida Fish and Wildlife Conservation Commission, Living with Alligators.", "National Park Service, Everglades National Park: Burmese Pythons."]
}

PRINT = {
 "directions": "Answer in complete sentences. This page reviews the whole unit.",
 "items": [
  {"q":"Name two biotic and two abiotic factors in a Florida ecosystem.","a":"Biotic: cypress tree, alligator; abiotic: water, sunlight.","lines":2},
  {"q":"Explain the 10 percent rule.","a":"Only about 10 percent of energy passes to the next level; the rest is used or lost as heat.","lines":2},
  {"q":"Describe how water moves from the Gulf to a Florida spring.","a":"Evaporation, condensation, precipitation over land, infiltration into the aquifer, flow out at the spring.","lines":3},
  {"q":"Name the five types of relationships and give an example of each.","a":"Predation, competition, mutualism, commensalism, parasitism, with correct examples.","lines":4},
  {"q":"Predict one ripple effect if decomposers disappeared from a pond.","a":"Dead matter piles up and nutrients stay locked away, so producers and the whole web suffer.","lines":2}]
}
