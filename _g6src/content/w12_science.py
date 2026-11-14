LEVELS = ('<svg viewBox="0 0 660 330" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Classification levels for the American alligator">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Eight levels of classification: the American alligator</text>'
  + ''.join(f'<rect x="{30+i*18}" y="{34+i*34}" width="{600-i*36}" height="30" rx="6" fill="{c}"/><text x="{44+i*18}" y="{54+i*34}" fill="#fff" font-weight="bold">{lv}</text><text x="{616-i*18}" y="{54+i*34}" text-anchor="end" fill="#fff" font-style="{'italic' if lv in ('Genus','Species') else 'normal'}">{nm}</text>'
            for i, (lv, nm, c) in enumerate([("Domain", "Eukarya: cells with a nucleus", "#0A1F3D"), ("Kingdom", "Animalia: animals", "#173a6b"), ("Phylum", "Chordata: animals with a nerve cord", "#0047BA"),
                                              ("Class", "Reptilia: reptiles", "#2a6fc9"), ("Order", "Crocodilia: crocodilians", "#3d9a2f"), ("Family", "Alligatoridae: alligators and caimans", "#8a6d1f"),
                                              ("Genus", "Alligator", "#C9A84C"), ("Species", "Alligator mississippiensis", "#DB2F30")])) +
  '<text x="330" y="318" text-anchor="middle" font-size="11" fill="#5b6676">Each level down holds fewer kinds of organisms that share more traits. Memory trick: Dear King Philip Came Over For Good Soup.</text></svg>')

KINGDOMS = ('<svg viewBox="0 0 660 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Three domains and six kingdoms">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Three domains and six kingdoms</text>'
  '<rect x="20" y="36" width="140" height="34" rx="6" fill="#6b3fa0"/><text x="90" y="58" text-anchor="middle" fill="#fff" font-weight="bold">Domain Bacteria</text>'
  '<rect x="175" y="36" width="140" height="34" rx="6" fill="#8a5a33"/><text x="245" y="58" text-anchor="middle" fill="#fff" font-weight="bold">Domain Archaea</text>'
  '<rect x="330" y="36" width="310" height="34" rx="6" fill="#0A1F3D"/><text x="485" y="58" text-anchor="middle" fill="#fff" font-weight="bold">Domain Eukarya (cells with a nucleus)</text>'
  + ''.join(f'<rect x="{x}" y="86" width="{w}" height="96" rx="8" fill="#fff" stroke="{c}" stroke-width="3"/><text x="{x+w/2}" y="108" text-anchor="middle" font-weight="bold" fill="{c}">{t}</text>'
            + ''.join(f'<text x="{x+w/2}" y="{126+j*15}" text-anchor="middle" font-size="11">{line}</text>' for j, line in enumerate(lines))
            for x, w, c, t, lines in [(20, 140, "#6b3fa0", "Bacteria", ["one cell, no nucleus", "everywhere: soil,", "yogurt, your gut"]),
                                      (175, 140, "#8a5a33", "Archaea", ["one cell, no nucleus", "many live in extreme", "places: hot springs"]),
                                      (330, 70, "#C9A84C", "Protists", ["mostly", "one cell:", "amoeba"]),
                                      (410, 70, "#a5552a", "Fungi", ["absorb", "food:", "mushrooms"]),
                                      (490, 70, "#3d9a2f", "Plants", ["make", "food by", "photosyn."]),
                                      (570, 70, "#DB2F30", "Animals", ["eat other", "organisms;", "most move"])]) +
  '<text x="330" y="204" text-anchor="middle" font-size="11">Bacteria and Archaea are both domains and kingdoms. Eukarya holds four kingdoms.</text>'
  '<text x="330" y="220" text-anchor="middle" font-size="10" fill="#5b6676">Viruses are not in any kingdom, because they are not made of cells (Week 11).</text></svg>')

NAMES = ('<svg viewBox="0 0 660 200" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="One animal with many common names">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Many common names, one scientific name</text>'
  '<g transform="translate(250,40)"><path d="M10 80 q30 -40 90 -30 q40 5 60 -10 l12 -12 l4 14 q10 6 6 18 q-8 6 -20 4 l-10 30 l8 34 h-10 l-12 -30 l-50 2 l-10 30 h-10 l2 -34 q-30 0 -60 -16z" fill="#c9a26b" stroke="#8a6d1f"/><path d="M10 80 q-14 10 -6 40" fill="none" stroke="#8a6d1f" stroke-width="4"/></g>'
  + ''.join(f'<text x="{x}" y="{y}" font-size="13" fill="#0047BA" text-anchor="middle">{t}</text>' for x, y, t in [(110, 70, "Florida panther"), (120, 120, "cougar"), (100, 170, "mountain lion"), (560, 70, "puma"), (570, 120, "catamount"), (560, 170, "león de montaña")]) +
  '<rect x="235" y="176" width="190" height="22" rx="4" fill="#0A1F3D"/><text x="330" y="192" text-anchor="middle" fill="#fff" font-style="italic" font-weight="bold">Puma concolor</text></svg>')

LESSON = {
 "unit": "Unit 3: The Diversity of Life",
 "title": "Classification and Scientific Names",
 "subtitle": "Scientists have named about two million species, and millions more are still unknown. Classification sorts them into groups, and scientific names give each one a single name that scientists everywhere understand.",
 "objectives": [
  "Explain why scientists classify organisms and how classification groups organisms by shared traits.",
  "Name the eight levels of classification in order.",
  "Write scientific names correctly using binomial nomenclature.",
  "Describe the three domains and six kingdoms and give an example from each kingdom.",
  "Explain how classification changes with new evidence, and evaluate Linnaeus's legacy fairly."],
 "vocab": [
  ["classification", "Sorting organisms into groups based on shared traits."],
  ["taxonomy", "The science of naming, describing and classifying organisms."],
  ["species", "A group of organisms that can breed with each other and produce offspring that can also reproduce."],
  ["genus", "A group of closely related species (plural: genera)."],
  ["binomial nomenclature", "The two-name system for naming species: genus plus species, such as Homo sapiens."],
  ["domain", "The broadest level of classification: Bacteria, Archaea or Eukarya."],
  ["kingdom", "The level below domain, such as Plants, Animals or Fungi."]],
 "reconnect": {
  "title": "Week 11: Characteristics of living things",
  "intro": "You can only classify things that are alive. Review what that means.",
  "items": [
   {"t":"open","key":"rc_seven","q":"List at least five of the seven characteristics of living things.","min":12,"rows":2,"rubric":["Five or more of: made of cells, organized, use energy, grow and develop, respond, reproduce, homeostasis"],"model":"Made of cells, organized, use energy, grow and develop, respond to stimuli, reproduce and maintain homeostasis."},
   {"t":"order","q":"Week 11: put the levels of organization in order from smallest to largest.","items":["cell","tissue","organ","organ system","organism"],"pts":2,"why":"Today's levels of classification are different: they sort whole organisms into groups."},
   {"t":"open","key":"rc_virus","q":"Why are viruses usually not classified in any kingdom of living things? Use Week 11.","min":12,"rows":2,"rubric":["Not made of cells; cannot use energy or reproduce on their own, so most biologists do not call them living"],"model":"Viruses are not made of cells and cannot use energy or reproduce on their own, so most biologists do not count them as living organisms."},
   {"t":"text","q":"In the yeast test, yeast released a gas that filled the balloon. Which gas?","a":[{"all":[["carbon dioxide","co2"]],"none":["not"]}],"show":"carbon dioxide","pts":2,"why":"Carbon dioxide. Yeast is a fungus; today you will see which kingdom it belongs to."}]},
 "hook": {
  "title": "What's a Gopher?",
  "html": "<p>Ask someone in Florida what a \"gopher\" is, and they may describe a large tortoise that digs deep burrows in sandy soil. Ask someone in Kansas, and they will describe a small furry rodent. Same word, completely different animals.</p><p>The Florida panther has the opposite problem: the same animal is called a cougar, mountain lion, puma or catamount, depending on where you live, and león de montaña in Spanish. Imagine scientists in Brazil, Japan and Florida trying to share research with all those names.</p><p>Scientists solved this with <b>scientific names</b>. The gopher tortoise is <i>Gopherus polyphemus</i>, and the Florida panther is <i>Puma concolor</i>, the same species as every cougar and mountain lion in the Americas. Every scientist on Earth uses the same names.</p><div class='callout'><b>Big question:</b> How do scientists organize and name millions of kinds of living things?</div>"},
 "learn": [
  {"title": "Why and How We Classify",
   "visual": LEVELS,
   "html": "<p>Scientists have named about two million species, and estimates of how many exist range from several million to many more. To make sense of that diversity, scientists <b>classify</b>: they sort organisms into groups based on shared traits, the way a library sorts books or a grocery store sorts food into aisles.</p><p>Modern classification has eight main levels, from the broadest to the most specific: <b>domain, kingdom, phylum, class, order, family, genus, species</b>. Each level contains fewer kinds of organisms that share more traits. All animals are in kingdom Animalia, but only alligators and caimans are in family Alligatoridae.</p><p>Today, scientists group organisms by how closely related they are, using body structures, development and especially DNA. Two species in the same genus share a recent common ancestor, like cousins in a family tree.</p>",
   "checks": [
    {"t":"order","q":"Put the eight levels of classification in order from broadest to most specific.","items":["domain","kingdom","phylum","class","order","family","genus","species"],"pts":4,"why":"Dear King Philip Came Over For Good Soup."},
    {"t":"open","key":"share","q":"A lion (Panthera leo) and a tiger (Panthera tigris) are in the same genus. A lion and a housecat (Felis catus) are in the same family but different genera. Which two are most closely related, and how do you know?","min":20,"rows":2,"rubric":["Lion and tiger","They share the most specific level (the same genus), so they share more traits and a more recent common ancestor"],"model":"The lion and the tiger, because they are in the same genus, Panthera, which is more specific than family. Sharing a more specific group means they are more closely related."},
    {"t":"open","key":"library","q":"Compare classification to how a grocery store organizes food. Match at least three store levels to classification levels.","min":25,"rows":3,"rubric":["A sensible analogy (store → department → aisle → shelf → item)","Explains that each level gets more specific"],"model":"The whole store is like a domain, the food department like a kingdom, the cereal aisle like a class, the oat cereals like a genus and one exact box of Oat Rings like a species. Each step gets more specific, with fewer items that are more alike."}]},
  {"title": "Binomial Nomenclature",
   "visual": NAMES,
   "html": "<p>In the 1750s, Swedish scientist <b>Carl Linnaeus</b> made popular a two-name system called <b>binomial nomenclature</b> (<i>bi</i> = two, <i>nomen</i> = name). Every species gets a name with two parts:</p><ul><li>The <b>genus</b> name, capitalized: <i>Alligator</i>.</li><li>The <b>species</b> name, all lowercase: <i>mississippiensis</i>.</li></ul><p>The whole name is written in <i>italics</i> (or underlined by hand): <i>Alligator mississippiensis</i>. After the first use, the genus can be shortened to its first letter: <i>A. mississippiensis</i>.</p><p>Scientific names are usually Latin or Greek, and they often describe the organism or honor a person or place. <i>Homo sapiens</i> means \"wise human.\" <i>Sabal palmetto</i> is Florida's state tree, the cabbage palm. <i>Quercus virginiana</i> is the southern live oak.</p>",
   "checks": [
    {"t":"open","key":"fixname","q":"Each scientific name is written wrong. Rewrite them correctly (describe the italics in words if you cannot type them) and explain the rules: (1) gopherus Polyphemus (2) Homo Sapiens (3) felis catus","min":20,"rows":3,"rubric":["Gopherus polyphemus; Homo sapiens; Felis catus","Rules: genus capitalized, species lowercase, whole name in italics or underlined"],"model":"Gopherus polyphemus, Homo sapiens and Felis catus, each in italics. The genus is always capitalized, the species name is always lowercase, and the whole name is italicized or underlined."},
    {"t":"text","q":"In the name Quercus virginiana, which word is the genus?","a":[{"all":[["quercus"]],"none":["virginiana","not"]}],"show":"Quercus","pts":2,"why":"The capitalized first word is the genus."},
    {"t":"open","key":"whysci","q":"Using the panther and the gopher, give two reasons scientific names are better than common names for scientists.","min":25,"rows":3,"rubric":["One organism can have many common names (panther, cougar, puma)","One common name can mean different organisms (gopher)","Scientific names are the same worldwide in every language"],"model":"One animal can have many common names, like panther, cougar and puma, while one common name like gopher can mean two different animals. A scientific name like Puma concolor is used by scientists everywhere, in every language, so there is no confusion."}]},
  {"title": "Domains and Kingdoms",
   "visual": KINGDOMS,
   "html": "<p>In 1977, American microbiologist <b>Carl Woese</b> studied the genes of tiny single-celled organisms and discovered that some \"bacteria\" were as different from bacteria as bacteria are from people. He named them <b>Archaea</b>. His work led scientists to recognize three <b>domains</b>: Bacteria, Archaea and Eukarya.</p><p>Many U.S. textbooks then divide life into six <b>kingdoms</b>:</p><ul><li><b>Bacteria</b> and <b>Archaea</b>: single cells with no nucleus.</li><li><b>Protists</b>: mostly single-celled organisms with a nucleus, like amoebas and some algae.</li><li><b>Fungi</b>: mushrooms, molds and yeast. They absorb food from their surroundings.</li><li><b>Plants</b>: many-celled organisms that make food by photosynthesis (Week 8).</li><li><b>Animals</b>: many-celled organisms that eat other organisms.</li></ul><p>Classification changes with evidence. Fungi were once classified as plants because they do not move and grow from the ground. But fungi cannot photosynthesize, their cell walls are made of a different material, and DNA shows they are more closely related to animals than to plants.</p>",
   "checks": [
    {"t":"blanks","q":"Name the kingdom for each organism.","sent":"The yeast from Week 11: ___ &nbsp; A Spanish moss plant: ___ &nbsp; An amoeba: ___","blanks":[[{"all":[["fungi","fungus"]],"none":["not"]}],[{"all":[["plant"]],"none":["not"]}],[{"all":[["protist"]],"none":["not"]}]],"show":"Fungi; Plants; Protists","pts":3,"why":"Yeast is a fungus; Spanish moss is a flowering plant (not a true moss); an amoeba is a single-celled protist."},
    {"t":"open","key":"fungi","q":"Explain why fungi are no longer classified as plants. Give two pieces of evidence.","min":25,"rows":3,"rubric":["Fungi cannot photosynthesize; they absorb food","Different cell wall material; DNA shows they are more closely related to animals"],"model":"Fungi cannot make their own food by photosynthesis; they absorb it. Their cell walls are made of a different material, and DNA evidence shows they are more closely related to animals than to plants."},
    {"t":"text","q":"Which domain includes all organisms whose cells have a nucleus?","a":[{"all":[["eukarya","eukaryote","eukaryota"]],"none":["not"]}],"show":"Eukarya","pts":2,"why":"Eukarya (eu = true, karyon = nucleus)."}]},
  {"title": "People Behind the Names",
   "html": "<p>Linnaeus's naming system is still used today, but his work also had a dark side. In his book, he divided humans into four \"varieties\" by continent and described them with prejudiced traits, ranking Europeans above Africans and others. Those ideas helped later writers justify racism and slavery, the same kind of thinking you saw in Week 7. Modern genetics shows that humans are one species, and that there is more genetic variation within any one population than between populations. Scientists today reject the idea of separate human races as biological categories.</p><p>Classification also depends on explorers and collectors from many backgrounds. <b>Ynés Mexía</b> (1870 to 1938), a Mexican American botanist, began studying plants in her fifties. She traveled through Mexico, South America and Alaska, collecting about 145,000 plant specimens. Around 500 of them were species new to science, and about 50 are named in her honor.</p><p>Long before Linnaeus, Indigenous peoples around the world had their own detailed systems for naming and grouping plants and animals, based on generations of observation. Scientists today increasingly learn from that knowledge.</p>",
   "checks": [
    {"t":"open","key":"linnaeus","q":"How should we judge Linnaeus? Explain one way his work helped science and one way it caused harm, and say how scientists today have corrected the harm.","min":35,"rows":4,"rubric":["Helped: binomial nomenclature and an organized system still used today","Harm: ranked human \"varieties\" with prejudiced traits, used to justify racism and slavery","Correction: genetics shows humans are one species with more variation within groups than between; race is not a biological category"],"model":"Linnaeus helped science by creating the two-name system and an organized way to classify life that we still use. But he also ranked humans into \"varieties\" with prejudiced traits, which was used to justify racism and slavery. Today genetics shows that all humans are one species, with more variation within groups than between them, so scientists reject those ideas."},
    {"t":"open","key":"mexia","q":"What does Ynés Mexía's story show about who can contribute to science?","min":20,"rows":2,"rubric":["People of any background and age can make major contributions; she began in her fifties and discovered about 500 new species"],"model":"It shows that people of any background and age can make major discoveries. She started studying plants in her fifties and still found about 500 species new to science."}]}],
 "handson": {
  "title": "Classify Your Collection",
  "intro": "Build your own classification system for a collection at home, then start a leaf collection you will use next week.",
  "materials": ["15 to 20 small objects of one type: buttons, dry pasta shapes, screws and bolts, or shells", "Index cards or sticky notes", "A large table or floor space", "A paper bag for leaves", "Optional: a field guide or plant identification app"],
  "steps": [
   "Spread your objects out. Find one trait that splits them into two or three big groups (your kingdoms). Label each group with a card.",
   "Split each group again by another trait, and again, until each final group holds only one kind of object. Use at least four levels.",
   "Give each final object a two-part \"scientific\" name in the binomial style, with a genus name for the group and a species name that describes it (for example, Buttonus quadriholus for a four-hole button).",
   "Take a walk with an adult and collect 6 to 8 different leaves that have already fallen (do not pick from plants you can't identify, and avoid poison ivy). Press them flat inside a heavy book for next week."],
  "record": [
   {"t":"open","key":"mysystem","q":"Draw or describe your classification system: the trait used at each level and the groups it created, down to at least four levels.","min":40,"rows":6,"rubric":["At least four levels","A clear trait at each level","Every object ends in its own group"],"model":"Level 1: metal or plastic buttons. Level 2 (plastic): round or shaped. Level 3 (round): two holes or four holes. Level 4 (four holes): white or colored. Each final group has one kind of button."},
   {"t":"open","key":"mynames","q":"List three of your binomial names, explain what each part means, and check that you followed the writing rules.","min":30,"rows":3,"rubric":["Three names in binomial form","Genus capitalized, species lowercase, italic or underlined","Meanings explained"],"model":"Buttonus quadriholus (four-hole button), Buttonus biholus (two-hole button) and Metallicus starrus (a star-shaped metal button). The genus groups similar buttons, and the species describes the exact kind. Genus capitalized, species lowercase, underlined."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"whale","q":"Whales live in the ocean and are shaped like fish, but scientists classify them as mammals, not fish. Explain why, using what you know about how scientists classify organisms.","min":70,"rows":6,"rubric":["Classification is based on shared traits and relatedness, not just where something lives or its shape","Whales breathe air with lungs, are warm-blooded, give birth to live young and feed them milk, have hair at some stage (mammal traits)","DNA and skeletons show whales are related to land mammals"],"model":"Scientists classify organisms by shared traits and how closely they are related, not by where they live or their shape. Whales breathe air with lungs, are warm-blooded, give birth to live young and feed them milk, which are mammal traits. Their skeletons and DNA also show they are related to land mammals. Their fish-like shape is just an adaptation to life in water."},
   {"t":"open","key":"newspecies","q":"Imagine you discover a new species of frog in a Florida spring. Explain what scientists would do to classify it and name it, and write a possible scientific name with a reason for each part.","min":70,"rows":6,"rubric":["Compare its traits and DNA with known frogs to place it in a genus and family","Write a species description and publish it","A properly written binomial name with reasons (describing a trait, place or person)"],"model":"Scientists would compare its body, behavior and DNA with known frogs to find its closest relatives, which would tell them its family and genus. Then they would describe the new species and publish it so other scientists can check it. If it belonged to the genus Lithobates, I might name it Lithobates fontinalis, from the Latin for \"of a spring,\" because it lives in a spring."}]},
 "exit": [
  {"t":"order","q":"Order these levels from broadest to most specific: genus, kingdom, family, species.","items":["kingdom","family","genus","species"],"pts":2,"why":"Kingdom, family, genus, species."},
  {"t":"open","key":"exit_rules","q":"Write the scientific name for humans correctly and state the two capitalization rules.","min":10,"rows":2,"rubric":["Homo sapiens (italic/underlined)","Genus capitalized; species lowercase"],"model":"Homo sapiens, in italics. The genus is capitalized and the species name is lowercase."},
  {"t":"text","q":"Which kingdom includes mushrooms, molds and yeast?","a":[{"all":[["fungi","fungus"]],"none":["not"]}],"show":"Fungi","pts":2,"why":"Fungi."},
  {"t":"open","key":"exit_change","q":"Give one example of how classification changed because of new evidence.","min":10,"rows":2,"rubric":["Fungi moved out of plants; Archaea separated from Bacteria (Woese); other accurate example"],"model":"Fungi used to be classified as plants, but evidence like DNA moved them into their own kingdom."}],
 "next": "Week 13: dichotomous keys, the tool scientists use to identify an unknown organism step by step."
}

TEACHER = {
 "standards": [
  "SC.6.L.15.1: Analyze and describe how and why organisms are classified according to shared characteristics with emphasis on the Linnaean system combined with the concept of Domains.",
  "SC.6.N.2.2: Explain that scientific knowledge is durable because it is open to change as new evidence or interpretations are encountered.",
  "SC.6.N.2.3: Recognize that scientists who make contributions to scientific knowledge come from all kinds of backgrounds and possess varied talents, interests, and goals.",
  "SC.6.L.14.1: Describe and identify patterns in the hierarchical organization of organisms from atoms to molecules to cells to tissues to organs to organ systems to organisms (reconnect).",
  "NGSS MS-LS4-2 (preview): Apply scientific ideas to construct an explanation for the anatomical similarities and differences among modern organisms."],
 "materials": ["The interactive lesson", "15 to 20 buttons, pasta shapes, bolts or shells", "Index cards", "A paper bag and a heavy book for pressing leaves", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 11 Reconnect questions."],
  [5, "Hook", "Ask what a gopher is. Show the many names for one panther."],
  [10, "Why classify", "Build the eight levels for the alligator. Compare lion, tiger and housecat."],
  [10, "Scientific names", "Fix the incorrectly written names. Discuss the meanings of Florida species names."],
  [10, "Domains and kingdoms", "Sort example organisms into kingdoms. Discuss why fungi moved out of plants."],
  [10, "People behind the names", "Discuss Linnaeus fairly: contributions and harm. Tell Ynés Mexía's story."],
  [9, "Assign", "Start the classification sort together; assign the leaf walk, Think Deeper and the Exit Check."]],
 "key_questions": ["What traits do these organisms share?", "Which level is more specific?", "Why use a scientific name instead of a common name?", "What evidence changed the classification?"],
 "misconceptions": ["Organisms are classified by where they live (whales as fish).", "Fungi are plants.", "Scientific names are capitalized like titles (both words capitalized).", "Human races are biological subspecies.", "Classification never changes."],
 "support": ["Give the memory sentence on a card: Dear King Philip Came Over For Good Soup.", "Provide a partly completed classification tree for the alligator.", "Sort picture cards of organisms into kingdoms."],
 "challenge": ["Look up the full classification of the Florida manatee or the gopher tortoise.", "Research a species named after a Black or Indigenous scientist or explorer and explain the honor."],
 "background": "<p>About 2.1 million species have been described; total estimates vary widely. Linnaeus applied binomial names consistently in Species Plantarum (1753) for plants and the 10th edition of Systema Naturae (1758) for animals; in Systema Naturae he divided Homo sapiens into four continental varieties with prejudiced descriptions. Carl Woese identified Archaea in 1977 using ribosomal RNA, and with colleagues proposed the three-domain system in 1990. U.S. textbooks often use six kingdoms (Bacteria/Eubacteria, Archaea/Archaebacteria, Protista, Fungi, Plantae, Animalia); kingdom schemes vary internationally. Ynés Mexía (1870 to 1938) collected about 145,000 to 150,000 specimens; about 500 new species and roughly 50 species named for her are commonly cited. The Florida panther is Puma concolor (subspecies designation revised in recent taxonomy). Spanish moss (Tillandsia usneoides) is a bromeliad, a flowering plant. Verify SC.6.L.15.1 wording on CPALMS.</p>",
 "sources": ["Woese, C. R., Kandler, O. and Wheelis, M. L. (1990), Towards a natural system of organisms: proposal for the domains Archaea, Bacteria, and Eucarya, PNAS 87.", "Smithsonian National Museum of Natural History, Ynés Mexía.", "Florida Fish and Wildlife Conservation Commission, Gopher Tortoise and Florida Panther.", "Natural History Museum (London), Linnaeus and taxonomy.", "CPALMS, SC.6.L.15.1."]
}

PRINT = {
 "directions": "Use complete sentences.",
 "items": [
  {"q":"List the eight levels of classification from broadest to most specific.","a":"domain, kingdom, phylum, class, order, family, genus, species","lines":1},
  {"q":"Write the scientific name of the American alligator correctly and label its parts.","a":"Alligator mississippiensis: genus Alligator, species mississippiensis (italic).","lines":2},
  {"q":"Why do scientists use scientific names?","a":"One name per species worldwide; avoids confusion from many or shared common names.","lines":2},
  {"q":"Name the three domains.","a":"Bacteria, Archaea, Eukarya","lines":1},
  {"q":"Name the kingdom of a mushroom, an oak tree and an amoeba.","a":"Fungi, Plants, Protists","lines":1},
  {"q":"Why are whales classified as mammals, not fish?","a":"They breathe air, are warm-blooded, give live birth and make milk; DNA links them to mammals.","lines":2}]
}
