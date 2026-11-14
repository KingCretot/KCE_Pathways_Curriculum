LADDER = ('<svg viewBox="0 0 680 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Levels of organization from atom to organism">'
  '<text x="340" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">From atoms to you: levels of organization</text>'
  '<defs><marker id="lo" viewBox="0 0 10 10" markerWidth="6" markerHeight="6" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="#0A1F3D"/></marker></defs>'
  + ''.join(f'<g transform="translate({14+i*95},40)"><rect width="84" height="130" rx="10" fill="{c}"/>{pic}<text x="42" y="104" text-anchor="middle" fill="#fff" font-weight="bold" font-size="12">{a}</text><text x="42" y="120" text-anchor="middle" fill="#fff" font-size="10">{b}</text></g>'
            + (f'<path d="M{100+i*95} 105 L{108+i*95} 105" stroke="#0A1F3D" stroke-width="2" marker-end="url(#lo)"/>' if i < 6 else '')
            for i, (a, b, c, pic) in enumerate([
              ("atom", "oxygen", "#6b3fa0", '<circle cx="42" cy="46" r="8" fill="#fff"/><circle cx="42" cy="46" r="22" fill="none" stroke="#fff" stroke-width="1.5"/>'),
              ("molecule", "water, DNA", "#5a4fb0", '<circle cx="34" cy="46" r="12" fill="#fff"/><circle cx="54" cy="36" r="7" fill="#d9d4f5"/><circle cx="54" cy="58" r="7" fill="#d9d4f5"/>'),
              ("cell", "muscle cell", "#0047BA", '<ellipse cx="42" cy="46" rx="30" ry="12" fill="#fff"/><circle cx="42" cy="46" r="5" fill="#0047BA"/>'),
              ("tissue", "muscle tissue", "#1d6fb8", ''.join(f'<ellipse cx="{24+(j%3)*18}" cy="{32+(j//3)*14}" rx="9" ry="5" fill="#fff"/>' for j in range(9))),
              ("organ", "heart", "#DB2F30", '<path d="M42 70 C10 46 22 22 42 36 C62 22 74 46 42 70Z" fill="#fff"/>'),
              ("organ system", "circulatory", "#b8322a", '<path d="M42 70 C10 46 22 22 42 36 C62 22 74 46 42 70Z" fill="#fff"/><path d="M14 30 Q42 10 70 30 M14 66 Q42 86 70 66" stroke="#fff" stroke-width="2" fill="none"/>'),
              ("organism", "you", "#3d9a2f", '<circle cx="42" cy="22" r="8" fill="#fff"/><path d="M42 30 v24 M42 54 l-10 18 M42 54 l10 18 M28 40 h28" stroke="#fff" stroke-width="4" stroke-linecap="round"/>')])) +
  '<text x="340" y="200" text-anchor="middle" font-size="11" fill="#5b6676">Each level is made of the level before it, and each level can do things the level below cannot do alone.</text>'
  '<text x="340" y="218" text-anchor="middle" font-size="11" fill="#5b6676">Simplified drawings, not to scale.</text></svg>')

TISSUES = ('<svg viewBox="0 0 660 246" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="The four main types of animal tissue">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The four main types of animal tissue</text>'
  + ''.join(f'<g transform="translate({12+i*162},36)"><rect width="150" height="180" rx="12" fill="{c}"/><text x="75" y="22" text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">{a}</text>{pic}'
            + ''.join(f'<text x="75" y="{128+j*15}" text-anchor="middle" fill="#fff" font-size="11">{t}</text>' for j, t in enumerate(lines)) + '</g>'
            for i, (a, c, pic, lines) in enumerate([
              ("Epithelial", "#8f6f1e", ''.join(f'<rect x="{20+j*22}" y="44" width="20" height="18" fill="#fff" stroke="#8a6d1f"/>' for j in range(5)) + ''.join(f'<rect x="{20+j*22}" y="64" width="20" height="18" fill="#fff" stroke="#8a6d1f"/>' for j in range(5)), ["covers and lines", "skin, stomach lining", "packed tightly to", "protect and absorb"]),
              ("Connective", "#a5552a", '<rect x="20" y="40" width="110" height="50" rx="6" fill="#f4dcc9"/>' + ''.join(f'<circle cx="{32+j*20}" cy="{52+(j%2)*18}" r="5" fill="#a5552a"/>' for j in range(5)) + '<path d="M22 60 Q75 40 128 70" stroke="#fff" stroke-width="2" fill="none"/>', ["supports and connects", "bone, tendon, fat,", "cartilage, blood", "cells in a matrix"]),
              ("Muscle", "#DB2F30", ''.join(f'<rect x="20" y="{42+j*12}" width="110" height="9" rx="4" fill="#fff"/>' for j in range(4)), ["moves the body", "skeletal, smooth,", "cardiac (heart)", "cells contract"]),
              ("Nervous", "#0047BA", '<circle cx="60" cy="64" r="11" fill="#fff"/><path d="M71 64 L130 64 M60 53 L48 40 M52 70 L36 84 M56 54 L66 38" stroke="#fff" stroke-width="3"/>', ["carries signals", "brain, spinal cord,", "nerves", "long cells with branches"])])) +
  '<text x="330" y="238" text-anchor="middle" font-size="11" fill="#5b6676">Each tissue\'s structure (shape) fits its function (job). Simplified drawings.</text></svg>')

LESSON = {
 "unit": "Unit 4: The Human Body",
 "title": "Levels of Organization",
 "subtitle": "You are made of about 30 trillion cells, but not a pile of them. Cells form tissues, tissues form organs, organs form systems, and systems work together to keep you alive. This week goes far beyond the basics you met in Week 11.",
 "objectives": [
  "Describe the full hierarchy of organization from atoms and molecules to cells, tissues, organs, organ systems and organisms.",
  "Identify the four main types of animal tissue and explain how each tissue's structure fits its function.",
  "Explain how cells become specialized, even though nearly every cell in the body has the same DNA.",
  "Explain how an organ is built from several tissues and how organ systems interact to maintain homeostasis.",
  "Compare levels of organization in plants and animals, and investigate a plant's vascular tissue."],
 "vocab": [
  ["specialized cell", "A cell with a particular structure and job, such as a nerve cell or a red blood cell."],
  ["differentiation", "The process by which unspecialized cells become specialized cells."],
  ["stem cell", "An unspecialized cell that can divide and become different kinds of cells."],
  ["tissue", "A group of similar cells that work together to do one job."],
  ["organ", "A structure made of two or more tissue types that work together, such as the heart or a leaf."],
  ["organ system", "A group of organs that work together to do a major job, such as the digestive system."],
  ["xylem and phloem", "Plant vascular tissues: xylem carries water up from the roots; phloem carries sugars made in the leaves."]],
 "reconnect": {
  "title": "Unit 3: The diversity of life",
  "intro": "Unit 4 zooms inside one organism, you. Start with what you know about living things.",
  "items": [
   {"t":"text","q":"Keeping a stable internal balance, such as body temperature, is called ___.","a":[{"all":[["homeostasis"]],"none":["not"]}],"show":"homeostasis","pts":2,"why":"A characteristic of life from Week 11."},
   {"t":"text","q":"Humans are in which kingdom?","a":[{"all":[["animal"]],"none":["not","plant"]}],"show":"Animalia","pts":2,"why":"Many-celled eukaryotes that eat other organisms."},
   {"t":"text","q":"Cells with a nucleus are called eukaryotic. Cells with no nucleus, like bacteria, are called ___.","a":[{"all":[["prokaryot"]],"none":["not prokaryot","eukaryot"]}],"show":"prokaryotic","pts":2,"why":"Week 15."},
   {"t":"open","key":"rc_cellfun","q":"In Unit 2 you learned that cells are the basic unit of life. Name one job a single cell can do and one job it cannot do alone in your body.","min":12,"rows":2,"rubric":["A job a single cell does (uses energy, makes proteins, divides, takes in nutrients)","A job that needs many cells (pumping blood, thinking, walking, digesting a meal)"],"model":"A single cell can use energy and make proteins, but one cell alone cannot pump blood around the body; that takes the whole heart."}]},
 "hook": {
  "title": "One Scraped Knee, Four Tissues",
  "visual": LADDER,
  "html": "<p>You trip on the sidewalk and scrape your knee. In that one moment, four different kinds of tissue go to work. <b>Nervous tissue</b> sends a pain signal to your brain in a fraction of a second. <b>Muscle tissue</b> pulls your leg back. <b>Connective tissue</b>, in the form of blood, rushes in with cells that plug the wound. Over the next week, <b>epithelial tissue</b> grows back over the scrape to seal your skin.</p><p>In Week 11 you learned the basic levels: cells, tissues, organs, systems. This week you go deeper: down to the atoms and molecules inside cells, into the four tissue types and how they are built, and out to the way your organ systems talk to each other.</p><div class='callout'><b>Big question:</b> How do trillions of cells work together as one living person?</div>"},
 "learn": [
  {"title": "From Atoms to Organisms",
   "html": "<p>The levels of organization start even smaller than cells:</p><ol><li><b>Atoms</b> such as carbon, hydrogen, oxygen and nitrogen are the building blocks of all matter.</li><li>Atoms join to form <b>molecules</b>: water, sugars, proteins, fats and DNA.</li><li>Molecules build <b>cells</b>, the smallest level that is alive.</li><li>Similar cells form <b>tissues</b>; tissues form <b>organs</b>; organs form <b>organ systems</b>; systems make an <b>organism</b>.</li></ol><p>The human body has about 30 trillion human cells, hundreds of kinds of specialized cells, dozens of organs and about 11 major organ systems.</p><p>Here is the key idea: <b>each level can do something the level below cannot do alone.</b> A single heart muscle cell can twitch, but only a whole heart can pump blood. No single neuron can think, but your brain can. Scientists call these new abilities <b>emergent properties</b>.</p>",
   "checks": [
    {"t":"order","q":"Put these levels in order from smallest to largest.","items":["atom","molecule","cell","tissue","organ","organ system","organism"],"pts":3,"why":"Each level is built from the one before it."},
    {"t":"text","q":"What is the smallest level of organization that is alive?","a":[{"all":[["cell"]],"none":["not cell","atom","molecule"]}],"show":"the cell","pts":2,"why":"Atoms and molecules are not alive by themselves."},
    {"t":"open","key":"emergent","q":"Explain the idea of an emergent property using an example from your body that is not the heart or the brain.","min":25,"rows":3,"rubric":["A new ability that appears only when parts work together at a higher level","A valid example (stomach digesting a meal, lungs breathing, legs walking, eyes seeing)"],"model":"One stomach cell can make a little acid or mucus, but only the whole stomach, with its muscle squeezing and its lining releasing acid and enzymes, can churn and break down a meal. Digesting a meal is an ability that emerges at the organ level."}]},
  {"title": "Specialized Cells: Same DNA, Different Jobs",
   "html": "<p>You began as a single fertilized cell. That cell divided again and again, and its descendants became nerve cells, muscle cells, skin cells and red blood cells. This process is called <b>differentiation</b>.</p><p>Here is the surprising part: nearly every cell in your body carries the same DNA, the same complete set of instructions. Cells become different because each type <b>uses</b> different instructions. A muscle cell switches on the genes for proteins that contract; a red blood cell fills with hemoglobin, the protein that carries oxygen. (Mature red blood cells even lose their nucleus to make more room.)</p><p>Some cells, called <b>stem cells</b>, stay unspecialized and can still become other cell types. Stem cells in your bone marrow make about 2 million new red blood cells every second.</p><ul><li><b>Nerve cell:</b> long branches carry signals over long distances.</li><li><b>Red blood cell:</b> a small, flexible disk with a dent in the middle squeezes through tiny vessels and has lots of surface for oxygen.</li><li><b>Muscle cell:</b> long and full of proteins that pull and shorten.</li></ul>",
   "checks": [
    {"t":"text","q":"What is the name for the process by which unspecialized cells become specialized cells?","a":[{"all":[["differentiat"]],"none":["not"]}],"show":"differentiation","pts":2,"why":"Cells \"differ\" by using different genes."},
    {"t":"open","key":"samedna","q":"A nerve cell and a muscle cell in your arm have the same DNA. Why are they so different?","min":20,"rows":2,"rubric":["Each cell uses (switches on) different parts of the DNA instructions","So they make different proteins and develop different shapes and jobs"],"model":"They have the same instructions but use different parts of them. The nerve cell switches on genes for carrying signals, and the muscle cell switches on genes for proteins that contract, so they build different shapes and do different jobs."},
    {"t":"open","key":"rbcshape","q":"Explain how one feature of a red blood cell's structure fits its function.","min":20,"rows":2,"rubric":["A structure (small flexible disk, dent in the middle, no nucleus, full of hemoglobin)","Linked to its function (fitting through tiny vessels, more surface or room for carrying oxygen)"],"model":"A red blood cell is small and flexible, so it can bend to squeeze through the tiniest blood vessels and deliver oxygen everywhere in the body."}]},
  {"title": "The Four Tissue Types",
   "visual": TISSUES,
   "html": "<p>Animal bodies are built from four main kinds of tissue:</p><ul><li><b>Epithelial tissue</b> covers surfaces and lines organs: your skin, the lining of your mouth and stomach. Its cells are packed tightly to protect, absorb or release substances.</li><li><b>Connective tissue</b> supports and connects. Bone, cartilage, tendons, fat and even blood are connective tissues: cells scattered in a material called a matrix (hard in bone, liquid in blood).</li><li><b>Muscle tissue</b> contracts to move things: <i>skeletal</i> muscle moves bones, <i>smooth</i> muscle squeezes organs like the stomach, and <i>cardiac</i> muscle pumps the heart.</li><li><b>Nervous tissue</b> carries electrical signals: the brain, spinal cord and nerves.</li></ul><p>An <b>organ</b> uses several tissues together. Your stomach has epithelial tissue lining it, smooth muscle to churn food, connective tissue holding the layers together, and nervous tissue controlling it all.</p>",
   "checks": [
    {"t":"blanks","q":"Name the tissue type.","sent":"Bone and blood: ___ &nbsp; Brain and nerves: ___ &nbsp; The lining of your stomach: ___","blanks":[[{"all":[["connective"]],"none":["not"]}],[{"all":[["nervous","nerve","neural"]],"none":["not"]}],[{"all":[["epithel"]],"none":["not"]}]],"show":"connective; nervous; epithelial","pts":3,"why":"Blood has cells in a liquid matrix, so it counts as connective tissue."},
    {"t":"text","q":"Which type of muscle tissue pumps the heart?","a":[{"all":[["cardiac","heart"]],"none":["not","skeletal","smooth"]}],"show":"cardiac muscle","pts":2,"why":"Cardiac muscle never gets tired the way skeletal muscle does."},
    {"t":"open","key":"stomachlayers","q":"Use the stomach to explain why an organ needs more than one type of tissue.","min":25,"rows":3,"rubric":["Names at least three tissues in the stomach and their jobs","Explains that digestion needs all the jobs working together"],"model":"The stomach's epithelial lining releases acid and enzymes, its smooth muscle churns the food, connective tissue holds the layers together, and nervous tissue tells it when to work. No single tissue could digest a meal; the stomach needs all of those jobs at once."}]},
  {"title": "Systems That Work Together, in Animals and Plants",
   "html": "<p>Your organ systems never work alone. When you run, your <b>muscular</b> system works harder and needs more oxygen. Your <b>nervous</b> system signals your <b>respiratory</b> system to breathe faster and your <b>circulatory</b> system to pump faster. Your skin, part of the <b>integumentary</b> system, sweats to cool you. Together they keep your body in homeostasis.</p><p><b>Plants</b> have levels of organization too, with three main tissue systems: <b>dermal tissue</b> (the protective outer layer), <b>ground tissue</b> (where photosynthesis and storage happen) and <b>vascular tissue</b>. Vascular tissue includes <b>xylem</b>, tubes that carry water and minerals up from the roots, and <b>phloem</b>, which carries sugars from the leaves to the rest of the plant. Leaves, stems and roots are a plant's organs; the root system and shoot system are its organ systems.</p>",
   "checks": [
    {"t":"text","q":"Which plant vascular tissue carries water up from the roots?","a":[{"all":[["xylem"]],"none":["not xylem","phloem"]}],"show":"xylem","pts":2,"why":"Phloem carries sugars."},
    {"t":"open","key":"running","q":"During a long run, name two organ systems that work together and explain how their teamwork helps maintain homeostasis.","min":25,"rows":3,"rubric":["Two correct systems (muscular, respiratory, circulatory, nervous, integumentary)","How they cooperate (more oxygen delivered, heat released, signals sent) to keep conditions stable"],"model":"The respiratory system breathes faster to bring in more oxygen, and the circulatory system pumps that oxygen to working muscles faster. Together they keep the muscles supplied, so the body's oxygen level stays balanced even during hard exercise."},
    {"t":"num","q":"A human body has about 30 trillion cells. About 25 trillion of them are red blood cells. About what percent of your cells are red blood cells? Round to the nearest whole percent.","a":83,"tol":1,"unit":"%","pts":2,"why":"25 ÷ 30 ≈ 0.83, about 83%. Red blood cells are tiny but extremely numerous."}]}],
 "handson": {
  "title": "Zoom In: Build the Ladder and Watch Vascular Tissue Work",
  "intro": "Build a physical model of the levels of organization, then watch a plant's xylem carry colored water.",
  "materials": ["7 containers that nest inside one another (bowls, boxes or cups) or 7 sheets of paper of different sizes", "Sticky notes and a marker", "A stalk of napa cabbage or a white carnation", "A clear glass or jar of water", "Blue or red food coloring", "A knife (used by an adult) and a cutting board", "A magnifying glass", "Paper and pencil"],
  "steps": [
   "Label the containers from smallest to largest: atom, molecule, cell, tissue, organ, organ system, organism. Nest them together, then take them apart one level at a time, saying aloud one example from your body for each level.",
   "Vascular tissue test: fill a glass halfway with water and add 15 to 20 drops of food coloring. An adult trims the bottom of the cabbage stalk or flower stem with a fresh cut. Stand it in the colored water.",
   "Check it after 1 hour, 4 hours and 24 hours. Sketch what you see each time.",
   "After 24 hours, an adult cuts across the stem. Look at the cut end with a magnifying glass and count the colored dots or lines: those are bundles of xylem.",
   "Food coloring stains skin and fabric: wear old clothes and wipe spills right away. Do not eat the stained plant. Pour the colored water down the sink when you finish."],
  "record": [
   {"t":"open","key":"vascrec","q":"Describe your observations at 1, 4 and 24 hours, and what you saw in the cut stem. What tissue carried the color, and in which direction?","min":40,"rows":5,"rubric":["Observations at three times","Describes the colored dots or lines in the cut stem","Identifies xylem carrying water (and color) upward from the cut end toward the leaves or petals"],"model":"At 1 hour nothing showed. At 4 hours thin blue lines appeared in the cabbage's white rib. At 24 hours the leaf edges were tinted blue. When my dad cut the stem I counted about 14 blue dots. Those are bundles of xylem, which carried the colored water up from the bottom toward the leaves."},
   {"t":"open","key":"ladderrec","q":"For each of the seven levels in your nesting model, write one example from your own body. Then explain why the cabbage stalk counts as an organ, not a tissue.","min":40,"rows":5,"rubric":["Seven correct examples in order","Explains that the stalk contains several tissue types (dermal, ground, vascular) working together"],"model":"Atom: oxygen. Molecule: water. Cell: red blood cell. Tissue: cardiac muscle. Organ: heart. Organ system: circulatory system. Organism: me. The cabbage stalk is an organ because it contains more than one tissue: a dermal outer layer, ground tissue and the xylem and phloem in its vascular bundles."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"cityanalogy","q":"Some people compare the body to a city: cells are workers, tissues are teams, organs are buildings and organ systems are city services. Explain where this comparison works well and one place where it breaks down.","min":80,"rows":6,"rubric":["Explains how the levels map onto the city (accurately)","Identifies at least one real limit of the analogy (workers can change jobs freely; city parts are not all made from one original cell with the same instructions; bodies grow and repair themselves; emergent properties)","Uses correct vocabulary"],"model":"The comparison works because, like workers in teams, cells of the same kind group into tissues, and different teams work together in buildings the way tissues build organs. City services such as water and power resemble organ systems like the circulatory system, and the whole city depends on all of them. It breaks down because city workers can change jobs, while most specialized cells cannot; and every cell in the body came from one original cell with the same DNA, which is nothing like how a city is built."},
   {"t":"open","key":"transplant","q":"When a person receives a kidney transplant, doctors replace an organ, not individual cells. Using levels of organization, explain why replacing the whole organ makes more sense than replacing kidney cells one at a time.","min":70,"rows":5,"rubric":["The kidney's function depends on many tissues arranged in a precise structure","Individual cells cannot do the organ's job (emergent property)","Organization at the organ level cannot be rebuilt cell by cell (at least not with today's technology)"],"model":"A kidney filters blood because millions of cells are arranged into tissues and tiny structures that work together in a precise pattern. Individual kidney cells alone cannot filter blood; that ability only emerges when they are organized into the whole organ. Doctors cannot build that organization one cell at a time, so replacing the whole organ, with all its tissues already arranged, is the way to restore the function."}]},
 "exit": [
  {"t":"text","q":"Which tissue type covers and lines body surfaces, such as your skin?","a":[{"all":[["epithel"]],"none":["not"]}],"show":"epithelial tissue","pts":2,"why":"Tightly packed cells protect and line."},
  {"t":"text","q":"Which plant tissue carries sugars from the leaves to the rest of the plant?","a":[{"all":[["phloem"]],"none":["not phloem","xylem"]}],"show":"phloem","pts":2,"why":"Xylem carries water up; phloem carries sugars."},
  {"t":"text","q":"What type of cell is still unspecialized and can become other kinds of cells?","a":[{"all":[["stem"]],"none":["not"]}],"show":"a stem cell","pts":2,"why":"Bone marrow stem cells make blood cells."},
  {"t":"open","key":"exit_organ","q":"Explain the difference between a tissue and an organ, with one example of each.","min":12,"rows":2,"rubric":["A tissue is a group of similar cells doing one job; an organ is made of two or more tissue types working together","Correct examples"],"model":"A tissue is a group of similar cells doing one job, like cardiac muscle. An organ is made of several tissues working together, like the heart, which has muscle, nervous, connective and epithelial tissue."}],
 "next": "Week 17: the skeletal and muscular systems."
}

TEACHER = {
 "standards": [
  "SC.6.L.14.1: Describe and identify patterns in the hierarchical organization of organisms from atoms to molecules to cells to tissues to organs to organ systems to organisms.",
  "SC.6.L.14.5: Identify and investigate the general functions of the major systems of the human body (digestive, respiratory, circulatory, reproductive, excretory, immune, nervous, and musculoskeletal) and describe ways these systems interact with each other to maintain homeostasis.",
  "SC.6.L.14.3: Recognize and explore how cells of all organisms undergo similar processes to maintain homeostasis, including extracting energy from food, getting rid of waste, and reproducing.",
  "NGSS MS-LS1-3: Use argument supported by evidence for how the body is a system of interacting subsystems composed of groups of cells."],
 "materials": ["The interactive lesson", "7 nesting containers or papers, sticky notes, a marker", "A napa cabbage stalk or white carnation, a glass, food coloring", "A knife (adult use), cutting board, magnifying glass", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Unit 3 warm-up questions."],
  [4, "Hook", "Walk through the scraped knee: which tissue does what?"],
  [10, "Atoms to organisms", "Order the levels; discuss emergent properties."],
  [11, "Specialized cells", "Explain differentiation and same-DNA, different-genes; study the red blood cell."],
  [12, "Four tissue types", "Study the tissue chart; build the stomach from its layers."],
  [10, "Systems and plants", "Trace the systems during a run; introduce plant tissue systems and xylem."],
  [7, "Assign", "Start the dye test today; assign the nesting model, Think Deeper and the Exit Check."]],
 "key_questions": ["What can this level do that the level below cannot?", "How does this structure fit its function?", "Which tissues build this organ?", "Which systems are working together here?"],
 "misconceptions": ["Cells are not alive; only organisms are.", "Different body cells have different DNA.", "Blood is not a tissue.", "Each organ system works on its own."],
 "support": ["Keep the nesting containers on the desk during the lesson.", "Use a four-color tissue chart.", "Pre-label the stomach-layers drawing."],
 "challenge": ["Research how scientists grow skin tissue in labs to treat burns.", "Compare the number of organ systems in a frog and a human."],
 "background": "<p>Cell counts: Sender, Fuchs and Milo (2016) estimated about 30 trillion human cells in a reference adult, of which about 84% (roughly 25 trillion) are red blood cells, and a similar number of bacteria. Estimates of distinct human cell types range from about 200 (classical histology) to many hundreds with modern single-cell methods. Bone marrow produces roughly 2 to 3 million red blood cells per second. The 11 organ systems commonly listed: integumentary, skeletal, muscular, nervous, endocrine, circulatory (cardiovascular), lymphatic/immune, respiratory, digestive, urinary/excretory and reproductive. Napa cabbage and white carnations show xylem staining within a few hours; celery was used in Week 9 for osmosis, so it is not repeated here.</p>",
 "sources": ["Sender, R., Fuchs, S. and Milo, R. (2016), Revised estimates for the number of human and bacteria cells in the body, PLOS Biology 14(8).", "National Cancer Institute SEER Training Modules, Body Functions and Life Process; Tissues.", "OpenStax, Anatomy and Physiology 2e, Chapter 4 (The Tissue Level of Organization).", "University of Florida IFAS, plant structure resources."]
}

PRINT = {
 "directions": "Answer in complete sentences.",
 "items": [
  {"q":"List the levels of organization from atom to organism, with a human example for each.","a":"Atom (oxygen), molecule (water), cell (muscle cell), tissue (muscle tissue), organ (heart), organ system (circulatory), organism (a person).","lines":3},
  {"q":"Name the four main animal tissue types and one example of each.","a":"Epithelial (skin), connective (bone, blood), muscle (cardiac), nervous (brain).","lines":2},
  {"q":"Explain differentiation in your own words.","a":"Unspecialized cells become specialized cells by using different parts of the same DNA.","lines":2},
  {"q":"What is an emergent property? Give an example.","a":"An ability that appears only at a higher level, such as a heart pumping blood (not possible for one cell).","lines":2},
  {"q":"Compare xylem and phloem.","a":"Xylem carries water and minerals up from roots; phloem carries sugars from leaves.","lines":2},
  {"q":"Name two organ systems that work together when you are hot, and explain how.","a":"Nervous system senses heat and signals; integumentary system sweats; circulatory system sends blood to the skin to release heat.","lines":2}]
}
