from geo import africa_map

SITES = africa_map([(-8.9, 31.9, 'Jebel Irhoud', 6, -4), (40.5, 11.1, 'Hadar: Lucy', 6, 0), (35.9, 5.4, 'Omo Kibish', 6, 4),
                    (35.4, -3.0, 'Olduvai Gorge', 6, 4), (36.0, 3.0, 'Lomekwi', -6, -2), (26.0, -28.8, 'Florisbad', 6, 4), (21.2, -34.4, 'Blombos Cave', -6, 14)],
                   'Where the evidence was found', rivers=False)

LAYERS = ('<svg viewBox="0 0 520 240" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Rock layers with fossils">'
  '<text x="260" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Reading the layers (law of superposition)</text>'
  '<rect x="30" y="30" width="300" height="40" fill="#d9c7a1"/><rect x="30" y="70" width="300" height="45" fill="#b99b6b"/><rect x="30" y="115" width="300" height="50" fill="#8f7450"/><rect x="30" y="165" width="300" height="55" fill="#6b5639"/>'
  '<text x="80" y="55" font-size="11">pottery shard</text><text x="210" y="98" font-size="11" fill="#fff">stone blade</text><text x="70" y="145" font-size="11" fill="#fff">hand axe</text><text x="190" y="198" font-size="11" fill="#fff">simple chopping tool</text>'
  '<path d="M360 40 V210" stroke="#0A1F3D" stroke-width="3"/><path d="M360 40 l-7 12 h14z" fill="#0A1F3D"/><text x="372" y="48" font-weight="bold">Youngest (top)</text><text x="372" y="214" font-weight="bold">Oldest (bottom)</text>'
  '<text x="372" y="112">Layers pile up</text><text x="372" y="128">over time, so deeper</text><text x="372" y="144">usually means older.</text></svg>')

def spread():
    rows = [("Africa: Homo sapiens appear", 300000, "#C9A84C"), ("Main dispersal out of Africa", 65000, "#0047BA"), ("South and East Asia", 55000, "#0047BA"), ("Australia", 50000, "#0047BA"), ("Europe", 45000, "#0047BA"), ("The Americas (debated)", 20000, "#DB2F30")]
    dates = ["about 300,000", "60,000 to 70,000", "60,000 to 45,000", "at least 50,000", "about 45,000", "15,000 to 23,000"]
    s = '<svg viewBox="0 0 560 250" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Timeline of human spread from Africa">'
    s += '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Spreading across the world (approximate years ago)</text>'
    sc = lambda y: 540 - y / 300000 * 330
    s += '<line x1="210" y1="220" x2="540" y2="220" stroke="#0A1F3D"/>'
    for t in (300000, 200000, 100000, 0):
        s += f'<line x1="{sc(t):.0f}" y1="216" x2="{sc(t):.0f}" y2="224" stroke="#0A1F3D"/><text x="{sc(t):.0f}" y="238" text-anchor="middle" font-size="10">{t:,}</text>'
    for i, (lab, y, c) in enumerate(rows):
        yy = 40 + i * 30
        s += f'<text x="200" y="{yy+5}" text-anchor="end">{lab}</text><line x1="{sc(y):.0f}" y1="{yy}" x2="540" y2="{yy}" stroke="{c}" stroke-width="10" opacity=".8"/><text x="{min(sc(y)+4, 470):.0f}" y="{yy-8}" font-size="10" fill="#5b6676">{dates[i]}</text>'
    s += '<text x="540" y="30" text-anchor="end" font-size="10" fill="#5b6676">today &#8594;</text></svg>'
    return s

LESSON = {
 "unit": "Unit 1: How We Know the Past",
 "title": "Human Beginnings in Africa",
 "subtitle": "Every person on Earth shares one origin story, and it begins in Africa.",
 "objectives": [
  "Explain how scientists date the deep past using fossils, layers of earth and dating methods.",
  "Describe key evidence of early human ancestors and the first stone tools in Africa.",
  "Explain why scientists now think Homo sapiens emerged across Africa about 300,000 years ago.",
  "Trace how people spread from Africa to every continent.",
  "Use genetic evidence to explain why all humans are one family, and why skin color varies."],
 "vocab": [
  ["fossil", "The preserved remains or traces of a living thing from long ago."],
  ["hominin", "Humans and our closest extinct relatives that walked upright."],
  ["Homo sapiens", "Our own species. The name means wise human."],
  ["stratigraphy", "The study of layers of rock and soil to learn about the past."],
  ["law of superposition", "In undisturbed layers, the deepest layers are the oldest."],
  ["migration", "The movement of people from one place to another to live."],
  ["DNA", "The material inside our cells that carries the instructions for how living things grow and work, passed from parents to children."],
  ["melanin", "The natural pigment that gives skin its color and protects it from the sun's ultraviolet (UV) rays."],
  ["symbolic thinking", "Using one thing to stand for another, such as patterns, art or beads, which shows complex minds."]],
 "reconnect": {
  "title": "Weeks 1 and 2: sources, time and maps",
  "intro": "Today you will use everything so far: evidence, timelines and maps of Africa.",
  "items": [
   {"t":"text","q":"Lake Turkana in Kenya is at about 3°N, 36°E. Which two hemispheres is it in?","a":[{"all":[["north"],["east"]]}],"show":"Northern and Eastern","pts":2,"why":"N is north of the equator; E is east of the prime meridian."},
   {"t":"num","q":"Africa is about 30.4 million km² and the United States about 9.8 million km². About how many times larger is Africa? Round to the nearest whole number.","a":3,"tol":0.5,"unit":"times","pts":3,"why":"30.4 ÷ 9.8 ≈ 3.1, so about 3."},
   {"t":"text","q":"Which map projection makes Africa look much smaller than it really is, compared with places near the poles?","a":["mercator","the mercator","mercator projection"],"show":"Mercator","pts":2,"why":"Mercator enlarges places far from the equator."},
   {"t":"text","q":"A stone tool dug up by archaeologists is a primary or secondary source?","a":["primary","^primary"],"pts":2,"why":"It was made and used at the time."},
   {"t":"num","q":"How many years passed from 4800 BCE (Nabta Playa) to 3000 BCE (Stonehenge)?","a":1800,"show":"1,800","unit":"years","pts":3,"why":"Both BCE: 4800 − 3000 = 1,800 years."},
   {"t":"text","q":"Why do historians corroborate evidence?","a":[{"all":[["confirm","check","true","accurate","bias","trust","agree","verify","reliable","sure"]]}],"show":"To confirm it with other sources so they can trust it","pts":2,"why":"Corroboration checks one source against others."}]},
 "hook": {
  "title": "Your Oldest Family Tree",
  "html": "<p>Ask anyone where their family comes from, and you might hear Haiti, Mexico, Ireland, Nigeria, Vietnam or Georgia. But follow any family tree back far enough, tens of thousands of years, and every branch leads to the same place: <b>Africa</b>.</p><p>How can scientists know something that happened before writing existed? They read evidence buried in the ground, in rock layers, in tools and bones, and even inside our own cells. This week you are the detective, using the tools from Weeks 1 and 2.</p><div class='callout'><b>Big idea:</b> Fossils, tools and DNA all point to the same conclusion: Homo sapiens, our species, began in Africa, and every person alive today is part of one human family.</div>"},
 "learn": [
  {"title": "How Do We Know How Old It Is?",
   "visual": LAYERS,
   "html": "<p><b>Stratigraphy:</b> layers of soil and rock build up over time like pages in a book. In undisturbed ground, the deepest layer is the oldest. This is the <b>law of superposition</b>.</p><p><b>Dating methods:</b> scientists measure natural clocks. Some kinds of atoms change into other kinds at a steady, known rate, like sand in an hourglass. Measuring how much has changed tells how old a rock or burned flint is. Radiocarbon dating works for material up to about 50,000 years old; other methods reach millions of years.</p><p><b>Corroboration:</b> scientists trust a date most when several methods agree.</p>",
   "checks": [
    {"t":"text","q":"In the diagram, which tool is the oldest? Type only its name.","a":[{"all":[["chopping","chopper"]],"none":["blade","point","arrow","pottery","not"]}],"show":"the simple chopping tool (deepest layer)","pts":2,"why":"It is in the deepest layer, so it is the oldest."},
    {"t":"text","q":"A pottery shard is found above a stone blade in undisturbed layers. Which object is older? Type only its name.","a":["blade","stone blade","the stone blade","^stone blade","^blade","^the blade"],"show":"the stone blade","pts":2,"why":"Lower layers are older, so the blade is older than the pottery above it."},
    {"t":"open","key":"disturbed","q":"Why do scientists say <b>undisturbed</b> layers? Describe something that could mix up the layers and make the rule unreliable.","min":15,"rows":3,"rubric":["Names a real disturbance (digging, animals burrowing, earthquakes, floods, burials)","Explains that it could put younger objects below older ones"],"model":"An animal digging a burrow or people digging a grave could push a newer object down into an older layer, so it would look older than it really is."}]},
  {"title": "Our Earliest Ancestors",
   "visual": SITES,
   "html": "<p>Long before our species existed, other hominins lived in Africa:</p><ul><li><b>Lucy</b>, found in 1974 at Hadar, Ethiopia, is a skeleton about <b>3.2 million years</b> old. Her species, <i>Australopithecus afarensis</i>, walked upright on two legs but still had a small brain. In Ethiopia she is also known as <b>Dinkinesh</b>, Amharic for \"you are marvelous.\"</li><li>The <b>oldest known stone tools</b>, about <b>3.3 million years</b> old, were found at <b>Lomekwi</b> near Lake Turkana in Kenya.</li><li><b>Olduvai Gorge</b> in Tanzania holds nearly two million years of tools and fossils in its layers.</li><li><i>Homo erectus</i>, about 1.9 million years ago, made hand axes and was among the first known hominins to spread out of Africa into Asia.</li></ul>",
   "checks": [
    {"t":"num","q":"About how many million years old is Lucy?","a":3.2,"tol":0.05,"unit":"million years","pts":2,"why":"Lucy is about 3.2 million years old."},
    {"t":"text","q":"What does Lucy's skeleton show about how her species moved?","a":[{"all":[["upright","two legs","bipedal","stood","stand"]]}],"show":"They walked upright on two legs.","pts":3,"why":"Her hip and leg bones show she walked upright."},
    {"t":"text","q":"In which country were the oldest known stone tools found?","a":["kenya"],"show":"Kenya","pts":2,"why":"At Lomekwi, near Lake Turkana, Kenya, about 3.3 million years old."},
    {"t":"text","q":"What does Lucy's Ethiopian name, Dinkinesh, mean?","a":[{"all":[["marvel","wonderful","amazing"]]}],"show":"you are marvelous","pts":2,"why":"Dinkinesh means \"you are marvelous\" in Amharic."}]},
  {"title": "The First Homo sapiens",
   "html": "<p>For years, the oldest known fossils of our own species came from <b>Omo Kibish, Ethiopia</b>, now dated to about <b>233,000 years</b> ago. Many scientists pictured our species beginning in one region of East Africa.</p><p>Then, in 2017, scientists announced new dates for fossils from <b>Jebel Irhoud, Morocco</b>, in North Africa: about <b>300,000 years</b> old. Together with a 260,000-year-old skull from <b>Florisbad, South Africa</b>, the evidence suggests our species emerged across <b>the whole African continent</b>, not in one spot.</p><p>Early Homo sapiens also showed <b>symbolic thinking</b>. At <b>Blombos Cave, South Africa</b>, people engraved patterns on red ochre and made shell beads more than 70,000 years ago, among the oldest known art and jewelry in the world.</p><div class='callout'>Notice what happened: new evidence changed the story. Good scientists and historians update their conclusions when the evidence demands it.</div>",
   "checks": [
    {"t":"num","q":"About how old are the Jebel Irhoud fossils, in years?","a":300000,"show":"300,000","unit":"years","pts":2,"why":"About 300,000 years old, the oldest known Homo sapiens fossils."},
    {"t":"num","q":"How many years older are the Jebel Irhoud fossils than the Omo Kibish fossils (233,000 years)?","a":67000,"show":"67,000","unit":"years","pts":3,"why":"300,000 − 233,000 = 67,000 years."},
    {"t":"text","q":"Jebel Irhoud is in Morocco, Omo Kibish in Ethiopia and Florisbad in South Africa. What does finding early Homo sapiens in all three places suggest?","a":[{"all":[["across","all over","whole","entire","many places","different parts","throughout","continent","pan"]]}],"show":"That Homo sapiens emerged across the whole African continent, not in just one region.","pts":3,"why":"The sites are thousands of kilometers apart, in the north, east and south of Africa."},
    {"t":"text","q":"What did people at Blombos Cave make that shows symbolic thinking?","a":[{"all":[["engrav","pattern","bead","ochre","art","shell","jewel"]]}],"show":"engraved ochre patterns and shell beads","pts":2,"why":"Patterns and beads stand for ideas, which shows complex, symbolic minds."}]},
  {"title": "Spreading Across the World, and One Human Family",
   "visual": spread(),
   "html": "<p>Groups of Homo sapiens began moving out of Africa in waves, with a major spread starting roughly 60,000 to 70,000 years ago. People reached Australia by at least 50,000 years ago, crossing open water by boat. They reached Europe about 45,000 years ago, and the Americas by at least 15,000 years ago; fossilized footprints at White Sands, New Mexico suggest people were there more than 20,000 years ago.</p><p><b>DNA evidence:</b> any two people on Earth share about <b>99.9 percent</b> of their DNA. Africa holds the greatest human genetic diversity in the world, because people have lived there the longest.</p><p><b>Skin color</b> is one small adaptation. Near the equator, where the sun's UV rays are strongest, darker skin with more <b>melanin</b> protects the body. Farther from the equator, lighter skin helps the body make vitamin D from weaker sunlight. Skin color tells you about your ancestors' sunlight, not about intelligence, ability or worth.</p>",
   "checks": [
    {"t":"num","q":"About what percent of their DNA do any two humans share?","a":99.9,"tol":0.05,"unit":"%","pts":2,"why":"About 99.9 percent."},
    {"t":"text","q":"Why does Africa have the greatest human genetic diversity?","a":[{"all":[["longest","longer","first","oldest","began","origin","started","most time","earliest"]]}],"show":"Because humans have lived there the longest","pts":3,"why":"Populations that have existed longer have had more time to develop genetic variety."},
    {"t":"text","q":"How did the first people reach Australia?","a":[{"all":[["boat","raft","canoe","sail","paddl","crossing open water","across the sea","across water"]],"none":["land bridge","walked"]}],"show":"By crossing open water in boats","pts":2,"why":"Australia was never connected to Asia by land during this time, so people needed boats."},
    {"t":"open","key":"skin","q":"Explain, in two or three sentences, why human skin color varies, and what skin color does and does not tell us about a person.","min":30,"rows":3,"rubric":["Explains UV protection near the equator (melanin)","Explains vitamin D and lighter skin far from the equator","States that skin color says nothing about intelligence, ability or worth"],"model":"Skin color varies because of sunlight. People whose ancestors lived near the equator have more melanin, which protects against strong UV rays, while lighter skin helped people farther from the equator make vitamin D from weaker sunlight. Skin color tells us about where our ancestors lived, not about anyone's intelligence, character or worth."}]}],
 "handson": {
  "title": "Dig Box Archaeology",
  "intro": "Become an archaeologist and read the layers yourself.",
  "materials": ["A clear plastic container or shoebox", "Three or four materials for layers: slightly damp sand or soil (so layers hold their shape), plus rice, oatmeal or birdseed", "Four small objects to bury as artifacts (a coin, a button, a pebble, a toy figure)", "A spoon, a paintbrush, a tray and a ruler", "A family member to build the dig box without showing you"],
  "steps": [
   "Ask a family member to build the dig box: put down one layer, bury an artifact in it away from the sides, then add the next layer and artifact, and so on. If the box is clear, wrap the sides in paper so the order is hidden. They should write down the order secretly.",
   "Challenge: ask your family member to secretly push one extra object down into an older layer, like an animal burrow.",
   "Dig slowly from the top with the spoon and brush. Do not dig straight down; remove one layer at a time.",
   "For each layer, record the material, its depth in centimeters, and the artifact you found.",
   "Use the law of superposition to put the artifacts in order from oldest to youngest.",
   "Compare your order with your family member's secret list."],
  "record": [
   {"t":"open","key":"dig","q":"Record each layer from top to bottom: material, depth in cm and artifact. Then list the artifacts from oldest to youngest.","min":40,"rows":6},
   {"t":"open","key":"dig2","q":"Did your order match the secret list? If something seemed out of place, what could explain it? How is your dig like the work at Olduvai Gorge?","min":30,"rows":4,"model":"Yes, my order matched, except the bottle cap was in a deeper layer than it should have been. My mom had pushed it down like a burrow, so the layers were disturbed there. Like scientists at Olduvai Gorge, I dug one layer at a time, measured the depth and used superposition to decide which objects were older."}]},
 "think": {
  "intro": "Use evidence from the lesson in every answer.",
  "items": [
   {"t":"open","key":"updated","q":"Before 2017, many textbooks said our species began about 200,000 years ago in East Africa. Explain how the Jebel Irhoud discovery changed that story, and why changing conclusions is a strength of science and history, not a weakness.","min":70,"rows":7,"rubric":["Explains the new date (300,000 years) and location (Morocco, North Africa)","Explains the new idea of a pan-African origin","Explains why updating conclusions with new evidence is a strength","Connects to corroboration or evidence from Week 1"],"model":"The Jebel Irhoud fossils in Morocco turned out to be about 300,000 years old, about 100,000 years older than the East African fossils textbooks used. Because early Homo sapiens fossils were also found in South Africa, scientists now think our species emerged across the whole continent. Changing the story is a strength, because it shows scientists follow the evidence instead of protecting old ideas, just as historians corroborate and correct sources."},
   {"t":"open","key":"onefamily","q":"Why does it matter that every human being shares African ancestors and 99.9 percent of their DNA? Explain what this evidence means for how people should think about race and about Africa's place in world history.","min":60,"rows":6,"rubric":["Uses the 99.9 percent DNA and African origin evidence","Explains that humans are one family and that races are not separate biological groups","Explains that Africa is central to world history, not on its edge","Clear claim and reasoning"],"model":"If all humans share African ancestors and 99.9 percent of our DNA, then we are one family, and the differences people use to divide each other are tiny. Africa is not on the edge of world history; it is where human history begins. Knowing this should make people question anyone who claims one group is naturally better than another."}]},
 "exit": [
  {"t":"open","key":"exitlayers","q":"In undisturbed layers, where are the oldest objects found, and why? Name one thing that could disturb the layers.","min":15,"rows":2,"rubric":["Bottom","Layers pile up over time","Names a real disturbance (burrowing animals, digging, floods, earthquakes)"],"model":"At the bottom, because layers pile up on top of each other over time. A burrowing animal or a flood could mix the layers."},
  {"t":"text","q":"In what country were Lucy's bones found?","a":["ethiopia"],"show":"Ethiopia","pts":2,"why":"At Hadar, Ethiopia, in 1974."},
  {"t":"text","q":"Where were the oldest known Homo sapiens fossils, about 300,000 years old, found? Name the site or the country.","a":["jebel irhoud","morocco","jebel irhoud morocco"],"show":"Jebel Irhoud, Morocco","pts":2,"why":"Jebel Irhoud, Morocco."},
  {"t":"num","q":"How many years passed between the oldest stone tools (3,300,000 years ago) and Lucy (3,200,000 years ago)?","a":100000,"show":"100,000","unit":"years","pts":3,"why":"3,300,000 − 3,200,000 = 100,000 years. The tools are older than Lucy."},
  {"t":"text","q":"What pigment protects skin from the sun's UV rays?","a":["melanin"],"pts":2,"why":"Melanin gives skin its color and protects it."},
  {"t":"text","q":"Name one piece of evidence that early Homo sapiens had symbolic thinking.","a":[{"all":[["engrav","pattern","bead","ochre","art","shell","jewel","blombos"]]}],"show":"engraved ochre or shell beads from Blombos Cave","pts":3,"why":"Patterns and beads represent ideas."}],
 "next": "Week 4: farming, villages and the first towns. You will discover that people invented farming in at least seven places around the world, on their own."
}

TEACHER = {
 "standards": [
  "SS.6.W.2.1: Compare the lifestyles of hunter-gatherers with those of settlers of early agricultural communities (preview for Week 4; today establishes the hunter-gatherer world).",
  "SS.6.W.1.4: Describe the methods of historical inquiry and how history relates to the other social sciences.",
  "SS.6.W.1.5: Describe the roles of historians and recognize varying historical interpretations (historiography).",
  "SS.6.G.4.2: Use maps to trace significant migrations, and analyze their results.",
  "C3 Framework D2.His.16.6-8: Organize applicable evidence into a coherent argument about the past."],
 "materials": ["The interactive lesson", "A world map or globe", "Dig box materials (prepared by a family member before the after-class activity)", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Reconnect questions. Have the student find Lake Turkana and Morocco on a real map of Africa."],
  [6, "Hook", "Ask the student where their own family comes from. Then reveal that every family tree, followed far enough, leads to Africa."],
  [10, "Dating the past", "Use the layer diagram. Ask what could disturb layers. Explain natural clocks with the hourglass comparison."],
  [10, "Earliest ancestors", "Locate each site on the map. Discuss Lucy and the meaning of Dinkinesh, and the 3.3-million-year-old Lomekwi tools."],
  [12, "First Homo sapiens", "Compare the old East Africa story with the new pan-African evidence. Emphasize that evidence changed the conclusion."],
  [12, "Spreading out and one family", "Use the spread timeline. Discuss the 99.9 percent DNA figure and the science of skin color. Make clear that skin color is about sunlight, not ability."],
  [4, "Assign", "Assign the dig box, Think Deeper and the Exit Check."]],
 "key_questions": ["How can we know about people who left no writing?", "What could make a layer lie about its age?", "Why did the Jebel Irhoud dates change the story?", "If we share 99.9 percent of our DNA, what does that say about the idea of separate races?", "Why might older textbooks have ignored or shrunk Africa's role?"],
 "misconceptions": ["Thinking humans evolved from chimpanzees. Humans and chimpanzees share a common ancestor that lived millions of years ago.", "Thinking Lucy was a human. Her species was an earlier hominin.", "Thinking skin color reflects ability or that races are separate biological groups.", "Thinking people moved out of Africa in a single trip; it happened in waves over tens of thousands of years."],
 "support": ["Give a simple timeline card with four dates: 3.3 million (tools), 3.2 million (Lucy), 300,000 (Homo sapiens), 65,000 (leaving Africa).", "Use the Africa map to color-code sites by age."],
 "challenge": ["Research the Leakey family's discoveries at Olduvai Gorge and Lake Turkana and present one.", "Investigate the debate over the White Sands footprints and explain what evidence each side uses."],
 "background": "<p>Key facts: Lucy (A. afarensis, AL 288-1) was found at Hadar, Ethiopia, in 1974 and dates to about 3.2 million years ago. The Lomekwi 3 tools (Kenya, published 2015) date to about 3.3 million years ago. Jebel Irhoud (Morocco) Homo sapiens fossils were dated to about 300,000 years ago (Hublin et al., Nature, 2017); Florisbad (South Africa) to about 260,000 years; Omo Kibish (Ethiopia) to about 233,000 years (revised in 2022). Blombos Cave engraved ochre dates to about 73,000 to 77,000 years. Dates for reaching Australia (50,000 to 65,000 years) and the Americas (at least 15,000 years; White Sands footprints about 21,000 to 23,000 years) are still being debated, so the lesson gives conservative figures. Any two humans share about 99.9 percent of their DNA.</p>",
 "sources": ["Hublin, J.-J. et al. (2017). New fossils from Jebel Irhoud, Morocco and the pan-African origin of Homo sapiens. Nature 546: 289 to 292.", "Harmand, S. et al. (2015). 3.3-million-year-old stone tools from Lomekwi 3, West Turkana, Kenya. Nature 521: 310 to 315.", "Smithsonian National Museum of Natural History: Human Origins Program.", "National Human Genome Research Institute: Genetics vs. genomics and human genetic variation."]
}

PRINT = {
 "directions": "Answer in complete sentences. Show any math.",
 "items": [
  {"q":"Explain the law of superposition and one thing that could make it unreliable.","a":"In undisturbed layers the deepest is oldest; digging, burrowing animals, floods or earthquakes can mix layers.","lines":3},
  {"q":"Put in order from oldest to youngest: Homo sapiens at Jebel Irhoud; Lomekwi stone tools; Lucy; Blombos Cave beads.","a":"Lomekwi tools (3.3 million), Lucy (3.2 million), Jebel Irhoud (300,000), Blombos beads (over 70,000)","lines":2},
  {"q":"How many years older is Lucy than the Jebel Irhoud fossils? (3,200,000 and 300,000 years) Show your work.","a":"3,200,000 − 300,000 = 2,900,000 years","lines":2},
  {"q":"Why do scientists now think Homo sapiens emerged across all of Africa, not in one region?","a":"Early Homo sapiens fossils have been found far apart, in Morocco, Ethiopia and South Africa.","lines":3},
  {"q":"Explain why human skin color varies.","a":"More melanin protects against strong UV near the equator; lighter skin helps make vitamin D where sunlight is weaker.","lines":3},
  {"q":"What does the fact that all humans share about 99.9 percent of their DNA tell us?","a":"All humans are one closely related family; the differences between groups are very small.","lines":2}]
}
