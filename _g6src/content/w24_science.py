REL = ('<svg viewBox="0 0 660 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="A chart of five relationships showing whether each species benefits, is harmed or is unaffected">'
  '<text x="330" y="22" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Who wins? Five ways organisms interact</text>'
  + ''.join(f'<g transform="translate({14+i*128},40)"><rect width="120" height="176" rx="10" fill="{c}"/><text x="60" y="26" text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">{n}</text><text x="60" y="78" text-anchor="middle" fill="#fff" font-weight="bold" font-size="34">{s}</text><text x="60" y="118" text-anchor="middle" fill="#fff" font-size="11">{e1}</text><text x="60" y="134" text-anchor="middle" fill="#fff" font-size="11">{e2}</text><text x="60" y="160" text-anchor="middle" fill="#fff" font-size="10">{k}</text></g>'
            for i, (n, s, e1, e2, k, c) in enumerate([("predation", "+ / \u2212", "lynx eats", "snowshoe hare", "predator / prey", "#DB2F30"), ("competition", "\u2212 / \u2212", "two anoles want", "the same perch", "both get less", "#5b6676"), ("mutualism", "+ / +", "goby cleans", "grouper", "both benefit", "#2c6e22"), ("commensalism", "+ / 0", "Spanish moss", "on a live oak", "one benefits", "#0047BA"), ("parasitism", "+ / \u2212", "tick feeds", "on a deer", "parasite / host", "#8a6d1f")])) +
  '</svg>')

LYNX = ('<svg viewBox="0 0 660 300" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="A stylized graph of snowshoe hare and lynx populations rising and falling in cycles about ten years apart, with lynx peaks following hare peaks">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Predator and prey: snowshoe hare and Canada lynx (pattern)</text>'
  '<path d="M60 230 H630 M60 230 V40" stroke="#0A1F3D" stroke-width="2"/>'
  '<text x="345" y="262" text-anchor="middle" fill="#0A1F3D">years (one cycle is about 10 years)</text>'
  '<text x="20" y="140" fill="#0A1F3D" transform="rotate(-90 20 140)" text-anchor="middle">number of animals</text>'
  '<path d="M60 200 C100 200 120 60 160 60 C200 60 210 200 260 205 C300 205 320 70 360 60 C400 55 410 200 460 205 C500 205 520 70 560 60 C590 55 610 170 630 190" fill="none" stroke="#8a6d1f" stroke-width="3"/>'
  '<path d="M60 215 C110 215 140 140 190 130 C230 125 250 210 290 215 C330 215 350 140 390 130 C430 125 450 210 490 215 C530 215 550 140 590 130 C610 128 620 160 630 180" fill="none" stroke="#DB2F30" stroke-width="3" stroke-dasharray="7 4"/>'
  '<path d="M140 284 h30" stroke="#8a6d1f" stroke-width="3"/><text x="178" y="288" fill="#8a6d1f" font-weight="bold">snowshoe hare (prey)</text>'
  '<path d="M360 284 h30" stroke="#DB2F30" stroke-width="3" stroke-dasharray="7 4"/><text x="398" y="288" fill="#DB2F30" font-weight="bold">Canada lynx (predator)</text>'
  '<text x="175" y="52" fill="#8a6d1f" font-size="10">hare peak</text></svg>')

LESSON = {
 "unit": "Unit 5: Ecosystems",
 "title": "How Organisms Interact",
 "subtitle": "Food webs show who eats whom, but organisms also compete, cooperate and take advantage of one another. This week you sort the relationships that tie an ecosystem together, from Florida's coral reefs to the forests of the Yukon, and model how predators and prey rise and fall together.",
 "objectives": [
  "Describe and give examples of predation, competition, mutualism, commensalism and parasitism.",
  "Classify relationships by who benefits, who is harmed and who is unaffected.",
  "Interpret a predator–prey graph and explain why the populations cycle.",
  "Explain how limiting factors and competition, including from invasive species, affect populations.",
  "Model a predator–prey relationship and analyze the data."],
 "vocab": [
  ["predation", "A relationship in which one organism (the predator) hunts and eats another (the prey)."],
  ["competition", "A relationship in which organisms struggle for the same limited resource, such as food, water, space or light."],
  ["symbiosis", "A close, long-term relationship between two different species."],
  ["mutualism", "A symbiosis in which both species benefit."],
  ["commensalism", "A symbiosis in which one species benefits and the other is neither helped nor harmed."],
  ["parasitism", "A symbiosis in which one species (the parasite) benefits and the other (the host) is harmed."],
  ["limiting factor", "Anything that limits the size of a population, such as food, space, water or predators."],
  ["carrying capacity", "The largest population an environment can support over time."]],
 "reconnect": {
  "title": "Week 23: Cycles of matter",
  "intro": "Matter cycles through every relationship you'll study this week.",
  "items": [
   {"t":"text","q":"Which process do plants use to take carbon dioxide out of the air?","a":[{"all":[["photosynth"]],"none":["not photosynth","respiration"]}],"show":"photosynthesis","pts":2,"why":"Producers start every food web."},
   {"t":"text","q":"What is the name of the underground limestone layer that feeds Florida's springs?","a":[{"all":[["floridan"]],"none":["not"]}],"show":"the Floridan aquifer","pts":2,"why":"Spring ecosystems depend on it."},
   {"t":"text","q":"When a predator eats its prey, does energy cycle back or flow on and get lost as heat?","a":[{"all":[["flow","lost","heat"]],"none":["not","cycle"]}],"show":"it flows on, and most is lost as heat","pts":2,"why":"Matter cycles; energy flows."},
   {"t":"open","key":"rc_carbonprey","q":"A lynx eats a snowshoe hare. Trace one carbon atom from a willow twig, through the hare and the lynx, and back into the air.","min":20,"rows":2,"rubric":["Willow (photosynthesis) to hare (eating) to lynx (eating)","Returns to the air through respiration or decomposition"],"model":"The willow made sugar from carbon dioxide; the hare ate the twig, the lynx ate the hare, and the lynx breathed the carbon out as carbon dioxide (or decomposers released it after the lynx died)."}]},
 "hook": {
  "title": "The Fish That Cleans Other Fish",
  "visual": REL,
  "html": "<p>On Florida's coral reefs, a big grouper swims to a particular spot, stops and opens its mouth wide. A tiny, striped neon goby swims right in, picks off parasites and dead skin, and swims out unharmed. The grouper could swallow it in a second, but doesn't.</p><p>The grouper gets cleaned; the goby gets a meal. Both win. Divers call these places <b>cleaning stations</b>, and fish line up at them like customers at a car wash.</p><p>Not every relationship is that friendly. Ticks drink deer blood, and lynx hunt hares. In every ecosystem, relationships like these shape who survives.</p><div class='callout'><b>Big question:</b> How do the ways organisms interact shape populations and ecosystems?</div>"},
 "learn": [
  {"title": "Predation and the Predator–Prey Cycle",
   "visual": LYNX,
   "html": "<p>In <b>predation</b>, the predator benefits and the prey is harmed. Last week's food web showed many predator–prey links. Here's what happens to the populations over time.</p><p>Fur traders for the Hudson's Bay Company in Canada kept records of the lynx and snowshoe hare pelts they bought for about 100 years, starting in the 1800s. Scientists noticed the numbers rose and fell in a cycle of about 10 years:</p><ol><li>Lots of hares means plenty of food, so lynx numbers grow.</li><li>More lynx eat more hares, and the hares also run short of winter food, so hare numbers crash.</li><li>With few hares, many lynx starve or raise fewer kittens, so lynx numbers fall.</li><li>With few lynx and regrown plants, hares recover, and the cycle repeats.</li></ol><p>The lynx peak always comes a little <i>after</i> the hare peak. These are the same Yukon forests where Buck runs with the wolves.</p>",
   "checks": [
    {"t":"text","q":"In the graph, which population peaks first, the hare or the lynx?","a":[{"all":[["hare"]],"none":["not hare","lynx"]}],"show":"the hare","pts":2,"why":"Predators increase after their food supply does."},
    {"t":"num","q":"If hare populations peaked in 1886, 1896 and 1906, in about what year would you predict the next peak?","a":1916,"tol":1,"unit":"","pts":2,"why":"The cycle is about 10 years."},
    {"t":"open","key":"lynxlag","q":"Explain why the lynx population peaks a year or two after the hare population, not at the same time.","min":25,"rows":3,"rubric":["Lynx need time to reproduce and raise young after food becomes plentiful","By the time lynx numbers peak, hares are already declining"],"model":"When hares become plentiful, the lynx have more food, but it takes time for them to have kittens and for those kittens to grow. By the time the lynx population peaks, the hares are already declining because there are so many predators and less food."}]},
  {"title": "Competition and Limiting Factors",
   "html": "<p>In <b>competition</b>, organisms struggle for the same limited resource, and both are harmed because each gets less. Competition can happen within a species (two male deer fighting) or between species.</p><p>A Florida example: the native <b>green anole</b> once lived on tree trunks and low branches throughout Florida. When the <b>brown anole</b>, an invasive lizard from Cuba and the Bahamas, spread across the state, it took over the lower perches. Scientists studying small islands off Florida found that, in about 15 years, green anoles moved higher into the trees, and their toe pads grew larger and stickier for gripping smooth leaves, an example of evolution happening quickly.</p><p>A <b>limiting factor</b> is anything that keeps a population from growing forever: food, water, space, shelter, disease or predators. The largest population an environment can support over time is its <b>carrying capacity</b>.</p>",
   "checks": [
    {"t":"text","q":"Two species of birds eat the same seeds in a park. What type of relationship is this?","a":[{"all":[["compet"]],"none":["not"]}],"show":"competition","pts":2,"why":"Both want the same limited resource."},
    {"t":"open","key":"anoles","q":"Explain how competition with brown anoles changed where green anoles live and how their bodies changed. Why is this considered evidence of evolution?","min":30,"rows":3,"rubric":["Green anoles moved higher in trees","Toe pads got larger and stickier over generations","Evolution: the population's traits changed over generations because those traits helped survival"],"model":"Brown anoles took over the low perches, so green anoles moved higher into the trees. Over about 20 generations, green anoles with bigger, stickier toe pads survived better up high, so the population's toe pads got larger. A change in a population's traits over generations is evolution."},
    {"t":"open","key":"homelimit","q":"Think of a population you can observe at home or nearby (squirrels in your yard, ants by your door, fish in a tank, plants in a garden bed). Name two limiting factors for it and predict what would happen if one were removed.","min":30,"rows":3,"rubric":["A real local population","Two reasonable limiting factors","A prediction (grows until another factor limits it)"],"model":"The squirrels in our yard are limited by how many acorns the oaks drop and by the hawks that hunt them. If the hawks disappeared, the squirrel population would grow until food or nesting space became the new limit."}]},
  {"title": "Symbiosis: Mutualism, Commensalism and Parasitism",
   "html": "<p><b>Symbiosis</b> is a close, long-term relationship between two species. There are three kinds, sorted by who benefits:</p><ul><li><b>Mutualism (+/+):</b> both benefit. The goby and the grouper. Reef-building coral and the tiny algae living inside them: the algae make food by photosynthesis and share it, and the coral gives them shelter. Bees and the orange blossoms they pollinate.</li><li><b>Commensalism (+/0):</b> one benefits, the other is unaffected. Spanish moss hangs on live oaks to reach sunlight but takes no food from the tree. Cattle egrets follow cows to catch insects the cows stir up.</li><li><b>Parasitism (+/−):</b> one benefits, the host is harmed. Ticks on deer; heartworms in dogs, spread by mosquitoes.</li></ul><p>Some relationships are hard to classify. Remoras ride on sharks and eat their scraps, usually called commensalism, but some remoras also eat parasites off the shark, which would make it mutualism. Scientists keep testing which label fits.</p>",
   "checks": [
    {"t":"blanks","q":"Classify each relationship.","sent":"Spanish moss on a live oak: ___ &nbsp; A tick on a deer: ___ &nbsp; Coral and the algae inside it: ___","blanks":[[{"all":[["commensal"]],"none":["not"]}],[{"all":[["parasit"]],"none":["not"]}],[{"all":[["mutual"]],"none":["not"]}]],"show":"commensalism; parasitism; mutualism","pts":3,"why":"+/0; +/−; +/+."},
    {"t":"open","key":"coralbleach","q":"When ocean water gets too warm, corals expel the algae living inside them and turn white, which is called bleaching. Use the idea of mutualism to explain why bleached coral may starve and die.","min":30,"rows":3,"rubric":["The algae provided food to the coral by photosynthesis","Without the partner, the coral loses most of its food (the mutualism breaks down)"],"model":"Coral and algae are partners in mutualism: the algae make food by photosynthesis and share it with the coral. When the coral expels the algae, it loses most of its food supply, so if the water stays too warm for too long, the coral can starve and die."},
    {"t":"open","key":"remoraclass","q":"Explain why the remora and shark relationship is hard to classify. What evidence would a scientist need to decide?","min":30,"rows":3,"rubric":["Remora clearly benefits; the question is whether the shark is helped, harmed or unaffected","Evidence: whether remoras remove parasites, slow the shark down or have no effect, measured with observations or data"],"model":"The remora clearly benefits from free rides and scraps, but it's unclear whether the shark gains anything. A scientist would need evidence such as observations of remoras eating the shark's parasites, or measurements of whether sharks with remoras swim more slowly or stay healthier."}]},
  {"title": "People and Relationships in Ecosystems",
   "html": "<p>Humans are part of these relationships too. People have mutualism with the honeybees they keep and the crops they plant. Florida citrus growers depend on bees for pollination, and in turn plant flowers and provide hives.</p><p>Human actions can also break relationships. Invasive species such as Burmese pythons and brown anoles add new predators and competitors that native species never evolved alongside. Warmer seas break the coral–algae partnership. Pesticides can harm pollinators.</p><p>Indigenous peoples have long practiced relationships that benefit both people and land. The Seminole and Miccosukee people of Florida have harvested resources like sabal palm (used for chickee roofs) in ways that allow the plants to regrow, and in the Yukon, the Tr'ondëk Hwëch'in managed salmon fishing and caribou hunting for thousands of years.</p>",
   "checks": [
    {"t":"open","key":"beepeople","q":"Explain the relationship between Florida citrus growers and honeybees. What type is it, and what would happen to orange harvests if local bee populations crashed?","min":28,"rows":3,"rubric":["Mutualism: bees get nectar and pollen (and hives); growers get pollination and fruit","Fewer bees means fewer flowers pollinated, so fewer oranges"],"model":"It's mutualism: the bees get nectar, pollen and safe hives, and the growers get their trees pollinated. If bee populations crashed, many orange blossoms wouldn't be pollinated, so trees would produce fewer oranges."}]}],
 "handson": {
  "title": "Lynx and Hares on the Kitchen Floor",
  "intro": "Model the predator–prey cycle with paper squares, then graph your own data.",
  "materials": ["About 200 small paper squares about 1 inch across (the hares), cut from scrap paper", "About 40 paper squares about 3 inches across (the lynx), cut from a different color", "A 3-foot by 3-foot area marked with tape on the floor or a table", "Paper and pencil, or graph paper", "Colored pencils"],
  "steps": [
   "Start with 3 hares in the area, scattered randomly.",
   "Generation 1: toss one lynx square from about 2 feet above the area. Every hare it touches is caught; remove those hares. A lynx must catch at least 3 hares to survive; if it does, it also produces one new lynx for the next generation. A lynx that catches fewer than 3 dies.",
   "Hares that survive each produce one new hare (double the hares left). Hares also always increase by at least 3 from outside the area if the count is low.",
   "Record the number of hares and lynx at the start of each generation. Repeat for 15 to 20 generations. If all lynx die, add one lynx as if it wandered in from outside.",
   "Graph both populations over time on the same axes with two colors.",
   "Pick up all paper squares when you're done so pets don't eat them."],
  "record": [
   {"t":"open","key":"simdata","q":"Describe your graph. Did the hare and lynx populations rise and fall? Did the lynx peaks come after the hare peaks? Give numbers from your data.","min":45,"rows":4,"rubric":["Describes the pattern with numbers","Compares the timing of the peaks","Honest about anything that didn't match the real cycle"],"model":"Hares grew from 3 to 48 by generation 6, while lynx stayed at 1 or 2. Then lynx jumped to 7 in generation 8, catching so many hares that hares dropped to 9 by generation 10. Lynx crashed to 1 in generation 11, and hares started climbing again. The lynx peak came two generations after the hare peak, like the real data."},
   {"t":"open","key":"simlimits","q":"Name two ways this model is different from a real Yukon forest. How might adding one real factor (like limited winter plants for hares) change your results?","min":35,"rows":3,"rubric":["Two real differences (no plant food limit, no other predators or prey, random tossing, no weather or disease, small area)","A reasonable prediction about adding a factor"],"model":"Real lynx search with their senses instead of landing randomly, and real hares are limited by winter food, not just by lynx. If I limited hares to 60 because of winter plants, hare peaks would be lower and the crash would come sooner, even before the lynx numbers rose much."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"wolfreturn","q":"In 1995 and 1996, wolves were brought back to Yellowstone National Park after being missing for about 70 years. Elk numbers dropped and elk stopped grazing so heavily along rivers. Predict two ripple effects on other organisms, using at least two relationship types from this week.","min":48,"rows":6,"rubric":["Two plausible ripple effects","At least two relationship types named and used correctly (predation, competition, mutualism, commensalism)","Logical chain of cause and effect"],"model":"Wolves are predators of elk, so with fewer elk browsing, willows and aspens along rivers could regrow. Beavers, which compete with elk for willows, would have more food and build more dams, creating ponds for fish and frogs. Ravens and eagles feed on scraps from wolf kills, a commensal relationship, so their food supply would grow too."},
   {"t":"open","key":"invasivewhy","q":"Explain why invasive species like the brown anole or the Burmese python can harm native species so much, using what you learned about relationships, limiting factors and evolution.","min":56,"rows":5,"rubric":["Native species didn't evolve defenses or strategies against the newcomer","Invasives may lack their own predators or competitors (no limiting factors), so populations explode","They compete with or prey on natives, reducing native populations"],"model":"Native species never evolved alongside the invader, so they have no defenses against a new predator or strategies to compete with it. The invader often has no predators or diseases in its new home, so few limiting factors keep its population down. It can quickly outcompete or eat native species, as brown anoles pushed green anoles up the trees and pythons cut mammal numbers in the Everglades."}]},
 "exit": [
  {"t":"text","q":"A relationship in which both species benefit is called ___.","a":[{"all":[["mutual"]],"none":["not"]}],"show":"mutualism","pts":2,"why":"Like the goby and the grouper."},
  {"t":"text","q":"Heartworms living in a dog: which type of symbiosis?","a":[{"all":[["parasit"]],"none":["not"]}],"show":"parasitism","pts":2,"why":"The worm benefits; the dog is harmed."},
  {"t":"text","q":"The largest population an environment can support over time is its ___.","a":[{"all":[["carrying capacity"]],"none":["not"]}],"show":"carrying capacity","pts":2,"why":"Limiting factors set it."},
  {"t":"open","key":"exit_cycle","q":"In one or two sentences, explain why predator and prey populations rise and fall in cycles.","min":15,"rows":2,"rubric":["More prey lets predators increase; more predators reduce prey; then predators decline, and prey recover"],"model":"When prey are plentiful, predators increase and eat more prey, so prey decline; then predators starve and decline, letting prey recover."}],
 "next": "Week 25: Unit 5 checkpoint and ecosystem study project."
}

TEACHER = {
 "standards": [
  "SC.7.L.17.2: Compare and contrast the relationships among organisms such as mutualism, predation, parasitism, competition, and commensalism.",
  "SC.7.L.17.3: Describe and investigate various limiting factors in the local ecosystem and their impact on native populations, including food, shelter, water, space, disease, parasitism, predation, and nesting sites.",
  "SC.6.N.3.4: Identify the role of models in the context of the sixth grade science benchmarks.",
  "NGSS MS-LS2-2: Construct an explanation that predicts patterns of interactions among organisms across multiple ecosystems."],
 "materials": ["The interactive lesson", "About 200 small and 40 larger paper squares in two colors, tape, paper or graph paper, colored pencils", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 23 warm-up questions."],
  [4, "Hook", "Cleaning stations on Florida reefs."],
  [12, "Predation", "Read the lynx and hare cycle; explain the lag."],
  [11, "Competition and limiting factors", "Green and brown anoles; carrying capacity."],
  [12, "Symbiosis", "Classify; coral bleaching; the remora debate."],
  [9, "People and relationships", "Bees and citrus; invasive species; Indigenous stewardship."],
  [6, "Assign", "Set up the simulation; assign the graph, Think Deeper and the Exit Check."]],
 "key_questions": ["Who benefits, who is harmed, who is unaffected?", "What limits this population?", "Why does the predator peak come later?", "How do people change these relationships?"],
 "misconceptions": ["Predators wipe out their prey.", "Symbiosis always means both species benefit.", "Competition always involves fighting.", "Parasites usually kill their hosts quickly (most don't; a dead host is bad for a parasite)."],
 "support": ["Use a +, −, 0 chart to classify relationships.", "Act out the cleaning station and the tick on a deer.", "Provide a partially filled data table for the simulation."],
 "challenge": ["Research the Isle Royale wolves and moose and compare their graph with the lynx and hares.", "Design an experiment to test whether remoras help or harm sharks."],
 "background": "<p>The lynx–hare cycle comes from Hudson's Bay Company fur records (roughly 1845 to 1935), analyzed by Charles Elton and others; trapping effort affects pelt counts, so the data reflect populations only approximately. Hare cycles are driven by both predation and food supply. The green and brown anole study is Stuart and colleagues (2014, Science): on islands in Mosquito Lagoon, green anoles perched higher within months of brown anole introduction, and toe pads enlarged within about 15 years (about 20 generations). Wolves were reintroduced to Yellowstone in 1995 and 1996; the extent of the resulting ripple effects is still debated by ecologists. Florida places these benchmarks in Grade 7 (SC.7.L.17.2 and 17.3); KCE teaches them here per the Grade 6 scope.</p>",
 "sources": ["Stuart, Y. E., and others, \"Rapid evolution of a native species following invasion by a congener,\" Science 346 (2014).", "Elton, C., and M. Nicholson, \"The ten-year cycle in numbers of the lynx in Canada,\" Journal of Animal Ecology (1942).", "NOAA, Coral Reef Conservation Program: What is coral bleaching?", "National Park Service, Yellowstone: Wolf Restoration."]
}

PRINT = {
 "directions": "Answer in complete sentences.",
 "items": [
  {"q":"Define and give one example of each: predation, competition, mutualism, commensalism, parasitism.","a":"Lynx and hare; two birds for seeds; goby and grouper; Spanish moss on oak; tick on deer.","lines":4},
  {"q":"Why does the lynx population peak after the hare population?","a":"Lynx need time to reproduce after food increases; by their peak, hares are already declining.","lines":2},
  {"q":"How did brown anoles affect green anoles in Florida?","a":"Competition pushed green anoles higher in trees, and their toe pads grew larger over generations.","lines":2},
  {"q":"Name three limiting factors and define carrying capacity.","a":"Food, water, space, predators, disease; the largest population an environment can support over time.","lines":2},
  {"q":"Explain coral bleaching using mutualism.","a":"Warm water makes coral expel its food-making algae partners, so the coral may starve.","lines":2},
  {"q":"Describe one way people break or support relationships in ecosystems.","a":"Invasive species or warmer seas break them; keeping bees or sustainable harvesting supports them.","lines":2}]
}
