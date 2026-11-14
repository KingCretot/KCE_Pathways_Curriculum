def cell():
    s = ('<svg viewBox="0 0 560 330" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Diagram of an animal cell">'
         '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">An animal cell (simplified)</text>'
         '<ellipse cx="250" cy="175" rx="185" ry="140" fill="#fde8d0" stroke="#DB2F30" stroke-width="4"/>'
         '<circle cx="245" cy="170" r="48" fill="#c9b6e4" stroke="#5a3d8a" stroke-width="3"/><circle cx="255" cy="165" r="15" fill="#5a3d8a"/>'
         '<path d="M300 130 q20 -8 30 6 q-20 4 -30 -6 M305 150 q25 -6 36 10 q-24 2 -36 -10 M302 172 q28 -2 38 14 q-26 0 -38 -14" fill="none" stroke="#2f6b8a" stroke-width="3"/>'
         '<path d="M140 120 q30 -12 50 0 M138 132 q32 -12 54 0 M140 144 q30 -12 50 0" fill="none" stroke="#C9A84C" stroke-width="4"/>'
         + ''.join(f'<ellipse cx="{x}" cy="{y}" rx="22" ry="11" fill="#e59b3a" stroke="#8a5a12" stroke-width="2" transform="rotate({r} {x} {y})"/><path d="M{x-14} {y} q5 -6 9 0 q5 6 9 0 q5 -6 9 0" fill="none" stroke="#8a5a12" stroke-width="1.5" transform="rotate({r} {x} {y})"/>' for x, y, r in [(170, 230, 20), (330, 240, -15), (300, 90, 10)]) +
         ''.join(f'<circle cx="{x}" cy="{y}" r="3" fill="#0A1F3D"/>' for x, y in [(190, 200), (205, 215), (222, 250), (280, 245), (300, 215), (318, 205), (200, 100), (330, 110), (150, 175)]) +
         '<circle cx="380" cy="190" r="13" fill="#7fb06a" stroke="#2e7d32" stroke-width="2"/><circle cx="130" cy="210" r="10" fill="#bcd9ef" stroke="#0047BA" stroke-width="2"/>')
    tg = [(250, 36, "Cell membrane: controls what enters and leaves"), (245, 124, "Nucleus: holds DNA, the control center"), (190, 128, "Endoplasmic reticulum: transport network"),
          (330, 150, "Golgi apparatus: packages and ships"), (258, 165, "Nucleolus: makes ribosomes"), (380, 190, "Lysosome: breaks down waste"), (318, 205, "Ribosomes: build proteins"),
          (130, 210, "Vacuole: stores water and materials"), (330, 240, "Mitochondria: release energy from food"), (200, 290, "Cytoplasm: jelly-like fluid that fills the cell")]
    labels = [(x, y, 455, 40 + k * 30, t) for k, (x, y, t) in enumerate(tg)]
    for x1, y1, x2, y2, t in labels:
        s += f'<path d="M{x1} {y1} L{x2-4} {y2-4}" stroke="#8a8f99" stroke-width=".8"/><text x="{x2}" y="{y2}" font-size="10">{t}</text>'
    return s.replace('viewBox="0 0 560 330"', 'viewBox="0 0 700 330"') + '</svg>'

FACTORY = ('<svg viewBox="0 0 560 170" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="How a protein is made and shipped">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">From instructions to delivery: how a cell makes a protein</text>'
  + ''.join(f'<rect x="{10+i*112}" y="40" width="98" height="80" rx="10" fill="{c}"/><text x="{59+i*112}" y="66" text-anchor="middle" fill="#fff" font-weight="bold">{a}</text><text x="{59+i*112}" y="84" text-anchor="middle" fill="#fff">{b}</text><text x="{59+i*112}" y="100" text-anchor="middle" fill="#fff">{d}</text>'
            + (f'<path d="M{108+i*112} 80 h12" stroke="#0A1F3D" stroke-width="2"/><path d="M{120+i*112} 80 l-6 -4 v8z" fill="#0A1F3D"/>' if i < 4 else '')
            for i, (a, b, d, c) in enumerate([("Nucleus", "DNA holds the", "instructions", "#5a3d8a"), ("Ribosome", "reads the copy,", "builds protein", "#0A1F3D"), ("ER", "carries it", "through the cell", "#C9A84C"), ("Golgi", "packages and", "labels it", "#2f6b8a"), ("Membrane", "ships it out", "of the cell", "#DB2F30")])) +
  '<text x="280" y="148" text-anchor="middle">Mitochondria power every step by releasing energy from food.</text></svg>')

def sizes():
    s = ('<svg viewBox="0 0 560 160" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Different shapes of human cells">'
         '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Shape fits the job: three human cells</text>'
         '<circle cx="90" cy="80" r="34" fill="#DB2F30"/><circle cx="90" cy="80" r="16" fill="#b51e1e"/><text x="90" y="134" text-anchor="middle" font-weight="bold">Red blood cell</text><text x="90" y="148" text-anchor="middle">squeezes through tiny vessels</text>'
         '<circle cx="280" cy="80" r="14" fill="#c9b6e4" stroke="#5a3d8a" stroke-width="2"/>'
         + ''.join(f'<path d="M280 80 L{280+dx} {80+dy}" stroke="#5a3d8a" stroke-width="3"/>' for dx, dy in [(-60, -30), (-50, 30), (40, -40), (90, 10), (30, 40)]) +
         '<text x="280" y="134" text-anchor="middle" font-weight="bold">Nerve cell</text><text x="280" y="148" text-anchor="middle">long branches carry signals</text>'
         '<rect x="420" y="60" width="110" height="36" rx="18" fill="#e59b3a"/><circle cx="450" cy="78" r="5" fill="#8a5a12"/><circle cx="500" cy="78" r="5" fill="#8a5a12"/>'
         '<text x="475" y="134" text-anchor="middle" font-weight="bold">Muscle cell</text><text x="475" y="148" text-anchor="middle">long and able to contract</text></svg>')
    return s

LESSON = {
 "unit": "Unit 2: Cells, the Building Blocks of Life",
 "title": "Inside an Animal Cell",
 "subtitle": "A single cell is busier than a city. Every part has a job, and every job keeps you alive.",
 "objectives": [
  "Identify the main parts of an animal cell and describe the job of each.",
  "Explain how organelles work together, such as in making and shipping a protein.",
  "Compare a cell to a system you know (a city, school or factory) and explain the limits of the comparison.",
  "Explain how a cell's shape relates to its job.",
  "Describe the story of Henrietta Lacks and the ethics of using human cells in research."],
 "vocab": [
  ["organelle", "A tiny structure inside a cell that does a specific job."],
  ["cell membrane", "The thin, flexible outer layer that controls what enters and leaves the cell."],
  ["cytoplasm", "The jelly-like fluid that fills the cell and holds the organelles."],
  ["nucleus", "The control center of the cell, which holds the DNA."],
  ["DNA", "The molecule that carries the instructions for building and running a living thing."],
  ["mitochondria", "Organelles that release energy from food for the cell to use (singular: mitochondrion)."],
  ["ribosome", "A tiny organelle that builds proteins."],
  ["protein", "A large molecule that does much of the work in cells, such as building structures and speeding up chemical reactions."]],
 "reconnect": {
  "title": "Week 6: cell theory and the microscope",
  "intro": "Today you zoom inside the cell. First, check last week's ideas.",
  "items": [
   {"t":"open","key":"rc_theory","q":"State the three parts of the cell theory.","min":15,"rows":2,"rubric":["Living things are made of cells","The cell is the basic unit of life","Cells come from existing cells"],"model":"All living things are made of cells, the cell is the basic unit of life, and all cells come from other cells."},
   {"t":"num","q":"What is the total magnification with a 10× eyepiece and a 40× objective?","a":400,"unit":"×","pts":2,"why":"10 × 40 = 400×."},
   {"t":"num","q":"A cell looks 8 mm wide at 400×. How wide is it really, in millimeters?","a":0.02,"unit":"mm","pts":3,"why":"8 ÷ 400 = 0.02 mm."},
   {"t":"text","q":"Which scientist showed the importance of the cell's outer surface in fertilization?","a":["ernest everett just","ernest just","just","e. e. just"],"show":"Ernest Everett Just","pts":2,"why":"Ernest Everett Just studied the cell surface of marine eggs at Woods Hole."}]},
 "hook": {
  "title": "A City Too Small to See",
  "visual": cell(),
  "html": "<p>Right now, inside each of your roughly 30 trillion cells, thousands of tasks are happening at once. Instructions are being read, proteins are being built and shipped, energy is being released from food, and waste is being broken down and recycled. A cell is a living system with many parts working together.</p><p>Scientists call these parts <b>organelles</b>, which means \"little organs.\" This week you learn what each one does and how they cooperate.</p><div class='callout'><b>Big idea:</b> Each organelle has a job, and the cell stays alive only when they all work together.</div>"},
 "learn": [
  {"title": "The Boundary and the Control Center",
   "html": "<p>The <b>cell membrane</b> is a thin, flexible layer that surrounds the cell. It lets some things in (like water, oxygen and food molecules) and keeps others out. Scientists say it is <i>selectively permeable</i>.</p><p>Inside, the <b>cytoplasm</b> is a jelly-like fluid that holds everything in place.</p><p>The <b>nucleus</b> is the control center. It holds <b>DNA</b>, the instructions for building and running the cell. Inside the nucleus, a dark spot called the <b>nucleolus</b> makes ribosomes.</p>",
   "checks": [
    {"t":"open","key":"membrane","q":"Explain why a cell needs a membrane that lets some things in but not others.","min":15,"rows":2,"rubric":["Needs to take in useful things (water, oxygen, food)","Needs to keep out harmful things and keep its contents in"],"model":"The cell needs to take in useful things like water, oxygen and food, but it must keep harmful things out and keep its own important parts from leaking away."},
    {"t":"text","q":"Which organelle holds the cell's DNA?","a":["nucleus","the nucleus"],"pts":2,"why":"The nucleus is the control center that holds DNA."},
    {"t":"open","key":"nucleus","q":"Why do scientists call the nucleus the control center of the cell? What would happen to a cell that lost its nucleus?","min":20,"rows":3,"rubric":["It holds DNA, the instructions for everything the cell does","Without it the cell could not make new proteins or divide, and would eventually die"],"model":"The nucleus holds the DNA, which has the instructions for everything the cell does. A cell that lost its nucleus could not make new proteins the way it normally does or divide to make new cells, so it would eventually stop working."}]},
  {"title": "The Workers: Making and Shipping Proteins",
   "visual": FACTORY,
   "html": "<p><b>Ribosomes</b> are tiny organelles that build proteins by following the instructions copied from DNA. Some float in the cytoplasm; many sit on the <b>endoplasmic reticulum (ER)</b>, a folded network of membranes that carries materials through the cell.</p><p>The <b>Golgi apparatus</b> receives proteins from the ER, packages them and sends them where they are needed, inside the cell or out through the membrane.</p><p><b>Mitochondria</b> release energy from food (sugar) so the cell can do all this work. Muscle cells, which work hard, have many mitochondria.</p><p><b>Lysosomes</b> break down waste and worn-out parts, and <b>vacuoles</b> store water and materials. Animal cells usually have several small vacuoles.</p>",
   "checks": [
    {"t":"open","key":"order","q":"Put these in the order a protein travels and describe each step: Golgi apparatus, ribosome, cell membrane, endoplasmic reticulum.","min":20,"rows":3,"rubric":["Ribosome builds it","ER carries it","Golgi packages it","Membrane ships it out"],"model":"First the ribosome builds the protein, then the endoplasmic reticulum carries it through the cell, then the Golgi apparatus packages and labels it, and finally it leaves through the cell membrane."},
    {"t":"text","q":"Which organelle releases energy from food for the cell?","a":["mitochondria","mitochondrion","the mitochondria"],"show":"mitochondria","pts":2,"why":"Mitochondria release energy from food."},
    {"t":"open","key":"muscle","q":"Heart muscle cells contain far more mitochondria than skin cells. Explain why, using what you know about each cell's job.","min":20,"rows":3,"rubric":["Heart muscle works constantly and needs lots of energy","Mitochondria release energy, so more mitochondria supply more energy"],"model":"Heart muscle cells contract every second of your life, so they need a huge amount of energy. Mitochondria release energy from food, so having more of them gives heart cells the energy they need. Skin cells do less work, so they need fewer."}]},
  {"title": "Models, Analogies and Their Limits",
   "visual": sizes(),
   "html": "<p>An <b>analogy</b> compares something new to something familiar. Many people compare a cell to a city: the nucleus is city hall, ribosomes are factories, the ER is the road system, the Golgi is the post office, mitochondria are power plants, lysosomes are recycling centers and the membrane is the city border with checkpoints.</p><p>Analogies help, but like all models (Week 4), they have limits. A city does not divide into two new cities, and a power plant makes electricity, not the chemical energy a cell uses.</p><p>Cells also come in many shapes, because <b>shape fits the job</b>. Red blood cells are smooth disks that squeeze through tiny blood vessels; nerve cells have long branches to carry signals; muscle cells are long and can shorten (contract).</p>",
   "checks": [
    {"t":"open","key":"analogy","q":"Create your own analogy comparing a cell to a school. Match at least four organelles to parts of a school, and explain one way your analogy does not fit.","min":40,"rows":4,"rubric":["Four sensible matches with reasons","Names a real limit of the analogy"],"model":"The nucleus is the principal's office with the plans, ribosomes are the classrooms where things are made, the Golgi is the front office that sends things out, and the cell membrane is the front door with a guard. One way it does not fit: a school cannot split into two identical schools, but a cell can divide."},
    {"t":"text","q":"Which kind of cell has long branches to carry signals through the body?","a":[{"all":[["nerve","neuron"]]}],"show":"nerve cell (neuron)","pts":2,"why":"Nerve cells have long branches to carry signals."},
    {"t":"open","key":"rbc","q":"Mature human red blood cells have no nucleus. Use the idea that shape fits the job to explain why that might help them.","min":20,"rows":3,"rubric":["Without a nucleus there is more room for hemoglobin to carry oxygen","Allows a flexible disk shape to squeeze through narrow vessels"],"model":"Without a nucleus, a red blood cell has more room to carry oxygen, and it can be a flexible, flat disk that bends to squeeze through the narrowest blood vessels."}]},
  {"title": "Spotlight: Henrietta Lacks and HeLa Cells",
   "html": "<p>In 1951, <b>Henrietta Lacks</b>, a 31-year-old Black mother of five from Virginia and Maryland, was treated for cervical cancer at Johns Hopkins Hospital in Baltimore. Doctors took a sample of her cancer cells without her knowledge or permission, which was common then. Her cells, later called <b>HeLa cells</b>, did something no human cells had done before in a lab: they kept dividing, again and again.</p><p>HeLa cells helped scientists test the polio vaccine, study cancer and viruses, and make many other discoveries that have saved lives around the world. Yet for decades her family did not know her cells were being used or sold. Her story led to important conversations about <b>consent</b> (permission), privacy and fairness in science. In 2023, her family reached a settlement with a company that had profited from her cells.</p>",
   "checks": [
    {"t":"open","key":"lacks","q":"Henrietta Lacks's cells led to life-saving discoveries, but they were taken without her permission. Why does consent matter in science, even when the research helps many people?","min":35,"rows":4,"rubric":["People have the right to decide what happens to their own bodies and information","Respect, trust and fairness (including sharing benefits)","Recognizes both the benefits and the wrong done"],"model":"Consent matters because every person has the right to decide what happens to their own body and cells. Even though HeLa cells helped create vaccines and treatments, taking them without asking was wrong. When scientists ask permission and treat people fairly, people can trust science, and families are not left out of the benefits."}]}],
 "handson": {
  "title": "Walk Through the Cell",
  "intro": "Turn your home into a giant animal cell and walk a protein through it.",
  "materials": ["Index cards or sheets of paper and a marker", "Tape", "A small toy or ball to be the protein", "A string or yarn to outline the cell membrane (optional)", "A family member to be a visitor"],
  "steps": [
   "Make a sign for each organelle: nucleus, ribosome, endoplasmic reticulum, Golgi apparatus, mitochondria, lysosome, vacuole and cell membrane.",
   "Choose a location in your home for each one. The front door could be the cell membrane; a desk with papers could be the nucleus.",
   "On each sign, write the organelle's job and a reason you chose that location.",
   "Carry the protein from the nucleus (instructions) to the ribosome, through the ER, to the Golgi and out the membrane. Explain each stop aloud to your visitor.",
   "Stop at the mitochondria between steps to show the energy needed. End at the lysosome to recycle a worn-out part."],
  "record": [
   {"t":"open","key":"walk","q":"List each organelle, the home location you chose, its job and why the location fits.","min":60,"rows":8,"rubric":["All eight organelles","Correct jobs","Sensible reasons for locations"],"model":"Nucleus: my desk with the family calendar, because it holds the plans. Ribosome: the kitchen counter, where things are made. ER: the hallway, the path things travel. Golgi: the mail basket, where things are packaged to send. Mitochondria: the pantry, where the energy (food) is. Lysosome: the trash and recycling bin. Vacuole: the hall closet for storage. Cell membrane: the front door, which decides what comes in and out."},
   {"t":"open","key":"walk2","q":"What question did your visitor ask, and how did you answer it? What part of your model does not match a real cell?","min":25,"rows":3,"rubric":["Reports a question and an accurate answer","Names a real limit of the model"],"model":"My sister asked why the protein had to go to the Golgi. I explained the Golgi packages and labels proteins so they reach the right place. One limit: in a real cell all of this happens at the same time, millions of times, in a space far too small to see."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"breakdown","q":"Choose two organelles. For each, predict what would happen to a cell if that organelle stopped working, and explain why. Then explain why scientists say a cell is a system.","min":60,"rubric":["Two accurate predictions with reasons","Explains that parts depend on each other (system)"],"model":"If the mitochondria stopped working, the cell would run out of energy, and every other job would slow down and stop. If the lysosomes stopped working, waste and worn-out parts would pile up and damage the cell. A cell is a system because its parts depend on one another: the ribosomes need energy from mitochondria, and the Golgi needs proteins from the ER, so a problem in one part affects the whole cell."},
   {"t":"open","key":"ethics","q":"Today, many hospitals ask patients for permission before using leftover tissue in research. Write two rules you think scientists should follow when using human cells, and explain why each rule is fair.","min":45,"rubric":["Two clear rules (ask consent, explain how cells will be used, protect privacy, share benefits, let people say no)","Explains fairness for each"],"model":"Rule 1: Always ask permission and explain how the cells will be used, because people have the right to decide about their own bodies. Rule 2: Protect people's names and medical information, because their families deserve privacy, which Henrietta Lacks's family did not get for many years."}]},
 "exit": [
  {"t":"text","q":"Which organelle builds proteins?","a":["ribosome","ribosomes","the ribosome"],"show":"ribosome","pts":2,"why":"Ribosomes build proteins."},
  {"t":"text","q":"Which part controls what enters and leaves the cell?","a":["cell membrane","membrane","the cell membrane","plasma membrane"],"show":"cell membrane","pts":2,"why":"The cell membrane is selectively permeable."},
  {"t":"open","key":"exit_pair","q":"Explain how the ER and the Golgi apparatus work together.","min":12,"rows":2,"rubric":["ER carries proteins","Golgi packages and ships them"],"model":"The ER carries newly built proteins through the cell to the Golgi, which packages and labels them and sends them where they are needed."},
  {"t":"open","key":"exit_shape","q":"Give one example of how a cell's shape fits its job.","min":10,"rows":2,"rubric":["Accurate example (red blood cell disk, nerve cell branches, muscle cell length)"],"model":"Nerve cells have long branches so they can carry signals over long distances in the body."},
  {"t":"text","q":"What is the name of the cell line that came from Henrietta Lacks?","a":["hela","hela cells"],"show":"HeLa","pts":2,"why":"HeLa, from the first two letters of her first and last names."}],
 "next": "Week 8: plant cells and photosynthesis. What do plant cells have that animal cells do not?"
}

TEACHER = {
 "standards": [
  "SC.6.L.14.4: Compare and contrast the structure and function of major organelles of plant and animal cells, including cell wall, cell membrane, nucleus, cytoplasm, chloroplasts, mitochondria, and vacuoles.",
  "SC.6.L.14.3: Recognize and explore how cells of all organisms undergo similar processes to maintain homeostasis, including extracting energy from food, getting rid of waste, and reproducing.",
  "SC.6.N.3.4: Identify the role of models in the context of the sixth grade science benchmarks.",
  "SC.6.N.2.3: Recognize that scientists who make contributions to scientific knowledge come from all kinds of backgrounds and possess varied talents, interests, and goals.",
  "NGSS MS-LS1-2: Develop and use a model to describe the function of a cell as a whole and ways the parts of cells contribute to the function."],
 "materials": ["The interactive lesson", "Index cards, tape and a marker", "A small toy or ball", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 6 Reconnect questions."],
  [5, "Hook", "Show the cell diagram. Ask the student to guess the job of each part from its look."],
  [10, "Membrane and nucleus", "Discuss selective permeability and DNA as instructions."],
  [14, "Protein path", "Trace a protein from the nucleus to the membrane on the flow diagram. Discuss mitochondria and energy."],
  [10, "Analogies and shapes", "Build a cell-as-city analogy together, then name its limits. Compare cell shapes and jobs."],
  [10, "Henrietta Lacks", "Tell her story. Discuss consent and fairness respectfully."],
  [5, "Assign", "Assign the walk-through, Think Deeper and the Exit Check."]],
 "key_questions": ["What job does this organelle do, and what depends on it?", "How do organelles work together?", "Where does this analogy break down?", "Why does consent matter in science?"],
 "misconceptions": ["Thinking the cell membrane is a rigid wall (that is the plant cell wall, next week).", "Believing mitochondria make energy from nothing (they release energy stored in food).", "Thinking all cells look alike.", "Treating an analogy as an exact description."],
 "support": ["Provide a labeled diagram with a job card for each organelle.", "Use color coding: one color per organelle on the diagram and the walk-through signs.", "Focus first on five organelles: membrane, nucleus, cytoplasm, ribosome, mitochondria."],
 "challenge": ["Research why mitochondria have their own DNA and what that suggests about their origin.", "Read about the 2023 settlement in the Henrietta Lacks case and summarize what changed."],
 "background": "<p>Henrietta Lacks (1920 to 1951) was treated at Johns Hopkins in 1951; cells from her tumor were taken without her knowledge, as was common practice then, and became the first immortalized human cell line (HeLa). HeLa cells were used in testing the Salk polio vaccine and in countless research projects. In 2013 the National Institutes of Health reached an agreement with the Lacks family about access to her genome data, and in 2023 the family settled a lawsuit with Thermo Fisher Scientific. Handle the topic with respect; the focus is consent and fairness. Mature mammalian red blood cells lack a nucleus.</p>",
 "sources": ["Johns Hopkins Medicine: The Legacy of Henrietta Lacks.", "National Institutes of Health: HeLa cells and the Lacks family agreement (2013).", "OpenStax Biology 2e, Chapter 4: Cell Structure."]
}

PRINT = {
 "directions": "Use complete sentences.",
 "items": [
  {"q":"Match each organelle to its job: nucleus, mitochondria, ribosome, Golgi apparatus, lysosome, cell membrane.","a":"Nucleus: holds DNA, control center; mitochondria: release energy; ribosome: builds proteins; Golgi: packages and ships; lysosome: breaks down waste; cell membrane: controls what enters and leaves.","lines":3},
  {"q":"Describe the path of a protein from instructions to leaving the cell.","a":"Nucleus (DNA instructions) → ribosome (builds) → ER (carries) → Golgi (packages) → cell membrane (ships out).","lines":3},
  {"q":"Draw a simple animal cell and label five parts.","a":"Drawing with membrane, cytoplasm, nucleus, mitochondria and ribosomes labeled.","lines":5},
  {"q":"Why do muscle cells have many mitochondria?","a":"Muscles work hard and need lots of energy; mitochondria release energy from food.","lines":2},
  {"q":"Write one cell analogy and one way it does not fit.","a":"For example: the nucleus is like a principal's office; but a school cannot divide into two schools.","lines":2},
  {"q":"Why is the story of Henrietta Lacks important for science today?","a":"Her cells were taken without permission; it led to rules about consent, privacy and fairness in research.","lines":2}]
}
