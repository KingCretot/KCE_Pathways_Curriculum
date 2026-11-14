FACTOR = ('<svg viewBox="0 0 560 210" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Factor trees for 36 and 48">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Factor trees: break a number into primes</text>'
  # 36 tree
  '<g><text x="140" y="48" text-anchor="middle" font-weight="bold">36</text><path d="M134 54 L100 82 M146 54 L180 82" stroke="#0A1F3D"/>'
  '<text x="100" y="98" text-anchor="middle">4</text><text x="180" y="98" text-anchor="middle">9</text>'
  '<path d="M96 104 L76 132 M104 104 L124 132 M176 104 L156 132 M184 104 L204 132" stroke="#0A1F3D"/>'
  + ''.join(f'<circle cx="{x}" cy="144" r="13" fill="#C9A84C"/><text x="{x}" y="149" text-anchor="middle" font-weight="bold">{n}</text>' for x, n in [(76, 2), (124, 2), (156, 3), (204, 3)]) +
  '<text x="140" y="186" text-anchor="middle">36 = 2 × 2 × 3 × 3</text></g>'
  # 48 tree
  '<g><text x="410" y="48" text-anchor="middle" font-weight="bold">48</text><path d="M404 54 L370 82 M416 54 L450 82" stroke="#0A1F3D"/>'
  '<text x="370" y="98" text-anchor="middle">6</text><text x="450" y="98" text-anchor="middle">8</text>'
  '<path d="M366 104 L346 132 M374 104 L394 132 M446 104 L426 132 M454 104 L474 132" stroke="#0A1F3D"/>'
  + ''.join(f'<circle cx="{x}" cy="144" r="13" fill="#C9A84C"/><text x="{x}" y="149" text-anchor="middle" font-weight="bold">{n}</text>' for x, n in [(346, 2), (394, 3), (426, 2)]) +
  '<text x="474" y="149" text-anchor="middle">4</text><path d="M470 156 L462 170 M478 156 L486 170" stroke="#0A1F3D"/>'
  + ''.join(f'<circle cx="{x}" cy="180" r="11" fill="#C9A84C"/><text x="{x}" y="185" text-anchor="middle" font-weight="bold" font-size="12">2</text>' for x in (458, 490)) +
  '<text x="380" y="204" text-anchor="middle">48 = 2 × 2 × 2 × 2 × 3</text></g></svg>')

VENN = ('<svg viewBox="0 0 560 225" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="14" role="img" aria-label="Venn diagram of prime factors of 36 and 48">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Shared primes give the GCF; all primes give the LCM</text>'
  '<circle cx="220" cy="115" r="75" fill="#0047BA" fill-opacity=".15" stroke="#0047BA" stroke-width="2"/><circle cx="340" cy="115" r="75" fill="#DB2F30" fill-opacity=".15" stroke="#DB2F30" stroke-width="2"/>'
  '<text x="160" y="42" text-anchor="middle" font-weight="bold" fill="#0047BA">36</text><text x="400" y="42" text-anchor="middle" font-weight="bold" fill="#DB2F30">48</text>'
  '<text x="180" y="115" text-anchor="middle" font-size="18">3</text>'
  '<text x="280" y="96" text-anchor="middle" font-size="18">2   2</text><text x="280" y="126" text-anchor="middle" font-size="18">3</text>'
  '<text x="380" y="115" text-anchor="middle" font-size="18">2   2</text>'
  '<text x="20" y="214" font-size="12">GCF = 2 × 2 × 3 = 12 (the middle)</text><text x="300" y="214" font-size="12">LCM = 3 × 2 × 2 × 3 × 2 × 2 = 144 (everything)</text></svg>')

def savings():
    s = ('<svg viewBox="0 0 560 220" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Savings goal progress chart">'
         '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Amara\'s goal: a $189.50 stand mixer for the bakery</text>')
    x0, y0, w, h = 60, 190, 460, 150
    s += f'<line x1="{x0}" y1="{y0}" x2="{x0+w}" y2="{y0}" stroke="#0A1F3D"/><line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0-h}" stroke="#0A1F3D"/>'
    for v in range(0, 201, 50):
        y = y0 - v / 200 * h
        s += f'<line x1="{x0}" y1="{y}" x2="{x0+w}" y2="{y}" stroke="#e1e6ee"/><text x="{x0-6}" y="{y+4}" text-anchor="end">${v}</text>'
    gy = y0 - 189.5 / 200 * h
    s += f'<line x1="{x0}" y1="{gy}" x2="{x0+w}" y2="{gy}" stroke="#DB2F30" stroke-dasharray="6 4"/><text x="{x0+w}" y="{gy-6}" text-anchor="end" fill="#DB2F30" font-weight="bold">goal $189.50</text>'
    for i in range(9):
        amt = 42 + 18.5 * i
        bh = amt / 200 * h
        s += f'<rect x="{x0+12+i*50}" y="{y0-bh}" width="32" height="{bh}" fill="#0047BA" opacity="{1 if i < 5 else .25}"/><text x="{x0+28+i*50}" y="{y0+14}" text-anchor="middle">W{i}</text>'
    s += f'<text x="{x0+w/2}" y="{y0+28}" text-anchor="middle" font-size="11">Week (W0 = today, $42.00 saved; faded bars are the plan)</text></svg>'
    return s

LESSON = {
 "unit": "Unit 1: Number Power",
 "title": "GCF, LCM and Unit 1 Checkpoint",
 "subtitle": "Factors and multiples solve real puzzles: packing equal bags, lining up schedules, and planning how long a savings goal will take.",
 "objectives": [
  "Find the prime factorization of a whole number with a factor tree.",
  "Find the greatest common factor (GCF) and least common multiple (LCM) of two numbers.",
  "Decide whether a real-world problem calls for the GCF or the LCM.",
  "Plan a savings goal: find how much is left and how many weeks it will take.",
  "Show mastery of Unit 1 on the checkpoint (85 or higher)."],
 "vocab": [
  ["factor", "A whole number that divides another number with no remainder. 4 is a factor of 36."],
  ["multiple", "The product of a number and a whole number. 36, 72 and 108 are multiples of 36."],
  ["prime number", "A whole number greater than 1 with exactly two factors, 1 and itself, such as 2, 3, 5, 7 and 11."],
  ["composite number", "A whole number greater than 1 with more than two factors, such as 4, 9 and 36."],
  ["prime factorization", "A number written as a product of prime numbers: 36 = 2 × 2 × 3 × 3."],
  ["greatest common factor (GCF)", "The largest factor two or more numbers share."],
  ["least common multiple (LCM)", "The smallest multiple two or more numbers share (other than 0)."],
  ["savings goal", "A specific amount of money you plan to save by a certain time, for a certain purpose."]],
 "reconnect": {
  "title": "Week 4: dividing decimals and unit prices",
  "intro": "Division is the heart of factors, so start with last week's skills and words.",
  "items": [
   {"t":"num","q":"4.56 ÷ 0.12 = ?","a":38,"pts":2,"why":"Multiply both by 100: 456 ÷ 12 = 38."},
   {"t":"num","q":"8.75 ÷ 5 = ?","a":1.75,"pts":2,"why":"Long division with the decimal point straight up: 1.75."},
   {"t":"text","q":"In 8.75 ÷ 5 = 1.75, which number is the divisor?","a":["5","five"],"show":"5","pts":2,"why":"The divisor is the number you divide by."},
   {"t":"num","q":"A 24-ounce box of cereal costs $5.04. What is the unit price per ounce?","a":0.21,"tol":0.001,"unit":"dollars per oz","show":"$0.21 per ounce","pts":3,"why":"5.04 ÷ 24 = $0.21 per ounce."},
   {"t":"num","q":"A 15-ounce box of the same cereal costs $3.45. How much cheaper per ounce is the 24-ounce box, in dollars?","a":0.02,"tol":0.001,"unit":"dollars per oz","show":"$0.02 per ounce","pts":3,"why":"3.45 ÷ 15 = $0.23 per ounce. 0.23 − 0.21 = $0.02 cheaper."},
   {"t":"open","key":"rc_bulk","q":"Give one reason a family might buy the 15-ounce box anyway, even though it costs more per ounce.","min":10,"rows":2,"rubric":["A real-life reason: spoilage, storage, budget today, trying a new kind"],"model":"If they have only $4 left in this week's budget, they cannot afford the big box today, even though it is the better unit price."}]},
 "hook": {
  "title": "Packing the Bakery Bags",
  "html": "<p>Amara's banana bread business from Week 1 is growing. For the farmers market she has 36 mini muffins and 48 cookies. She wants to pack identical bags, with the same mix of muffins and cookies in every bag and nothing left over. What is the greatest number of bags she can make?</p><p>She also has a new goal: a $189.50 stand mixer. She has $42.00 saved. How long will it take?</p><div class='callout'><b>Big idea:</b> The GCF splits things into the largest equal groups. The LCM finds when things line up again. A savings plan uses subtraction and division to turn a wish into a schedule.</div>"},
 "learn": [
  {"title": "Prime Factorization",
   "visual": FACTOR,
   "html": "<p>Every composite number can be broken into prime factors. Start with any factor pair and keep splitting until every branch ends in a prime. No matter how you start, you always end with the same primes.</p><div class='example'>36 = 4 × 9 = (2 × 2) × (3 × 3). Written with exponents: 36 = 2² × 3².</div>",
   "checks": [
    {"t":"text","q":"Is 51 prime or composite? Type the word, then give a factor pair to prove it.","a":[{"all":[["composite"],["3","17"]]}],"show":"composite (3 × 17 = 51)","pts":3,"why":"5 + 1 = 6, which is divisible by 3, so 51 = 3 × 17. Many people guess 51 is prime."},
    {"t":"blanks","q":"Complete the prime factorization of 60.","sent":"60 = 2 × ___ × ___ × 5","blanks":[["2"],["3"]],"show":"60 = 2 × 2 × 3 × 5","pts":3,"why":"60 = 6 × 10 = (2 × 3) × (2 × 5) = 2 × 2 × 3 × 5."},
    {"t":"num","q":"What number has the prime factorization 2 × 3 × 3 × 7?","a":126,"pts":2,"why":"2 × 3 = 6, × 3 = 18, × 7 = 126."},
    {"t":"open","key":"sameprimes","q":"Jalen made a factor tree for 48 starting with 6 × 8. Priya started with 4 × 12. Will they end with the same primes? Explain why.","min":15,"rows":2,"rubric":["Yes","Every number has only one prime factorization, no matter how you start"],"model":"Yes. Both trees end with 2 × 2 × 2 × 2 × 3, because every whole number has exactly one set of prime factors. Only the order of splitting changes."}]},
  {"title": "Greatest Common Factor (GCF)",
   "visual": VENN,
   "html": "<p><b>Method 1: list factors.</b> Factors of 36: 1, 2, 3, 4, 6, 9, 12, 18, 36. Factors of 48: 1, 2, 3, 4, 6, 8, 12, 16, 24, 48. The greatest one they share is <b>12</b>.</p><p><b>Method 2: shared primes.</b> Put the prime factors in a Venn diagram. Multiply the primes in the middle: 2 × 2 × 3 = 12.</p><p>So Amara can make <b>12 bags</b>, each with 36 ÷ 12 = 3 muffins and 48 ÷ 12 = 4 cookies.</p>",
   "checks": [
    {"t":"num","q":"What is the GCF of 24 and 40?","a":8,"pts":2,"why":"24 = 2 × 2 × 2 × 3 and 40 = 2 × 2 × 2 × 5. Shared: 2 × 2 × 2 = 8."},
    {"t":"num","q":"A homeschool co-op has 54 pencils and 72 erasers. They want identical supply kits with nothing left over. What is the greatest number of kits?","a":18,"unit":"kits","pts":3,"why":"GCF of 54 and 72 is 18."},
    {"t":"blanks","q":"How many pencils and erasers go in each of those kits?","sent":"___ pencils and ___ erasers","blanks":[["3","three"],["4","four"]],"pts":3,"why":"54 ÷ 18 = 3 pencils; 72 ÷ 18 = 4 erasers."},
    {"t":"num","q":"Use the distributive property and the GCF to rewrite 36 + 48 as 12 × (3 + ___). What goes in the blank?","a":4,"pts":2,"why":"36 + 48 = 12 × 3 + 12 × 4 = 12 × (3 + 4) = 84."}]},
  {"title": "Least Common Multiple (LCM)",
   "html": "<p>Hot dogs come in packs of 10. Buns come in packs of 8. What is the fewest of each you can buy to have exactly the same number of hot dogs and buns?</p><p>Multiples of 10: 10, 20, 30, <b>40</b>, 50... Multiples of 8: 8, 16, 24, 32, <b>40</b>... The LCM is <b>40</b>: 4 packs of hot dogs and 5 packs of buns.</p><p><b>Shared-prime method:</b> 10 = 2 × 5 and 8 = 2 × 2 × 2. Use every prime the greatest number of times it appears in either number: 2 × 2 × 2 × 5 = 40.</p><div class='callout'><b>GCF or LCM?</b> Splitting into the largest equal groups: GCF. Finding when events happen together again, or the smallest amount that works for both: LCM.</div>",
   "checks": [
    {"t":"num","q":"What is the LCM of 6 and 9?","a":18,"pts":2,"why":"Multiples of 9: 9, 18. 18 is also a multiple of 6."},
    {"t":"num","q":"Kwame waters the garden-center ferns every 4 days and the orchids every 6 days. He watered both today. In how many days will he water both on the same day again?","a":12,"unit":"days","pts":3,"why":"LCM of 4 and 6 is 12."},
    {"t":"num","q":"One bus leaves the station every 15 minutes and another every 20 minutes. Both leave at 8:00 AM. How many minutes until they leave together again?","a":60,"unit":"minutes","pts":3,"why":"LCM of 15 and 20 is 60, so 9:00 AM."},
    {"t":"open","key":"gcforlcm","q":"For each situation, decide GCF or LCM and explain how you knew: (a) cutting a 24-inch and a 36-inch ribbon into equal pieces as long as possible; (b) two lighthouses flash every 8 and 12 seconds, and you want to know when they flash together.","min":25,"rows":3,"rubric":["(a) GCF, because it splits into the largest equal pieces (12 inches)","(b) LCM, because it finds when events line up (24 seconds)"],"model":"(a) GCF, because I am splitting both ribbons into the longest equal pieces; the GCF of 24 and 36 is 12 inches. (b) LCM, because I want the first time both flashes happen together; the LCM of 8 and 12 is 24 seconds."}]},
  {"title": "Planning a Savings Goal",
   "visual": savings(),
   "html": "<p>A <b>savings goal</b> needs three things: <b>what</b> you are saving for, <b>how much</b> it costs, and <b>when</b> you want it. Then work backward.</p><div class='example'>Amara needs $189.50 and has $42.00. Amount left: 189.50 − 42.00 = $147.50. She can save $18.50 a week from her bread sales. Weeks needed: 147.50 ÷ 18.50 = 7.97..., so she needs <b>8 weeks</b> (7 weeks would leave her short).</div><p>Notice that a partial week rounds <b>up</b>, because you cannot buy the mixer until you have all the money.</p>",
   "checks": [
    {"t":"num","q":"How much more money does Amara need?","a":147.5,"unit":"dollars","show":"$147.50","pts":2,"why":"189.50 − 42.00 = $147.50."},
    {"t":"num","q":"After 7 weeks of saving $18.50, how much will Amara have in total?","a":171.5,"unit":"dollars","show":"$171.50","pts":3,"why":"42.00 + 7 × 18.50 = 42.00 + 129.50 = $171.50, still short of $189.50."},
    {"t":"num","q":"Amara wants the mixer in 5 weeks instead. How much must she save each week, to the nearest cent?","a":29.5,"tol":0.001,"unit":"dollars","show":"$29.50","pts":3,"why":"147.50 ÷ 5 = $29.50 a week."},
    {"t":"open","key":"goalplan","q":"Kwame earns $15.75 an hour and works 10 hours a week. He wants a $350.00 used bike in 6 weeks and has $65.00 saved. Can he do it if he saves 0.3 of each paycheck (30 cents of every dollar)? Show your work and explain.","min":30,"rows":4,"rubric":["Weekly pay $157.50","Saving 0.3 of pay is $47.25 a week","6 weeks saves $283.50; with $65 = $348.50, $1.50 short","Clear conclusion with a suggestion"],"model":"His weekly pay is 15.75 × 10 = $157.50. Saving 0.3 of it is 0.3 × 157.50 = $47.25 a week. In 6 weeks that is $283.50, plus his $65.00 makes $348.50. He would be $1.50 short, so he should save a little more one week or wait one more week."}]}],
 "handson": {
  "title": "Make Your Own Savings Goal Plan",
  "intro": "Choose something real you want, and build a plan your family can check.",
  "materials": ["A real item you want (from a store website or flyer, with its price)", "Paper or a notebook for a savings chart", "Colored pencils", "A jar or envelope labeled with your goal (optional)"],
  "steps": [
   "Write your goal: the item, its price (add sales tax if it is not food) and the date you want it.",
   "Write how much you have now and how you will earn or save money each week (chores, allowance, a small business).",
   "Calculate the amount left and the number of weeks needed. Round partial weeks up.",
   "Draw a bar chart like Amara's with your weekly totals and a goal line.",
   "Share the plan with a parent and agree on a check-in day each week."],
  "record": [
   {"t":"open","key":"mygoal","q":"Write your goal, price, current savings, weekly amount and the number of weeks needed. Show all calculations.","min":30,"rows":5,"rubric":["States item, price and date","Correct amount left","Correct weeks, rounded up","Shows calculations"],"model":"Goal: a $64.99 telescope plus 7% tax = $69.54, by March 1. I have $15.00, so I need $54.54 more. I can save $8.00 a week from chores. 54.54 ÷ 8 = 6.8, so I need 7 weeks."},
   {"t":"open","key":"mygoal2","q":"What could make your plan go faster or slower? Name one risk and one way to stay on track.","min":20,"rows":3,"rubric":["A realistic risk","A realistic strategy"],"model":"If I spend some of my chore money on snacks, the plan will take longer. To stay on track, I will put my savings in the envelope the same day I get paid."}]},
 "think": {
  "intro": "Explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"gcflcmrel","q":"For 12 and 18, find the GCF and the LCM. Then multiply GCF × LCM and compare it with 12 × 18. Try one more pair of your own. What do you notice, and why might it be true?","min":45,"rubric":["GCF 6 and LCM 36","Notices GCF × LCM = product of the numbers (216)","Tests another pair correctly","Gives a reason using shared primes"],"model":"GCF(12, 18) = 6 and LCM = 36. 6 × 36 = 216 and 12 × 18 = 216, the same. With 8 and 10: GCF 2, LCM 40, 2 × 40 = 80 = 8 × 10. It works because the GCF holds the shared primes once and the LCM holds every prime, so together they use every prime from both numbers exactly as many times as the two numbers do."}]},
 "checkpoint": {
  "title": "Unit 1 Checkpoint: Number Power",
  "intro": "This checkpoint covers Weeks 1 to 5. Work each problem on paper, then type your answer. No calculator. Mastery is 85 or higher. If you score below 85, your teacher will review with you, then you will retake it.",
  "parts": [
   {"title": "Part A: Whole numbers and long division", "items": [
    {"t":"num","q":"6,384 ÷ 24 = ?","a":266,"pts":3,"why":"24 × 266 = 6,384."},
    {"t":"num","q":"A school orders 1,250 books packed 32 to a box. How many boxes are needed?","a":40,"unit":"boxes","pts":3,"why":"1,250 ÷ 32 = 39 R2. The 2 extra books need one more box: 40."}]},
   {"title": "Part B: Adding, subtracting and multiplying decimals", "items": [
    {"t":"num","q":"14.3 − 6.78 = ?","a":7.52,"pts":3,"why":"14.30 − 6.78 = 7.52."},
    {"t":"num","q":"A receipt shows $3.49, $12.05 and $0.89. What is the total?","a":16.43,"unit":"dollars","show":"$16.43","pts":3,"why":"3.49 + 12.05 + 0.89 = $16.43."},
    {"t":"num","q":"0.06 × 4.5 = ?","a":0.27,"pts":3,"why":"6 × 45 = 270, with 3 decimal places: 0.270 = 0.27."},
    {"t":"num","q":"Gas costs $3.289 per gallon. What do 11.5 gallons cost, to the nearest cent?","a":37.82,"tol":0.001,"unit":"dollars","show":"$37.82","pts":3,"why":"3.289 × 11.5 = 37.8235, which rounds to $37.82."}]},
   {"title": "Part C: Dividing decimals and unit prices", "items": [
    {"t":"num","q":"9.36 ÷ 0.4 = ?","a":23.4,"pts":3,"why":"Multiply both by 10: 93.6 ÷ 4 = 23.4."},
    {"t":"num","q":"A 3-pound bag of apples costs $4.47 and a 5-pound bag costs $6.95. What is the unit price of the better buy, per pound?","a":1.39,"tol":0.001,"unit":"dollars per lb","show":"$1.39 per pound","pts":3,"why":"4.47 ÷ 3 = $1.49 and 6.95 ÷ 5 = $1.39. The 5-pound bag is the better buy at $1.39 per pound."}]},
   {"title": "Part D: Factors, multiples and money", "items": [
    {"t":"num","q":"What is the GCF of 42 and 70?","a":14,"pts":3,"why":"42 = 2 × 3 × 7, 70 = 2 × 5 × 7. Shared: 2 × 7 = 14."},
    {"t":"num","q":"Juice boxes come in packs of 6 and snack bars in packs of 9. What is the fewest juice boxes you can buy to have the same number of each?","a":18,"unit":"juice boxes","pts":3,"why":"LCM of 6 and 9 is 18."},
    {"t":"num","q":"Maya earns $16.25 an hour and works 8 hours. She saves 0.25 of her pay (25 cents of every dollar). How much does she save?","a":32.5,"unit":"dollars","show":"$32.50","pts":3,"why":"16.25 × 8 = $130.00. 0.25 × 130 = $32.50."},
    {"t":"open","key":"cp_explain","q":"Andre says 4.8 ÷ 0.06 = 8. Find his mistake, give the correct answer, and show how to check it.","min":25,"rows":3,"rubric":["Correct answer 80","Explains he did not move both decimal points the same number of places","Checks by multiplying 0.06 × 80 = 4.8"],"model":"He moved the decimal point two places in 0.06 but only one place in 4.8, so he divided 48 by 6. Both must move two places: 480 ÷ 6 = 80. Check: 0.06 × 80 = 4.80."}]}]},
 "next": "Unit 2: Fractions and Ratios begins with multiplying fractions, and the money thread turns to percents of savings and simple interest."
}

TEACHER = {
 "standards": [
  "MA.6.NSO.3.1: Given a mathematical or real-world context, find the greatest common factor and least common multiple of two whole numbers.",
  "MA.6.NSO.3.2: Rewrite the sum of two composite whole numbers having a common factor, as a common factor multiplied by the sum of two whole numbers.",
  "MA.6.NSO.3.3: Evaluate positive rational numbers and integers with natural number exponents (prime factorization with exponents, preview).",
  "MA.6.NSO.2.1: Multiply and divide positive multi-digit numbers with decimals to the thousandths, including using a standard algorithm with procedural fluency (checkpoint).",
  "Financial literacy: setting and planning savings goals (Jump$tart Spending and Saving)."],
 "materials": ["The interactive lesson", "Counters, beans or coins (36 of one kind and 48 of another) for the bag-packing model", "Paper for factor trees", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 4 Reconnect questions."],
  [4, "Hook", "Have the student physically sort 36 and 48 counters into identical groups. Ask for the greatest number of groups."],
  [10, "Prime factorization", "Build factor trees for 36 and 48 two different ways to show the primes are the same."],
  [10, "GCF", "Find the GCF by listing factors, then with the Venn diagram. Connect to the counters."],
  [10, "LCM", "Hot dogs and buns. Practice deciding GCF or LCM with the ribbon and lighthouse problems."],
  [10, "Savings goal", "Work Amara's mixer plan. Stress rounding weeks up. Start the student's own savings plan."],
  [10, "Checkpoint preview", "Explain that the checkpoint is completed after class, independently, without a calculator. Mastery is 85; below 85 means a review lesson and a retake."]],
 "key_questions": ["Are we splitting into groups or waiting for things to line up?", "How do you know a number is prime?", "Why do we round the number of weeks up?", "What would change your savings plan?"],
 "misconceptions": ["Confusing GCF and LCM, or always multiplying the two numbers to get the LCM.", "Thinking 1 is prime, or that odd numbers like 51 and 91 are prime.", "Rounding a partial week down in a savings plan.", "Stopping a factor tree before every branch is prime."],
 "support": ["Provide a hundreds chart with primes shaded.", "Use counters for GCF problems before moving to numbers.", "Let the student list multiples in two rows to find the LCM."],
 "challenge": ["Find the GCF and LCM of three numbers: 12, 18 and 30 (GCF 6, LCM 180).", "Plan a family savings goal that includes sales tax and a deadline."],
 "background": "<p>The checkpoint covers MA.6.NSO.2.1 and MA.6.NSO.3.1. Score it with the engine; the one written item is scored with its rubric. A student below 85 gets a targeted review lesson on the parts missed (A to D), then retakes the checkpoint. Record checkpoint scores in the student's Weekly Score Log.</p>",
 "sources": ["CPALMS: MA.6.NSO.3.1 and MA.6.NSO.3.2.", "Jump$tart Coalition National Standards for Personal Financial Education: Saving."]
}

PRINT = {
 "directions": "Show your work. No calculator.",
 "items": [
  {"q":"Make a factor tree and write the prime factorization of 84.","a":"84 = 2 × 2 × 3 × 7","lines":3},
  {"q":"Find the GCF and LCM of 18 and 24.","a":"GCF 6; LCM 72","lines":2},
  {"q":"A teacher has 30 red beads and 45 blue beads. What is the greatest number of identical bracelets she can make with no beads left over? How many of each color go on each bracelet?","a":"15 bracelets; 2 red and 3 blue on each","lines":3},
  {"q":"One light blinks every 6 seconds and another every 10 seconds. They blink together now. When will they blink together next?","a":"In 30 seconds (LCM of 6 and 10)","lines":2},
  {"q":"Rewrite 24 + 40 using the GCF and the distributive property.","a":"8 × (3 + 5)","lines":1},
  {"q":"You want a $95.00 tablet case. You have $20.00 and save $12.50 a week. How many weeks until you can buy it? Explain your rounding.","a":"75 ÷ 12.50 = 6 weeks exactly (if it were not exact, round up).","lines":3}]
}
