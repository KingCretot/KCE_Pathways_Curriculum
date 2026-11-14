SCALE = ('<svg viewBox="0 0 640 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="A balance scale showing x plus 5 equals 12; removing 5 from both sides leaves x equals 7">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">An equation is a balance: do the same to both sides</text>'
  + ''.join(
    f'<g transform="translate({ox},0)"><path d="M150 190 L150 70" stroke="#0A1F3D" stroke-width="4"/><path d="M110 200 h80" stroke="#0A1F3D" stroke-width="6"/><path d="M40 70 h220" stroke="#0A1F3D" stroke-width="4"/>'
    f'<path d="M40 70 l-38 50 h76Z" fill="none" stroke="#0A1F3D" stroke-width="2"/><path d="M260 70 l-38 50 h76Z" fill="none" stroke="#0A1F3D" stroke-width="2"/>'
    f'{left}{right}<text x="150" y="222" text-anchor="middle" font-weight="bold" fill="#0A1F3D">{cap}</text></g>'
    for ox, left, right, cap in [
      (0, '<rect x="10" y="98" width="20" height="20" fill="#DB2F30"/><text x="20" y="113" text-anchor="middle" fill="#fff" font-weight="bold">x</text>' + ''.join(f'<circle cx="{40+(k%3)*9}" cy="{113-(k//3)*9}" r="4" fill="#C9A84C"/>' for k in range(5)),
       ''.join(f'<circle cx="{228+(k%6)*8}" cy="{114-(k//6)*9}" r="4" fill="#C9A84C"/>' for k in range(12)), "x + 5 = 12"),
      (320, '<rect x="30" y="98" width="20" height="20" fill="#DB2F30"/><text x="40" y="113" text-anchor="middle" fill="#fff" font-weight="bold">x</text>',
       ''.join(f'<circle cx="{232+(k%4)*8}" cy="{114-(k//4)*9}" r="4" fill="#C9A84C"/>' for k in range(7)), "subtract 5 from both sides: x = 7")]) +
  '<path d="M300 120 h30" stroke="#0047BA" stroke-width="3"/><path d="M324 114 l8 6 l-8 6" fill="none" stroke="#0047BA" stroke-width="3"/></svg>')

LESSON = {
 "unit": "Unit 5: Expressions and Equations",
 "title": "Solving One-Step Equations",
 "subtitle": "An expression is a phrase; an equation is a complete sentence that says two things are equal. This week you solve equations by keeping them balanced, check your solutions, and use equations to find a missing price, the kind of math shoppers and small businesses do every day.",
 "objectives": [
  "Explain the difference between an expression and an equation, and what a solution is.",
  "Solve one-step equations using inverse operations, including equations with rational numbers.",
  "Check a solution by substitution.",
  "Write a one-step equation to represent a real-world situation and solve it.",
  "Find a missing price, quantity or rate using equations."],
 "vocab": [
  ["equation", "A mathematical sentence that says two expressions are equal, using an equal sign."],
  ["solution", "A value of the variable that makes an equation true."],
  ["inverse operations", "Operations that undo each other: addition and subtraction, multiplication and division."],
  ["isolate", "To get the variable alone on one side of an equation."],
  ["properties of equality", "Rules saying that doing the same operation to both sides keeps an equation true."],
  ["unit price", "The price for one item or one unit of measure."]],
 "reconnect": {
  "title": "Week 22: Writing and evaluating expressions",
  "intro": "Last week you put numbers into expressions. This week you work backward: you know the result and find the input.",
  "items": [
   {"t":"num","q":"Evaluate 9n + 4 when n = 6.","a":58,"pts":2,"why":"9(6) + 4 = 54 + 4 = 58."},
   {"t":"text","q":"Write an expression for \"a number decreased by 15.\"","a":["n-15","n − 15","n - 15","x-15","x − 15","x - 15"],"show":"n − 15","pts":2,"why":"Start with the number, then subtract 15."},
   {"t":"text","q":"Simplify: 5(x + 2) − 3x","a":["2x+10","2x + 10","10+2x","10 + 2x"],"show":"2x + 10","pts":2,"why":"5x + 10 − 3x = 2x + 10."},
   {"t":"open","key":"rc_backward","q":"Maya's order formula is 9n + 4. A customer paid $40. Without solving formally, how could you figure out how many loaves they bought?","min":14,"rows":2,"rubric":["A sensible backward strategy (undo the fee, then the price per loaf) or guess and check","A correct number of loaves"],"model":"Take away the $4 delivery fee to get $36, then divide by $9 a loaf: 4 loaves."}]},
 "hook": {
  "title": "The Mystery Price",
  "visual": SCALE,
  "html": "<p>Jordan bought a skateboard and a $14 helmet, and the receipt says the total was $67, but the skateboard's price is smudged. How much was the skateboard? You probably figured it out in your head: 67 − 14 = 53. Without realizing it, you solved the equation <b>s + 14 = 67</b>.</p><p>Equations let us find unknown numbers when we know how they relate to other numbers. Think of an equation as a balance scale: whatever you do to one side, you must do to the other to keep it level.</p><div class='callout'><b>Big question:</b> How can you find an unknown number and prove you are right?</div>"},
 "learn": [
  {"title": "Expressions, Equations and Solutions",
   "html": "<p>An <b>expression</b> like s + 14 has no equal sign; it names a value. An <b>equation</b> like s + 14 = 67 says two expressions are equal. A <b>solution</b> is a value that makes the equation true: s = 53, because 53 + 14 = 67.</p><p>You can test any value by substituting it. If both sides are equal, it's a solution; if not, it isn't.</p>",
   "checks": [
    {"t":"text","q":"Is 3x + 1 an expression or an equation?","a":["^expression",{"all":[["expression"]],"none":["not expression","equation"]}],"show":"an expression","pts":2,"why":"It has no equal sign."},
    {"t":"text","q":"Is n = 8 a solution of 6n = 42? Type yes or no.","a":[{"all":[["no"]],"none":["yes"]}],"show":"no","pts":2,"why":"6(8) = 48, not 42. The solution is n = 7."},
    {"t":"open","key":"exprvseq","q":"Explain the difference between an expression and an equation in your own words, with an example of each from shopping.","min":20,"rows":2,"rubric":["An expression names a value (no equal sign); an equation says two things are equal","A shopping example of each"],"model":"An expression is like a price formula, such as 4p + 3 for 4 shirts plus $3 shipping. An equation says two things are equal, such as 4p + 3 = 39, which tells me the total was $39."}]},
  {"title": "Solving with Inverse Operations",
   "html": "<p>To <b>solve</b> an equation, <b>isolate</b> the variable by using the <b>inverse operation</b> on both sides:</p><ul><li>x + 9 = 23 → subtract 9 from both sides → x = 14.</li><li>y − 6.5 = 10 → add 6.5 to both sides → y = 16.5.</li><li>4m = 52 → divide both sides by 4 → m = 13.</li><li>k/3 = 7 → multiply both sides by 3 → k = 21.</li><li>(2/5)w = 8 → multiply both sides by 5/2 (the reciprocal) → w = 20.</li></ul><p>Always <b>check</b>: substitute your answer into the original equation.</p>",
   "checks": [
    {"t":"num","q":"Solve: x − 17 = 29","a":46,"pts":2,"why":"Add 17 to both sides: x = 46."},
    {"t":"num","q":"Solve: 8p = 96","a":12,"pts":2,"why":"Divide both sides by 8: p = 12."},
    {"t":"num","q":"Solve: t/6 = 4.5","a":27,"pts":2,"why":"Multiply both sides by 6: t = 27."},
    {"t":"num","q":"Solve: (3/4)n = 18","a":24,"pts":2,"why":"Multiply both sides by 4/3: n = 24. Check: 3/4 of 24 is 18."},
    {"t":"open","key":"wrongop","q":"To solve x + 12 = 30, Ana added 12 to both sides and got x = 42. Explain her mistake, give the correct solution, and show a check.","min":25,"rows":3,"rubric":["Explains that she should use the inverse operation","Correct solution with a check"],"model":"Ana should have used the inverse operation. Since 12 is added to x, she should subtract 12 from both sides: x = 18. Check: 18 + 12 = 30, which is true."}]},
  {"title": "Writing Equations from Situations",
   "html": "<p>To write an equation from a word problem:</p><ol><li>Decide what the variable stands for, and write it down: \"Let c = the cost of one notebook.\"</li><li>Find the relationship and write the equation.</li><li>Solve and check, then answer in a sentence with units.</li></ol><p>Example: A Florida spring's water temperature is 72°F, which is 19 degrees warmer than the nearby river. Let r = the river's temperature. r + 19 = 72, so r = 53°F.</p>",
   "checks": [
    {"t":"text","q":"Five friends split a $65 kayak rental equally. Let s = each person's share. Write the equation.","a":["5s=65","5s = 65","65=5s","65 = 5s","5 s = 65"],"show":"5s = 65","pts":2,"why":"Five shares make $65. (Each share is $13.)"},
    {"t":"num","q":"A spider plant grew 4.5 inches this month and is now 18.25 inches tall. How tall was it at the start of the month? Write and solve an equation.","a":13.75,"tol":0.01,"unit":"inches","pts":2,"why":"Subtract 4.5: h = 13.75 inches."},
    {"t":"open","key":"writeeq","q":"Write your own one-step word problem about something in your home or homeschool, write its equation with a defined variable, solve it and check it.","min":36,"rows":4,"rubric":["A realistic word problem","A defined variable and correct one-step equation","Correct solution and check"],"model":"Problem: We need 48 cupcakes for a co-op party, and each pan holds 12. How many pans do we need? Let p = number of pans. 12p = 48. Divide both sides by 12: p = 4. Check: 12 × 4 = 48."}]},
  {"title": "Money: Solving for a Missing Price",
   "html": "<p>Shoppers and business owners often know a total and need a missing piece:</p><ul><li><b>Missing item price:</b> a receipt shows $42.80 for 4 identical books: 4b = 42.80, so b = $10.70 each.</li><li><b>Missing original price:</b> after a $15 discount, a jacket costs $49: p − 15 = 49, so p = $64.</li><li><b>Missing quantity:</b> Maya made $108 selling $9 loaves: 9n = 108, so n = 12 loaves.</li></ul>",
   "checks": [
    {"t":"num","q":"Six identical pens cost $7.50. Write and solve an equation to find the price of one pen.","a":1.25,"tol":0.001,"unit":"dollars","pts":2,"why":"6p = 7.50, so p = $1.25."},
    {"t":"num","q":"A pair of shoes is on sale for $38, which is $22 off the original price. What was the original price?","a":60,"unit":"dollars","pts":2,"why":"p − 22 = 38, so p = $60."},
    {"t":"open","key":"unitcheck","q":"A store sign says a 4-pack of juice boxes is $3.80 and a single box is $1.05. Use equations to find the unit price of the 4-pack, and decide which is the better buy.","min":29,"rows":3,"rubric":["A correct equation and unit price for the 4-pack","A correct comparison and better buy"],"model":"Let u = the price of one box in the 4-pack. 4u = 3.80, so u = $0.95. The single box is $1.05, so the 4-pack is the better buy by 10 cents a box."}]}],
 "handson": {
  "title": "Balance Scale Equations and the Mystery Receipt",
  "intro": "Build a balance from a hanger, solve equations with real objects, then crack mystery receipts.",
  "materials": ["A clothes hanger with notches", "2 identical paper or plastic cups and string (or 2 bags)", "About 30 identical small objects (pennies, paper clips or dried beans)", "An envelope or small opaque bag (the \"x\")", "A family member", "Paper and pencil", "A few real store receipts (optional)"],
  "steps": [
   "Hang the two cups from the hanger's notches with string so they balance. Hang the hanger from a doorknob or have someone hold it.",
   "Your partner secretly puts some pennies in the envelope (this is x) and places it in the left cup with a few loose pennies. They add pennies to the right cup until it balances. Write the equation (for example, x + 4 = 11).",
   "Solve it by removing the same number of loose pennies from both sides until only the envelope is left on one side. Open the envelope to check.",
   "Mystery receipts: your partner covers one price on a real (or made-up) receipt and tells you the total. Write and solve an equation to find the hidden price.",
   "Keep pennies and beans away from young children and pets."],
  "record": [
   {"t":"open","key":"balancerec","q":"Write three balance equations you solved, how you removed objects to solve each, and whether your answer matched what was in the envelope.","min":40,"rows":4,"rubric":["Three equations with correct solutions","Describes removing the same amount from both sides","Checks against the envelope"],"model":"1. x + 4 = 11: removed 4 pennies from each side, x = 7, and the envelope had 7. 2. x + 9 = 15: removed 9 from each side, x = 6, correct. 3. x + 2 = 10: x = 8, correct. Removing the same number from both sides kept the scale balanced every time."},
   {"t":"open","key":"receiptrec","q":"Describe two mystery receipts: the known prices, the total, your equation and the hidden price. Show your check.","min":30,"rows":4,"rubric":["Two receipts with equations","Correct hidden prices","Checks shown"],"model":"Receipt 1: milk $3.49, bread $2.99, hidden cereal, total $10.47. c + 6.48 = 10.47, so c = $3.99. Check: 3.49 + 2.99 + 3.99 = 10.47. Receipt 2: 3 identical notebooks, total $7.47. 3n = 7.47, so n = $2.49. Check: 3 × 2.49 = 7.47."}]},
 "think": {
  "intro": "Explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"pricedecide","q":"Maya wants to earn $135 this week selling loaves. She is deciding between charging $9 or $10 a loaf. Write and solve an equation for each price to find how many loaves she must sell. Then use what you know about running a business to recommend a price.","min":49,"rows":5,"rubric":["Correct equations and solutions for both prices","Recommends a price with a business reason (customers, ingredients, time, competition)"],"model":"At $9: 9n = 135, so n = 15 loaves. At $10: 10n = 135, so n = 13.5, which means 14 loaves to reach at least $135. I'd recommend $10 if her customers are happy to pay it, since she'd bake fewer loaves, saving flour and time. If raising the price loses customers, $9 might sell more."},
   {"t":"open","key":"samesolution","q":"Write three different one-step equations, using three different operations, that all have the solution x = 12. Explain how you created them.","min":39,"rows":4,"rubric":["Three correct equations with solution 12","Three different operations","Explains the method (start with x = 12 and apply an operation to both sides)"],"model":"x + 5 = 17, x − 3 = 9 and 4x = 48. I started with x = 12 and did the same operation to both sides: added 5, subtracted 3, multiplied by 4. Because I kept it balanced, 12 is the solution to all three."}]},
 "exit": [
  {"t":"num","q":"Solve: n + 23 = 51","a":28,"pts":2,"why":"Subtract 23: n = 28."},
  {"t":"num","q":"Solve: 7y = 84","a":12,"pts":2,"why":"Divide by 7: y = 12."},
  {"t":"num","q":"Four tickets cost $46. What is the price of one ticket?","a":11.5,"tol":0.001,"unit":"dollars","pts":2,"why":"4t = 46, so t = $11.50."},
  {"t":"open","key":"exit_check","q":"Why should you always check your solution, and how do you do it?","min":12,"rows":2,"rubric":["Explains how to check a solution","Explains why checking matters"],"model":"Substitute your answer into the original equation; if both sides are equal, it's right. Checking catches mistakes like using the wrong operation."}],
 "next": "Week 24: inequalities, and staying within a budget."
}

TEACHER = {
 "standards": [
  "MA.6.AR.2.1: Given an equation or inequality and a specified set of integer values, determine which values make the equation or inequality true or false.",
  "MA.6.AR.2.2: Write and solve one-step equations in one variable within a mathematical or real-world context using addition and subtraction, where all terms and solutions are integers.",
  "MA.6.AR.2.3: Write and solve one-step equations in one variable within a mathematical or real-world context using multiplication and division, where all terms and solutions are integers.",
  "MA.6.AR.2.4: Determine the unknown decimal or fraction in an equation involving any of the four operations, relating three numbers, with the unknown in any position.",
  "MA.6.AR.1.1: Given a mathematical or real-world context, translate written descriptions into algebraic expressions and translate algebraic expressions into written descriptions.",
  "Financial literacy: unit prices, discounts and checking receipts (Jump$tart Spending and Saving)."],
 "materials": ["The interactive lesson", "A clothes hanger, 2 cups and string, about 30 pennies or beans, an envelope", "Paper, pencil, optional real receipts", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 22 warm-up questions."],
  [4, "Hook", "The smudged skateboard price and the balance."],
  [9, "Expressions, equations, solutions", "Test values by substitution."],
  [13, "Inverse operations", "Solve all four types and a fraction coefficient; fix Ana's mistake."],
  [11, "Writing equations", "Define the variable; the spring temperature; student-written problems."],
  [11, "Missing prices", "Receipts, discounts, quantities and unit prices."],
  [6, "Assign", "Build the hanger balance; assign mystery receipts, Think Deeper and the Exit Check."]],
 "key_questions": ["What operation is being done to the variable?", "What undoes it?", "Did you do the same thing to both sides?", "Does your answer make the original equation true?"],
 "misconceptions": ["Using the same operation instead of the inverse.", "Doing an operation to only one side.", "An expression can be solved.", "Forgetting to answer the question with units."],
 "support": ["Use the hanger balance or a drawn balance for every problem.", "Provide an inverse-operations chart.", "Allow guess-and-check before formal solving."],
 "challenge": ["Solve (5/6)x = 2.5 and explain each step.", "Solve Maya's two-step equation 9n + 4 = 85 and explain each step."],
 "background": "<p>Two-step equations are not required by Grade 6 B.E.S.T. (MA.6.AR.2.2 and 2.3 are one-step; 2.4 covers decimal and fraction unknowns); the reconnect and challenge preview them informally. Inequalities follow in Week 24. Prices are practice figures.</p>",
 "sources": ["Florida Department of Education, B.E.S.T. Standards for Mathematics (2020).", "Jump$tart Coalition, National Standards for Personal Financial Education (2021)."]
}

PRINT = {
 "directions": "Solve and check each equation. Show your work.",
 "items": [
  {"q":"Solve: (a) x + 38 = 71 (b) y − 2.75 = 6.5 (c) 9m = 117 (d) k/8 = 5","a":"(a) 33 (b) 9.25 (c) 13 (d) 40","lines":3},
  {"q":"Solve: (2/3)n = 14","a":"n = 14 × 3/2 = 21.","lines":2},
  {"q":"Is x = 9 a solution of 7x = 56? Explain.","a":"No; 7 × 9 = 63, not 56 (x = 8).","lines":1},
  {"q":"A jacket costs $54 after a $18 discount. Write and solve an equation for the original price.","a":"p − 18 = 54; p = $72.","lines":2},
  {"q":"Eight packs of seeds cost $14. Write and solve an equation for the price of one pack.","a":"8s = 14; s = $1.75.","lines":2},
  {"q":"Write a one-step equation with the solution 15 and a word problem to match.","a":"Model: 4c = 60; four friends each paid the same amount for a $60 gift, so each paid $15.","lines":3}]
}
