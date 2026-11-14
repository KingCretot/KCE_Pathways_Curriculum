def paw(x, y, r=0):
    toes = ''.join(f'<line x1="{x+bx}" y1="{y+by}" x2="{x+tx}" y2="{y+ty}" stroke="#5b4a36" stroke-width="3.6" stroke-linecap="round"/><circle cx="{x+tx}" cy="{y+ty}" r="2.6" fill="#5b4a36"/>'
                   for bx, by, tx, ty in [(-8, -6, -20, -18), (-4, -9, -9, -27), (1, -10, 3, -30), (6, -8, 15, -25), (9, -3, 23, -12)])
    return f'<g transform="rotate({r} {x} {y})"><path d="M{x-9} {y-4} Q{x} {y-12} {x+10} {y-3} Q{x+12} {y+10} {x} {y+12} Q{x-11} {y+10} {x-9} {y-4}Z" fill="#5b4a36"/>{toes}</g>'

GARDEN = ('<svg viewBox="0 0 520 260" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Muddy garden bed with tracks and a bitten tomato">'
          '<rect x="0" y="0" width="520" height="260" fill="#efe6d2"/><rect x="0" y="150" width="520" height="110" fill="#b9a079"/>'
          '<text x="10" y="20" font-weight="bold" fill="#0A1F3D" font-size="15">The garden bed on Saturday morning</text>'
          '<line x1="430" y1="150" x2="430" y2="40" stroke="#3d7a33" stroke-width="5"/><circle cx="410" cy="80" r="16" fill="#DB2F30"/><circle cx="452" cy="100" r="14" fill="#DB2F30"/>'
          '<path d="M446 160 a14 14 0 1 0 28 0 Z" fill="#DB2F30"/><path d="M455 152 q5 6 10 0" stroke="#efe6d2" stroke-width="5" fill="none"/>'
          '<text x="440" y="200" font-size="11">bitten tomato</text>'
          + ''.join(paw(60 + 70*i, 210 - (i % 2) * 22, 80) for i in range(5)) +
          '<text x="20" y="250" font-size="11" fill="#2a2a2a">tracks: about 7 cm long, five long toes, look like small hands</text>'
          '<rect x="300" y="10" width="110" height="26" fill="#fff" stroke="#5b6676"/><text x="355" y="28" text-anchor="middle" font-size="11">Rain stopped 2 a.m.</text></svg>')

TRACKS = ('<svg viewBox="0 0 520 210" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Raccoon track compared with dog track">'
  '<text x="260" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Compare the evidence</text>'
  '<rect x="10" y="30" width="240" height="170" rx="8" fill="#fff8e6" stroke="#C9A84C"/><rect x="270" y="30" width="240" height="170" rx="8" fill="#eef3fb" stroke="#0047BA"/>'
  + paw(130, 125, 0).replace('<g transform="rotate(0 130 125)">','<g transform="translate(130 125) scale(1.8) translate(-130 -125)">') +
  '<text x="130" y="190" text-anchor="middle" font-weight="bold">Raccoon: 5 long, finger-like toes</text>'
  '<ellipse cx="390" cy="135" rx="24" ry="20" fill="#5b4a36"/>'
  + ''.join(f'<ellipse cx="{390+dx}" cy="{98+dy}" rx="9" ry="11" fill="#5b4a36"/><path d="M{390+dx} {86+dy} l0 -9" stroke="#5b4a36" stroke-width="3"/>' for dx, dy in [(-27, 10), (-10, -2), (10, -2), (27, 10)]) +
  '<text x="390" y="190" text-anchor="middle" font-weight="bold">Dog: 4 round toes, claw marks</text></svg>')

TESTABLE = ('<svg viewBox="0 0 520 170" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Turning a question into a testable question">'
  '<rect x="10" y="20" width="190" height="130" rx="8" fill="#fde8e8" stroke="#DB2F30"/><text x="105" y="44" text-anchor="middle" font-weight="bold" fill="#DB2F30">NOT TESTABLE</text>'
  '<text x="105" y="80" text-anchor="middle">Is plant food good?</text><text x="105" y="104" text-anchor="middle" fill="#5b6676" font-size="12">"Good" cannot be measured.</text>'
  '<path d="M208 85 H262" stroke="#0A1F3D" stroke-width="3"/><path d="M262 85 l-10 -7 v14z" fill="#0A1F3D"/>'
  '<rect x="270" y="20" width="240" height="130" rx="8" fill="#eef3fb" stroke="#0047BA"/><text x="390" y="44" text-anchor="middle" font-weight="bold" fill="#0047BA">TESTABLE</text>'
  '<text x="390" y="70" text-anchor="middle">Does plant food change how tall</text><text x="390" y="88" text-anchor="middle">bean plants grow in 3 weeks?</text>'
  '<text x="390" y="114" text-anchor="middle" font-size="12"><tspan fill="#0047BA" font-weight="bold">Change:</tspan> plant food or none</text>'
  '<text x="390" y="134" text-anchor="middle" font-size="12"><tspan fill="#DB2F30" font-weight="bold">Measure:</tspan> height in cm</text></svg>')

CARDS = ('<svg viewBox="0 0 520 190" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Diagram of a colored card experiment with bees">'
  '<text x="260" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">A colored-card experiment like Turner\'s</text>'
  '<text x="130" y="44" text-anchor="middle" font-weight="bold">1. Training</text><rect x="95" y="58" width="70" height="70" fill="#0047BA"/><circle cx="130" cy="93" r="12" fill="#f2c94c" stroke="#8a6d1f"/><text x="130" y="148" text-anchor="middle">Honey always on blue</text>'
  '<text x="380" y="44" text-anchor="middle" font-weight="bold">2. Test (no honey anywhere)</text>'
  '<rect x="285" y="58" width="55" height="55" fill="#DB2F30"/><rect x="352" y="58" width="55" height="55" fill="#0047BA"/><rect x="419" y="58" width="55" height="55" fill="#2f7d32"/>'
  '<text x="380" y="135" text-anchor="middle">Where do the bees land?</text><text x="380" y="153" text-anchor="middle">If most land on blue, they learned the color.</text>'
  '<g fill="#0A1F3D"><ellipse cx="370" cy="78" rx="6" ry="4"/><ellipse cx="386" cy="92" rx="6" ry="4"/><ellipse cx="372" cy="100" rx="6" ry="4"/><ellipse cx="300" cy="96" rx="6" ry="4"/></g>'
  '<text x="260" y="182" text-anchor="middle" font-size="11" fill="#5b6676">Independent variable: card color. Dependent variable: where the bees land.</text></svg>')

LESSON = {
 "unit": "Unit 1: Thinking Like a Scientist",
 "title": "Observations, Inferences and Questions",
 "subtitle": "Science starts with paying close attention, and with knowing the difference between what you see and what you think it means.",
 "objectives": [
  "Tell the difference between an observation and an inference.",
  "Make qualitative and quantitative observations using your senses and tools.",
  "Make inferences that are supported by evidence, and recognize that more than one inference can fit the same evidence.",
  "Turn a question you wonder about into a testable scientific question.",
  "Describe how scientist Charles Henry Turner used careful observation to discover how insects learn."],
 "vocab": [
  ["observation", "Information gathered directly with your senses or with tools. Example: the leaf is 6 centimeters long."],
  ["inference", "An explanation or conclusion based on observations and what you already know. Example: an animal ate the leaf."],
  ["qualitative observation", "An observation that describes qualities, such as color, texture, smell or shape."],
  ["quantitative observation", "An observation that uses numbers or measurements."],
  ["evidence", "Observations and data that support an idea."],
  ["testable question", "A question that can be answered by doing an investigation and collecting data."],
  ["prior knowledge", "What you already know before you begin, which helps you make inferences."],
  ["hypothesis", "A testable prediction that explains what you expect to happen and why."]],
 "reconnect": {
  "title": "Science skills from Grade 5",
  "intro": "You already know a lot about how science works. Answer these to warm up the skills you will use all year.",
  "items": [
   {"t":"text","q":"What tool measures temperature?","a":["thermometer","a thermometer"],"pts":2,"why":"A thermometer measures temperature in degrees Celsius or Fahrenheit."},
   {"t":"text","q":"Scientists use the metric system. What is the basic metric unit of length?","a":["meter","meters","metre","metres","the meter","m"],"show":"meter","pts":2,"why":"The meter is the basic unit of length. Centimeters and kilometers are based on it."},
   {"t":"text","q":"What is the basic metric unit of mass?","a":["gram","grams","g","kilogram","kilograms","kg"],"show":"gram (scientists treat the kilogram as the official base unit)","pts":2,"why":"Mass is measured in grams and kilograms."},
   {"t":"text","q":"You want to measure the length of a leaf. Name the tool and the metric unit you would use. Answer like this: tool, unit.","a":[{"all":[["ruler","meter stick","meterstick","tape"],["cm","centimet","mm","millimet"]]}],"show":"a ruler, centimeters (or millimeters)","pts":3,"why":"A metric ruler measures small lengths in centimeters or millimeters."},
   {"t":"text","q":"In an experiment, what do we call the part you change on purpose?","a":["independent variable","the independent variable","variable","manipulated variable","test variable"],"show":"independent variable","pts":2,"why":"The independent variable is what you change. You will master variables in Week 2."},
   {"t":"text","q":"What tool makes small objects look larger so you can see details?","a":["magnifying glass","hand lens","magnifier","microscope","a magnifying glass","a hand lens"],"show":"hand lens (magnifying glass) or microscope","pts":2,"why":"A hand lens magnifies a little; a microscope magnifies much more. Microscopes return in Unit 2."}]},
 "hook": {
  "title": "Who Was in the Garden?",
  "visual": GARDEN,
  "html": "<p>The Okafor family homeschools outside Gainesville, Florida. On Saturday morning, Chidi found a tomato in the garden with a bite missing and tracks pressed into the wet mud. His little sister announced, \"A dog ate it!\"</p><p>Chidi is not so sure. Before deciding, a scientist would separate two things: <b>what we can actually see</b> and <b>what we think it means</b>.</p><div class='callout'><b>Big idea:</b> Observations are facts you gather. Inferences are explanations you build from them. Good scientists keep the two separate, so they can change their minds when new evidence appears.</div>"},
 "learn": [
  {"title": "Observations: What You Actually Notice",
   "html": "<p>An <b>observation</b> uses your senses (sight, hearing, touch, smell, and taste only when it is safe) or a tool such as a ruler, scale or thermometer.</p><table class='t'><tr><th>Qualitative (qualities)</th><th>Quantitative (numbers)</th></tr><tr><td>The tomato is red.</td><td>The tracks are about 7 centimeters long.</td></tr><tr><td>The mud is soft and wet.</td><td>There are 5 tracks in a line.</td></tr><tr><td>Each track shows long, thin toes.</td><td>Each track shows 5 toes.</td></tr></table><p>A tip: if you can measure it or count it, the observation becomes quantitative and more useful.</p>",
   "checks": [
    {"t":"text","q":"\"The tracks are about 7 centimeters long.\" Is this a <b>qualitative</b> or <b>quantitative</b> observation?","a":["quantitative"],"pts":2,"why":"It uses a measurement with a number, so it is quantitative."},
    {"t":"text","q":"\"The mud smells earthy.\" Qualitative or quantitative?","a":["qualitative"],"pts":2,"why":"It describes a quality (smell) with no number."},
    {"t":"text","q":"Change this qualitative observation into a quantitative one: <i>The tomato plant is tall.</i>","a":[{"all":[["0","1","2","3","4","5","6","7","8","9"],["cm","centimet","meter","metre","inch","feet","foot","ft"]]}],"show":"For example: The tomato plant is 110 centimeters tall.","pts":3,"why":"Adding a measurement with a unit makes it quantitative."},
    {"t":"num","q":"Look at the picture. How many tracks are in the mud?","a":5,"pts":2,"why":"Counting is a quantitative observation: 5 tracks."}]},
  {"title": "Inferences: What It Might Mean",
   "visual": TRACKS,
   "html": "<p>An <b>inference</b> is an explanation built from observations plus <b>prior knowledge</b>. Chidi knows that dog tracks are rounded with short toes and claw marks, while raccoon tracks have five long, finger-like toes and look like small human hands.</p><div class='example'><b>Observations:</b> five long, thin toes; tracks about 7 cm; a bite in a low-hanging tomato; the rain stopped at 2 a.m.<br><b>Inference:</b> A raccoon probably visited the garden after 2 a.m.<br><b>Why after 2 a.m.?</b> Tracks made during the rain would have been washed out or blurred.</div><p>Notice the word <b>probably</b>. An inference can be wrong. A neighbor's pet or a different animal is possible, and new evidence could change the inference. That is not a weakness of science. It is its greatest strength.</p>",
   "checks": [
    {"t":"text","q":"\"A raccoon ate the tomato.\" Is this an <b>observation</b> or an <b>inference</b>?","a":["inference"],"pts":2,"why":"Nobody saw a raccoon. It is an explanation built from the tracks and the bite."},
    {"t":"open","key":"oi_pair","q":"Look at the garden picture. Write one observation a scientist could <b>measure</b> and one <b>inference</b> that the observation supports.","min":15,"rows":3,"rubric":["Observation includes a number or measurement","Inference is an explanation, not a fact","Inference is supported by the observation"],"model":"Observation: the tracks are about 7 centimeters long. Inference: a small animal about the size of a raccoon made them."},
    {"t":"text","q":"Which observation is the best evidence that the visitor was <b>not</b> a dog?","a":[{"all":[["toe","finger","hand"]]}],"show":"The five long, finger-like toes (dog tracks have short, rounded toes).","pts":3,"why":"The shape of the toes matches a raccoon, not a dog."},
    {"t":"text","q":"What additional evidence could Chidi collect tonight to test his inference?","a":[{"all":[["camera","video","watch","photo","trail cam","flour","observe","stay up","record","check","track","trap","night"]]}],"show":"Set up a trail camera, or spread flour near the plant and check for fresh tracks.","pts":3,"why":"New observations, such as a camera recording, can support or reject the inference."}]},
  {"title": "Asking Testable Questions",
   "visual": TESTABLE,
   "html": "<p>Scientists turn wondering into investigating. A <b>testable question</b> can be answered by changing one thing and measuring what happens.</p><table class='t'><tr><th>Not testable</th><th>Testable</th></tr><tr><td>Do raccoons like tomatoes better than anything?</td><td>Do raccoons eat more red tomatoes or green tomatoes in one night?</td></tr><tr><td>Which flower is the prettiest?</td><td>Which flower color do bees visit most often in one hour?</td></tr><tr><td>Is plant food good?</td><td>Does adding plant food change how tall bean plants grow in three weeks?</td></tr></table><p>Testable questions usually name <b>what you will change</b> and <b>what you will measure</b>.</p>",
   "checks": [
    {"t":"text","q":"Is this question testable? <i>Which smells best: lemon, mint or lavender?</i> Type <b>yes</b> or <b>no</b>.","a":["no"],"pts":2,"why":"\"Best\" is an opinion. Nothing can be measured to settle it."},
    {"t":"text","q":"Is this question testable? <i>Does the temperature of water change how fast sugar dissolves?</i> Type yes or no.","a":["yes"],"pts":2,"why":"You can change the water temperature and measure the time it takes the sugar to dissolve."},
    {"t":"blanks","q":"In the sugar question, identify the parts.","sent":"What you change: ___. What you measure: ___.","blanks":[[{"all":[["temperature","temp","hot","warm","heat","cold"]]}],[{"all":[["time","fast","minutes","seconds","how long","speed","rate","dissolv"]]}]],"show":"water temperature / time for the sugar to dissolve","pts":3,"why":"The water temperature is changed; the dissolving time is measured."},
    {"t":"text","q":"Rewrite as a testable question: <i>Is sunlight good for plants?</i>","a":[{"all":[["sun","light"],["grow","height","tall","leaves","cm","measure","size"]]}],"show":"For example: Does the number of hours of sunlight change how tall bean plants grow in two weeks?","pts":3,"why":"A testable version names what you change (sunlight) and what you measure (growth)."}]},
  {"title": "Scientist Spotlight: Charles Henry Turner",
   "visual": CARDS,
   "html": "<p><b>Charles Henry Turner</b> (1867 to 1923) was an American zoologist who studied how insects behave and learn. In 1907 he became one of the first African Americans to earn a doctorate (PhD) from the University of Chicago. He spent the last 14 years of his career teaching at Sumner High School in St. Louis, Missouri, where he did not have a university laboratory, so he designed clever experiments with simple materials.</p><p>Many scientists of his time believed insects acted only on instinct, like tiny machines. Turner tested that idea. He set out dishes of honey on colored cards and gathered early evidence that <b>honeybees can learn to connect food with colors and patterns</b>. He showed that <b>insects can hear</b> and that ants could learn their way back to their nest. His careful observations helped prove that insects can learn.</p><div class='callout'>Turner faced racism that kept him out of university jobs, yet he published dozens of scientific papers. Notice how he worked: careful observations, a testable question, and evidence that changed what scientists believed.</div>",
   "checks": [
    {"t":"text","q":"What did many scientists believe about insects before Turner's experiments?","a":[{"all":[["instinct","machine","could not learn","can't learn","cannot learn","don't learn","not learn","think","dumb","smart","only react"]]}],"show":"That insects act only on instinct and cannot learn.","pts":3,"why":"Turner's evidence challenged the idea that insects only act on instinct."},
    {"t":"text","q":"Write Turner's honeybee investigation as a testable question.","a":[{"all":[["bee"],["color","colour","pattern"]]}],"show":"For example: Can honeybees learn to find food by the color of the card it is on?","pts":3,"why":"He changed the card color and observed where the bees went."},
    {"t":"num","q":"In what year did Turner earn his PhD from the University of Chicago?","a":1907,"pts":2,"why":"1907. He was one of the first African Americans to earn a doctorate from that university."}]}],
 "handson": {
  "title": "The Mystery Container",
  "intro": "Become a scientist who cannot see the answer. You will gather observations, build inferences, and then find out how close you got.",
  "materials": ["A shoebox or container with a lid (or a paper bag folded shut)", "A family member to secretly place one ordinary household object inside", "An identical empty container if you have one", "A kitchen scale (optional) and a ruler"],
  "steps": [
   "Ask a family member to put one object inside the container without letting you see it, and close it.",
   "Gather observations without opening it: shake it gently, tilt it slowly, listen, feel how the weight shifts. If you have a scale, weigh it and an identical empty container and subtract.",
   "Write at least 6 observations. Label each one QL (qualitative) or QN (quantitative).",
   "Write 2 different inferences about what the object might be, and the evidence for each.",
   "Write one more test you could do without opening the box. Do it if you can.",
   "Open the container. Compare the real object with your inferences."],
  "record": [
   {"t":"open","key":"mystery_obs","q":"List your 6 or more observations, each labeled QL or QN.","min":35,"rows":6},
   {"t":"open","key":"mystery_inf","q":"Write your 2 inferences with evidence, your extra test, and what the object turned out to be. Which observation helped most, and which one misled you?","min":45,"rows":6}]},
 "think": {
  "intro": "These questions ask you to reason like a scientist and explain your thinking.",
  "items": [
   {"t":"open","key":"footprints","model":"Inference 1: the large animal caught and carried off the small animal, because the small tracks stop where the sand is trampled. Inference 2: the small animal climbed onto the large animal or flew away, which would also end its tracks. Looking for drag marks, feathers or fur at the trampled spot would help decide.","q":"<b>The footprint puzzle.</b> Two sets of animal tracks, one large and one small, come toward each other across the wet sand from opposite directions. Where they meet, the sand is trampled and scattered. After that spot, only the large tracks continue. Write <b>two different inferences</b> about what happened, the evidence for each, and one observation that would help you decide between them.","min":46,"rows":7,"rubric":["Two different, reasonable inferences","Each inference is tied to specific observations","Separates observation from inference clearly","Names a new observation that could help decide between them"]},
   {"t":"open","key":"wonder","q":"Write one question you truly wonder about in your home, yard or neighborhood. Then rewrite it as a testable question, naming what you would change and what you would measure.","min":30,"rows":4,"rubric":["Original question from the student's own world","Rewritten question is testable","Names what is changed and what is measured"]}]},
 "exit": [
  {"t":"text","q":"\"The ice cube melted in 12 minutes.\" Observation or inference?","a":["observation"],"pts":2,"why":"It was measured directly."},
  {"t":"text","q":"\"The room must be warm because the ice melted fast.\" Observation or inference?","a":["inference"],"pts":2,"why":"It explains the observation using prior knowledge."},
  {"t":"text","q":"\"The leaf has 7 holes in it.\" Qualitative or quantitative?","a":["quantitative"],"pts":2,"why":"It uses a count."},
  {"t":"open","key":"backto_obs","q":"Turn this inference back into the observations that could support it: <i>The dog is hungry.</i> Write two observations.","min":12,"rows":3,"rubric":["Two observations someone could see or measure","Neither observation is itself an inference"],"model":"The dog is standing by its empty bowl. The dog has not eaten since 7 a.m., and it is whining."},
  {"t":"text","q":"Is this testable? <i>Does the height a ball is dropped from change how high it bounces?</i> Type yes or no.","a":["yes"],"pts":2,"why":"Change the drop height and measure the bounce height."},
  {"t":"text","q":"Why do scientists use the word <i>probably</i> when they state an inference?","a":[{"all":[["wrong","change","new evidence","not sure","not certain","not proven","know for sure","not a fact","isn't a fact","not seen","didn't see"]]}],"show":"Because an inference could be wrong and might change with new evidence.","pts":3,"why":"Inferences are explanations, not direct facts, so they stay open to new evidence."},
  {"t":"text","q":"Turner's experiments gave evidence that honeybees can learn to recognize what two things?","a":[{"all":[["color","colour","pattern"]]}],"show":"colors and patterns","pts":2,"why":"His colored-card experiments gave early evidence that bees learn colors and patterns. The German scientist Karl von Frisch later proved bee color vision in 1914."}],
 "next": "Week 2: designing a fair test. You will learn how scientists change one variable at a time so their results can be trusted."
}

TEACHER = {
 "standards": [
  "SC.6.N.1.1: Define a problem from the sixth grade curriculum, use appropriate reference materials to support scientific understanding, plan and carry out scientific investigation of various types, such as systematic observations or experiments, identify variables, collect and organize data, interpret data in charts, tables, and graphics, analyze information, make predictions, and defend conclusions.",
  "SC.6.N.1.4: Discuss, compare and negotiate methods used, results obtained and explanations among groups of students conducting the same investigation.",
  "SC.6.N.2.3: Recognize that scientists who make contributions to scientific knowledge come from all kinds of backgrounds and possess varied talents, interests and goals.",
  "SC.7.N.1.6 (preview): Explain that empirical evidence is the cumulative body of observations of a natural phenomenon on which scientific explanations are based.",
  "NGSS Science and Engineering Practices 1 and 7: asking questions; engaging in argument from evidence."],
 "materials": ["The interactive lesson", "A shoebox or bag and one hidden object (prepared by a family member before class if possible)", "Ruler and kitchen scale (optional)", "Printable practice page"],
 "flow": [
  [5, "Reconnect", "Run the Reconnect questions. Note whether the student already knows metric units; they matter in Week 3."],
  [8, "Hook: the garden", "Show the garden picture. Ask the student to say everything they notice for one minute without explaining anything. Write the list. Then ask for explanations and write them in a second column. Label the columns observations and inferences."],
  [12, "Observations and inferences", "Sort statements together. Push on why 'a raccoon ate it' is an inference. Introduce the word probably, and ask what new evidence would change the inference."],
  [10, "Testable questions", "Convert two not-testable questions together. Have the student name what is changed and what is measured in each."],
  [10, "Scientist spotlight", "Read about Charles Henry Turner together. Discuss: how did he do serious science without a university lab? How did evidence change what other scientists believed?"],
  [12, "Mystery container live", "If a container is ready, do the activity live: the student makes observations out loud while you record them, then infers before opening. Otherwise model with an object you hide on your side of the camera."],
  [3, "Assign", "Assign the Think Deeper questions, the Exit Check and the printable page."]],
 "key_questions": ["Did you see that, or are you thinking it?", "What else could explain the same evidence?", "What would make you change your mind?", "How could you turn that into a number?", "What would you change, and what would you measure?"],
 "misconceptions": ["Believing an inference is a guess. It must be based on evidence and prior knowledge.", "Believing there is only one correct inference for a set of observations.", "Thinking qualitative observations are less scientific; both types matter.", "Writing a question that names what is measured but not what is changed."],
 "support": ["Use a two-column chart labeled I SEE and I THINK for every statement.", "Give sentence frames: I observe... This makes me infer... because I know...", "Reduce the mystery container to a choice among four objects the student sees beforehand."],
 "challenge": ["Have the student research one more of Turner's discoveries, such as how ants find their way home, and describe the experiment.", "Ask the student to design a trail-camera investigation for the garden mystery with a clear testable question."],
 "background": "<p>Charles Henry Turner (1867 to 1923) earned his PhD in zoology from the University of Chicago in 1907 and taught at Sumner High School in St. Louis. His 1910 experiments gave early evidence that honeybees learn color and pattern (Karl von Frisch later proved bee color vision in 1914), that insects can hear, and that ants learn routes. A circling behavior of ants returning to the nest is known as Turner's circling. He published dozens of papers despite being shut out of university positions by racism.</p><p>Raccoon front tracks are about 5 to 8 centimeters long with five long, finger-like toes. Dog tracks show four toes with claw marks and a triangular pad.</p>",
 "sources": ["Encyclopaedia Britannica: Charles Henry Turner (entry title)", "Abramson, C. I. (2009). A study in inspiration: Charles Henry Turner (1867 to 1923) and the investigation of insect behavior. Annual Review of Entomology 54: 343 to 359."]
}

PRINT = {
 "directions": "Write O for observation or I for inference, and answer in complete sentences.",
 "items": [
  {"q":"Mark each O or I.  ___ The puddle is 40 cm wide.  ___ It rained last night.  ___ The bread has green spots.  ___ The bread is old.  ___ The dog is barking.  ___ The dog wants to go outside.","a":"O, I, O, I, O, I","lines":1},
  {"q":"Write two qualitative and two quantitative observations about an object on your table right now.","a":"Answers vary; qualitative describe qualities (color, texture, smell); quantitative use numbers with units.","lines":3},
  {"q":"A plant on the windowsill is drooping and its soil is dry and cracked. Write one inference and the evidence for it.","a":"For example: the plant needs water, because the soil is dry and cracked and drooping leaves are a sign of water loss.","lines":2},
  {"q":"Write another inference that could explain the same drooping plant.","a":"For example: the plant is getting too much heat from the window, or it has a disease or pests.","lines":2},
  {"q":"Rewrite as a testable question: Are cats smart?","a":"For example: Can a cat learn to find a treat under a red cup faster after five practice days?","lines":2},
  {"q":"In your testable question, what would you change and what would you measure?","a":"Answers should name one changed variable and one measured result.","lines":2},
  {"q":"Explain how Charles Henry Turner's work changed what scientists believed about insects.","a":"His experiments showed insects can see color, hear and learn, challenging the belief that insects act only on instinct.","lines":3}]
}
