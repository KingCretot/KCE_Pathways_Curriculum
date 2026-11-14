SQ = ('<svg viewBox="0 0 640 220" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Squares and cubes: 3 squared is a 3 by 3 square of 9 tiles; 3 cubed is a 3 by 3 by 3 cube of 27 blocks">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Why we say \"squared\" and \"cubed\"</text>'
  + ''.join(f'<rect x="{60+c*34}" y="{50+r*34}" width="32" height="32" fill="#0047BA"/>' for r in range(3) for c in range(3)) +
  '<text x="111" y="172" text-anchor="middle" font-weight="bold" fill="#0A1F3D">3² = 3 × 3 = 9</text><text x="111" y="190" text-anchor="middle" font-size="11" fill="#5b6676">a square: 9 tiles</text>'
  + ''.join(f'<g transform="translate({360+c*30-r*14},{90+r*14-l*30})"><path d="M0 0 h30 v30 h-30Z" fill="#DB2F30" stroke="#fff"/><path d="M0 0 l14 -14 h30 l-14 14Z" fill="#e86a6a" stroke="#fff"/><path d="M30 0 l14 -14 v30 l-14 14Z" fill="#a8221f" stroke="#fff"/></g>' for l in range(3) for r in range(2, -1, -1) for c in range(3)) +
  '<text x="440" y="172" text-anchor="middle" font-weight="bold" fill="#0A1F3D">3³ = 3 × 3 × 3 = 27</text><text x="440" y="190" text-anchor="middle" font-size="11" fill="#5b6676">a cube: 27 blocks</text>'
  '<text x="320" y="212" text-anchor="middle" font-size="11" fill="#5b6676">In 3⁴, 3 is the base and 4 is the exponent: multiply four 3s.</text></svg>')

GROW = ('<svg viewBox="0 0 600 260" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Bar chart comparing simple interest growth of 500 dollars at 4 percent per year over 5 years">'
  '<text x="300" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="14">$500 saved at 4% simple interest per year</text>'
  '<line x1="60" y1="220" x2="570" y2="220" stroke="#0A1F3D"/><line x1="60" y1="40" x2="60" y2="220" stroke="#0A1F3D"/>'
  + ''.join(f'<rect x="{90+i*90}" y="{220-500*0.3}" width="50" height="{500*0.3}" fill="#0047BA"/><rect x="{90+i*90}" y="{220-(500+20*i)*0.3}" width="50" height="{20*i*0.3}" fill="#C9A84C"/><text x="{115+i*90}" y="{214-(500+20*i)*0.3}" text-anchor="middle" font-weight="bold" fill="#0A1F3D">${500+20*i}</text><text x="{115+i*90}" y="236" text-anchor="middle">Year {i}</text>' for i in range(6)) +
  '<rect x="80" y="34" width="12" height="12" fill="#0047BA"/><text x="98" y="44">principal ($500)</text><rect x="200" y="34" width="12" height="12" fill="#C9A84C"/><text x="218" y="44">interest earned</text>'
  '<text x="300" y="254" text-anchor="middle" font-size="10" fill="#5b6676">Simple interest adds the same $20 every year. Bars start at $0 (scale: 0.3 pixel per dollar).</text></svg>')

LESSON = {
 "unit": "Unit 5: Expressions and Equations",
 "title": "Exponents and Order of Operations",
 "subtitle": "Unit 5 is about the language of algebra. It starts with exponents, a shortcut for repeated multiplication, and the order of operations that tells everyone in the world how to read the same expression the same way. Then you'll see how savings grow with interest.",
 "objectives": [
  "Write repeated multiplication with exponents and evaluate powers, including squares and cubes.",
  "Evaluate powers of fractions, decimals and integers.",
  "Apply the order of operations, including parentheses and exponents, to evaluate expressions.",
  "Explain and correct common order-of-operations mistakes.",
  "Calculate simple interest and compare how savings grow over time."],
 "vocab": [
  ["exponent", "A small raised number that tells how many times to use the base as a factor."],
  ["base", "The number being multiplied repeatedly in a power."],
  ["power", "An expression with a base and an exponent, such as 2⁵."],
  ["squared", "Raised to the power 2, like the area of a square."],
  ["cubed", "Raised to the power 3, like the volume of a cube."],
  ["principal", "The amount of money first saved or borrowed."],
  ["simple interest", "Interest paid only on the principal: I = P × r × t."]],
 "reconnect": {
  "title": "Unit 4: Integers",
  "intro": "Today's expressions include negative numbers, so warm up with Unit 4.",
  "items": [
   {"t":"num","q":"(−3) × (−3) = ?","a":9,"pts":2,"why":"Same signs: positive. Today you'll write it as (−3)²."},
   {"t":"num","q":"(−2) × (−2) × (−2) = ?","a":-8,"pts":2,"why":"Three negatives: negative."},
   {"t":"num","q":"Evaluate: −10 + 4 × (−3)","a":-22,"pts":2,"why":"Multiply first: 4 × (−3) = −12; −10 + (−12) = −22."},
   {"t":"open","key":"rc_oops","q":"In Week 20, Leo subtracted before multiplying and got the wrong answer. Why do we need everyone to agree on an order of operations?","min":12,"rows":2,"rubric":["Without an agreed order, people would get different answers to the same expression"],"model":"If everyone did the steps in a different order, the same expression would give different answers, so we agree on one order."}]},
 "hook": {
  "title": "The Grain of Rice Legend",
  "visual": SQ,
  "html": "<p>An old legend from India tells of a wise man who invented the game of chess and showed it to a king. Delighted, the king offered any reward. The inventor asked for rice: 1 grain on the first square of the chessboard, 2 on the second, 4 on the third, doubling on each square up to the 64th. The king laughed at such a small request, until his treasurers did the math.</p><p>The 64th square alone would need 2⁶³ grains, more than 9 quintillion, far more rice than the world grows in many centuries. Exponents grow shockingly fast. This week you learn to write and use them.</p><div class='callout'><b>Big question:</b> How do exponents and the order of operations let us write big ideas in a small space?</div>"},
 "learn": [
  {"title": "Exponents: Repeated Multiplication",
   "html": "<p>An <b>exponent</b> tells how many times to use the <b>base</b> as a factor:</p><ul><li>2⁵ = 2 × 2 × 2 × 2 × 2 = 32 (not 2 × 5).</li><li>10³ = 10 × 10 × 10 = 1,000. Powers of 10 help write big numbers: a million is 10⁶.</li><li>Any number to the first power is itself: 7¹ = 7.</li></ul><p>A number to the second power is <b>squared</b> because 3² is the area of a 3-by-3 square. A number to the third power is <b>cubed</b> because 3³ is the volume of a 3-by-3-by-3 cube.</p>",
   "checks": [
    {"t":"num","q":"Evaluate 4³.","a":64,"pts":2,"why":"4 × 4 × 4 = 64."},
    {"t":"text","q":"Write 6 × 6 × 6 × 6 × 6 using an exponent.","a":["6^5","6⁵","6 to the 5th","6 to the fifth"],"show":"6⁵","pts":2,"why":"Five factors of 6. On a keyboard, type 6^5."},
    {"t":"open","key":"notmult","q":"Aria says 5² = 10. Explain her mistake and give the correct value.","min":15,"rows":2,"rubric":["She multiplied base × exponent","5² means 5 × 5 = 25"],"model":"Aria multiplied 5 × 2. The exponent means use 5 as a factor two times: 5 × 5 = 25."}]},
  {"title": "Powers of Fractions, Decimals and Negatives",
   "html": "<p>The same idea works for any base:</p><ul><li>(1/2)³ = 1/2 × 1/2 × 1/2 = 1/8.</li><li>(0.3)² = 0.3 × 0.3 = 0.09.</li><li>(−4)² = (−4) × (−4) = 16, but −4² means −(4 × 4) = −16. The parentheses matter: the exponent applies only to what it touches.</li></ul><p>Notice that squaring a fraction between 0 and 1 makes it <b>smaller</b>, not bigger.</p>",
   "checks": [
    {"t":"text","q":"Evaluate (2/3)². Type a fraction.","a":["4/9"],"show":"4/9","pts":2,"why":"2/3 × 2/3 = 4/9."},
    {"t":"num","q":"Evaluate (1.5)².","a":2.25,"tol":0.001,"pts":2,"why":"1.5 × 1.5 = 2.25."},
    {"t":"open","key":"negsquare","q":"Explain why (−5)² and −5² have different values, and find both.","min":20,"rows":2,"rubric":["(−5)² = (−5)(−5) = 25: the exponent applies to −5","−5² = −(5 × 5) = −25: the exponent applies only to 5"],"model":"In (−5)², the parentheses make the whole −5 the base: (−5) × (−5) = 25. In −5², only the 5 is squared, then the result is made negative: −25."}]},
  {"title": "Order of Operations",
   "html": "<p>To evaluate an expression, follow this order:</p><ol><li><b>Grouping symbols</b>: parentheses ( ), brackets [ ] and the fraction bar.</li><li><b>Exponents</b>.</li><li><b>Multiplication and division</b>, from left to right.</li><li><b>Addition and subtraction</b>, from left to right.</li></ol><p>Example: 3 + 2 × (8 − 5)² = 3 + 2 × 3² = 3 + 2 × 9 = 3 + 18 = 21.</p><p>A common memory aid is \"Please Excuse My Dear Aunt Sally,\" but be careful: multiplication does <b>not</b> always come before division, and addition does not always come before subtraction. Those pairs are done left to right.</p>",
   "checks": [
    {"t":"num","q":"Evaluate: 20 − 12 ÷ 4 × 3","a":11,"pts":2,"why":"12 ÷ 4 = 3; 3 × 3 = 9; 20 − 9 = 11."},
    {"t":"num","q":"Evaluate: (6 + 4)² ÷ 5 − 2³","a":12,"pts":2,"why":"10² = 100; 100 ÷ 5 = 20; 2³ = 8; 20 − 8 = 12."},
    {"t":"num","q":"Evaluate: [18 − (3 + 1)²] × (−2)","a":-4,"pts":2,"why":"(4)² = 16; 18 − 16 = 2; 2 × (−2) = −4."},
    {"t":"open","key":"pemdastrap","q":"Jayden evaluated 24 ÷ 4 × 2 as 24 ÷ 8 = 3. Explain his mistake and find the correct value.","min":20,"rows":2,"rubric":["Multiplication and division are done left to right, so divide first","24 ÷ 4 = 6; 6 × 2 = 12"],"model":"Jayden multiplied first because M comes before D in the memory aid, but multiplication and division are done left to right. 24 ÷ 4 = 6, then 6 × 2 = 12."}]},
  {"title": "Money: Simple Interest and Growth",
   "visual": GROW,
   "html": "<p>When you put money in a savings account, the bank pays you <b>interest</b> for letting it use your money. With <b>simple interest</b>, you earn interest only on the <b>principal</b> (the amount you started with):</p><p style='text-align:center;font-size:16px'><b>I = P × r × t</b></p><p>where P is the principal, r is the yearly interest rate as a decimal, and t is the time in years. Maya puts $500 from her bakery into a savings account paying 4% simple interest: I = 500 × 0.04 × 1 = $20 per year. After 5 years: 500 × 0.04 × 5 = $100 in interest, for a total of $600.</p><p>Many real accounts pay <b>compound interest</b>, where interest also earns interest. Then exponents appear: $500 at 4% compounded yearly for 5 years grows to 500 × (1.04)⁵, about $608.33.</p>",
   "checks": [
    {"t":"num","q":"How much simple interest does $800 earn in 3 years at 5% per year?","a":120,"unit":"dollars","pts":2,"why":"800 × 0.05 × 3 = 120."},
    {"t":"num","q":"Maya's $500 earns 4% simple interest. What is her total after 8 years?","a":660,"unit":"dollars","pts":2,"why":"Interest: 500 × 0.04 × 8 = 160; total 500 + 160 = 660."},
    {"t":"open","key":"compoundwhy","q":"After 5 years, Maya's $500 grows to $600 with simple interest but about $608.33 with yearly compound interest. Explain why compound interest grows more.","min":25,"rows":3,"rubric":["Compound interest is paid on the principal plus earlier interest","So each year's interest is a little bigger, and the gap grows over time"],"model":"With compound interest, each year's interest is added to the balance, and the next year's interest is figured on that bigger amount. So the interest itself earns interest, and each year's growth is a little larger than the year before."}]}],
 "handson": {
  "title": "Doubling Rice and the Order-of-Operations Card Game",
  "intro": "Watch exponents grow with real rice, then race to build expressions with the order of operations.",
  "materials": ["A bag of uncooked rice (or dried beans)", "A muffin tin, egg carton or 10 small cups", "A kitchen scale (optional)", "A deck of playing cards (face cards removed)", "A family member", "Paper and pencil"],
  "steps": [
   "Rice doubling: put 1 grain in the first cup, 2 in the second, 4 in the third, and keep doubling. Fill as many cups as you can (at least 8). Write each amount as a power of 2: 2⁰ = 1, 2¹ = 2, 2² = 4 ...",
   "Estimate: how many cups could you fill before you ran out of rice? A 2-pound bag holds roughly 40,000 grains. Which power of 2 is closest to 40,000?",
   "Card game: deal 4 cards each. Flip one more card as the target. Using all 4 of your cards, parentheses, exponents and the four operations, build an expression equal to the target (or as close as possible). Write it down and evaluate it step by step for your partner to check.",
   "Play 5 rounds. Score 2 points for an exact match and 1 point for being within 2.",
   "Keep the rice away from young children (a choking hazard) and pour it back into the bag to cook later."],
  "record": [
   {"t":"open","key":"ricerec","q":"Record how many grains were in each cup you filled, written as powers of 2. Which power of 2 is closest to 40,000? Explain what this shows about how fast doubling grows.","min":30,"rows":4,"rubric":["Correct powers of 2 for each cup","2¹⁵ = 32,768 (or 2¹⁶ = 65,536) closest to 40,000","Explains rapid growth"],"model":"Cups: 2⁰ = 1, 2¹ = 2, 2² = 4, 2³ = 8, 2⁴ = 16, 2⁵ = 32, 2⁶ = 64, 2⁷ = 128, 2⁸ = 256. 2¹⁵ = 32,768 is closest to 40,000, so a whole 2-pound bag would run out around cup 16. Doubling grows so fast that just 16 cups use up a whole bag, and 64 squares would need more rice than exists."},
   {"t":"open","key":"cardrec","q":"Write your two best expressions from the card game, evaluate each step by step, and name the target.","min":30,"rows":4,"rubric":["Two expressions using four cards","Correct step-by-step evaluation following the order of operations","Target named"],"model":"Target 10, cards 2, 3, 4, 6: (3 + 2) × (6 − 4) = 5 × 2 = 10, an exact match for 2 points. Target 18, cards 4, 1, 5, 2: 4² + (5 − 2) − 1 = 16 + 3 − 1 = 18, also exact. I used each card once and did the parentheses first, then the exponent, then left to right."}]},
 "think": {
  "intro": "Explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"savingsplan","q":"Maya has $1,200 to save for 6 years. Bank A pays 3% simple interest. Bank B pays 2.5% simple interest but adds a one-time $50 bonus when she opens the account. Which bank gives her more money after 6 years? Show your work for both.","min":33,"rows":5,"rubric":["Bank A: 1,200 × 0.03 × 6 = 216; total 1,416","Bank B: 1,200 × 0.025 × 6 = 180, plus 50 = 230; total 1,430","Bank B gives $14 more","Clear work"],"model":"Bank A: 1,200 × 0.03 × 6 = $216 interest, so $1,416. Bank B: 1,200 × 0.025 × 6 = $180 interest plus a $50 bonus = $230, so $1,430. Bank B gives Maya $14 more after 6 years."},
   {"t":"open","key":"insertparen","q":"Insert parentheses to make each statement true, and explain how parentheses change the value: (a) 2 + 3² × 4 = 100 (b) 18 − 6 ÷ 3 + 3 = 7","min":30,"rows":4,"rubric":["(a) (2 + 3)² × 4 = 100","(b) (18 − 6) ÷ 3 + 3 = 7","Explains that parentheses change which operation happens first"],"model":"(a) (2 + 3)² × 4 = 5² × 4 = 25 × 4 = 100. Without parentheses it would be 2 + 9 × 4 = 38. (b) (18 − 6) ÷ 3 + 3 = 12 ÷ 3 + 3 = 4 + 3 = 7. Without parentheses it would be 18 − 2 + 3 = 19. Parentheses tell you which operation to do first, which changes the answer."}]},
 "exit": [
  {"t":"num","q":"Evaluate 2⁶.","a":64,"pts":2,"why":"2 × 2 × 2 × 2 × 2 × 2 = 64."},
  {"t":"num","q":"Evaluate: 5 + 3 × 2²","a":17,"pts":2,"why":"2² = 4; 3 × 4 = 12; 5 + 12 = 17."},
  {"t":"num","q":"How much simple interest does $300 earn in 2 years at 6%?","a":36,"unit":"dollars","pts":2,"why":"300 × 0.06 × 2 = 36."},
  {"t":"open","key":"exit_order","q":"List the order of operations in your own words.","min":12,"rows":2,"rubric":["Grouping symbols, exponents, multiply and divide left to right, add and subtract left to right"],"model":"First do anything in parentheses or other grouping symbols, then exponents, then multiply and divide from left to right, then add and subtract from left to right."}],
 "next": "Week 22: writing and evaluating expressions with variables, and writing cost formulas."
}

TEACHER = {
 "standards": [
  "MA.6.NSO.3.3: Evaluate positive rational numbers and integers with natural number exponents.",
  "MA.6.NSO.3.4: Express composite whole numbers as a product of prime factors with natural number exponents.",
  "MA.6.AR.1.3: Evaluate algebraic expressions using substitution and order of operations.",
  "Financial literacy: saving, interest and growth (Jump$tart Saving)."],
 "materials": ["The interactive lesson", "Uncooked rice or dried beans, a muffin tin or egg carton", "A deck of playing cards (face cards removed)", "Paper and pencil", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Unit 4 warm-up questions."],
  [4, "Hook", "The rice and chessboard legend."],
  [10, "Exponents", "Squares and cubes; powers of 10; fix Aria's mistake."],
  [9, "Fractions, decimals, negatives", "(1/2)³, (0.3)², and (−4)² versus −4²."],
  [13, "Order of operations", "Work the examples; the left-to-right pairs; fix Jayden's mistake."],
  [12, "Simple interest", "I = Prt; Maya's savings; simple versus compound."],
  [6, "Assign", "Start the rice doubling; assign the card game, Think Deeper and the Exit Check."]],
 "key_questions": ["What is the base, and how many times is it a factor?", "What does the exponent touch?", "Which operation comes next, and are these two done left to right?", "Is the interest earned only on the principal?"],
 "misconceptions": ["2⁵ means 2 × 5.", "Multiplication always comes before division.", "−4² equals 16.", "Squaring always makes a number bigger."],
 "support": ["Write out repeated multiplication before evaluating.", "Underline the next operation at each step.", "Use a percent-to-decimal reference card."],
 "challenge": ["How many grains would be on the whole chessboard? (2⁶⁴ − 1.) Research how that compares with world rice production.", "Compare simple and compound interest on $1,000 at 5% for 20 years."],
 "background": "<p>The wheat and chessboard (or rice) legend appears in many versions, often attributed to India and to the invention of chess (chaturanga). 2⁶³ ≈ 9.22 × 10¹⁸; the whole board totals 2⁶⁴ − 1 ≈ 1.8 × 10¹⁹ grains. A 2-pound bag of long-grain rice holds roughly 30,000 to 45,000 grains, depending on the variety. Compound interest appears here only as a preview; it is not assessed.</p>",
 "sources": ["Florida Department of Education, B.E.S.T. Standards for Mathematics (2020).", "Jump$tart Coalition, National Standards for Personal Financial Education (2021).", "FDIC, Money Smart for Young People."]
}

PRINT = {
 "directions": "Show your work.",
 "items": [
  {"q":"Evaluate: (a) 3⁴ (b) 10⁵ (c) (1/3)² (d) (−2)⁵","a":"(a) 81 (b) 100,000 (c) 1/9 (d) −32","lines":2},
  {"q":"Write with an exponent: (a) 7 × 7 × 7 (b) 0.5 × 0.5 × 0.5 × 0.5","a":"(a) 7³ (b) (0.5)⁴","lines":1},
  {"q":"Evaluate: 4 + 18 ÷ 3² × 2","a":"3² = 9; 18 ÷ 9 = 2; 2 × 2 = 4; 4 + 4 = 8.","lines":2},
  {"q":"Evaluate: (15 − 3 × 2)² − 4 × 5","a":"15 − 6 = 9; 9² = 81; 81 − 20 = 61.","lines":2},
  {"q":"Find the simple interest on $650 at 4% for 3 years, and the total.","a":"650 × 0.04 × 3 = $78; total $728.","lines":2},
  {"q":"Explain the difference between −3² and (−3)².","a":"−3² = −9 (only 3 is squared); (−3)² = 9 (−3 is the base).","lines":2}]
}
