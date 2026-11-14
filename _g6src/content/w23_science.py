WATER = ('<svg viewBox="0 0 660 300" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="The water cycle over Florida: evaporation, transpiration, condensation, precipitation, runoff and groundwater in the Floridan aquifer">'
  '<rect width="660" height="300" fill="#eaf2fb"/>'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The water cycle in Florida</text>'
  '<circle cx="600" cy="56" r="24" fill="#C9A84C"/><text x="600" y="92" text-anchor="middle" font-size="10" fill="#8a6d1f">sun powers it</text>'
  '<ellipse cx="250" cy="62" rx="70" ry="22" fill="#fff" stroke="#b9c3d0"/><ellipse cx="300" cy="56" rx="50" ry="18" fill="#fff" stroke="#b9c3d0"/><text x="270" y="64" text-anchor="middle" font-weight="bold" fill="#0A1F3D">condensation</text>'
  '<path d="M0 230 L250 230 Q300 215 340 222 L660 230 L660 300 L0 300Z" fill="#c8b48a"/>'
  '<path d="M420 226 Q520 222 660 230 L660 250 L420 250Z" fill="#9fc6e8"/><text x="560" y="244" text-anchor="middle" fill="#0047BA" font-weight="bold">Gulf of Mexico</text>'
  '<rect x="0" y="262" width="660" height="38" fill="#e6dcc0"/><text x="330" y="286" text-anchor="middle" fill="#8a6d1f" font-weight="bold">Floridan aquifer: water stored in limestone underground</text>'
  '<path d="M150 230 v-50 M140 196 l10 -16 l10 16 M134 210 l16 -20 l16 20" stroke="#2c6e22" stroke-width="5" fill="none"/>'
  '<defs><marker id="wc" viewBox="0 0 10 10" markerWidth="7" markerHeight="7" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="#0047BA"/></marker></defs>'
  '<path d="M520 220 Q500 150 330 80" fill="none" stroke="#0047BA" stroke-width="2.5" stroke-dasharray="6 4" marker-end="url(#wc)"/><text x="470" y="150" fill="#0047BA" font-weight="bold">evaporation</text>'
  '<path d="M150 176 Q170 120 210 82" fill="none" stroke="#2c6e22" stroke-width="2.5" stroke-dasharray="6 4" marker-end="url(#wc)"/><text x="40" y="130" fill="#2c6e22" font-weight="bold">transpiration</text><text x="40" y="144" fill="#2c6e22" font-size="10">(water from leaves)</text>'
  + ''.join(f'<path d="M{x} 92 l-6 16" stroke="#0047BA" stroke-width="2"/>' for x in (230, 250, 270, 290, 310)) +
  '<text x="225" y="128" fill="#0047BA" font-weight="bold">precipitation</text>'
  '<path d="M300 226 Q360 228 420 232" fill="none" stroke="#0047BA" stroke-width="2.5" marker-end="url(#wc)"/><text x="330" y="214" fill="#0047BA" font-size="10">runoff</text>'
  '<path d="M240 236 v28" stroke="#0047BA" stroke-width="2.5" stroke-dasharray="4 3" marker-end="url(#wc)"/><text x="250" y="254" fill="#0047BA" font-size="10">infiltration</text>'
  '<path d="M80 264 Q70 240 80 228" stroke="#0047BA" stroke-width="2.5" marker-end="url(#wc)" fill="none"/><text x="20" y="222" fill="#0047BA" font-size="10">spring</text></svg>')

CARBON = ('<svg viewBox="0 0 660 260" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="The carbon cycle: photosynthesis takes in carbon dioxide; respiration, decomposition and burning fuels release it">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The carbon cycle</text>'
  '<rect x="250" y="34" width="160" height="40" rx="10" fill="#5b6676"/><text x="330" y="58" text-anchor="middle" fill="#fff" font-weight="bold">carbon dioxide in the air</text>'
  + ''.join(f'<rect x="{x}" y="{y}" width="150" height="44" rx="10" fill="{c}"/><text x="{x+75}" y="{y+18}" text-anchor="middle" fill="#fff" font-weight="bold">{a}</text><text x="{x+75}" y="{y+34}" text-anchor="middle" fill="#fff" font-size="10">{b}</text>'
            for x, y, a, b, c in [(40, 120, "plants and algae", "store carbon in sugars", "#2c6e22"), (255, 200, "animals", "eat plants; store carbon", "#8a6d1f"), (470, 120, "decomposers", "break down dead things", "#a5552a"), (470, 200, "fossil fuels", "coal, oil, gas (ancient life)", "#0A1F3D")]) +
  '<defs><marker id="cc" viewBox="0 0 10 10" markerWidth="7" markerHeight="7" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="#0A1F3D"/></marker></defs>'
  '<path d="M255 70 Q150 80 115 118" fill="none" stroke="#2c6e22" stroke-width="2.5" marker-end="url(#cc)"/><text x="120" y="88" fill="#2c6e22" font-weight="bold">photosynthesis</text>'
  '<path d="M190 155 Q250 190 258 205" fill="none" stroke="#8a6d1f" stroke-width="2.5" marker-end="url(#cc)"/><text x="175" y="196" fill="#8a6d1f">eating</text>'
  '<path d="M185 118 L262 76" fill="none" stroke="#5b6676" stroke-width="2" marker-end="url(#cc)"/><text x="200" y="116" fill="#5b6676" font-size="10">respiration</text><path d="M330 198 Q330 140 330 78" fill="none" stroke="#5b6676" stroke-width="2.5" marker-end="url(#cc)"/><text x="338" y="140" fill="#5b6676" font-weight="bold">respiration</text>'
  '<path d="M520 118 Q480 80 412 62" fill="none" stroke="#a5552a" stroke-width="2.5" marker-end="url(#cc)"/><text x="440" y="104" fill="#a5552a">decomposition</text>'
  '<path d="M560 198 Q680 110 412 50" fill="none" stroke="#DB2F30" stroke-width="2.5" marker-end="url(#cc)"/><text x="600" y="108" fill="#DB2F30" font-weight="bold">burning</text>'
  '<text x="330" y="256" text-anchor="middle" font-size="10" fill="#5b6676">Carbon atoms are never used up; they keep moving between air, living things, soil, oceans and rock.</text></svg>')

LESSON = {
 "unit": "Unit 5: Ecosystems",
 "title": "Cycles of Matter: Water and Carbon",
 "subtitle": "Last week you learned that energy flows through an ecosystem and is lost as heat. Matter is different: the same atoms of water and carbon go around and around. The water in your glass may once have flowed through a Florida spring, fallen as rain in Africa or been breathed by a dinosaur.",
 "objectives": [
  "Explain the difference between energy flow and matter cycling in ecosystems.",
  "Describe the water cycle, including evaporation, transpiration, condensation, precipitation, runoff and groundwater.",
  "Explain how Florida's springs and the Floridan aquifer fit into the water cycle.",
  "Describe the carbon cycle, including photosynthesis, respiration, decomposition and burning fossil fuels.",
  "Model a cycle and explain how human activity can change it."],
 "vocab": [
  ["evaporation", "The change of liquid water into water vapor, powered by the sun's energy."],
  ["transpiration", "The release of water vapor from plant leaves."],
  ["condensation", "The change of water vapor into liquid droplets, forming clouds and dew."],
  ["precipitation", "Water falling from clouds as rain, snow, sleet or hail."],
  ["aquifer", "An underground layer of rock or sand that holds water."],
  ["cellular respiration", "The process in which living things use oxygen to break down sugar for energy, releasing carbon dioxide and water."],
  ["fossil fuel", "Coal, oil or natural gas, formed over millions of years from the remains of ancient living things."]],
 "reconnect": {
  "title": "Week 22: Food chains, webs and energy",
  "intro": "Energy flows; matter cycles. Start with last week's energy ideas.",
  "items": [
   {"t":"text","q":"About what percent of energy passes from one level of a food chain to the next?","a":["10","10%","ten","10 percent"],"show":"about 10 percent","pts":2,"why":"The rest is used or lost as heat."},
   {"t":"text","q":"Which organisms break down dead matter and return nutrients to the soil?","a":[{"all":[["decomposer","fungi","bacteria"]],"none":["not"]}],"show":"decomposers","pts":2,"why":"They are key to the carbon cycle today."},
   {"t":"text","q":"Mercury builds up in panthers because it is stored in the body, not used up. Is mercury energy or matter?","a":["^matter",{"all":[["matter"]],"none":["not matter","energy"]}],"show":"matter","pts":2,"why":"Matter is never used up; it moves and accumulates."},
   {"t":"open","key":"rc_energylost","q":"Last week you learned energy is lost as heat at each level. Where does that heat go, and can the ecosystem use it again?","min":12,"rows":2,"rubric":["Says where the heat goes","Says whether the food chain can reuse it and what that means for ecosystems"],"model":"The heat spreads into the air and eventually out into space. The food chain can't reuse it, so ecosystems need new energy from the sun all the time."}]},
 "hook": {
  "title": "Florida's Underground Ocean",
  "visual": WATER,
  "html": "<p>Below your feet in much of Florida lies the <b>Floridan aquifer</b>, one of the most productive aquifers in the world: layers of porous limestone, full of water like a giant sponge. Rain soaks into the ground, slowly fills the aquifer, and bubbles back up in more than 1,000 springs, one of the largest concentrations of freshwater springs on Earth. The aquifer also supplies drinking water to about 10 million people in Florida and nearby states.</p><p>When you drink a glass of water in Orlando, Gainesville or Tallahassee, it may have fallen as rain years or even decades ago and traveled through the limestone. Water, like all matter, is never used up. It cycles.</p><div class='callout'><b>Big question:</b> How do water and carbon cycle through Earth's living and nonliving systems?</div>"},
 "learn": [
  {"title": "Energy Flows, Matter Cycles",
   "html": "<p>Ecosystems need two things: <b>energy</b> and <b>matter</b>.</p><ul><li><b>Energy</b> flows in one direction: from the sun to producers to consumers, with most lost as heat along the way. Ecosystems need a constant new supply of sunlight.</li><li><b>Matter</b> (atoms of water, carbon, nitrogen and other elements) is <b>recycled</b>. The same atoms move again and again between air, water, soil, rock and living things. Earth gets almost no new matter from space.</li></ul><p>Decomposers are the great recyclers: they break dead organisms back into simple substances that producers can use again.</p>",
   "checks": [
    {"t":"blanks","q":"Energy or matter?","sent":"It flows in one direction and is lost as heat: ___. It is recycled again and again: ___.","blanks":[[{"all":[["energy"]],"none":["not","matter"]}],[{"all":[["matter"]],"none":["not","energy"]}]],"show":"energy; matter","pts":2,"why":"Energy flows; matter cycles."},
    {"t":"open","key":"atomstory","q":"A carbon atom in a sawgrass leaf could later be part of a marsh rabbit, a panther and the air. Describe one possible journey for that atom, using at least three living or nonliving stops.","min":30,"rows":3,"rubric":["At least three stops in a logical order","Correct processes linking them"],"model":"The carbon atom in a sawgrass leaf is eaten by a marsh rabbit and becomes part of its muscle. A panther eats the rabbit. When the panther breathes out, the atom leaves as carbon dioxide in the air, where another sawgrass plant takes it in during photosynthesis."}]},
  {"title": "The Water Cycle",
   "html": "<p>The sun powers the water cycle:</p><ul><li><b>Evaporation:</b> the sun heats oceans, lakes and rivers, turning liquid water into invisible water vapor.</li><li><b>Transpiration:</b> plants pull water up from their roots and release vapor through tiny pores in their leaves. A single large tree can release hundreds of liters (about 100 gallons) of water a day.</li><li><b>Condensation:</b> as vapor rises and cools, it forms tiny droplets: clouds, fog and dew.</li><li><b>Precipitation:</b> droplets combine and fall as rain (or snow, sleet or hail).</li><li><b>Runoff and infiltration:</b> rain flows over land into rivers and the sea, or soaks into the ground to become <b>groundwater</b>.</li></ul><p>Florida's summer thunderstorms show the cycle in fast motion: morning sun evaporates water from the land and the surrounding Gulf and Atlantic; by afternoon, rising moist air condenses into towering clouds that pour rain.</p>",
   "checks": [
    {"t":"order","q":"Put these steps in a logical order, starting with water in the Gulf.","items":["evaporation","condensation","precipitation","runoff into a river"],"pts":2,"why":"Then the river carries water back to the sea."},
    {"t":"text","q":"Water vapor released from plant leaves is called ___.","a":[{"all":[["transpiration"]],"none":["not"]}],"show":"transpiration","pts":2,"why":"Plants are part of the water cycle."},
    {"t":"open","key":"afternoonstorm","q":"Explain why Florida often has thunderstorms on summer afternoons rather than mornings, using water-cycle words.","min":25,"rows":3,"rubric":["Explains what the morning sun does, using a water-cycle word", "Explains what happens to the rising air by afternoon, using at least two more water-cycle words"],"model":"In the morning, the sun heats the land and the water around Florida, so lots of water evaporates. The warm, moist air rises, cools and condenses into big storm clouds by afternoon, and then the water falls as rain."}]},
  {"title": "Springs and the Floridan Aquifer",
   "html": "<p>In Florida, much of the rain that infiltrates the ground seeps into the <b>Floridan aquifer</b>, a thick layer of limestone with countless tiny spaces and caves filled with water. Rainwater is slightly acidic, and over thousands of years it has dissolved the limestone, carving underground channels and <b>sinkholes</b>.</p><p>Where the water pressure pushes groundwater up to the surface, a <b>spring</b> forms. Silver Springs, Wakulla Springs and Rainbow Springs each pour out hundreds of millions of gallons a day. The water stays about 68 to 72°F all year, which is why manatees gather there in winter, as you learned in Week 21.</p><p>When people pump too much groundwater, or when fertilizer and wastewater soak into the ground, spring flow can drop and nitrates can feed algae that cloud the water.</p>",
   "checks": [
    {"t":"text","q":"What is the name of the huge underground layer of water-filled limestone beneath much of Florida?","a":[{"all":[["floridan","florida aquifer"]],"none":["not"]}],"show":"the Floridan aquifer","pts":2,"why":"It feeds Florida's springs."},
    {"t":"open","key":"springthreat","q":"Explain how fertilizer used on lawns and farms miles from a spring can affect the spring's ecosystem. Use the water cycle in your answer.","min":30,"rows":3,"rubric":["Traces the fertilizer's path to the spring using water-cycle steps", "Explains at least one effect on living things in the spring"],"model":"When it rains, water soaks into the ground and carries fertilizer with it into the aquifer. The groundwater flows underground to the spring, bringing extra nutrients that feed algae. The algae cloud the water, block sunlight from eelgrass and harm the animals that depend on the spring."}]},
  {"title": "The Carbon Cycle",
   "visual": CARBON,
   "html": "<p>Carbon is in every living thing: in sugars, proteins, fats and DNA. It cycles too:</p><ul><li><b>Photosynthesis</b> (Unit 2): plants and algae take in carbon dioxide from the air and use sunlight to make sugar.</li><li><b>Eating:</b> animals take in carbon when they eat plants or other animals.</li><li><b>Cellular respiration:</b> all living things, plants included, break down sugar for energy and release carbon dioxide. (You breathe it out every few seconds.)</li><li><b>Decomposition:</b> decomposers release carbon from dead organisms back into the air and soil.</li><li><b>Fossil fuels:</b> over millions of years, some buried remains became coal, oil and natural gas. Burning them releases that ancient carbon as carbon dioxide.</li></ul><p>Scientists have measured carbon dioxide in the air since 1958 at Mauna Loa in Hawaii. It has risen from about 315 parts per million then to more than 420 today, mainly from burning fossil fuels, which traps more heat in Earth's atmosphere.</p>",
   "checks": [
    {"t":"text","q":"Which carbon-cycle process removes carbon dioxide from the air?","a":[{"all":[["photosynth"]],"none":["not photosynth"]}],"show":"photosynthesis","pts":2,"why":"Respiration releases carbon dioxide."},
    {"t":"num","q":"Carbon dioxide in the air was about 315 parts per million in 1958 and about 425 in 2024. By how many parts per million did it rise?","a":110,"unit":"ppm","pts":2,"why":"425 − 315 = 110."},
    {"t":"open","key":"fossilcarbon","q":"Fossil fuels formed from living things millions of years ago. Explain why burning them adds carbon to today's air even though that carbon was once part of the cycle.","min":30,"rows":3,"rubric":["Explains where the carbon was for millions of years", "Explains why releasing it now raises carbon dioxide in the air"],"model":"The carbon in fossil fuels was locked underground for millions of years, out of the active cycle. Burning coal, oil and gas releases that stored carbon as carbon dioxide all at once, much faster than plants and oceans can take it back in, so the amount in the air goes up."}]}],
 "handson": {
  "title": "Water Cycle in a Bag and Breath Test",
  "intro": "Build a mini water cycle, then test how plants and people move carbon dioxide.",
  "materials": ["A clear zipper sandwich bag", "Water and blue food coloring (optional)", "A permanent marker", "Tape", "A sunny window", "A 1/4-cup measure", "2 clear cups", "For the indicator: a few red cabbage leaves, a knife, a heat-safe bowl, hot water and a strainer (adult only), or bromothymol blue from an aquarium pH test kit (add a few drops to a cup of tap water)", "A drinking straw", "A sprig of an aquarium plant such as elodea (optional, from a pet store)", "Paper and pencil"],
  "steps": [
   "Water cycle bag: draw a sun, clouds and the ground on the bag with marker. Add about 1/4 cup of water (a drop of blue coloring helps you see it). Seal it and tape it to a sunny window.",
   "Check every few hours for 2 days. Look for droplets forming near the top (condensation) and running down (precipitation).",
   "Breath test: pour cabbage juice indicator into two cups. Using a straw, gently blow bubbles into one cup for 1 to 2 minutes (blow out only; never suck in). Compare the colors with the unbreathed control cup. Carbon dioxide forms a weak acid in water, which changes the indicator's color.",
   "Optional: put an elodea sprig in the color-changed cup and set it in sunlight for several hours. Watch whether the color shifts back as the plant takes in carbon dioxide.",
   "Safety: an adult does all chopping and makes the cabbage juice with hot water; don't drink any of the liquids; wash hands afterward; store the indicator, bromothymol blue and food coloring where young children and pets can't reach them (food coloring and cabbage juice stain). Never release aquarium plants or water outdoors; throw the elodea in the trash, because it is invasive in Florida."],
  "record": [
   {"t":"open","key":"bagrec","q":"Describe what you saw in the water cycle bag over 2 days. Label which parts of the water cycle happened, and name one way the bag is not like the real water cycle.","min":40,"rows":4,"rubric":["Observations over time","Evaporation, condensation and precipitation identified","A limit"],"model":"After a few hours, fog appeared on the inside of the bag; by evening there were droplets at the top that slid down. The sun's heat caused evaporation, the cooler top caused condensation, and the dripping was like precipitation. Unlike the real cycle, the bag is sealed, with no plants, rivers, oceans or groundwater."},
   {"t":"open","key":"breathrec","q":"What color change did you see after blowing bubbles? What does it show about the carbon cycle? If you tried the plant, what happened?","min":30,"rows":3,"rubric":["Describes the color change compared with the control cup", "Explains what in your breath caused it and which process produced it", "Reports and explains the plant result, or notes honestly that you did not try it"],"model":"The purple cabbage juice turned pinkish after I blew bubbles, because my breath contains carbon dioxide from cellular respiration, which made the water slightly acidic. When I put the elodea in sunlight for an afternoon, the color slowly shifted back toward purple, because the plant used the carbon dioxide for photosynthesis."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"pavement","q":"A new shopping center covers a Florida field with pavement and buildings. Predict how this changes the water cycle in that area, including what happens to infiltration, runoff and the aquifer.","min":48,"rows":6,"rubric":["Predicts what happens to infiltration and runoff", "Predicts the effect on the aquifer and springs", "Considers what removing the plants changes"],"model":"Pavement stops rain from soaking into the ground, so infiltration drops. More water runs off the parking lot into storm drains, carrying oil and litter into rivers and lakes and causing flooding. With less water soaking in, less recharges the Floridan aquifer, which over time can lower spring flow. Removing the field's plants also means less transpiration."},
   {"t":"open","key":"treesolution","q":"Some people propose planting more trees to reduce carbon dioxide in the air. Use the carbon cycle to explain why that could help, and give one limit of this solution.","min":54,"rows":5,"rubric":["Explains how trees remove and store carbon", "Gives one limit, explained"],"model":"Trees take in carbon dioxide during photosynthesis and store the carbon in their wood for decades or even centuries, so more trees can pull carbon out of the air. But it takes many years for trees to grow, and when trees die and decompose or burn, they release that carbon again. Trees alone can't absorb carbon as fast as burning fossil fuels releases it."}]},
 "exit": [
  {"t":"text","q":"Water vapor cooling into droplets to form clouds is called ___.","a":[{"all":[["condensation"]],"none":["not"]}],"show":"condensation","pts":2,"why":"Then precipitation falls."},
  {"t":"text","q":"Which process returns carbon dioxide to the air every time you breathe out?","a":[{"all":[["respiration"]],"none":["not"]}],"show":"cellular respiration","pts":2,"why":"All living things do it."},
  {"t":"text","q":"Where does the water in Florida's springs come from?","a":[{"all":[["aquifer","groundwater","ground water","floridan","underground"]],"none":["not"]},{"all":[["rain"],["ground","soak","infiltrat","limestone"]]}],"show":"the Floridan aquifer (groundwater from rain)","pts":2,"why":"Rain soaks in and flows out at springs."},
  {"t":"open","key":"exit_cycle","q":"How is the way matter moves through an ecosystem different from the way energy moves?","min":12,"rows":2,"rubric":["Describes how matter moves","Contrasts it with how energy moves"],"model":"Matter is recycled over and over, but energy flows in one direction and is lost as heat, so the sun must keep supplying it."}],
 "next": "Week 24: how organisms interact."
}

TEACHER = {
 "standards": [
  "SC.8.L.18.4: Cite evidence that living systems follow the Laws of Conservation of Mass and Energy.",
  "SC.8.L.18.3: Construct a scientific model of the carbon cycle to show how matter and energy are continuously transferred within and between organisms and their physical environment.",
  "SC.6.E.7.2: Investigate and apply how the cycling of water between the atmosphere and hydrosphere has an effect on weather patterns and climate.",
  "SC.6.N.3.4: Identify the role of models in the context of the sixth grade science benchmarks.",
  "NGSS MS-LS2-3: Develop a model to describe the cycling of matter and flow of energy among living and nonliving parts of an ecosystem."],
 "materials": ["The interactive lesson", "A zipper bag, water, food coloring, marker, tape", "Red cabbage juice indicator (adult-made) or bromothymol blue, 2 clear cups, a straw", "Optional: an elodea sprig", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 22 warm-up questions."],
  [5, "Hook", "The Floridan aquifer, an underground ocean."],
  [9, "Energy flows, matter cycles", "Trace a carbon atom's journey."],
  [11, "Water cycle", "Read the diagram; afternoon thunderstorms."],
  [11, "Springs and the aquifer", "Limestone, sinkholes, springs; fertilizer and overpumping."],
  [12, "Carbon cycle", "Photosynthesis, respiration, decomposition, fossil fuels; the Mauna Loa record."],
  [6, "Assign", "Start the water cycle bag; assign the breath test, Think Deeper and the Exit Check."]],
 "key_questions": ["Is this energy or matter, and is it flowing or cycling?", "Where does this water or carbon go next?", "What powers this cycle?", "How do people change this cycle?"],
 "misconceptions": ["Plants don't do respiration.", "Clouds are water vapor (they are liquid droplets or ice).", "Matter is used up or destroyed in ecosystems.", "Groundwater is underground lakes or rivers everywhere (mostly it fills spaces in rock)."],
 "support": ["Act out the water cycle as a single water drop.", "Color-code the carbon cycle arrows (in versus out of the air).", "Provide a cycle vocabulary card."],
 "challenge": ["Research how much water your county pumps from the aquifer and where it goes.", "Find the latest Mauna Loa carbon dioxide reading from NOAA and graph the trend for five years."],
 "background": "<p>The Floridan aquifer system underlies all of Florida and parts of Georgia, Alabama and South Carolina and supplies drinking water to roughly 10 million people (USGS). Florida has more than 1,000 documented springs. The Mauna Loa record (Keeling Curve) began in 1958 at about 315 ppm; annual averages passed 420 ppm in 2023 and rose to about 424 to 427 ppm in 2024 (NOAA). Matter cycling standards appear in Florida's Grade 8 (SC.8.L.18.x); KCE teaches them here per the Grade 6 scope. Red cabbage indicator turns pinker in acid; carbonated water from breath gives a mild change that is best seen against an unbreathed control cup.</p>",
 "sources": ["U.S. Geological Survey, Floridan Aquifer System; The Water Cycle.", "Florida Department of Environmental Protection, Florida's Springs.", "NOAA Global Monitoring Laboratory, Trends in Atmospheric Carbon Dioxide (Mauna Loa).", "NASA Earth Observatory, The Carbon Cycle."]
}

PRINT = {
 "directions": "Answer in complete sentences.",
 "items": [
  {"q":"Explain the difference between how energy and matter move through an ecosystem.","a":"Energy flows one way and is lost as heat; matter is recycled again and again.","lines":2},
  {"q":"Describe the water cycle using evaporation, transpiration, condensation, precipitation and runoff.","a":"Sun evaporates water and plants transpire; vapor condenses into clouds; precipitation falls; water runs off or soaks in.","lines":3},
  {"q":"How do Florida's springs connect to the water cycle?","a":"Rain infiltrates into the Floridan aquifer, flows through limestone and comes back up at springs.","lines":2},
  {"q":"Name four processes in the carbon cycle and whether each adds CO2 to the air or removes it.","a":"Photosynthesis removes; respiration, decomposition and burning fossil fuels add.","lines":2},
  {"q":"Why has the amount of carbon dioxide in the air risen since 1958?","a":"Mainly because people burn fossil fuels, releasing carbon stored underground for millions of years.","lines":2},
  {"q":"Rain can take years to travel through the aquifer. Explain why a drought two years ago could still lower a spring's flow today.","a":"Spring water fell as rain years earlier; less rain then means less water reaching the spring now.","lines":2}]
}
