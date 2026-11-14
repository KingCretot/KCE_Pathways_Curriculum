PATTERN = ('<svg viewBox="0 0 600 250" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="14" role="img" aria-label="Pattern table showing why a negative times a negative is positive">'
  '<text x="300" y="22" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Follow the pattern</text>'
  + ''.join(f'<text x="60" y="{56+i*28}" font-family="Courier New, monospace" fill="#0A1F3D">{a}</text>' for i, a in enumerate(["3 × (−4) = −12", "2 × (−4) =  −8", "1 × (−4) =  −4", "0 × (−4) =   0", "−1 × (−4) =   4", "−2 × (−4) =   8", "−3 × (−4) =  12"])) +
  '<path d="M250 50 v170" stroke="#0047BA" stroke-width="2"/><text x="262" y="140" font-size="12" fill="#0047BA">each answer goes</text><text x="262" y="156" font-size="12" fill="#0047BA">UP by 4</text>'
  '<rect x="380" y="56" width="200" height="150" rx="12" fill="#0A1F3D"/><text x="480" y="84" text-anchor="middle" fill="#C9A84C" font-weight="bold">Sign rules</text>'
  + ''.join(f'<text x="480" y="{112+i*24}" text-anchor="middle" fill="#fff" font-size="13">{t}</text>' for i, t in enumerate(["positive × positive = +", "negative × negative = +", "positive × negative = −", "same rules for dividing"])) +
  '<text x="300" y="242" text-anchor="middle" font-size="11" fill="#5b6676">Keep the pattern going past zero and the products become positive.</text></svg>')

LESSON = {
 "unit": "Unit 4: Integers and the Coordinate Plane",
 "title": "Multiplying and Dividing Integers",
 "subtitle": "Last week you added and subtracted integers. Now you multiply and divide them: repeated losses, average changes and sharing debts. And you finally find out why a negative times a negative is positive.",
 "objectives": [
  "Model multiplication of integers as repeated addition and with patterns.",
  "Explain and apply the sign rules for multiplying and dividing integers.",
  "Divide integers and interpret the quotient in context (average change, equal shares).",
  "Evaluate expressions with integers using the order of operations you already know.",
  "Calculate profit and loss for a small business, including average weekly profit."],
 "vocab": [
  ["product", "The result of multiplying."],
  ["quotient", "The result of dividing."],
  ["factor", "A number being multiplied."],
  ["average change", "The total change divided by the number of time periods."],
  ["revenue", "All the money a business takes in from sales."],
  ["profit", "Revenue minus expenses, when the result is positive."],
  ["loss", "Revenue minus expenses, when the result is negative."]],
 "reconnect": {
  "title": "Week 18: Adding and subtracting integers",
  "intro": "Multiplication is repeated addition, so last week's skills are today's building blocks.",
  "items": [
   {"t":"num","q":"−8 + (−8) + (−8) = ?","a":-24,"pts":2,"why":"Three groups of −8: −24. Today you'll write this as 3 × (−8)."},
   {"t":"num","q":"6 − (−9) = ?","a":15,"pts":2,"why":"6 + 9 = 15."},
   {"t":"num","q":"A credit card balance is −$70. The owner pays $45. What is the new balance?","a":-25,"unit":"dollars","pts":2,"why":"−70 + 45 = −25."},
   {"t":"open","key":"rc_subneg","q":"Explain why subtracting a negative number makes the result greater.","min":12,"rows":2,"rubric":["Subtracting a number is adding its opposite; the opposite of a negative is positive (or: taking away a debt leaves you better off)"],"model":"Subtracting a number is the same as adding its opposite, and the opposite of a negative number is positive, so the result goes up."}]},
 "hook": {
  "title": "Losing Altitude",
  "html": "<p>A hot-air balloon over the Florida countryside drops 12 feet every minute for 5 minutes as it comes in to land. How far does it drop? A change of −12 feet, five times: 5 × (−12) = −60 feet.</p><p>Now rewind the video. Five minutes <i>before</i> landing, where was the balloon compared with now? Playing a loss backward in time is like multiplying two negatives, and it gives a positive answer: it was 60 feet higher. This week you'll see why that pattern always holds.</p><div class='callout'><b>Big question:</b> What happens to the sign of a number when you multiply or divide with negatives?</div>"},
 "learn": [
  {"title": "Multiplying: Repeated Groups",
   "html": "<p>Multiplication means equal groups:</p><ul><li>4 × 3 = 12: four groups of +3.</li><li>4 × (−3) = −12: four groups of −3, like losing $3 four times.</li><li>(−3) × 4 = −12 too: multiplication works in either order.</li></ul><p>So a <b>positive times a negative is negative</b>. Products with more than two factors follow the same idea: count the negative factors. An even number of negatives gives a positive product; an odd number gives a negative product. For example, (−2) × (−3) × (−1) has three negatives, so it is −6.</p>",
   "checks": [
    {"t":"num","q":"6 × (−7) = ?","a":-42,"pts":2,"why":"Six groups of −7."},
    {"t":"num","q":"A diver descends 9 feet per minute for 4 minutes. Write the change in depth as an integer.","a":-36,"unit":"feet","pts":2,"why":"4 × (−9) = −36 feet."},
    {"t":"open","key":"oddeven","q":"Without multiplying, decide whether (−1) × (−1) × (−1) × (−1) × (−1) is positive or negative, and explain how you know.","min":15,"rows":2,"rubric":["Negative","Five negative factors is an odd number"],"model":"Negative. There are five negative factors, an odd number, so the product is negative. (It equals −1.)"}]},
  {"title": "Why Negative × Negative Is Positive",
   "visual": PATTERN,
   "html": "<p>Look at the pattern table. As the first factor goes down by 1 each row, the product goes <b>up</b> by 4. When the first factor drops below zero, the pattern keeps going: −1 × (−4) = 4, −2 × (−4) = 8. So a <b>negative times a negative is positive</b>.</p><p>A story makes it feel real: Maya's bakery loses $4 of flour to spills each day (−4 per day). Three days <i>ago</i> (−3 days), she had $12 <i>more</i> flour than now: (−3) × (−4) = +12.</p><p>Another way to think of it: a negative sign means \"the opposite of.\" −3 × (−4) is the opposite of 3 × (−4), and the opposite of −12 is 12.</p>",
   "checks": [
    {"t":"num","q":"(−8) × (−5) = ?","a":40,"pts":2,"why":"Negative × negative = positive."},
    {"t":"num","q":"(−2) × 3 × (−5) = ?","a":30,"pts":2,"why":"Two negatives: positive. 2 × 3 × 5 = 30."},
    {"t":"open","key":"explainnegneg","q":"Use the pattern table or a story to explain to a younger student why (−2) × (−6) = 12.","min":30,"rows":3,"rubric":["Uses a correct pattern (products increase by 6 as the first factor decreases) or a valid story (reversing a loss, the opposite of a negative)","Reaches 12 with clear reasoning"],"model":"2 × (−6) = −12, 1 × (−6) = −6, 0 × (−6) = 0. Each time the first number goes down by 1, the answer goes up by 6. Keep going: −1 × (−6) = 6, −2 × (−6) = 12."}]},
  {"title": "Dividing Integers",
   "html": "<p>Division undoes multiplication, so the sign rules are the same:</p><ul><li>−24 ÷ 6 = −4, because 6 × (−4) = −24.</li><li>−24 ÷ (−6) = 4, because −6 × 4 = −24.</li><li>24 ÷ (−6) = −4.</li></ul><p><b>Same signs: positive quotient. Different signs: negative quotient.</b> Dividing by zero is undefined.</p><p><b>Average change:</b> if the temperature fell 18 degrees over 6 hours, the average change was −18 ÷ 6 = −3 degrees per hour.</p><p><b>Order of operations</b> still applies: multiply and divide (left to right) before you add and subtract. For example, −3 + 4 × (−2) = −3 + (−8) = −11.</p>",
   "checks": [
    {"t":"num","q":"−56 ÷ (−8) = ?","a":7,"pts":2,"why":"Same signs: positive."},
    {"t":"num","q":"A stock's value changed by −$45 over 5 days. What was the average change per day?","a":-9,"unit":"dollars","pts":2,"why":"−45 ÷ 5 = −9 dollars per day."},
    {"t":"num","q":"Evaluate: 10 + (−12) ÷ 4 × (−2)","a":16,"pts":2,"why":"−12 ÷ 4 = −3; −3 × (−2) = 6; 10 + 6 = 16."},
    {"t":"open","key":"divzero","q":"Explain why −15 ÷ 0 has no answer. Use the connection between multiplication and division.","min":20,"rows":2,"rubric":["Division undoes multiplication: −15 ÷ 0 = ? means 0 × ? = −15","No number times 0 gives −15"],"model":"−15 ÷ 0 would have to be a number that, times 0, gives −15. But any number times 0 is 0, so no number works. Division by zero is undefined."}]},
  {"title": "Money: Profit and Loss",
   "html": "<p>A business's <b>profit</b> or <b>loss</b> is revenue minus expenses. Maya tracks her bakery's weekly results as integers (in dollars):</p><div class='card' style='font-family:Courier New,monospace;font-size:14px'>Week 1 &nbsp; +$48<br>Week 2 &nbsp; −$14 (bought a new oven thermometer and baskets)<br>Week 3 &nbsp; +$52<br>Week 4 &nbsp; +$38<br>Week 5 &nbsp; −$24 (flour price jumped; she didn't raise prices)<br>Week 6 &nbsp; +$60</div><p>To find her <b>average weekly profit</b>, add all the weeks and divide by the number of weeks. She also wonders about the future: if a bad month brings a loss of $8 a week, what would four such weeks do? 4 × (−8) = −32.</p>",
   "checks": [
    {"t":"num","q":"What is Maya's total for the six weeks?","a":160,"unit":"dollars","pts":2,"why":"48 − 14 + 52 + 38 − 24 + 60 = 160."},
    {"t":"num","q":"What is her average weekly profit? Round to the nearest cent if needed.","a":26.67,"tol":0.01,"unit":"dollars","pts":2,"why":"160 ÷ 6 ≈ 26.67 dollars per week."},
    {"t":"num","q":"Maya sells loaves at $9. Each loaf costs her $3 in ingredients. One week, she bakes 20 loaves but sells only 14, and the rest go stale. What is her profit or loss? Use a negative number for a loss.","a":66,"unit":"dollars","pts":2,"why":"Revenue: 14 × $9 = $126. Expenses: 20 × $3 = $60. 126 − 60 = $66 profit."},
    {"t":"open","key":"pricerise","q":"In Week 5, flour prices jumped and Maya lost money. Suggest two business decisions she could make, and use integers to show how one of them would change her result.","min":40,"rows":4,"rubric":["Two reasonable decisions (raise prices, bake fewer loaves, buy flour in bulk, add a higher-priced product)","Shows with numbers how one decision changes profit or loss"],"model":"She could raise her price to $10 or buy flour in bulk at a lower price. If she sells 14 loaves at $10 instead of $9, that's 14 × $1 = $14 more revenue, which would turn her −$24 week into −$10, much closer to breaking even."}]}],
 "handson": {
  "title": "Integer Product War and the Bakery Ledger",
  "intro": "Play a card game that practices sign rules, then build a bakery (or other business) ledger of profits and losses.",
  "materials": ["A deck of playing cards with face cards removed (black = positive, red = negative)", "A family member", "Paper and pencil", "Optional: a real recipe and grocery receipt or online prices"],
  "steps": [
   "Product War: use last week's card rule (black = positive, red = negative), but now multiply. Each player flips two cards and multiplies them. The greater product wins all four cards. Play at least 10 rounds, saying each product aloud.",
   "Quotient round: flip two cards. Divide the larger number (ignoring signs) by the smaller, then decide the sign of the quotient. Keep any quotient that is not a whole number as a fraction.",
   "Bakery ledger: choose a product you could make and sell (cookies, bread, bracelets, dog treats). Estimate the cost to make one and the price you would charge.",
   "Write 6 weeks of results as integers, including at least two weeks with a loss and a reason for each (a price jump, a rainy market day, a big purchase).",
   "Find your total and average weekly profit or loss."],
  "record": [
   {"t":"open","key":"warrec","q":"Write five Product War rounds and two quotient rounds with the cards and answers. Did you notice a pattern about when products were positive?","min":30,"rows":4,"rubric":["Five products and two quotients, with correct signs and values","States the pattern: same signs positive, different signs negative"],"model":"Black 7 × red 6 = −42. Red 4 × red 9 = 36. Black 8 × black 3 = 24. Red 10 × black 2 = −20. Red 5 × red 5 = 25. Quotients: red 8 ÷ black 2 = −4; red 9 ÷ red 3 = 3. Pattern: two cards of the same color gave a positive product; different colors gave a negative one."},
   {"t":"open","key":"ledgerrec","q":"Share your business, your cost and price per item, your 6-week ledger with reasons for losses, and your total and average weekly result.","min":38,"rows":6,"rubric":["Business, cost and price","Six weekly integers including two losses with reasons","Correct total and average"],"model":"Dog treats: cost $0.50 a bag, price $3. Week 1: +$24. Week 2: −$10 (bought cookie cutters and bags). Week 3: +$18. Week 4: −$4 (rainy market, few sales). Week 5: +$30. Week 6: +$20. Total: +$78. Average: 78 ÷ 6 = $13 a week."}]},
 "think": {
  "intro": "Explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"tempavg","q":"Over 5 nights in Tallahassee, the low temperature changed from the night before by −4, +2, −7, −3 and +2 degrees. Find the total change and the average change per night, and describe what the average means.","min":36,"rows":4,"rubric":["Total: −10 degrees","Average: −10 ÷ 5 = −2 degrees per night","Interprets: on average the low dropped 2 degrees each night"],"model":"Total change: −4 + 2 − 7 − 3 + 2 = −10 degrees. Average: −10 ÷ 5 = −2 degrees per night. It means that, overall, the nights got colder by about 2 degrees each night, even though some nights warmed up."},
   {"t":"open","key":"signerror","q":"Jordan says, \"Two negatives make a positive, so −6 + (−4) = 10.\" Explain his mistake, give the correct answer, and give an example where \"two negatives make a positive\" really is true.","min":39,"rows":4,"rubric":["The rule applies to multiplying and dividing, not adding","Correct answer: −10","A correct example (−6 × (−4) = 24, or −24 ÷ (−6) = 4)"],"model":"Jordan mixed up the rules. \"Two negatives make a positive\" is true for multiplying and dividing, not adding. Adding two negatives is like owing $6 and then owing $4 more: −6 + (−4) = −10. But −6 × (−4) = 24, where the rule does work."}]},
 "exit": [
  {"t":"num","q":"(−9) × 7 = ?","a":-63,"pts":2,"why":"Different signs: negative."},
  {"t":"num","q":"(−72) ÷ (−9) = ?","a":8,"pts":2,"why":"Same signs: positive."},
  {"t":"num","q":"A business had results of +$30, −$12 and −$6 over three weeks. What was its average weekly profit?","a":4,"unit":"dollars","pts":2,"why":"(30 − 12 − 6) ÷ 3 = 12 ÷ 3 = 4."},
  {"t":"open","key":"exit_signs","q":"How do you decide the sign of the answer when you multiply or divide two integers?","min":12,"rows":2,"rubric":["Same signs: positive; different signs: negative"],"model":"If the signs are the same, the answer is positive. If they're different, it's negative."}],
 "next": "Week 20: Unit 4 review and checkpoint."
}

TEACHER = {
 "standards": [
  "MA.6.NSO.4.2: Apply and extend previous understandings of operations with whole numbers to multiply and divide integers with procedural fluency.",
  "MA.6.NSO.4.1: Apply and extend previous understandings of operations with whole numbers to add and subtract integers with procedural fluency.",
  "MA.K12.MTR.5.1: Use patterns and structure to help understand and connect mathematical concepts.",
  "Financial literacy: revenue, expenses, profit and loss (Jump$tart Earning Income)."],
 "materials": ["The interactive lesson", "A deck of playing cards (face cards removed)", "Paper and pencil", "Optional: a recipe and grocery prices", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 18 warm-up questions."],
  [4, "Hook", "The balloon dropping and the rewind."],
  [10, "Multiplying", "Groups of negatives; counting negative factors."],
  [12, "Negative × negative", "Extend the pattern table; the flour story; \"opposite of.\""],
  [11, "Dividing", "Sign rules for division; average change; order of operations with integers; dividing by zero."],
  [11, "Profit and loss", "Total and average Maya's weeks; the stale-loaf problem; pricing decisions."],
  [6, "Assign", "Play two rounds of Product War; assign the ledger, Think Deeper and the Exit Check."]],
 "key_questions": ["How many negative factors are there?", "What does this quotient mean in the story?", "Is this rule for adding or for multiplying?", "Did the business make or lose money, and why?"],
 "misconceptions": ["Two negatives always make a positive, even when adding.", "Negative × negative is negative because \"negatives make it smaller.\"", "Order of operations doesn't apply to integers.", "Average must be positive."],
 "support": ["Keep the sign-rule card visible.", "Use repeated addition on a number line for positive × negative.", "Let students build the pattern table themselves."],
 "challenge": ["Find three integers whose product is −24 and whose sum is −1.", "Investigate: is (−2) to the power 10 positive or negative? What about (−2) to the power 11?"],
 "background": "<p>MA.6.NSO.4.2 completes the integer operations benchmarks in Grade 6 B.E.S.T. The pattern argument and the \"opposite of\" argument are both standard justifications for the sign rules; avoid teaching the rule as an unexplained slogan. Order of operations with whole numbers was taught earlier in the year; exponents are formally studied in Week 21. All business figures are practice data.</p>",
 "sources": ["Florida Department of Education, B.E.S.T. Standards for Mathematics (2020).", "Jump$tart Coalition, National Standards for Personal Financial Education (2021)."]
}

PRINT = {
 "directions": "Show your work.",
 "items": [
  {"q":"Find each product: (a) 8 × (−6) (b) (−7) × (−7) (c) (−1) × 4 × (−3) × (−2)","a":"(a) −48 (b) 49 (c) −24","lines":2},
  {"q":"Find each quotient: (a) −81 ÷ 9 (b) −36 ÷ (−4) (c) 50 ÷ (−10)","a":"(a) −9 (b) 9 (c) −5","lines":2},
  {"q":"A submarine descends 25 feet per minute for 8 minutes. What is its change in depth?","a":"8 × (−25) = −200 feet.","lines":2},
  {"q":"The temperature dropped 21 degrees over 7 hours. What was the average change per hour?","a":"−21 ÷ 7 = −3 degrees per hour.","lines":2},
  {"q":"Evaluate: −20 ÷ 5 + 3 × (−4)","a":"−4 + (−12) = −16.","lines":2},
  {"q":"A lemonade stand has weekly results of +$15, −$6, +$21, −$3 and +$13. Find the total and the average weekly profit.","a":"Total $40; average $8 per week.","lines":2}]
}
