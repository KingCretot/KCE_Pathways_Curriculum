LADDER = ('<svg viewBox="0 0 560 250" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Metric prefix staircase">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The metric staircase: each step is × 10 or ÷ 10</text>'
  + ''.join(f'<rect x="{20+i*76}" y="{40+i*24}" width="72" height="{180-i*24}" fill="{c}" stroke="#0A1F3D"/><text x="{56+i*76}" y="{58+i*24}" text-anchor="middle" font-weight="bold" fill="{tc}">{p}</text><text x="{56+i*76}" y="{74+i*24}" text-anchor="middle" font-size="10" fill="{tc}">{v}</text>'
            for i, (p, v, c, tc) in enumerate([("kilo-", "1,000", "#0A1F3D", "#fff"), ("hecto-", "100", "#1d3b66", "#fff"), ("deka-", "10", "#2f5a91", "#fff"),
                                              ("BASE", "m, g, L", "#C9A84C", "#0A1F3D"), ("deci-", "0.1", "#9ec3f0", "#0A1F3D"), ("centi-", "0.01", "#c4dbf6", "#0A1F3D"), ("milli-", "0.001", "#e4eefb", "#0A1F3D")])) +
  '<path d="M60 240 L520 240" stroke="#DB2F30" stroke-width="2"/><path d="M520 240 l-8 -5 v10z" fill="#DB2F30"/><text x="290" y="234" text-anchor="middle" fill="#DB2F30" font-size="11">Going down the stairs: multiply by 10 for each step</text></svg>')

def ruler():
    s = '<svg viewBox="0 0 560 150" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="A leaf measured with a centimeter ruler">'
    s += '<text x="280" y="16" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Read to the nearest millimeter</text>'
    s += '<path d="M40 60 Q120 28 228 52 Q300 64 296 60 Q200 92 40 60Z" fill="#5c9e4c" stroke="#2f6b25"/><line x1="40" y1="60" x2="296" y2="60" stroke="#2f6b25"/>'
    s += '<rect x="30" y="90" width="500" height="44" fill="#fff8e6" stroke="#8a6d1f"/>'
    for mm in range(0, 121):
        x = 40 + mm * 4; h = 18 if mm % 10 == 0 else (12 if mm % 5 == 0 else 7)
        s += f'<line x1="{x}" y1="90" x2="{x}" y2="{90+h}" stroke="#2a2a2a" stroke-width="{1.2 if mm%10==0 else .7}"/>'
        if mm % 10 == 0: s += f'<text x="{x}" y="{124}" text-anchor="middle">{mm//10}</text>'
    s += '<line x1="296" y1="58" x2="296" y2="92" stroke="#DB2F30" stroke-dasharray="3 2"/><text x="527" y="105" text-anchor="end" font-size="10">cm</text></svg>'
    return s

CYL = ('<svg viewBox="0 0 520 260" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Graduated cylinder with meniscus">'
  '<text x="260" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Read a graduated cylinder at the bottom of the meniscus</text>'
  '<rect x="150" y="40" width="70" height="200" fill="#fff" stroke="#0A1F3D" stroke-width="2"/>'
  '<path d="M151 137 Q185 151 219 137 L219 239 L151 239Z" fill="#9ec3f0"/>'
  + ''.join(f'<line x1="{150 if v%5 else 150}" y1="{y}" x2="{166 if v%5==0 else 160}" y2="{y}" stroke="#0A1F3D"/>' + (f'<text x="144" y="{y+4}" text-anchor="end">{v}</text>' if v % 5 == 0 else '')
            for v, y in [(v, 240 - (v - 20) * 8) for v in range(20, 45)]) +
  '<line x1="226" y1="144" x2="300" y2="144" stroke="#DB2F30" stroke-width="2"/><text x="306" y="140" fill="#DB2F30" font-weight="bold">Eye level here</text>'
  '<text x="306" y="158" fill="#DB2F30">Read the bottom of the curve</text><text x="140" y="34" text-anchor="end" font-size="11">mL</text></svg>')

DARTS = ('<svg viewBox="0 0 560 170" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Accuracy and precision targets">'
  + ''.join(f'<g transform="translate({i*140} 10)"><circle cx="70" cy="60" r="55" fill="#fff" stroke="#0A1F3D"/><circle cx="70" cy="60" r="35" fill="#fff" stroke="#0A1F3D"/><circle cx="70" cy="60" r="14" fill="#DB2F30"/>'
            + ''.join(f'<circle cx="{70+dx}" cy="{60+dy}" r="4" fill="#0047BA"/>' for dx, dy in pts) + f'<text x="70" y="136" text-anchor="middle" font-weight="bold">{a}</text><text x="70" y="152" text-anchor="middle" font-weight="bold">{b}</text></g>'
            for i, (a, b, pts) in enumerate([("Accurate", "and precise", [(-3, 2), (2, -3), (4, 3), (-2, -2)]), ("Precise,", "not accurate", [(30, -28), (34, -24), (28, -22), (33, -30)]),
                                             ("Accurate,", "not precise", [(-30, 8), (28, -14), (6, 32), (-6, -30)]), ("Neither", "", [(20, 18), (40, 4), (12, 40), (36, 30)])])) + '</svg>')

LESSON = {
 "unit": "Unit 1: Thinking Like a Scientist",
 "title": "Measuring and Recording Data",
 "subtitle": "In 1999 a spacecraft was lost because two teams used different units. Measurement is not a small detail.",
 "objectives": [
  "Explain why scientists around the world use the metric system (SI).",
  "Convert between metric units by multiplying and dividing by powers of ten.",
  "Measure length, volume, mass and temperature with the correct tools and units, including reading a meniscus.",
  "Explain the difference between accuracy and precision.",
  "Organize measurements in a clear data table with labeled units."],
 "vocab": [
  ["metric system (SI)", "The International System of Units, a base-ten measurement system used by scientists worldwide."],
  ["meter (m)", "The base unit of length."],
  ["gram (g) and kilogram (kg)", "Units of mass. The kilogram is the official SI base unit; 1 kg = 1,000 g."],
  ["liter (L)", "A unit of volume. 1 L = 1,000 mL."],
  ["degrees Celsius (°C)", "The metric temperature scale. Water freezes at 0 °C and boils at 100 °C at sea level."],
  ["mass", "The amount of matter in an object, measured with a balance or scale."],
  ["volume", "The amount of space something takes up."],
  ["meniscus", "The curved surface of a liquid in a narrow container. Read the volume at the bottom of the curve."],
  ["accuracy", "How close a measurement is to the true value."],
  ["precision", "How close repeated measurements are to each other."]],
 "reconnect": {
  "title": "Week 2: fair tests and variables",
  "intro": "Every fair test ends with measurements. Warm up the experiment skills from last week.",
  "items": [
   {"t":"text","q":"A student tests whether the color of a cup changes how fast ice melts in the sun. What is the independent variable?","a":[{"all":[["color","colour"]]}],"show":"the color of the cup","pts":2,"why":"The color is what the student changes."},
   {"t":"blanks","q":"Name two different variables the student must control in that test.","sent":"Variable 1: ___   Variable 2: ___","blanks":[[{"all":[["size","amount","sun","time","temperat","cup","material","shape","ice","location","place","spot","water","light","volume","mass","weight","start"]]}],[{"all":[["size","amount","sun","time","temperat","cup","material","shape","ice","location","place","spot","water","light","volume","mass","weight","start"]]}]],"distinct":True,"show":"For example: the size of the ice cube, the type and size of cup, the amount of sun, the starting temperature","pts":3,"why":"Everything except cup color must stay the same."},
   {"t":"num","q":"Four trials took 8, 10, 9 and 13 minutes. What is the average?","a":10,"unit":"minutes","pts":3,"why":"8 + 10 + 9 + 13 = 40, and 40 ÷ 4 = 10 minutes."},
   {"t":"open","key":"rc_hyp","q":"Write a hypothesis for the cup color test in if, then, because form.","min":12,"rows":2,"rubric":["Has if, then and because","Names cup color as the change and melting time as the result","Gives a scientific reason"],"model":"If I put the ice in a black cup, then it will melt faster than in a white cup, because dark colors absorb more energy from sunlight."},
   {"t":"open","key":"controlvs","q":"What is the difference between a control group and controlled variables? Use the bean-plant example if it helps.","min":20,"rows":3,"rubric":["Control group: the group that gets no change, used for comparison","Controlled variables: conditions kept the same for every group"],"model":"The control group is the group that gets no change, like the bean plants with plain water, so we can compare the others to it. Controlled variables are the conditions kept the same for every group, like the same pot, soil and sunlight."}]},
 "hook": {
  "title": "The $125 Million Unit Mistake",
  "html": "<p>In September 1999, NASA's Mars Climate Orbiter reached Mars after a nine-month journey, then vanished. Investigators discovered why: one engineering team had calculated thruster impulse in U.S. customary units (pound-force seconds) while the navigation team expected metric units (newton-seconds). Nobody converted. The spacecraft flew far too close to Mars and was destroyed. The orbiter alone cost about $125 million.</p><p>Science is shared around the world, so scientists everywhere use one system of measurement: the <b>metric system</b>, also called <b>SI</b>. This week you will learn to measure like a professional, and to never forget the units.</p><div class='callout'><b>Big idea:</b> A number without a unit is meaningless. Is \"12\" twelve centimeters, twelve kilograms or twelve seconds?</div>"},
 "learn": [
  {"title": "Why the Metric System?",
   "html": "<p>The metric system is built on <b>tens</b>, just like our place-value system. That makes converting as easy as moving a decimal point. It is the official measurement system of nearly every country in the world. The United States, Liberia and Myanmar are often listed as the main countries that still use customary units (inches, pounds, gallons) in everyday life, but American scientists, doctors and engineers use metric every day.</p><table class='t'><tr><th>Quantity</th><th>Metric unit</th><th>Tool</th></tr><tr><td>Length</td><td>meter (m)</td><td>ruler, meter stick, measuring tape</td></tr><tr><td>Mass</td><td>gram (g), kilogram (kg)</td><td>balance or digital scale</td></tr><tr><td>Volume of a liquid</td><td>liter (L), milliliter (mL)</td><td>graduated cylinder, measuring cup</td></tr><tr><td>Temperature</td><td>degrees Celsius (°C)</td><td>thermometer</td></tr><tr><td>Time</td><td>second (s)</td><td>stopwatch, timer</td></tr></table>",
   "checks": [
    {"t":"text","q":"Why did the Mars Climate Orbiter fail?","a":[{"all":[["unit","metric","customary","pound","newton","convert","system"]]}],"show":"Two teams used different units (customary and metric) and nobody converted.","pts":3,"why":"A unit mismatch sent the spacecraft too close to Mars."},
    {"t":"text","q":"Which tool and unit would you use to measure the mass of an apple? Answer like this: tool, unit.","a":[{"all":[["scale","balance"],["gram","kilogram","kg","grams g"]]}],"show":"a scale (or balance), grams","pts":3,"why":"Mass is measured with a scale or balance, in grams."},
    {"t":"text","q":"Why is the metric system easier to convert than inches, feet and yards?","a":[{"all":[["10","ten","decimal","place value","power"]]}],"show":"Because it is based on powers of ten, so you just move the decimal point.","pts":3,"why":"12 inches in a foot and 3 feet in a yard do not follow a pattern; metric always uses tens."}]},
  {"title": "Climbing the Metric Staircase",
   "visual": LADDER,
   "html": "<p>Metric prefixes tell you how big a unit is compared with the base unit. The same prefixes work for meters, grams and liters.</p><p><b>Going down the stairs</b> (to smaller units): <b>multiply</b> by 10 for each step. <b>Going up</b> (to larger units): <b>divide</b> by 10 for each step.</p><div class='example'>3.2 km to meters: kilo to base is 3 steps down, so 3.2 × 1,000 = <b>3,200 m</b>.<br>450 cm to meters: centi to base is 2 steps up, so 450 ÷ 100 = <b>4.5 m</b>.</div><p>This is the same powers-of-ten math you practiced in Math this week.</p>",
   "checks": [
    {"t":"num","q":"2,500 mL = ? L","a":2.5,"unit":"L","pts":3,"why":"milli to base is 3 steps up: 2,500 ÷ 1,000 = 2.5 L."},
    {"t":"num","q":"0.75 kg = ? g","a":750,"unit":"g","pts":3,"why":"kilo to base is 3 steps down: 0.75 × 1,000 = 750 g."},
    {"t":"num","q":"68 mm = ? cm","a":6.8,"unit":"cm","pts":3,"why":"milli to centi is 1 step up: 68 ÷ 10 = 6.8 cm."},
    {"t":"num","q":"A trail is 4.6 km long. How many meters is that?","a":4600,"show":"4,600","unit":"m","pts":3,"why":"4.6 × 1,000 = 4,600 m."}]},
  {"title": "Reading Tools Correctly",
   "visual": ruler() + CYL,
   "html": "<p><b>Rulers:</b> each centimeter has 10 millimeter marks. The leaf above starts at 0 and ends at the red line, 6 full centimeters plus 4 millimeters: <b>6.4 cm</b>.</p><p><b>Graduated cylinders:</b> water curves up at the edges, forming a <b>meniscus</b>. Put your eye level with the liquid and read the <b>bottom</b> of the curve.</p><p><b>Mass and weight</b> are different. Mass is the amount of matter (grams). Weight is the pull of gravity on that matter. On the Moon your mass is the same, but you weigh about one-sixth as much.</p><p><b>Temperature:</b> water freezes at 0 °C and boils at 100 °C at sea level. A healthy human body is about 37 °C.</p>",
   "checks": [
    {"t":"num","q":"How long is the leaf on the ruler, in centimeters?","a":6.4,"unit":"cm","pts":3,"why":"6 whole centimeters plus 4 millimeters = 6.4 cm."},
    {"t":"num","q":"Read the graduated cylinder. What is the volume, in mL? (Each small line is 1 mL.)","a":32,"unit":"mL","pts":3,"why":"The bottom of the meniscus sits at the 32 mL line, 2 marks above 30."},
    {"t":"open","key":"moon","q":"An astronaut travels to the Moon. Does her mass change? Does her weight change? Explain both.","min":15,"rows":2,"rubric":["Mass stays the same (same amount of matter)","Weight decreases (weaker gravity, about 1/6)"],"model":"Her mass stays the same because she is made of the same amount of matter. Her weight drops to about one sixth because the Moon's gravity is weaker."},
    {"t":"num","q":"A thermometer in a glass of ice water should read about how many degrees Celsius?","a":0,"tol":1,"unit":"°C","pts":2,"why":"Ice water is at the freezing point of water: about 0 °C."}]},
  {"title": "Accuracy, Precision and Data Tables",
   "visual": DARTS,
   "html": "<p><b>Accuracy</b> means close to the true value. <b>Precision</b> means repeated measurements are close to each other. A scale that always reads 2 grams too heavy is precise but not accurate.</p><p>Record measurements in a <b>data table</b>. Put the independent variable in the first column and the dependent variable in the next columns. Put the <b>units in the column headings</b> so you do not have to write them in every cell.</p><table class='t'><tr><th>Water temperature (°C)</th><th>Trial 1 (s)</th><th>Trial 2 (s)</th><th>Trial 3 (s)</th><th>Average (s)</th></tr><tr><td>10</td><td>95</td><td>101</td><td>98</td><td>98</td></tr><tr><td>25</td><td>62</td><td>58</td><td>60</td><td>?</td></tr><tr><td>50</td><td>31</td><td>29</td><td>33</td><td>?</td></tr></table>",
   "checks": [
    {"t":"num","q":"What is the average dissolving time at 25 °C?","a":60,"unit":"s","pts":3,"why":"62 + 58 + 60 = 180, and 180 ÷ 3 = 60 seconds."},
    {"t":"num","q":"What is the average dissolving time at 50 °C?","a":31,"unit":"s","pts":3,"why":"31 + 29 + 33 = 93, and 93 ÷ 3 = 31 seconds."},
    {"t":"text","q":"What pattern does the data show?","a":[{"all":[["hot","warm","higher","increas","rais","goes up"],["fast","less time","quick","shorter","faster"]],"none":["decreas","colder","lower temperature","slower","more time"]}],"show":"As water temperature increases, sugar dissolves faster (in less time).","pts":3,"why":"98 s at 10 °C, 60 s at 25 °C, 31 s at 50 °C: warmer water, less time."},
    {"t":"text","q":"Your kitchen scale reads 5 g when nothing is on it, every single time. Are its measurements accurate, precise, or both? Type precise, accurate or both.","a":["precise","^precise but not accurate","^precise not accurate","^precise because","^precise since"],"show":"precise (but not accurate)","pts":3,"why":"It is consistent (precise) but always 5 g off (not accurate). Press the tare button to zero it."}]}],
 "handson": {
  "title": "Kitchen Metric Lab",
  "intro": "Your kitchen is full of metric measuring tools. Estimate first, then measure, and see how good your estimates are.",
  "materials": ["A ruler with centimeters", "A kitchen scale that shows grams", "A measuring cup with milliliter marks", "A thermometer if you have one (a meat or candy thermometer works with adult help)", "Five household objects, such as a spoon, a book, an apple, a pencil and a cup of water"],
  "steps": [
   "Make a data table with columns: Object, What I measured, Estimate (with unit), Measurement (with unit), Difference.",
   "For each object, estimate first, then measure: the length of the spoon and pencil (cm), the mass of the book and apple (g), the volume of water in the cup (mL).",
   "If you have a thermometer, measure the temperature of cold tap water and warm tap water (°C). Ask an adult before using hot water.",
   "Convert two of your measurements to a different metric unit (for example, grams to kilograms).",
   "Before weighing, check that the empty scale reads 0. If it does not, press the tare or zero button.",
   "Measure one object three times and record all three readings. Are they precise?",
   "Read the measuring cup with your eye level with the water.",
   "Find which estimate was closest."],
  "record": [
   {"t":"open","key":"lab","q":"Type your data table with every estimate, measurement and unit, plus your two conversions.","min":40,"rows":7},
   {"t":"open","key":"lab2","q":"Which kind of measurement were you best at estimating, and which were you worst at? Were your three repeated readings precise? Give reasons, and say how you could improve.","min":25,"rows":3}]},
 "think": {
  "intro": "Explain like a scientist.",
  "items": [
   {"t":"open","key":"units","q":"A classmate writes the result of an experiment as \"The plant grew 15.\" Explain why this is a problem, and connect your answer to the Mars Climate Orbiter.","min":43,"rubric":["Explains that a number without a unit cannot be interpreted","Gives possible units (mm, cm) to show the confusion","Connects to the orbiter's unit mismatch","Suggests the correct way to write it"],"model":"Without a unit, nobody knows whether the plant grew 15 millimeters or 15 centimeters, which is ten times more. The Mars Climate Orbiter was destroyed because two teams used different units and never checked. The classmate should write \"The plant grew 15 cm\" and label the units in the table heading."},
   {"t":"open","key":"table","q":"Design the data table you would use for the fair paper towel test from Week 2. Write the column headings with units, and explain why you arranged it that way.","min":40,"rubric":["Independent variable (paper type) in the first column","Columns for repeated trials and an average","Units in the headings (mL or g)","Explains the arrangement"],"model":"Columns: Paper type | Trial 1 (mL absorbed) | Trial 2 (mL) | Trial 3 (mL) | Average (mL). The independent variable goes first because it is what I chose to change, the trials go next so I can see how consistent they are, and the average goes last because I calculate it from the trials. Putting mL in the headings means I do not have to write it in every cell."}]},
 "exit": [
  {"t":"num","q":"5.3 m = ? cm","a":530,"unit":"cm","pts":3,"why":"Base to centi is 2 steps down: 5.3 × 100 = 530 cm."},
  {"t":"num","q":"1,250 g = ? kg","a":1.25,"unit":"kg","pts":3,"why":"Base to kilo is 3 steps up: 1,250 ÷ 1,000 = 1.25 kg."},
  {"t":"num","q":"0.4 L = ? mL","a":400,"unit":"mL","pts":3,"why":"0.4 × 1,000 = 400 mL."},
  {"t":"text","q":"What tool and unit would you use to measure 50 milliliters of vinegar precisely? Answer like this: tool, unit.","a":[{"all":[["graduated cylinder","cylinder","syringe","pipette"],["ml","milliliter","millilitre"]]}],"show":"a graduated cylinder, milliliters","pts":3,"why":"A graduated cylinder measures liquid volume precisely in milliliters."},
  {"t":"text","q":"When you read a graduated cylinder, which part of the meniscus do you read?","a":[{"all":[["bottom","lowest","low"]]}],"show":"the bottom of the curve","pts":2,"why":"For water, read the bottom of the meniscus at eye level."},
  {"t":"open","key":"exit_accuracy","q":"Explain the difference between accuracy and precision using an example from your own kitchen or yard.","min":20,"rows":3,"rubric":["Accuracy = close to the true value","Precision = repeated results close together","A real example"],"model":"If my bathroom scale always says I weigh 3 pounds less than the doctor's scale, it is precise because it gives the same number every time, but not accurate because the number is wrong."}],
 "next": "Week 4: graphs, models and scientific tools. You will turn data into graphs that tell a story."
}

TEACHER = {
 "standards": [
  "SC.6.N.1.1: Define a problem from the sixth grade curriculum, use appropriate reference materials to support scientific understanding, plan and carry out scientific investigation of various types, such as systematic observations or experiments, identify variables, collect and organize data, interpret data in charts, tables, and graphics, analyze information, make predictions, and defend conclusions.",
  "SC.6.N.1.4: Discuss, compare and negotiate methods used, results obtained and explanations among groups of students conducting the same investigation (for a homeschool student: compare results with a parent or a KCE classmate).",
  "SC.8.P.8.2 (preview): Differentiate between weight and mass recognizing that weight is the amount of gravitational pull on an object and is distinct from, though proportional to, mass.",
  "MA.6 connection: multiplying and dividing by powers of ten (Math Week 3).",
  "NGSS Science and Engineering Practices 3 and 5: planning investigations; using mathematics and computational thinking."],
 "materials": ["The interactive lesson", "Ruler with millimeters, kitchen scale in grams, measuring cup in milliliters", "A clear glass and water to show a meniscus on camera", "Thermometer if available", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 2 Reconnect questions."],
  [6, "Hook", "Tell the Mars Climate Orbiter story. Ask: what single habit would have saved it?"],
  [8, "Why metric", "Compare converting 2 miles to inches with converting 2 km to cm. Let the student feel the difference."],
  [12, "Metric staircase", "Draw the staircase. Practice four conversions, connecting each to moving the decimal point from Math."],
  [12, "Reading tools", "On camera, measure something with a ruler to the millimeter and show water in a clear glass to point out the meniscus."],
  [10, "Accuracy, precision and data tables", "Use the dart targets. Complete the dissolving table together and describe the pattern."],
  [6, "Assign", "Assign the Kitchen Metric Lab, Think Deeper and the Exit Check."]],
 "key_questions": ["What unit goes with that number?", "Are you going up or down the staircase, so will you multiply or divide?", "Where should your eye be when you read the cylinder?", "Is that tool giving you accuracy, precision, both or neither?"],
 "misconceptions": ["Multiplying when converting to a larger unit (should divide).", "Reading the top of the meniscus.", "Using mass and weight as if they mean the same thing.", "Thinking precise measurements must be accurate."],
 "support": ["Give a printed metric staircase to keep beside the work.", "Use a place-value chart to show decimal points moving.", "Practice reading a ruler using a printed enlarged ruler."],
 "challenge": ["Ask the student to research the 2019 redefinition of the kilogram, which replaced a metal cylinder kept near Paris with a definition based on a constant of nature.", "Have the student convert a family recipe from cups and ounces to milliliters and grams."],
 "background": "<p>The Mars Climate Orbiter was lost on September 23, 1999. The NASA investigation board found that ground software produced thruster impulse data in pound-force seconds while the navigation software expected newton-seconds. The orbiter's cost is commonly reported as about $125 million (about $327.6 million for the whole Mars Surveyor 98 program, which also included the Mars Polar Lander). Since 2019 the kilogram has been defined using the Planck constant.</p>",
 "sources": ["NASA Jet Propulsion Laboratory: Mars Climate Orbiter mission overview.", "Mars Climate Orbiter Mishap Investigation Board Phase I Report (November 10, 1999).", "National Institute of Standards and Technology (NIST): SI units."]
}

PRINT = {
 "directions": "Show each conversion. Always include units.",
 "items": [
  {"q":"Convert:  7.2 km = ______ m    350 mL = ______ L    46 mm = ______ cm    0.08 kg = ______ g","a":"7,200 m; 0.35 L; 4.6 cm; 80 g","lines":2},
  {"q":"Name the tool and metric unit for each: the length of a pencil; the mass of a potato; the volume of juice in a glass; the temperature of a pool.","a":"ruler, cm; scale, g; measuring cup or graduated cylinder, mL; thermometer, °C","lines":3},
  {"q":"Explain how to read a graduated cylinder correctly.","a":"Put your eye level with the liquid and read the bottom of the meniscus.","lines":2},
  {"q":"Explain the difference between mass and weight. Would your mass change on Mars?","a":"Mass is the amount of matter; weight is the pull of gravity. Mass would not change on Mars; weight would be less.","lines":3},
  {"q":"A student measures a book three times: 412 g, 413 g, 412 g. The true mass is 450 g. Are the measurements accurate, precise, both or neither? Explain.","a":"Precise (close together) but not accurate (far from 450 g).","lines":2},
  {"q":"Draw a data table for testing how the height of a ramp changes how far a toy car rolls. Include headings with units and 3 trials.","a":"Ramp height (cm) | Trial 1 distance (cm) | Trial 2 (cm) | Trial 3 (cm) | Average (cm)","lines":3}]
}
