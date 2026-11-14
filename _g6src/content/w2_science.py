VARS = '''<svg viewBox="0 0 540 200" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Diagram of independent, dependent and controlled variables">
<text x="270" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Question: Does water temperature change how fast sugar dissolves?</text>
<rect x="15" y="40" width="160" height="140" rx="8" fill="#eef3fb" stroke="#0047BA" stroke-width="2"/>
<text x="95" y="64" text-anchor="middle" font-weight="bold" fill="#0047BA">INDEPENDENT</text><text x="95" y="82" text-anchor="middle">What I change</text>
<text x="95" y="112" text-anchor="middle">water temperature:</text><text x="95" y="130" text-anchor="middle">10°C, 25°C, 50°C</text>
<path d="M180 110 H210" stroke="#0A1F3D" stroke-width="3" marker-end="url(#a)"/>
<defs><marker id="a" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8Z" fill="#0A1F3D"/></marker></defs>
<rect x="215" y="40" width="160" height="140" rx="8" fill="#fde8e8" stroke="#DB2F30" stroke-width="2"/>
<text x="295" y="64" text-anchor="middle" font-weight="bold" fill="#DB2F30">DEPENDENT</text><text x="295" y="82" text-anchor="middle">What I measure</text>
<text x="295" y="112" text-anchor="middle">time for sugar to</text><text x="295" y="130" text-anchor="middle">dissolve (seconds)</text>
<rect x="390" y="40" width="140" height="140" rx="8" fill="#fff8e6" stroke="#C9A84C" stroke-width="2"/>
<text x="460" y="64" text-anchor="middle" font-weight="bold" fill="#8a6d1f">CONTROLLED</text><text x="460" y="82" text-anchor="middle">What I keep the same</text>
<text x="460" y="106" text-anchor="middle">amount of water</text><text x="460" y="124" text-anchor="middle">amount of sugar</text><text x="460" y="142" text-anchor="middle">type of sugar</text><text x="460" y="160" text-anchor="middle">stirring</text></svg>'''

def bean(x, h, food):
    return (f'<rect x="{x-14}" y="160" width="28" height="22" fill="#b5651d"/><line x1="{x}" y1="160" x2="{x}" y2="{160-h}" stroke="#2f7d32" stroke-width="3"/>'
            f'<ellipse cx="{x-8}" cy="{160-h+8}" rx="8" ry="4" fill="#3d8a30"/><ellipse cx="{x+8}" cy="{160-h+14}" rx="8" ry="4" fill="#3d8a30"/>' + (f'<circle cx="{x+16}" cy="152" r="4" fill="#C9A84C"/>' if food else ''))
GROUPS = ('<svg viewBox="0 0 540 220" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Control group and experimental group of bean plants">'
  '<text x="270" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Does plant food help bean plants grow?</text>'
  '<rect x="10" y="30" width="250" height="180" rx="8" fill="#fff" stroke="#5b6676"/><rect x="280" y="30" width="250" height="180" rx="8" fill="#fff" stroke="#C9A84C" stroke-width="2"/>'
  '<text x="135" y="50" text-anchor="middle" font-weight="bold">Control group: plain water</text><text x="405" y="50" text-anchor="middle" font-weight="bold">Experimental group: plant food</text>'
  + bean(60, 60, False) + bean(135, 66, False) + bean(210, 58, False) + bean(330, 84, True) + bean(405, 90, True) + bean(480, 80, True) +
  '<text x="270" y="204" text-anchor="middle" font-size="11" fill="#5b6676">Same soil, pots, light, water amount and bean type. Only the plant food changes.</text></svg>')
def avgbar():
    s = '<svg viewBox="0 0 520 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Bar graph of paper towel averages with trial dots">'
    s += '<text x="260" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Water absorbed (mL): averages and every trial</text>'
    s += '<line x1="70" y1="190" x2="480" y2="190" stroke="#0A1F3D"/><line x1="70" y1="30" x2="70" y2="190" stroke="#0A1F3D"/>'
    for v in (0, 20, 40, 60):
        y = 190 - v * 2.5; s += f'<text x="62" y="{y+4}" text-anchor="end" fill="#5b6676">{v}</text><line x1="70" y1="{y}" x2="480" y2="{y}" stroke="#eee"/>'
    for x, lab, trials, avg, c in [(170, 'Brand A', (42, 45, 39), 42, '#0047BA'), (360, 'Brand B', (38, 51, 41), 43.33, '#C9A84C')]:
        s += f'<rect x="{x-45}" y="{190-avg*2.5}" width="90" height="{avg*2.5}" fill="{c}" opacity=".85"/><text x="{x}" y="208" text-anchor="middle" font-weight="bold">{lab}</text>'
        for i, t in enumerate(trials): s += f'<circle cx="{x-20+i*20}" cy="{190-t*2.5}" r="5" fill="#DB2F30" stroke="#fff"/>'
    s += '<circle cx="400" cy="40" r="5" fill="#DB2F30"/><text x="410" y="44">= one trial</text></svg>'
    return s
def tree(x, y, treated):
    return (f'<circle cx="{x}" cy="{y}" r="11" fill="{"#3d8a30" if treated else "#8fb07a"}"/><rect x="{x-2}" y="{y+9}" width="4" height="7" fill="#6b4f2a"/>' +
            (f'<circle cx="{x+4}" cy="{y-2}" r="3" fill="#f39c12"/>' if treated else ''))
GROVE = ('<svg viewBox="0 0 520 200" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Layout of a citrus field trial">'
  '<text x="260" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">A citrus greening field trial (one test block)</text>'
  + ''.join(tree(60 + c * 45, 50 + r * 40, r % 2 == 0) for r in range(4) for c in range(6)) +
  '<rect x="340" y="40" width="14" height="14" fill="#3d8a30"/><text x="360" y="52">rows that get the treatment</text>'
  '<rect x="340" y="70" width="14" height="14" fill="#8fb07a"/><text x="360" y="82">control rows: no treatment</text>'
  '<text x="340" y="112">Rows alternate so soil, sun</text><text x="340" y="128">and water are the same for both.</text><text x="340" y="152">Measured for several seasons:</text><text x="340" y="168">fruit count, fruit size, tree health.</text></svg>')

LESSON = {
 "unit": "Unit 1: Thinking Like a Scientist",
 "title": "Designing a Fair Test: Variables",
 "subtitle": "If you change two things at once, you can never know which one made the difference.",
 "objectives": [
  "Identify the independent, dependent and controlled variables in an investigation.",
  "Explain why a fair test changes only one variable at a time and uses a control group.",
  "Write a hypothesis in if, then, because form.",
  "Explain why scientists repeat trials and average the results.",
  "Design and carry out a fair test at home."],
 "vocab": [
  ["variable", "Any factor that can change in an investigation."],
  ["independent variable", "The one variable the scientist changes on purpose."],
  ["dependent variable", "The variable that is measured; it may change because of the independent variable."],
  ["controlled variables", "Everything kept the same so the test is fair (also called constants)."],
  ["control group", "The group that does not get the change being tested, used for comparison."],
  ["fair test", "An investigation in which only one variable is changed at a time."],
  ["hypothesis", "A testable prediction, often written as If..., then..., because..."],
  ["trial", "One run of an experiment. Scientists repeat trials to make results reliable."],
  ["data", "Facts and measurements collected during an investigation."]],
 "reconnect": {
  "title": "Week 1: observations, inferences and testable questions",
  "intro": "A fair test begins with a testable question. Check what you remember from last week.",
  "items": [
   {"t":"text","q":"\"The plant grew 4 centimeters in a week.\" Observation or inference?","a":["observation"],"pts":2,"why":"It was measured directly."},
   {"t":"open","key":"rc_backobs","q":"\"The plant grew because it had more sunlight\" is an inference. Write one observation that could support it.","min":8,"rows":2,"rubric":["A direct observation or measurement","Connected to sunlight or growth"],"model":"The plant by the window grew 6 cm in two weeks, while the plant in the hallway grew 2 cm."},
   {"t":"text","q":"\"The water is cloudy.\" Qualitative or quantitative?","a":["qualitative"],"pts":2,"why":"It describes a quality with no number."},
   {"t":"text","q":"Is this testable? <i>Do heavier paper airplanes fly shorter distances?</i> Type yes or no.","a":["yes"],"pts":2,"why":"You can change the plane's mass and measure the distance it flies."},
   {"t":"text","q":"A testable question names what you change and what you ___.","a":["measure","measure.","observe"],"show":"measure","pts":2,"why":"Change one thing, measure the result."},
   {"t":"text","q":"What did Charles Henry Turner change in his honeybee experiments?","a":[{"all":[["color","colour","card","pattern"]]}],"show":"The color of the cards the honey dishes sat on","pts":2,"why":"He changed the card colors and observed which ones the bees chose. Today you will learn the name for that kind of variable."}]},
 "hook": {
  "title": "The Paper Towel Showdown",
  "html": "<p>Jaylen's family buys a lot of paper towels, and his mom wonders whether the expensive brand really absorbs more than the store brand. Jaylen grabs a sheet of each. He dunks the expensive one in a full bowl of water for ten seconds and the store brand in a half-full mug for three seconds. The expensive one soaks up more. \"Expensive wins!\" he announces.</p><p>His older sister shakes her head. \"That proves nothing.\"</p><p>She is right. Jaylen changed the brand, the container, the amount of water and the time all at once. The result could have come from any of them.</p><div class='callout'><b>Big idea:</b> A fair test changes only <b>one</b> thing and keeps everything else the same. That is the only way to know what caused the result.</div>"},
 "learn": [
  {"title": "Three Kinds of Variables",
   "visual": VARS,
   "html": "<p>Every fair test has three kinds of variables:</p><ul><li>The <b>independent variable</b> is the one thing you change on purpose.</li><li>The <b>dependent variable</b> is what you measure. It <i>depends</i> on the independent variable.</li><li>The <b>controlled variables</b> are everything you keep the same.</li></ul><p>A memory trick: <i>I change the Independent; the Dependent is the Data.</i></p>",
   "checks": [
    {"t":"text","q":"In a fair version of Jaylen's test, what should the independent variable be?","a":[{"all":[["brand","type","kind"]]}],"show":"the brand (type) of paper towel","pts":3,"why":"The question is about brands, so brand is the only thing that should change."},
    {"t":"text","q":"What should Jaylen measure (the dependent variable)?","a":[{"all":[["water","liquid","absorb","soak","ml","milliliter","spoon"]]}],"show":"the amount of water each towel absorbs","pts":3,"why":"The question asks how much each towel absorbs."},
    {"t":"text","q":"Name two variables Jaylen must keep the same.","a":[{"all":[["time","second","how long","minute"],["water","container","bowl","size","amount","temperature","sheet","cup"]]},{"all":[["water","amount"],["container","bowl","cup","size","sheet","temperature"]]}],"show":"For example: the amount of water, the soaking time, the container, and the size of the towel","pts":3,"why":"Water amount, soaking time, container and sheet size must all be controlled."},
    {"t":"text","q":"A student tests whether the height a ball is dropped from changes how high it bounces. What is the dependent variable?","a":[{"all":[["bounce"]]}],"show":"how high the ball bounces","pts":2,"why":"Bounce height is measured; drop height is changed."}]},
  {"title": "Control Groups and Repeated Trials",
   "visual": GROUPS + avgbar(),
   "html": "<p>A <b>control group</b> gets no change at all. It gives you something to compare against. To test whether plant food helps beans grow, one group of plants gets plant food and the control group gets plain water, with everything else the same.</p><p>Scientists also repeat each test several times, called <b>trials</b>, then find the <b>average</b> (the mean). One trial might be a fluke; three or more trials make results reliable.</p><table class='t'><tr><th>Towel</th><th>Trial 1</th><th>Trial 2</th><th>Trial 3</th><th>Average</th></tr><tr><td>Brand A</td><td>42 mL</td><td>45 mL</td><td>39 mL</td><td>?</td></tr><tr><td>Brand B</td><td>38 mL</td><td>51 mL</td><td>41 mL</td><td>?</td></tr></table><p>To average: add the trials and divide by the number of trials.</p>",
   "checks": [
    {"t":"num","q":"What is the average for Brand A?","a":42,"unit":"mL","pts":3,"why":"42 + 45 + 39 = 126, and 126 ÷ 3 = 42 mL."},
    {"t":"num","q":"What is the average for Brand B?","a":43.33,"tol":0.04,"show":"43.33 (about 43.3)","unit":"mL","pts":3,"hint":"Add the three trials, then divide by 3. Round to the hundredths.","why":"38 + 51 + 41 = 130, and 130 ÷ 3 = 43.33 mL."},
    {"t":"text","q":"Look at Brand B's trials. Why is it a good thing the student did not stop after Trial 1?","a":[{"all":[["fluke","vary","varied","different results","51","38","reliable","accident","mistake","wrong","inconsistent","spread","not the same","luck","misleading","worse"]]}],"show":"Trial 1 alone (38 mL) would have made Brand B look worse; the trials varied, so one result could be a fluke.","pts":3,"why":"Brand B's results ranged from 38 to 51. One trial could have led to the wrong conclusion."},
    {"t":"text","q":"In the bean plant test, which group is the control group?","a":[{"all":[["no plant food","without","plain water","only water","just water","no food","don't get","do not get","doesn't get","no fertilizer"]]}],"show":"the plants that get plain water and no plant food","pts":2,"why":"The control group gets no change, so it is the plants without plant food."}]},
  {"title": "Writing a Hypothesis",
   "html": "<p>A <b>hypothesis</b> is a testable prediction with a reason. Scientists often write it in three parts:</p><div class='example'><b>If</b> I use hotter water, <b>then</b> the sugar will dissolve faster, <b>because</b> water molecules move faster when they are hot and pull sugar molecules away from the crystal more quickly.</div><p>The <b>if</b> names the independent variable. The <b>then</b> names the dependent variable. The <b>because</b> gives your reasoning. A hypothesis can turn out to be wrong, and that is still useful science.</p>",
   "checks": [
    {"t":"blanks","q":"Complete the hypothesis for the ball experiment.","sent":"If I drop the ball from a ___ height, then it will bounce ___, because it has more energy when it hits the ground.","blanks":[["higher","greater","taller","bigger"],["higher","more","taller"]],"pts":3,"why":"If I drop it from a higher height, then it will bounce higher."},
    {"t":"open","key":"towelhyp","q":"Write your own hypothesis for the paper towel test in if, then, because form.","min":15,"rows":2,"rubric":["Has all three parts: if, then, because","Names the paper type as the change and water absorbed as the result","Gives a reason"],"model":"If I test the thicker, more expensive brand, then it will absorb more water, because thicker towels have more fibers and spaces to hold water."},
    {"t":"text","q":"Jaylen redoes his test fairly, and the results show his hypothesis was wrong: the store brand absorbed more. Did his experiment fail? Type yes or no.","a":["no"],"pts":2,"why":"A fair test that disproves a hypothesis still teaches something true. It saved his family money, too."}]},
  {"title": "Fair Tests in the Real World",
   "visual": GROVE,
   "html": "<p>Since 2005, a disease called <b>citrus greening</b> has damaged orange groves across Florida. A tiny insect called the Asian citrus psyllid spreads bacteria that make oranges small, bitter and green, and eventually kill the trees.</p><p>Scientists at the University of Florida and in other labs test possible treatments the same way you will test paper towels. They treat one group of trees, keep a <b>control group</b> of untreated trees, keep the soil, water and fertilizer the same, and measure results over many seasons with many trees.</p><div class='callout'>Why many trees and many seasons? The same reason you run three trials: a single tree or a single year could give a misleading result.</div>",
   "checks": [
    {"t":"text","q":"In a citrus greening treatment test, what is the independent variable?","a":[{"all":[["treat","medicine","spray","whether"]]}],"show":"whether the tree gets the treatment","pts":3,"why":"Scientists change whether the trees get the treatment."},
    {"t":"text","q":"Name a dependent variable scientists could measure in that test.","a":[{"all":[["fruit","orange","size","yield","health","leaves","green","sweet","alive","die","survive","bacteria","number","weight","sugar"]]}],"show":"For example: number or size of oranges, or how many trees stay healthy","pts":3,"why":"They could measure fruit yield, fruit size or tree health."},
    {"t":"text","q":"Why do scientists keep the soil, water and fertilizer the same for both groups of trees?","a":[{"all":[["cause","difference","fair","treatment","only thing","only variable","know what","because of the","responsible","made the"]]}],"show":"So any difference can only be caused by the treatment","pts":3,"why":"Controlled variables make sure the treatment is the only difference between the groups."}]}],
 "handson": {
  "title": "The Fair Paper Towel Test",
  "intro": "Redo Jaylen's test the right way. Use real data and averages.",
  "materials": ["Three kinds of paper: two brands of paper towel and a paper napkin (or toilet paper)", "A kitchen scale that shows grams", "A bowl of water", "A timer and scissors", "A cookie sheet or tray to keep things tidy"],
  "steps": [
   "Write your hypothesis in if, then, because form before you start.",
   "Use half of a full sheet for every test so all pieces are the same size.",
   "Weigh the dry half sheet on a kitchen scale in grams. Dip it in a bowl of water for exactly 10 seconds, lift it, and let it drip for exactly 10 seconds.",
   "Weigh the wet sheet. Water absorbed = wet mass − dry mass. One gram of water is about one milliliter, so grams and milliliters match.",
   "Repeat three trials for each kind of paper with a fresh half sheet each time.",
   "Make a data table and find the average for each kind of paper."],
  "record": [
   {"t":"open","key":"hyp","q":"Write your hypothesis and list your independent variable, dependent variable and at least three controlled variables.","min":35,"rows":5},
   {"t":"open","key":"data","q":"Type your data table: every trial for every kind of paper and each average. Which absorbed the most? Was your hypothesis supported?","min":40,"rows":7}]},
 "think": {
  "items": [
   {"t":"open","key":"flawed","model":"Kayla changed two things at once: music and light. The window plant got sunlight and the closet plant got none, so the light could explain the growth. A fair test would put several plants of the same type in the same sunny room, with the same soil, pot and water, and play music for only half of them. She should measure height over several weeks and compare the averages.","q":"Kayla wants to know whether music helps plants grow. She puts one plant by a sunny window with music playing and another plant in a dark closet with no music. After two weeks the music plant is taller, so she says music helps plants grow. Explain what is wrong with her experiment and redesign it as a fair test.","min":58,"rows":7,"rubric":["Identifies that two variables changed (music and light)","Explains why the conclusion cannot be trusted","Redesign changes only music","Lists controlled variables (light, water, soil, plant type, pot size)","Includes a control group and repeated trials or several plants"]},
   {"t":"open","key":"design","model":"(Example built on the question: Does the brand of bird seed change how many birds visit the feeder?) Hypothesis: If I use seed with sunflower hearts, then more birds will visit in one hour, because many birds prefer sunflower seeds. Independent: brand of seed. Dependent: number of birds that land in one hour. Controlled: same feeder, location, time of day, amount of seed. Control group: the seed we usually buy. Trials: five mornings for each seed.","q":"Go back to the testable question you wrote in Week 1 about your home or neighborhood. Write a full plan: hypothesis, independent variable, dependent variable, at least three controlled variables, control group, and number of trials.","min":60,"rows":6,"rubric":["Hypothesis in if, then, because form","Correct independent and dependent variables","Three or more sensible controlled variables","Identifies a control group","Plans repeated trials"]}]},
 "exit": [
  {"t":"text","q":"A student tests whether the amount of salt changes how fast ice melts. What is the independent variable?","a":[{"all":[["salt"]]}],"show":"the amount of salt","pts":2,"why":"The amount of salt is what the student changes."},
  {"t":"text","q":"In that test, what is the dependent variable?","a":[{"all":[["time","melt","fast","how long","speed","minutes"]]}],"show":"how long the ice takes to melt","pts":2,"why":"Melting time is measured."},
  {"t":"text","q":"Name one controlled variable for the salt and ice test.","a":[{"all":[["size","temperat","type of salt","kind of salt","amount of ice","container","shape","cube","room","same ice"]]}],"show":"For example: size of the ice cubes, room temperature or type of salt","pts":2,"why":"These must stay the same so only the salt amount changes."},
  {"t":"num","q":"Three trials gave melting times of 12, 15 and 18 minutes. What is the average?","a":15,"unit":"minutes","pts":3,"why":"12 + 15 + 18 = 45, and 45 ÷ 3 = 15 minutes."},
  {"t":"text","q":"What is the purpose of a control group?","a":[{"all":[["compar","normal","baseline","no change","without","difference"]]}],"show":"To give a group with no change to compare against","pts":3,"why":"The control group shows what happens without the change being tested."},
  {"t":"text","q":"What three words begin the three parts of a hypothesis in the form you learned?","a":[{"all":[["if"],["then"],["because"]]}],"show":"if, then, because","pts":2,"why":"If (change), then (result), because (reason)."}],
 "next": "Week 3: measuring and recording data with metric tools."
}

TEACHER = {
 "standards": [
  "SC.6.N.1.1: Define a problem from the sixth grade curriculum, use appropriate reference materials to support scientific understanding, plan and carry out scientific investigation of various types, such as systematic observations or experiments, identify variables, collect and organize data, interpret data in charts, tables, and graphics, analyze information, make predictions, and defend conclusions.",
  "SC.6.N.1.2: Explain why scientific investigations should be replicable.",
  "MA.6 connection: finding the mean of a data set (formally taught in Math Unit 6).",
  "NGSS Science and Engineering Practice 3: planning and carrying out investigations."],
 "materials": ["The interactive lesson", "Paper towels, napkins, three identical cups, a measuring cup in milliliters, a timer", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 1 Reconnect questions. The Turner question bridges to independent variables."],
  [6, "Hook", "Read Jaylen's test. Ask the student to list everything Jaylen changed. Count them together."],
  [12, "Variables", "Use the sugar diagram. Then have the student label variables in three quick examples you invent."],
  [10, "Control groups and trials", "Work the Brand A and Brand B averages. Discuss why Brand B's results vary and what one trial would have told us."],
  [8, "Hypothesis", "Model one if, then, because hypothesis. The student writes one for the paper towel test."],
  [8, "Real-world fair tests", "Read about citrus greening. Ask: why would a citrus scientist need hundreds of trees instead of two?"],
  [10, "Start the paper towel test live", "If materials are ready, do Trial 1 together on camera so the student sees the procedure, then they finish the trials after class."]],
 "key_questions": ["What exactly are you changing?", "What will you measure, and with what tool?", "What could accidentally change that you need to control?", "How many trials will you run, and why?", "What would it mean if your hypothesis turns out wrong?"],
 "misconceptions": ["Changing more than one variable at a time.", "Confusing the control group with controlled variables (a group versus things kept the same).", "Thinking a wrong hypothesis means the experiment failed.", "Thinking one trial is enough."],
 "support": ["Use a three-column variables organizer: I change / I measure / I keep the same.", "Provide sentence frames for the hypothesis.", "Reduce the hands-on test to two kinds of paper with three trials each."],
 "challenge": ["Have the student graph their paper towel averages as a bar graph (preview of Week 4).", "Ask the student to research one real citrus greening treatment being tested and identify its variables."],
 "background": "<p>Citrus greening (huanglongbing, or HLB) was first detected in Florida in 2005. It is caused by bacteria spread by the Asian citrus psyllid and has sharply reduced Florida's orange production. The University of Florida's Institute of Food and Agricultural Sciences (UF/IFAS) runs many controlled field trials of possible treatments.</p>",
 "sources": ["UF/IFAS Citrus Research and Education Center: Citrus greening (HLB).", "USDA Animal and Plant Health Inspection Service: Citrus greening."]
}

PRINT = {
 "directions": "Read each investigation and answer in complete sentences.",
 "items": [
  {"q":"Marisol tests whether the type of soil changes how tall bean plants grow in 3 weeks. Name the independent variable, the dependent variable and two controlled variables.","a":"Independent: type of soil. Dependent: plant height after 3 weeks. Controlled: amount of water, sunlight, type of bean, pot size, temperature.","lines":3},
  {"q":"Write a hypothesis for Marisol's investigation in if, then, because form.","a":"For example: If I use potting soil, then the beans will grow taller, because potting soil has more nutrients.","lines":2},
  {"q":"Three trials of a paper airplane flew 4.2 m, 3.9 m and 4.5 m. Find the average distance.","a":"(4.2 + 3.9 + 4.5) ÷ 3 = 12.6 ÷ 3 = 4.2 m","lines":2},
  {"q":"Why should Marisol test several bean plants in each soil type instead of just one?","a":"One plant could be unusual; several plants make the results reliable.","lines":2},
  {"q":"Malik tests a new sports drink. He gives it to his friends before a race and they run fast. What is missing from his experiment?","a":"A control group of runners who drink water (or no sports drink), plus controlled variables and repeated trials.","lines":2},
  {"q":"Explain the difference between a control group and controlled variables.","a":"A control group is the group that gets no change, for comparison. Controlled variables are the factors kept the same for every group.","lines":3}]
}
