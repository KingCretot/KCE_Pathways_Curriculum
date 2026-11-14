CHAR = ('<svg viewBox="0 0 660 260" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Seven characteristics of living things">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Seven characteristics shared by all living things</text>'
  + ''.join(f'<rect x="{x}" y="{y}" width="200" height="62" rx="10" fill="{c}"/><text x="{x+100}" y="{y+24}" text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">{t1}</text><text x="{x+100}" y="{y+42}" text-anchor="middle" fill="#fff" font-size="11">{t2}</text><text x="{x+100}" y="{y+56}" text-anchor="middle" fill="#fff" font-size="10">{t3}</text>'
            for x, y, c, t1, t2, t3 in [(15, 34, "#0A1F3D", "1. Made of cells", "one cell or trillions", "(Unit 2)"),
                                        (230, 34, "#0047BA", "2. Organized", "cells, tissues, organs,", "organ systems"),
                                        (445, 34, "#3d9a2f", "3. Use energy", "food or sunlight powers", "every life process"),
                                        (15, 108, "#C9A84C", "4. Grow and develop", "get bigger and change", "over a lifetime"),
                                        (230, 108, "#DB2F30", "5. Respond", "react to stimuli such as", "light, heat or touch"),
                                        (445, 108, "#6b3fa0", "6. Reproduce", "make more of their own", "kind"),
                                        (230, 182, "#8a6d1f", "7. Keep a stable inside", "homeostasis: steady", "temperature, water, sugar")]) +
  '<text x="70" y="214" font-size="11" fill="#5b6676">Over many generations,</text><text x="70" y="228" font-size="11" fill="#5b6676">populations also adapt</text><text x="70" y="242" font-size="11" fill="#5b6676">to their environment.</text>'
  '<text x="460" y="214" font-size="11" fill="#5b6676">A living thing must show</text><text x="460" y="228" font-size="11" fill="#5b6676">ALL of these, not just</text><text x="460" y="242" font-size="11" fill="#5b6676">one or two.</text></svg>')

ORG = ('<svg viewBox="0 0 660 190" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Levels of organization from cell to organism">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Levels of organization in a many-celled organism</text>'
  '<defs><marker id="og" viewBox="0 0 10 10" markerWidth="5" markerHeight="5" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="#0A1F3D"/></marker></defs>'
  # cell
  '<ellipse cx="60" cy="90" rx="30" ry="22" fill="#f7c9c9" stroke="#DB2F30" stroke-width="2"/><circle cx="60" cy="90" r="7" fill="#6b3fa0"/>'
  '<text x="60" y="140" text-anchor="middle" font-weight="bold">Cell</text><text x="60" y="156" text-anchor="middle" font-size="11">a muscle cell</text>'
  '<path d="M100 90 h30" stroke="#0A1F3D" stroke-width="2" marker-end="url(#og)"/>'
  # tissue
  + ''.join(f'<ellipse cx="{160+i%3*22}" cy="{75+i//3*16}" rx="12" ry="8" fill="#f7c9c9" stroke="#DB2F30"/>' for i in range(9)) +
  '<text x="182" y="140" text-anchor="middle" font-weight="bold">Tissue</text><text x="182" y="156" text-anchor="middle" font-size="11">muscle tissue</text>'
  '<path d="M222 90 h30" stroke="#0A1F3D" stroke-width="2" marker-end="url(#og)"/>'
  # organ heart
  '<path d="M300 112 C268 92 270 62 292 64 C302 65 300 74 300 74 C300 74 298 65 308 64 C330 62 332 92 300 112z" fill="#DB2F30"/>'
  '<text x="300" y="140" text-anchor="middle" font-weight="bold">Organ</text><text x="300" y="156" text-anchor="middle" font-size="11">the heart</text>'
  '<path d="M340 90 h30" stroke="#0A1F3D" stroke-width="2" marker-end="url(#og)"/>'
  # organ system
  '<path d="M420 112 C392 94 394 68 412 70 C420 71 420 78 420 78 C420 78 420 71 428 70 C446 68 448 94 420 112z" fill="#DB2F30"/>'
  '<path d="M420 112 v30 M420 70 v-26 M405 80 q-20 20 -10 60 M435 80 q20 20 10 60" stroke="#0047BA" stroke-width="2.5" fill="none"/>'
  '<text x="420" y="160" text-anchor="middle" font-weight="bold">Organ system</text><text x="420" y="176" text-anchor="middle" font-size="11">circulatory system</text>'
  '<path d="M470 90 h30" stroke="#0A1F3D" stroke-width="2" marker-end="url(#og)"/>'
  # organism
  '<circle cx="560" cy="52" r="14" fill="#8a5a33"/><path d="M560 66 v50 M560 80 l-24 20 M560 80 l24 20 M560 116 l-18 34 M560 116 l18 34" stroke="#8a5a33" stroke-width="7" stroke-linecap="round"/>'
  '<text x="560" y="174" text-anchor="middle" font-weight="bold">Organism</text></svg>')

LESSON = {
 "unit": "Unit 3: The Diversity of Life",
 "title": "Characteristics of Living Things",
 "subtitle": "A seed, a virus, a fire and a tardigrade: which are alive? Scientists use a set of shared characteristics to decide, and some cases are surprisingly hard.",
 "objectives": [
  "Name and explain seven characteristics shared by all living things.",
  "Describe the levels of organization from cell to organism.",
  "Explain homeostasis with examples from the human body.",
  "Use the characteristics to classify things as living, once living or never living, and argue about hard cases.",
  "Run a controlled yeast investigation and use the results as evidence that yeast is alive."],
 "vocab": [
  ["organism", "Any individual living thing, from a bacterium to a blue whale."],
  ["stimulus", "A change in the environment that causes a living thing to react (plural: stimuli)."],
  ["response", "A reaction to a stimulus."],
  ["homeostasis", "Keeping conditions inside an organism stable, such as body temperature or water level."],
  ["development", "The changes an organism goes through as it grows, such as a tadpole becoming a frog."],
  ["tissue", "A group of similar cells that do the same job."],
  ["organ", "A structure made of different tissues working together, such as the heart or a leaf."],
  ["unicellular / multicellular", "Made of one cell / made of many cells."]],
 "reconnect": {
  "title": "Week 10: Unit 2 big ideas",
  "intro": "Unit 3 is about all the different kinds of life. It starts with the cell.",
  "items": [
   {"t":"open","key":"rc_theory","q":"In your own words, why does cell theory matter for deciding whether something is alive?","min":15,"rows":2,"rubric":["Cell theory says all living things are made of cells, so being made of cells is a test for life"],"model":"Cell theory says all living things are made of cells, so if something is not made of cells, that is a strong sign it is not alive."},
   {"t":"text","q":"Which organelle releases energy from glucose for a cell?","a":[{"all":[["mitochondri"]],"none":["not"]}],"show":"mitochondria","pts":2,"why":"Mitochondria. Using energy is one of today's characteristics of life."},
   {"t":"open","key":"rc_endo","q":"Week 10: Lynn Margulis argued that mitochondria were once free-living bacteria. Give one piece of evidence.","min":10,"rows":2,"rubric":["Own DNA; divide like bacteria; bacteria-like ribosomes; two membranes"],"model":"Mitochondria have their own loop of DNA, like bacteria."},
   {"t":"open","key":"rc_model","q":"Your cell model showed one process. Which process did you show, and what does it tell you about what cells do to stay alive?","min":15,"rows":2,"rubric":["Names a process (photosynthesis, active transport, osmosis)","Connects it to a life need: making or using energy, taking in materials"],"model":"I showed active transport. It shows that cells spend energy to bring in the materials they need to stay alive."}]},
 "hook": {
  "title": "The Water Bear That Came Back",
  "html": "<p>Tardigrades, also called water bears, are animals about half a millimeter long that live in damp moss. When their home dries out, they curl into a tiny dry ball called a tun. Their bodies almost stop working. They do not eat, grow or move.</p><p>Then add water, and minutes to hours later, they uncurl and start crawling. In 2016, scientists in Japan revived tardigrades that had been frozen in a sample of Antarctic moss for more than 30 years. One of them went on to lay eggs.</p><p>So was the dried, frozen tardigrade alive during those 30 years? To answer, you need to know what scientists mean by \"alive.\"</p><div class='callout'><b>Big question:</b> What makes something alive?</div>"},
 "learn": [
  {"title": "Seven Characteristics of Life",
   "visual": CHAR,
   "html": "<p>Biologists agree that living things share a set of characteristics. Something is living only if it shows <b>all</b> of them, at least at some point in its life:</p><ol><li><b>Made of cells.</b> Some organisms, like bacteria, are one cell (<b>unicellular</b>). Others, like you, have trillions (<b>multicellular</b>).</li><li><b>Organized.</b> Inside cells, organelles work together. In many-celled organisms, cells form tissues, organs and organ systems.</li><li><b>Use energy.</b> Plants capture it from sunlight; animals and fungi get it from food. Cells release it in mitochondria.</li><li><b>Grow and develop.</b> An acorn becomes an oak; a caterpillar becomes a butterfly.</li><li><b>Respond to stimuli.</b> A plant bends toward a window; you pull your hand from a hot pan.</li><li><b>Reproduce.</b> Organisms make more of their own kind. A single organism does not have to reproduce to be alive, but its kind must.</li><li><b>Maintain homeostasis.</b> They keep their insides stable even when the outside changes.</li></ol><p>Over many generations, populations of living things also <b>adapt</b> to their environments.</p>",
   "checks": [
    {"t":"open","key":"seed","q":"A dry bean seed sits in a jar for a year without changing. Is it alive? Use at least two characteristics to explain.","min":30,"rows":3,"rubric":["Alive (dormant)","Made of cells; when given water it will use stored energy, grow and develop into a plant (and later reproduce)"],"model":"Yes, it is alive but dormant. It is made of cells, and when it gets water it will use its stored energy to grow and develop into a bean plant that can reproduce."},
    {"t":"open","key":"mule","q":"A mule cannot have babies. Does that mean a mule is not alive? Explain.","min":20,"rows":2,"rubric":["A mule is alive","It shows the other characteristics (cells, energy, growth, response, homeostasis); reproduction applies to living things as a kind, and a single organism does not have to reproduce"],"model":"A mule is alive. It is made of cells, uses energy, grows, responds and keeps homeostasis. Not every single organism has to reproduce for it to be alive."},
    {"t":"text","q":"What is the word for a change in the environment, such as light or heat, that causes a living thing to react?","a":["stimulus","stimuli"],"show":"stimulus","pts":2,"why":"A stimulus causes a response."}]},
  {"title": "Levels of Organization",
   "visual": ORG,
   "html": "<p>Living things are highly organized. In a many-celled organism like you, the levels build on one another:</p><ul><li><b>Cells</b> are the basic units (Unit 2).</li><li>Similar cells form a <b>tissue</b>, such as muscle tissue.</li><li>Different tissues form an <b>organ</b>, such as the heart, which contains muscle, nerve and other tissues.</li><li>Organs work together in an <b>organ system</b>, such as the circulatory system (heart, blood vessels and blood).</li><li>All the organ systems together make an <b>organism</b>.</li></ul><p>Plants have levels too: leaf cells form tissues, tissues form organs such as leaves, stems and roots.</p><p>Notice that each level depends on the one below it. If heart muscle cells are damaged, the heart (an organ) cannot pump well, the circulatory system struggles, and the whole organism is affected.</p>",
   "checks": [
    {"t":"order","q":"Put the levels in order from smallest to largest.","items":["cell","tissue","organ","organ system","organism"],"pts":3,"why":"Cells form tissues, tissues form organs, organs form organ systems, and systems form the organism."},
    {"t":"text","q":"A leaf is made of several kinds of tissue working together. Which level of organization is a leaf?","a":[{"all":[["organ"]],"none":["system","not","tissue"]}],"show":"an organ","pts":2,"why":"A leaf is an organ: different tissues working together to do photosynthesis."},
    {"t":"open","key":"levels","q":"A bacterium is a single cell. Which levels of organization does it have, and which does it not have? Is it still organized?","min":20,"rows":2,"rubric":["It is one cell, which is also the whole organism; no tissues, organs or organ systems","Still organized: its cell parts work together"],"model":"A bacterium is both a cell and an organism, but it has no tissues, organs or organ systems. It is still organized, because the parts inside its single cell work together."}]},
  {"title": "Homeostasis and Responding to the World",
   "html": "<p>Your body works best at an inside temperature of about 98.6°F (37°C), even when the air outside is 40°F or 100°F. On a hot Florida afternoon, you sweat; as the sweat evaporates, it cools your skin. On a cold morning, you shiver; your muscles twitch quickly and make heat. Keeping conditions inside steady like this is <b>homeostasis</b>.</p><p>Homeostasis depends on <b>responding</b> to stimuli. Your body senses the change (too hot) and responds (sweating). You also respond on purpose: you drink water when you are thirsty and move into the shade.</p><p>Responses can be studied scientifically. <b>Dr. Charles Henry Turner</b> (1867 to 1923), the first African American to earn a doctorate from the University of Chicago, ran careful experiments on insects. He showed that honeybees can see color and remember the time of day food is available, and that ants can learn routes. In an era when few people believed insects could learn, his evidence changed how scientists understood animal behavior. He did much of this research while teaching high school in St. Louis.</p>",
   "checks": [
    {"t":"open","key":"sweat","q":"Explain how sweating on a hot day is an example of both responding to a stimulus and maintaining homeostasis.","min":25,"rows":3,"rubric":["Stimulus: body temperature rising; response: sweating","Evaporating sweat cools the body, keeping temperature stable (homeostasis)"],"model":"Rising body temperature is the stimulus, and sweating is the response. When the sweat evaporates, it cools the skin, which keeps the body's temperature steady. That is homeostasis."},
    {"t":"open","key":"turner","q":"Dr. Turner tested whether honeybees can see color. Describe how you could design a simple fair test of that question.","min":30,"rows":3,"rubric":["Train bees to find sugar water on one color, then offer that color and other colors (or gray shades) without sugar","Controls: same size, shape, position changed, same scent; observe where bees land; repeat"],"model":"I would put sugar water on a blue card for several days, then put out a blue card and gray cards of different shades, all with no sugar, moving their positions. If the bees still go to the blue card, they must see blue as a color, not just as light or dark."},
    {"t":"text","q":"What is the word for keeping conditions inside an organism stable?","a":["homeostasis"],"show":"homeostasis","pts":2,"why":"Homeostasis: homeo (same) + stasis (standing still)."}]},
  {"title": "Hard Cases: Viruses, Fire and Water Bears",
   "html": "<p>Some things show a few characteristics of life but not all of them.</p><ul><li><b>Fire</b> grows, uses oxygen and spreads. But it is not made of cells, has no organization and cannot keep a stable inside. It is not alive.</li><li><b>Crystals</b> grow, but only by adding more of the same material. They are not alive.</li><li><b>Viruses</b> are tiny packets of genetic material wrapped in protein. They are not made of cells, and they cannot use energy or reproduce on their own; they can only copy themselves inside a living cell. Most biologists do not classify viruses as living, but some argue they are on the edge of life. This is a real debate in science.</li><li><b>A dried tardigrade</b> is made of cells and can grow, respond and reproduce again when water returns. Most scientists call it alive but in suspended animation, like a dormant seed.</li></ul><p>We also sort things that are <b>once living</b>, like a wooden table or a fallen leaf, which were alive but no longer carry out life processes.</p>",
   "checks": [
    {"t":"open","key":"fire","q":"A classmate says, \"Fire is alive because it grows, eats fuel and has babies when sparks start new fires.\" Respond using at least two characteristics of life.","min":30,"rows":3,"rubric":["Fire is not alive","Not made of cells; no organization; cannot maintain homeostasis; its \"growth\" and \"spreading\" are a chemical reaction, not reproduction"],"model":"Fire looks alive, but it is not. It is not made of cells, it has no organization, and it cannot keep a stable inside. Its \"growth\" and \"babies\" are just a chemical reaction spreading to new fuel, not reproduction."},
    {"t":"open","key":"virus","q":"Give one reason a biologist might say viruses are not alive and one reason another biologist might say they are on the edge of life.","min":25,"rows":3,"rubric":["Not alive: no cells; cannot use energy or reproduce on their own","Edge of life: they carry genetic material, reproduce (inside cells) and change over time"],"model":"Viruses are not made of cells and cannot use energy or reproduce on their own. But they carry genetic material, make copies of themselves inside cells and change over time, so some biologists say they are on the edge of life."},
    {"t":"open","key":"sort","q":"Sort each into living, once living or never living: a wooden chair, a mushroom, a rock, a houseplant, a cotton T-shirt, a robot vacuum. Explain one choice you think others might get wrong.","min":30,"rows":3,"rubric":["Living: mushroom, houseplant; once living: wooden chair, cotton T-shirt; never living: rock, robot vacuum","Explains a tricky choice (robot responds and uses energy but has no cells; cotton came from a plant)"],"model":"Living: mushroom and houseplant. Once living: wooden chair and cotton T-shirt. Never living: rock and robot vacuum. Someone might call the robot vacuum alive because it uses energy and responds to walls, but it has no cells and cannot grow or reproduce."}]}],
 "handson": {
  "title": "Is Yeast Alive? The Balloon Test",
  "intro": "Dry baker's yeast looks like brown sand. Test whether it shows signs of life: using energy and making a gas as a waste product.",
  "materials": ["3 packets (or 6 1/2 teaspoons) of active dry yeast", "Sugar", "Warm tap water (about as warm as a comfortable bath, near 105°F or 40°C) and cold water", "3 empty plastic bottles of the same size (about 16 to 20 ounces)", "3 balloons, stretched out first", "A funnel or a rolled piece of paper", "A measuring cup and spoons", "A ruler or tape measure, a timer, a marker"],
  "steps": [
   "Label the bottles A, B and C.",
   "A: 1 packet of yeast + 1 tablespoon of sugar + 1 cup of warm water. B: 1 packet of yeast + 1 cup of warm water, no sugar. C: 1 packet of yeast + 1 tablespoon of sugar + 1 cup of cold water.",
   "Swirl each bottle gently and quickly stretch a balloon over the top.",
   "Predict what will happen to each balloon.",
   "Every 10 minutes for 40 minutes, measure around each balloon at its widest point with a tape measure (or measure its height with a ruler) and record it.",
   "Afterward, pour the mixtures down the sink with running water. Do not drink them."],
  "record": [
   {"t":"open","key":"yeastdata","q":"Record a data table: time, and balloon size for A, B and C. Describe the pattern.","min":30,"rows":6,"rubric":["Complete table for three bottles at four times","Clear description: A grew most; B little; C slowly or little"],"model":"At 40 minutes: A 32 cm around, B 12 cm, C 15 cm. Balloon A inflated the most, C grew slowly, and B barely changed."},
   {"t":"open","key":"yeastcer","q":"Write a CER: Is yeast alive? Use your data, and name the independent variables you tested and one variable you kept the same.","min":60,"rows":6,"rubric":["Claim: yeast is alive","Evidence: specific measurements showing gas made with sugar and warmth","Reasoning: yeast used sugar for energy and gave off carbon dioxide as waste; it responded to temperature; uses at least one characteristic of life","Variables: sugar (A versus B) and temperature (A versus C); controlled: amount of yeast, water, bottle size"],"model":"Claim: Yeast is alive. Evidence: The balloon on bottle A, with sugar and warm water, grew to 32 cm around in 40 minutes, while bottle B (no sugar) stayed at 12 cm and bottle C (cold water) reached only 15 cm. Reasoning: The yeast used the sugar as food for energy and gave off carbon dioxide gas as waste, which filled the balloon. It also responded to temperature, working faster when warm. Using energy and responding are characteristics of life. I tested sugar (A versus B) and temperature (A versus C) and kept the yeast, the amount of water and the bottle size the same."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"tardi","q":"Return to the big question. Was the frozen tardigrade alive during its 30 years in the freezer? Write a paragraph that takes a position and supports it with at least three characteristics of life, and address one argument on the other side.","min":110,"rows":10,"rubric":["Clear position","Uses at least three characteristics accurately (cells, organization, growth, reproduction after revival, response, energy use slowed, homeostasis)","Addresses a counterargument","Organized paragraph"],"model":"I think the frozen tardigrade was alive the whole time, in a state like a dormant seed. It was still made of cells and its body was still organized, which is why it could start again. After it thawed, it moved, responded to its surroundings and even laid eggs, so it could grow and reproduce. Someone could argue it was not alive because it was not using energy or responding while frozen. But its life processes had only slowed almost to a stop, not ended, so it was alive in suspended animation, not dead."},
   {"t":"open","key":"robot","q":"Engineers are building robots that can repair themselves and learn. Imagine a future robot that uses energy, responds to its surroundings and builds copies of itself. Would it be alive? Use the characteristics of life to argue your answer.","min":70,"rows":6,"rubric":["Takes a position","Uses characteristics accurately (cells, growth and development, homeostasis)","Thoughtful reasoning about what makes life different"],"model":"Even if it used energy, responded and built copies of itself, I would say the robot is not alive, because it is not made of cells and does not grow and develop from within or keep homeostasis the way organisms do. It would be a very advanced machine. But if scientists ever built a machine that met every characteristic, we might need to rethink our definition of life."}]},
 "exit": [
  {"t":"open","key":"exit_seven","q":"List the seven characteristics of living things.","min":15,"rows":3,"rubric":["Made of cells; organized; use energy; grow and develop; respond to stimuli; reproduce; maintain homeostasis"],"model":"Made of cells, organized, use energy, grow and develop, respond to stimuli, reproduce, and maintain homeostasis."},
  {"t":"text","q":"A group of similar cells that do the same job is called a what?","a":[{"all":[["tissue"]],"none":["not","organ"]}],"show":"a tissue","pts":2,"why":"A tissue, such as muscle tissue."},
  {"t":"open","key":"exit_shiver","q":"Why do you shiver when you are cold?","min":10,"rows":2,"rubric":["Muscles twitch to make heat, keeping body temperature stable (homeostasis)"],"model":"Shivering makes my muscles twitch and produce heat, which keeps my body temperature steady."},
  {"t":"open","key":"exit_virus","q":"Why do most biologists say a virus is not alive?","min":10,"rows":2,"rubric":["Not made of cells; cannot use energy or reproduce on its own"],"model":"It is not made of cells and cannot use energy or reproduce without a living cell."}],
 "next": "Week 12: how scientists classify millions of kinds of living things and give each one a scientific name."
}

TEACHER = {
 "standards": [
  "SC.6.L.14.1: Describe and identify patterns in the hierarchical organization of organisms from atoms to molecules to cells to tissues to organs to organ systems to organisms.",
  "SC.6.L.14.3: Recognize and explore how cells of all organisms undergo similar processes to maintain homeostasis, including extracting energy from food, getting rid of waste, and reproducing.",
  "SC.6.N.1.1: Define a problem from the sixth grade curriculum, use appropriate reference materials to support scientific understanding, plan and carry out scientific investigation of various types, such as systematic observations or experiments, identify variables, collect and organize data, interpret data in charts, tables, and graphics, analyze information, make predictions, and defend conclusions.",
  "SC.6.N.2.3: Recognize that scientists who make contributions to scientific knowledge come from all kinds of backgrounds and possess varied talents, interests, and goals.",
  "NGSS MS-LS1-1: Conduct an investigation to provide evidence that living things are made of cells; either one cell or many different numbers and types of cells."],
 "materials": ["The interactive lesson", "Active dry yeast, sugar, warm and cold water, 3 plastic bottles, 3 balloons, a funnel, measuring tools, a tape measure", "Optional: a bean seed soaked overnight, a houseplant near a window", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 10 Reconnect questions."],
  [5, "Hook", "Tell the tardigrade story. Take a quick vote: alive or not?"],
  [12, "Seven characteristics", "Build the list together. Test the bean seed and the mule."],
  [8, "Organization", "Order the levels. Name a tissue, organ and system in your own body."],
  [8, "Homeostasis and response", "Discuss sweating and shivering. Tell Charles Henry Turner's story."],
  [10, "Hard cases", "Debate fire, crystals and viruses. Sort the household objects."],
  [11, "Yeast test", "Set up the three bottles together; the student measures every 10 minutes after the lesson."]],
 "key_questions": ["Does it show ALL the characteristics, or only some?", "What is the stimulus, and what is the response?", "How does this level depend on the one below it?", "What would change your mind?"],
 "misconceptions": ["Anything that moves is alive (and anything that does not move is not).", "Plants are not alive because they do not move.", "A single organism must reproduce to be alive.", "Viruses are tiny bacteria.", "Seeds are dead until planted."],
 "support": ["Give a checklist card with the seven characteristics to test each case.", "Use the acronym CORGEHR: Cells, Organized, Respond, Grow, Energy, Homeostasis, Reproduce.", "Pre-label the yeast bottles and a data table."],
 "challenge": ["Research tardigrades' survival records (heat, cold, radiation, space) and evaluate which claims come from peer-reviewed studies.", "Repeat the yeast test with honey, salt or flour instead of sugar and explain the results."],
 "background": "<p>Lists of life's characteristics vary by textbook (six to eight items); this lesson uses seven plus adaptation at the population level. Tardigrades: in 2016, Tsujimoto and colleagues (Cryobiology) reported reviving tardigrades from Antarctic moss collected in 1983 and stored frozen for 30.5 years; one laid eggs that hatched. Yeast (Saccharomyces cerevisiae) ferments sugar and releases carbon dioxide; warm water near 105 to 110°F works well, and water above about 130°F kills yeast. Charles Henry Turner (1867 to 1923) earned his PhD in zoology from the University of Chicago in 1907, published on bee color vision and time memory (1910s) and on ant homing; he taught at Sumner High School in St. Louis. Normal body temperature averages about 98.6°F (37°C), with modern studies finding slightly lower averages. Viruses are generally not considered living; some biologists argue otherwise.</p>",
 "sources": ["Tsujimoto, M., Imura, S. and Kanda, H. (2016), Recovery and reproduction of an Antarctic tardigrade retrieved from a moss sample frozen for over 30 years, Cryobiology 72.", "Abramson, C. I. (2009), A study in inspiration: Charles Henry Turner (1867-1923) and the investigation of insect behavior, Annual Review of Entomology 54.", "CK-12 Life Science, Characteristics of Living Things.", "Science Buddies, Yeast Balloon Experiment."]
}

PRINT = {
 "directions": "Use complete sentences.",
 "items": [
  {"q":"List the seven characteristics of living things.","a":"Cells; organized; use energy; grow and develop; respond to stimuli; reproduce; maintain homeostasis.","lines":2},
  {"q":"Put in order: organ, cell, organism, tissue, organ system.","a":"cell, tissue, organ, organ system, organism","lines":1},
  {"q":"Give an example of a stimulus and a response in a plant.","a":"Light from a window (stimulus); the plant bends toward it (response).","lines":2},
  {"q":"Explain homeostasis using sweating or shivering.","a":"Sweating cools the body when hot; shivering warms it when cold; both keep temperature stable.","lines":2},
  {"q":"Is fire alive? Explain.","a":"No; it is not made of cells, has no organization and cannot maintain homeostasis.","lines":2},
  {"q":"In the yeast test, why did the balloon with sugar and warm water grow most?","a":"The yeast used the sugar for energy and gave off carbon dioxide gas; warmth made it work faster.","lines":2}]
}
