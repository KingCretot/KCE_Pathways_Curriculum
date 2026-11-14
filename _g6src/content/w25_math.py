TOOLKIT = ('<svg viewBox="0 0 640 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Unit 5 toolkit: exponents and order of operations, expressions, one-step equations, inequalities">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Unit 5 toolkit</text>'
  + ''.join(f'<g transform="translate({16+i*156},36)"><rect width="144" height="180" rx="12" fill="{c}"/><text x="72" y="24" text-anchor="middle" fill="#fff" font-weight="bold" font-size="12">{a}</text>'
            + ''.join(f'<text x="72" y="{50+j*18}" text-anchor="middle" fill="#fff" font-size="11">{t}</text>' for j, t in enumerate(lines)) + '</g>'
            for i, (a, c, lines) in enumerate([
              ("Week 21: Exponents", "#0A1F3D", ["3⁴ = 3 × 3 × 3 × 3", "order: ( ), exponents,", "× and ÷ left to right,", "+ and − left to right", "simple interest", "I = P × r × t"]),
              ("Week 22: Expressions", "#0047BA", ["terms, coefficients,", "constants", "words ↔ symbols", "substitute to evaluate", "3(x + 2) = 3x + 6", "cost formula 9n + 4"]),
              ("Week 23: Equations", "#2c6e22", ["a solution makes it true", "use the inverse", "on both sides", "always check", "find a missing price", "unit price"]),
              ("Week 24: Inequalities", "#DB2F30", ["< > ≤ ≥", "at least = ≥", "at most = ≤", "open or closed circle", "budget: round down", "goal: round up"])])) +
  '</svg>')

LESSON = {
 "unit": "Unit 5: Expressions and Equations",
 "title": "Unit 5 Review and Checkpoint",
 "subtitle": "This week you pull together exponents, expressions, equations and inequalities, use them to plan a real homeschool event on a budget, and then show your mastery on the Unit 5 checkpoint.",
 "objectives": [
  "Choose the right algebra tool for a problem: evaluate, simplify, solve or compare.",
  "Use exponents and the order of operations, including simple interest.",
  "Write and evaluate expressions and cost formulas.",
  "Solve one-step equations and test values in inequalities, including budget problems.",
  "Demonstrate mastery of Unit 5 on the checkpoint (85 or higher)."],
 "vocab": [
  ["exponent", "Tells how many times the base is used as a factor."],
  ["expression", "Numbers, variables and operations with no equal sign."],
  ["equation", "Two expressions set equal; a solution makes it true."],
  ["inequality", "Two expressions compared with <, >, ≤ or ≥."],
  ["inverse operations", "Operations that undo each other."],
  ["simple interest", "Interest earned only on the principal: I = P × r × t."]],
 "reconnect": {
  "title": "Unit 5, one question from each week",
  "intro": "Warm up with one question from each week of the unit.",
  "items": [
   {"t":"num","q":"Week 21: 18 − 2³ × 2 = ?","a":2,"pts":2,"why":"2³ = 8; 8 × 2 = 16; 18 − 16 = 2."},
   {"t":"num","q":"Week 22: Evaluate 4a + 3b when a = 5 and b = 2.","a":26,"pts":2,"why":"20 + 6 = 26."},
   {"t":"num","q":"Week 23: Solve: x/4 = 9","a":36,"pts":2,"why":"Multiply both sides by 4."},
   {"t":"text","q":"Week 24: Write an inequality for \"no more than 30 people.\" Use p. Write the symbol in words (for example, \"x is less than 5\").","a":["^p is less than or equal to 30","^30 is greater than or equal to p"],"show":"p ≤ 30 (p is less than or equal to 30)","pts":2,"why":"No more than means 30 or fewer."}]},
 "hook": {
  "title": "Planning the Co-op Spring Fair",
  "visual": TOOLKIT,
  "html": "<p>Your homeschool co-op is planning a spring fair, and you're on the planning team. You have a budget, booth fees to set, supplies to price and a savings account to grow. Every tool from Unit 5 has a job: exponents and interest for the savings, expressions for the costs, equations for missing prices and inequalities for staying within the budget.</p><div class='callout'><b>Big question:</b> How do I choose the right algebra tool for a real problem?</div>"},
 "learn": [
  {"title": "Review: Exponents, Order of Operations and Interest",
   "html": "<p>Exponents are repeated multiplication: 5² = 25 and 2⁵ = 32. Order of operations: parentheses, exponents, multiplication and division from left to right, then addition and subtraction from left to right. Simple interest: I = P × r × t, with the rate written as a decimal.</p>",
   "checks": [
    {"t":"num","q":"Evaluate: (7 − 3)² + 12 ÷ 4","a":19,"pts":2,"why":"4² = 16; 12 ÷ 4 = 3; 16 + 3 = 19."},
    {"t":"num","q":"The co-op puts $600 in a savings account earning 3% simple interest. How much interest does it earn in 2 years?","a":36,"unit":"dollars","pts":2,"why":"600 × 0.03 × 2 = 36."}]},
  {"title": "Review: Expressions and Cost Formulas",
   "html": "<p>An expression names a value. A cost formula usually has a <b>rate</b> (the coefficient) and a <b>fixed fee</b> (the constant): renting tables at $8 each plus a $25 delivery fee costs 8t + 25. Use the distributive property to rewrite, and combine like terms to simplify.</p>",
   "checks": [
    {"t":"text","q":"Write a cost formula: face painting kits cost $6 each, plus $10 shipping. Use k.","a":["6k+10","6k + 10","10+6k","10 + 6k"],"show":"6k + 10","pts":2,"why":"$6 per kit plus a $10 fixed fee."},
    {"t":"text","q":"Simplify: 4(2x + 3) − 5x","a":["3x+12","3x + 12","12+3x","12 + 3x"],"show":"3x + 12","pts":2,"why":"8x + 12 − 5x = 3x + 12."}]},
  {"title": "Review: Equations and Inequalities",
   "html": "<p>To solve, undo the operation with its inverse on both sides, then check by substituting. An inequality has many solutions: test values, graph with an open or closed circle and, in budget problems, round down for limits and up for goals.</p>",
   "checks": [
    {"t":"num","q":"Twelve identical prizes cost $54. What is the price of one prize?","a":4.5,"tol":0.001,"unit":"dollars","pts":2,"why":"12p = 54, so p = $4.50."},
    {"t":"open","key":"solvevsineq","q":"Explain when you would write an equation and when you would write an inequality for a fair-planning problem. Give one example of each.","min":25,"rows":3,"rubric":["Explains when an exact amount calls for an equation","Explains when a limit or goal calls for an inequality","One fair example of each"],"model":"Use an equation when the amount is exact, such as finding the price of one prize when 12 cost $54: 12p = 54. Use an inequality for a limit or goal, such as buying balloons at $0.40 each with at most $20: 0.40b ≤ 20."}]},
  {"title": "Money: Planning the Fair Budget",
   "html": "<p>The fair has a <b>$300 budget</b>. Fixed costs: a $75 park pavilion and $40 for signs. Supplies: craft kits at $3.50 each. Booths will charge a fee to cover costs.</p><ul><li>Spending inequality: 75 + 40 + 3.50k ≤ 300, so 3.50k ≤ 185, k ≤ 52.86: at most <b>52 kits</b>.</li><li>Booth fees: 15 booths at $f each must raise at least $300: 15f ≥ 300, f ≥ 20.</li></ul>",
   "checks": [
    {"t":"num","q":"Using the $300 budget, how much money is left after the pavilion and signs?","a":185,"unit":"dollars","pts":2,"why":"300 − 75 − 40 = 185."},
    {"t":"num","q":"If 18 booths sign up instead of 15, what is the lowest whole-dollar booth fee that raises at least $300?","a":17,"unit":"dollars","pts":2,"why":"18f ≥ 300, f ≥ 16.67, so $17."},
    {"t":"open","key":"fairadvice","q":"The team wants to add a $45 bounce house. Use an inequality to decide how many craft kits they could still buy within the $300 budget, and give your advice on whether to add it.","min":35,"rows":3,"rubric":["A correct inequality including the bounce house","Correct greatest number of kits","A recommendation with a reason"],"model":"75 + 40 + 45 + 3.50k ≤ 300, so 3.50k ≤ 140 and k ≤ 40. They could still buy 40 craft kits. I'd add the bounce house if 40 kits is enough for the expected crowd, since it draws families to the fair."}]}],
 "handson": {
  "title": "Algebra Stations Relay",
  "intro": "Rotate through four stations, one for each week of the unit, racing a family member to solve and check.",
  "materials": ["4 sheets of paper labeled Station 1 to 4", "Index cards and a marker", "A timer", "A family member", "Paper and pencil", "Painter's tape (optional, for a floor number line)"],
  "steps": [
   "Set up four stations around the room. On index cards, your family member writes three problems for each station: Station 1 exponents and order of operations, Station 2 evaluating or simplifying expressions, Station 3 one-step equations, Station 4 inequalities (write, test or graph).",
   "Start a 3-minute timer at Station 1. Solve as many cards as you can, showing your work. Then move to the next station.",
   "At Station 3, check every solution by substituting. At Station 4, act out one graph on a tape number line, standing on the solutions.",
   "Swap roles: you write the cards for your family member, including one card with a deliberate mistake for them to find.",
   "Keep markers capped and pick up the tape so no one slips."],
  "record": [
   {"t":"open","key":"relayrec","q":"Which station was easiest and which was hardest for you? Show one problem from your hardest station, solved and checked, and explain what you'll review before the checkpoint.","min":40,"rows":4,"rubric":["Names the easiest and hardest stations","One worked and checked problem from the hardest station","A specific review plan"],"model":"Station 2 was easiest. Station 4 was hardest, especially deciding when to round up. Problem: save at least $95 at $12 a week: 12w ≥ 95, w ≥ 7.92, so 8 weeks; check: 12 × 8 = 96, which is at least 95. Before the checkpoint I'll review the rounding rule for goals and limits."}]},
 "think": {
  "intro": "Your teacher scores this.",
  "items": [
   {"t":"open","key":"unitreflect","q":"Unit 5 moved from evaluating expressions to solving equations to working with inequalities. Explain how these three ideas are connected, using one example that uses all three.","min":60,"rows":5,"rubric":["Explains how expressions are the building blocks of equations and inequalities","Explains how solving and testing are related","One example that uses all three ideas"],"model":"An expression like 5n + 20 can describe the cost of n tickets plus parking. Setting it equal to a total, 5n + 20 = 60, makes an equation with one solution, n = 8. Comparing it to a limit, 5n + 20 ≤ 60, makes an inequality with many solutions, 8 tickets or fewer. All three use the same expression; the equal sign or inequality symbol decides what kind of answer you get."}]},
 "checkpoint": {
  "title": "Unit 5 Checkpoint: Expressions and Equations",
  "intro": "This checkpoint covers Weeks 21 to 24. Work each problem on paper, then type your answer. Mastery is 85 or higher. If you score below 85, your teacher will review with you, then you will retake it.",
  "parts": [
   {"title": "Part A: Exponents, order of operations and interest", "items": [
    {"t":"num","q":"Evaluate: 6² − 4 × 5","a":16,"pts":3,"why":"36 − 20 = 16."},
    {"t":"num","q":"Evaluate: 3 × (2 + 4)² ÷ 9","a":12,"pts":3,"why":"6² = 36; 3 × 36 = 108; 108 ÷ 9 = 12."},
    {"t":"blanks","q":"Write 7 × 7 × 7 × 7 × 7 in exponent form.","sent":"Base: ___ &nbsp; Exponent: ___","blanks":[["^7"],["^5"]],"show":"7; 5","pts":3,"why":"Seven used as a factor five times."},
    {"t":"num","q":"$1,200 is borrowed at 6% simple interest for 3 years. How much interest is owed?","a":216,"unit":"dollars","pts":4,"why":"1,200 × 0.06 × 3 = 216."}]},
   {"title": "Part B: Expressions", "items": [
    {"t":"text","q":"Write an expression for \"8 less than three times a number n.\"","a":["3n-8","3n − 8","3n - 8","3 n - 8"],"show":"3n − 8","pts":3,"why":"Three times n, then subtract 8."},
    {"t":"num","q":"Evaluate 2x² + 3y when x = 4 and y = 5.","a":47,"pts":3,"why":"2(16) + 15 = 47."},
    {"t":"text","q":"Simplify: 5(y + 2) + 3y − 4","a":["8y+6","8y + 6","6+8y","6 + 8y"],"show":"8y + 6","pts":3,"why":"5y + 10 + 3y − 4 = 8y + 6."},
    {"t":"open","key":"cpformula","q":"A bike shop charges $15 per hour plus a $12 helmet fee to rent a bike. Write a cost formula, find the cost for 4 hours, and explain what each part of the formula means.","min":20,"rows":3,"pts":4,"rubric":["Correct formula 15h + 12","Correct cost $72","Explains the rate and the fixed fee"],"model":"C = 15h + 12. For 4 hours: 15(4) + 12 = 60 + 12 = $72. The 15 is the hourly rate, which changes with time, and the 12 is the fixed helmet fee, paid once."}]},
   {"title": "Part C: One-step equations", "items": [
    {"t":"num","q":"Solve: x + 27 = 63","a":36,"pts":3,"why":"Subtract 27."},
    {"t":"num","q":"Solve: 9m = 108","a":12,"pts":3,"why":"Divide by 9."},
    {"t":"num","q":"Solve: (2/3)k = 16","a":24,"pts":3,"why":"Multiply by 3/2."},
    {"t":"open","key":"cpmissing","q":"A receipt shows 5 identical notebooks and a $3.25 pen, for a total of $16.75. Write an equation for the price of one notebook, solve it, and check it.","min":18,"rows":3,"pts":4,"rubric":["Correct equation","Correct price $2.70","A correct check"],"model":"5n + 3.25 = 16.75. Subtract 3.25: 5n = 13.50. Divide by 5: n = $2.70. Check: 5 × 2.70 + 3.25 = 13.50 + 3.25 = 16.75."}]},
   {"title": "Part D: Inequalities", "items": [
    {"t":"text","q":"Write an inequality for \"Riders must be at least 42 inches tall.\" Use h. Write the symbol in words (for example, \"x is less than 5\").","a":["^h is greater than or equal to 42","^42 is less than or equal to h"],"show":"h ≥ 42 (h is greater than or equal to 42)","pts":3,"why":"At least means 42 or more."},
    {"t":"num","q":"Test x = 3, 4, 5 and 6 in 7x − 5 > 23. Which is the smallest of these that makes it true?","a":5,"pts":3,"why":"7(4) − 5 = 23, not greater than 23; 7(5) − 5 = 30."},
    {"t":"blanks","q":"Describe the graph of n < −2.","sent":"Circle: ___ (open or closed). Shade: ___ (left or right).","blanks":[[{"all":[["open"]],"none":["not","closed"]}],[{"all":[["left"]],"none":["not","right"]}]],"show":"open; left","pts":3,"why":"< does not include −2; smaller numbers are to the left."},
    {"t":"open","key":"cpbudget","q":"You have $45 for a gift basket. The basket costs $9 and each jar of jam costs $4.75. Write an inequality, solve it, and explain the greatest number of jars you can buy.","min":18,"rows":3,"pts":4,"rubric":["Correct inequality","Correct solving steps","Correct answer with rounding explained"],"model":"9 + 4.75j ≤ 45, so 4.75j ≤ 36 and j ≤ 7.58. I can buy at most 7 jars, rounding down because 8 jars would go over the $45 limit."}]}]},
 "next": "Unit 6: geometry and data, starting with the area of triangles, quadrilaterals and composite figures."
}

TEACHER = {
 "standards": [
  "MA.6.NSO.3.3: Evaluate positive rational numbers and integers with natural number exponents.",
  "MA.6.AR.1.3: Evaluate algebraic expressions using substitution and order of operations.",
  "MA.6.AR.1.4: Apply the properties of operations to generate equivalent algebraic expressions with integer coefficients.",
  "MA.6.AR.1.1: Given a mathematical or real-world context, translate written descriptions into algebraic expressions and translate algebraic expressions into written descriptions.",
  "MA.6.AR.2.1: Given an equation or inequality and a specified set of integer values, determine which values make the equation or inequality true or false.",
  "MA.6.AR.2.3: Write and solve one-step equations in one variable within a mathematical or real-world context using multiplication and division, where all terms and solutions are integers.",
  "MA.6.AR.2.4: Determine the unknown decimal or fraction in an equation involving any of the four operations, relating three numbers, with the unknown in any position.",
  "Financial literacy: budgeting and simple interest (Jump$tart Spending and Saving; Credit and Borrowing)."],
 "materials": ["The interactive lesson", "4 station sheets, index cards, a marker, a timer, optional painter's tape", "Printable practice page", "The Unit 5 checkpoint"],
 "flow": [
  [6, "Reconnect", "Run one question from each week of the unit."],
  [4, "Hook", "The co-op spring fair and the toolkit chart."],
  [8, "Exponents and interest", "Order of operations; simple interest on the fair savings."],
  [8, "Expressions", "Cost formulas; simplify."],
  [9, "Equations and inequalities", "Missing prices; when to use which."],
  [10, "Fair budget", "Spending limits and booth fees; the bounce house decision."],
  [5, "Assign", "Set up the stations relay and assign Think Deeper."],
  [10, "Checkpoint preview", "Explain that the checkpoint is completed after class, independently, one try per item, with no answers shown until you review it. Mastery is 85; below 85 means a review lesson and a retake."]],
 "key_questions": ["Am I evaluating, simplifying, solving or comparing?", "What operation undoes this one?", "Is the boundary included?", "Does my answer make sense with whole items?"],
 "misconceptions": ["2³ means 2 × 3.", "Solving means doing the same operation that appears.", "Inequalities have one answer.", "Budget answers are always rounded to the nearest whole number."],
 "support": ["Provide the toolkit chart during review (not during the checkpoint).", "Use the balance model for equations.", "Let the student explain a problem aloud before writing."],
 "challenge": ["Plan a full fair budget with five cost lines and a booth fee that raises at least $50 profit.", "Solve the two-step problem 5n + 3.25 = 16.75 two different ways."],
 "background": "<p>The checkpoint includes two two-step items (Part C notebooks and Part D gift basket); Week 23's challenge previewed this, and both are scored with rubrics that allow partial credit. Checkpoint totals: Part A 13, Part B 13, Part C 13, Part D 13, total 52. Prices are practice figures.</p>",
 "sources": ["Florida Department of Education, B.E.S.T. Standards for Mathematics (2020).", "Jump$tart Coalition, National Standards for Personal Financial Education (2021)."]
}

PRINT = {
 "directions": "Show your work. This page reviews the whole unit.",
 "items": [
  {"q":"Evaluate: (a) 4³ (b) 50 − 3² × 4 (c) (10 − 6)² ÷ 2","a":"(a) 64 (b) 14 (c) 8","lines":2},
  {"q":"How much simple interest does $900 earn at 4% for 5 years?","a":"900 × 0.04 × 5 = $180.","lines":1},
  {"q":"Write a cost formula: $7 per pizza plus a $4 delivery fee. Find the cost of 6 pizzas.","a":"7p + 4; 7(6) + 4 = $46.","lines":2},
  {"q":"Solve and check: (a) y − 4.6 = 9.4 (b) 15w = 165","a":"(a) 14 (b) 11","lines":2},
  {"q":"Write and graph: you must be at least 16 to drive.","a":"a ≥ 16; closed circle at 16, shaded right.","lines":2},
  {"q":"You have $60. Movie tickets cost $11.50 each. What is the greatest number you can buy?","a":"11.50t ≤ 60; t ≤ 5.2; 5 tickets.","lines":2}]
}
