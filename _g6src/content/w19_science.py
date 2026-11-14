GUT = ('<svg viewBox="0 0 640 300" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="The path of food through the digestive system">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The journey of a bite of food</text>'
  + ''.join(f'<g transform="translate({x},{y})"><rect width="180" height="52" rx="10" fill="{c}"/><text x="90" y="21" text-anchor="middle" fill="#fff" font-weight="bold">{n}. {a}</text><text x="90" y="39" text-anchor="middle" fill="#fff" font-size="10">{b}</text></g>'
            for n, (x, y, a, b, c) in enumerate([
              (20, 40, "Mouth", "teeth chew; saliva starts on starch", "#8a6d1f"),
              (230, 40, "Esophagus", "muscle waves push food down", "#a5552a"),
              (440, 40, "Stomach", "churns; acid and enzymes; 2 to 4 hours", "#DB2F30"),
              (440, 130, "Small intestine", "about 20 feet; nutrients absorbed", "#0047BA"),
              (230, 130, "Large intestine", "absorbs water; helpful bacteria", "#1d6fb8"),
              (20, 130, "Rectum", "stores waste until it leaves the body", "#5b6676")], 1)) +
  '<path d="M200 66 h30 M410 66 h30 M530 92 v38 M440 156 h-30 M230 156 h-30" stroke="#0A1F3D" stroke-width="3"/>'
  '<rect x="120" y="210" width="400" height="70" rx="10" fill="#f4ecd8" stroke="#8a6d1f"/><text x="320" y="232" text-anchor="middle" font-weight="bold" fill="#0A1F3D">Helpers food never passes through</text><text x="320" y="252" text-anchor="middle" font-size="11">liver (makes bile to break up fats), gallbladder (stores bile),</text><text x="320" y="268" text-anchor="middle" font-size="11">pancreas (makes enzymes and insulin)</text></svg>')

NEURON = ('<svg viewBox="0 0 640 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="A reflex arc: sensory neuron, spinal cord, motor neuron">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Touching a hot pan: a reflex arc</text>'
  '<rect x="270" y="40" width="100" height="150" rx="16" fill="#e6ecf3" stroke="#0047BA"/><text x="320" y="62" text-anchor="middle" font-weight="bold" fill="#0047BA">spinal</text><text x="320" y="78" text-anchor="middle" font-weight="bold" fill="#0047BA">cord</text>'
  '<circle cx="320" cy="120" r="10" fill="#C9A84C"/><text x="320" y="146" text-anchor="middle" font-size="10">interneuron</text>'
  '<path d="M60 90 Q180 70 310 116" fill="none" stroke="#DB2F30" stroke-width="4"/><text x="70" y="70" font-size="11" fill="#DB2F30">1. sensory neuron: "HOT!"</text>'
  '<path d="M330 124 Q460 170 580 150" fill="none" stroke="#0047BA" stroke-width="4"/><text x="430" y="196" font-size="11" fill="#0047BA">2. motor neuron: "pull away!"</text>'
  '<rect x="30" y="90" width="40" height="30" rx="6" fill="#5b6676"/><text x="50" y="135" text-anchor="middle" font-size="10">hand</text>'
  '<rect x="580" y="135" width="40" height="30" rx="6" fill="#DB2F30"/><text x="600" y="180" text-anchor="middle" font-size="10">arm muscle</text>'
  '<path d="M320 40 v-10" stroke="#5b6676" stroke-width="2"/><text x="380" y="40" font-size="11" fill="#5b6676">3. message also goes up to the brain:</text><text x="380" y="54" font-size="11" fill="#5b6676">you feel the pain a moment later</text>'
  '<text x="320" y="222" text-anchor="middle" font-size="10" fill="#5b6676">A reflex skips the brain to save time. Simplified diagram.</text></svg>')

LESSON = {
 "unit": "Unit 4: The Human Body",
 "title": "Digestive and Nervous Systems",
 "subtitle": "Your digestive system turns a sandwich into molecules your cells can use, and your nervous system sends signals faster than a race car to control everything you do. This week you follow a meal through your body, test your reaction time and see how these systems team up with the ones you already know.",
 "objectives": [
  "Trace the path of food through the digestive system and describe mechanical and chemical digestion.",
  "Explain how the small intestine's structure helps it absorb nutrients.",
  "Describe the parts of the nervous system (brain, spinal cord, nerves, neurons) and how signals travel.",
  "Explain the difference between voluntary actions and reflexes.",
  "Measure and analyze reaction time, and explain how the digestive and nervous systems interact with other systems to maintain homeostasis."],
 "vocab": [
  ["mechanical digestion", "Physically breaking food into smaller pieces, as by chewing or churning."],
  ["chemical digestion", "Using enzymes and acids to break food into molecules the body can absorb."],
  ["enzyme", "A protein that speeds up a chemical reaction, such as breaking down food."],
  ["villi", "Tiny fingerlike folds lining the small intestine that absorb nutrients."],
  ["neuron", "A nerve cell that carries electrical and chemical signals."],
  ["reflex", "A fast, automatic response that doesn't wait for the brain to decide."],
  ["central nervous system", "The brain and spinal cord."]],
 "reconnect": {
  "title": "Week 18: Circulatory and respiratory systems",
  "intro": "Nutrients from digestion ride in the blood you studied last week.",
  "items": [
   {"t":"text","q":"Which blood vessels have walls one cell thick so materials can pass in and out?","a":[{"all":[["capillar"]],"none":["not"]}],"show":"capillaries","pts":2,"why":"They also line the villi you'll meet today."},
   {"t":"text","q":"Tiny air sacs in the lungs give a huge surface area. What are they called?","a":[{"all":[["alveol"]],"none":["not"]}],"show":"alveoli","pts":2,"why":"Watch for another huge surface today."},
   {"t":"text","q":"During exercise, which body system detects rising carbon dioxide and speeds up your breathing?","a":[{"all":[["nervous"]],"none":["not"]}],"show":"the nervous system","pts":2,"why":"Today you study it in detail."},
   {"t":"open","key":"rc_glucose","q":"Last week you learned blood carries oxygen and sugar to cells. Where do you think the sugar comes from, and how does it get into the blood?","min":12,"rows":2,"rubric":["From food, broken down by digestion","Absorbed into the blood (through the intestine walls)"],"model":"It comes from the food we eat. Digestion breaks food down into sugar molecules, which pass through the intestine walls into the blood."}]},
 "hook": {
  "title": "The Doctor Who Watched Digestion Through a Hole",
  "html": "<p>In 1822, a fur trader named Alexis St. Martin was accidentally shot in the stomach at Fort Mackinac, Michigan. Army surgeon William Beaumont saved his life, but the wound healed with an opening, called a fistula, that led straight into his stomach. Over the next ten years, Beaumont lowered pieces of food on silk strings into St. Martin's stomach and took out samples of stomach juice, discovering that digestion is a chemical process driven by acid, not just grinding.</p><p>Today we ask hard questions about those experiments. St. Martin was poor, could not read or write, and signed a contract to serve as Beaumont's servant. Did he truly choose to be studied? Modern science requires <b>informed consent</b>: people must understand an experiment and freely agree to it.</p><div class='callout'><b>Big question:</b> How does your body break down food and control everything you do?</div>"},
 "learn": [
  {"title": "The Digestive Path",
   "visual": GUT,
   "html": "<p>Digestion has two kinds of work. <b>Mechanical digestion</b> breaks food into smaller pieces: your teeth chew, and your stomach's smooth muscle churns. <b>Chemical digestion</b> uses <b>enzymes</b> and acid to break food into molecules small enough to absorb: starches into sugars, proteins into amino acids, fats into fatty acids.</p><ul><li><b>Mouth:</b> teeth chew; saliva contains an enzyme that starts breaking down starch.</li><li><b>Esophagus:</b> waves of muscle contraction (peristalsis) push food to the stomach, even if you're upside down.</li><li><b>Stomach:</b> churns food with strong acid and enzymes that break down protein, for about 2 to 4 hours.</li><li><b>Small intestine:</b> bile from the liver and enzymes from the pancreas finish digestion; nutrients are absorbed into the blood.</li><li><b>Large intestine:</b> absorbs water; trillions of helpful bacteria live here.</li></ul>",
   "checks": [
    {"t":"blanks","q":"Mechanical or chemical?","sent":"Teeth grinding a carrot: ___ &nbsp; An enzyme in saliva breaking down starch: ___ &nbsp; The stomach churning: ___","blanks":[[{"all":[["mechanical"]],"none":["not"]}],[{"all":[["chemical"]],"none":["not"]}],[{"all":[["mechanical"]],"none":["not"]}]],"show":"mechanical; chemical; mechanical","pts":3,"why":"Mechanical changes size; chemical changes molecules."},
    {"t":"order","q":"Put the path of food in order.","items":["mouth","esophagus","stomach","small intestine","large intestine"],"pts":2,"why":"The liver and pancreas help but food never passes through them."},
    {"t":"open","key":"crackertest","q":"If you chew a plain cracker for a full minute without swallowing, it starts to taste slightly sweet. Explain why, using the vocabulary.","min":20,"rows":2,"rubric":["An enzyme in saliva breaks down starch","into sugar, which tastes sweet (chemical digestion)"],"model":"Saliva contains an enzyme that breaks the cracker's starch into sugar molecules. That's chemical digestion beginning in the mouth, and the sugar tastes sweet."}]},
  {"title": "Absorption: The Small Intestine",
   "html": "<p>Your small intestine is about 20 feet long, folded into your belly. Its inner wall is covered with millions of tiny fingerlike <b>villi</b>, and each villus is covered with even tinier microvilli. Inside every villus are capillaries. Digested nutrients pass through the thin walls of the villi into the blood, which carries them to every cell.</p><p>The folds, villi and microvilli give the small intestine an enormous surface for absorbing food, the same structure-function idea you saw in the alveoli of the lungs.</p>",
   "checks": [
    {"t":"text","q":"What are the tiny fingerlike folds that absorb nutrients in the small intestine called?","a":[{"all":[["villi","villus"]],"none":["not"]}],"show":"villi","pts":2,"why":"Each holds capillaries."},
    {"t":"open","key":"villialveoli","q":"Compare villi in the small intestine with alveoli in the lungs. How are their structures alike, and why?","min":30,"rows":3,"rubric":["Both create huge surface area and have thin walls next to capillaries","Because both exchange materials with the blood (nutrients; oxygen and carbon dioxide)"],"model":"Both villi and alveoli create a huge surface area with very thin walls wrapped in capillaries. That's because both have the job of moving materials into the blood: nutrients in the intestine, oxygen in the lungs."}]},
  {"title": "The Nervous System",
   "html": "<p>The nervous system is your body's communication network:</p><ul><li>The <b>central nervous system</b> is the brain and spinal cord. The brain has about 86 billion neurons.</li><li>The <b>peripheral nervous system</b> is the network of nerves that reaches every part of your body.</li></ul><p>A <b>neuron</b> has branches called dendrites that receive signals, a cell body, and a long axon that sends the signal on. Signals travel as electrical impulses, up to about 268 miles per hour in some neurons, and pass to the next cell with chemicals that cross a tiny gap called a synapse.</p><p>Different parts of the brain have different jobs: the <b>cerebrum</b> handles thinking, memory, senses and voluntary movement; the <b>cerebellum</b> controls balance and coordination; the <b>brain stem</b> runs automatic functions such as breathing and heart rate.</p><p>Dr. <b>Alexa Canady</b> became the first Black woman neurosurgeon in the United States in 1981 and later led pediatric neurosurgery at Children's Hospital of Michigan, operating on children's brains and spinal cords.</p>",
   "checks": [
    {"t":"text","q":"Which part of the brain controls balance and coordination?","a":[{"all":[["cerebellum"]],"none":["not","cerebrum "]}],"show":"the cerebellum","pts":2,"why":"The cerebrum handles thinking and voluntary movement."},
    {"t":"text","q":"What is the tiny gap between two neurons called?","a":[{"all":[["synapse"]],"none":["not"]}],"show":"a synapse","pts":2,"why":"Chemical messengers cross it."},
    {"t":"open","key":"brainstem","q":"Why is it important that the brain stem controls breathing and heartbeat automatically, instead of the cerebrum controlling them on purpose?","min":20,"rows":2,"rubric":["You'd have to remember to breathe and beat your heart every moment, even while asleep","Automatic control keeps you alive without thinking (homeostasis)"],"model":"If you had to choose to breathe and make your heart beat, you'd die the moment you fell asleep or got distracted. Automatic control from the brain stem keeps these vital jobs going without thinking."}]},
  {"title": "Reflexes and Reaction Time",
   "visual": NEURON,
   "html": "<p>Most actions are <b>voluntary</b>: you decide to catch a ball, and signals travel from your eyes to your brain, then down the spinal cord to your muscles. That takes time, usually about a quarter of a second.</p><p>A <b>reflex</b> is faster. If you touch a hot pan, a sensory neuron sends a signal to the spinal cord, which immediately sends a signal back through a motor neuron to pull your hand away, before your brain has even registered the pain.</p><p>Systems work together: when you eat, your nervous system signals the stomach and intestines to move and release digestive juices, and later tells you when you feel full. Digestion provides the glucose your brain needs; the brain uses about 20 percent of your body's energy while making up only about 2 percent of its weight.</p>",
   "checks": [
    {"t":"text","q":"Pulling your hand off a hot pan before you feel pain is an example of a ___.","a":[{"all":[["reflex"]],"none":["not"]}],"show":"reflex","pts":2,"why":"The spinal cord responds before the brain decides."},
    {"t":"num","q":"In a ruler-drop test, the ruler fell 20 centimeters before Ana caught it, which equals a reaction time of about 0.20 seconds. Her brother caught it after 15 centimeters, about 0.17 seconds. How much faster was her brother, in seconds?","a":0.03,"tol":0.001,"unit":"seconds","pts":2,"why":"0.20 − 0.17 = 0.03 seconds."},
    {"t":"open","key":"reflexwhy","q":"Why does a reflex skip the brain? Explain how this helps keep you safe.","min":20,"rows":2,"rubric":["A shorter path (spinal cord only) is faster","Speed reduces injury, like a smaller burn"],"model":"Going only to the spinal cord and back is a much shorter path than going to the brain, so the response is faster. Pulling away a fraction of a second sooner means a smaller burn."}]}],
 "handson": {
  "title": "Digestion in a Bag and the Ruler-Drop Test",
  "intro": "Model mechanical and chemical digestion with a zipper bag, then measure your reaction time.",
  "materials": ["A gallon zipper bag", "4 plain crackers or a slice of bread", "1/2 cup water", "2 tablespoons vinegar (stands in for stomach acid)", "An old, clean pair of tights or a knee-high stocking and scissors (used by an adult)", "A bowl", "A 30-centimeter (12-inch) ruler", "A family member", "Paper and pencil"],
  "steps": [
   "Mouth: break the crackers into the bag (teeth). Add the water (saliva).",
   "Stomach: add the vinegar, seal the bag tightly, and squeeze and knead it for 2 minutes (churning). Notice the changes.",
   "Small intestine: an adult cuts the foot off the tights to make a tube. Hold it over the bowl and pour the mixture in. Gently squeeze the tube from top to bottom (peristalsis). The liquid that drips into the bowl stands for absorbed nutrients; what stays inside goes on to the large intestine.",
   "Ruler drop: your partner holds the ruler by the top, with the 0 mark between your open thumb and finger. Without warning, they let go; catch it as fast as you can. Record the centimeter mark. Do 5 trials with each hand.",
   "Use the chart to convert centimeters to seconds: 5 cm = 0.10 s, 10 cm = 0.14 s, 15 cm = 0.17 s, 20 cm = 0.20 s, 25 cm = 0.23 s, 30 cm = 0.25 s.",
   "Don't eat any of the model; throw it away and wash hands. Keep it away from pets."],
  "record": [
   {"t":"open","key":"bagrec","q":"Describe what happened at each step of the digestion model and which body part each step represents. Name one way the model is NOT like real digestion.","min":40,"rows":5,"rubric":["Describes mouth, stomach and intestine steps with matching body parts","Identifies mechanical and chemical parts","A limit (no real enzymes, no villi or blood, vinegar is weaker than stomach acid, much faster)"],"model":"Breaking crackers was chewing in the mouth, and the water was saliva. Squeezing the bag with vinegar was the stomach churning with acid; the crackers turned to mush. Squeezing the tights was peristalsis in the small intestine, and the liquid in the bowl was like absorbed nutrients. The model isn't like real digestion because there are no real enzymes, no villi or blood vessels, and real digestion takes hours."},
   {"t":"open","key":"rulerrec","q":"Record your 10 ruler-drop results, find the average for each hand, and convert to seconds. Was one hand faster? Did you improve with practice? Explain why using the nervous system.","min":40,"rows":5,"rubric":["Ten results and two correct averages","Converted to seconds with the chart","Compares hands and trials","Explains: signals travel eye → brain → spinal cord → muscle; practice and the dominant hand may speed it up"],"model":"Right hand: 14, 12, 15, 11, 13 cm, average 13 cm, about 0.16 seconds. Left hand: 18, 17, 16, 19, 15 cm, average 17 cm, about 0.19 seconds. My right (writing) hand was faster, and I got a little faster with practice. The signal goes from my eyes to my brain, down my spinal cord and to my hand muscles, and practice helps my brain respond faster."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"lunchsystems","q":"Trace what happens to the starch in a slice of bread from the moment you see it on your plate until its sugar reaches a muscle cell in your leg. Name at least four body systems and how they work together.","min":100,"rows":8,"rubric":["Nervous: seeing the food, signals to start digestion, controlling chewing and swallowing","Digestive: mechanical and chemical digestion of starch to sugar; absorption in villi","Circulatory: blood carries sugar to the leg","Respiratory (oxygen to use the sugar) or muscular (chewing, peristalsis)","Correct sequence"],"model":"My nervous system sees the bread and signals my mouth to make saliva. My muscular system helps me chew while saliva's enzyme starts breaking starch into sugar. Peristalsis pushes it down my esophagus, my stomach churns it, and in my small intestine enzymes finish turning the starch into sugar. The sugar passes through the villi into capillaries, where my circulatory system carries it to a muscle cell in my leg. My respiratory system brings in the oxygen the cell needs to release energy from that sugar."},
   {"t":"open","key":"beaumontethics","q":"William Beaumont's experiments on Alexis St. Martin taught the world how digestion works. Was it right for Beaumont to do these experiments? Consider what we learned and whether St. Martin truly chose to take part. Explain your position and acknowledge the other view.","min":80,"rows":6,"rubric":["A clear position","Uses facts: St. Martin's poverty, inability to read, servant contract; the scientific value","Discusses informed consent","Acknowledges the other view"],"model":"I think the experiments were wrong as they were done, even though they taught us a lot. St. Martin was poor, couldn't read, and signed a contract to be Beaumont's servant, so it's not clear he understood or freely agreed. Some people say the discoveries saved many lives and St. Martin did get medical care and pay. That's true, but scientific discoveries don't justify using someone who can't truly say no. That's why researchers today must get informed consent."}]},
 "exit": [
  {"t":"text","q":"Where are most nutrients absorbed into the blood?","a":[{"all":[["small intestine"]],"none":["not","large"]}],"show":"the small intestine","pts":2,"why":"Through the villi."},
  {"t":"text","q":"The brain and spinal cord together make up the ___ nervous system.","a":[{"all":[["central"]],"none":["not","peripheral"]}],"show":"central","pts":2,"why":"Nerves throughout the body are the peripheral nervous system."},
  {"t":"text","q":"What kind of protein speeds up the breakdown of food?","a":[{"all":[["enzyme"]],"none":["not"]}],"show":"an enzyme","pts":2,"why":"Saliva, the stomach and the pancreas all make enzymes."},
  {"t":"open","key":"exit_mechchem","q":"Explain the difference between mechanical and chemical digestion, with an example of each.","min":15,"rows":2,"rubric":["Mechanical: breaking into smaller pieces (chewing, churning)","Chemical: enzymes or acid changing food into smaller molecules (saliva on starch, stomach acid on protein)"],"model":"Mechanical digestion breaks food into smaller pieces, like chewing. Chemical digestion uses enzymes or acid to change food into new, smaller molecules, like saliva turning starch into sugar."}],
 "next": "Week 20: the Unit 4 checkpoint and body systems project."
}

TEACHER = {
 "standards": [
  "SC.6.L.14.5: Identify and investigate the general functions of the major systems of the human body (digestive, respiratory, circulatory, reproductive, excretory, immune, nervous, and musculoskeletal) and describe ways these systems interact with each other to maintain homeostasis.",
  "SC.6.N.1.1: Define a problem from the sixth grade curriculum, use appropriate reference materials to support scientific understanding, plan and carry out scientific investigation of various types, such as systematic observations or experiments, identify variables, collect and organize data, interpret data in charts, tables, and graphics, analyze information, make predictions, and defend conclusions.",
  "SC.6.N.3.4: Identify the role of models in the context of the sixth grade science benchmarks.",
  "SC.6.N.2.3: Recognize that scientists who make contributions to scientific knowledge come from all kinds of backgrounds and possess varied talents, interests, and goals."],
 "materials": ["The interactive lesson", "A gallon zipper bag, crackers, water, vinegar, old tights, scissors (adult), a bowl", "A 30-cm ruler", "Paper and pencil", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 18 warm-up questions."],
  [5, "Hook", "Beaumont and St. Martin; informed consent."],
  [12, "Digestive path", "Trace the diagram; mechanical versus chemical; the cracker test."],
  [8, "Absorption", "Villi and microvilli; compare with alveoli."],
  [12, "Nervous system", "CNS and PNS; the neuron; brain regions; Dr. Alexa Canady."],
  [11, "Reflexes", "Reflex arc diagram; reaction time; systems working together. Try one ruler drop."],
  [6, "Assign", "Assign digestion in a bag, the ruler-drop trials, Think Deeper and the Exit Check."]],
 "key_questions": ["Is this mechanical or chemical?", "How does this structure fit its function?", "Does this signal go to the brain or only to the spinal cord?", "Which systems are working together here?"],
 "misconceptions": ["Most digestion happens in the stomach (most chemical digestion and absorption happen in the small intestine).", "Food passes through the liver and pancreas.", "Nerves carry signals instantly.", "Reflexes are controlled by the brain."],
 "support": ["Label the digestive diagram together before the lesson.", "Act out a reflex arc with three people passing a message.", "Provide the reaction-time conversion chart."],
 "challenge": ["Research how helpful bacteria in the large intestine affect health.", "Graph reaction time against the number of practice trials and describe the trend."],
 "background": "<p>Beaumont's observations of St. Martin ran from 1825 to 1833 and were published in 1833. The small intestine is about 6 to 7 meters (20 to 23 feet) long in a living adult. Neuron estimates: about 86 billion (Azevedo et al., 2009). The fastest myelinated axons conduct at about 120 meters per second (about 268 miles per hour). The brain uses about 20 percent of resting energy. Alexa Canady completed her neurosurgery residency at the University of Minnesota in 1984 after becoming the first Black woman admitted to a U.S. neurosurgery residency (1981); she was chief of neurosurgery at Children's Hospital of Michigan from 1987 to 2001. Reaction-time chart: t = square root of (2d ÷ 9.8 m/s²), rounded.</p>",
 "sources": ["National Library of Medicine, William Beaumont and Alexis St. Martin.", "OpenStax, Anatomy and Physiology 2e, Chapters 12-14 and 23.", "National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK), Your Digestive System and How It Works.", "National Library of Medicine, Changing the Face of Medicine: Dr. Alexa Irene Canady."]
}

PRINT = {
 "directions": "Answer in complete sentences.",
 "items": [
  {"q":"List the organs food passes through, in order, and one job of each.","a":"Mouth (chew, saliva starts starch), esophagus (peristalsis), stomach (acid, churning), small intestine (finish digestion, absorb), large intestine (absorb water).","lines":3},
  {"q":"Compare mechanical and chemical digestion.","a":"Mechanical breaks food into smaller pieces; chemical uses enzymes and acid to make smaller molecules.","lines":2},
  {"q":"Explain how villi help the small intestine do its job.","a":"They create a huge surface area with thin walls and capillaries, so nutrients are absorbed quickly.","lines":2},
  {"q":"Name the three main parts of the brain and a job of each.","a":"Cerebrum (thinking, voluntary movement), cerebellum (balance, coordination), brain stem (breathing, heart rate).","lines":2},
  {"q":"Describe the path of a reflex signal when you touch something sharp.","a":"Sensory neuron to spinal cord to motor neuron to muscle; the brain is told afterward.","lines":2},
  {"q":"A ruler fell 25 cm in a reaction test. Use the chart to give the reaction time.","a":"About 0.23 seconds.","lines":1}]
}
