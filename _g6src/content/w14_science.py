SIZES = ('<svg viewBox="0 0 660 220" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Size scale comparing a sand grain, a hair, a paramecium, a human cell, a bacterium and a virus">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">How small is a microorganism? (1 millimeter = 1,000 micrometers)</text>'
  + ''.join(f'<g transform="translate({60+i*108},0)">{pic}<text x="0" y="168" text-anchor="middle" font-weight="bold">{name}</text><text x="0" y="184" text-anchor="middle" font-size="11" fill="#5b6676">{size}</text></g>'
            for i, (pic, name, size) in enumerate([
              ('<circle cx="0" cy="100" r="44" fill="#e7cf95" stroke="#8a6d1f" stroke-width="2"/>', "sand grain", "about 1,000 µm"),
              ('<rect x="-6" y="40" width="12" height="110" rx="5" fill="#5a3a1a"/>', "human hair", "about 70 µm wide"),
              ('<ellipse cx="0" cy="100" rx="40" ry="14" fill="#bfe0a8" stroke="#2c6e22" stroke-width="2" transform="rotate(-20 0 100)"/>', "paramecium", "about 200 µm long"),
              ('<circle cx="0" cy="100" r="18" fill="#f3c7c7" stroke="#DB2F30" stroke-width="2"/><circle cx="0" cy="100" r="6" fill="#DB2F30"/>', "cheek cell", "about 50 µm"),
              ('<rect x="-7" y="96" width="14" height="6" rx="3" fill="#0047BA"/>', "bacterium", "about 2 µm"),
              ('<circle cx="0" cy="99" r="1.5" fill="#6b3fa0"/>', "virus", "about 0.1 µm")])) +
  '<text x="330" y="208" text-anchor="middle" font-size="11" fill="#5b6676">Not drawn to scale. Viruses are not living cells.</text></svg>')

MICROBES = ('<svg viewBox="0 0 660 200" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Helpful and harmful microorganisms">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Microbes: mostly helpful, sometimes harmful</text>'
  '<rect x="20" y="36" width="300" height="150" rx="12" fill="#e6f2e1" stroke="#3d9a2f" stroke-width="2"/><text x="170" y="58" text-anchor="middle" font-weight="bold" fill="#2c6e22">HELPFUL</text>'
  + ''.join(f'<text x="36" y="{84+i*20}" font-size="12">• {t}</text>' for i, t in enumerate(["decomposers recycle dead plants and animals", "root bacteria add nitrogen to soil", "gut bacteria help digest food", "yeast and bacteria make bread, yogurt, cheese", "ocean plankton make much of Earth's oxygen"])) +
  '<rect x="340" y="36" width="300" height="150" rx="12" fill="#fde8e8" stroke="#DB2F30" stroke-width="2"/><text x="490" y="58" text-anchor="middle" font-weight="bold" fill="#DB2F30">HARMFUL</text>'
  + ''.join(f'<text x="356" y="{84+i*20}" font-size="12">• {t}</text>' for i, t in enumerate(["bacteria cause strep throat and food poisoning", "protists cause malaria and red tide", "fungi cause athlete's foot and spoil food", "viruses cause colds and flu", "(but viruses are not living cells)"])) +
  '</svg>')

LESSON = {
 "unit": "Unit 3: The Diversity of Life",
 "title": "Microorganisms",
 "subtitle": "Most living things on Earth are too small to see. Microorganisms recycle nutrients, make oxygen, help digest our food and give us bread and medicines, and a few of them cause disease.",
 "objectives": [
  "Describe the main groups of microorganisms (bacteria, archaea, protists and microscopic fungi) and explain why viruses are not counted as living.",
  "Use metric units to compare the sizes of microorganisms.",
  "Explain how microorganisms help ecosystems, people and food production.",
  "Compare bacteria, viruses, fungi and protists that cause infections, and explain how hand-washing and antibiotics work.",
  "Design and carry out a fair test of hand-washing, identifying variables."],
 "vocab": [
  ["microorganism", "A living thing too small to see without a microscope; also called a microbe."],
  ["bacteria", "Single-celled organisms with no nucleus; found almost everywhere."],
  ["protist", "A usually single-celled organism with a nucleus, such as an amoeba, a paramecium or an alga."],
  ["decomposer", "An organism that breaks down dead plants and animals and returns nutrients to the soil."],
  ["pathogen", "A microorganism or virus that causes disease."],
  ["antibiotic", "A medicine that kills bacteria or stops them from growing; it does not work on viruses."],
  ["micrometer (µm)", "One millionth of a meter; 1,000 micrometers = 1 millimeter."]],
 "reconnect": {
  "title": "Week 13: Keys for identifying organisms",
  "intro": "Scientists identify microbes with keys too, using traits seen under a microscope. Review last week.",
  "items": [
   {"t":"text","q":"What is the name for a tool that identifies organisms through a series of paired, opposite choices?","a":[{"all":[["dichotomous"]],"none":["not"]}],"show":"a dichotomous key","pts":2,"why":"Dicho = in two."},
   {"t":"num","q":"How many couplets does a key need to identify 10 different organisms?","a":9,"unit":"couplets","pts":2,"why":"Always one fewer couplet than organisms: 10 − 1 = 9."},
   {"t":"text","q":"A leaf edge with small jagged points is called ___ (the opposite of smooth or entire).","a":[{"all":[["toothed","teeth","serrated"]],"none":["not","smooth"]}],"show":"toothed","pts":2,"why":"The margin is toothed."},
   {"t":"open","key":"rc_color","q":"Why should a good key avoid color as a trait?","min":10,"rows":2,"rubric":["Color changes with season, age or light, so the same organism could key out two ways"],"model":"Color changes with the season, the leaf's age and the light, so the same tree could be identified two different ways."}]},
 "hook": {
  "title": "Red Water on the Gulf Coast",
  "html": "<p>Some summers and falls, Florida's Gulf beaches turn strange. The water looks reddish brown, dead fish wash ashore, and people walking on the sand start coughing. The cause is a living thing so small that thousands could fit on the head of a pin: <i>Karenia brevis</i>, a single-celled protist. When conditions are right, it multiplies into a <b>red tide</b>, and the toxin it makes harms fish, manatees, dolphins and people's lungs.</p><p>Yet other microorganisms make the oxygen you breathe, help turn your food into energy and gave us some of the most important medicines in history.</p><div class='callout'><b>Big question:</b> How can living things too small to see shape the whole planet?</div>"},
 "learn": [
  {"title": "Meet the Microbes",
   "visual": SIZES,
   "html": "<p>In Week 6 you learned that Antonie van Leeuwenhoek was the first to see microorganisms, which he called \"animalcules,\" or \"little animals.\" Today scientists know microbes include:</p><ul><li><b>Bacteria:</b> single cells with <b>no nucleus</b>, usually 1 to 5 micrometers long. They live in soil, water, air, ice, hot springs and inside you.</li><li><b>Archaea:</b> look like bacteria but are a separate domain (Week 12); many live in extreme places like salty lakes and hot springs.</li><li><b>Protists:</b> usually single cells <b>with a nucleus</b>, such as amoebas, paramecia, diatoms and <i>Karenia brevis</i>.</li><li><b>Microscopic fungi:</b> such as the yeast from Week 11 and the molds that grow on old bread.</li></ul><p><b>Viruses</b> are even smaller, but as you learned in Week 11, most biologists do not call them living, because they are not cells and can only copy themselves inside a living cell.</p><p>Microbes are measured in <b>micrometers (µm)</b>: 1 millimeter = 1,000 micrometers.</p>",
   "checks": [
    {"t":"num","q":"A bacterium is about 2 micrometers long. How many could line up end to end across a sand grain 1 millimeter (1,000 µm) wide?","a":500,"unit":"bacteria","pts":2,"why":"1,000 ÷ 2 = 500."},
    {"t":"text","q":"Bacteria and protists are both single-celled, but only protists have a ___.","a":[{"all":[["nucleus","nuclei"]],"none":["not"]}],"show":"nucleus","pts":2,"why":"Bacteria have no nucleus; protists do."},
    {"t":"text","q":"What group of microorganism is the red tide organism Karenia brevis?","a":[{"all":[["protist","dinoflagellate"]],"none":["not","bacteria","bacterium"]}],"show":"a protist","pts":2,"why":"It is a single-celled organism with a nucleus."},
    {"t":"open","key":"everywhere","q":"Bacteria live in hot springs, polar ice, deep oceans and inside your body. Why might being tiny and single-celled help them live in so many places?","min":20,"rows":2,"rubric":["Small size lets them spread easily (air, water, on surfaces) and need few resources","They reproduce quickly, so populations adapt to many conditions"],"model":"Because they are tiny, bacteria are carried easily by air, water and animals, and they need very little food or space. They also reproduce very fast, so some can survive almost anywhere."}]},
  {"title": "Helpful Microbes",
   "visual": MICROBES,
   "html": "<p>Most microbes are harmless or helpful:</p><ul><li><b>Decomposers:</b> bacteria and fungi break down dead leaves, logs and animals, returning nutrients to the soil. Without them, the planet would be buried in dead matter.</li><li><b>Soil and roots:</b> bacteria living in the roots of beans, peanuts and clover turn nitrogen from the air into a form plants can use.</li><li><b>Oxygen:</b> tiny ocean organisms called phytoplankton make roughly half of the oxygen produced on Earth through photosynthesis.</li><li><b>Food:</b> yeast makes bread rise; bacteria turn milk into yogurt and cheese and cabbage into sauerkraut.</li><li><b>Your body:</b> trillions of bacteria in your gut help digest food and make some vitamins.</li></ul><p><b>Medicine from mold:</b> in 1928, Scottish scientist Alexander Fleming noticed that a mold growing on one of his bacteria dishes had killed the bacteria around it. That mold, <i>Penicillium</i>, led to <b>penicillin</b>, the first widely used antibiotic, which has saved millions of lives.</p>",
   "checks": [
    {"t":"text","q":"A fallen oak log in a Florida hammock turns soft and crumbly over a few years as fungi and bacteria break it down. What role are those fungi and bacteria playing?","a":[{"all":[["decompos"]],"none":["not","producer","consumer"]}],"show":"decomposers","pts":2,"why":"Decomposers break down dead matter and return nutrients to the soil."},
    {"t":"text","q":"Which scientist noticed in 1928 that a mold killed the bacteria around it, leading to penicillin?","a":[{"all":[["fleming"]],"none":["not"]}],"show":"Alexander Fleming","pts":2,"why":"The mold was Penicillium."},
    {"t":"open","key":"nodecomp","q":"Imagine all decomposers on Earth disappeared. Describe two things that would happen to a Florida forest over the next few years.","min":30,"rows":3,"rubric":["Dead leaves, logs and animals would pile up instead of breaking down","Soil would run out of nutrients, so new plants could not grow well (the whole food web suffers)"],"model":"Dead leaves, fallen branches and dead animals would pile up and never rot away. The nutrients locked in them would not return to the soil, so new plants would grow poorly, and the animals that eat those plants would suffer too."},
    {"t":"open","key":"luck","q":"Fleming's discovery started with an accident: a mold got into his dish. Why do you think he noticed it when someone else might have thrown the dish away? What does this say about how science works?","min":25,"rows":3,"rubric":["He observed carefully and asked why the bacteria near the mold had died","Science depends on curiosity and careful observation, not only planned experiments (chance favors a prepared mind)"],"model":"Fleming looked carefully and asked why there were no bacteria around the mold instead of just cleaning the dish. Science often moves forward when someone notices something unexpected and is curious enough to investigate it."}]},
  {"title": "Harmful Microbes and How We Fight Them",
   "html": "<p>A <b>pathogen</b> is anything that causes disease. Different types cause different infections:</p><ul><li><b>Bacteria:</b> strep throat, food poisoning from <i>Salmonella</i>, and Hansen's disease (leprosy).</li><li><b>Viruses:</b> colds, flu and chickenpox.</li><li><b>Fungi:</b> athlete's foot and ringworm (a skin infection, not a worm).</li><li><b>Protists and other parasites:</b> malaria, spread by mosquitoes.</li></ul><p><b>Hand-washing</b> with soap and water for at least 20 seconds removes many germs. <b>Antibiotics</b> kill bacteria or stop their growth, but they do <b>not</b> work on viruses. When antibiotics are overused, the few bacteria that survive can multiply, creating <b>antibiotic-resistant</b> bacteria that are harder to treat.</p><p><b>A scientist to know:</b> in 1915, Alice Ball, a 23-year-old African American chemist at the College of Hawaii, developed a way to turn oil from the chaulmoogra tree into an injectable medicine for Hansen's disease. It was the best treatment for decades. She died at 24, and another scientist published her work without giving her credit. Today it is known as the Ball Method.</p>",
   "checks": [
    {"t":"text","q":"Antibiotics can kill bacteria. What kind of pathogen do they not work on, such as the ones that cause colds and flu?","a":[{"all":[["virus","viral"]],"none":["not"]}],"show":"viruses","pts":2,"why":"Viruses are not cells, so antibiotics cannot attack them."},
    {"t":"blanks","q":"Match each disease to the type of pathogen that causes it.","sent":"Strep throat: ___ &nbsp; Malaria: ___ &nbsp; Athlete's foot: ___","blanks":[[{"all":[["bacteri"]],"none":["not","virus","fung","protist"]}],[{"all":[["protist","parasit","plasmodium"]],"none":["not","virus","bacteri","fung"]}],[{"all":[["fung"]],"none":["not","virus","bacteri","protist"]}]],"show":"bacteria; protist (parasite); fungus","pts":3,"why":"Strep is bacterial; malaria is caused by a protist parasite; athlete's foot is a fungus."},
    {"t":"open","key":"resistance","q":"Explain in your own words how overusing antibiotics can create antibiotic-resistant bacteria.","min":25,"rows":3,"rubric":["A few bacteria naturally survive the antibiotic","Those survivors multiply, so the new population is mostly resistant and harder to treat"],"model":"When antibiotics are used, most bacteria die, but a few that happen to be tougher survive. Those survivors multiply, so soon most of the bacteria are the tough kind, and the antibiotic no longer works against them."},
    {"t":"open","key":"aliceball","q":"Alice Ball's work was published by someone else without credit. Why does it matter that scientists today recognize who really made a discovery?","min":25,"rows":3,"rubric":["Fairness and honesty: people deserve credit for their work","Recognition shows that scientists come from all backgrounds and inspires young people; accurate history"],"model":"It matters because it is fair and honest to give people credit for their work. Recognizing Alice Ball also shows that great scientists come from every background, which can inspire students who might not otherwise see themselves as scientists."}]},
  {"title": "Testing Microbes Safely: A Fair Test",
   "html": "<p>You cannot see bacteria and mold spores on your hands, but you can see the colonies they grow into. In this week's hands-on you will test whether hand-washing changes how much mold grows on bread.</p><p>A <b>fair test</b> changes only one thing at a time:</p><ul><li><b>Independent variable</b> (what you change): how the hands were cleaned (not touched, unwashed hands, hands washed with soap).</li><li><b>Dependent variable</b> (what you measure): how much of each slice is covered with mold, as a percent, each day.</li><li><b>Controlled variables</b> (kept the same): bread type, slice size, bag type, a few drops of water, temperature and place.</li><li><b>Control:</b> a slice touched only with clean tongs, to compare against.</li></ul><p><b>Safety:</b> never eat the test bread, and never open the bags once they are sealed. Some people are allergic to mold. When you finish, throw the bags away still sealed.</p>",
   "checks": [
    {"t":"text","q":"A different student tests whether bread kept in the refrigerator grows less mold than bread kept on the counter. What is the independent variable in her test?","a":[{"all":[["temperature","where","location","place","stor","fridge","refrigerat","counter","cold","warm"]],"none":["not","amount of mold","how much mold","mold growth"]}],"show":"where the bread is stored (its temperature)","pts":2,"why":"She changes only where the bread is stored; the mold is what she measures."},
    {"t":"open","key":"control","q":"Why do you need the control slice that is touched only with clean tongs?","min":20,"rows":2,"rubric":["It shows how much mold grows without hands, from spores already in the air or bread","Gives a baseline to compare the other slices against"],"model":"The control shows how much mold grows from spores that were already in the air or on the bread, without any hands. Then I can tell whether the hands added more."},
    {"t":"num","q":"On Day 5, mold covers 18 of the 24 squares of a grid drawn on the bag over one slice. What percent of the slice is covered?","a":75,"unit":"%","pts":2,"why":"18/24 = 3/4 = 75%."}]}],
 "handson": {
  "title": "The Hand-Washing Bread Test",
  "intro": "Find out whether hand-washing makes a visible difference, using bread, three sealed bags and a week of careful observation.",
  "materials": ["3 slices of the same bread (bread without preservatives grows mold faster)", "3 zip-top bags and a permanent marker", "Clean tongs", "Soap and water", "A few drops of water", "A clean towel or paper towels", "A fine-tipped marker to draw a 4 by 6 grid on each bag", "Paper and pencil"],
  "steps": [
   "Label the bags: CONTROL, UNWASHED and WASHED. Draw a 4 by 6 grid (24 squares) on each bag.",
   "Using tongs, put one slice in the CONTROL bag without touching it. Add 3 drops of water and seal.",
   "Before washing your hands (after playing outside or touching doorknobs), rub both hands on the second slice. Put it in the UNWASHED bag with 3 drops of water and seal.",
   "Wash your hands with soap for 20 seconds and dry them on a clean towel. Rub the third slice the same way, bag it with 3 drops of water and seal.",
   "Keep all three bags together in a dark, room-temperature place, away from food, pets and younger children. Each day for 5 to 7 days, count how many grid squares show mold and sketch each slice. Never open the bags. Throw them away sealed when you finish. Skip this test if anyone in your home is allergic to mold. Never eat any of the test bread, and wash your hands after handling the bags. If you see no mold by Day 7, keep observing up to Day 14."],
  "record": [
   {"t":"open","key":"breaddata","q":"Make a data table with the day and the number of squares (out of 24) showing mold for each bag. Convert your last day's counts to percents.","min":40,"rows":7,"rubric":["Table with days and counts for all three bags","Last-day counts converted to percents correctly","Observations or sketches described"],"model":"Day 1: 0, 0, 0. Day 3: control 0, unwashed 2, washed 0. Day 5: control 1, unwashed 9, washed 2. Day 7: control 3, unwashed 18, washed 5. Day 7 percents: control 12.5%, unwashed 75%, washed about 20.8%. The unwashed slice grew fuzzy green and black spots first."},
   {"t":"open","key":"breadconc","q":"Write a conclusion. What did your evidence show about hand-washing? Name one way your test could be improved to make it more reliable.","min":40,"rows":4,"rubric":["A claim supported by the data","Compares with the control","A sensible improvement (more slices per group, repeat the test, same person rubbing the same way, measure area more precisely)"],"model":"My evidence shows that hand-washing reduced mold growth: on Day 7 the unwashed slice was 75% covered but the washed slice only about 21%, close to the control's 12.5%. To make it more reliable, I would use three slices for each group and repeat the test, because one slice could be unusual."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"helpharm","q":"Some people think of all microbes as \"germs.\" Are microorganisms more helpful or more harmful to life on Earth? Take a position and support it with at least three examples from the lesson.","min":100,"rows":8,"rubric":["Clear position (helpful is the stronger, evidence-based answer)","At least three accurate examples","Acknowledges harmful microbes","Logical conclusion"],"model":"Microorganisms are far more helpful than harmful. Decomposers recycle dead matter so forests can keep growing, bacteria in roots add nitrogen that crops need, and ocean phytoplankton make roughly half of Earth's oxygen. Gut bacteria help us digest food, and a mold gave us penicillin. Some microbes do cause harm, like the bacteria behind strep throat or the toxins of a red tide, and we have to protect ourselves with hand-washing and medicine. But without microbes, life on Earth could not exist, while without pathogens it would simply be healthier."},
   {"t":"open","key":"coldantibiotic","q":"A friend has a cold and asks a doctor for antibiotics \"just in case.\" Explain why the doctor says no, using what you know about viruses, bacteria and resistance.","min":70,"rows":6,"rubric":["Colds are caused by viruses, which antibiotics cannot kill","Taking unneeded antibiotics can help resistant bacteria spread","A helpful alternative (rest, fluids, hand-washing; see a doctor if it gets worse)"],"model":"Colds are caused by viruses, and antibiotics only work on bacteria, so they would not help. Taking antibiotics when they aren't needed also gives bacteria in the body a chance to become resistant, so the medicine might not work when it is really needed. The friend should rest, drink fluids and wash hands, and see the doctor again if they get worse."}]},
 "exit": [
  {"t":"text","q":"What kind of pathogen causes colds and flu?","a":[{"all":[["virus","viral"]],"none":["not","bacteri"]}],"show":"viruses","pts":2,"why":"That is why antibiotics do not help a cold."},
  {"t":"num","q":"How many micrometers are in 3 millimeters?","a":3000,"unit":"µm","pts":2,"why":"3 × 1,000 = 3,000 µm."},
  {"t":"text","q":"What is the name for a medicine that kills bacteria, such as penicillin?","a":[{"all":[["antibiotic"]],"none":["not"]}],"show":"an antibiotic","pts":2,"why":"Penicillin came from a mold."},
  {"t":"open","key":"exit_help","q":"Give one way microorganisms help people or ecosystems.","min":10,"rows":2,"rubric":["An accurate example (decomposing, nitrogen in soil, oxygen, digestion, food, medicine)"],"model":"Decomposer bacteria and fungi break down dead plants and return nutrients to the soil."}],
 "next": "Week 15: mid-year review and the Field Guide Project."
}

TEACHER = {
 "standards": [
  "SC.6.L.14.6: Compare and contrast types of infectious agents that may infect the human body, including viruses, bacteria, fungi, and parasites.",
  "SC.6.L.15.1: Analyze and describe how and why organisms are classified according to shared characteristics with emphasis on the Linnaean system combined with the concept of Domains.",
  "SC.6.N.1.1: Define a problem from the sixth grade curriculum, use appropriate reference materials to support scientific understanding, plan and carry out scientific investigation of various types, such as systematic observations or experiments, identify variables, collect and organize data, interpret data in charts, tables, and graphics, analyze information, make predictions, and defend conclusions.",
  "SC.6.N.1.2: Explain why scientific investigations should be replicable.",
  "SC.6.N.2.3: Recognize that scientists who make contributions to scientific knowledge come from all kinds of backgrounds and possess varied talents, interests, and goals."],
 "materials": ["The interactive lesson", "3 slices of bread, 3 zip-top bags, tongs, soap, water, a clean towel, paper and pencil, a permanent marker and a fine-tipped marker", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 13 Reconnect questions."],
  [4, "Hook", "Describe red tide on Florida's Gulf coast."],
  [11, "Meet the microbes", "Compare sizes with the scale. Review groups and why viruses are not living."],
  [11, "Helpful microbes", "Discuss decomposers, oxygen, food and Fleming."],
  [12, "Harmful microbes", "Sort pathogens; explain antibiotics and resistance; read about Alice Ball."],
  [10, "Fair test", "Plan the bread test together: variables and control."],
  [6, "Assign", "Set up the three bags together today; assign daily observations, Think Deeper and the Exit Check. Score the bread-test record items when observations end (this may fall in Week 15)."]],
 "key_questions": ["What makes something a microorganism?", "How do microbes help us?", "Why don't antibiotics cure a cold?", "What makes a test fair?"],
 "misconceptions": ["All bacteria are harmful.", "Antibiotics kill viruses.", "Viruses are tiny bacteria.", "Hand sanitizer and hand-washing remove every germ."],
 "support": ["Use a sorting chart: bacteria / protist / fungus / virus.", "Pre-draw the data table for the bread test.", "Review metric conversions before the size items."],
 "challenge": ["Research how scientists track red tide (FWC's daily red tide reports).", "Find out what the Ball Method was and how it was eventually replaced."],
 "background": "<p>Karenia brevis is a dinoflagellate protist; Florida red tides produce brevetoxins (FWC Fish and Wildlife Research Institute). Phytoplankton produce roughly half of the oxygen generated on Earth (NOAA estimates range from about 50% to 80% of oxygen production occurs in the ocean). Fleming observed Penicillium's effect in September 1928; Florey and Chain developed penicillin as a drug around 1940. Alice Ball (1892 to 1916) developed an injectable chaulmoogra oil extract in 1915 at the College of Hawaii; Arthur Dean published it without credit; the University of Hawaii formally recognized her work in 2000. CDC recommends scrubbing hands for at least 20 seconds. Size estimates: bacteria about 1 to 5 µm; human hair about 17 to 180 µm wide; Paramecium about 50 to 300 µm. Bread mold test: sealed bags only; discard unopened.</p>",
 "sources": ["Florida Fish and Wildlife Conservation Commission, Red Tide (Karenia brevis).", "NOAA Ocean Service, How much oxygen comes from the ocean?", "CDC, When and How to Wash Your Hands.", "American Chemical Society, Discovery and Development of Penicillin (National Historic Chemical Landmark).", "University of Hawaii, Alice Ball."]
}

PRINT = {
 "directions": "Answer in complete sentences.",
 "items": [
  {"q":"Name the four main groups of microorganisms and give one example of each.","a":"Bacteria (Salmonella); archaea (hot-spring microbes); protists (amoeba, Karenia brevis); microscopic fungi (yeast, bread mold).","lines":3},
  {"q":"Why are viruses not usually considered living?","a":"They are not cells and can only copy themselves inside a living cell.","lines":2},
  {"q":"Give three ways microbes help people or ecosystems.","a":"Decomposing; adding nitrogen to soil; making oxygen; digestion; bread, yogurt and cheese; penicillin.","lines":2},
  {"q":"Why don't antibiotics work on colds?","a":"Colds are caused by viruses; antibiotics only work on bacteria.","lines":2},
  {"q":"How many 4-micrometer bacteria fit across 2 millimeters?","a":"2,000 ÷ 4 = 500.","lines":1},
  {"q":"Name the independent, dependent and controlled variables in the bread test.","a":"Independent: how the hands were cleaned. Dependent: percent of bread covered with mold. Controlled: bread type, bags, water, place, temperature.","lines":3}]
}
