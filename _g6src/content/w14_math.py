LADDER = ('<svg viewBox="0 0 660 250" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Conversion ladders for customary length and capacity">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Customary units: each step is a ratio</text>'
  '<text x="165" y="44" text-anchor="middle" font-weight="bold" fill="#0047BA">Length</text><text x="495" y="44" text-anchor="middle" font-weight="bold" fill="#3d9a2f">Capacity</text>'
  + ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="6" fill="{c}"/><text x="{x+w/2}" y="{y+20}" text-anchor="middle" fill="#fff" font-weight="bold">{t}</text>'
            for x, y, w, t, c in [(105, 56, 120, "mile", "#0A1F3D"), (105, 106, 120, "yard", "#0047BA"), (105, 156, 120, "foot", "#0047BA"), (105, 206, 120, "inch", "#5b8fd6"),
                                  (435, 56, 120, "gallon", "#1f5e17"), (435, 106, 120, "quart", "#3d9a2f"), (435, 156, 120, "pint", "#3d9a2f"), (435, 206, 120, "cup", "#6bb35a")]) +
  ''.join(f'<text x="{x}" y="{y}" font-size="11">{t}</text>' for x, y, t in [(235, 95, "1 mile = 1,760 yards = 5,280 feet"), (235, 145, "1 yard = 3 feet"), (235, 195, "1 foot = 12 inches"),
                                                                              (565, 95, "1 gallon = 4 quarts"), (565, 145, "1 quart = 2 pints"), (565, 195, "1 pint = 2 cups")]) +
  '<path d="M90 70 v150" stroke="#DB2F30" stroke-width="2.5" marker-end="url(#ld)"/><text x="82" y="136" text-anchor="end" font-size="11" fill="#DB2F30">to a</text><text x="82" y="150" text-anchor="end" font-size="11" fill="#DB2F30">smaller</text><text x="82" y="164" text-anchor="end" font-size="11" fill="#DB2F30">unit:</text><text x="82" y="178" text-anchor="end" font-size="11" fill="#DB2F30" font-weight="bold">multiply</text>'
  '<path d="M420 220 v-150" stroke="#0A1F3D" stroke-width="2.5" marker-end="url(#lu)"/><text x="412" y="136" text-anchor="end" font-size="11">to a</text><text x="412" y="150" text-anchor="end" font-size="11">larger</text><text x="412" y="164" text-anchor="end" font-size="11">unit:</text><text x="412" y="178" text-anchor="end" font-size="11" font-weight="bold">divide</text>'
  '<defs><marker id="ld" viewBox="0 0 10 10" markerWidth="6" markerHeight="6" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="#DB2F30"/></marker><marker id="lu" viewBox="0 0 10 10" markerWidth="6" markerHeight="6" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="#0A1F3D"/></marker></defs>'
  '<text x="330" y="246" text-anchor="middle" font-size="11" fill="#5b6676">Weight: 1 pound = 16 ounces. Capacity: 1 cup = 8 fluid ounces.</text></svg>')

METRIC = ('<svg viewBox="0 0 660 190" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Metric prefixes as powers of ten">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Metric units: every step is a power of 10</text>'
  + ''.join(f'<rect x="{30+i*150}" y="40" width="130" height="78" rx="10" fill="{c}"/><text x="{95+i*150}" y="64" text-anchor="middle" fill="#fff" font-weight="bold" font-size="16">{p}</text><text x="{95+i*150}" y="84" text-anchor="middle" fill="#fff" font-size="11">{m}</text><text x="{95+i*150}" y="104" text-anchor="middle" fill="#fff" font-size="11">{ex}</text>'
            for i, (p, m, ex, c) in enumerate([("kilo-", "1,000 of the base", "1 km = 1,000 m", "#0A1F3D"), ("(base)", "meter, liter, gram", "m, L, g", "#0047BA"), ("centi-", "1/100 of the base", "100 cm = 1 m", "#3d9a2f"), ("milli-", "1/1,000 of the base", "1,000 mL = 1 L", "#DB2F30")])) +
  '<text x="330" y="146" text-anchor="middle" font-size="12">Converting is moving the decimal point: 2.5 km = 2,500 m; 350 cm = 3.5 m; 1.2 L = 1,200 mL</text>'
  '<text x="330" y="170" text-anchor="middle" font-size="11" fill="#5b6676">Roots: kilo (Greek, thousand), centi (Latin, hundred), milli (Latin, thousand).</text></svg>')

LESSON = {
 "unit": "Unit 3: Rates and Percents",
 "title": "Converting Units with Ratios, and Currency Exchange",
 "subtitle": "Feet and yards, cups and gallons, meters and kilometers, dollars and pesos: every conversion is a ratio. Get it right and a fence fits, a recipe works and a trip stays on budget.",
 "objectives": [
  "Use conversion ratios to convert customary units of length, capacity and weight.",
  "Convert metric units by using powers of 10.",
  "Choose whether to multiply or divide, and check that the answer makes sense.",
  "Use an exchange rate as a ratio to convert between currencies, including fees.",
  "Solve multi-step real-world problems that combine unit conversions, unit rates and money."],
 "vocab": [
  ["conversion factor", "A ratio of two equal amounts in different units, such as 12 inches : 1 foot."],
  ["customary units", "The measurement system used in the United States: inches, feet, cups, pounds and so on."],
  ["metric system", "A measurement system based on powers of 10: meters, liters, grams."],
  ["exchange rate", "How much of one currency equals one unit of another, such as 1 U.S. dollar = 18 Mexican pesos."],
  ["exchange fee", "A charge, often a percent, for changing money from one currency to another."]],
 "reconnect": {
  "title": "Week 13: Discounts, markups and tips",
  "intro": "Money and percents come back today. Warm up with last week's skills.",
  "items": [
   {"t":"num","q":"A $48 jacket is 25% off. What is the sale price?","a":36,"unit":"dollars","show":"$36","pts":2,"why":"Pay 75%: 0.75 × $48 = $36."},
   {"t":"num","q":"Find a 20% tip on a $55 bill.","a":11,"unit":"dollars","show":"$11","pts":2,"why":"10% = $5.50; double it: $11."},
   {"t":"num","q":"A craft seller's supplies cost $14. She uses a 50% markup. What is her selling price?","a":21,"unit":"dollars","show":"$21","pts":2,"why":"50% of $14 = $7; $14 + $7 = $21."},
   {"t":"open","key":"rc_stack","q":"Explain why 30% off followed by an extra 20% off is not the same as 50% off.","min":15,"rows":2,"rubric":["The second discount is a percent of the smaller sale price, not the original","Example: $100 → $70 → $56, a 44% total discount"],"model":"The extra 20% comes off the sale price, not the original price. On $100 you pay $70, then $56, which is only 44% off."}]},
 "hook": {
  "title": "The $125-Million Unit Mistake",
  "html": "<p>In 1999, NASA's Mars Climate Orbiter flew 416 million miles to Mars and then disappeared. Investigators found the cause: one team had calculated the spacecraft's thruster force in pounds (customary units), while another team's software expected newtons (metric units). Nobody converted. The orbiter flew too close to Mars and was lost.</p><p>Units mistakes happen at home, too: a fence that comes up three yards short, a recipe with three times too much salt, a vacation budget that runs out because of an exchange fee. Today you will learn to convert units and money with confidence.</p><div class='callout'><b>Big idea:</b> A conversion factor is a ratio of two equal amounts. Multiplying or dividing by it changes the units, not the amount.</div>"},
 "learn": [
  {"title": "Customary Length: Ratio Tables and Conversion Factors",
   "visual": LADDER,
   "html": "<p>Because 1 foot = 12 inches, the ratio of inches to feet is always 12 : 1. You can use a ratio table:</p><div class='card' style='font-family:Georgia,serif'>feet: 1, 2, 5, 7 <br>inches: 12, 24, 60, 84</div><p>Or multiply by the conversion factor. Going to a <b>smaller</b> unit, you need <b>more</b> of them, so multiply: 7 feet × 12 = 84 inches. Going to a <b>larger</b> unit, you need <b>fewer</b>, so divide: 54 inches ÷ 12 = 4.5 feet.</p><p><b>Check:</b> ask, \"Should my number get bigger or smaller?\" Inches are small, so a length in inches should be a bigger number than the same length in feet.</p>",
   "checks": [
    {"t":"num","q":"A homeschool garden bed is 7 feet long. How many inches is that?","a":84,"unit":"inches","pts":2,"why":"Smaller unit, so multiply: 7 × 12 = 84."},
    {"t":"num","q":"A child is 54 inches tall. How many feet is that? Write a decimal.","a":4.5,"unit":"feet","pts":2,"why":"Larger unit, so divide: 54 ÷ 12 = 4.5 feet (4 feet 6 inches)."},
    {"t":"num","q":"A family hikes 2 miles. How many feet is that?","a":10560,"unit":"feet","pts":2,"why":"2 × 5,280 = 10,560 feet."},
    {"t":"num","q":"A soccer field is 120 yards long. How many feet is that?","a":360,"unit":"feet","pts":2,"why":"120 × 3 = 360 feet."},
    {"t":"open","key":"biggersmaller","q":"Leo converts 15 feet to yards and gets 45 yards. Explain his mistake and give the correct answer.","min":20,"rows":2,"rubric":["He multiplied instead of dividing; yards are larger, so the number should be smaller","Correct answer: 5 yards"],"model":"He multiplied by 3, but yards are bigger than feet, so there should be fewer of them. He should divide: 15 ÷ 3 = 5 yards."}]},
  {"title": "Capacity and Weight in the Kitchen and Barn",
   "html": "<p>Capacity units build on one another: 2 cups = 1 pint, 2 pints = 1 quart, 4 quarts = 1 gallon. So 1 gallon = 4 quarts = 8 pints = 16 cups. Weight: 16 ounces = 1 pound.</p><p>For a multi-step conversion, chain the ratios: 3 gallons → 3 × 4 = 12 quarts → 12 × 2 = 24 pints → 24 × 2 = 48 cups.</p><p>Watch out: a <b>fluid ounce</b> measures capacity (1 cup = 8 fluid ounces), but an <b>ounce</b> on a scale measures weight. They are not the same thing.</p>",
   "checks": [
    {"t":"num","q":"A canning recipe needs 3 quarts of water. How many cups is that?","a":12,"unit":"cups","pts":2,"why":"3 × 2 = 6 pints; 6 × 2 = 12 cups (or 1 quart = 4 cups)."},
    {"t":"num","q":"A family's goats give 2 gallons of milk a day. How many pints is that?","a":16,"unit":"pints","pts":2,"why":"2 × 4 = 8 quarts; 8 × 2 = 16 pints."},
    {"t":"num","q":"A bag of chicken feed weighs 50 pounds. How many ounces is that?","a":800,"unit":"ounces","pts":2,"why":"50 × 16 = 800 ounces."},
    {"t":"num","q":"A package of ground turkey weighs 40 ounces. How many pounds is that?","a":2.5,"unit":"pounds","pts":2,"why":"40 ÷ 16 = 2.5 pounds."},
    {"t":"open","key":"flozoz","q":"A recipe says \"8 ounces of honey.\" Ana pours 1 cup (8 fluid ounces) of honey. Is that the same thing? Explain.","min":20,"rows":2,"rubric":["Not necessarily: fluid ounces measure volume, ounces measure weight","Honey is heavier than water, so 1 cup of honey weighs more than 8 ounces (she should weigh it)"],"model":"No. Fluid ounces measure how much space something takes up, but ounces on a scale measure weight. Honey is heavier than water, so a cup of honey weighs more than 8 ounces. She should weigh it."}]},
  {"title": "The Metric System: Powers of 10",
   "visual": METRIC,
   "html": "<p>Most of the world, and scientists everywhere, use the <b>metric system</b>. Every unit is 10, 100 or 1,000 times another, so converting means moving the decimal point.</p><ul><li>1 kilometer (km) = 1,000 meters (m)</li><li>1 meter = 100 centimeters (cm) = 1,000 millimeters (mm)</li><li>1 liter (L) = 1,000 milliliters (mL)</li><li>1 kilogram (kg) = 1,000 grams (g)</li></ul><p>Multiply by 1,000: move the decimal 3 places right. Divide by 100: move it 2 places left. You used centimeters to measure leaves in Science and milliliters in the Indus drain test.</p>",
   "checks": [
    {"t":"num","q":"A cross-country race is 2.5 kilometers. How many meters is that?","a":2500,"unit":"meters","pts":2,"why":"2.5 × 1,000 = 2,500 m."},
    {"t":"num","q":"A sunflower is 350 centimeters tall. How many meters is that?","a":3.5,"unit":"meters","pts":2,"why":"350 ÷ 100 = 3.5 m."},
    {"t":"num","q":"A water bottle holds 1.2 liters. How many milliliters is that?","a":1200,"unit":"mL","pts":2,"why":"1.2 × 1,000 = 1,200 mL."},
    {"t":"open","key":"whymetric","q":"Compare converting 3.2 kilometers to meters with converting 3.2 miles to feet. Which is easier, and why?","min":20,"rows":2,"rubric":["Kilometers is easier: multiply by 1,000 (move the decimal) = 3,200 m","Miles needs 5,280, a harder number (16,896 feet); metric uses powers of 10"],"model":"Kilometers is easier: 3.2 × 1,000 = 3,200 meters, just a decimal move. Miles to feet means 3.2 × 5,280 = 16,896, which takes real multiplication, because customary units don't use powers of 10."}]},
  {"title": "Money: Currency Exchange",
   "html": "<p>Different countries use different money. An <b>exchange rate</b> is a ratio that tells how much of one currency equals another. Rates change every day; the rates in this lesson are examples for practice.</p><div class='card' style='font-family:Georgia,serif'>Example rates: 1 U.S. dollar (USD) = 0.90 euro (EUR) &nbsp;|&nbsp; 1 USD = 18 Mexican pesos (MXN) &nbsp;|&nbsp; 1 USD = 155 Jamaican dollars (JMD)</div><p><b>Dollars to another currency:</b> multiply. $200 × 0.90 = 180 euros. <b>Another currency to dollars:</b> divide. 3,100 JMD ÷ 155 = $20.</p><p>Banks, airports and card companies often charge an <b>exchange fee</b>, usually a percent. With a 3% fee on $200, you pay $6, so only $194 is exchanged: $194 × 0.90 = 174.60 euros.</p>",
   "checks": [
    {"t":"num","q":"At 1 USD = 18 MXN, how many Mexican pesos do you get for $50?","a":900,"unit":"pesos","pts":2,"why":"50 × 18 = 900 pesos."},
    {"t":"num","q":"A souvenir in Jamaica costs 4,650 Jamaican dollars. At 1 USD = 155 JMD, how much is that in U.S. dollars?","a":30,"unit":"dollars","show":"$30","pts":2,"why":"4,650 ÷ 155 = $30."},
    {"t":"num","q":"You exchange $300 for euros at 1 USD = 0.90 EUR, but the airport charges a 5% fee first. How many euros do you receive?","a":256.5,"unit":"euros","show":"256.50 euros","pts":3,"why":"Fee: 5% of $300 = $15, leaving $285. $285 × 0.90 = 256.50 euros."},
    {"t":"open","key":"sandwich","q":"In Paris, a sandwich costs 9 euros. At home the same sandwich costs $9.50. At 1 USD = 0.90 EUR, which is more expensive? Show your work.","min":20,"rows":2,"rubric":["Converts 9 euros to dollars: 9 ÷ 0.90 = $10","Concludes Paris is more expensive by $0.50"],"model":"9 euros ÷ 0.90 = $10. So the Paris sandwich costs $10, which is $0.50 more than the $9.50 one at home."}]}],
 "handson": {
  "title": "Measure Your Home Three Ways",
  "intro": "Measure, pour and pace around your home, then convert every measurement with ratios.",
  "materials": ["A tape measure or yardstick (inches and centimeters)", "A 1-cup measure and a clean gallon jug or pitcher", "Water (work in a sink or outdoors)", "Paper and pencil", "A calculator for checking only", "Optional: a kitchen scale"],
  "steps": [
   "Length: measure three things in inches (a door, a table, your bed). Convert each to feet and to yards. Then measure one in centimeters and convert to meters.",
   "Capacity: count how many cups of water it takes to fill the gallon jug. Use your count to find how many cups are in a quart and a pint. Pour the water onto plants afterward and wipe up spills.",
   "Pacing: walk 10 normal steps and measure the total distance in inches. Find the length of one step. Then count the steps across your yard or a hallway and convert the distance to feet and yards.",
   "Optional: weigh a bag of flour or rice in ounces and convert to pounds; compare with the label."],
  "record": [
   {"t":"open","key":"measurerec","q":"Record your measurements and conversions for length, capacity and pacing. Show the ratio or operation you used for each.","min":40,"rows":6,"rubric":["Three length measurements converted to feet and yards, one to meters","Cups to fill a gallon recorded and used for quarts and pints","Step length and paced distance converted","Correct multiply or divide each time"],"model":"Door: 80 in ÷ 12 = 6 2/3 ft; ÷ 36 = 2 2/9 yd. Table: 72 in = 6 ft = 2 yd. Bed: 75 in = 6.25 ft. Door in cm: 203 cm ÷ 100 = 2.03 m. Gallon: 16 cups, so a quart is 16 ÷ 4 = 4 cups and a pint is 2 cups. 10 steps = 240 in, so 1 step = 24 in = 2 ft. Yard: 45 steps × 2 ft = 90 ft = 30 yd."},
   {"t":"open","key":"measurecheck","q":"Did your gallon count match the 16 cups in the lesson? If not, give two reasons your count might be off.","min":20,"rows":2,"rubric":["Compares the count with 16","Two sensible sources of error (cups not filled exactly, spills, jug not exactly a gallon, foam or bubbles)"],"model":"I counted 16 1/2 cups. My cups were probably not filled exactly to the line, and some water spilled, so my count was a little off."}]},
 "think": {
  "intro": "Show your calculations, then explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"fence","q":"A family needs 150 feet of fencing for a goat pen. Fencing is sold in rolls of 10 yards for $24 per roll. How many rolls should they buy, and what will it cost? Then explain what could go wrong if they forgot to convert units.","min":60,"rows":5,"rubric":["Converts 150 feet to 50 yards","5 rolls; $120","Explains the error (thinking 150 feet means 15 rolls and spending $360, or buying too little)"],"model":"150 feet ÷ 3 = 50 yards. Each roll is 10 yards, so they need 50 ÷ 10 = 5 rolls, costing 5 × $24 = $120. If they forgot to convert, they might think they need 150 ÷ 10 = 15 rolls and spend $360, three times too much."},
   {"t":"open","key":"exchangeplace","q":"A family is taking $300 to Mexico. The airport exchange gives 16.5 pesos per dollar. A bank at home gives 17.8 pesos per dollar. How many more pesos does the bank give? About how many dollars is that difference worth? Should they care? Explain.","min":60,"rows":5,"rubric":["Airport 4,950 pesos; bank 5,340 pesos; difference 390 pesos","390 ÷ 17.8 ≈ $21.91 (about $22)","A reasoned judgment (yes: about 8% more money; compare rates and fees before exchanging)"],"model":"Airport: 300 × 16.5 = 4,950 pesos. Bank: 300 × 17.8 = 5,340 pesos. The bank gives 390 more pesos, which is about 390 ÷ 17.8 ≈ $21.91. Yes, they should care: that is about 8% more money, enough for a few meals, just for comparing rates before they travel."}]},
 "exit": [
  {"t":"num","q":"How many yards are in 9 feet?","a":3,"unit":"yards","pts":2,"why":"9 ÷ 3 = 3 yards."},
  {"t":"num","q":"How many cups are in 6 quarts?","a":24,"unit":"cups","pts":2,"why":"6 × 4 = 24 cups."},
  {"t":"num","q":"How many grams are in 4.2 kilograms?","a":4200,"unit":"grams","pts":2,"why":"4.2 × 1,000 = 4,200 g."},
  {"t":"num","q":"At 1 USD = 155 JMD, how many Jamaican dollars do you get for $40?","a":6200,"unit":"Jamaican dollars","pts":2,"why":"40 × 155 = 6,200 JMD."}],
 "next": "Week 15: mid-year review and checkpoint."
}

TEACHER = {
 "standards": [
  "MA.6.AR.3.5: Solve mathematical and real-world problems involving ratios, rates and unit rates, including comparisons, mixtures, ratios of lengths and conversions within the same measurement system.",
  "MA.K12.MTR.2.1: Demonstrate understanding by representing problems in multiple ways.",
  "MA.K12.MTR.7.1: Apply mathematics to real-world contexts.",
  "Financial literacy: exchange rates and exchange fees (Jump$tart Spending)."],
 "materials": ["The interactive lesson", "A tape measure or yardstick, a 1-cup measure, a gallon jug, water", "Paper, pencil, a calculator for checking only", "Optional: a kitchen scale", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 13 Reconnect questions."],
  [4, "Hook", "Tell the Mars Climate Orbiter story."],
  [13, "Customary length", "Use ratio tables and the bigger-or-smaller check. Fix Leo's mistake."],
  [10, "Capacity and weight", "Chain ratios from gallons to cups. Discuss fluid ounces versus ounces."],
  [9, "Metric", "Move decimals by powers of 10. Connect the prefixes to roots."],
  [12, "Currency exchange", "Multiply to convert dollars out; divide to convert back. Work a fee problem."],
  [6, "Assign", "Measure one object together; assign the rest of the hands-on, Think Deeper and the Exit Check."]],
 "key_questions": ["Should the number get bigger or smaller?", "What ratio connects these two units?", "Which direction does the exchange rate go?", "How does a fee change what you receive?"],
 "misconceptions": ["Multiplying when converting to a larger unit.", "Treating fluid ounces and ounces as the same.", "Using 10 or 100 for customary units.", "Multiplying by the exchange rate when converting back to dollars."],
 "support": ["Use ratio tables for every conversion.", "Post the conversion ladder.", "Start currency problems with whole-number rates (18 and 155) before 0.90."],
 "challenge": ["Convert your height to millimeters and to miles.", "Find today's real exchange rate for the euro and compare it with the lesson's example rate."],
 "background": "<p>Mars Climate Orbiter was lost September 23, 1999; the mishap investigation board found that ground software reported thruster impulse in pound-force seconds while navigation software expected newton-seconds. The orbiter cost about $125 million (the full mission about $328 million). Customary equivalences: 1 mi = 1,760 yd = 5,280 ft; 1 gal = 4 qt = 8 pt = 16 c; 1 c = 8 fl oz; 1 lb = 16 oz. Exchange rates in the lesson are examples, not current market rates; MA.6.AR.3.5 limits conversions to within one measurement system, so the lesson does not convert between metric and customary units.</p>",
 "sources": ["NASA, Mars Climate Orbiter Mishap Investigation Board Phase I Report (1999).", "NIST Handbook 44, Appendix C: General Tables of Units of Measurement.", "Federal Reserve, Foreign Exchange Rates (for current rates).", "Jump$tart Coalition, National Standards for Personal Financial Education (Spending)."]
}

PRINT = {
 "directions": "Show your work.",
 "items": [
  {"q":"Convert 8 feet to inches and 8 feet to yards.","a":"96 inches; 2 2/3 yards.","lines":2},
  {"q":"How many cups are in 2 1/2 gallons?","a":"40 cups.","lines":1},
  {"q":"Convert 3,750 grams to kilograms.","a":"3.75 kg.","lines":1},
  {"q":"Convert 72 ounces to pounds.","a":"4.5 pounds.","lines":1},
  {"q":"At 1 USD = 0.90 EUR, how many euros is $80? How many dollars is 45 euros?","a":"72 euros; $50.","lines":2},
  {"q":"You exchange $250 with a 4% fee at 1 USD = 18 MXN. How many pesos do you receive?","a":"Fee $10; $240 × 18 = 4,320 pesos.","lines":2}]
}
