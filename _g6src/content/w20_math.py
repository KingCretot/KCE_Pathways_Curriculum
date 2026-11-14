TOOLKIT = ('<svg viewBox="0 0 640 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Unit 4 toolkit: integers, coordinate plane, adding and subtracting, multiplying and dividing">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Unit 4 toolkit</text>'
  + ''.join(f'<g transform="translate({16+i*156},36)"><rect width="144" height="180" rx="12" fill="{c}"/><text x="72" y="24" text-anchor="middle" fill="#fff" font-weight="bold" font-size="12">{a}</text>'
            + ''.join(f'<text x="72" y="{50+j*18}" text-anchor="middle" fill="#fff" font-size="11">{t}</text>' for j, t in enumerate(lines)) + '</g>'
            for i, (a, c, lines) in enumerate([
              ("Week 16: Integers", "#0A1F3D", ["opposites: 7 and −7", "|−7| = 7", "farther left = less", "zero has a meaning", "(sea level, $0, 0°)", "bank balances"]),
              ("Week 17: The plane", "#0047BA", ["(x, y): across, then", "up or down", "quadrants I to IV", "flip a sign = reflect", "distance: add or", "subtract | |"]),
              ("Week 18: + and −", "#2c6e22", ["same signs: add,", "keep the sign", "different: subtract,", "sign of the larger", "a − b = a + (−b)", "debt and credit"]),
              ("Week 19: × and ÷", "#DB2F30", ["same signs: +", "different signs: −", "count negatives", "average change", "= total ÷ periods", "profit and loss"])])) +
  '</svg>')

LESSON = {
 "unit": "Unit 4: Integers and the Coordinate Plane",
 "title": "Unit 4 Review and Checkpoint",
 "subtitle": "This week you pull together everything from Unit 4, from opposites and absolute value to all four operations with integers and the coordinate plane, and use it to review a small business's money, then show your mastery on the Unit 4 checkpoint.",
 "objectives": [
  "Choose the right integer tool for a problem: absolute value, a coordinate distance or an operation.",
  "Compute with integers using all four operations and the order of operations.",
  "Plot points, reflect them and find distances on the coordinate plane.",
  "Interpret integers in real contexts: elevation, temperature, balances, debt, profit and loss.",
  "Demonstrate mastery of Unit 4 on the checkpoint (85 or higher)."],
 "vocab": [
  ["integer", "A whole number or its opposite."],
  ["absolute value", "A number's distance from zero."],
  ["ordered pair", "(x, y): a location on the coordinate plane."],
  ["additive inverse", "A number's opposite; together they make 0."],
  ["average change", "Total change divided by the number of periods."],
  ["net worth", "What you own minus what you owe."]],
 "reconnect": {
  "title": "Unit 4, one question from each week",
  "intro": "Warm up with one question from each week of the unit.",
  "items": [
   {"t":"num","q":"Week 16: What is |−38|?","a":38,"pts":2,"why":"Distance from zero."},
   {"t":"text","q":"Week 17: Reflect (−4, 7) across the y-axis. Type the ordered pair.","a":["^(4, 7)","^(4,7)","^4, 7"],"show":"(4, 7)","pts":2,"why":"Across the y-axis, x changes sign."},
   {"t":"num","q":"Week 18: −13 − (−20) = ?","a":7,"pts":2,"why":"−13 + 20 = 7."},
   {"t":"num","q":"Week 19: (−48) ÷ 6 × (−2) = ?","a":16,"pts":2,"why":"−48 ÷ 6 = −8; −8 × (−2) = 16."}]},
 "hook": {
  "title": "Maya's Year-End Review",
  "visual": TOOLKIT,
  "html": "<p>Maya's sourdough business has had a busy fall. She borrowed money for a mixer, mapped delivery routes, had good weeks and bad weeks, and now she wants to know: how is her business really doing? Is she ahead or behind? What should she change for next year?</p><p>Every question she asks needs a tool from Unit 4. This week you'll help her answer them, then take the Unit 4 checkpoint.</p><div class='callout'><b>Big question:</b> How do positive and negative numbers help us describe and make decisions about the real world?</div>"},
 "learn": [
  {"title": "Review: Integers, Opposites and Absolute Value",
   "html": "<p>Integers describe quantities with opposite directions, and <b>zero</b> always has a meaning in context: sea level, a balance of $0, the freezing point on the Celsius scale. On a number line, numbers increase to the right, so −15 is less than −4. <b>Absolute value</b> is distance from zero: |−15| = 15. A bigger debt has a greater absolute value but a smaller (more negative) balance.</p>",
   "checks": [
    {"t":"order","q":"Order from least to greatest: 3, −9, 0, −2, 7, −12","items":["−12","−9","−2","0","3","7"],"pts":2,"why":"Farther left on the number line is less."},
    {"t":"open","key":"revdebt","q":"Account A has a balance of −$30 and account B has −$75. Which balance is greater, and which account has the bigger debt? Explain how both can be true.","min":25,"rows":3,"rubric":["−30 is greater (to the right of −75)","Account B has the bigger debt (|−75| = 75 > 30)","Explains the difference between comparing values and comparing absolute values"],"model":"−$30 is the greater balance because it is to the right of −$75 on a number line. But account B has the bigger debt, because |−75| = 75 is larger than |−30| = 30. Comparing balances compares the numbers; comparing debts compares their absolute values."}]},
  {"title": "Review: The Coordinate Plane",
   "html": "<p>Plot (x, y) by moving across first, then up or down. The signs tell the quadrant: I (+, +), II (−, +), III (−, −), IV (+, −). Changing the sign of x reflects a point across the y-axis; changing the sign of y reflects it across the x-axis. For points that share a coordinate, find the distance with absolute values: add them if the points are on opposite sides of an axis, subtract if they're on the same side.</p>",
   "checks": [
    {"t":"num","q":"How many units apart are (−3, −6) and (−3, 9)?","a":15,"unit":"units","pts":2,"why":"Opposite sides: |−6| + |9| = 15."},
    {"t":"open","key":"revsquare","q":"Three corners of a square are (−2, 3), (4, 3) and (4, −3). Find the fourth corner and the area. Explain how you know it is a square.","min":30,"rows":3,"rubric":["Fourth corner (−2, −3)","Sides of 6 and 6 found with absolute value, so it is a square","Area 36 square units"],"model":"The fourth corner is (−2, −3). The top side, from (−2, 3) to (4, 3), is |−2| + |4| = 6 units, and the right side, from (4, 3) to (4, −3), is |3| + |−3| = 6 units. All sides are 6, so it's a square, and the area is 6 × 6 = 36 square units."}]},
  {"title": "Review: All Four Operations",
   "html": "<p><b>Add:</b> same signs, add absolute values and keep the sign; different signs, subtract and take the sign of the larger absolute value. <b>Subtract:</b> add the opposite. <b>Multiply and divide:</b> same signs give a positive answer; different signs give a negative answer. Follow the order of operations: multiply and divide left to right, then add and subtract left to right.</p>",
   "checks": [
    {"t":"num","q":"Evaluate: −6 + 4 × (−5) − (−18) ÷ 3","a":-20,"pts":2,"why":"4 × (−5) = −20; −18 ÷ 3 = −6; −6 + (−20) − (−6) = −6 − 20 + 6 = −20."},
    {"t":"open","key":"reverror","q":"Leo wrote: −8 − 5 × (−2) = −13 × (−2) = 26. Find his mistake, explain it, and give the correct answer.","min":19,"rows":3,"rubric":["He subtracted before multiplying (order of operations)","Correct work: 5 × (−2) = −10; −8 − (−10) = −8 + 10 = 2"],"model":"Leo subtracted first, but multiplication comes before subtraction. 5 × (−2) = −10, then −8 − (−10) = −8 + 10 = 2."}]},
  {"title": "Money: Year-End Money Review",
   "html": "<p>Maya's year-end numbers (in dollars):</p><div class='card' style='font-family:Courier New,monospace;font-size:14px'>Cash in her business account &nbsp;&nbsp;&nbsp;&nbsp;+$185<br>Mixer loan still owed to parents &nbsp;&nbsp;−$30<br>Credit owed to the flour mill &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;−$22<br>Value of baking equipment &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+$140<br>Profit or loss, last 4 weeks: +$52, −$18, +$40, +$34</div><p>Her <b>net worth</b> is what she owns minus what she owes. Her <b>average weekly profit</b> tells her whether the business is growing.</p>",
   "checks": [
    {"t":"num","q":"What is Maya's net worth? (Add everything she owns and everything she owes, as integers.)","a":273,"unit":"dollars","pts":2,"why":"185 + 140 = 325 owned; −30 + (−22) = −52 owed; 325 + (−52) = 273."},
    {"t":"num","q":"What was her average weekly profit for the last 4 weeks?","a":27,"unit":"dollars","pts":2,"why":"52 − 18 + 40 + 34 = 108; 108 ÷ 4 = 27."},
    {"t":"open","key":"yearplan","q":"Write Maya two pieces of advice for next year, each backed by one of her numbers.","min":40,"rows":4,"rubric":["Two pieces of advice","Each supported with a specific number and correct reasoning (pay off the loan and mill credit with her cash; average $27 profit suggests steady growth; avoid loss weeks)"],"model":"First, she should pay off the $30 loan and the $22 she owes the mill now, since she has $185 in cash; then she won't owe anyone. Second, her average profit of $27 a week is good, but the −$18 week shows one bad week can erase a lot, so she should keep $50 saved for emergencies like a flour price jump."}]}],
 "handson": {
  "title": "Integer Escape Room",
  "intro": "Solve a chain of integer clues to \"escape,\" moving around your home for each clue.",
  "materials": ["5 envelopes or folded papers", "Paper, pencil and tape", "A family member to hide the clues", "A small treat or prize (optional; check for food allergies and keep treats away from pets)"],
  "steps": [
   "A family member copies the five clues below onto papers, puts each in an envelope, and hides them around the house. The answer to each clue tells where the next one is hidden (for example, 5 = bookshelf, −17 = kitchen, 12 = front door, −12 = closet, −3 = the prize spot). The family member makes a key.",
   "Clue 1: Find |−9| − |4|. Clue 2: A diver at −14 feet rises 6 feet, then dives 9 more. Where is she? Clue 3: What is the distance between (−5, 2) and (7, 2)? Clue 4: (−2) × (−3) × (−1) × 2 = ? Clue 5: The temperature changed −24 degrees over 8 hours. What was the average change per hour?",
   "Solve each clue on paper before moving. Show your work.",
   "When you reach the last envelope, write one new clue of your own for a family member to solve."],
  "record": [
   {"t":"open","key":"escaperec","q":"Show your work and answer for all five clues. Then write the clue you invented and its answer.","min":40,"rows":6,"rubric":["Clue 1: 5; Clue 2: −17; Clue 3: 12; Clue 4: −12; Clue 5: −3","Work shown","A correct original clue with answer"],"model":"Clue 1: 9 − 4 = 5. Clue 2: −14 + 6 − 9 = −17 feet. Clue 3: |−5| + |7| = 12. Clue 4: three negatives, so negative: 2 × 3 × 1 × 2 = 12, so −12. Clue 5: −24 ÷ 8 = −3 degrees per hour. My clue: \"A balance of −$40 gets three payments of $15. What is the new balance?\" Answer: −40 + 45 = $5."}]},
 "think": {
  "intro": "Explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"unitletter","q":"Write a letter to a younger student explaining what negative numbers are and how to add, subtract, multiply and divide them. Use at least two real-life examples and one number line or counter explanation.","min":102,"rows":9,"rubric":["Explains what negative numbers mean (opposites, below zero)","Correct explanation for each operation","At least two real-life examples","A number line or counter model","Clear and friendly"],"model":"Dear Sam, negative numbers are numbers less than zero, like a temperature of −5° on a cold morning or a bank balance of −$10 when you owe money. On a number line they go to the left of zero. To add, think of moving: adding a positive moves right, adding a negative moves left, so 3 + (−7) lands on −4. To subtract, add the opposite: 2 − (−5) is 2 + 5 = 7, like canceling a $5 debt. To multiply or divide, work out the numbers first, then the sign: if the signs match, the answer is positive; if they're different, it's negative. So (−3) × 4 = −12, but (−3) × (−4) = 12. Your friend, Jordan"}]},
 "checkpoint": {
  "title": "Unit 4 Checkpoint: Integers and the Coordinate Plane",
  "intro": "This checkpoint covers Weeks 16 to 19. Work each problem on paper, then type your answer. Type negative numbers with a minus sign. Mastery is 85 or higher. If you score below 85, your teacher will review with you, then you will retake it.",
  "parts": [
   {"title": "Part A: Integers and absolute value", "items": [
    {"t":"num","q":"The bottom of a Florida spring is 42 feet below the water's surface. Write the bottom as an integer, with the water's surface as 0.","a":-42,"unit":"feet","pts":3,"why":"Below the surface is negative."},
    {"t":"text","q":"Which is greater, −11 or −7? Type only the greater number.","a":["^-7","^−7"],"show":"−7","pts":3,"why":"−7 is to the right of −11."},
    {"t":"num","q":"What is the opposite of |−16|?","a":-16,"pts":3,"why":"|−16| = 16; its opposite is −16."},
    {"t":"open","q":"A diver is at −35 feet and a pelican is flying at 28 feet. Which is farther from sea level, and by how many feet? Explain using absolute value.","key":"cpdiver","min":19,"rows":2,"pts":4,"rubric":["The diver","|−35| = 35 and |28| = 28; 35 − 28 = 7 feet farther"],"model":"The diver is farther from sea level: |−35| = 35 feet and |28| = 28 feet, so the diver is 7 feet farther."}]},
   {"title": "Part B: The coordinate plane", "items": [
    {"t":"text","q":"Which quadrant contains (6, −2.5)? Type the Roman numeral.","a":[{"all":[["iv","4"]],"none":["iii"]}],"show":"IV","pts":3,"why":"(+, −)."},
    {"t":"text","q":"Reflect (−8, −3) across the x-axis. Type the ordered pair.","a":["(−8, 3)","(-8,3)","-8, 3"],"show":"(−8, 3)","pts":3,"why":"Across the x-axis, y changes sign."},
    {"t":"num","q":"How many units apart are (−9, 4) and (−1, 4)?","a":8,"unit":"units","pts":3,"why":"Same side: 9 − 1 = 8."},
    {"t":"open","q":"A rectangle has corners at (−5, 2), (3, 2), (3, −4) and (−5, −4). Find its perimeter and area. Show how you found each side length.","key":"cprect","min":25,"rows":3,"pts":4,"rubric":["Sides 8 and 6 found with absolute values","Perimeter 28 units","Area 48 square units"],"model":"Top side: |−5| + |3| = 8 units. Right side: |2| + |−4| = 6 units. Perimeter: 8 + 6 + 8 + 6 = 28 units. Area: 8 × 6 = 48 square units."}]},
   {"title": "Part C: Operations with integers", "items": [
    {"t":"num","q":"−17 + 9 = ?","a":-8,"pts":3,"why":"Different signs: 17 − 9 = 8, negative."},
    {"t":"num","q":"−8 − 14 = ?","a":-22,"pts":3,"why":"−8 + (−14) = −22."},
    {"t":"num","q":"(−7) × (−9) = ?","a":63,"pts":3,"why":"Same signs: positive."},
    {"t":"num","q":"Evaluate: 20 ÷ (−4) − 3 × (−6)","a":13,"pts":3,"why":"−5 − (−18) = −5 + 18 = 13."},
    {"t":"open","q":"Explain why −5 − (−8) equals 3. Use a number line, counters or a real-life example.","key":"cpwhy","min":20,"rows":2,"pts":4,"rubric":["Subtracting −8 means adding 8 (or removing a debt)","Correct model or story reaching 3"],"model":"Subtracting −8 is the same as adding 8. Start at −5 on a number line and move 8 to the right: you land on 3. It's like owing $5 and then having an $8 debt canceled."}]},
   {"title": "Part D: Integers in the real world", "items": [
    {"t":"num","q":"At 5 a.m. the temperature was −11°F. By noon it was 16°F. What was the change in temperature?","a":27,"unit":"degrees","pts":3,"why":"16 − (−11) = 27."},
    {"t":"num","q":"A credit card balance is −$140. The owner pays $65, then buys a $28 book. What is the new balance?","a":-103,"unit":"dollars","pts":3,"why":"−140 + 65 − 28 = −103."},
    {"t":"num","q":"A business had weekly results of +$45, −$15, +$30 and −$20. What was its average weekly profit?","a":10,"unit":"dollars","pts":3,"why":"40 ÷ 4 = 10."},
    {"t":"open","q":"A submarine descends at 15 feet per minute for 6 minutes, then rises 40 feet. Write one expression for its final depth, evaluate it, and explain what your answer means.","key":"cpsub","min":16,"rows":3,"pts":4,"rubric":["Expression such as 6 × (−15) + 40","Value −50","Meaning: 50 feet below the surface"],"model":"6 × (−15) + 40 = −90 + 40 = −50. The submarine ends 50 feet below the surface."}]}]},
 "next": "Unit 5: expressions and equations, starting with exponents and the order of operations."
}

TEACHER = {
 "standards": [
  "MA.6.NSO.1.1: Extend previous understanding of numbers to define rational numbers. Plot, order and compare rational numbers.",
  "MA.6.NSO.1.2: Given a mathematical or real-world context, represent quantities that have opposite direction using rational numbers. Compare them on a number line and explain the meaning of zero within its context.",
  "MA.6.NSO.1.3: Given a mathematical or real-world context, interpret the absolute value of a number as the distance from zero on a number line. Find the absolute value of rational numbers.",
  "MA.6.NSO.4.1: Apply and extend previous understandings of operations with whole numbers to add and subtract integers with procedural fluency.",
  "MA.6.NSO.4.2: Apply and extend previous understandings of operations with whole numbers to multiply and divide integers with procedural fluency.",
  "MA.6.GR.1.1: Extend previous understanding of the coordinate plane to plot rational number ordered pairs in all four quadrants and on both axes. Identify the x- or y-axis as the line of reflection when two ordered pairs have an opposite x- or y-coordinate.",
  "MA.6.GR.1.2: Find distances between ordered pairs, limited to the same x-coordinate or the same y-coordinate, represented on the coordinate plane."],
 "materials": ["The interactive lesson", "5 envelopes or folded papers, paper, pencil, tape", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run one question from each week of the unit."],
  [4, "Hook", "Maya's year-end review and the toolkit chart."],
  [9, "Integers and absolute value", "Order integers; balances versus debts."],
  [9, "Coordinate plane", "Distances and the square problem."],
  [9, "Operations", "Order of operations with integers; fix Leo's mistake."],
  [9, "Money review", "Net worth and average weekly profit; advice for Maya."],
  [4, "Assign", "Assign the escape room and Think Deeper."],
  [10, "Checkpoint preview", "Explain that the checkpoint is completed after class, independently, one try per item, with no answers shown until you review it. Mastery is 85; below 85 means a review lesson and a retake."]],
 "key_questions": ["Which tool fits this problem?", "What does zero mean here?", "Same side or opposite sides?", "Same signs or different signs?"],
 "misconceptions": ["A bigger debt is a greater number.", "Two negatives make a positive when adding.", "Subtract before multiplying.", "Points on an axis belong to a quadrant."],
 "support": ["Keep the Unit 4 toolkit chart visible during review (not during the checkpoint).", "Allow counters and a number line during review.", "Read checkpoint word problems aloud if reading is a barrier."],
 "challenge": ["Create a five-clue integer escape room for a family member.", "Find the net worth of an imaginary business with ten entries."],
 "background": "<p>The checkpoint is scored out of 55 points: Part A 13, Part B 13, Part C 16, Part D 13. A score of 85 percent is about 47 of 55 points. Open items are scored with the rubric after submission.</p>",
 "sources": ["Florida Department of Education, B.E.S.T. Standards for Mathematics (2020).", "Jump$tart Coalition, National Standards for Personal Financial Education (2021)."]
}

PRINT = {
 "directions": "Show your work. This is review practice, not the checkpoint.",
 "items": [
  {"q":"Order from least to greatest: −4, 6, −10, 0, −1, 3.","a":"−10, −4, −1, 0, 3, 6.","lines":1},
  {"q":"Name the quadrant of each point: (−3, 5), (2, −7), (−1, −1).","a":"II; IV; III.","lines":1},
  {"q":"Find the distance between (4, −6) and (4, 5).","a":"|−6| + |5| = 11 units.","lines":2},
  {"q":"Evaluate: (a) −12 + (−9) (b) 8 − 15 (c) −36 ÷ (−4) (d) 7 × (−6)","a":"(a) −21 (b) −7 (c) 9 (d) −42","lines":2},
  {"q":"Evaluate: −10 + 6 × (−3) ÷ 2","a":"6 × (−3) = −18; −18 ÷ 2 = −9; −10 + (−9) = −19.","lines":2},
  {"q":"A balance of −$60 receives payments of $25 and $25, then a $12 purchase. Find the balance.","a":"−60 + 25 + 25 − 12 = −22.","lines":2}]
}
