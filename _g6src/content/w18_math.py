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
  "Track a loan and a credit card balance below zero, and explain how debt and interest work."],
 "vocab": [
  ["zero pair", "A positive and a negative of the same size, such as 1 and −1, that add to zero."],
  ["additive inverse", "A number's opposite; a number plus its additive inverse equals 0."],
  ["sum", "The result of adding."],
  ["difference", "The result of subtracting."],
  ["debt", "Money you owe; it can be shown as a negative balance."],
  ["credit", "Trust that lets you borrow now and pay later."],
  ["interest", "Extra money charged for borrowing, added to a debt over time."]],
 "reconnect": {
  "title": "Week 17: The coordinate plane",
  "intro": "Last week you found distances on the grid with absolute value. Those distances are differences between integers, today's topic.",
  "items": [
   {"t":"text","q":"Which quadrant is (−3, −8) in? Type the Roman numeral.","a":[{"all":[["iii","3"]],"none":["iv"]}],"show":"III","pts":2,"why":"Both coordinates are negative."},
   {"t":"num","q":"How many units apart are (−4, 6) and (5, 6)?","a":9,"unit":"units","pts":2,"why":"|−4| + |5| = 9."},
   {"t":"text","q":"Reflect (2, −9) across the x-axis. Type the ordered pair.","a":["(2, 9)","(2,9)","2, 9"],"show":"(2, 9)","pts":2,"why":"Across the x-axis, y changes sign."},
   {"t":"open","key":"rc_distance","q":"Last week, to find the distance from −4 to 5 you added 4 + 5. Explain in your own words why you added instead of subtracted.","min":15,"rows":2,"rubric":["The numbers are on opposite sides of zero, so you travel 4 to reach zero, then 5 more"],"model":"−4 and 5 are on opposite sides of zero. You go 4 units to reach zero, then 5 more, so you add 4 + 5 = 9."}]},
 "hook": {
  "title": "The Coldest Morning",
  "html": "<p>From January 14 to 15, 1972, the temperature in Loma, Montana, rose from −54°F to 49°F in 24 hours, the biggest one-day temperature change ever recorded in the United States. How many degrees is that? You can't just subtract 54 from 49.</p><p>Meanwhile, Maya, the 12-year-old sourdough baker from last week, wants to borrow $60 for a stand mixer. How do you keep track of money you owe? Both questions need the same skill: adding and subtracting integers.</p><div class='callout'><b>Big question:</b> What happens when positive and negative quantities combine?</div>"},
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
   "html": "<p>On a number line, start at the first number. Adding a positive number moves <b>right</b>; adding a negative number moves <b>left</b>. For 3 + (−7), start at 3 and move 7 to the left: you land on −4.</p><p>You can add several integers in any order. Group the positives and the negatives: 6 + (−4) + 9 + (−8) = (6 + 9) + ((−4) + (−8)) = 15 + (−12) = 3.</p>",
   "checks": [
    {"t":"num","q":"A cave diver at Ginnie Springs is at −30 feet and rises 12 feet. What is the diver's new position relative to the surface, as an integer? (Write −30 + 12.)","a":-18,"unit":"feet","pts":2,"why":"Start at −30 and move 12 toward zero."},
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
  {"title": "Money: Debt and Credit, Going Below Zero",
   "html": "<p>When you borrow money, your balance goes <b>below zero</b>: you have a <b>debt</b>. Maya wants a $60 stand mixer for her bakery. Her parents lend her the money, and she agrees to repay $15 each Saturday.</p><div class='card' style='font-family:Courier New,monospace;font-size:14px'>Start &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; borrow for mixer &nbsp;&nbsp; −$60<br>Sat 1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; repay &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; +$15 &nbsp;&nbsp; balance −$45<br>Sat 2 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; repay &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; +$15 &nbsp;&nbsp; balance −$30</div><p>A <b>credit card</b> works the same way: each purchase adds debt (a negative amount), and each payment brings the balance back toward zero. But a credit card company charges <b>interest</b> on debt you don't pay off each month, so the debt can grow even if you buy nothing more. Many cards charge more than 20 percent a year.</p><p><b>Credit</b> means a lender trusts you to pay back later. Paying on time builds a good credit history; missing payments makes borrowing harder and more expensive.</p>",
   "checks": [
    {"t":"num","q":"After Saturday 2, Maya's balance is −$30. What is her balance after two more $15 payments?","a":0,"unit":"dollars","pts":2,"why":"−30 + 15 + 15 = 0: the loan is paid off."},
    {"t":"num","q":"A credit card balance is −$120. The owner pays $50, then buys a $35 bike helmet. What is the new balance?","a":-105,"unit":"dollars","pts":2,"why":"−120 + 50 + (−35) = −105."},
    {"t":"num","q":"In January a card balance was −$240. In February it was −$95. What was the change in the balance? (February − January)","a":145,"unit":"dollars","pts":2,"why":"−95 − (−240) = −95 + 240 = 145: the debt shrank by $145."},
    {"t":"open","key":"interestwhy","q":"Two friends each owe $200 on credit cards that charge interest. One pays it off this month; the other pays only $10 a month. Explain, using what you know about negative balances, why the second friend could end up paying much more than $200.","min":30,"rows":3,"rubric":["Interest adds to the negative balance each month the debt remains","Small payments barely reduce it, so interest keeps being added for a long time"],"model":"Every month the debt stays, interest is added, making the balance more negative. Paying only $10 barely brings it toward zero, so interest keeps getting added for many months, and the total paid ends up much more than $200."}]}],
 "handson": {
  "title": "Counter Game and the Debt Walk",
  "intro": "Play an integer card game, then walk a loan and a credit card on a floor number line.",
  "materials": ["A deck of playing cards (remove face cards) or 20 index cards numbered 1 to 10 twice", "Two colors of counters (beans, coins or paper squares), about 20 of each", "Painter's tape or chalk number line from −20 to 20 (or paper)", "A family member", "Paper and pencil"],
  "steps": [
   "Integer card game: black cards are positive, red cards are negative. Each player draws 2 cards and adds them. The greater sum wins the round. Model each sum with counters at least three times, removing zero pairs.",
   "Subtraction round: draw 2 cards and subtract the second from the first (first − second). Rewrite each as adding the opposite before calculating.",
   "Debt walk: make a number line from −20 to 20 on the floor. Start at 0. A family member reads a list for a pretend credit card (each step is $1): −12 (art supplies), −6 (a book), +10 (payment), −8 (a game), −3 (interest), +15 (payment). Walk each one and say your balance.",
   "Write your own 6-step list for borrowing and repaying money for something you would like to buy, and walk it."],
  "record": [
   {"t":"open","key":"cardrec","q":"Write three addition and two subtraction problems from your card game, with answers. For one subtraction, show how you rewrote it as adding the opposite.","min":30,"rows":4,"rubric":["Five problems with correct answers","One subtraction rewritten correctly as adding the opposite"],"model":"Black 7 + red 9: 7 + (−9) = −2. Red 4 + red 6: −10. Black 8 + red 3: 5. Red 5 − black 2: −5 − 2 = −5 + (−2) = −7. Black 3 − red 8: 3 − (−8) = 3 + 8 = 11."},
   {"t":"open","key":"budgetrec","q":"What was the credit card's final balance? Then share your own borrowing-and-repaying list and its final balance.","min":30,"rows":4,"rubric":["Card balance: −4","Own list of six steps with a correct final balance","Says whether the debt is paid off"],"model":"Credit card: −12 − 6 + 10 − 8 − 3 + 15 = −4, so $4 is still owed. My list: borrow $18 for a skateboard (−18), pay +5, +5, borrow $4 for wheels (−4), pay +6, +6: final balance 0, paid off."}]},
 "think": {
  "intro": "Explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"temprule","q":"At 6 a.m. the temperature in Fairbanks, Alaska, was −23°F. By 2 p.m. it was −9°F, and by midnight it was −31°F. Find the change from 6 a.m. to 2 p.m. and from 2 p.m. to midnight, and the total change. Explain how you know whether each change is a rise or a drop.","min":51,"rows":5,"rubric":["6 a.m. to 2 p.m.: −9 − (−23) = 14 (rise)","2 p.m. to midnight: −31 − (−9) = −22 (drop)","Total: −31 − (−23) = −8 (or 14 + (−22) = −8)","The sign of the change shows rise (+) or drop (−)"],"model":"6 a.m. to 2 p.m.: −9 − (−23) = −9 + 23 = 14, a rise of 14 degrees. 2 p.m. to midnight: −31 − (−9) = −31 + 9 = −22, a drop of 22 degrees. Total: 14 + (−22) = −8, a drop of 8 degrees. A positive change means the temperature rose; a negative change means it dropped."},
   {"t":"open","key":"alwaysbigger","q":"Kai says, \"Subtracting always makes a number smaller.\" Is he right? Give an example that supports him and one that proves him wrong, and explain.","min":31,"rows":4,"rubric":["Supporting example: subtracting a positive (10 − 3 = 7)","Counterexample: subtracting a negative (5 − (−2) = 7)","Explains that subtracting a negative is adding a positive"],"model":"He's only sometimes right. 10 − 3 = 7 gets smaller. But 5 − (−2) = 5 + 2 = 7 gets bigger. Subtracting a negative is the same as adding a positive, so the result increases."}]},
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
  "Financial literacy: borrowing, debt, credit and interest (Jump$tart Managing Credit)."],
 "materials": ["The interactive lesson", "Playing cards or numbered index cards", "Two colors of counters (about 20 each)", "Tape or chalk number line from −20 to 20", "Paper and pencil", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 17 warm-up questions."],
  [4, "Hook", "Loma, Montana, and Maya's mixer loan."],
  [12, "Counters", "Model sums with zero pairs; derive the same-sign and different-sign rules."],
  [9, "Number line", "Model sums as moves; group positives and negatives."],
  [13, "Subtraction", "Add the opposite; the debt story; finding change; Kilimanjaro and Lake Assal."],
  [10, "Debt and credit", "Track Maya's loan and a credit card balance; discuss interest."],
  [6, "Assign", "Play two rounds of the card game; assign the budget walk, Think Deeper and the Exit Check."]],
 "key_questions": ["Are there more positives or more negatives?", "What is the opposite of the number being subtracted?", "Which way does this move on the number line?", "Is the change a rise or a drop?"],
 "misconceptions": ["Two negatives always make a positive (true for multiplying, not adding).", "Subtracting always makes a number smaller.", "−9 + 4 = −13 or 13 (adding absolute values with different signs).", "Change means start minus final."],
 "support": ["Keep counters available for every problem.", "Use a vertical number line (thermometer) for temperature problems.", "Color-code positive and negative numbers."],
 "challenge": ["Create a magic square where every row, column and diagonal of integers sums to −3.", "Find the record low and high temperatures for your county and compute the range."],
 "background": "<p>The Loma, Montana, record (January 14-15, 1972: −54°F to 49°F, a 103-degree rise in 24 hours) is listed by NOAA's National Centers for Environmental Information. Kilimanjaro is commonly given as 5,895 m (19,341 ft); Lake Assal's surface is about 155 m (509 ft) below sea level. Maya's loan and the card figures are practice data; typical U.S. credit card interest rates have been above 20 percent a year since 2023 (Federal Reserve G.19). The rules here are taught as summaries of counter and number-line models, not memorized first.</p>",
 "sources": ["NOAA National Centers for Environmental Information, State Climate Extremes.", "Florida Department of Education, B.E.S.T. Standards for Mathematics (2020).", "Jump$tart Coalition, National Standards for Personal Financial Education (2021).", "Federal Reserve, Consumer Credit G.19 release (credit card interest rates)."]
}

PRINT = {
 "directions": "Show your work.",
 "items": [
  {"q":"Find each sum: (a) −8 + (−9) (b) −13 + 5 (c) 21 + (−14)","a":"(a) −17 (b) −8 (c) 7","lines":2},
  {"q":"Find each difference: (a) 6 − 14 (b) −7 − 9 (c) −12 − (−20)","a":"(a) −8 (b) −16 (c) 8","lines":2},
  {"q":"A hiker starts at the shore of the Dead Sea, about 1,410 feet below sea level, and climbs to a lookout 200 feet above sea level. How many feet did she climb?","a":"200 − (−1,410) = 1,610 feet.","lines":2},
  {"q":"A temperature falls from 5°F to −12°F. What is the change?","a":"−12 − 5 = −17 degrees (a drop of 17).","lines":2},
  {"q":"A loan balance is −$85. The borrower pays $30, then borrows $12 more, then pays $40. What is the balance?","a":"−85 + 30 − 12 + 40 = −27; $27 is still owed.","lines":2},
  {"q":"Explain why subtracting a negative number gives a greater result.","a":"Subtracting a negative is adding its opposite (a positive), like canceling a debt.","lines":2}]
}
