CHAIN = ('<svg viewBox="0 0 660 200" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Concept chain linking the four Unit 3 science lessons">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Unit 3: The Diversity of Life in four questions</text>'
  '<defs><marker id="ch" viewBox="0 0 10 10" markerWidth="6" markerHeight="6" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="#0A1F3D"/></marker></defs>'
  + ''.join(f'<rect x="{12+i*162}" y="40" width="150" height="130" rx="12" fill="{c}"/><text x="{87+i*162}" y="62" text-anchor="middle" fill="#fff" font-weight="bold" font-size="12">{wk}</text><text x="{87+i*162}" y="84" text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">{q1}</text><text x="{87+i*162}" y="102" text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">{q2}</text>'
            + ''.join(f'<text x="{87+i*162}" y="{126+j*16}" text-anchor="middle" fill="#fff" font-size="11">{t}</text>' for j, t in enumerate(ans))
            + (f'<path d="M{162+i*162} 105 L{174+i*162} 105" stroke="#0A1F3D" stroke-width="2.5" marker-end="url(#ch)"/>' if i < 3 else '')
            for i, (wk, q1, q2, ans, c) in enumerate([
              ("Week 11", "Is it", "alive?", ["cells, growth, energy,", "response, reproduction,", "homeostasis, adaptation"], "#3d9a2f"),
              ("Week 12", "Where does", "it belong?", ["domain to species;", "Genus species names;", "3 domains, 6 kingdoms"], "#0047BA"),
              ("Week 13", "What is", "its name?", ["dichotomous keys:", "paired, opposite,", "observable traits"], "#C9A84C"),
              ("Week 14", "What about", "the tiny ones?", ["bacteria, archaea,", "protists, fungi;", "helpful and harmful"], "#DB2F30")])) +
  '<text x="330" y="194" text-anchor="middle" font-size="11" fill="#5b6676">A field guide uses all four: living things, classified, identified with a key, including the microscopic.</text></svg>')

LESSON = {
 "unit": "Unit 3: The Diversity of Life",
 "title": "Mid-Year Review and Field Guide Project",
 "subtitle": "Connect everything from Unit 3 (the characteristics of life, classification, dichotomous keys and microorganisms) to the cells you studied in Unit 2. Then build a field guide to the living things around your home and take the Unit 3 checkpoint.",
 "objectives": [
  "Explain how the four Unit 3 ideas connect: characteristics of life, classification, keys and microorganisms.",
  "Connect classification to cell structure from Unit 2 (nucleus, cell wall, chloroplasts).",
  "Plan and produce a field guide with accurate classification, scientific names, observations and a dichotomous key.",
  "Observe living things safely and record evidence.",
  "Show mastery of Unit 3 on the checkpoint."],
 "vocab": [
  ["field guide", "A book that helps people identify living things in nature, with pictures, descriptions and keys."],
  ["naturalist", "A person who studies plants and animals by observing them in nature."],
  ["prokaryote", "A single-celled organism with no nucleus (bacteria and archaea)."],
  ["eukaryote", "An organism whose cells have a nucleus (protists, fungi, plants and animals)."],
  ["community science", "Science in which members of the public collect data, such as photographing plants and animals for researchers."]],
 "reconnect": {
  "title": "Week 14: Microorganisms",
  "intro": "Start with last week, including your bread test.",
  "items": [
   {"t":"text","q":"Antibiotics kill bacteria. What kind of pathogen do they not work against?","a":[{"all":[["virus"]],"none":["not virus","no virus","bacteria and","and bacteri","or bacteri","bacteria or","fung"]}],"show":"viruses","pts":2,"why":"Viruses are not cells."},
   {"t":"num","q":"How many micrometers are in 2 millimeters?","a":2000,"unit":"µm","pts":2,"why":"2 × 1,000 = 2,000 µm."},
   {"t":"text","q":"Which scientist's 1928 observation of a mold led to penicillin?","a":[{"all":[["fleming"]],"none":["not"]}],"show":"Alexander Fleming","pts":2,"why":"The mold was Penicillium."},
   {"t":"open","key":"rc_bread","q":"What did your bread test show about hand-washing? Give your evidence in one or two sentences.","min":15,"rows":2,"rubric":["A claim about hand-washing","Evidence from the student's own data (mold percents or squares compared with the control)"],"model":"Hand-washing reduced mold: by the last day the unwashed slice was 75% covered and the washed slice about 21%, close to the control's 12.5%."}]},
 "hook": {
  "title": "A Naturalist in Early Florida",
  "visual": CHAIN,
  "html": "<p>In the 1720s, an English naturalist named Mark Catesby traveled through South Carolina and the Bahamas, sketching birds, fish, snakes and plants. (In his book's title, \"Florida\" meant the lands south of Carolina, which Spain then claimed.) His book, <i>The Natural History of Carolina, Florida and the Bahama Islands</i>, published in parts between 1729 and 1747, was one of the first richly illustrated books about North American plants and animals. Catesby relied on Native American guides and learned from enslaved Africans, who knew the land's plants and animals far better than he did, though he rarely named them.</p><p>Today anyone can add to the world's record of life. Through community science apps, families photograph plants and animals so scientists can track where species live. This week you become a naturalist and make a field guide to your own corner of the world.</p><div class='callout'><b>Big question:</b> How do scientists organize and identify the incredible diversity of life?</div>"},
 "learn": [
  {"title": "Connecting the Big Ideas of Unit 3",
   "html": "<p>Every idea in Unit 3 builds on the one before it:</p><ol><li><b>Week 11:</b> To be alive, something must be made of cells, use energy, grow and develop, respond to its environment, reproduce, maintain homeostasis and adapt over generations.</li><li><b>Week 12:</b> Scientists classify living things by shared traits and ancestry, from domain to species, and give each species a two-part scientific name.</li><li><b>Week 13:</b> A dichotomous key uses paired, opposite, observable traits to identify an organism.</li><li><b>Week 14:</b> Most life is microscopic: bacteria, archaea, protists and microscopic fungi, mostly helpful and sometimes harmful.</li></ol>",
   "checks": [
    {"t":"text","q":"In the scientific name Quercus virginiana (the southern live oak), which word is the species name?","a":[{"all":[["virginiana"]],"none":["not","quercus"]}],"show":"virginiana","pts":2,"why":"The genus comes first (Quercus); the species name second."},
    {"t":"open","key":"rv_virus","q":"Use the characteristics of life to explain why a virus is not placed in any kingdom.","min":20,"rows":2,"rubric":["Viruses are not made of cells and cannot use energy or reproduce on their own","Classification kingdoms are for living things"],"model":"Kingdoms group living things, and viruses fail key characteristics of life: they are not cells and cannot use energy or reproduce on their own, only inside a host cell."},
    {"t":"blanks","q":"Order the levels of classification from broadest to most specific.","sent":"Domain, ___, phylum, ___, order, family, genus, species","blanks":[[{"all":[["kingdom"]],"none":["not"]}],[{"all":[["class"]],"none":["not"]}]],"show":"kingdom; class","pts":2,"why":"Domain, kingdom, phylum, class, order, family, genus, species."}]},
  {"title": "Mid-Year Review: Cells and Classification",
   "html": "<p>Classification connects to the cells you studied in Unit 2:</p><ul><li><b>Prokaryotes</b> (bacteria and archaea) have no nucleus. Their DNA floats in the cytoplasm.</li><li><b>Eukaryotes</b> (protists, fungi, plants and animals) have a nucleus and other organelles, such as mitochondria.</li><li><b>Plants</b> have cell walls and chloroplasts, so they make their own food by photosynthesis (Week 8).</li><li><b>Fungi</b> have cell walls but no chloroplasts; they absorb food.</li><li><b>Animals</b> have no cell walls and no chloroplasts; they eat other organisms.</li></ul><p>So a single microscope view can tell a scientist a lot about where an organism belongs.</p>",
   "checks": [
    {"t":"text","q":"Under a microscope, a cell has a nucleus, a cell wall and chloroplasts. Which kingdom does it most likely belong to?","a":[{"all":[["plant"]],"none":["not","animal","fung"]}],"show":"Plants","pts":2,"why":"Only plant (and some protist) cells have chloroplasts; together with a cell wall and nucleus, this points to a plant."},
    {"t":"text","q":"Bacteria and archaea have no nucleus. What are organisms whose cells have no nucleus called?","a":[{"all":[["prokaryot","procaryot"]],"none":["not prokaryot","eukaryot"]}],"show":"prokaryotes","pts":2,"why":"Pro = before; karyon = nucleus."},
    {"t":"open","key":"pondcell","q":"A green film covers a pond. Under a microscope, each organism is a single cell with a nucleus and chloroplasts. Which kingdom does it most likely belong to, and why not the plant kingdom?","min":25,"rows":3,"rubric":["Protists: single-celled organisms with a nucleus, some with chloroplasts (such as algae)","Plants are many-celled, so a single cell with chloroplasts points to a protist"],"model":"It is most likely a protist, such as an alga. It has a nucleus, so it is a eukaryote, and its chloroplasts let it make food, but it is only one cell. Plants are made of many cells, so a single cell like this belongs with the protists."}]},
  {"title": "Planning Your Field Guide",
   "html": "<p>Your Unit 3 project is a <b>field guide to the living things near your home</b>. A strong field guide page includes:</p><ul><li>A labeled drawing or photo you took yourself.</li><li>The common name and the scientific name (genus and species, written correctly).</li><li>Its classification as far as you can find it: domain, kingdom, phylum, class, order, family, genus.</li><li>Observable traits someone could use to identify it, and where and when you saw it.</li><li>One fact about how it lives, and whether it is native to Florida or invasive.</li><li>A source for facts you looked up (for example, UF/IFAS Extension or the Florida Fish and Wildlife Conservation Commission).</li></ul><p>Your guide also needs a <b>dichotomous key</b> to all of your organisms and one page on a <b>microorganism</b> (you could use the mold from your bread test or <i>Karenia brevis</i>).</p><p><b>Observe safely:</b> look but don't touch unknown plants or animals; Florida has venomous snakes, fire ants and poison ivy; go with an adult; never collect in state parks; wash your hands afterward.</p>",
   "checks": [
    {"t":"text","q":"In a scientific name such as Gopherus polyphemus, which part is always capitalized: the genus or the species name?","a":[{"all":[["genus"]],"none":["not genus","species not","species and","and species","both","species is"]}],"show":"the genus (Gopherus)","pts":2,"why":"Only the genus is capitalized; the species name is lowercase, and the whole name is italicized when printed."},
    {"t":"num","q":"Your field guide has 6 organisms. How many couplets will its dichotomous key need?","a":5,"unit":"couplets","pts":2,"why":"One fewer couplet than organisms."},
    {"t":"open","key":"goodtrait","q":"For your field guide, why is \"has a white stripe on each side of its body\" a better identifying trait than \"is cute\"?","min":15,"rows":2,"rubric":["The stripe is observable and the same for every observer","\"Cute\" is an opinion and varies by person"],"model":"Anyone can see a white stripe, so everyone will identify it the same way. \"Cute\" is an opinion, and people would disagree."}]}],
 "handson": {
  "title": "Field Guide Fieldwork",
  "intro": "Go outside as a naturalist. Observe, sketch and record the living things near your home for your field guide.",
  "materials": ["A notebook or clipboard and pencil", "Colored pencils", "A ruler with centimeters", "A phone or camera for photos (with a parent)", "Optional: a magnifying glass and binoculars", "Optional: a Florida field guide from the library", "Water, sunscreen and closed-toe shoes", "Insect repellent (applied by an adult)"],
  "steps": [
   "With an adult, explore your yard, a neighborhood park or a nature trail for 30 to 45 minutes. Choose at least 5 different living things to observe in person: plants, insects, birds, lizards, fungi.",
   "For each one, make a quick sketch with labels, measure it in centimeters if you safely can (or estimate), and note where, when and what it was doing.",
   "Look but don't touch unknown plants or animals. Watch for fire ants, snakes and poison ivy. Do not collect anything in a state park. Stay well away from gopher tortoise burrows. Wash your hands and check for ticks when you come in.",
   "At home, use a field guide, UF/IFAS Extension or the FWC website with a parent to find each organism's scientific name and classification.",
   "Draft your dichotomous key for all of your organisms, then test it on a family member."],
  "record": [
   {"t":"open","key":"fieldnotes","q":"List your organisms with common name, scientific name, kingdom, and one observation of each (where, when, what it was doing).","min":50,"rows":8,"rubric":["At least 5 organisms observed in person","Correct common and scientific names, written correctly","Correct kingdom for each","Specific, dated observations"],"model":"1. Green anole, Anolis carolinensis, Animalia: on the porch rail at 4 p.m., Nov 20, puffing out its pink throat fan. 2. Cabbage palm, Sabal palmetto, Plantae: by the driveway, fan leaves with a curved midrib. 3. Monarch butterfly, Danaus plexippus, Animalia: on milkweed, 10 a.m. 4. Saw palmetto, Serenoa repens, Plantae: along the fence. 5. Turkey tail fungus, Trametes versicolor, Fungi: on a fallen oak log."},
   {"t":"open","key":"fieldkey","q":"Write your draft dichotomous key, and describe one couplet you changed after testing it.","min":40,"rows":8,"rubric":["One fewer couplet than organisms","True opposites with observable traits","Describes a revision based on the test"],"model":"1a. Moves on its own ........ go to 2\n1b. Does not move on its own ........ go to 3\n2a. Has wings ........ monarch butterfly\n2b. No wings; has scales ........ green anole\n3a. Grows from wood; no leaves ........ turkey tail fungus\n3b. Has leaves ........ go to 4\n4a. Leaf stem is smooth ........ cabbage palm\n4b. Leaf stem has sharp teeth along its edges ........ saw palmetto\nI changed couplet 1 from \"is an animal / is not an animal\" because my tester didn't know whether to call a fungus an animal."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores this.",
  "items": [
   {"t":"open","key":"changing","q":"Scientists once divided all life into two kingdoms, plants and animals. Today they use three domains and six kingdoms. Explain what evidence changed their minds and why changing a classification is a strength of science, not a weakness.","min":80,"rows":6,"rubric":["Evidence: microscopes revealed microorganisms; cell structure (nucleus or not); DNA and Woese's work on archaea","Science changes when new evidence appears; durable but open to change (SC.6.N.2.2)","Clear, organized explanation"],"model":"Microscopes revealed microorganisms that were neither plants nor animals, and studying cells showed that bacteria have no nucleus. Later, Carl Woese's study of genetic material showed that archaea are a separate domain. Scientists changed the system because the evidence demanded it. That is a strength: science is trustworthy because it corrects itself when better evidence appears, instead of holding onto old ideas."}]},
 "checkpoint": {
  "title": "Unit 3 Checkpoint: The Diversity of Life",
  "intro": "This checkpoint covers Weeks 11 to 15. Mastery is 85 or higher. If you score below 85, your teacher will review with you, then you will retake it.",
  "parts": [
   {"title": "Part A: Characteristics of living things", "items": [
    {"t":"text","q":"A tomato plant bends toward a sunny window. Which characteristic of life does this show?","a":[{"all":[["respond","response","stimul","react","tropism"]],"none":["not respon","not react","adapt"]}],"show":"response to the environment (stimuli)","pts":3,"why":"Plants respond to light."},
    {"t":"text","q":"Your body sweats on a hot day to keep its temperature steady. What is keeping a stable internal balance called?","a":[{"all":[["homeostasis"]],"none":["not"]}],"show":"homeostasis","pts":3,"why":"Sweating cools the body."},
    {"t":"open","key":"cp_storm","q":"A hurricane grows stronger by taking in energy from warm ocean water, moves across the sea, and can spin off smaller storms. Explain why a hurricane is still not alive, using at least two characteristics of life.","pts":4,"min":20,"rows":2,"rubric":["A hurricane is not made of cells","It does not maintain homeostasis, grow and develop in an organized way, produce offspring like itself, or adapt over generations"],"model":"A hurricane is not made of cells, and every living thing is. It cannot keep a stable internal balance the way a body does, and the smaller storms it spins off are not offspring that inherit its traits, so it is not alive."}]},
   {"title": "Part B: Classification and scientific names", "items": [
    {"t":"text","q":"Two organisms are in the same family but different genera. Are they in the same order? Type yes or no.","a":["yes"],"show":"yes","pts":3,"why":"Every member of a family belongs to the same order."},
    {"t":"text","q":"The polar bear is Ursus maritimus. Which animal is more closely related to it: the Florida black bear (Ursus americanus) or the Florida panther (Puma concolor)? Type its common name.","a":[{"all":[["black bear","americanus"]],"none":["not black","not bear","not americanus","not ursus","panther not","panther because","puma because","panther is"]}],"show":"the Florida black bear (same genus, Ursus)","pts":3,"why":"Species in the same genus share a recent common ancestor (Week 12)."},
    {"t":"text","q":"Which domain includes all organisms whose cells have a nucleus?","a":[{"all":[["eukary","eucary"]],"none":["not eukary","prokary"]}],"show":"Eukarya","pts":3,"why":"Bacteria and Archaea are prokaryotes."},
    {"t":"open","key":"cp_newspecies","q":"Scientists discover a new species of beetle in a Florida forest. Explain two kinds of evidence they would compare with known beetles to decide which genus it belongs in.","pts":3,"min":15,"rows":2,"rubric":["Body structures or other observable traits (and development)","DNA, the strongest evidence of shared ancestry"],"model":"They would compare its body structures, such as its legs, antennae and wing covers, with known beetles, and they would compare its DNA. If its body and DNA are most like one genus, it shares a recent common ancestor with those beetles and belongs in that genus."}]},
   {"title": "Part C: Dichotomous keys", "items": [
    {"t":"cp_key_placeholder","q":"","pts":0}]},
   {"title": "Part D: Microorganisms", "items": [
    {"t":"text","q":"Which group of single-celled prokaryotes often lives in extreme places, such as hot springs and very salty lakes?","a":[{"all":[["archae","archea"]],"none":["not archae","protist","fung"]}],"show":"archaea","pts":3,"why":"Archaea are prokaryotes found in many extreme habitats (Week 14)."},
    {"t":"text","q":"What group of organisms breaks down dead plants and animals and returns nutrients to the soil?","a":[{"all":[["decompos","fung","bacteri"]],"none":["not decompos","scaveng","producer","consumer"]}],"show":"decomposers","pts":3,"why":"Many bacteria and fungi are decomposers."},
    {"t":"blanks","q":"Match each disease to its type of pathogen.","sent":"Chickenpox: ___ &nbsp; Salmonella food poisoning: ___ &nbsp; Ringworm: ___","blanks":[[{"all":[["virus","viral"]],"none":["not virus","not viral","bacteria and","and bacteri","fung"]}],[{"all":[["bacteri"]],"none":["not bacteri","virus and","and virus","fung"]}],[{"all":[["fung"]],"none":["not fung","virus","bacteri","or worm","worm or","and worm","worm and"]}]],"show":"virus; bacteria; fungus","pts":3,"why":"Chickenpox is viral; Salmonella is a bacterium; ringworm is a fungal skin infection, not a worm."},
    {"t":"open","key":"cp_redtide","q":"Karenia brevis, the cause of Florida's red tide, is a single cell with a nucleus. Is it a bacterium or a protist? Explain using cell evidence, and give one way a red tide harms people or wildlife.","pts":4,"min":20,"rows":2,"rubric":["Protist: it has a nucleus (a eukaryote); bacteria have no nucleus","An accurate harm: its toxin kills fish and other sea life, or makes beachgoers cough"],"model":"It is a protist, because it has a nucleus, and bacteria never do. During a red tide its toxin kills fish, and people walking on the beach can start coughing."}]}]},
 "next": "Unit 4: the human body, starting with levels of organization."
}

KEYPART = [
 {"t":"text","q":"<div class='cp-text'><div class='card' style='font-family:Georgia,serif'><b>Key to four Florida animals</b><br>1a. Has feathers ........ go to 2<br>1b. Has no feathers ........ go to 3<br>2a. Long legs; wades in water ........ great blue heron<br>2b. Short legs; perches in trees ........ northern cardinal<br>3a. Has a hard shell ........ gopher tortoise<br>3b. Has no shell; has fur ........ Florida panther</div></div>Use the key. An animal has no feathers and has a hard shell. What is it?","a":[{"all":[["gopher tortoise","tortoise"]],"none":["not"]}],"show":"gopher tortoise","pts":3,"why":"1b → 3a."},
 {"t":"text","q":"Use the same key. A bird with short legs is perched in an oak tree. What is it?","a":[{"all":[["cardinal"]],"none":["not","heron"]}],"show":"northern cardinal","pts":3,"why":"1a → 2b."},
 {"t":"open","key":"cp_couplet","q":"Explain what is wrong with this couplet and rewrite it: \"1a. Animal is brown. / 1b. Animal is large.\"","pts":4,"min":20,"rows":2,"rubric":["Not opposites (an animal could be both or neither); color and \"large\" without a measurement are weak traits","A correct rewrite with opposite, observable traits"],"model":"The statements are not opposites: an animal could be brown and large, or neither. Color and \"large\" are also unreliable. Better: \"1a. Animal has four legs. / 1b. Animal does not have four legs.\""}]
for part in LESSON["checkpoint"]["parts"]:
    if part["title"].startswith("Part C"):
        part["items"] = KEYPART

TEACHER = {
 "standards": [
  "SC.6.L.15.1: Analyze and describe how and why organisms are classified according to shared characteristics with emphasis on the Linnaean system combined with the concept of Domains.",
  "SC.6.L.14.3: Recognize and explore how cells of all organisms undergo similar processes to maintain homeostasis, including extracting energy from food, getting rid of waste, and reproducing.",
  "SC.6.L.14.6: Compare and contrast types of infectious agents that may infect the human body, including viruses, bacteria, fungi, and parasites.",
  "SC.6.N.2.2: Explain that scientific knowledge is durable because it is open to change as new evidence or interpretations are encountered.",
  "SC.6.N.1.1: Define a problem from the sixth grade curriculum, use appropriate reference materials to support scientific understanding, plan and carry out scientific investigation of various types, such as systematic observations or experiments, identify variables, collect and organize data, interpret data in charts, tables, and graphics, analyze information, make predictions, and defend conclusions."],
 "materials": ["The interactive lesson", "Notebook, pencils, colored pencils, a centimeter ruler", "A phone or camera; optional magnifying glass, binoculars and field guide", "The Unit 3 project rubric", "The Unit 3 checkpoint (in the lesson)"],
 "flow": [
  [6, "Reconnect", "Run the Week 14 Reconnect questions; discuss bread test results."],
  [4, "Hook", "Tell Catesby's story; show the concept chain."],
  [10, "Connecting big ideas", "Link the four weeks with the chain diagram."],
  [12, "Cells and classification", "Review prokaryotes, eukaryotes and kingdom cell traits."],
  [12, "Planning the field guide", "Walk through a model page; review safety rules."],
  [6, "Assign", "Assign the fieldwork, the field guide and Think Deeper."],
  [10, "Checkpoint preview", "Explain that the checkpoint is completed after class, independently, one try per item, with no answers shown until you review it. Mastery is 85; below 85 means a review lesson and a retake."]],
 "key_questions": ["Is it alive? How do you know?", "Where does it belong, and what evidence tells you?", "Could someone else use your key?", "Is it native or invasive?"],
 "misconceptions": ["All microorganisms are germs.", "Fungi are plants.", "Classification never changes.", "Ringworm is caused by a worm."],
 "support": ["Allow 5 organisms, with 4 observed in person; a photo from a library field guide may replace the fungus if none can be found.", "Provide a field guide page template.", "Let the student photograph instead of sketch."],
 "challenge": ["Upload observations to a community science app with a parent's permission.", "Add a page comparing a native species with an invasive look-alike."],
 "background": "<p>Mark Catesby (1683 to 1749) published The Natural History of Carolina, Florida and the Bahama Islands in parts from 1729 to 1747; he relied on Native American guides and learned from enslaved Africans (for example, medicinal uses of snakeroot and the identification of fossil teeth at Stono Plantation), though he rarely named them. Anolis carolinensis, Danaus plexippus, Serenoa repens, Trametes versicolor and Sabal palmetto are common Florida examples. Fungal cell walls contain chitin. Checkpoint total: 45 points (Part A 10, Part B 12, Part C 10, Part D 13).</p>",
 "sources": ["Royal Society and Smithsonian Libraries, Mark Catesby's Natural History.", "University of Florida IFAS Extension, Florida plants and wildlife fact sheets.", "Florida Fish and Wildlife Conservation Commission, Species profiles.", "Woese, C. R., Kandler, O. and Wheelis, M. L. (1990), PNAS 87."]
}

PRINT = {
 "directions": "Mid-year review. Answer in complete sentences.",
 "items": [
  {"q":"List the seven characteristics of living things.","a":"Made of cells; use energy; grow and develop; respond to the environment; reproduce; maintain homeostasis; adapt over generations.","lines":3},
  {"q":"Write the eight levels of classification in order and a memory sentence.","a":"Domain, kingdom, phylum, class, order, family, genus, species; Dear King Philip Came Over For Good Soup.","lines":2},
  {"q":"Compare prokaryotes and eukaryotes and give an example of each.","a":"Prokaryotes have no nucleus (bacteria); eukaryotes have a nucleus (plants, animals, fungi, protists).","lines":2},
  {"q":"Write a two-couplet key for a pine needle, an oak leaf and a palm frond.","a":"Model: 1a. Needle-shaped ... pine; 1b. Flat ... go to 2; 2a. Fan-shaped with folds ... palm; 2b. Not fan-shaped ... oak.","lines":3},
  {"q":"Give two helpful and two harmful roles of microorganisms.","a":"Helpful: decomposing, oxygen, digestion, food, medicine. Harmful: strep throat, food poisoning, malaria, red tide.","lines":2},
  {"q":"Why does classification sometimes change?","a":"New evidence (microscopes, cell structure, DNA) shows new relationships, and science updates its ideas.","lines":2}]
}
