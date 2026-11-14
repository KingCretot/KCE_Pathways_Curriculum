TYPES = ('<svg viewBox="0 0 660 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Three kinds of adaptations with Florida examples: structural, behavioral and physiological">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Three kinds of adaptations, with Florida examples</text>'
  + ''.join(f'<g transform="translate({16+i*214},36)"><rect width="200" height="180" rx="12" fill="{c}"/><text x="100" y="28" text-anchor="middle" fill="#fff" font-weight="bold" font-size="15">{a}</text><text x="100" y="48" text-anchor="middle" fill="#fff" font-size="11">{b}</text>'
            + ''.join(f'<text x="100" y="{78+j*22}" text-anchor="middle" fill="#fff" font-size="11">{t}</text>' for j, t in enumerate(lines)) + '</g>'
            for i, (a, b, c, lines) in enumerate([("Structural", "body parts and shapes", "#0047BA", ["roseate spoonbill's spoon bill", "red mangrove's prop roots", "alligator's eyes on top of head", "longleaf pine's thick bark", "osprey's curved talons"]),
                                                 ("Behavioral", "actions", "#2c6e22", ["manatees moving to warm springs", "gopher tortoises digging burrows", "burrowing owls bobbing to warn", "sea turtles nesting at night", "opossums playing dead"]),
                                                 ("Physiological", "body chemistry and processes", "#8a6d1f", ["black mangroves excreting salt", "red mangroves filtering salt", "alligators slowing their hearts", "sharks sensing electricity", "frogs surviving drought"])])) +
  '</svg>')

BEAKS = ('<svg viewBox="0 0 660 210" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Florida bird beaks matched to foods: spoonbill sweeps for shrimp, osprey tears fish, cardinal cracks seeds, hummingbird sips nectar">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Beak shape fits food: structural adaptations in Florida birds</text>'
  + ''.join(f'<g transform="translate({20+i*160},40)"><rect width="150" height="150" rx="10" fill="#faf8f2" stroke="#e6dfcc"/>{pic}<text x="75" y="118" text-anchor="middle" fill="#0A1F3D" font-weight="bold">{n}</text><text x="75" y="136" text-anchor="middle" fill="#5b6676" font-size="11">{f}</text></g>'
            for i, (n, f, pic) in enumerate([("roseate spoonbill", "sweeps for shrimp", '<circle cx="45" cy="50" r="18" fill="#f3a7c0"/><path d="M60 48 L110 46" stroke="#8a95a5" stroke-width="5"/><ellipse cx="118" cy="46" rx="12" ry="8" fill="#8a95a5"/>'),
                                             ("osprey", "hooks and tears fish", '<circle cx="60" cy="50" r="20" fill="#5b6676"/><path d="M78 44 Q102 44 100 62 Q92 54 80 56Z" fill="#0A1F3D"/>'),
                                             ("northern cardinal", "cracks seeds", '<circle cx="60" cy="52" r="20" fill="#DB2F30"/><path d="M78 46 L100 54 L78 62Z" fill="#e89a3c"/>'),
                                             ("hummingbird", "sips nectar", '<circle cx="50" cy="52" r="14" fill="#2c6e22"/><path d="M63 50 L125 46" stroke="#0A1F3D" stroke-width="2.5"/>')])) +
  '</svg>')

LESSON = {
 "unit": "Unit 6: Heredity and Adaptation",
 "title": "Adaptations",
 "subtitle": "Why does a spoonbill have a spoon for a bill and a mangrove stand on stilts? In Week 11 you learned that living things adapt over generations, and in Week 24 you watched green anoles' toe pads change. This week you classify structural, behavioral and physiological adaptations, test how body shapes fit jobs, and connect adaptations to the genes and variation of Weeks 26 and 27.",
 "objectives": [
  "Define an adaptation and classify adaptations as structural, behavioral or physiological.",
  "Explain how specific adaptations help Florida organisms survive and reproduce in their environments.",
  "Distinguish inherited adaptations from changes an individual makes during its life (acclimatization and learning).",
  "Explain camouflage and mimicry as adaptations.",
  "Connect adaptations to inherited variation in a population."],
 "vocab": [
  ["adaptation", "An inherited trait that helps an organism survive and reproduce in its environment."],
  ["structural adaptation", "A body part or shape that helps an organism survive, such as a beak or a thick coat."],
  ["behavioral adaptation", "An inherited action or pattern of behavior that helps an organism survive, such as migration."],
  ["physiological adaptation", "A body process or chemistry that helps an organism survive, such as making venom."],
  ["camouflage", "Coloring or shape that helps an organism blend into its surroundings."],
  ["mimicry", "When an organism looks or acts like another species, which helps it survive."],
  ["variation", "Differences in traits among individuals of the same species."]],
 "reconnect": {
  "title": "Week 27: Punnett squares",
  "intro": "Adaptations are inherited, so they follow last week's rules.",
  "items": [
   {"t":"num","q":"In a Bb × bb cross, what percent of offspring are expected to show the recessive trait?","a":50,"unit":"percent","pts":2,"why":"2 of 4 boxes are bb."},
   {"t":"text","q":"The pair of allele letters an organism has, such as Bb, is its ___.","a":[{"all":[["genotype"]],"none":["not","phenotype"]}],"show":"genotype","pts":2,"why":"The trait that shows is the phenotype."},
   {"t":"text","q":"Whose pea plant experiments discovered dominant and recessive traits?","a":[{"all":[["mendel"]],"none":["not"]}],"show":"Gregor Mendel","pts":2,"why":"In the 1850s and 1860s."},
   {"t":"open","key":"rc_variation","q":"Last week's Punnett squares showed that offspring of the same parents can have different traits. Why might that variety matter if the environment changes?","min":15,"rows":2,"rubric":["Explains that some individuals may have traits that help in the new conditions"],"model":"If the environment changes, some offspring might have a trait that helps them survive the new conditions, so the population is more likely to survive."}]},
 "hook": {
  "title": "Built for the Job",
  "visual": TYPES,
  "html": "<p>A roseate spoonbill wades through a Florida marsh, sweeping its flat, spoon-shaped bill side to side. When the bill touches a shrimp, it snaps shut. Nearby, a red mangrove stands on arching prop roots in salty water that would kill most trees, and its roots filter out most of the salt before water enters the tree.</p><p>These are <b>adaptations</b>: inherited traits that help organisms survive and reproduce where they live. The spoonbill's pink color even comes from the shrimp it eats, like the flamingo you learned about in Week 26.</p><div class='callout'><b>Big question:</b> How do adaptations help organisms survive, and where do they come from?</div>"},
 "learn": [
  {"title": "Three Kinds of Adaptations",
   "html": "<p>Scientists sort adaptations into three kinds:</p><ul><li><b>Structural</b> adaptations are body parts and shapes: a spoonbill's bill, an osprey's curved talons, an alligator's eyes and nostrils on top of its head so it can see and breathe while almost hidden.</li><li><b>Behavioral</b> adaptations are inherited patterns of action: manatees moving to warm springs in winter, sea turtles nesting at night, gopher tortoises digging burrows up to 40 feet long that more than 350 other species share.</li><li><b>Physiological</b> adaptations are body processes: red mangroves filtering salt out at their roots and black and white mangroves pushing extra salt out through their leaves, alligators slowing their heart rate to stay underwater for long periods, sharks sensing the tiny electric fields of hidden prey.</li></ul>",
   "checks": [
    {"t":"blanks","q":"Classify each adaptation as structural, behavioral or physiological.","sent":"A pitcher plant's slippery tube-shaped leaves: ___ &nbsp; An anhinga spreading its wings to dry in the sun: ___ &nbsp; A rattlesnake making venom: ___","blanks":[[{"all":[["structur"]],"none":["not"]}],[{"all":[["behavior"]],"none":["not"]}],[{"all":[["physiolog"]],"none":["not"]}]],"show":"structural; behavioral; physiological","pts":3,"why":"A body part; an action; a body process."},
    {"t":"open","key":"tortoise","q":"Gopher tortoise burrows shelter more than 350 other species, such as indigo snakes and burrowing owls, during fires and cold. Explain why scientists call the gopher tortoise a keystone species, using an idea from Unit 5.","min":30,"rows":3,"rubric":["Explains that many species depend on the burrows","Connects to food webs, interactions or commensalism from Unit 5"],"model":"So many other animals depend on gopher tortoise burrows that losing the tortoise would affect a huge part of the community, like removing a keystone collapses an arch. Animals sheltering in the burrows is commensalism from Week 24: they benefit, and the tortoise isn't harmed."}]},
  {"title": "Adaptations Fit Environments",
   "visual": BEAKS,
   "html": "<p>An adaptation is only helpful in a particular environment. A spoonbill's bill is perfect for sweeping muddy water but useless for cracking seeds. A cardinal's thick, cone-shaped beak cracks seeds; a hummingbird's long, thin bill reaches nectar deep in flowers.</p><p>Fire is part of many Florida ecosystems. Longleaf pines spend their first years as a grassy tuft with the growing bud protected by thick needles, then grow fast; their thick bark survives low fires. Saw palmettos resprout quickly after burning. In these forests, fire-adapted plants win, and fires actually help keep the ecosystem healthy.</p>",
   "checks": [
    {"t":"open","key":"wrongplace","q":"Predict what would happen to a population of roseate spoonbills moved to a dry pine forest with no shallow water. Explain using the idea of adaptations fitting environments.","min":25,"rows":3,"rubric":["A prediction about the population", "Explains using how the bill fits the environment"],"model":"They would struggle to survive because their spoon-shaped bills are adapted to sweeping shallow water for shrimp and small fish. In a dry forest there's no food they can catch that way, so most would starve or leave."},
    {"t":"open","key":"fireadapt","q":"In Week 21 you saw fire as an abiotic factor in longleaf forests. Now explain how longleaf pines are adapted to fire, and why firefighters and land managers sometimes set controlled burns in Florida forests.","min":30,"rows":3,"rubric":["Describes a fire adaptation of longleaf pine","Explains why controlled burns help the ecosystem"],"model":"Young longleaf pines protect their growing bud inside a thick tuft of needles, and older trees have thick bark, so low fires don't kill them. Land managers set controlled burns because fire clears out competing shrubs and keeps the pine forest healthy for the many species adapted to it, like gopher tortoises."}]},
  {"title": "Camouflage and Mimicry",
   "html": "<p><b>Camouflage</b> helps organisms hide: a Florida green anole can shift between green and brown, and a juvenile alligator's black-and-yellow bands break up its outline among reeds and shadows. <b>Mimicry</b> means looking like another species:</p><ul><li>Viceroy and monarch butterflies look alike. Both taste bad to birds, so a bird that tries one learns to avoid both.</li><li>The harmless scarlet kingsnake has red, black and yellow bands similar to the venomous eastern coral snake, so predators that avoid coral snakes often avoid kingsnakes too.</li></ul><p><b>Safety:</b> never handle any snake in the wild. Color-pattern rhymes are not reliable for identifying snakes; stay back and let it move away.</p>",
   "checks": [
    {"t":"text","q":"A harmless scarlet kingsnake looks like a venomous coral snake. What is this adaptation called?","a":[{"all":[["mimicry","mimic"]],"none":["not"]}],"show":"mimicry","pts":2,"why":"Predators avoid both."},
    {"t":"open","key":"mimicwhy","q":"Explain how looking like a coral snake helps a scarlet kingsnake survive, even though it has no venom.","min":20,"rows":2,"rubric":["Explains how predators respond to the kingsnake's appearance", "Connects that response to the kingsnake's survival"],"model":"Predators that have learned to avoid coral snakes stay away from anything with similar bands, so the kingsnake gets left alone even though it can't hurt them."}]},
  {"title": "Inherited Adaptations Versus Changes in a Lifetime",
   "html": "<p>An adaptation is <b>inherited</b>: it comes from genes, as you learned in Weeks 26 and 27. Changes that happen during one organism's life are different:</p><ul><li><b>Acclimatization:</b> a person who moves from Florida to Colorado makes more red blood cells after a few weeks in the thin mountain air. Their children won't inherit those extra cells.</li><li><b>Learning:</b> a raccoon learns to open trash cans. Its babies must learn it themselves.</li></ul><p>Adaptations exist because individuals in a population have <b>variation</b>. Those with helpful inherited traits survive and reproduce more, passing those traits on. Next week you'll see how this process, natural selection, changes populations over time.</p>",
   "checks": [
    {"t":"open","key":"adaptvsaccl","q":"A dog grows a thicker coat when its family moves from Miami to Minnesota. Is the thicker coat an adaptation in the scientific sense? Explain.","min":25,"rows":3,"rubric":["A clear decision about whether it is an adaptation", "Explains the difference between an inherited ability and a change during one lifetime"],"model":"Not exactly. The dog's ability to grow a thicker coat in cold weather is an inherited adaptation, but the thicker coat itself is a change in one dog's lifetime, called acclimatization. Its puppies born in Miami wouldn't be born with thicker coats."}]}],
 "handson": {
  "title": "Beak Buffet",
  "intro": "Test which \"beak\" tools are best adapted for different foods, then design an organism for a Florida habitat.",
  "materials": ["Four tools to act as beaks: a spoon, tweezers, a clothespin and a pair of chopsticks (or two pencils)", "Four foods: dry rice, small marbles or dried beans, cut-up drinking straws, and water in a shallow bowl with a few floating cereal pieces", "Four paper plates and a cup for each \"bird's stomach\"", "A timer", "A family member", "Paper and pencil"],
  "steps": [
   "Spread each food on its own plate (put the floating cereal in the bowl of water).",
   "Choose one beak tool. Set a timer for 30 seconds and move as much of one food as you can into your cup. Count or measure what you collected.",
   "Repeat with the same beak for every food, then repeat the whole test with each beak. Record everything in a table.",
   "Find the best beak for each food. Then race a family member using two different beaks on the same food to see which wins.",
   "Design an organism with at least one structural, one behavioral and one physiological adaptation for a Florida habitat (a spring, a mangrove, a pine forest or a beach). Draw and label it.",
   "Don't eat the food used in the test. Keep marbles and beans away from young children (choking hazard), and wipe up spilled water so no one slips."],
  "record": [
   {"t":"open","key":"beakrec","q":"Share your data table. Which beak was best for each food, and which real Florida bird does each winning beak resemble?","min":34,"rows":5,"rubric":["A data table for all beaks and foods","Best beak named for each food","A real bird connection for each"],"model":"Rice: tweezers won (42 grains), like a warbler picking insects. Marbles: clothespin won (9), like a cardinal's strong seed-cracking beak. Straw pieces: chopsticks won (14), like a heron grabbing fish. Floating cereal: spoon won (11), like a spoonbill sweeping water."},
   {"t":"open","key":"designrec","q":"Describe the organism you designed, its habitat and its three adaptations, and explain how each helps it survive or reproduce there.","min":45,"rows":5,"rubric":["A habitat and organism","One structural, one behavioral and one physiological adaptation","Explains how each helps"],"model":"My \"spring sprinter\" is a small fish for Florida's springs. Structural: a flat, silver body to blend with the sandy bottom. Behavioral: it schools with others near eelgrass so predators can't single one out. Physiological: it can handle the spring's constant 72°F water and low oxygen near the vents. Each helps it avoid predators and live where few other fish can."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"pythonadv","q":"Burmese pythons have spread through the Everglades (Week 22). Name two adaptations that help them survive there, and explain why native animals had no defenses against them.","min":37,"rows":4,"rubric":["Two plausible python adaptations","Explains the mismatch with native prey's adaptations"],"model":"Pythons are strong swimmers and can go months between meals, both adaptations for swampy habitats with patchy food. Native mammals like raccoons and marsh rabbits never evolved alongside giant constrictors, so they don't recognize pythons as a danger or have behaviors to avoid them."},
   {"t":"open","key":"climateadapt","q":"As Florida's climate warms and seas rise, which kinds of organisms might do better and which might struggle? Use the idea of adaptations fitting environments and give one example of each. What could happen to a species that cannot adapt?","min":34,"rows":4,"rubric":["One organism likely to do better, with a reason", "One organism likely to struggle, with a reason", "Uses the idea of adaptations fitting environments", "Explains a possible outcome for a species that cannot adapt"],"model":"Mangroves, adapted to salty water, are already spreading north as winters get warmer, so they may do better. Freshwater plants near the coast, like some sawgrass marshes, may struggle as salt water moves inland, because they aren't adapted to handle salt. A species that can't adapt or move could decline or even go extinct."}]},
 "exit": [
  {"t":"text","q":"Manatees moving to warm springs in winter is what kind of adaptation?","a":["^behavioral",{"all":[["behavior"]],"none":["not behavior","structural","physiological","learned"]}],"show":"behavioral","pts":2,"why":"It's an action."},
  {"t":"text","q":"Coloring that helps an organism blend into its surroundings is called ___.","a":[{"all":[["camouflage","camoflage"]],"none":["not"]}],"show":"camouflage","pts":2,"why":"Like a green anole on a leaf."},
  {"t":"open","key":"exit_inherit","q":"Why isn't a suntan an adaptation, even though it protects the skin?","min":10,"rows":2,"rubric":["Explains that it develops during one lifetime and is not inherited"],"model":"A tan develops during one person's life and isn't passed on to their children, so it isn't an inherited adaptation."}],
 "next": "Week 29: natural selection over time."
}

TEACHER = {
 "standards": [
  "SC.7.L.15.2: Explore the scientific theory of evolution by recognizing and explaining ways in which genetic variation and environmental factors contribute to evolution by natural selection and diversity of organisms.",
  "SC.7.L.15.3: Explore the scientific theory of evolution by relating how the inability of a species to adapt within a changing environment may contribute to the extinction of that species.",
  "SC.6.N.1.1: Define a problem from the sixth grade curriculum, use appropriate reference materials to support scientific understanding, plan and carry out scientific investigation of various types, such as systematic observations or experiments, identify variables, collect and organize data, interpret data in charts, tables, and graphics, analyze information, make predictions, and defend conclusions."],
 "materials": ["The interactive lesson", "A spoon, tweezers, a clothespin, chopsticks; rice, marbles or beans, cut straws, a shallow bowl of water with cereal; paper plates and cups; a timer", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 27 warm-up questions."],
  [4, "Hook", "Spoonbill and mangrove; the three kinds."],
  [11, "Three kinds", "Classify; the gopher tortoise as keystone."],
  [12, "Fit to environment", "Beaks and foods; fire-adapted pines."],
  [10, "Camouflage and mimicry", "Anoles, viceroys, kingsnakes; snake safety."],
  [11, "Inherited versus lifetime changes", "Acclimatization; variation; preview natural selection."],
  [6, "Assign", "Set up the beak buffet; assign Think Deeper and the Exit Check."]],
 "key_questions": ["Is this a body part, an action or a body process?", "How does this trait help it survive or reproduce here?", "Would this trait help in a different environment?", "Was this trait inherited or developed during one life?"],
 "misconceptions": ["Organisms adapt on purpose because they need to.", "Changes during one lifetime are passed on.", "An adaptation is helpful in every environment.", "Rhymes reliably identify venomous snakes."],
 "support": ["Provide a three-column sorting chart.", "Use pictures of Florida animals for classifying.", "Demonstrate one beak test first."],
 "challenge": ["Research why the Florida scrub-jay lives only in Florida scrub and is adapted to fire.", "Compare Darwin's finch beaks with the beak buffet results."],
 "background": "<p>Gopher tortoise burrows average about 15 feet long and can exceed 40 feet; more than 350 commensal species are documented (FWC). Viceroy and monarch mimicry is now understood as mutual (Müllerian) mimicry, since both are distasteful. Scarlet kingsnakes resemble eastern coral snakes; KCE avoids teaching color rhymes as a safety rule because they vary by region and pattern. Florida places these benchmarks in Grade 7 (SC.7.L.15.x); KCE teaches them here per the Grade 6 scope.</p>",
 "sources": ["Florida Fish and Wildlife Conservation Commission, Gopher Tortoise; Roseate Spoonbill.", "University of Florida IFAS Extension, Florida's Fire-Adapted Ecosystems.", "Smithsonian Ocean, Mangroves."]
}

PRINT = {
 "directions": "Answer in complete sentences.",
 "items": [
  {"q":"Define adaptation and give one structural, one behavioral and one physiological example.","a":"An inherited trait that helps survival and reproduction; spoonbill bill; manatees moving to springs; black mangroves pushing out salt through their leaves.","lines":3},
  {"q":"How are red mangroves adapted to salty coastal water?","a":"Prop roots hold them up in water and bring in air; their roots filter out most of the salt.","lines":2},
  {"q":"Explain mimicry with an example.","a":"Looking like another species; a scarlet kingsnake resembles a venomous coral snake, so predators avoid it.","lines":2},
  {"q":"Why is a raccoon's learned trash-can skill not an adaptation?","a":"It's learned in one lifetime, not inherited.","lines":2},
  {"q":"Why do Florida land managers use controlled burns?","a":"Many Florida plants and animals are adapted to fire, which clears competitors and keeps the ecosystem healthy.","lines":2}]
}
