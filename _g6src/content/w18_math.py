def chips(pos, neg, title, w=520):
    s = [f'<svg viewBox="0 0 {w} 150" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="{title}">',
         f'<text x="{w/2}" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="14">{title}</text>']
    x = 30
    for i in range(pos):
        s.append(f'<circle cx="{x+i*34}" cy="60" r="14" fill="#C9A84C"/><text x="{x+i*34}" y="65" text-anchor="middle" font-weight="bold" font-size="16">+</text>')
    for i in range(neg):
        s.append(f'<circle cx="{x+i*34}" cy="104" r="14" fill="#DB2F30"/><text x="{x+i*34}" y="109" text-anchor="middle" font-weight="bold" font-size="18" fill="#fff">−</text>')
    z = min(pos, neg)
    if z:
        s.append(f'<rect x="{x-20}" y="40" width="{z*34+6}" height="86" rx="10" fill="none" stroke="#0047BA" stroke-width="2" stroke-dasharray="6 3"/>'
                 f'<text x="{x-14+z*17}" y="142" text-anchor="middle" font-size="11" fill="#0047BA">{z} zero pairs</text>')
    r = pos - neg
    s.append(f'<text x="{x+max(pos,neg)*34+10}" y="88" font-weight="bold" font-size="13" fill="#0A1F3D">Left over: {abs(r)} {"positive" if r>0 else "negative"}{"s" if abs(r)!=1 else ""} = {str(r).replace("-", "−")}</text>')
    s.append('</svg>')
    return "".join(s)

CHIPS = chips(5, 8, "5 + (−8): pair up positives and negatives")

def jump(start, moves, title, lo=-10, hi=10, w=640):
    pad = 30; u = (w - 2 * pad) / (hi - lo); X = lambda v: pad + (v - lo) * u
    s = [f'<svg viewBox="0 0 {w} 150" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="{title}">',
         f'<text x="{w/2}" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="14">{title}</text>',
         f'<line x1="{pad}" y1="110" x2="{w-pad}" y2="110" stroke="#0A1F3D" stroke-width="2"/>']
    for v in range(lo, hi + 1):
        s.append(f'<line x1="{X(v)}" y1="104" x2="{X(v)}" y2="116" stroke="#0A1F3D"/><text x="{X(v)}" y="132" text-anchor="middle" fill="{"#DB2F30" if v < 0 else "#0A1F3D"}">{str(v).replace("-", "−")}</text>')
    cur = start; y = 88
    s.append(f'<circle cx="{X(start)}" cy="110" r="6" fill="#0047BA"/>')
    for m in moves:
        nxt = cur + m; col = "#2c6e22" if m > 0 else "#DB2F30"
        s.append(f'<path d="M{X(cur)} 104 Q{(X(cur)+X(nxt))/2} {y-26} {X(nxt)} 104" fill="none" stroke="{col}" stroke-width="2.5"/>'
                 f'<text x="{(X(cur)+X(nxt))/2}" y="{y-28}" text-anchor="middle" font-weight="bold" fill="{col}">{"+" if m > 0 else "−"}{abs(m)}</text>')
        cur = nxt
    s.append(f'<circle cx="{X(cur)}" cy="110" r="7" fill="#C9A84C" stroke="#0A1F3D"/></svg>')
    return "".join(s)

JUMP = jump(3, [-7], "3 + (−7): start at 3, move 7 to the left")
SUBJ = jump(-2, [6], "−2 − (−6) is the same as −2 + 6: move 6 to the right")

LESSON = {
 "unit": "Unit 4: Integers and the Coordinate Plane",
 "title": "Adding and Subtracting Integers",
 "subtitle": "Last week you measured distances on the coordinate plane. Now you calculate with negative numbers directly: temperatures that drop, elevations that change, and a small business budget that has to balance.",
 "objectives": [
  "Model integer addition with counters (zero pairs) and on a number line.",
  "Add integers with the same sign and with different signs fluently, and explain the rules.",
  "Subtract integers by adding the opposite, and explain why it works.",
  "Find the change between two integers (temperature, elevation, balance) by subtracting.",
  "Track a small business's income and expenses as positive and negative integers to find profit or loss."],
 "vocab": [
  ["zero pair", "A positive and a negative of the same size, such as 1 and −1, that add to zero."],
  ["additive inverse", "A number's opposite; a number plus its additive inverse equals 0."],
  ["sum", "The result of adding."],
  ["difference", "The result of subtracting."],
  ["profit", "Money left after expenses when income is greater than expenses (a positive result)."],
  ["loss", "When expenses are greater than income (a negative result)."],
  ["expense", "Money a business spends, such as on supplies."]],
 "reconnect": {
  "title": "Week 17: The coordinate plane",
  "intro": "Last week you found distances on the grid with absolute value. Those distances are differences between integers, today's topic.",
  "items": [
   {"t":"text","q":"Which quadrant is (−3, −8) in? Type the Roman numeral.","a":[{"all":[["iii","3"]],"none":["iv"]}],"show":"III","pts":2,"why":"Both coordinates are negative."},
   {"t":"num","q":"How many units apart are (−4, 6) and (5, 6)?","a":9,"unit":"units","pts":2,"why":"|−4| + |5| = 9."},
   {"t":"text","q":"Reflect (2, −9) across the x-axis. Type the ordered pair.","a":[{"all":[["^2","(2"],["9"]],"none":["-9","-2","not"]}],"show":"(2, 9)","pts":2,"why":"Across the x-axis, y changes sign."},
   {"t":"open","key":"rc_distance","q":"Last week, to find the distance from −4 to 5 you added 4 + 5. Explain in your own words why you added instead of subtracted.","min":15,"rows":2,"rubric":["The numbers are on opposite sides of zero, so you travel 4 to reach zero, then 5 more"],"model":"−4 and 5 are on opposite sides of zero. You go 4 units to reach zero, then 5 more, so you add 4 + 5 = 9."}]},
 "hook": {
  "title": "The Coldest Morning",
  "html": "<p>On January 15, 1972, the temperature in Loma, Montana, rose from −54°F to 49°F in 24 hours, the biggest one-day temperature change ever recorded in the United States. How many degrees is that? You can't just subtract 54 from 49.</p><p>Meanwhile, Maya, the 12-year-old sourdough baker from last week, is reviewing her October: she earned money from sales, but spent money on flour, jars and gas. Did she make a profit or a loss? Both questions need the same skill: adding and subtracting integers.</p><div class='callout'><b>Big question:</b> What happens when positive and negative quantities combine?</div>"},
 "learn": [
  {"title": "Adding Integers with Counters",
   "visual": CHIPS,
   "html": "<p>Use yellow counters for +1 and red counters for −1. A yellow and a red together make a <b>zero pair</b>: +1 + (−1) = 0, like earning a dollar and spending a dollar.</p><p>To find 5 + (−8), lay out 5 yellow and 8 red counters. Remove the 5 zero pairs. Three red counters are left, so 5 + (−8) = −3.</p><ul><li><b>Same signs:</b> add the absolute values and keep the sign. −4 + (−6) = −10 (owing $4 and then owing $6 more means owing $10).</li><li><b>Different signs:</b> subtract the smaller absolute value from the larger, and keep the sign of the number with the larger absolute value. −9 + 4 = −5, because there are more negatives.</li></ul>",
   "checks": [
    {"t":"num","q":"−7 + (−5) = ?","a":-12,"pts":2,"why":"Same signs: 7 + 5 = 12, keep the negative sign."},
    {"t":"num","q":"−11 + 6 = ?","a":-5,"pts":2,"why":"Different signs: 11 − 6 = 5; there are more negatives."},
    {"t":"num","q":"14 + (−9) = ?","a":5,"pts":2,"why":"14 − 9 = 5; there are more positives."},
    {"t":"open","key":"zeropairwhy","q":"Explain, using zero pairs, why 8 + (−8) = 0. Then give a real-life example.","min":20,"rows":2,"rubric":["Each positive pairs with a negative; all 8 pairs make 0","A real example (earn $8, spend $8; climb 8 feet, descend 8 feet)"],"model":"8 yellow and 8 red counters make 8 zero pairs, and each pair is worth 0, so the sum is 0. If I earn $8 and then spend $8, I'm back where I started."}]},
  {"title": "Adding on a Number Line",
   "visual": JUMP,
   "html": "<p>On a number line, start at the first number. Adding a positive number moves <b>right</b>; adding a negative number moves <b>left</b>. For 3 + (−7), start at 3 and move 7 to the left: you land on −4.</p><p>You can add several integers in any order. Group the positives and the negatives: 6 + (−4) + 9 + (−8) = (6 + 9) + (−4 + −8) = 15 + (−12) = 3.</p>",
   "checks": [
    {"t":"num","q":"A scuba diver is at −30 feet and rises 12 feet. What is the new depth? (Write −30 + 12.)","a":-18,"unit":"feet","pts":2,"why":"Start at −30 and move 12 toward zero."},
    {"t":"num","q":"6 + (−4) + 9 + (−8) + (−5) = ?","a":-2,"pts":2,"why":"Positives 15; negatives −17; 15 + (−17) = −2."},
    {"t":"open","key":"orderproof","q":"Lena says −8 + 5 and 5 + (−8) have different answers because one starts negative. Is she right? Show both on a number line in words.","min":20,"rows":2,"rubric":["Both equal −3 (addition is commutative)","Describes both moves: start at −8 move 5 right; start at 5 move 8 left"],"model":"She's not right. Start at −8 and move 5 right: −3. Start at 5 and move 8 left: −3. Addition works in any order."}]},
  {"title": "Subtracting: Add the Opposite",
   "visual": SUBJ,
   "html": "<p>Subtracting a number is the same as adding its <b>opposite</b> (its additive inverse):</p><p style='font-size:17px;text-align:center'><b>a − b = a + (−b)</b></p><ul><li>9 − 13 = 9 + (−13) = −4</li><li>−5 − 7 = −5 + (−7) = −12</li><li>−2 − (−6) = −2 + 6 = 4</li></ul><p>Why does subtracting a negative make the answer bigger? Think of taking away a debt: if someone cancels $6 you owe, you are $6 better off. With counters, to take away 6 red counters from −2, you first add 6 zero pairs, then remove the 6 reds, leaving +4.</p><p><b>Finding change:</b> to find how much something changed, subtract: final − start. The Loma temperature change was 49 − (−54) = 49 + 54 = 103 degrees.</p>",
   "checks": [
    {"t":"num","q":"8 − 15 = ?","a":-7,"pts":2,"why":"8 + (−15) = −7."},
    {"t":"num","q":"−3 − (−10) = ?","a":7,"pts":2,"why":"−3 + 10 = 7."},
    {"t":"num","q":"The highest point in Africa, Mount Kilimanjaro in Tanzania, is about 19,341 feet above sea level. The shore of Lake Assal in Djibouti, Africa's lowest point, is about 509 feet below sea level. What is the difference in elevation?","a":19850,"tol":1,"unit":"feet","pts":2,"why":"19,341 − (−509) = 19,341 + 509 = 19,850 feet."},
    {"t":"open","key":"debtcancel","q":"Explain with a money story why 10 − (−4) = 14.","min":20,"rows":2,"rubric":["Subtracting a negative = removing a debt or loss","So the total goes up by 4"],"model":"I have $10 but also an IOU saying I owe my brother $4. If he tears up the IOU, a −4 is taken away, and I'm worth $14 now. Taking away a negative makes the total bigger."}]},
  {"title": "Money: Profit or Loss?",
   "html": "<p>Maya records income as positive and expenses as negative:</p><div class='card' style='font-family:Courier New,monospace;font-size:14px'>Week 1 &nbsp; bread sales &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+$72<br>Week 1 &nbsp; flour and salt &nbsp;&nbsp;&nbsp;−$18<br>Week 2 &nbsp; bread sales &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+$54<br>Week 2 &nbsp; new banneton baskets −$64<br>Week 3 &nbsp; gas for deliveries &nbsp;−$9<br>Week 3 &nbsp; bread sales &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+$45<br>Week 4 &nbsp; market stall fee &nbsp;&nbsp;&nbsp;−$25<br>Week 4 &nbsp; bread sales &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+$81</div><p>The sum of all the entries is her <b>profit</b> (if positive) or <b>loss</b> (if negative) for the month. Some months can show a loss because of a one-time purchase, like baskets she will use for years.</p>",
   "checks": [
    {"t":"num","q":"What is Maya's total for Week 2 alone (+$54 and −$64)?","a":-10,"unit":"dollars","pts":2,"why":"54 + (−64) = −10: a $10 loss that week."},
    {"t":"num","q":"What is Maya's profit or loss for the whole month? Use a negative number for a loss.","a":136,"unit":"dollars","pts":2,"why":"Income: 72 + 54 + 45 + 81 = 252. Expenses: 18 + 64 + 9 + 25 = 116. 252 + (−116) = 136."},
    {"t":"open","key":"weeklossok","q":"Maya was upset about her Week 2 loss. Explain to her why one week with a loss isn't necessarily bad for her business.","min":30,"rows":3,"rubric":["The baskets are a one-time purchase she'll use for many weeks (an investment)","The month overall shows a profit of $136"],"model":"The baskets cost a lot once, but she'll use them for years, so it's an investment, not a weekly cost. And the whole month still made a $136 profit, so the business is doing fine."}]}],
 "handson": {
  "title": "Counter Game and the Integer Budget Walk",
  "intro": "Play an integer card game, then walk a month of business transactions on a floor number line.",
  "materials": ["A deck of playing cards (remove face cards) or 20 index cards numbered 1 to 10 twice", "Two colors of counters (beans, coins or paper squares), about 20 of each", "Painter's tape or chalk number line from −20 to 20 (or paper)", "A family member", "Paper and pencil"],
  "steps": [
   "Integer card game: black cards are positive, red cards are negative. Each player draws 2 cards and adds them. The greater sum wins the round. Model each sum with counters at least three times, removing zero pairs.",
   "Subtraction round: draw 2 cards and subtract the second from the first (first − second). Rewrite each as adding the opposite before calculating.",
   "Budget walk: make a number line from −20 to 20 on the floor. Start at 0. A family member reads a transaction list for a lemonade stand: +12 (sales), −8 (lemons and sugar), −6 (cups), +15 (sales), −20 (a new cooler), +9 (sales). Walk each one and say your total.",
   "Write your own 6-transaction list for a real or imagined business you could run (pet sitting, crafts, yard work) and walk it."],
  "record": [
   {"t":"open","key":"cardrec","q":"Write three addition and two subtraction problems from your card game, with answers. For one subtraction, show how you rewrote it as adding the opposite.","min":30,"rows":4,"rubric":["Five problems with correct answers","One subtraction rewritten correctly as adding the opposite"],"model":"Black 7 + red 9: 7 + (−9) = −2. Red 4 + red 6: −10. Black 8 + red 3: 5. Red 5 − black 2: −5 − 2 = −5 + (−2) = −7. Black 3 − red 8: 3 − (−8) = 3 + 8 = 11."},
   {"t":"open","key":"budgetrec","q":"What was the lemonade stand's final total? Then share your own business transaction list and its profit or loss.","min":30,"rows":4,"rubric":["Lemonade total: 2","Own list of six transactions with a correct total","States profit or loss"],"model":"Lemonade stand: 12 − 8 − 6 + 15 − 20 + 9 = 2, a $2 profit. My pet-sitting list: +20, −5 (treats), +15, +20, −12 (leash), −3 (bags) = 35, a $35 profit."}]},
 "think": {
  "intro": "Explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"temprule","q":"At 6 a.m. the temperature in Fairbanks, Alaska, was −23°F. By 2 p.m. it was −9°F, and by midnight it was −31°F. Find the change from 6 a.m. to 2 p.m. and from 2 p.m. to midnight, and the total change. Explain how you know whether each change is a rise or a drop.","min":60,"rows":5,"rubric":["6 a.m. to 2 p.m.: −9 − (−23) = 14 (rise)","2 p.m. to midnight: −31 − (−9) = −22 (drop)","Total: −31 − (−23) = −8 (or 14 + (−22) = −8)","The sign of the change shows rise (+) or drop (−)"],"model":"6 a.m. to 2 p.m.: −9 − (−23) = −9 + 23 = 14, a rise of 14 degrees. 2 p.m. to midnight: −31 − (−9) = −31 + 9 = −22, a drop of 22 degrees. Total: 14 + (−22) = −8, a drop of 8 degrees. A positive change means the temperature rose; a negative change means it dropped."},
   {"t":"open","key":"alwaysbigger","q":"Kai says, \"Subtracting always makes a number smaller.\" Is he right? Give an example that supports him and one that proves him wrong, and explain.","min":50,"rows":4,"rubric":["Supporting example: subtracting a positive (10 − 3 = 7)","Counterexample: subtracting a negative (5 − (−2) = 7)","Explains that subtracting a negative is adding a positive"],"model":"He's only sometimes right. 10 − 3 = 7 gets smaller. But 5 − (−2) = 5 + 2 = 7 gets bigger. Subtracting a negative is the same as adding a positive, so the result increases."}]},
 "exit": [
  {"t":"num","q":"−15 + 8 = ?","a":-7,"pts":2,"why":"15 − 8 = 7; more negatives."},
  {"t":"num","q":"4 − 11 = ?","a":-7,"pts":2,"why":"4 + (−11) = −7."},
  {"t":"num","q":"−6 − (−6) = ?","a":0,"pts":2,"why":"−6 + 6 = 0, a zero pair."},
  {"t":"open","key":"exit_addopp","q":"Rewrite 7 − (−3) as an addition problem and solve it. Why does that work?","min":12,"rows":2,"rubric":["7 + 3 = 10","Subtracting a number equals adding its opposite"],"model":"7 + 3 = 10. Subtracting a number is the same as adding its opposite, and the opposite of −3 is 3."}],
 "next": "Week 19: multiplying and dividing integers."
}

TEACHER = {
 "standards": [
  "MA.6.NSO.4.1: Apply and extend previous understandings of operations with whole numbers to add and subtract integers with procedural fluency.",
  "MA.6.NSO.1.2: Given a mathematical or real-world context, represent quantities that have opposite direction using rational numbers. Compare them on a number line and explain the meaning of zero within its context.",
  "MA.K12.MTR.2.1: Demonstrate understanding by representing problems in multiple ways.",
  "Financial literacy: income, expenses, profit and loss (Jump$tart Earning Income; Spending and Saving)."],
 "materials": ["The interactive lesson", "Playing cards or numbered index cards", "Two colors of counters (about 20 each)", "Tape or chalk number line from −20 to 20", "Paper and pencil", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 17 warm-up questions."],
  [4, "Hook", "Loma, Montana, and Maya's October."],
  [12, "Counters", "Model sums with zero pairs; derive the same-sign and different-sign rules."],
  [9, "Number line", "Model sums as moves; group positives and negatives."],
  [13, "Subtraction", "Add the opposite; the debt story; finding change; Kilimanjaro and Lake Assal."],
  [10, "Profit or loss", "Total Maya's month; discuss one-time purchases."],
  [6, "Assign", "Play two rounds of the card game; assign the budget walk, Think Deeper and the Exit Check."]],
 "key_questions": ["Are there more positives or more negatives?", "What is the opposite of the number being subtracted?", "Which way does this move on the number line?", "Is the change a rise or a drop?"],
 "misconceptions": ["Two negatives always make a positive (true for multiplying, not adding).", "Subtracting always makes a number smaller.", "−9 + 4 = −13 or 13 (adding absolute values with different signs).", "Change means start minus final."],
 "support": ["Keep counters available for every problem.", "Use a vertical number line (thermometer) for temperature problems.", "Color-code positive and negative numbers."],
 "challenge": ["Create a magic square where every row, column and diagonal of integers sums to −3.", "Find the record low and high temperatures for your county and compute the range."],
 "background": "<p>The Loma, Montana, record (January 14-15, 1972: −54°F to 49°F, a 103-degree rise in 24 hours) is listed by NOAA's National Centers for Environmental Information. Kilimanjaro is commonly given as 5,895 m (19,341 ft); Lake Assal's surface is about 155 m (509 ft) below sea level. Maya's figures are practice data. The rules here are taught as summaries of counter and number-line models, not memorized first.</p>",
 "sources": ["NOAA National Centers for Environmental Information, State Climate Extremes.", "Florida Department of Education, B.E.S.T. Standards for Mathematics (2020).", "Jump$tart Coalition, National Standards for Personal Financial Education (2021)."]
}

PRINT = {
 "directions": "Show your work.",
 "items": [
  {"q":"Find each sum: (a) −8 + (−9) (b) −13 + 5 (c) 21 + (−14)","a":"(a) −17 (b) −8 (c) 7","lines":2},
  {"q":"Find each difference: (a) 6 − 14 (b) −7 − 9 (c) −12 − (−20)","a":"(a) −8 (b) −16 (c) 8","lines":2},
  {"q":"A hiker starts at 125 feet below sea level in Death Valley and climbs to 410 feet above sea level. How many feet did she climb?","a":"410 − (−125) = 535 feet.","lines":2},
  {"q":"A temperature falls from 5°F to −12°F. What is the change?","a":"−12 − 5 = −17 degrees (a drop of 17).","lines":2},
  {"q":"A craft business has: +$40, −$15, −$22, +$35, −$48. Find the profit or loss.","a":"75 − 85 = −10, a $10 loss.","lines":2},
  {"q":"Explain why subtracting a negative number gives a greater result.","a":"Subtracting a negative is adding its opposite (a positive), like canceling a debt.","lines":2}]
}
