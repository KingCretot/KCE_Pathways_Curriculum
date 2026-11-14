WEB = ('<svg viewBox="0 0 640 300" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Web showing how body systems interact around homeostasis">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Body systems work as one team</text>'
  '<circle cx="320" cy="160" r="54" fill="#0A1F3D"/><text x="320" y="156" text-anchor="middle" fill="#C9A84C" font-weight="bold">HOMEOSTASIS</text><text x="320" y="172" text-anchor="middle" fill="#fff" font-size="10">stable inside conditions</text>'
  + ''.join(f'<line x1="320" y1="160" x2="{x}" y2="{y}" stroke="#b9c3d0" stroke-width="2"/>' for x, y in [(130, 70), (510, 70), (100, 200), (540, 200), (220, 270), (420, 270)]) +
  ''.join(f'<rect x="{x-80}" y="{y-24}" width="160" height="48" rx="10" fill="{c}"/><text x="{x}" y="{y-4}" text-anchor="middle" fill="#fff" font-weight="bold" font-size="12">{a}</text><text x="{x}" y="{y+12}" text-anchor="middle" fill="#fff" font-size="10">{b}</text>'
          for x, y, a, b, c in [(130, 70, "Skeletal", "support, protect, blood cells", "#8a6d1f"), (510, 70, "Muscular", "movement, heat", "#DB2F30"), (100, 200, "Circulatory", "delivers O2 and nutrients", "#b8322a"), (540, 200, "Respiratory", "O2 in, CO2 out", "#1d6fb8"), (220, 270, "Digestive", "breaks down food", "#2c6e22"), (420, 270, "Nervous", "senses and controls", "#0047BA")]) +
  '</svg>')

LESSON = {
 "unit": "Unit 4: The Human Body",
 "title": "Unit 4 Checkpoint and Body Systems Project",
 "subtitle": "Over five weeks you zoomed from atoms to whole body systems. This week you connect all of them, finish your body systems project and show your mastery on the Unit 4 checkpoint.",
 "objectives": [
  "Describe the levels of organization from atoms to organisms.",
  "Explain the functions of the skeletal, muscular, circulatory, respiratory, digestive and nervous systems.",
  "Explain how body systems interact to maintain homeostasis in a real situation.",
  "Analyze data from a body investigation and use models to explain body functions.",
  "Demonstrate mastery of Unit 4 on the checkpoint (85 or higher)."],
 "vocab": [
  ["homeostasis", "Keeping stable internal conditions, such as temperature and oxygen level."],
  ["organ system", "A group of organs that work together to do a major job."],
  ["structure and function", "The idea that a part's shape fits its job."],
  ["interaction", "When two or more systems affect or depend on each other."],
  ["model", "A representation that helps explain how something works, with limits."]],
 "reconnect": {
  "title": "Unit 4, one question from each week",
  "intro": "Warm up with one question from each week of the unit.",
  "items": [
   {"t":"text","q":"Week 16: Which tissue type covers and lines body surfaces?","a":[{"all":[["epithel"]],"none":["not"]}],"show":"epithelial","pts":2,"why":"Skin, stomach lining."},
   {"t":"text","q":"Week 17: What connects bone to bone at a joint?","a":[{"all":[["ligament"]],"none":["not","tendon"]}],"show":"a ligament","pts":2,"why":"Tendons connect muscle to bone."},
   {"t":"text","q":"Week 18: Which side of the heart pumps blood to the lungs?","a":[{"all":[["right"]],"none":["not right","left"]}],"show":"the right side","pts":2,"why":"The left side pumps to the body."},
   {"t":"text","q":"Week 19: Where are most nutrients absorbed?","a":[{"all":[["small intestine"]],"none":["not","large"]}],"show":"the small intestine","pts":2,"why":"Through the villi."}]},
 "hook": {
  "title": "A Soccer Game, Inside and Out",
  "visual": WEB,
  "html": "<p>It's the last minute of a soccer game on a hot Florida afternoon. A player sprints toward the ball, heart pounding, breathing hard, sweat dripping. She sees a gap, plants her foot and kicks. Goal!</p><p>In those few seconds, every system you studied this unit was working: nerves fired, muscles pulled on bones, the heart and lungs raced to deliver oxygen, and energy from her lunch powered every cell. This week you put the whole body together.</p><div class='callout'><b>Big question:</b> How do trillions of cells and many organ systems work together as one living person?</div>"},
 "learn": [
  {"title": "Review: Levels and Structure-Function",
   "html": "<p>Atoms form molecules; molecules build cells; similar cells form tissues (epithelial, connective, muscle, nervous); tissues form organs; organs form systems; systems make an organism. Again and again this unit, a part's <b>structure fits its function</b>: thin capillary walls for exchange, hundreds of millions of alveoli and millions of villi for huge surface areas, hinge joints for stable back-and-forth motion, the thick left ventricle for high pressure.</p>",
   "checks": [
    {"t":"blanks","q":"Name the level of organization.","sent":"A neuron: ___ &nbsp; The stomach: ___ &nbsp; Bone tissue plus marrow plus cartilage working together as the femur: ___","blanks":[[{"all":[["cell"]],"none":["not"]}],[{"all":[["organ"]],"none":["not","organ system","organism"]}],[{"all":[["organ"]],"none":["not","organ system","organism"]}]],"show":"cell; organ; organ","pts":3,"why":"A bone is an organ made of several tissues."},
    {"t":"open","key":"revstruct","q":"Choose two structures from different weeks of this unit that both have a large surface area. Explain why a large surface helps each one do its job.","min":30,"rows":3,"rubric":["Two correct structures (alveoli, villi, capillary networks, dendrites)","Explains that more surface means more exchange or absorption for each"],"model":"Alveoli in the lungs and villi in the small intestine both have huge surface areas. More surface on the alveoli lets more oxygen move into the blood at once, and more surface on the villi lets more nutrients be absorbed."}]},
  {"title": "Review: Systems and Their Jobs",
   "html": "<ul><li><b>Skeletal:</b> support, protection, movement, blood cells, mineral storage.</li><li><b>Muscular:</b> movement through opposing pairs; heart and organ muscles.</li><li><b>Circulatory:</b> heart, vessels and blood deliver oxygen and nutrients and remove wastes in a double loop.</li><li><b>Respiratory:</b> the diaphragm draws air to the alveoli for gas exchange.</li><li><b>Digestive:</b> mechanical and chemical digestion; absorption in the small intestine.</li><li><b>Nervous:</b> brain, spinal cord and nerves sense, decide and control; reflexes protect us fast.</li></ul>",
   "checks": [
    {"t":"open","key":"revtwo","q":"Choose any two systems and describe one way they depend on each other.","min":20,"rows":2,"rubric":["Two correct systems","An accurate dependence (e.g., muscles need oxygen from the circulatory system; the nervous system signals muscles; bones make blood cells for the circulatory system)"],"model":"The nervous and respiratory systems depend on each other: the nervous system signals the diaphragm to contract so we breathe, and the respiratory system supplies the oxygen that neurons need to work."}]},
  {"title": "Putting It Together: Homeostasis",
   "html": "<p><b>Homeostasis</b> means keeping your internal conditions stable. When the soccer player sprints in the heat:</p><ul><li>Muscles use more oxygen and produce more heat and carbon dioxide.</li><li>The nervous system detects the changes and signals the heart to pump faster and the lungs to breathe faster.</li><li>Blood vessels in the skin widen and sweat glands release sweat, carrying heat away as it evaporates.</li><li>If she doesn't drink water, she loses fluid, and her body has a harder time cooling down, which is why drinking water on hot days matters so much.</li></ul>",
   "checks": [
    {"t":"open","key":"heatdanger","q":"Why can exercising hard on a hot, humid Florida day without drinking water be dangerous? Use at least two body systems in your answer.","min":30,"rows":3,"rubric":["Sweat removes heat but uses body water; humidity slows evaporation","Losing water makes it harder for the circulatory system to carry heat to the skin and supply muscles","Body temperature can rise too high (homeostasis fails)"],"model":"Sweating cools the body, but it uses up water, and in humid air sweat evaporates slowly so it cools less. Without enough water, there's less fluid for the circulatory system to carry heat to the skin and oxygen to muscles, so body temperature can climb too high and homeostasis breaks down."}]}],
 "handson": {
  "title": "Life-Size Body Map",
  "intro": "Trace your body and build a life-size map of the organ systems, the centerpiece of your body systems project.",
  "materials": ["A roll of butcher paper or several large sheets taped together (about 5 feet long)", "Markers and colored pencils", "Construction paper, scissors and glue or tape", "Yarn or string in red and blue", "A family member", "Your notes from Weeks 16 to 19"],
  "steps": [
   "Lie on the paper while a family member traces your outline.",
   "Cut out or draw organs from at least five systems (skeletal, muscular, circulatory, respiratory, digestive, nervous) to life size, in the right places. Use red yarn for oxygen-rich blood and blue yarn for oxygen-poor blood. (Real blood is always red; blue is only a diagram color.)",
   "Label every organ with its name and job.",
   "Add three interaction arrows, each with a sentence explaining how two systems work together.",
   "Present your body map to your family: explain what happens inside your body during one activity you love (swimming, dancing, climbing, playing an instrument)."],
  "record": [
   {"t":"open","key":"bodymaprec","q":"Describe your body map: which organs you placed, the three interactions you explained, and the activity you narrated. What was the most surprising thing you noticed about where organs sit in the body?","min":50,"rows":5,"rubric":["Organs from at least five systems","Three accurate interactions","An activity narrated with several systems","A thoughtful observation"],"model":"I placed the brain, spinal cord, lungs, heart, stomach, small and large intestines, liver, femur, ribs, skull and biceps. Interactions: the diaphragm and lungs bring in oxygen that the heart pumps to muscles; my ribs protect my heart and lungs; nerves signal my biceps to contract. I narrated swimming: my brain coordinates strokes, my muscles pull, and I breathe in rhythm. The surprise: my liver is much bigger than I thought and sits high on the right, under my ribs."}]},
 "think": {
  "intro": "Use evidence from the whole unit. Your teacher scores this.",
  "items": [
   {"t":"open","key":"astronautbody","q":"An astronaut spends six months on the International Space Station. Predict how at least three body systems are affected by living in near-weightlessness, and explain how exercise and other habits help. Use what you learned across Unit 4.","min":76,"rows":8,"rubric":["Skeletal: bone loss without weight-bearing (about 1 to 1.5 percent per month in weight-bearing bones)","Muscular: muscles weaken without use","Circulatory or other: heart works less against gravity, fluids shift","Explains exercise (treadmill with straps, resistance machine) and nutrition (calcium, vitamin D) as countermeasures"],"model":"Without gravity, astronauts' bones carry almost no weight, so they lose about 1 to 1.5 percent of the mineral in their leg and hip bones each month. Their muscles weaken too, because they don't have to hold the body up. Their heart doesn't have to pump blood upward against gravity, so it can lose some strength. Astronauts exercise about two hours a day on a treadmill with straps and a resistance machine to load their bones and muscles, and eat foods with calcium and vitamin D to help rebuild bone."}]},
 "checkpoint": {
  "title": "Unit 4 Checkpoint: The Human Body",
  "intro": "This checkpoint covers Weeks 16 to 19. Answer every question; for written answers, use science vocabulary. Mastery is 85 or higher. If you score below 85, your teacher will review with you, then you will retake it.",
  "parts": [
   {"title": "Part A: Levels of organization", "items": [
    {"t":"order","q":"Put these examples in order from smallest level to largest.","items":["a hemoglobin molecule","a red blood cell","heart muscle tissue","the heart","the circulatory system","a person"],"pts":3,"why":"Molecule, cell, tissue, organ, organ system, organism."},
    {"t":"text","q":"Which tissue type carries electrical signals?","a":[{"all":[["nervous","neural"]],"none":["not"]}],"show":"nervous tissue","pts":3,"why":"Brain, spinal cord, nerves."},
    {"t":"open","q":"Explain how a nerve cell and a muscle cell can have the same DNA but different structures and jobs.","key":"cpdna","min":20,"rows":2,"pts":4,"rubric":["Cells use (switch on) different parts of the same DNA","so they make different proteins and become specialized (differentiation)"],"model":"Each cell uses different parts of the same DNA instructions, so they make different proteins and develop different shapes and jobs. This is called differentiation."}]},
   {"title": "Part B: Support and movement", "items": [
    {"t":"text","q":"What part of a bone makes blood cells?","a":[{"all":[["red marrow","marrow"]],"none":["not","yellow"]}],"show":"red marrow","pts":3,"why":"Inside spongy bone."},
    {"t":"text","q":"Which type of joint is your knee?","a":[{"all":[["hinge"]],"none":["not"]}],"show":"a hinge joint","pts":3,"why":"Back and forth, like a door."},
    {"t":"open","q":"Explain how your biceps and triceps let you lift a cup to your mouth and put it back down.","key":"cparm","min":20,"rows":2,"pts":4,"rubric":["Biceps contracts to bend the elbow (lift) while triceps relaxes","Triceps contracts to straighten (lower) while biceps relaxes; muscles only pull"],"model":"To lift the cup, the biceps contracts and bends my elbow while the triceps relaxes. To put it down, the triceps contracts and straightens my arm while the biceps relaxes, because muscles can only pull."}]},
   {"title": "Part C: Transport and exchange", "items": [
    {"t":"text","q":"Which blood vessels carry blood back to the heart and have valves?","a":[{"all":[["vein"]],"none":["not"]}],"show":"veins","pts":3,"why":"Arteries carry blood away."},
    {"t":"num","q":"You count 23 heartbeats in 15 seconds. What is your heart rate in beats per minute?","a":92,"unit":"beats per minute","pts":3,"why":"23 × 4 = 92."},
    {"t":"open","q":"Trace the path of an oxygen molecule from the air you breathe in to a muscle cell in your leg. Name at least five structures.","key":"cpoxygen","min":40,"rows":3,"pts":5,"rubric":["Air path: nose/mouth, trachea, bronchi, bronchioles, alveoli","Into capillaries, to the left side of the heart (via lungs), pumped through arteries","Into leg capillaries and the muscle cell","At least five structures in correct order"],"model":"The oxygen enters my nose, travels down the trachea, through the bronchi and bronchioles, into an alveolus. It passes into a capillary, travels to the left side of my heart, gets pumped out through the aorta and arteries to my leg, and leaves a capillary to enter the muscle cell."}]},
   {"title": "Part D: Fuel and control", "items": [
    {"t":"text","q":"Chewing is an example of mechanical or chemical digestion?","a":[{"all":[["mechanical"]],"none":["not mechanical","chemical"]}],"show":"mechanical","pts":3,"why":"It changes size, not molecules."},
    {"t":"text","q":"A fast, automatic response that goes through the spinal cord without waiting for the brain is called a ___.","a":[{"all":[["reflex"]],"none":["not"]}],"show":"reflex","pts":3,"why":"Like pulling away from a hot pan."},
    {"t":"open","q":"After a big lunch, a student goes for a run. Describe how the digestive, circulatory and nervous systems work together during the next hour.","key":"cplunch","min":40,"rows":3,"pts":5,"rubric":["Digestive: breaking down food, absorbing nutrients in the small intestine","Circulatory: carrying nutrients and oxygen to muscles","Nervous: controlling heart rate, breathing and muscles; coordinating digestion","Shows interaction among all three"],"model":"The digestive system breaks the lunch into nutrients and absorbs them through the villi. The circulatory system carries those nutrients and oxygen to the leg muscles during the run. The nervous system speeds up the heart and breathing and tells the muscles when to contract, while still controlling digestion in the background."}]}]},
 "next": "Unit 5: ecosystems, starting with the living and nonliving parts of an ecosystem."
}

TEACHER = {
 "standards": [
  "SC.6.L.14.1: Describe and identify patterns in the hierarchical organization of organisms from atoms to molecules to cells to tissues to organs to organ systems to organisms.",
  "SC.6.L.14.5: Identify and investigate the general functions of the major systems of the human body (digestive, respiratory, circulatory, reproductive, excretory, immune, nervous, and musculoskeletal) and describe ways these systems interact with each other to maintain homeostasis.",
  "SC.6.N.3.4: Identify the role of models in the context of the sixth grade science benchmarks.",
  "SC.6.N.1.1: Define a problem from the sixth grade curriculum, use appropriate reference materials to support scientific understanding, plan and carry out scientific investigation of various types, such as systematic observations or experiments, identify variables, collect and organize data, interpret data in charts, tables, and graphics, analyze information, make predictions, and defend conclusions."],
 "materials": ["The interactive lesson", "Butcher paper (about 5 feet), markers, colored pencils, construction paper, scissors, glue or tape, red and blue yarn", "Notes from Weeks 16 to 19", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run one question from each week of the unit."],
  [4, "Hook", "The soccer game and the systems web."],
  [9, "Levels and structure-function", "Review the levels; compare large-surface structures."],
  [9, "Systems and jobs", "Review each system; pair systems that depend on each other."],
  [12, "Homeostasis", "Heat, sweat and water; the dangers of hot-weather exercise."],
  [10, "Assign", "Trace the body outline; assign the body map project and Think Deeper."],
  [10, "Checkpoint preview", "Explain that the checkpoint is completed after class, independently, one try per item, with no answers shown until you review it. Mastery is 85; below 85 means a review lesson and a retake."]],
 "key_questions": ["What level of organization is this?", "How does this structure fit its job?", "Which systems are working together?", "How does the body keep conditions stable?"],
 "misconceptions": ["Each system works alone.", "Bones are not alive.", "Blood in veins is blue.", "Most digestion happens in the stomach."],
 "support": ["Use the systems web as a study guide (not during the checkpoint).", "Pre-cut organ templates for the body map.", "Read checkpoint questions aloud if reading is a barrier."],
 "challenge": ["Add the excretory and immune systems to the body map with explanations.", "Research how a heart-lung machine takes over during surgery."],
 "background": "<p>The checkpoint is scored out of 42 points: Part A 10, Part B 10, Part C 11, Part D 11. A score of 85 percent is about 36 of 42 points. Open items are scored with the rubric after submission. NASA's figure for bone loss in weight-bearing bones during long missions is about 1 to 1.5 percent per month (Week 17).</p>",
 "sources": ["OpenStax, Anatomy and Physiology 2e.", "NASA, Human Research Program.", "National Weather Service and CDC, heat illness prevention."]
}

PRINT = {
 "directions": "Answer in complete sentences. This is review practice, not the checkpoint.",
 "items": [
  {"q":"List the levels of organization from atom to organism, with an example of each.","a":"Atom (oxygen), molecule (water), cell (neuron), tissue (muscle), organ (heart), organ system (circulatory), organism (a person).","lines":3},
  {"q":"Name one function each of the skeletal, muscular, circulatory, respiratory, digestive and nervous systems.","a":"Support/protection; movement; transport; gas exchange; breaking down and absorbing food; sensing and control.","lines":3},
  {"q":"Give two examples of structure fitting function from this unit.","a":"Thin capillary walls for exchange; alveoli/villi for surface area; thick left ventricle for pressure; hinge knee for stability.","lines":2},
  {"q":"Explain the path of blood through the double loop.","a":"Right heart → lungs → left heart → body → right heart.","lines":2},
  {"q":"Compare mechanical and chemical digestion with examples.","a":"Mechanical: chewing, churning. Chemical: enzymes and acid breaking food into molecules.","lines":2},
  {"q":"Describe how three systems respond when you exercise on a hot day.","a":"Nervous system detects heat and signals; circulatory system pumps faster and sends blood to the skin; respiratory system breathes faster (sweat glands in the skin release sweat).","lines":3}]
}
