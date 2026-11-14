NUMLINE = ('<svg viewBox="0 0 660 250" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Number lines showing x greater than 3 with an open circle and x less than or equal to 3 with a closed circle">'
  '<text x="330" y="22" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Graphing inequalities on a number line</text>'
  + ''.join(
    f'<g transform="translate(0,{oy})"><path d="M40 60 H620" stroke="#0A1F3D" stroke-width="2"/><path d="M620 54 l10 6 l-10 6Z M40 54 l-10 6 l10 6Z" fill="#0A1F3D"/>'
    + ''.join(f'<path d="M{70+k*60} 54 v12" stroke="#0A1F3D" stroke-width="2"/><text x="{70+k*60}" y="84" text-anchor="middle" fill="#0A1F3D">{k-2}</text>' for k in range(10))
    + f'<path d="M{x1} 60 H{x2}" stroke="{col}" stroke-width="6"/><circle cx="370" cy="60" r="8" fill="{fill}" stroke="{col}" stroke-width="3"/>'
    + f'<path d="M{tip} 52 l{d} 8 l{-d} 8Z" fill="{col}"/><text x="40" y="22" font-weight="bold" fill="{col}">{lab}</text></g>'
    for oy, x1, x2, col, fill, tip, d, lab in [
      (40, 378, 610, "#0047BA", "#fff", 610, 12, "x > 3: open circle (3 is not included), shade right"),
      (140, 50, 362, "#DB2F30", "#DB2F30", 50, -12, "x ≤ 3: closed circle (3 is included), shade left")]) +
  '</svg>')

LESSON = {
 "unit": "Unit 5: Expressions and Equations",
 "title": "Inequalities",
 "subtitle": "An equation has one answer, but life is full of limits: you can spend at most $40, you must be at least 48 inches tall to ride, a bridge holds no more than 10 tons. This week you write, test and graph inequalities, and use them to stay within a budget.",
 "objectives": [
  "Read and write inequalities using <, >, ≤ and ≥.",
  "Determine whether given values make an inequality true or false.",
  "Graph an inequality on a number line using open and closed circles.",
  "Write inequalities to represent real-world limits, including budgets.",
  "Solve one-step inequalities in budget situations and explain what the solutions mean."],
 "vocab": [
  ["inequality", "A mathematical sentence that compares two expressions using <, >, ≤, ≥ or ≠."],
  ["solution of an inequality", "Any value of the variable that makes the inequality true; there are often infinitely many."],
  ["at least", "Greater than or equal to (≥)."],
  ["at most", "Less than or equal to (≤)."],
  ["open circle", "A circle on a number line showing the number is not included (< or >)."],
  ["budget", "A plan for how much money you can spend; the spending limit."]],
 "reconnect": {
  "title": "Week 23: Solving one-step equations",
  "intro": "Equations have one balance point. Start there before you explore limits.",
  "items": [
   {"t":"num","q":"Solve: 6p = 48","a":8,"pts":2,"why":"Divide both sides by 6."},
   {"t":"num","q":"Solve: m − 12.5 = 30","a":42.5,"tol":0.001,"pts":2,"why":"Add 12.5 to both sides."},
   {"t":"num","q":"Five identical books cost $43.75. What does one book cost?","a":8.75,"tol":0.001,"unit":"dollars","pts":2,"why":"5b = 43.75, so b = $8.75."},
   {"t":"open","key":"rc_exactly","q":"Maya needs to earn exactly $135. Last week you solved 9n = 135. But in real life, would Maya be upset if she earned more than $135? What kind of math sentence fits \"at least $135\" better than an equation?","min":15,"rows":2,"rubric":["Notes that more than $135 is fine","Suggests an inequality"],"model":"No, earning more would be fine. \"At least $135\" means $135 or more, so an inequality like 9n ≥ 135 fits better than an equation."}]},
 "hook": {
  "title": "The $40 Field Trip",
  "visual": NUMLINE,
  "html": "<p>Your homeschool co-op is visiting the Kennedy Space Center gift shop, and you have $40 to spend. Can you spend $40? Yes. $25? Yes. $39.99? Yes. $41? No. There isn't one right amount; there's a whole range of amounts that work.</p><p>We write that as <b>s ≤ 40</b>: \"the amount spent is less than or equal to 40.\" That is an <b>inequality</b>, and it has infinitely many solutions.</p><div class='callout'><b>Big question:</b> How do we describe and work with limits when there's more than one right answer?</div>"},
 "learn": [
  {"title": "Reading and Writing Inequalities",
   "html": "<p>The symbols:</p><ul><li><b>&lt;</b> is less than; <b>&gt;</b> is greater than.</li><li><b>≤</b> is less than or equal to (at most, no more than, maximum).</li><li><b>≥</b> is greater than or equal to (at least, no less than, minimum).</li><li><b>≠</b> is not equal to.</li></ul><p>Read the inequality from the variable: <b>h ≥ 48</b> means \"height is at least 48 inches.\" Key phrases matter: \"more than 5\" is x &gt; 5 (5 doesn't count), but \"at least 5\" is x ≥ 5 (5 counts).</p>",
   "checks": [
    {"t":"text","q":"Write an inequality: \"You must be at least 13 years old.\" Use a for age.","a":["a>=13","a ≥ 13","a≥13","13<=a","13 ≤ a","13≤a"],"show":"a ≥ 13","pts":2,"why":"At least means 13 or older."},
    {"t":"text","q":"Write an inequality: \"A carry-on bag can weigh no more than 22 pounds.\" Use w.","a":["w<=22","w ≤ 22","w≤22","22>=w","22 ≥ w","22≥w"],"show":"w ≤ 22","pts":2,"why":"No more than means 22 or less."},
    {"t":"open","key":"morevsleast","q":"Explain the difference between \"more than 10 students\" and \"at least 10 students.\" Write an inequality for each.","min":20,"rows":2,"rubric":["Explains whether 10 is included in each","Correct inequality for each"],"model":"\"More than 10\" doesn't include 10, so it's s > 10 (11, 12, and so on). \"At least 10\" includes 10, so it's s ≥ 10."}]},
  {"title": "Testing Solutions",
   "html": "<p>To test whether a value is a solution, substitute it, just as you checked equations last week. Is 7 a solution of 3x + 2 &lt; 25? 3(7) + 2 = 23, and 23 &lt; 25 is true, so yes. Is 8? 3(8) + 2 = 26, and 26 &lt; 25 is false, so no.</p><p>An inequality can have many solutions, including fractions and decimals: 7.5 makes 3x + 2 &lt; 25 true too (24.5 &lt; 25).</p>",
   "checks": [
    {"t":"num","q":"Test the values 6, 7, 7.5 and 8 in 4n ≥ 30. Which is the smallest of them that makes it true?","a":7.5,"tol":0.001,"pts":2,"why":"4(7.5) = 30, and 30 ≥ 30 is true; 4(7) = 28 is too small."},
    {"t":"text","q":"Is −2 a solution of x + 5 > 2? Type yes or no.","a":[{"all":[["yes"]],"none":["no"]}],"show":"yes","pts":2,"why":"−2 + 5 = 3, and 3 > 2."},
    {"t":"open","key":"manysolutions","q":"An equation like x + 4 = 10 has one solution. Explain why x + 4 < 10 has infinitely many, and name four of them, including one negative and one decimal.","min":25,"rows":3,"rubric":["Explains why there are infinitely many solutions", "Four correct solutions, including a negative and a decimal"],"model":"Any number less than 6 makes x + 4 < 10 true, and there are infinitely many numbers below 6, including fractions and decimals. Four examples: 5, 0, −3 and 2.5."}]},
  {"title": "Graphing on a Number Line",
   "html": "<p>Because an inequality has many solutions, we show them on a number line:</p><ul><li><b>Open circle</b> for &lt; or &gt; (the number itself is not included).</li><li><b>Closed (filled) circle</b> for ≤ or ≥ (the number is included).</li><li>Shade the direction of the solutions, with an arrow showing they continue forever.</li></ul><p>Tip: if the variable is on the left, the inequality symbol points in the direction to shade: x &gt; 3 points right; x ≤ 3 points left.</p>",
   "checks": [
    {"t":"blanks","q":"Describe the graph of y ≥ −1.","sent":"Circle at −1: ___ (open or closed). Shade to the ___ (left or right).","blanks":[[{"all":[["closed","filled","solid"]],"none":["not","open"]}],[{"all":[["right"]],"none":["not","left"]}]],"show":"closed; right","pts":2,"why":"≥ includes −1, and greater numbers are to the right."},
    {"t":"open","key":"readgraph","q":"A number line has an open circle at 50 and shading to the left. Write the inequality, then describe a real situation it could represent.","min":20,"rows":2,"rubric":["Correct inequality with the correct symbol","A real situation where the boundary is not included"],"model":"x < 50. It could mean a speed limit sign that says you must drive under 50 miles per hour in a construction zone."}]},
  {"title": "Money: Staying Within a Budget",
   "html": "<p>Budgets are inequalities. Solve them like equations, using inverse operations, then think about what the solutions mean:</p><ul><li>You have $40 and notebooks cost $3.50 each: 3.50n ≤ 40. Divide both sides by 3.50: n ≤ 11.43. You can't buy part of a notebook, so you can buy <b>at most 11</b>.</li><li>You've spent $18 of a $50 budget: 18 + s ≤ 50, so s ≤ 32. You can spend <b>up to $32</b> more.</li><li>Maya wants to earn at least $135 at $10 a loaf: 10n ≥ 135, n ≥ 13.5, so she must sell <b>at least 14</b> loaves.</li></ul><p>Notice how rounding depends on the situation: round <b>down</b> when you can't go over a limit, <b>up</b> when you must reach a goal.</p>",
   "checks": [
    {"t":"num","q":"Art kits cost $6.25 each and the co-op has $50. What is the greatest number of kits it can buy?","a":8,"unit":"kits","pts":2,"why":"6.25k ≤ 50, so k ≤ 8."},
    {"t":"num","q":"Jordan has $75 for a bike repair. The part costs $28. What is the most he can spend on labor?","a":47,"unit":"dollars","pts":2,"why":"28 + L ≤ 75, so L ≤ 47."},
    {"t":"num","q":"A family wants to save at least $500 for a trip and can save $45 a week. What is the fewest number of weeks needed?","a":12,"unit":"weeks","pts":2,"why":"45w ≥ 500, w ≥ 11.1, so 12 weeks (11 weeks gives only $495)."},
    {"t":"open","key":"roundingrule","q":"In one problem the answer 11.43 became 11, and in another 13.5 became 14. Explain the rule for which way to round in budget and goal problems.","min":25,"rows":3,"rubric":["States when to round down, with a reason", "States when to round up, with a reason", "Mentions whole items"],"model":"When you have a spending limit, round down, because rounding up would put you over budget. When you must reach a goal, round up, because rounding down would leave you short. Either way, you can only buy or sell whole items."}]}],
 "handson": {
  "title": "Human Number Line and the $50 Grocery Challenge",
  "intro": "Become the solutions of an inequality, then plan a real shopping trip that stays within a budget.",
  "materials": ["Painter's tape or chalk", "11 sheets of paper and a marker", "Two paper plates (one plain, one colored in)", "A family member", "A grocery store flyer, a store's website or a recent receipt", "Paper and pencil", "A calculator for checking (optional)"],
  "steps": [
   "Make a number line on the floor with tape or on a driveway with chalk, labeled −5 to 5 on sheets of paper.",
   "Your partner calls out an inequality (for example x ≥ −2). Place the plain plate (open circle) or the colored plate (closed circle) on the boundary, then walk to every whole number that's a solution, saying each one aloud. Then stand between two numbers to show a decimal solution. Do at least five inequalities, swapping roles.",
   "Grocery challenge: plan dinner for your family for two nights with a $50 budget. Using real prices from a flyer, website or receipt, list items and prices, and write an inequality for your total.",
   "Find how much money is left for a treat, and how many of one item (such as $1.29 fruit cups) you could still buy, using an inequality.",
   "Wipe off chalk when done and pick up the tape so no one slips."],
  "record": [
   {"t":"open","key":"humanline","q":"Write three inequalities you acted out, the type of circle you used and the solutions you stood on. Which one was trickiest and why?","min":39,"rows":4,"rubric":["Three inequalities with the correct circles","Correct whole-number solutions","Reflects on the trickiest"],"model":"x ≥ −2: closed circle at −2, stood on −2, −1, 0, 1, 2, 3, 4, 5. x < 1: open circle at 1, stood on 0, −1 down to −5. x > −4: open circle, stood on −3 through 5. The trickiest was x < 1, because I wanted to stand on 1, but the open circle means 1 doesn't count."},
   {"t":"open","key":"groceryrec","q":"Show your grocery plan: items, prices, total, your inequality and how much you had left. How many extra items could you buy with the leftover money? Show the inequality.","min":42,"rows":5,"rubric":["Itemized list with real prices","Total and a budget inequality","Leftover found","Extra-item inequality solved and rounded correctly"],"model":"Chicken $11.48, rice $3.29, broccoli $4.50, tortillas $3.19, beans $2.58, cheese $4.99, salsa $3.49, milk $3.89. Total $37.41, and 37.41 ≤ 50 is true, so I'm within budget. Left: 50 − 37.41 = $12.59. Fruit cups at $1.29: 1.29f ≤ 12.59, f ≤ 9.76, so at most 9 fruit cups."}]},
 "think": {
  "intro": "Explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"phoneplan","q":"Your family's phone plan costs $35 a month plus $5 for each GB of data over the limit, and the family budget for the phone is no more than $60 a month. Write an inequality, solve it, and explain what your answer means. Then give one piece of advice to someone who keeps going over.","min":45,"rows":5,"rubric":["Correct inequality and solution","Explains the meaning in context","Practical advice about staying within budget"],"model":"35 + 5g ≤ 60. Subtract 35: 5g ≤ 25. Divide by 5: g ≤ 5. That means we can use at most 5 GB over the limit each month and still stay within $60. My advice is to use Wi-Fi at home and check data usage weekly so there are no surprises."},
   {"t":"open","key":"ineqvseq","q":"Explain how solving 4x ≤ 20 is like solving 4x = 20, and how the solutions are different. Then describe a real situation where each makes more sense.","min":45,"rows":4,"rubric":["Compares the solving steps", "Compares the solutions", "A situation for each"],"model":"Both are solved by dividing both sides by 4. But 4x = 20 has one solution, x = 5, while 4x ≤ 20 has every number 5 or less. An equation fits buying exactly 5 tickets at $4 when the total was $20; an inequality fits having up to $20 to spend on $4 tickets."}]},
 "exit": [
  {"t":"text","q":"Write an inequality: \"The temperature stayed below 32°F.\" Use t.","a":["t<32","t < 32","32>t","32 > t"],"show":"t < 32","pts":2,"why":"Below 32 doesn't include 32."},
  {"t":"text","q":"Which kind of circle do you draw for x ≥ 4: open or closed?","a":[{"all":[["closed","filled","solid"]],"none":["not","open"]}],"show":"closed","pts":2,"why":"≥ includes 4."},
  {"t":"num","q":"Tickets cost $9 each and you have $60. What is the greatest number of tickets you can buy?","a":6,"unit":"tickets","pts":2,"why":"9t ≤ 60, t ≤ 6.67, so 6."},
  {"t":"open","key":"exit_budget","q":"Why is a budget better described by an inequality than an equation?","min":12,"rows":2,"rubric":["Explains what a budget limit means", "Explains why one exact amount does not fit"],"model":"A budget is a limit, so you can spend any amount up to it, not just one exact number."}],
 "next": "Week 25: Unit 5 review and checkpoint."
}

TEACHER = {
 "standards": [
  "MA.6.AR.2.1: Given an equation or inequality and a specified set of integer values, determine which values make the equation or inequality true or false.",
  "MA.6.AR.2.3: Write and solve one-step equations in one variable within a mathematical or real-world context using multiplication and division, where all terms and solutions are integers.",
  "MA.6.AR.2.4: Determine the unknown decimal or fraction in an equation involving any of the four operations, relating three numbers, with the unknown in any position.",
  "Financial literacy: budgeting and comparing spending to income (Jump$tart Spending and Saving)."],
 "materials": ["The interactive lesson", "Painter's tape or chalk, 11 sheets of paper, a marker, 2 paper plates", "A grocery flyer, website or receipt; optional calculator", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 23 warm-up questions."],
  [4, "Hook", "The $40 gift shop budget."],
  [11, "Reading and writing", "Symbols and key phrases; more than versus at least."],
  [11, "Testing solutions", "Substitute values; many solutions including decimals."],
  [11, "Graphing", "Open and closed circles; read a graph into a situation."],
  [12, "Budgets", "Solve one-step inequalities; rounding up versus down."],
  [5, "Assign", "Set up the human number line; assign the grocery challenge, Think Deeper and the Exit Check."]],
 "key_questions": ["Is the boundary number included?", "Which way do the solutions go?", "Does your answer make sense with whole items?", "Should you round up or down here?"],
 "misconceptions": ["\"At least\" means less than.", "An inequality has only one solution.", "Open and closed circles mean the same thing.", "Always round to the nearest whole number in budget problems."],
 "support": ["Provide a phrase-to-symbol chart.", "Use the human number line for every graph.", "Test two values (one solution, one not) before graphing."],
 "challenge": ["Graph the compound situation \"at least 48 inches and less than 76 inches\" for a ride.", "Explain what happens to 4 > 2 when you multiply both sides by −1, and why (a Grade 7 preview)."],
 "background": "<p>Florida B.E.S.T. Grade 6 asks students to test values in inequalities (MA.6.AR.2.1); writing, solving and graphing one-step inequalities is formally Grade 7 (MA.7.AR.2.1), so this week treats solving as an extension through budget contexts, with only positive coefficients. Prices are practice figures; the grocery challenge uses real local prices.</p>",
 "sources": ["Florida Department of Education, B.E.S.T. Standards for Mathematics (2020).", "Jump$tart Coalition, National Standards for Personal Financial Education (2021)."]
}

PRINT = {
 "directions": "Show your work.",
 "items": [
  {"q":"Write an inequality for each: (a) at least 18 people (b) less than $25 (c) no more than 3 hours","a":"(a) p ≥ 18 (b) c < 25 (c) h ≤ 3","lines":2},
  {"q":"Which values make 5x − 2 > 18 true: 3, 4, 4.5, 6?","a":"4.5 and 6 (5x − 2 = 20.5 and 28); 4 gives 18, which is not greater than 18.","lines":2},
  {"q":"Draw number lines for x < −2 and x ≥ 0.","a":"Open circle at −2 shaded left; closed circle at 0 shaded right.","lines":3},
  {"q":"Pencils cost $0.85 each. You have $10. Write and solve an inequality for the greatest number you can buy.","a":"0.85p ≤ 10; p ≤ 11.76; at most 11 pencils.","lines":2},
  {"q":"You need at least $240 for a tablet and earn $18 a week mowing. Write and solve an inequality for the fewest weeks.","a":"18w ≥ 240; w ≥ 13.33; 14 weeks.","lines":2},
  {"q":"Explain when to round up and when to round down in budget problems.","a":"Round down for a spending limit; round up to reach a goal.","lines":2}]
}
