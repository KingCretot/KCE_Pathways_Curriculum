PUNNETT = ('<svg viewBox="0 0 640 232" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Punnett square for two parents with genotype Tt for tall pea plants: TT, Tt, Tt, tt; three tall to one short">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Unit 6 in one picture: a Tt × Tt pea plant cross</text>'
  '<text x="170" y="50" text-anchor="middle" fill="#0047BA" font-weight="bold">T</text><text x="250" y="50" text-anchor="middle" fill="#0047BA" font-weight="bold">t</text>'
  '<text x="110" y="100" text-anchor="middle" fill="#DB2F30" font-weight="bold">T</text><text x="110" y="180" text-anchor="middle" fill="#DB2F30" font-weight="bold">t</text>'
  + ''.join(f'<rect x="{130+c*80}" y="{60+r*80}" width="80" height="80" fill="{"#f4ecd6" if (r,c)!=(1,1) else "#e0e8f5"}" stroke="#0A1F3D" stroke-width="2"/><text x="{170+c*80}" y="{106+r*80}" text-anchor="middle" fill="#0A1F3D" font-size="18" font-weight="bold">{g}</text>'
            for (r, c), g in zip([(0,0),(0,1),(1,0),(1,1)], ["TT", "Tt", "Tt", "tt"])) +
  '<text x="460" y="80" fill="#0A1F3D" font-weight="bold">T = tall (dominant)</text><text x="460" y="100" fill="#0A1F3D" font-weight="bold">t = short (recessive)</text>'
  '<text x="460" y="134" fill="#0A1F3D">3 of 4 boxes: tall</text><text x="460" y="154" fill="#0A1F3D">1 of 4 boxes: short</text><text x="460" y="186" fill="#5b6676" font-size="11">Each box is a 25% chance,</text><text x="460" y="202" fill="#5b6676" font-size="11">not a promise.</text></svg>')

LESSON = {
 "unit": "Unit 6: Heredity and Adaptation",
 "title": "End-of-Year Review and Capstone Investigation",
 "subtitle": "This week you tie together heredity and adaptation, from traits and Punnett squares to natural selection, look back at a full year of life science, and design and run your own capstone investigation using every science practice you've built since Week 1. Then you show your mastery on the Unit 6 checkpoint.",
 "objectives": [
  "Explain how traits pass from parents to offspring and predict outcomes with Punnett squares.",
  "Explain how adaptations arise through natural selection over generations.",
  "Connect ideas across the year: cells, classification, body systems, ecosystems and heredity.",
  "Design, carry out and report a fair-test capstone investigation.",
  "Demonstrate mastery of Unit 6 on the checkpoint (85 or higher)."],
 "vocab": [
  ["allele", "One version of a gene, such as T for tall or t for short."],
  ["dominant", "An allele whose trait shows whenever it is present."],
  ["recessive", "An allele whose trait shows only when two copies are present."],
  ["genotype", "The pair of alleles an organism has."],
  ["phenotype", "The trait that actually shows."],
  ["natural selection", "Individuals with helpful inherited traits survive and reproduce more, so those traits become more common over generations."],
  ["independent variable", "The one factor a scientist changes on purpose in a fair test."]],
 "reconnect": {
  "title": "Unit 6, one question from each week",
  "intro": "Warm up with one question from each week of the unit.",
  "items": [
   {"t":"text","q":"Week 26: Thread-like structures in the nucleus that carry genes are called ___.","a":[{"all":[["chromosome"]],"none":["not"]}],"show":"chromosomes","pts":2,"why":"Humans have 23 pairs."},
   {"t":"num","q":"Week 27: In a Tt × tt cross, what percent of offspring are expected to be short (recessive)?","a":50,"unit":"percent","pts":2,"why":"2 of 4 boxes are tt."},
   {"t":"blanks","q":"Week 28: Classify each adaptation as structural, behavioral or physiological.","sent":"A gopher tortoise's shovel-like front legs: ___ &nbsp; Ospreys migrating south in fall: ___","blanks":[[{"all":[["structur"]],"none":["not"]}],[{"all":[["behavior"]],"none":["not","learned"]}]],"show":"structural; behavioral","pts":2,"why":"A body part; an inherited action."},
   {"t":"open","key":"rc_vist","q":"Week 29: Use V-I-S-T in one or two sentences to explain why Florida's Gulf Coast beach mice are pale.","min":20,"rows":2,"rubric":["Uses all four steps correctly"],"model":"Mice varied in coat color, color is inherited, owls caught more dark mice on white sand, and over many generations most beach mice became pale."}]},
 "hook": {
  "title": "From Cells to Populations",
  "visual": PUNNETT,
  "html": "<p>In Week 6 you looked at cells under a microscope. Inside each nucleus are chromosomes carrying genes (Week 26). Those genes come in alleles that pass from parents to offspring in patterns you can predict (Week 27). Some inherited traits help organisms survive in their environment (Week 28), and over many generations natural selection makes those traits common (Week 29). The whole year connects: cells, classification, body systems, ecosystems and heredity are all parts of one story about life.</p><div class='callout'><b>Big question:</b> How do traits pass from one generation to the next, and how do populations change over time?</div>"},
 "learn": [
  {"title": "Review: Traits, Genes and Punnett Squares",
   "html": "<p>Offspring get one allele for each gene from each parent. A <b>dominant</b> allele (capital letter) shows whenever present; a <b>recessive</b> allele (lowercase) shows only with two copies. A Punnett square shows the possible combinations; each box is a 25% chance. Some traits, like height in people, are also shaped by the environment (food, sleep, health).</p>",
   "checks": [
    {"t":"num","q":"Two pea plants that both carry one tall and one short allele (Tt × Tt) are crossed. Out of 100 offspring, about how many would you expect to be short?","a":25,"unit":"plants","pts":2,"why":"1 of 4 boxes is tt; 25% of 100."},
    {"t":"open","key":"rvcarrier","q":"Two brown-eyed parents have a blue-eyed child. Using the words dominant, recessive and allele, explain how this is possible. (Use the simple one-gene model from Week 27.)","min":25,"rows":3,"rubric":["Explains that each parent carries a hidden recessive allele","Explains that the child received one from each parent"],"model":"Each parent has one dominant brown allele and one hidden recessive blue allele. The child inherited the recessive blue allele from both parents, so with two copies, the blue trait shows. (Real eye color involves several genes, but this model shows how a recessive trait can skip a generation.)"}]},
  {"title": "Review: Adaptations and Natural Selection",
   "html": "<p>An <b>adaptation</b> is an inherited trait that helps an organism survive and reproduce in its environment (structural, behavioral or physiological). Adaptations arise through <b>natural selection</b>: variation, inheritance, selection and time. Populations change; individuals don't. When the environment changes faster than a species can adapt, or there's too little variation, extinction can follow.</p>",
   "checks": [
    {"t":"open","key":"rvpython","q":"Burmese pythons now live in the Everglades. Predict how natural selection might change a native prey population, such as marsh rabbits, over many generations, if some rabbits are better at detecting or escaping pythons.","min":30,"rows":3,"rubric":["Applies variation and inheritance","Explains differential survival","Describes change over generations, not in individuals"],"model":"Rabbits vary in how alert they are, and that alertness can be inherited. Rabbits that notice pythons sooner survive and have more babies. Over many generations, more of the population would be very alert. But if pythons eat rabbits faster than they can reproduce, the population could disappear first."}]},
  {"title": "The Year in Review: The Science Practices",
   "html": "<p>Every unit used the same science practices from Unit 1: observe and ask a testable question, change <b>one independent variable</b>, measure a <b>dependent variable</b>, keep everything else the same (<b>controlled variables</b>), repeat trials, record data in tables, graph it and draw a conclusion supported by evidence. Your capstone puts all of that together.</p><ul><li>Unit 1: fair tests and measurement</li><li>Unit 2: cells and the microscope</li><li>Unit 3: classification and dichotomous keys</li><li>Unit 4: body systems</li><li>Unit 5: ecosystems, energy and matter</li><li>Unit 6: heredity and adaptation</li></ul>",
   "checks": [
    {"t":"open","key":"rvvariables","q":"A student tests whether fertilizer amount affects bean plant height. Name the independent variable, the dependent variable and two controlled variables.","min":20,"rows":3,"rubric":["Correct independent variable","Correct dependent variable","Two reasonable controlled variables"],"model":"Independent: the amount of fertilizer. Dependent: plant height. Controlled: the amount of water and the amount of sunlight (also the type of bean and pot size)."},
    {"t":"open","key":"rvconnect","q":"Choose two units from this year and explain one connection between them.","min":25,"rows":3,"rubric":["Two units named","A specific, accurate connection"],"model":"Unit 2 and Unit 6: genes are stored on chromosomes inside the nucleus of every cell, so the cell parts I studied in Unit 2 hold the instructions for traits in Unit 6."}]}],
 "handson": {
  "title": "Capstone Investigation",
  "intro": "Design and carry out your own fair-test investigation on a life science question, then report it like a scientist. This is your Unit 6 science project.",
  "materials": ["Your science notebook, paper and pencil", "Graph paper and a ruler", "A metric ruler or measuring tape", "A timer or clock", "Materials for your chosen investigation (see the Unit 6 projects page for parent-approved ideas, such as bean seeds, cups, potting soil and water)", "A family member"],
  "steps": [
   "Choose a testable question from the Unit 6 projects page or your own idea, and get a parent's approval. Example: Does the amount of light affect how fast bean seeds sprout?",
   "Write a hypothesis, and identify your independent, dependent and controlled variables.",
   "Plan at least three trials for each condition, and list every material and safety step.",
   "Carry out the investigation, recording data in a table every day or every trial.",
   "Graph your results, write a conclusion supported by your data, and name one source of error and one next question.",
   "Wash hands after handling soil, seeds or plants; never taste materials; use only living things and materials your parent approves, and treat any animals gently and only by observing."],
  "record": [
   {"t":"open","key":"caprec","q":"Share your question, hypothesis, variables and data table (or a summary of it).","min":50,"rows":5,"rubric":["A testable question and hypothesis","Independent, dependent and controlled variables","Data from at least three trials per condition"],"model":"Question: Does light affect how fast bean seeds sprout? Hypothesis: Seeds in the dark will sprout at about the same speed, because seeds use stored food. Independent: light or dark. Dependent: days to sprout. Controlled: same bean type, soil, water and temperature. Data: light cups sprouted in 4, 5 and 4 days (mean 4.3); dark cups in 4, 4 and 5 days (mean 4.3)."},
   {"t":"open","key":"capconclude","q":"What is your conclusion? Support it with your data, and name one source of error and one new question.","min":35,"rows":4,"rubric":["A conclusion supported by data","A specific source of error","A new testable question"],"model":"Light didn't affect sprouting speed: both groups averaged 4.3 days, which supports my hypothesis. One source of error was that the dark closet might have been cooler than the windowsill. Next I'd test whether light affects how tall seedlings grow after sprouting."}]},
 "think": {
  "intro": "Your teacher scores this.",
  "items": [
   {"t":"open","key":"yearreflect","q":"Which science idea from this year changed how you see the living world around you? Describe something you now notice or understand in your own backyard, a park or your own body that you didn't before, and connect it to at least two units.","min":66,"rows":6,"rubric":["Names a specific idea and an example from the student's world","Connects to at least two units accurately","Reflects on how the student's thinking changed"],"model":"Learning about adaptations changed how I see our backyard. Now when I see an anole change from green to brown, I know it's a physiological adaptation for camouflage (Unit 6), and I know it's a consumer eating insects in our yard's food web (Unit 5). I also notice that the anoles on our fence look different from the ones in our trees, and I wonder whether natural selection is at work, like the green anoles in Mosquito Lagoon."}]},
 "checkpoint": {
  "title": "Unit 6 Checkpoint: Heredity and Adaptation",
  "intro": "This checkpoint covers Weeks 26 to 29. Answer every question; for written answers, use science vocabulary. Mastery is 85 or higher. If you score below 85, your teacher will review with you, then you will retake it.",
  "parts": [
   {"title": "Part A: Traits and inheritance", "items": [
    {"t":"text","q":"Each body cell in a human has how many chromosomes?","a":["^46","^46 chromosomes","^forty-six","^forty six","^23 pairs","^twenty-three pairs"],"show":"46 (23 pairs)","pts":3,"why":"One of each pair comes from each parent."},
    {"t":"open","key":"cpinherit","q":"Explain why a child resembles both parents but is not identical to either one.","min":20,"rows":2,"pts":3,"rubric":["Explains that half the alleles come from each parent","Explains that the combination is new"],"model":"A child gets half of its chromosomes and alleles from each parent, so it shares traits with both, but the mix of alleles is a new combination that neither parent has."},
    {"t":"open","key":"cpenviron","q":"Identical twins share the same genes. One grows up playing outdoor sports and the other mostly indoors. Name one trait that could differ between them and explain why.","min":18,"rows":2,"pts":4,"rubric":["Names a trait that the environment can affect","Explains the role of the environment"],"model":"Their muscle strength or skin tone could differ, because exercise and sunlight affect the body even when the genes are the same."}]},
   {"title": "Part B: Punnett squares", "items": [
    {"t":"num","q":"In guinea pigs, black fur (B) is dominant over white fur (b). A Bb guinea pig is crossed with a bb guinea pig. What percent of offspring are expected to have white fur?","a":50,"unit":"percent","pts":3,"why":"Two of four boxes are bb."},
    {"t":"num","q":"In the same species, two Bb guinea pigs are crossed. How many of the four Punnett-square boxes would show black fur?","a":3,"unit":"boxes","pts":3,"why":"BB, Bb and Bb are all black."},
    {"t":"open","key":"cpchance","q":"A Bb × Bb cross predicts 25% white offspring, but a litter of 4 pups has no white pups. Does this prove the Punnett square is wrong? Explain.","min":25,"rows":3,"pts":4,"rubric":["Clear decision","Explains that each box is a probability for each offspring","Explains that small samples can differ from predictions"],"model":"No. A Punnett square shows the chance for each pup, not a promise. With only 4 pups, it's like flipping a coin 4 times and not getting exactly 2 heads. With many more pups, about 25% would be white."}]},
   {"title": "Part C: Adaptations", "items": [
    {"t":"blanks","q":"Classify each adaptation.","sent":"A mangrove's prop roots: ___ &nbsp; Sea turtles returning to nest on the beach where they hatched: ___ &nbsp; A rattlesnake making venom: ___","blanks":[[{"all":[["structur"]],"none":["not"]}],[{"all":[["behavior"]],"none":["not","learned"]}],[{"all":[["physiolog"]],"none":["not"]}]],"show":"structural; behavioral; physiological","pts":3,"why":"A body part; an inherited action; a body process."},
    {"t":"open","key":"cpcamo","q":"Explain how camouflage helps both a predator and its prey. Give one Florida example.","min":25,"rows":3,"pts":4,"rubric":["Explains the benefit to prey","Explains the benefit to predators","A valid Florida example"],"model":"Camouflage helps prey hide from predators and helps predators sneak up on prey. A green anole blends into leaves to hide from birds, and an alligator lying still in dark water looks like a log until prey comes close."},
    {"t":"open","key":"cplearned","q":"A dog learns to open a gate latch. Explain why this is not an adaptation in the scientific sense.","min":15,"rows":2,"pts":3,"rubric":["Explains that it is learned during one lifetime","Explains that it is not inherited"],"model":"The dog learned it during its own life, and the skill isn't carried in its genes, so its puppies won't inherit it."}]},
   {"title": "Part D: Natural selection and extinction", "items": [
    {"t":"open","key":"cpvist","q":"Bacteria in an infection vary in how well they resist an antibiotic. Use all four steps of natural selection to explain how a population of resistant bacteria can develop.","min":31,"rows":4,"pts":5,"rubric":["Variation","Inheritance","Selection","Time (change over generations)"],"model":"The bacteria vary: a few can resist the antibiotic. Resistance is passed on when bacteria divide. The antibiotic kills the others, so the resistant ones survive and multiply. Over many generations, most of the population becomes resistant."},
    {"t":"text","q":"What kind of preserved evidence shows that organisms like mammoths and giant ground sloths once lived in Florida?","a":[{"all":[["fossil"]],"none":["not"]}],"show":"fossils","pts":3,"why":"Remains or traces preserved in rock or sediment."},
    {"t":"open","key":"cpextinct","q":"Use the Florida panther to explain why a population with very little variation is at greater risk of extinction, and what scientists did about it.","min":30,"rows":3,"pts":4,"rubric":["Explains the risk of low variation","Describes the 1995 action","Explains why it helped"],"model":"With only 20 to 30 panthers left, there was little variation, so harmful traits like heart defects were common and the population couldn't adapt to new problems. In 1995 scientists released eight Texas pumas, adding new variation, and the population grew healthier and larger."}]}]},
 "next": "Congratulations on finishing Grade 6! Next: the end-of-year comprehensive mastery test."
}

TEACHER = {
 "standards": [
  "SC.7.L.16.1: Understand and explain that every organism requires a set of instructions that specifies its traits, that this hereditary information (DNA) contains genes located in the chromosomes of each cell, and that heredity is the passage of these instructions from one generation to another.",
  "SC.7.L.16.2: Determine the probabilities for genotype and phenotype combinations using Punnett Squares and pedigrees.",
  "SC.7.L.15.2: Explore the scientific theory of evolution by recognizing and explaining ways in which genetic variation and environmental factors contribute to evolution by natural selection and diversity of organisms.",
  "SC.7.L.15.3: Explore the scientific theory of evolution by relating how the inability of a species to adapt within a changing environment may contribute to the extinction of that species.",
  "SC.6.N.1.1: Define a problem from the sixth grade curriculum, use appropriate reference materials to support scientific understanding, plan and carry out scientific investigation of various types, such as systematic observations or experiments, identify variables, collect and organize data, interpret data in charts, tables, and graphics, analyze information, make predictions, and defend conclusions."],
 "materials": ["The interactive lesson", "Science notebook, graph paper, a ruler, a metric ruler or measuring tape, a timer, and materials for the chosen capstone (such as bean seeds, cups, potting soil and water)", "The Unit 6 project rubric", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run one question from each week of the unit."],
  [4, "Hook", "From cells to populations; the Tt × Tt square."],
  [9, "Traits and Punnett squares", "Pea cross out of 100; two brown-eyed parents."],
  [9, "Adaptations and natural selection", "Pythons and marsh rabbits."],
  [9, "Science practices", "Variables review; connect two units."],
  [13, "Capstone launch", "Approve the question, hypothesis and variables; start the first trial."],
  [10, "Checkpoint preview", "Explain that the checkpoint is completed after class, independently, one try per item, with no answers shown until you review it. Mastery is 85; below 85 means a review lesson and a retake."]],
 "key_questions": ["Which allele came from each parent?", "Is each box a promise or a probability?", "Was this trait inherited or developed during one lifetime?", "What is the one thing you changed, and what did you measure?"],
 "misconceptions": ["A Punnett square predicts exact numbers.", "Dominant means more common.", "Individuals evolve.", "A single trial is enough to draw a conclusion."],
 "support": ["Provide a blank Punnett square template.", "Offer three pre-approved capstone questions to choose from.", "Provide a data-table template with columns for each trial."],
 "challenge": ["Design a capstone with two dependent variables (for example, sprouting time and height).", "Research a real Florida natural selection study and present its data."],
 "background": "<p>The capstone runs about one to two weeks for plant investigations; families may finish after the Unit 6 checkpoint. Eye color in the review uses the simplified one-gene model from Week 27, and the model answer notes that real eye color involves several genes. Florida places heredity and evolution benchmarks in Grade 7 (SC.7.L.15.x and 16.x); KCE teaches them here per the Grade 6 scope. Verify standard wording against CPALMS before release.</p>",
 "sources": ["Florida Department of Education, Next Generation Sunshine State Standards for Science.", "Florida Fish and Wildlife Conservation Commission, Florida Panther.", "National Human Genome Research Institute, Talking Glossary of Genomic and Genetic Terms."]
}

PRINT = {
 "directions": "Answer in complete sentences.",
 "items": [
  {"q":"Define dominant and recessive alleles.","a":"Dominant shows whenever present; recessive shows only with two copies.","lines":2},
  {"q":"Draw a Punnett square for Rr × rr. What percent of offspring show the recessive trait?","a":"Rr, Rr, rr, rr; 50%.","lines":4},
  {"q":"Explain the difference between an inherited adaptation and a learned behavior, with an example of each.","a":"Inherited: passed in genes, like a spoonbill's bill; learned: in one lifetime, like a dog opening a latch.","lines":3},
  {"q":"Explain natural selection with V-I-S-T.","a":"Variation; inheritance; selection (helpful traits survive and reproduce more); time (traits become common over generations).","lines":3},
  {"q":"Name the independent, dependent and controlled variables in your capstone.","a":"Answers vary; one changed factor, one measured result, factors kept the same.","lines":3}]
}
