PARTS = ('<svg viewBox="0 0 640 210" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Parts of an algebraic expression: 4x plus 7, with term, coefficient, variable and constant labeled">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The parts of an expression</text>'
  '<text x="320" y="110" text-anchor="middle" font-size="56" font-family="Georgia, serif" fill="#0A1F3D"><tspan fill="#0047BA">4</tspan><tspan fill="#DB2F30" font-style="italic">x</tspan> + <tspan fill="#2c6e22">7</tspan></text>'
  '<path d="M262 120 v24" stroke="#0047BA" stroke-width="2"/><text x="262" y="160" text-anchor="middle" fill="#0047BA" font-weight="bold">coefficient</text><text x="262" y="176" text-anchor="middle" fill="#0047BA" font-size="11">number times the variable</text>'
  '<path d="M300 60 v-14" stroke="#DB2F30" stroke-width="2"/><text x="300" y="40" text-anchor="middle" fill="#DB2F30" font-weight="bold">variable</text><text x="370" y="40" text-anchor="start" fill="#DB2F30" font-size="11">a letter for an unknown or changing number</text>'
  '<path d="M386 120 v24" stroke="#2c6e22" stroke-width="2"/><text x="430" y="160" text-anchor="middle" fill="#2c6e22" font-weight="bold">constant</text><text x="430" y="176" text-anchor="middle" fill="#2c6e22" font-size="11">a fixed number</text>'
  '<path d="M240 190 h90 M370 190 h40" stroke="#8a6d1f" stroke-width="3"/><text x="320" y="204" text-anchor="middle" fill="#8a6d1f" font-size="11">two terms: 4x and 7 (terms are separated by + or −)</text></svg>')

LESSON = {
 "unit": "Unit 5: Expressions and Equations",
 "title": "Writing and Evaluating Expressions",
 "subtitle": "Last week you evaluated expressions full of numbers. Now you use variables, letters that stand for numbers that change. With them you can write one formula that works for every customer, every week and every order, and businesses use exactly this to set prices.",
 "objectives": [
  "Identify the parts of an algebraic expression: terms, variables, coefficients and constants.",
  "Translate words into algebraic expressions and expressions into words.",
  "Evaluate expressions by substituting values and using the order of operations.",
  "Use properties (distributive, commutative, associative) to write equivalent expressions.",
  "Write and use cost formulas for real businesses."],
 "vocab": [
  ["variable", "A letter or symbol that stands for an unknown or changing number."],
  ["expression", "A mathematical phrase with numbers, variables and operations but no equal sign."],
  ["term", "A part of an expression separated by + or − signs."],
  ["coefficient", "The number multiplied by a variable, such as 4 in 4x."],
  ["constant", "A term with no variable; its value doesn't change."],
  ["substitute", "To replace a variable with a number."],
  ["equivalent expressions", "Expressions that have the same value for every value of the variable."]],
 "reconnect": {
  "title": "Week 21: Exponents and order of operations",
  "intro": "Evaluating an expression with a variable uses exactly last week's order of operations.",
  "items": [
   {"t":"num","q":"Evaluate 3⁴.","a":81,"pts":2,"why":"3 × 3 × 3 × 3 = 81."},
   {"t":"num","q":"Evaluate: 2 + 5 × (6 − 4)²","a":22,"pts":2,"why":"2² = 4; 5 × 4 = 20; 2 + 20 = 22."},
   {"t":"num","q":"How much simple interest does $400 earn in 3 years at 5%?","a":60,"unit":"dollars","pts":2,"why":"400 × 0.05 × 3 = 60. I = Prt is itself an expression with variables."},
   {"t":"open","key":"rc_formula","q":"Last week you used I = P × r × t. What do P, r and t stand for, and why is it useful to write a formula with letters instead of numbers?","min":15,"rows":2,"rubric":["Names what each letter stands for","Letters let one formula work for any amount, rate and time"],"model":"P is the principal, r is the rate and t is the time in years. Using letters means one formula works for any amount of money, any rate and any number of years."}]},
 "hook": {
  "title": "One Formula, Every Order",
  "visual": PARTS,
  "html": "<p>Maya's bakery now takes online orders. Every order costs $9 per loaf plus a $4 delivery fee. A customer who orders 1 loaf pays $13; 2 loaves, $22; 5 loaves, $49. Instead of figuring each order from scratch, Maya writes one rule: <b>9n + 4</b>, where n is the number of loaves.</p><p>That little expression is a tiny machine: put in any number of loaves and out comes the price. Every online store, phone plan and ride-share app runs on expressions like this.</p><div class='callout'><b>Big question:</b> How can one expression describe a whole pattern?</div>"},
 "learn": [
  {"title": "The Language of Algebra",
   "html": "<p>An <b>expression</b> combines numbers, variables and operations. In 4x + 7, there are two <b>terms</b>: 4x and 7. The <b>coefficient</b> 4 multiplies the <b>variable</b> x; 7 is a <b>constant</b>.</p><p>A term keeps the sign in front of it: in 8y − 3, the constant is −3 (Week 19 integers).</p><p>Conventions: 4x means 4 × x (no multiplication sign needed); x/3 or x ÷ 3 means x divided by 3; x² means x × x.</p><p><b>Words to symbols:</b></p><ul><li>\"5 more than a number\": n + 5</li><li>\"7 less than a number\": n − 7 (careful: not 7 − n)</li><li>\"the product of 6 and a number\": 6n</li><li>\"a number divided by 4\": n/4</li><li>\"3 times the sum of a number and 2\": 3(n + 2)</li></ul>",
   "checks": [
    {"t":"blanks","q":"For the expression 8y − 3 + 2z:","sent":"How many terms? ___ &nbsp; The coefficient of y: ___ &nbsp; The constant: ___","blanks":[["3","three"],["8","^8"],["-3","−3","^-3"]],"show":"3; 8; −3","pts":3,"why":"Terms 8y, −3 and 2z. The constant is −3 because subtraction makes it negative."},
    {"t":"text","q":"Write an expression for \"10 less than a number n.\"","a":["n-10","n − 10","n - 10","-10+n","−10 + n"],"show":"n − 10","pts":2,"why":"Start with n, then subtract 10. 10 − n would be \"n less than 10.\""},
    {"t":"text","q":"Write an expression for \"twice the sum of a number x and 5.\"","a":["2(x+5)","2(x + 5)","2*(x+5)","2(5+x)","2(5 + x)","2x+10","2x + 10","10+2x","10 + 2x"],"show":"2(x + 5) or 2x + 10","pts":2,"why":"The sum goes in parentheses so all of it is doubled. Type the parentheses with no spaces."},
    {"t":"open","key":"wordsfor","q":"Write the expression 3(k − 4) in words, then explain how it is different from 3k − 4.","min":20,"rows":2,"rubric":["Correct words for 3(k − 4)","3(k − 4) multiplies all of (k − 4) by 3; 3k − 4 multiplies only k, then subtracts 4"],"model":"Three times the difference of k and 4. In 3(k − 4), you subtract 4 from k first and then multiply the whole result by 3. In 3k − 4, you multiply only k by 3, then subtract 4."}]},
  {"title": "Evaluating Expressions",
   "html": "<p>To <b>evaluate</b> an expression, <b>substitute</b> a number for each variable, then follow the order of operations. Use parentheses when you substitute, especially for negative numbers.</p><p>Example: evaluate 2a² − 3b when a = 4 and b = −5.</p><p>2(4)² − 3(−5) = 2(16) − (−15) = 32 + 15 = 47.</p>",
   "checks": [
    {"t":"num","q":"Evaluate 6x + 11 when x = 7.","a":53,"pts":2,"why":"6(7) + 11 = 42 + 11 = 53."},
    {"t":"num","q":"Evaluate 3m² − m when m = 4.","a":44,"pts":2,"why":"3(16) − 4 = 48 − 4 = 44."},
    {"t":"num","q":"Evaluate (p + q)/2 when p = 13 and q = −5.","a":4,"pts":2,"why":"(13 + (−5))/2 = 8/2 = 4."},
    {"t":"open","key":"negsub","q":"Kai evaluated −x² when x = 3 and got 9. Explain his mistake and give the correct value.","min":18,"rows":2,"rubric":["Explains which part the exponent applies to, then gives the correct value","Identifies what Kai squared by mistake"],"model":"The expression −x² means the opposite of x². So −(3)² = −9. Kai squared −3, which would be (−x)², a different expression."}]},
  {"title": "Equivalent Expressions and Properties",
   "html": "<p>Properties let you rewrite expressions without changing their value:</p><ul><li><b>Commutative:</b> order doesn't matter for adding or multiplying: a + b = b + a; ab = ba.</li><li><b>Associative:</b> grouping doesn't matter for adding or multiplying: (a + b) + c = a + (b + c).</li><li><b>Distributive:</b> a(b + c) = ab + ac. For example, 5(x + 3) = 5x + 15.</li></ul><p>You can also <b>combine like terms</b>, terms with the same variable part: 4x + 2 + 3x − 6 = 7x − 4.</p><p>To check whether two expressions are equivalent, substitute the same number into both. If they ever give different values, they are not equivalent.</p>",
   "checks": [
    {"t":"text","q":"Use the distributive property to rewrite 6(2y − 5) without parentheses.","a":["12y-30","12y − 30","12y - 30","12 y - 30","-30+12y","−30 + 12y"],"show":"12y − 30","pts":2,"why":"6 × 2y = 12y and 6 × 5 = 30."},
    {"t":"text","q":"Combine like terms: 9a + 4 − 2a + 7","a":["7a+11","7a + 11","11+7a","11 + 7a"],"show":"7a + 11","pts":2,"why":"9a − 2a = 7a; 4 + 7 = 11."},
    {"t":"open","key":"equivcheck","q":"Are 2(x + 4) and 2x + 4 equivalent? Test them with x = 3 and explain.","min":20,"rows":2,"rubric":["Correct value of each expression for x = 3","Correct conclusion with the correct equivalent expression"],"model":"With x = 3, 2(3 + 4) = 14 but 2(3) + 4 = 10. They give different values, so they aren't equivalent. The correct equivalent expression is 2x + 8."}]},
  {"title": "Money: Writing Cost Formulas",
   "html": "<p>Many prices follow the pattern <b>(rate × amount) + fixed fee</b>:</p><ul><li>Maya's online orders: <b>9n + 4</b> dollars for n loaves.</li><li>A phone plan: $25 a month plus $10 per gigabyte of data: <b>25 + 10g</b>.</li><li>A pet-sitting business: $15 per visit plus a one-time $20 meet-and-greet: <b>15v + 20</b>.</li></ul><p>The coefficient is the rate (cost per item), and the constant is the fixed part. Formulas help businesses quote prices quickly and customers compare deals.</p>",
   "checks": [
    {"t":"num","q":"Use Maya's formula 9n + 4. How much does an order of 7 loaves cost?","a":67,"unit":"dollars","pts":2,"why":"9(7) + 4 = 63 + 4 = 67."},
    {"t":"text","q":"A bike rental costs $8 per hour plus a $5 helmet fee. Write an expression for the cost of h hours.","a":["8h+5","8h + 5","5+8h","5 + 8h"],"show":"8h + 5","pts":2,"why":"Rate × hours + fixed fee."},
    {"t":"open","key":"comparedeal","q":"Plan A costs 30 + 5g dollars a month and Plan B costs 15 + 10g dollars, where g is gigabytes used. Which plan is cheaper for 2 GB? For 5 GB? Explain what the coefficients and constants tell you.","min":40,"rows":4,"rubric":["Correct costs and cheaper plan for 2 GB","Correct costs and cheaper plan for 5 GB","Explains coefficients as cost per GB and constants as the fixed fee"],"model":"For 2 GB: Plan A costs 30 + 5(2) = $40 and Plan B costs 15 + 10(2) = $35, so B is cheaper. For 5 GB: A costs $55 and B costs $65, so A is cheaper. The constants are the fixed monthly fees and the coefficients are the cost per gigabyte. B has a lower fee but a higher rate, so it's better only for light users."}]}],
 "handson": {
  "title": "Expression Machine and Price-List Builder",
  "intro": "Build a paper \"function machine,\" then design a real price list using a cost formula.",
  "materials": ["A cereal box or shoebox", "Scissors (used by an adult if the box is thick)", "Index cards and a marker", "Tape", "A family member", "Paper and pencil", "Optional: a calculator for checking"],
  "steps": [
   "Expression machine: cut a slot near the top of the box (IN) and another near the bottom (OUT). Your partner writes a secret rule like 3x + 2 and hides it.",
   "Drop an index card with an input number into the IN slot. Your partner calculates and passes out a card with the output. After four inputs, guess the rule. Switch roles.",
   "Price-list builder: pick a business you could run (dog walking, car washing, bracelets, tutoring a younger sibling's friend). Choose a rate and a fixed fee. Write your cost formula with a variable.",
   "Make a price list for 1 to 6 units using your formula. Then make a poster or flyer showing your formula and price list.",
   "Ask a family member to \"order\" from you and check that your formula gives the right price."],
  "record": [
   {"t":"open","key":"machinerec","q":"Write two of the secret rules you played with, the inputs and outputs for each, and how you figured out the rule.","min":30,"rows":4,"rubric":["Two rules with input-output pairs that fit","A clear strategy for finding the rule"],"model":"Rule 3x + 2: inputs 1, 2, 5, 10 gave 5, 8, 17, 32. Each time the input went up by 1, the output went up by 3, so the coefficient was 3; then 3(1) = 3 and 5 − 3 = 2, so the constant was 2. Rule 4x − 1: inputs 0, 1, 3 gave −1, 3, 11."},
   {"t":"open","key":"pricerec","q":"Share your business, your cost formula (explain each part), and your price list for 1 to 6 units.","min":33,"rows":4,"rubric":["A formula with a coefficient and constant explained","Six correct prices"],"model":"Dog walking: 6w + 3, where w is the number of walks: $6 per walk plus a $3 booking fee. Prices: 1 walk $9, 2 walks $15, 3 walks $21, 4 walks $27, 5 walks $33, 6 walks $39."}]},
 "think": {
  "intro": "Explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"perimeter","q":"A rectangular garden is x feet long and 4 feet wider than it is long. Write an expression for its width and two different equivalent expressions for its perimeter. Then find the perimeter when x = 10, using both expressions.","min":46,"rows":5,"rubric":["Correct expression for the width","Two correct equivalent perimeter expressions","Both evaluated correctly for x = 10"],"model":"The width is x + 4. Perimeter: 2x + 2(x + 4), which simplifies to 2x + 2x + 8 = 4x + 8. When x = 10: 2(10) + 2(14) = 20 + 28 = 48 feet, and 4(10) + 8 = 48 feet. Both give the same answer because the expressions are equivalent."},
   {"t":"open","key":"bakerycost","q":"Maya's costs are $3 in ingredients per loaf plus $10 a week for gas. She charges 9n + 4 per order. Write an expression for her weekly costs if she bakes n loaves, and an expression for her profit if she sells all n loaves in one order. How many loaves must she sell in one order to make a profit of at least $40?","min":47,"rows":5,"rubric":["Correct cost expression","Correct, simplified profit expression","Tests values and finds the correct number of loaves"],"model":"Costs: 3n + 10. Profit: (9n + 4) − (3n + 10) = 9n − 3n + 4 − 10 = 6n − 6. If n = 7, profit is 6(7) − 6 = $36, not enough. If n = 8, profit is 6(8) − 6 = $42. She needs to sell at least 8 loaves."}]},
 "exit": [
  {"t":"text","q":"In the expression 5w + 9, what is the coefficient?","a":["^5","five"],"show":"5","pts":2,"why":"It multiplies the variable w."},
  {"t":"num","q":"Evaluate 4t − 7 when t = 6.","a":17,"pts":2,"why":"24 − 7 = 17."},
  {"t":"text","q":"Write an expression for \"8 more than the product of 3 and a number n.\"","a":["3n+8","3n + 8","8+3n","8 + 3n"],"show":"3n + 8","pts":2,"why":"The product of 3 and n is 3n; 8 more adds 8."},
  {"t":"open","key":"exit_variable","q":"Why is it useful to write a business's prices with a variable?","min":12,"rows":2,"rubric":["One formula gives the price for any number of items","Quick, consistent pricing and easy comparison"],"model":"One formula gives the price for any amount, so the business can quote prices quickly and the same way every time."}],
 "next": "Week 23: solving one-step equations and finding a missing price."
}

TEACHER = {
 "standards": [
  "MA.6.AR.1.1: Given a mathematical or real-world context, translate written descriptions into algebraic expressions and translate algebraic expressions into written descriptions.",
  "MA.6.AR.1.3: Evaluate algebraic expressions using substitution and order of operations.",
  "MA.6.AR.1.4: Apply the properties of operations to generate equivalent algebraic expressions with integer coefficients.",
  "Financial literacy: comparing prices and plans; writing cost formulas (Jump$tart Spending and Saving)."],
 "materials": ["The interactive lesson", "A cereal box or shoebox, scissors, index cards, a marker, tape", "Paper and pencil", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 21 warm-up questions."],
  [4, "Hook", "Maya's 9n + 4 order formula."],
  [12, "Language of algebra", "Parts of an expression; words to symbols and back."],
  [10, "Evaluating", "Substitute with parentheses; fix Kai's −x² mistake."],
  [11, "Equivalent expressions", "Distributive, commutative and associative properties; combine like terms; test with a number."],
  [11, "Cost formulas", "Maya, the phone plans and pet sitting; compare plans."],
  [6, "Assign", "Build the expression machine; assign the price list, Think Deeper and the Exit Check."]],
 "key_questions": ["What does the variable stand for here?", "Which is the rate and which is the fixed fee?", "Did you use parentheses when you substituted?", "How could you check whether two expressions are equivalent?"],
 "misconceptions": ["\"7 less than n\" means 7 − n.", "3(x + 2) = 3x + 2.", "Variables always stand for one fixed secret number.", "4x means 4 + x or a 40-something number."],
 "support": ["Highlight coefficients, variables and constants in three colors.", "Use a words-to-symbols reference card.", "Allow input-output tables before writing formulas."],
 "challenge": ["Write a cost formula for a business with two variables (for example, a price per hour and a price per mile).", "Make a table of costs for Plans A and B for 0 to 5 GB and find where they are closest."],
 "background": "<p>Expressions in this lesson use integer coefficients, consistent with MA.6.AR.1.4. Equations and inequalities are taught in Weeks 23 and 24; the Think Deeper profit question is solved by testing values, not by solving an inequality. Prices are practice figures.</p>",
 "sources": ["Florida Department of Education, B.E.S.T. Standards for Mathematics (2020).", "Jump$tart Coalition, National Standards for Personal Financial Education (2021)."]
}

PRINT = {
 "directions": "Show your work.",
 "items": [
  {"q":"Identify the terms, coefficients and constant in 7a − 2b + 10.","a":"Terms: 7a, −2b, 10; coefficients 7 and −2; constant 10.","lines":2},
  {"q":"Write expressions: (a) 12 less than a number n (b) the quotient of a number and 6 (c) 4 times the sum of a number and 9","a":"(a) n − 12 (b) n/6 (c) 4(n + 9)","lines":2},
  {"q":"Evaluate 5x² − 2y when x = 3 and y = −4.","a":"5(9) − 2(−4) = 45 + 8 = 53.","lines":2},
  {"q":"Simplify: 3(2m + 5) − 4m","a":"6m + 15 − 4m = 2m + 15.","lines":2},
  {"q":"A car wash charges $12 per car plus a $5 travel fee. Write a formula and find the cost for 6 cars.","a":"12c + 5; 12(6) + 5 = $77.","lines":2},
  {"q":"Show that 4(x − 2) and 4x − 8 are equivalent by testing x = 5.","a":"4(3) = 12 and 20 − 8 = 12; same value (and the distributive property shows they are always equal).","lines":2}]
}
