PUNNETT = ('<svg viewBox="0 0 660 250" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="14" role="img" aria-label="A Punnett square crossing two pea plants that are both Pp for purple flowers: PP, Pp, Pp and pp, a 3 to 1 ratio">'
  '<text x="330" y="22" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">A Punnett square: Pp × Pp (purple flowers are dominant)</text>'
  '<text x="230" y="58" text-anchor="middle" fill="#0047BA" font-weight="bold">P</text><text x="310" y="58" text-anchor="middle" fill="#0047BA" font-weight="bold">p</text>'
  '<text x="170" y="108" text-anchor="middle" fill="#DB2F30" font-weight="bold">P</text><text x="170" y="188" text-anchor="middle" fill="#DB2F30" font-weight="bold">p</text>'
  '<text x="270" y="44" text-anchor="middle" fill="#0047BA" font-size="11">parent 1 alleles</text><text x="120" y="150" text-anchor="middle" fill="#DB2F30" font-size="11">parent 2</text><text x="120" y="164" text-anchor="middle" fill="#DB2F30" font-size="11">alleles</text>'
  + ''.join(f'<rect x="{x}" y="{y}" width="80" height="80" fill="{bg}" stroke="#0A1F3D" stroke-width="2"/><text x="{x+40}" y="{y+38}" text-anchor="middle" fill="#0A1F3D" font-weight="bold" font-size="18">{g}</text><text x="{x+40}" y="{y+58}" text-anchor="middle" fill="#5b6676" font-size="11">{ph}</text>'
            for x, y, g, ph, bg in [(190, 68, "PP", "purple", "#efe2f7"), (270, 68, "Pp", "purple", "#efe2f7"), (190, 148, "Pp", "purple", "#efe2f7"), (270, 148, "pp", "white", "#fff")]) +
  '<text x="400" y="100" fill="#0A1F3D">genotypes: 1 PP : 2 Pp : 1 pp</text><text x="400" y="128" fill="#0A1F3D">phenotypes: 3 purple : 1 white</text><text x="400" y="156" fill="#0A1F3D">chance of white: 1 in 4 = 25%</text>'
  '<text x="330" y="244" text-anchor="middle" fill="#5b6676" font-size="11">Each box is one equally likely outcome, not an exact count of offspring.</text></svg>')

LESSON = {
 "unit": "Unit 6: Heredity and Adaptation",
 "title": "Punnett Squares",
 "subtitle": "Last week you learned that each parent passes on one allele for each gene. This week you meet Gregor Mendel and his pea plants, learn to write genotypes and phenotypes, use Punnett squares to predict the chances of a trait, and see why a prediction about probability is not a promise.",
 "objectives": [
  "Explain how Mendel's pea plant experiments revealed dominant and recessive traits.",
  "Use genotype and phenotype, homozygous and heterozygous correctly.",
  "Complete Punnett squares for single-gene crosses and state outcomes as ratios, fractions and percents.",
  "Explain the difference between a predicted probability and actual results.",
  "Recognize that many traits involve more than one gene or incomplete dominance."],
 "vocab": [
  ["genotype", "The alleles an organism has for a gene, written with letters such as PP, Pp or pp."],
  ["phenotype", "The trait that actually shows, such as purple or white flowers."],
  ["homozygous", "Having two identical alleles for a gene (PP or pp)."],
  ["heterozygous", "Having two different alleles for a gene (Pp); also called a carrier for a recessive trait."],
  ["Punnett square", "A grid used to predict the possible genotypes of offspring from two parents."],
  ["probability", "The chance that an event will happen, written as a fraction, ratio or percent."]],
 "reconnect": {
  "title": "Week 26: Traits and inheritance",
  "intro": "Last week's ideas become this week's predictions.",
  "items": [
   {"t":"text","q":"What do we call the different forms of a gene?","a":[{"all":[["allele"]],"none":["not"]}],"show":"alleles","pts":2,"why":"Such as purple or white."},
   {"t":"num","q":"How many alleles for each gene does an offspring receive from each parent?","a":1,"pts":2,"why":"One from each parent, two in all."},
   {"t":"text","q":"An allele whose trait shows when at least one copy is present is called ___.","a":[{"all":[["dominant"]],"none":["not"]}],"show":"dominant","pts":2,"why":"A recessive trait needs two copies."},
   {"t":"open","key":"rc_beads","q":"In last week's bead babies, about what fraction of babies showed the recessive trait? Did every family get exactly the same result?","min":15,"rows":2,"rubric":["Reports a fraction near one-fourth","Notes that results varied by chance"],"model":"About one-fourth of my babies were dd. My results weren't exactly one-fourth, and other families got slightly different numbers because each draw was random."}]},
 "hook": {
  "title": "The Monk in the Garden",
  "visual": PUNNETT,
  "html": "<p>In the 1850s and 1860s, a monk named <b>Gregor Mendel</b> grew and studied about 28,000 pea plants in his monastery garden in Brno, in today's Czech Republic. He crossed tall plants with short ones and purple-flowered plants with white-flowered ones, and he counted the offspring carefully.</p><p>When he crossed two purple plants whose parents were purple and white, about three out of every four offspring were purple and one was white, again and again. Mendel realized that traits come in pairs of \"factors\" (we now call them alleles) and that some hide others. His work was ignored for 34 years before scientists rediscovered it in 1900. Today he is called the father of genetics.</p><div class='callout'><b>Big question:</b> How can we predict the traits offspring might inherit?</div>"},
 "learn": [
  {"title": "Genotype and Phenotype",
   "html": "<p>Scientists use letters for alleles: a capital letter for the dominant allele (P for purple) and the same letter lowercase for the recessive allele (p for white).</p><ul><li>The <b>genotype</b> is the pair of letters: PP, Pp or pp.</li><li>The <b>phenotype</b> is what shows: PP and Pp plants are purple; only pp is white.</li><li><b>Homozygous</b> means two identical alleles (PP or pp). <b>Heterozygous</b> means two different alleles (Pp); a heterozygous plant is a carrier of the hidden recessive allele.</li></ul>",
   "checks": [
    {"t":"blanks","q":"For pea flower color (P = purple, p = white), give the phenotype of each genotype.","sent":"PP: ___ &nbsp; Pp: ___ &nbsp; pp: ___","blanks":[[{"all":[["purple"]],"none":["not","white"]}],[{"all":[["purple"]],"none":["not","white"]}],[{"all":[["white"]],"none":["not","purple"]}]],"show":"purple; purple; white","pts":3,"why":"Only two recessive alleles show white."},
    {"t":"open","key":"samelook","q":"Two purple pea plants look exactly alike, but one is PP and one is Pp. How could a scientist find out which is which without a DNA test?","min":25,"rows":3,"rubric":["Cross each with a white (pp) plant or breed them","Explains that only the Pp plant can produce white offspring"],"model":"Cross each purple plant with a white (pp) plant. The PP plant can only pass on P, so all its offspring will be purple. The Pp plant can pass on p, so about half its offspring will be white."}]},
  {"title": "Making a Punnett Square",
   "html": "<p>A <b>Punnett square</b>, invented by Reginald Punnett in 1905, shows every possible combination of alleles:</p><ol><li>Write one parent's two alleles across the top and the other parent's down the side.</li><li>Fill each box with one letter from its column and one from its row (capital letter first).</li><li>Count the outcomes. Each box is one equally likely chance.</li></ol><p>For Pp × Pp: PP, Pp, Pp, pp. The <b>genotype ratio</b> is 1 PP : 2 Pp : 1 pp. The <b>phenotype ratio</b> is 3 purple : 1 white, so each offspring has a 1 in 4, or 25 percent, chance of being white.</p>",
   "checks": [
    {"t":"num","q":"Cross Pp × pp. How many of the four boxes have the genotype pp?","a":2,"pts":2,"why":"The pp parent always gives p; the Pp parent gives P or p, so two boxes are Pp and two are pp."},
    {"t":"num","q":"In the Pp × pp cross, what percent of offspring are expected to have white flowers?","a":50,"unit":"percent","pts":2,"why":"2 of 4 boxes are pp."},
    {"t":"num","q":"In a PP × pp cross, what percent of offspring are expected to be purple?","a":100,"unit":"percent","pts":2,"why":"Every box is Pp."}]},
  {"title": "Probability Is Not a Promise",
   "html": "<p>A Punnett square predicts <b>probability</b>, not exact results. If a Pp × Pp cross makes 4 seeds, they won't always be 3 purple and 1 white; all 4 could be purple. Each seed is a new chance, like flipping a coin.</p><p>That's why Mendel counted thousands of plants. With large numbers, results get close to the predicted ratio: in one experiment he counted 705 purple and 224 white flowers, very close to 3 : 1.</p>",
   "checks": [
    {"t":"num","q":"Mendel counted 705 purple and 224 white flowers. To the nearest tenth, how many purple flowers were there for each white one?","a":3.1,"tol":0.05,"pts":2,"why":"705 ÷ 224 ≈ 3.15, close to 3 : 1."},
    {"t":"open","key":"fourpuppies","q":"Two dogs, both carriers (Bb) of a recessive coat color, have 4 puppies. The Punnett square predicts 1 in 4 with the recessive color. Their litter has 2 puppies with the recessive color. Did the Punnett square make a mistake? Explain.","min":30,"rows":3,"rubric":["Says the Punnett square was not wrong","Explains probability for each puppy and small numbers"],"model":"No. The square gives each puppy a 1 in 4 chance, but each puppy is a separate chance, like a coin flip. In a small litter of 4, getting 2 is possible. With hundreds of puppies, the results would get close to one-fourth."}]},
  {"title": "Beyond Simple Dominance",
   "html": "<p>Mendel chose traits controlled by one gene with two alleles. Many traits are more complex:</p><ul><li><b>Incomplete dominance:</b> neither allele fully hides the other. Crossing red and white snapdragons gives pink offspring.</li><li><b>Codominance:</b> both alleles show fully, like a roan cow with red and white hairs, or human AB blood type.</li><li><b>Many genes:</b> height, skin color and eye color in humans are shaped by many genes plus the environment, which is why people show a smooth range of shades and heights instead of just two types.</li></ul>",
   "checks": [
    {"t":"text","q":"Red snapdragons crossed with white snapdragons produce pink flowers. What is this pattern called?","a":[{"all":[["incomplete"]],"none":["not"]}],"show":"incomplete dominance","pts":2,"why":"Neither allele fully hides the other."},
    {"t":"open","key":"manygenes","q":"Why do humans show a wide range of heights instead of just \"tall\" and \"short\" like Mendel's pea plants?","min":23,"rows":3,"rubric":["Height depends on many genes","Environment (nutrition, health) also affects it"],"model":"Human height depends on hundreds of genes, each adding a little, plus nutrition and health while growing. All those combinations make a smooth range instead of two types."}]}],
 "handson": {
  "title": "Coin-Toss Crosses",
  "intro": "Use coins as parents' alleles to test a Punnett square prediction, then combine data to see the law of large numbers.",
  "materials": ["Two coins", "Masking tape and a marker (to label the coins)", "Paper and pencil", "A family member", "A calculator for checking (optional)"],
  "steps": [
   "Label both sides of each coin with tape: one side P (purple) and the other p (white). Each coin is a Pp parent.",
   "Predict the results of 20 offspring using a Punnett square.",
   "Flip both coins at once 20 times. Record each genotype (PP, Pp or pp) and phenotype in a table.",
   "Flip 30 more times (50 total). Then combine your results with a family member's 50 for 100 offspring.",
   "Compare your 20, 50 and 100 results with the predicted 3 : 1 ratio and 25 percent white.",
   "Keep coins away from young children (choking hazard)."],
  "record": [
   {"t":"open","key":"coinrec","q":"Show your results for 20, 50 and 100 offspring (purple and white counts and percent white). How did the percent white compare with 25 percent as the number grew?","min":35,"rows":4,"rubric":["Results at all three sizes","Percent white calculated","A conclusion about larger samples"],"model":"20 flips: 17 purple, 3 white (15 percent white). 50 flips: 36 purple, 14 white (28 percent). 100 combined: 74 purple, 26 white (26 percent). The more offspring, the closer I got to 25 percent, just like Mendel counting thousands of plants."},
   {"t":"open","key":"coinmodel","q":"How is the coin model like real inheritance, and how is it different?","min":25,"rows":3,"rubric":["One way it matches (each parent gives one allele by chance)","One difference (real traits can involve many genes, real cells use meiosis, coins can't model environment)"],"model":"Like real inheritance, each parent gives one of two alleles by chance, just as each coin lands on one side. But real traits often involve many genes and the environment, and the coin can't show incomplete dominance or the actual process of making sex cells."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"breeder","q":"A dog breeder has a black Labrador (Bb) and a chocolate Labrador (bb). Black (B) is dominant. Draw the Punnett square in words, give the genotype and phenotype ratios, and explain what the breeder should tell a family hoping for a chocolate puppy.","min":50,"rows":5,"rubric":["Correct Punnett square","Correct ratios (1 Bb : 1 bb; 1 black : 1 chocolate)","Explains probability honestly to the family"],"model":"Across the top: B and b. Down the side: b and b. Boxes: Bb, Bb, bb, bb. Genotypes: 2 Bb : 2 bb (1 : 1). Phenotypes: 1 black : 1 chocolate. The breeder should say each puppy has a 50 percent chance of being chocolate, so a litter will probably include some chocolate puppies, but it isn't guaranteed."},
   {"t":"open","key":"mendelignored","q":"Mendel's work was ignored for 34 years. Suggest two reasons why, and explain what his story teaches about how science works.","min":44,"rows":4,"rubric":["Two plausible reasons","A lesson about science (evidence, communication, replication)"],"model":"He published in a little-read journal, and many scientists of his time didn't use math to study living things, so his counts and ratios seemed strange. His story shows that good ideas need evidence that others can repeat and communicate; when scientists repeated his results in 1900, the idea finally took hold."}]},
 "exit": [
  {"t":"text","q":"The trait that actually shows, such as white flowers, is the ___.","a":[{"all":[["phenotype"]],"none":["not"]}],"show":"phenotype","pts":2,"why":"The letters are the genotype."},
  {"t":"num","q":"In a Bb × Bb cross, what percent of offspring are expected to show the recessive trait?","a":25,"unit":"percent","pts":2,"why":"1 of 4 boxes is bb."},
  {"t":"num","q":"A plant's genotype for height is TT, Tt or tt. How many of these three genotypes are heterozygous?","a":1,"pts":2,"why":"Only Tt has two different alleles."},
  {"t":"open","key":"exit_prob","q":"Why doesn't a Punnett square tell you exactly how many offspring will have a trait?","min":10,"rows":2,"rubric":["Explains that it shows probability for each offspring"],"model":"It shows the chance for each offspring, and each one is a separate chance, so actual results vary, especially in small numbers."}],
 "next": "Week 28: adaptations."
}

TEACHER = {
 "standards": [
  "SC.7.L.16.2: Determine the probabilities for genotype and phenotype combinations using Punnett Squares and pedigrees.",
  "SC.7.L.16.1: Understand and explain that every organism requires a set of instructions that specifies its traits, that this hereditary information (DNA) contains genes located in the chromosomes of each cell, and that heredity is the passage of these instructions from one generation to another."],
 "materials": ["The interactive lesson", "Two coins, masking tape and a marker", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 26 warm-up questions."],
  [5, "Hook", "Mendel's garden."],
  [11, "Genotype and phenotype", "Notation; test cross to tell PP from Pp."],
  [13, "Punnett squares", "Pp × Pp, Pp × pp, PP × pp; ratios and percents."],
  [10, "Probability", "Mendel's 705 and 224; the four puppies."],
  [9, "Beyond simple dominance", "Snapdragons, roan cattle, many genes."],
  [6, "Assign", "Set up the coin crosses; assign Think Deeper and the Exit Check."]],
 "key_questions": ["What alleles can each parent pass on?", "What does each box stand for?", "Is this a genotype or a phenotype?", "Why didn't the results match the prediction exactly?"],
 "misconceptions": ["A Punnett square tells exactly how many offspring will have a trait.", "Dominant means more common.", "Heterozygous organisms show a mix of both traits (only in incomplete dominance).", "Every trait is controlled by one gene."],
 "support": ["Provide blank Punnett square templates.", "Color-code each parent's alleles.", "Use the coins before drawing squares."],
 "challenge": ["Predict the results of a cross involving two genes (a dihybrid cross) for pea seed shape and color.", "Research the inheritance of sickle cell trait and why carriers are protected against malaria."],
 "background": "<p>Mendel published in 1866 (Proceedings of the Natural History Society of Brünn); his work was rediscovered in 1900 by Hugo de Vries, Carl Correns and Erich von Tschermak. Flower color counts: 705 purple and 224 white in the F2 generation. Reginald Punnett introduced the square around 1905. Black (B) and chocolate (b) in Labradors also depend on a second gene (E/e) for yellow; the example assumes the dogs are not yellow. Florida places Punnett squares in Grade 7 (SC.7.L.16.2); KCE teaches them here per the Grade 6 scope.</p>",
 "sources": ["Learn.Genetics, University of Utah: Punnett Squares and Probability.", "Mendel, Gregor, Experiments on Plant Hybridization (1866), English translation by William Bateson (1901).", "National Human Genome Research Institute, Punnett Square."]
}

PRINT = {
 "directions": "Show your Punnett squares.",
 "items": [
  {"q":"Define genotype, phenotype, homozygous and heterozygous.","a":"Genotype: allele letters; phenotype: the trait shown; homozygous: two identical alleles; heterozygous: two different alleles.","lines":3},
  {"q":"Complete a Punnett square for Tt × Tt (T = tall). Give the genotype and phenotype ratios.","a":"TT, Tt, Tt, tt; 1 : 2 : 1; 3 tall : 1 short.","lines":3},
  {"q":"Complete a Punnett square for Tt × tt. What percent are expected to be short?","a":"Tt, Tt, tt, tt; 50 percent short.","lines":3},
  {"q":"Why did Mendel study thousands of plants?","a":"Large numbers get closer to the predicted ratio; small numbers vary by chance.","lines":2},
  {"q":"Give one example of a trait that doesn't follow simple dominance.","a":"Pink snapdragons (incomplete dominance), roan cattle or AB blood (codominance), human height (many genes).","lines":2}]
}
