LEVELS = ('<svg viewBox="0 0 660 220" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Ecological levels from organism to biosphere, using an alligator in the Everglades">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Zooming out: levels of ecology</text>'
  + ''.join(f'<g transform="translate({14+i*130},40)"><rect width="118" height="150" rx="12" fill="{c}"/><text x="59" y="24" text-anchor="middle" fill="#fff" font-weight="bold">{a}</text>'
            + ''.join(f'<text x="59" y="{110+j*15}" text-anchor="middle" fill="#fff" font-size="10">{t}</text>' for j, t in enumerate(lines)) + pic + '</g>'
            for i, (a, c, lines, pic) in enumerate([
              ("Organism", "#2c6e22", ["one alligator"], '<ellipse cx="59" cy="66" rx="34" ry="10" fill="#fff"/>'),
              ("Population", "#3d7f33", ["all the alligators", "in Shark Valley"], ''.join(f'<ellipse cx="{30+k*22}" cy="{56+(k%2)*18}" rx="12" ry="5" fill="#fff"/>' for k in range(4))),
              ("Community", "#1d6fb8", ["alligators, egrets, fish,", "sawgrass: all the", "living things"], '<ellipse cx="38" cy="70" rx="14" ry="5" fill="#fff"/><path d="M76 52 v24 M80 50 v26 M84 54 v22" stroke="#fff" stroke-width="2"/><circle cx="60" cy="50" r="6" fill="#fff"/>'),
              ("Ecosystem", "#0047BA", ["the community plus", "water, sunlight, soil,", "temperature"], '<circle cx="90" cy="46" r="10" fill="#C9A84C"/><path d="M14 80 q20 -8 40 0 t40 0" stroke="#9fc6e8" stroke-width="4" fill="none"/><path d="M40 60 v20 M46 58 v22" stroke="#fff" stroke-width="2"/>'),
              ("Biosphere", "#0A1F3D", ["every ecosystem", "on Earth"], '<circle cx="59" cy="66" r="28" fill="#9fc6e8"/><path d="M42 56 q10 -8 20 0 q6 10 -6 16 q-14 2 -14 -16Z" fill="#7fb06f"/>')])) +
  '<text x="330" y="212" text-anchor="middle" font-size="11" fill="#5b6676">Week 16 zoomed in from atoms to organisms. Ecology zooms out from one organism to the whole Earth.</text></svg>')

LESSON = {
 "unit": "Unit 5: Ecosystems",
 "title": "Living and Nonliving Parts of an Ecosystem",
 "subtitle": "In Unit 4 you studied one organism, yourself, from the inside. Now you zoom out to see how organisms live together with the water, sunlight, soil and air around them. Florida, with its springs, swamps, pinelands and reefs, is one of the best places in the country to study ecosystems.",
 "objectives": [
  "Distinguish biotic (living) and abiotic (nonliving) factors in an ecosystem.",
  "Describe the levels of ecological organization: organism, population, community, ecosystem, biosphere.",
  "Explain how abiotic factors determine which organisms can live in an ecosystem.",
  "Identify limiting factors and explain carrying capacity.",
  "Investigate the biotic and abiotic factors of a local area with a field survey."],
 "vocab": [
  ["ecosystem", "All the living things in an area together with the nonliving parts of their environment."],
  ["biotic factor", "A living or once-living part of an ecosystem, such as plants, animals, fungi and bacteria."],
  ["abiotic factor", "A nonliving part of an ecosystem, such as sunlight, water, temperature, soil and air."],
  ["population", "All the members of one species living in an area."],
  ["community", "All the populations of different species living in an area."],
  ["limiting factor", "Anything that keeps a population from growing larger, such as food, water, space or predators."],
  ["carrying capacity", "The largest population an ecosystem can support over time."]],
 "reconnect": {
  "title": "Unit 4: The human body",
  "intro": "Your body is a system of parts working together. So is an ecosystem.",
  "items": [
   {"t":"order","q":"Week 16: Put these levels in order from smallest to largest.","items":["cell","tissue","organ","organ system","organism"],"pts":2,"why":"Today you keep zooming out past the organism."},
   {"t":"text","q":"Keeping stable internal conditions is called ___.","a":[{"all":[["homeostasis"]],"none":["not"]}],"show":"homeostasis","pts":2,"why":"Ecosystems also have balances that can be upset."},
   {"t":"text","q":"Which gas do your lungs take in that plants release during photosynthesis?","a":[{"all":[["oxygen","o2"]],"none":["not","carbon"]}],"show":"oxygen","pts":2,"why":"A connection between you and ecosystems."},
   {"t":"open","key":"rc_systems","q":"In Unit 4 you learned body systems depend on one another. Predict one way a plant and an animal in a Florida swamp might depend on each other.","min":12,"rows":2,"rubric":["A reasonable dependence (food, shelter, oxygen, seed spreading, pollination, nutrients from waste)"],"model":"A bird might eat a plant's berries and drop the seeds somewhere new, helping the plant spread while the plant feeds the bird."}]},
 "hook": {
  "title": "A River of Grass",
  "visual": LEVELS,
  "html": "<p>In 1947, the journalist <b>Marjory Stoneman Douglas</b> published <i>The Everglades: River of Grass</i>. She explained something many people had never understood: the Everglades is not a useless swamp but a slow-moving river, up to 60 miles wide and only inches deep in places, flowing south from Lake Okeechobee to Florida Bay. Sawgrass, alligators, wading birds, fish, and the water, sunlight and limestone beneath them all depend on one another. People had been draining it for farms and cities, and the whole system was in danger. That same year, Everglades National Park was dedicated.</p><p>The Everglades is also the homeland of the <b>Miccosukee</b> and <b>Seminole</b> peoples, who have lived with its seasons of flood and drought for generations.</p><div class='callout'><b>Big question:</b> How do living and nonliving things depend on each other in an ecosystem?</div>"},
 "learn": [
  {"title": "Biotic and Abiotic Factors",
   "html": "<p>Every <b>ecosystem</b> has two kinds of parts:</p><ul><li><b>Biotic factors</b> are living or once-living: plants, animals, fungi, bacteria, and also fallen leaves and logs, which were once alive.</li><li><b>Abiotic factors</b> are nonliving: sunlight, water, temperature, soil, rocks, air, salt and minerals.</li></ul><p>Biotic and abiotic factors constantly affect each other. Sunlight and water let sawgrass grow; sawgrass shelters fish; fish feed herons; when organisms die, bacteria and fungi break them down and return nutrients to the soil and water.</p>",
   "checks": [
    {"t":"blanks","q":"Biotic or abiotic?","sent":"A cypress tree: ___ &nbsp; Rainwater: ___ &nbsp; A rotting log: ___ &nbsp; Sand: ___","blanks":[[{"all":[["biotic"]],"none":["abiotic"]}],[{"all":[["abiotic"]],"none":["not"]}],[{"all":[["biotic"]],"none":["abiotic"]}],[{"all":[["abiotic"]],"none":["not"]}]],"show":"biotic; abiotic; biotic; abiotic","pts":4,"why":"A rotting log was once alive, so it is biotic."},
    {"t":"open","key":"fireabiotic","q":"Is fire a biotic or abiotic factor? Explain, and describe one way fire affects living things in a Florida longleaf pine forest.","min":25,"rows":3,"rubric":["Abiotic (nonliving), though it burns biotic material","An effect: clears brush, helps longleaf seeds sprout, keeps forest open for animals like gopher tortoises, returns nutrients"],"model":"Fire is abiotic because it is not alive, even though it burns living material. In longleaf pine forests, natural fires clear out shrubs, help longleaf seedlings grow, and keep the forest open so animals like gopher tortoises can find the plants they eat."}]},
  {"title": "Levels of Ecology",
   "html": "<p>In Week 16 you zoomed in from atoms to whole organisms. Ecology zooms out:</p><ol><li><b>Organism:</b> one living thing, such as one American alligator.</li><li><b>Population:</b> all the alligators living in one area.</li><li><b>Community:</b> all the populations living together: alligators, egrets, gar, apple snails, sawgrass, algae.</li><li><b>Ecosystem:</b> the community plus the abiotic factors: water, sunlight, limestone, temperature.</li><li><b>Biosphere:</b> all of Earth's ecosystems together.</li></ol>",
   "checks": [
    {"t":"text","q":"All the manatees living in Blue Spring State Park form a ___.","a":[{"all":[["population"]],"none":["not","community"]}],"show":"population","pts":2,"why":"One species in one area."},
    {"t":"text","q":"Manatees, fish, eelgrass and turtles in the spring together form a ___.","a":[{"all":[["community"]],"none":["not","population"]}],"show":"community","pts":2,"why":"Many populations of different species."},
    {"t":"open","key":"commvseco","q":"What is the difference between a community and an ecosystem? Use a Florida spring as your example.","min":25,"rows":3,"rubric":["A community is only the living things","An ecosystem adds the abiotic factors (water, temperature, sunlight, rock)","Spring example used"],"model":"A community is just the living things in the spring: manatees, fish, eelgrass and turtles. The ecosystem includes all those plus the nonliving parts, like the 72°F water, the sunlight and the limestone the spring flows from."}]},
  {"title": "Abiotic Factors Decide Who Lives Where",
   "html": "<p>Abiotic factors determine which organisms can survive in a place:</p><ul><li><b>Salt:</b> mangroves can live with their roots in salty water along the coast; most trees cannot.</li><li><b>Temperature:</b> Florida's springs stay about 72°F (22°C) all year, so manatees crowd into them in winter, when the Gulf and Atlantic can get cold enough to harm them.</li><li><b>Water depth and flooding:</b> sawgrass and cypress tolerate long floods; pine forests grow on slightly higher, drier ground.</li><li><b>Sunlight:</b> coral reefs in the Florida Keys need clear, shallow water so sunlight reaches the algae living inside the corals.</li></ul>",
   "checks": [
    {"t":"open","key":"manateewinter","q":"Explain why manatees gather in Florida springs during winter. Name the abiotic factor and describe what could happen to manatees without the springs.","min":25,"rows":3,"rubric":["Abiotic factor: water temperature (springs stay about 72°F)","Without warm water, manatees can suffer cold stress (illness or death) when the Gulf or Atlantic gets cold"],"model":"Springs stay about 72°F all year, while the ocean can get cold in winter. Manatees can't handle cold water for long; it can make them sick or even kill them, so they crowd into warm springs to survive."},
    {"t":"num","q":"A spring stays at 72°F. On a January morning the nearby river is 58°F. How many degrees warmer is the spring?","a":14,"unit":"degrees","pts":2,"why":"72 − 58 = 14."}]},
  {"title": "Limiting Factors and Carrying Capacity",
   "html": "<p>No population grows forever. <b>Limiting factors</b> hold populations in check: food, water, space, shelter, nesting sites, disease and predators. The largest population an ecosystem can support over time is its <b>carrying capacity</b>.</p><p>Example: Florida scrub-jays live only in Florida's rare oak scrub, where they nest in short scrub oaks and bury acorns. As scrub land has been cleared for buildings and orange groves, their populations have dropped, because the habitat, a limiting factor, shrank. They are now listed as a threatened species.</p><p>When a population grows above its carrying capacity, food or space runs out, and the population usually drops back down.</p>",
   "checks": [
    {"t":"text","q":"The largest population an ecosystem can support over time is its ___.","a":[{"all":[["carrying capacity"]],"none":["not"]}],"show":"carrying capacity","pts":2,"why":"Set by limiting factors."},
    {"t":"open","key":"scrubjay","q":"Name the main limiting factor for Florida scrub-jays and explain how people could help their population recover.","min":25,"rows":3,"rubric":["Limiting factor: oak scrub habitat (nesting sites, acorns), lost to development","A way to help: protect or restore scrub, controlled burns to keep scrub healthy, limit development"],"model":"Their main limiting factor is habitat: they can only live in oak scrub, which has been cleared for buildings and groves. People can help by protecting the scrub that's left, restoring cleared land and using controlled burns to keep the scrub low and healthy."}]}],
 "handson": {
  "title": "Quadrat Survey: Biotic and Abiotic Factors",
  "intro": "Mark a small square of ground and survey everything in it, like a field ecologist.",
  "materials": ["String or yarn (about 12 feet) and 4 sticks or pencils, or a hula hoop", "An outdoor thermometer", "A ruler", "A magnifying glass", "A notebook and pencil", "A cup of water (for a soil drainage test)", "Gloves", "Optional: a phone or camera"],
  "steps": [
   "Choose a spot in a yard, park or schoolyard. Make a 3-foot by 3-foot square with string and sticks (a quadrat), or lay down a hula hoop.",
   "Biotic survey: list every living or once-living thing you find in the square: plants (count or estimate), insects, spiders, worms, fungi, fallen leaves. Use the magnifying glass. Look but don't take animals out of their homes.",
   "Abiotic survey: record air temperature and ground temperature, the amount of sunlight (full sun, partial shade, full shade), whether the soil is sandy, muddy or rocky, and how long a cup of water takes to soak into the soil.",
   "Choose a second square in a different spot (shady versus sunny, or near water versus dry) and repeat.",
   "Safety: wear gloves and closed-toe shoes, watch for fire ants, poison ivy and snakes, don't touch unknown plants or animals, use insect repellent applied by an adult, and wash hands afterward. Don't collect in state parks."],
  "record": [
   {"t":"open","key":"quadrec","q":"Make a table comparing your two quadrats: biotic factors found, and abiotic measurements. Which square had more kinds of living things? Which abiotic factor do you think made the biggest difference, and why?","min":50,"rows":6,"rubric":["Data for both quadrats (biotic list and abiotic measurements)","Compares diversity","Identifies an abiotic factor and explains its effect with evidence"],"model":"Sunny square: 2 kinds of grass, dandelions, 6 ants, 1 beetle; air 84°F, ground 96°F, sandy soil, water soaked in in 8 seconds. Shady square under an oak: moss, 3 kinds of plants, fallen leaves, 2 earthworms, a mushroom, pill bugs; air 79°F, ground 75°F, darker soil, water soaked in in 30 seconds. The shady square had more kinds of living things. I think shade made the biggest difference: it kept the ground cooler and the soil moist, which worms, moss and fungi need."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"evergladesdrain","q":"In the 1900s, canals drained large parts of the Everglades. Using what you learned about biotic and abiotic factors, predict how draining water (an abiotic change) would affect at least three living things in the ecosystem.","min":67,"rows":6,"rubric":["Identifies water as the abiotic factor changed","Three predicted effects on organisms (fish lose habitat; wading birds lose food and nesting; alligators lose ponds; sawgrass replaced by other plants; fires spread; peat soil dries)","Shows connections between organisms (a chain of effects)"],"model":"Draining the water would shrink the shallow sheet of water fish and apple snails live in, so their populations would fall. Wading birds like wood storks feed on those fish, so they would lose food and nest less. Alligators dig ponds that hold water in the dry season; with less water overall, those ponds would dry up, hurting the animals that depend on them. Drier land also burns more easily, so fires could damage plants that need wet conditions."},
   {"t":"open","key":"douglasargue","q":"Marjory Stoneman Douglas called the Everglades a \"river of grass\" instead of a swamp. Why do you think that new description helped convince people to protect it? Connect to what you learned about argument in Unit 4.","min":49,"rows":5,"rubric":["\"River\" suggests flowing, living, valuable; \"swamp\" suggests useless land","Connects to persuasion: a vivid phrase (emotion) backed by scientific facts (logic)"],"model":"A \"swamp\" sounds like useless land to drain, but a \"river of grass\" sounds alive and moving, something worth protecting. Douglas used a vivid phrase, an emotional appeal, but she backed it with facts about how the water flows from Lake Okeechobee to Florida Bay, a logical appeal, just like the strong arguments we studied in Unit 4."}]},
 "exit": [
  {"t":"text","q":"Is sunlight a biotic or abiotic factor?","a":[{"all":[["abiotic"]],"none":["not abiotic"]}],"show":"abiotic","pts":2,"why":"It is not alive."},
  {"t":"text","q":"All the populations living in an area together form a ___.","a":[{"all":[["community"]],"none":["not","population"]}],"show":"community","pts":2,"why":"Add the abiotic factors and you have an ecosystem."},
  {"t":"text","q":"Anything that keeps a population from growing larger is a ___ factor.","a":[{"all":[["limiting"]],"none":["not"]}],"show":"limiting","pts":2,"why":"Food, water, space, predators, disease."},
  {"t":"open","key":"exit_depend","q":"Give one example of a biotic factor depending on an abiotic factor in a Florida ecosystem.","min":11,"rows":2,"rubric":["An accurate example (manatees and warm spring water; corals and sunlight; sawgrass and flooding; mangroves and salt water)"],"model":"Manatees depend on the warm 72°F water of Florida's springs to survive the winter."}],
 "next": "Week 22: food chains, food webs and the flow of energy."
}

TEACHER = {
 "standards": [
  "SC.7.L.17.3: Describe and investigate various limiting factors in the local ecosystem and their impact on native populations, including food, shelter, water, space, disease, parasitism, predation, and nesting sites.",
  "SC.7.L.17.2: Compare and contrast the relationships among organisms such as mutualism, predation, parasitism, competition, and commensalism.",
  "SC.6.L.14.1: Describe and identify patterns in the hierarchical organization of organisms from atoms to molecules to cells to tissues to organs to organ systems to organisms.",
  "SC.6.N.1.1: Define a problem from the sixth grade curriculum, use appropriate reference materials to support scientific understanding, plan and carry out scientific investigation of various types, such as systematic observations or experiments, identify variables, collect and organize data, interpret data in charts, tables, and graphics, analyze information, make predictions, and defend conclusions.",
  "NGSS MS-LS2-1: Analyze and interpret data to provide evidence for the effects of resource availability on organisms and populations of organisms in an ecosystem."],
 "materials": ["The interactive lesson", "String and 4 sticks (or a hula hoop), outdoor thermometer, ruler, magnifying glass", "A cup of water, gloves, notebook", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Unit 4 warm-up questions."],
  [5, "Hook", "Marjory Stoneman Douglas and the river of grass; the Miccosukee and Seminole peoples."],
  [10, "Biotic and abiotic", "Sort examples; discuss fire in longleaf pine forests."],
  [10, "Levels of ecology", "Connect to Week 16's levels; organism to biosphere."],
  [11, "Abiotic factors decide who lives where", "Mangroves, springs and manatees, sawgrass, coral reefs."],
  [11, "Limiting factors", "Florida scrub-jays; carrying capacity."],
  [7, "Assign", "Plan the quadrat survey; assign Think Deeper and the Exit Check."]],
 "key_questions": ["Is it living, once living or nonliving?", "Which abiotic factor makes this place right for this organism?", "What is limiting this population?", "What would happen if one factor changed?"],
 "misconceptions": ["Abiotic factors don't matter to living things.", "Dead things are abiotic.", "Populations can grow forever if there is food.", "Swamps are useless land."],
 "support": ["Use a two-column sorting chart (biotic/abiotic).", "Show photos of each Florida ecosystem.", "Provide a quadrat data table template."],
 "challenge": ["Read the first chapter of The Everglades: River of Grass (borrow from the library).", "Research the Comprehensive Everglades Restoration Plan and what it aims to fix."],
 "background": "<p>Florida's NGSSS place ecosystem benchmarks (SC.7.L.17.x) in Grade 7; KCE's Grade 6 scope teaches them in Unit 5 as planned, and the Grade 7 course should build on this unit rather than repeat it. Douglas's book was published in 1947; Everglades National Park was dedicated December 6, 1947. Most Florida springs stay about 68 to 72°F (Blue Spring is about 73°F); manatees experience cold stress below about 68°F. The Florida scrub-jay is federally listed as threatened (1987) and is found only in Florida. The Miccosukee Tribe of Indians of Florida and the Seminole Tribe of Florida have lands in and near the Everglades.</p>",
 "sources": ["National Park Service, Everglades National Park.", "Florida Fish and Wildlife Conservation Commission, Florida Manatee and Florida Scrub-Jay profiles.", "U.S. Fish and Wildlife Service, Florida Scrub-Jay.", "Miccosukee Tribe of Indians of Florida and Seminole Tribe of Florida, history pages."]
}

PRINT = {
 "directions": "Answer in complete sentences.",
 "items": [
  {"q":"Define biotic and abiotic factors and give two Florida examples of each.","a":"Biotic: living or once living (alligator, sawgrass). Abiotic: nonliving (spring water temperature, sunlight).","lines":3},
  {"q":"List the five levels of ecology from smallest to largest with an example of each.","a":"Organism (one manatee), population (all manatees in a spring), community (all living things there), ecosystem (plus water, sunlight, rock), biosphere (all of Earth).","lines":3},
  {"q":"Explain how one abiotic factor decides which organisms live in a Florida ecosystem.","a":"Example: salt water lets mangroves grow on coasts where most trees can't.","lines":2},
  {"q":"What is a limiting factor? Give three examples.","a":"Something that keeps a population from growing: food, water, space, shelter, predators, disease.","lines":2},
  {"q":"What is carrying capacity?","a":"The largest population an ecosystem can support over time.","lines":2},
  {"q":"Why are Florida scrub-jays threatened?","a":"Their oak scrub habitat has been cleared for development and agriculture.","lines":2}]
}
