VIST = ('<svg viewBox="0 0 660 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Four steps of natural selection shown with beach mice: variation in coat color, inheritance from parents, selection as owls catch dark mice on white sand, and over time the population becomes mostly light">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Natural selection in four steps: V-I-S-T</text>'
  + ''.join(
    f'<rect x="{18+i*162}" y="34" width="150" height="150" rx="8" fill="#f4ecd6" stroke="#0A1F3D" stroke-width="2"/>'
    f'<text x="{93+i*162}" y="54" text-anchor="middle" font-weight="bold" fill="#0047BA" font-size="14">{t}</text>'
    for i, t in enumerate(["Variation", "Inheritance", "Selection", "Time"])) +
  # variation: mice of different shades
  ''.join(f'<ellipse cx="{48+j*30}" cy="110" rx="12" ry="8" fill="{c}" stroke="#333"/>' for j, c in enumerate(["#f2ead8", "#c9b48a", "#8a6d45", "#4a3a28"])) +
  '<text x="93" y="170" text-anchor="middle" fill="#0A1F3D" font-size="11">coats differ in color</text>'
  # inheritance
  '<ellipse cx="225" cy="90" rx="13" ry="8" fill="#f2ead8" stroke="#333"/><ellipse cx="265" cy="90" rx="13" ry="8" fill="#f2ead8" stroke="#333"/>'
  '<path d="M245 100 V118" stroke="#0A1F3D" stroke-width="2"/><ellipse cx="230" cy="130" rx="10" ry="6" fill="#f2ead8" stroke="#333"/><ellipse cx="260" cy="130" rx="10" ry="6" fill="#f2ead8" stroke="#333"/>'
  '<text x="255" y="170" text-anchor="middle" fill="#0A1F3D" font-size="11">offspring resemble parents</text>'
  # selection: owl over dark mouse
  '<path d="M370 80 q20 -18 40 0 q-20 10 -40 0z" fill="#5b4a36"/><path d="M398 92 L402 110" stroke="#5b4a36" stroke-width="2"/>'
  '<ellipse cx="404" cy="120" rx="12" ry="8" fill="#4a3a28" stroke="#DB2F30" stroke-width="2"/><ellipse cx="370" cy="132" rx="12" ry="8" fill="#f2ead8" stroke="#333"/>'
  '<text x="417" y="170" text-anchor="middle" fill="#0A1F3D" font-size="11">dark mice stand out on</text><text x="417" y="182" text-anchor="middle" fill="#0A1F3D" font-size="11">white sand and get eaten</text>'
  # time
  + ''.join(f'<ellipse cx="{530+(j%4)*22}" cy="{92+(j//4)*22}" rx="9" ry="6" fill="{"#c9b48a" if j==6 else "#f2ead8"}" stroke="#333"/>' for j in range(12)) +
  '<text x="579" y="170" text-anchor="middle" fill="#0A1F3D" font-size="11">most mice become light</text>'
  '<text x="330" y="212" text-anchor="middle" fill="#5b6676" font-size="11">Based on Florida Gulf Coast beach mice. Populations change; individual mice do not.</text></svg>')

LESSON = {
 "unit": "Unit 6: Heredity and Change",
 "title": "Natural Selection Over Time",
 "subtitle": "Why are the beach mice on Florida's white Gulf Coast sand so pale while their inland cousins are dark? Last week you saw that adaptations fit organisms to their environments. This week you learn how those adaptations arise: through natural selection acting on inherited variation over many generations. You'll model it with a predator simulation, see it happening in Florida anoles and in bacteria, and connect it to extinction.",
 "objectives": [
  "Explain natural selection using variation, inheritance, selection and time.",
  "Distinguish changes in a population over generations from changes in one individual's life.",
  "Describe evidence for natural selection, including Florida beach mice, anoles and antibiotic resistance.",
  "Explain how environmental change can lead to extinction when a species cannot adapt.",
  "Model natural selection, collect data across generations and interpret the results."],
 "vocab": [
  ["natural selection", "The process in which individuals with inherited traits that help them survive and reproduce leave more offspring, so those traits become more common over generations."],
  ["variation", "Differences in traits among individuals of the same species."],
  ["population", "All the members of one species living in an area."],
  ["generation", "One step in a family line: parents, then offspring, then their offspring."],
  ["evolution", "Change in the inherited traits of a population over many generations."],
  ["fossil", "Preserved remains or traces of an organism that lived long ago."],
  ["extinction", "The permanent loss of every member of a species."]],
 "reconnect": {
  "title": "Week 28: Adaptations",
  "intro": "Last week: what adaptations are. This week: how they come to be.",
  "items": [
   {"t":"text","q":"A gopher tortoise digging a burrow is what kind of adaptation?","a":["^behavioral",{"all":[["behavior"]],"none":["not behavior","structural","physiological"]}],"show":"behavioral","pts":2,"why":"It's an action."},
   {"t":"open","key":"rc_tan","q":"Why can't a tan or a learned skill be passed to offspring?","min":12,"rows":2,"rubric":["Explains that it is not in the genes (not inherited)"],"model":"A tan or a learned skill develops during one life and isn't carried in the genes, so offspring don't inherit it."},
   {"t":"open","key":"rc_how","q":"Spoonbills have spoon-shaped bills. Do you think an ancestor spoonbill grew a spoon bill because it needed one? Explain your thinking.","min":15,"rows":2,"rubric":["States a prediction with a reason (scored for reasoning, revisited later in the lesson)"],"model":"No. I think birds with slightly wider bills caught more food and had more chicks, so over many generations the bills got wider. One bird can't change its bill by needing it."}]},
 "hook": {
  "title": "The Pale Mice of the White Sand",
  "visual": VIST,
  "html": "<p>Along Florida's Gulf Coast, from Perdido Key to Santa Rosa Island, the dunes are made of sugar-white quartz sand. The beach mice that live there are pale, nearly white. A short distance inland, where the soil is darker, the oldfield mice of the same species are brown.</p><p>Owls, herons and hawks hunt by sight. On white sand, a dark mouse is easy to spot. Scientists have even found the gene responsible for much of the coat-color difference (Hoekstra and colleagues, 2006).</p><div class='callout'><b>Big question:</b> How can a whole population change over time, when no single mouse ever changes its coat?</div>"},
 "learn": [
  {"title": "Darwin, Wallace and the Four Steps",
   "html": "<p>In 1858, Charles Darwin and Alfred Russel Wallace each described <b>natural selection</b>. Darwin had studied finches, tortoises and fossils on his voyage on HMS Beagle; Wallace worked in the Amazon and the islands of Southeast Asia. Remember it with <b>V-I-S-T</b>:</p><ul><li><b>Variation:</b> individuals in a population differ (coat color, beak depth).</li><li><b>Inheritance:</b> many traits are passed from parents to offspring through genes (Weeks 26 and 27).</li><li><b>Selection:</b> more offspring are born than can survive. Individuals with helpful traits survive and reproduce more.</li><li><b>Time:</b> over many generations, helpful traits become more common in the population.</li></ul><p>Key idea: <b>individuals don't evolve; populations do.</b> A mouse can't lighten its coat because it needs to. Light mice simply leave more pups.</p>",
   "checks": [
    {"t":"blanks","q":"Match each statement to its step: variation, inheritance, selection or time.","sent":"Pups of pale mice tend to be pale: ___ &nbsp; Owls catch more dark mice on white sand: ___ &nbsp; Coats range from cream to brown: ___ &nbsp; After hundreds of generations, nearly all beach mice are pale: ___","blanks":[[{"all":[["inherit"]],"none":["not"]}],[{"all":[["select"]],"none":["not"]}],[{"all":[["variation","vary"]],"none":["not"]}],[{"all":[["time"]],"none":["not"]}]],"show":"inheritance; selection; variation; time","pts":4,"why":"V-I-S-T."},
    {"t":"open","key":"giraffe","q":"A friend says, \"Giraffes got long necks because they stretched to reach leaves, and their babies were born with longer necks.\" Use natural selection to correct this.","min":30,"rows":3,"rubric":["Explains that stretching during a lifetime isn't inherited","Explains variation and differential survival","Explains change over generations"],"model":"Stretching your neck doesn't change your genes, so babies wouldn't inherit it. Instead, giraffes varied in neck length, and those with longer necks reached more food during droughts, survived and had more babies. Over many generations, long necks became more common."}]},
  {"title": "Natural Selection Happening Now",
   "html": "<p>Natural selection isn't just ancient history. Scientists have measured it:</p><ul><li><b>Galápagos finches:</b> Peter and Rosemary Grant measured medium ground finches for decades. After a 1977 drought left mostly large, hard seeds, birds with deeper beaks survived, and the next generation's beaks averaged about half a millimeter deeper.</li><li><b>Florida anoles:</b> after brown anoles were introduced to islands in a Florida lagoon, native green anoles moved higher into the trees. Within about 15 years (roughly 20 generations), green anoles there had larger, stickier toe pads for gripping thin branches (Stuart and colleagues, 2014).</li><li><b>Antibiotic resistance:</b> when antibiotics kill most bacteria in an infection, a few with resistant traits may survive and multiply. That's why doctors tell patients to take antibiotics exactly as prescribed, and not to use them for viruses like colds.</li></ul>",
   "checks": [
    {"t":"open","key":"anoletoes","q":"Explain the green anoles' larger toe pads using V-I-S-T.","min":32,"rows":3,"rubric":["Applies each of the four steps to anoles"],"model":"Green anoles varied in toe-pad size. Toe-pad size is inherited. After brown anoles pushed them higher, anoles with bigger pads gripped thin branches better, survived and laid more eggs. Over about 20 generations, big toe pads became common."},
    {"t":"open","key":"bacteria","q":"Why does using antibiotics when they aren't needed make resistant bacteria more common?","min":25,"rows":2,"rubric":["Explains that antibiotics kill susceptible bacteria","Explains that resistant survivors multiply"],"model":"Each use kills the bacteria that can't resist the drug, but any resistant ones survive and multiply with less competition. The more often antibiotics are used, the more often resistant bacteria get that advantage."}]},
  {"title": "Evidence from Fossils and Living Things",
   "html": "<p>Evidence that species change over long periods comes from several directions:</p><ul><li><b>Fossils</b> show organisms that no longer exist and changes over time in rock layers. Florida's fossil record includes mammoths, giant ground sloths, saber-toothed cats and huge sharks like megalodon.</li><li><b>Similar body structures:</b> a human arm, a bat wing, a whale flipper and a bird wing contain the same set of bones, suggesting a shared ancestor.</li><li><b>DNA:</b> closely related species share more DNA.</li></ul>",
   "checks": [
    {"t":"open","key":"limbs","q":"A bat wing and a human arm have the same bones arranged differently. What does this suggest, and why are they shaped differently?","min":24,"rows":2,"rubric":["Suggests a shared ancestor","Explains different shapes as fits to different ways of life"],"model":"It suggests bats and humans share an ancient ancestor with those bones. Over millions of years natural selection shaped them differently because bats fly and humans grab and carry."}]},
  {"title": "When a Species Can't Keep Up: Extinction",
   "html": "<p>Natural selection needs <b>variation</b> and <b>time</b>. When the environment changes faster than a population can adapt, or no individuals have helpful traits, a species can go <b>extinct</b>.</p><ul><li>Florida's Ice Age mammoths and giant sloths disappeared about 11,000 to 13,000 years ago as climate warmed and human hunting increased.</li><li>The dusky seaside sparrow, found only near Florida's Merritt Island and St. Johns River, went extinct in 1987 after its marsh habitat was flooded and drained.</li><li>Florida panthers dropped to about 20 to 30 animals by the 1990s. With so little variation, many had heart defects and kinked tails. In 1995, eight female Texas pumas were brought in to add variation, and the population has since grown to roughly 120 to 230 adults.</li></ul>",
   "checks": [
    {"t":"open","key":"panther","q":"Why did adding Texas pumas help Florida panthers survive? Use the word variation.","min":25,"rows":2,"rubric":["Uses variation correctly","Connects variation to survival or adaptation"],"model":"The tiny panther population had very little variation, so harmful traits like heart defects were common. The Texas pumas added new variation, so more kittens were healthy and the population could adapt."},
    {"t":"open","key":"sparrow","q":"Why couldn't the dusky seaside sparrow adapt in time to survive the loss of its marsh?","min":20,"rows":2,"rubric":["Explains the change was too fast or there was no helpful variation"],"model":"The marsh was flooded and drained in just a few decades, much faster than natural selection could work, and the sparrows had nowhere else to live."}]}],
 "handson": {
  "title": "Paper Dot Predators",
  "intro": "Model natural selection by being the predator, then track how the population changes over four generations.",
  "materials": ["A sheet of newspaper (black-and-white print)", "Two sheets of plain white paper and two extra sheets of newspaper to cut into dots", "Scissors (adult help as needed) or a hole punch", "A timer", "Tweezers or a clothespin", "Paper and pencil", "Graph paper and a ruler", "A family member"],
  "steps": [
   "Cut or punch 40 small dots: 20 from white paper and 20 from newspaper. These are your \"moths.\"",
   "Spread a full newspaper sheet on a table as the habitat. Your family member scatters all 40 dots on it while you look away.",
   "Generation 1: as the \"bird,\" pick up dots one at a time with the tweezers for 15 seconds. Count the white and newspaper dots that are left.",
   "Survivors reproduce: for each surviving dot, add one new dot of the same kind, so the population grows back toward 40. Record the counts.",
   "Repeat for 4 generations, then graph the number of each kind of dot by generation.",
   "Handle scissors carefully, and keep the paper dots and hole-punch pieces away from young children and pets (choking hazard)."],
  "record": [
   {"t":"open","key":"dotdata","q":"Record the number of white and newspaper dots at the start of each generation, and describe the trend in your graph.","min":30,"rows":5,"rubric":["Data for 4 generations","A graph described","Describes the trend correctly"],"model":"Start: 20 white, 20 newspaper. Gen 2: 12 white, 28 newspaper. Gen 3: 6 white, 34 newspaper. Gen 4: 2 white, 38 newspaper. My line graph shows white dots dropping and newspaper dots rising every generation."},
   {"t":"open","key":"dotexplain","q":"Explain your results using V-I-S-T, and predict what would happen on a plain white habitat.","min":40,"rows":4,"rubric":["Applies all four steps","A logical prediction for the white habitat"],"model":"The dots varied in color. Survivors made copies of themselves, like inheritance. I spotted and picked up white dots more easily, which is selection. Over four generations, camouflaged newspaper dots took over. On white paper the opposite would happen: white dots would survive and newspaper dots would disappear."}]},
 "think": {
  "intro": "Your teacher scores these.",
  "items": [
   {"t":"open","key":"spoonbillagain","q":"Return to your Reconnect answer about spoonbill bills. Rewrite your explanation using everything you learned, including V-I-S-T and the difference between individuals and populations.","min":54,"rows":5,"rubric":["Applies all four steps to spoonbills","States that populations, not individuals, change","Revises or confirms the earlier thinking"],"model":"Ancestral spoonbills varied in bill shape, and bill shape is inherited. Birds whose bills were a bit wider at the tip swept up more small fish and shrimp, survived and raised more chicks. Over many generations, the population came to have spoon-shaped bills. No single bird changed its bill; the population changed. My first answer was right, and now I can explain each step."},
   {"t":"open","key":"climate","q":"Florida's climate is warming and sea level is rising. Choose one Florida species and predict whether it might adapt, move or decline. Use variation, generation time and the speed of change in your reasoning.","min":46,"rows":5,"rubric":["Names a Florida species","Uses variation, generation time and speed of change","A reasoned prediction"],"model":"Key deer live only in the low Florida Keys. They have few individuals and produce one fawn a year, so natural selection would be slow, and rising seas are flooding their freshwater and habitat quickly. They can't easily move off the islands. I predict they'll decline unless people protect fresh water and habitat for them."}]},
 "exit": [
  {"t":"open","key":"exit_vist","q":"Name the four parts of natural selection.","min":3,"rows":1,"rubric":["Variation, inheritance, selection, time"],"model":"Variation, inheritance, selection and time."},
  {"t":"text","q":"Do individuals or populations evolve?","a":["^populations","^population",{"all":[["population"]],"none":["individual","not population"]}],"show":"populations","pts":2,"why":"Individuals can't change their genes."},
  {"t":"open","key":"exit_extinct","q":"Give one reason a species might go extinct.","min":8,"rows":2,"rubric":["A valid reason tied to environmental change or lack of variation"],"model":"Its habitat changed faster than natural selection could help it adapt."}],
 "next": "Week 30: end-of-year review and capstone investigation."
}

TEACHER = {
 "standards": [
  "SC.7.L.15.2: Explore the scientific theory of evolution by recognizing and explaining ways in which genetic variation and environmental factors contribute to evolution by natural selection and diversity of organisms.",
  "SC.7.L.15.3: Explore the scientific theory of evolution by relating how the inability of a species to adapt within a changing environment may contribute to the extinction of that species.",
  "SC.7.L.15.1: Recognize that fossil evidence is consistent with the scientific theory of evolution that living things evolved from earlier species.",
  "SC.6.N.1.1: Define a problem from the sixth grade curriculum, use appropriate reference materials to support scientific understanding, plan and carry out scientific investigation of various types, such as systematic observations or experiments, identify variables, collect and organize data, interpret data in charts, tables, and graphics, analyze information, make predictions, and defend conclusions."],
 "materials": ["The interactive lesson", "Newspaper, white paper, scissors or a hole punch, tweezers or a clothespin, a timer, graph paper, a ruler, paper and pencil", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 28 warm-up questions; note the spoonbill prediction."],
  [4, "Hook", "Pale beach mice on white sand."],
  [12, "V-I-S-T", "Darwin and Wallace; correct the giraffe myth."],
  [12, "Happening now", "Finches, Florida anoles, antibiotic resistance."],
  [8, "Evidence", "Fossils, limb bones, DNA."],
  [12, "Extinction", "Mammoths, dusky seaside sparrow, Florida panther."],
  [6, "Assign", "Set up paper dot predators; assign Think Deeper and the Exit Check."]],
 "key_questions": ["What varied, and was it inherited?", "Which individuals survived and reproduced more, and why?", "Did an individual change, or did the population?", "Why can't some species adapt in time?"],
 "misconceptions": ["Organisms change because they need or want to.", "Individuals evolve during their lifetimes.", "Natural selection always produces perfect organisms.", "Evolution means humans came from today's monkeys (we share common ancestors)."],
 "support": ["Provide a V-I-S-T graphic organizer.", "Run one generation of the simulation together before the student continues alone.", "Use the beach mouse diagram as a model for every example."],
 "challenge": ["Research the Grants' finch studies and graph the beak-depth change.", "Design a version of the dot simulation with three colors and predict the outcome."],
 "background": "<p>Beach mice (Peromyscus polionotus subspecies) on Gulf Coast barrier islands; Hoekstra et al., Science (2006), linked a Mc1r mutation to light coat color. Grant and Grant documented a mean beak-depth increase of about 0.5 mm after the 1977 Daphne Major drought. Stuart et al., Science (2014), measured green anole toe-pad change on Mosquito Lagoon spoil islands. Dusky seaside sparrow declared extinct 1990 after the last bird died in 1987. Florida panther: eight Texas females released 1995; FWC estimates 120 to 230 adults. Florida places evolution benchmarks in Grade 7 (SC.7.L.15.x); KCE teaches them here per the Grade 6 scope. Verify standard wording against CPALMS.</p>",
 "sources": ["Hoekstra, H. E., et al., \"A Single Amino Acid Mutation Contributes to Adaptive Beach Mouse Color Pattern,\" Science (2006).", "Grant, P. R., and B. R. Grant, How and Why Species Multiply (2008).", "Stuart, Y. E., et al., \"Rapid Evolution of a Native Species Following Invasion by a Congener,\" Science (2014).", "Florida Fish and Wildlife Conservation Commission, Florida Panther.", "U.S. Fish and Wildlife Service, Dusky Seaside Sparrow.", "Centers for Disease Control and Prevention, Antimicrobial Resistance."]
}

PRINT = {
 "directions": "Answer in complete sentences.",
 "items": [
  {"q":"Explain natural selection using V-I-S-T and one example.","a":"Variation in traits, inherited, individuals with helpful traits survive and reproduce more, over time traits become common; beach mice.","lines":4},
  {"q":"Why don't individuals evolve?","a":"An individual can't change its inherited genes; populations change as survivors pass on traits.","lines":2},
  {"q":"How do antibiotic-resistant bacteria become more common?","a":"Antibiotics kill susceptible bacteria; resistant survivors multiply.","lines":2},
  {"q":"Give two kinds of evidence that species change over time.","a":"Fossils; similar bone structures; DNA.","lines":2},
  {"q":"Why are species with little variation at greater risk of extinction?","a":"If the environment changes, there may be no individuals with helpful traits to survive, as with Florida panthers.","lines":2}]
}
