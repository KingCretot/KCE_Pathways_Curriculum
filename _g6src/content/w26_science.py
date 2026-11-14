DNA = ('<svg viewBox="0 0 660 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Zooming in from a cell to its nucleus, to a chromosome, to a gene on a DNA molecule">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">From cell to gene: where the instructions live</text>'
  '<circle cx="80" cy="115" r="58" fill="#fbf3df" stroke="#8a6d1f" stroke-width="2"/><circle cx="80" cy="115" r="22" fill="#C9A84C"/><text x="80" y="194" text-anchor="middle" fill="#0A1F3D" font-weight="bold">cell</text>'
  '<path d="M140 115 h30" stroke="#5b6676" stroke-width="2"/><path d="M164 109 l8 6 l-8 6" fill="none" stroke="#5b6676" stroke-width="2"/>'
  '<circle cx="230" cy="115" r="50" fill="#C9A84C" fill-opacity="0.5" stroke="#8a6d1f" stroke-width="2"/>'
  + ''.join(f'<path d="M{x} {y} q6 -12 12 0 q6 12 12 0" fill="none" stroke="#0047BA" stroke-width="3"/>' for x, y in [(200, 95), (225, 110), (205, 130), (235, 132), (215, 115)]) +
  '<text x="230" y="194" text-anchor="middle" fill="#0A1F3D" font-weight="bold">nucleus</text><text x="230" y="208" text-anchor="middle" fill="#5b6676" font-size="10">holds 46 chromosomes in a human</text>'
  '<path d="M290 115 h30" stroke="#5b6676" stroke-width="2"/><path d="M314 109 l8 6 l-8 6" fill="none" stroke="#5b6676" stroke-width="2"/>'
  '<path d="M350 60 q20 55 0 110 M380 60 q-20 55 0 110" fill="none" stroke="#0047BA" stroke-width="10" stroke-linecap="round"/><rect x="345" y="96" width="40" height="14" fill="#DB2F30"/>'
  '<text x="365" y="194" text-anchor="middle" fill="#0A1F3D" font-weight="bold">chromosome</text><text x="365" y="208" text-anchor="middle" fill="#5b6676" font-size="10">a long, coiled DNA molecule</text>'
  '<path d="M400 103 L450 80" stroke="#DB2F30" stroke-width="1.5" stroke-dasharray="4 3"/>'
  + ''.join(f'<path d="M{460+i*14} 60 C{467+i*14} 80 {467+i*14} 100 {460+i*14} 120" stroke="#2c6e22" stroke-width="2" fill="none"/>' for i in range(0)) +
  '<path d="M460 50 C520 80 520 130 600 160 M600 50 C540 80 540 130 460 160" fill="none" stroke="#2c6e22" stroke-width="3"/>'
  + ''.join(f'<path d="M{470+i*13} {60+i*11} H{590-i*13}" stroke="{c}" stroke-width="3"/>' for i, c in enumerate(["#DB2F30", "#0047BA", "#C9A84C", "#DB2F30", "#0047BA", "#C9A84C", "#DB2F30", "#0047BA"])) +
  '<rect x="455" y="88" width="150" height="40" fill="none" stroke="#DB2F30" stroke-width="2" stroke-dasharray="5 3"/><text x="530" y="194" text-anchor="middle" fill="#0A1F3D" font-weight="bold">gene</text><text x="530" y="208" text-anchor="middle" fill="#5b6676" font-size="10">a section of DNA that codes for a trait</text></svg>')

PEDIGREE = ('<svg viewBox="0 0 660 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="A three-generation family tree for the trait of attached earlobes; two parents with free earlobes have one child with attached earlobes">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">A pedigree: tracing a trait through a family</text>'
  '<rect x="210" y="40" width="34" height="34" fill="#fff" stroke="#0A1F3D" stroke-width="2"/><path d="M244 57 H396" stroke="#0A1F3D" stroke-width="2"/><circle cx="413" cy="57" r="17" fill="#fff" stroke="#0A1F3D" stroke-width="2"/>'
  '<path d="M320 57 V100 M170 100 H470 M170 100 V120 M320 100 V120 M470 100 V120" stroke="#0A1F3D" stroke-width="2" fill="none"/>'
  '<rect x="153" y="120" width="34" height="34" fill="#fff" stroke="#0A1F3D" stroke-width="2"/><circle cx="320" cy="137" r="17" fill="#0047BA" stroke="#0A1F3D" stroke-width="2"/><rect x="453" y="120" width="34" height="34" fill="#fff" stroke="#0A1F3D" stroke-width="2"/>'
  '<text x="227" y="92" text-anchor="middle" fill="#0A1F3D" font-size="11">Grandpa</text><text x="413" y="92" text-anchor="middle" fill="#0A1F3D" font-size="11">Grandma</text>'
  '<text x="170" y="172" text-anchor="middle" fill="#0A1F3D" font-size="11">son</text><text x="320" y="172" text-anchor="middle" fill="#0A1F3D" font-size="11">daughter</text><text x="470" y="172" text-anchor="middle" fill="#0A1F3D" font-size="11">son</text>'
  '<rect x="40" y="190" width="16" height="16" fill="#fff" stroke="#0A1F3D"/><text x="62" y="203" fill="#0A1F3D" font-size="11">square = male, circle = female</text>'
  '<circle cx="290" cy="198" r="8" fill="#0047BA"/><text x="304" y="203" fill="#0A1F3D" font-size="11">shaded = shows the trait</text><text x="460" y="203" fill="#5b6676" font-size="11">Practice data, not a real family.</text></svg>')

LESSON = {
 "unit": "Unit 6: Heredity and Adaptation",
 "title": "Traits and Inheritance",
 "subtitle": "Why do you have your grandmother's dimples but not her curly hair? In Week 7 you met DNA in the nucleus. This week you zoom in to chromosomes and genes, learn how traits pass from parents to offspring, tell inherited traits from learned ones, and see how the environment can shape how genes show up.",
 "objectives": [
  "Explain that DNA in chromosomes carries genes, the instructions for traits.",
  "Distinguish inherited traits from acquired (learned or environmental) traits.",
  "Explain that offspring get one copy of each gene from each parent in sexual reproduction, while asexual reproduction makes copies.",
  "Explain dominant and recessive alleles and why a trait can skip a generation.",
  "Interpret a pedigree and explain how the environment can affect how traits are expressed."],
 "vocab": [
  ["trait", "A characteristic of an organism, such as eye color, height or flower color."],
  ["heredity", "The passing of traits from parents to offspring."],
  ["chromosome", "A long, coiled strand of DNA inside the nucleus; humans have 46 (23 pairs)."],
  ["gene", "A section of DNA that carries the instructions for a trait."],
  ["allele", "One of the different forms of a gene, such as the form for brown eyes or blue eyes."],
  ["dominant", "An allele whose trait shows when at least one copy is present."],
  ["recessive", "An allele whose trait shows only when two copies are present."]],
 "reconnect": {
  "title": "Week 25: Ecosystems review",
  "intro": "Populations rise and fall. This unit asks why individuals in a population differ, and how differences are passed on.",
  "items": [
   {"t":"text","q":"What happened to green anoles' toe pads over about 20 generations after brown anoles arrived?","a":[{"all":[["larger","bigger","sticki"]],"none":["not","smaller"]}],"show":"they grew larger and stickier","pts":2,"why":"A trait that helped survival became more common."},
   {"t":"text","q":"In which part of a cell is DNA stored (Week 7)?","a":[{"all":[["nucleus"]],"none":["not"]}],"show":"the nucleus","pts":2,"why":"The control center."},
   {"t":"text","q":"What is the largest population an environment can support over time?","a":[{"all":[["carrying capacity"]],"none":["not"]}],"show":"carrying capacity","pts":2,"why":"Set by limiting factors."},
   {"t":"open","key":"rc_toepads","q":"The anoles' toe pads changed over generations, not within one lizard's life. What must be true about toe pad size for it to change across generations?","min":12,"rows":2,"rubric":["Toe pad size must be passed from parents to offspring (inherited)"],"model":"Toe pad size must be inherited, passed from parent lizards to their babies, so lizards that survived better passed bigger toe pads on."}]},
 "hook": {
  "title": "The Family Resemblance",
  "visual": DNA,
  "html": "<p>Look at photos of your family. Maybe you have your dad's nose and your aunt's laugh. Maybe your little brother has blue eyes though both parents have brown. How does that happen?</p><p>Every cell in your body (except red blood cells) carries a full set of instructions written in <b>DNA</b>, packed into <b>chromosomes</b> in the nucleus. Sections of that DNA, called <b>genes</b>, help build your traits. Half came from each parent. This week you learn how those instructions are passed on.</p><div class='callout'><b>Big question:</b> How are traits passed from parents to offspring, and why aren't siblings identical?</div>"},
 "learn": [
  {"title": "DNA, Chromosomes and Genes",
   "html": "<p>In Week 7 you learned that the nucleus holds <b>DNA</b>. Here's how it's organized:</p><ul><li><b>DNA</b> is a long molecule shaped like a twisted ladder (a double helix). Its \"rungs\" come in four chemical letters, abbreviated A, T, C and G, and their order is the code.</li><li>DNA is coiled tightly into <b>chromosomes</b>. Humans have 46 chromosomes in 23 pairs; one chromosome of each pair came from each parent. Dogs have 78; a fruit fly has 8.</li><li>A <b>gene</b> is a section of DNA with the instructions for making a protein, which helps produce a <b>trait</b>. Humans have about 20,000 genes.</li></ul><p>Rosalind Franklin's X-ray photograph of DNA, taken in 1952, gave James Watson and Francis Crick the key evidence they used to describe the double helix in 1953.</p>",
   "checks": [
    {"t":"order","q":"Order from largest to smallest.","items":["cell","nucleus","chromosome","gene"],"pts":2,"why":"Each is inside the one before it."},
    {"t":"num","q":"Humans have 46 chromosomes in each body cell. How many came from each parent?","a":23,"pts":2,"why":"One of each pair from each parent."},
    {"t":"open","key":"franklin","q":"Rosalind Franklin's photograph was used by Watson and Crick, but for many years she received little credit. Why does it matter to give credit to every scientist whose evidence leads to a discovery?","min":25,"rows":3,"rubric":["Explains fairness and accurate history","Connects to how science builds on evidence from many people"],"model":"Science builds on many people's evidence, and Franklin's photograph was key to discovering the double helix. Leaving her out gives a false history and can discourage people, especially women, who might think scientists like them don't count."}]},
  {"title": "Inherited and Acquired Traits",
   "html": "<p><b>Inherited traits</b> come from genes passed down from parents: eye color, blood type, the shape of a leaf, a dog's coat pattern. <b>Acquired traits</b> develop during an organism's life through experience or environment: a scar, the ability to ride a bike, speaking French, big muscles from exercise. Acquired traits are not passed on through genes; a weightlifter's baby isn't born strong.</p><p>Many traits are shaped by both. Height depends on many genes but also on nutrition. Hydrangeas carry genes for flower color, but soil chemistry decides whether the flowers bloom blue or pink. Flamingos are pink because of pigments in the shrimp and algae they eat.</p>",
   "checks": [
    {"t":"blanks","q":"Inherited or acquired?","sent":"Freckles: ___ &nbsp; Reading music: ___ &nbsp; A dog's ability to fetch a ball on command: ___","blanks":[[{"all":[["inherit"]],"none":["not","acquired"]}],[{"all":[["acquire","learn"]],"none":["not","inherit"]}],[{"all":[["acquire","learn"]],"none":["not","inherit"]}]],"show":"inherited; acquired; acquired","pts":3,"why":"Freckles come from genes; skills are learned."},
    {"t":"open","key":"flamingo","q":"A flamingo raised in a zoo on a diet without shrimp or algae turns pale. Is pink color an inherited trait, an acquired trait or both? Explain.","min":25,"rows":3,"rubric":["Concludes both (genes and environment interact)","Explains the role of genes and the role of diet"],"model":"Both. Flamingo genes give them the ability to store pigments in their feathers, but the pink color only appears if their diet contains those pigments. The environment decides how the inherited trait shows."}]},
  {"title": "Passing Genes On",
   "html": "<p>In <b>sexual reproduction</b>, each parent passes on half its chromosomes in a sex cell (egg or sperm). The offspring gets one copy of each gene from each parent, a new mix, which is why siblings (except identical twins) look different.</p><p>In <b>asexual reproduction</b>, one parent makes offspring with identical DNA: bacteria splitting, a strawberry plant sending out runners, a potato sprouting from an eye. Growers use this to copy plants they like: most Florida orange trees are grown by grafting buds from a chosen tree onto rootstock, so trees of one variety share the same DNA.</p><p>Different forms of a gene are called <b>alleles</b>. If an offspring gets two different alleles, a <b>dominant</b> allele's trait shows, and a <b>recessive</b> allele's trait is hidden. A recessive trait shows only with two recessive alleles, which is how two brown-eyed parents can have a blue-eyed child.</p>",
   "checks": [
    {"t":"text","q":"What kind of reproduction makes offspring with DNA identical to the parent?","a":[{"all":[["asexual"]],"none":["not"]}],"show":"asexual reproduction","pts":2,"why":"Like strawberry runners."},
    {"t":"open","key":"skipgen","q":"Use the words dominant and recessive to explain how two parents with free earlobes could have a child with attached earlobes (see the pedigree).","min":30,"rows":3,"rubric":["Each parent carries a hidden recessive allele","The child received the recessive allele from both parents"],"model":"Free earlobes are dominant in this example. Each parent has one dominant allele and one hidden recessive allele, so both show free earlobes. Their daughter got the recessive allele from both parents, so with two recessive alleles, her earlobes are attached."},
    {"t":"open","key":"siblings","q":"Explain why two siblings with the same parents can look quite different, but identical twins look almost the same.","min":25,"rows":3,"rubric":["Each sibling gets a different random mix of the parents' genes","Identical twins come from one fertilized egg, so they share the same DNA"],"model":"Each child gets a different random half of each parent's genes, so siblings get different mixes. Identical twins come from one fertilized egg that split in two, so they have the same DNA."}]},
  {"title": "Reading a Pedigree",
   "visual": PEDIGREE,
   "html": "<p>A <b>pedigree</b> is a family tree that tracks a trait. Squares are males, circles are females, a horizontal line connects parents, a vertical line leads to children, and a shaded shape shows the trait. Geneticists, doctors and animal breeders use pedigrees to see how a trait is inherited.</p><p>When two parents without a trait have a child with it, the trait must be recessive, and both parents must carry a hidden copy.</p>",
   "checks": [
    {"t":"num","q":"In the pedigree, how many people show the shaded trait?","a":1,"pts":2,"why":"Only the daughter."},
    {"t":"open","key":"pedigreereason","q":"Using the pedigree, explain how we know attached earlobes are recessive in this family.","min":17,"rows":2,"rubric":["Neither parent shows the trait, but a child does","So both parents must carry a hidden recessive allele"],"model":"Neither grandparent has attached earlobes, but their daughter does. The trait was hidden in both parents, so it must be recessive."}]}],
 "handson": {
  "title": "Trait Survey and Bead Babies",
  "intro": "Survey real inherited traits in your family, then model how alleles combine when parents pass them on.",
  "materials": ["Paper and pencil", "A mirror", "Two paper bags or cups", "Beads, buttons or paper squares in two colors (about 10 of each)", "A coin", "Family members (as many as are willing)"],
  "steps": [
   "Trait survey: check yourself and family members for these inherited traits: freckles (yes or no), dimples (yes or no), whether the earlobes hang free or are attached, and the hairline (straight or with a widow's peak). Record results in a table. (These traits are often taught as simple dominant and recessive traits, but real inheritance is usually more complex.)",
   "Bead babies: Parent bag A gets one dark bead (dominant allele, D) and one light bead (recessive, d). Parent bag B gets the same. Without looking, draw one bead from each bag: that's the baby's pair. Record it (DD, Dd or dd) and return the beads.",
   "Repeat 20 times. Count how many babies show the dominant trait (DD or Dd) and how many show the recessive trait (dd).",
   "Compare: what fraction of your 20 babies showed the recessive trait?",
   "Keep beads and buttons away from young children (choking hazard) and pets. Families with adopted children or donors may survey any willing group of people instead."],
  "record": [
   {"t":"open","key":"surveyrec","q":"Share your trait survey table. Did any trait show up in a child but not in either parent? What might explain it?","min":34,"rows":4,"rubric":["A completed table","An observation about patterns","An explanation using dominant and recessive alleles (or an honest note that no such case appeared)"],"model":"I surveyed six people. My mom and dad both have free earlobes, but I have attached earlobes, so they might both carry a recessive allele. My sister has dimples like my dad. Nobody in my family has a widow's peak."},
   {"t":"open","key":"beadrec","q":"Report your bead baby results: how many DD, Dd and dd? What fraction showed the recessive trait? Why might your results be different from another family's?","min":35,"rows":3,"rubric":["Counts for all three combinations","The recessive fraction","Explains that chance causes variation"],"model":"I got 6 DD, 9 Dd and 5 dd. So 5 of 20, or one-fourth, showed the recessive trait. Another family might get 3 or 7, because each draw is random chance; the more babies you make, the closer you get to one-fourth."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"giraffeneck","q":"A scientist in the 1800s claimed giraffes got long necks because each giraffe stretched to reach leaves and then passed its stretched neck to its babies. Use what you learned about acquired and inherited traits to explain what is wrong with this idea.","min":41,"rows":4,"rubric":["Stretching would be an acquired trait","Acquired traits are not passed on through genes","Neck length differences must be inherited"],"model":"A neck stretched during a giraffe's life would be an acquired trait, like a weightlifter's muscles, and acquired traits aren't passed through genes. Babies inherit genes for neck length from their parents. Next week's Punnett squares and the natural selection lesson will show how long necks really became common."},
   {"t":"open","key":"natureandnurture","q":"Choose one human trait that depends on both genes and environment (such as height, skin tone in the sun, or a talent). Explain how each one contributes, and why it matters not to judge people only by traits they were born with.","min":43,"rows":5,"rubric":["Accurate explanation of both contributions","A thoughtful reason about fairness"],"model":"Height depends on many genes from both parents, but good nutrition and sleep while growing also matter. Someone can be shorter because of genes or because they didn't have enough food as a child. That's one reason it's unfair to judge people by traits they were born with or couldn't control."}]},
 "exit": [
  {"t":"text","q":"A section of DNA that carries instructions for a trait is a ___.","a":[{"all":[["gene"]],"none":["not"]}],"show":"gene","pts":2,"why":"Humans have about 20,000."},
  {"t":"text","q":"Is speaking Spanish an inherited or an acquired trait?","a":["^acquired",{"all":[["acquire","learn"]],"none":["not acquired","not learned","inherit"]}],"show":"acquired","pts":2,"why":"Languages are learned."},
  {"t":"text","q":"An allele whose trait shows only when two copies are present is called ___.","a":[{"all":[["recessive"]],"none":["not"]}],"show":"recessive","pts":2,"why":"It can hide for generations."},
  {"t":"open","key":"exit_half","q":"Why does each child get exactly half of their chromosomes from each parent?","min":10,"rows":2,"rubric":["Each sex cell carries half the chromosomes","Together they make a full set"],"model":"Each egg and sperm carries 23 chromosomes, half a set, so together they make a full set of 46."}],
 "next": "Week 27: predicting traits with Punnett squares."
}

TEACHER = {
 "standards": [
  "SC.7.L.16.1: Understand and explain that every organism requires a set of instructions that specifies its traits, that this hereditary information (DNA) contains genes located in the chromosomes of each cell, and that heredity is the passage of these instructions from one generation to another.",
  "SC.7.L.16.3: Compare and contrast the general processes of sexual reproduction requiring meiosis and asexual reproduction requiring mitosis.",
  "SC.6.N.3.4: Identify the role of models in the context of the sixth grade science benchmarks."],
 "materials": ["The interactive lesson", "A mirror, two paper bags, about 20 beads or buttons in two colors, a coin", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 25 warm-up questions."],
  [4, "Hook", "Family resemblance; from cell to gene."],
  [11, "DNA, chromosomes, genes", "Order the levels; Rosalind Franklin."],
  [10, "Inherited and acquired", "Sort traits; genes and environment together."],
  [13, "Passing genes on", "Sexual and asexual; dominant and recessive."],
  [10, "Pedigrees", "Read the earlobe pedigree."],
  [6, "Assign", "Set up the trait survey and bead babies; assign Think Deeper and the Exit Check."]],
 "key_questions": ["Is this trait inherited, acquired or both?", "Where are the instructions stored?", "How can a trait skip a generation?", "Why aren't siblings identical?"],
 "misconceptions": ["Acquired traits can be inherited.", "Dominant traits are always the most common.", "Children are a blend of exactly half each parent's looks.", "Earlobes and dimples are always simple one-gene traits (they are more complex)."],
 "support": ["Use a nesting-dolls model for cell, nucleus, chromosome and gene.", "Provide a trait sorting chart.", "Act out the bead draw together first."],
 "challenge": ["Research how Gregor Mendel used pea plants to discover dominant and recessive traits (a preview of next week).", "Find out why some cats are calico and what it has to do with chromosomes."],
 "background": "<p>Family trait surveys can raise questions about adoption, donors or parentage. The lesson offers surveying any willing group instead; please steer the activity so no child feels singled out. Classic classroom traits (earlobes, dimples, widow's peak, tongue rolling) are not truly single-gene traits; the lesson flags this. Human genome estimates are about 19,000 to 20,000 protein-coding genes. Florida places heredity in Grade 7 (SC.7.L.16.x); KCE teaches it here per the Grade 6 scope.</p>",
 "sources": ["National Human Genome Research Institute, Talking Glossary of Genomic and Genetic Terms.", "Learn.Genetics, University of Utah: Heredity and Traits.", "Maddox, Brenda, Rosalind Franklin: The Dark Lady of DNA (2002)."]
}

PRINT = {
 "directions": "Answer in complete sentences.",
 "items": [
  {"q":"Explain the relationship among DNA, chromosomes and genes.","a":"DNA is coiled into chromosomes; a gene is a section of DNA that codes for a trait.","lines":2},
  {"q":"Give two inherited traits and two acquired traits.","a":"Inherited: eye color, blood type; acquired: a scar, riding a bike.","lines":2},
  {"q":"Compare sexual and asexual reproduction.","a":"Sexual: two parents, offspring get a mix of genes; asexual: one parent, identical offspring.","lines":3},
  {"q":"How can two brown-eyed parents have a blue-eyed child?","a":"Both carry a hidden recessive allele; the child received the recessive allele from each parent.","lines":2},
  {"q":"Give one example of the environment affecting how a trait shows.","a":"Hydrangea color depends on soil; flamingo color depends on diet; height depends on nutrition.","lines":2}]
}
