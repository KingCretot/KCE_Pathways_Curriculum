def numline(lo, hi, marks, title, w=640):
    n = hi - lo; x0, x1 = 40, w - 40; step = (x1 - x0) / n
    X = lambda v: round(x0 + (v - lo) * step, 1)
    s = (f'<svg viewBox="0 0 {w} 150" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="{title}">'
         f'<text x="{w/2}" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">{title}</text>'
         f'<line x1="{x0-14}" y1="80" x2="{x1+14}" y2="80" stroke="#0A1F3D" stroke-width="2"/>'
         f'<path d="M{x0-20} 80 l8 -5 v10z M{x1+20} 80 l-8 -5 v10z" fill="#0A1F3D"/>')
    for v in range(lo, hi + 1):
        big = v % 5 == 0
        s += f'<line x1="{X(v)}" y1="{80-(7 if big else 4)}" x2="{X(v)}" y2="{80+(7 if big else 4)}" stroke="#0A1F3D"/>'
        if big or n <= 20:
            s += f'<text x="{X(v)}" y="102" text-anchor="middle" font-size="11" fill="{"#DB2F30" if v < 0 else "#0A1F3D"}" font-weight="{"bold" if v == 0 else "normal"}">{"−" + str(-v) if v < 0 else v}</text>'
    for v, lab, col in marks:
        s += f'<circle cx="{X(v)}" cy="80" r="6" fill="{col}"/><text x="{X(v)}" y="{56}" text-anchor="middle" font-size="11" font-weight="bold" fill="{col}">{lab}</text>'
    return s + f'<text x="{w/2}" y="138" text-anchor="middle" font-size="11" fill="#5b6676">Numbers to the left of zero are negative; numbers to the right are positive.</text></svg>'

ELEV = ('<svg viewBox="0 0 560 300" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Vertical number line of elevations above and below sea level">'
  '<text x="280" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Elevation: zero is sea level</text>'
  '<rect x="40" y="168" width="480" height="110" fill="#e6ecf3"/><text x="56" y="270" font-size="11" fill="#0047BA" font-style="italic">below sea level (negative)</text><text x="56" y="160" font-size="11" fill="#2c6e22" font-style="italic">above sea level (positive)</text>'
  '<line x1="260" y1="40" x2="260" y2="280" stroke="#0A1F3D" stroke-width="2"/>'
  + ''.join(f'<line x1="252" y1="{y}" x2="268" y2="{y}" stroke="#0A1F3D"/><text x="244" y="{y+4}" text-anchor="end" font-size="11" fill="{c}">{lab}</text>'
            for y, lab, c in [(48, "400 ft", "#0A1F3D"), (108, "200 ft", "#0A1F3D"), (168, "0 (sea level)", "#0A1F3D"), (228, "−200 ft", "#DB2F30"), (276, "−360 ft", "#DB2F30")]) +
  ''.join(f'<circle cx="260" cy="{y}" r="6" fill="{c}"/><path d="M266 {y} L300 {y}" stroke="{c}"/><text x="306" y="{y+4}" font-size="12" fill="{c}"><tspan font-weight="bold">{a}</tspan> {b}</text>'
          for y, a, b, c in [(65, "Britton Hill, Florida:", "345 ft", "#2c6e22"), (168, "Gulf beach at Venice:", "0 ft", "#0A1F3D"), (198, "a scuba diver in the Gulf:", "−100 ft", "#0047BA"), (253, "Death Valley, California (dry land):", "−282 ft", "#DB2F30")]) +
  '<text x="280" y="296" text-anchor="middle" font-size="10" fill="#5b6676">Drawn to scale along the line. Britton Hill is Florida\'s highest point; Death Valley is dry land below sea level.</text></svg>')

LESSON = {
 "unit": "Unit 4: Integers and the Coordinate Plane",
 "title": "Integers, Opposites and Absolute Value",
 "subtitle": "Temperatures below zero, places below sea level and bank balances below nothing all need numbers less than zero. Integers let us describe opposite directions, and absolute value tells us how far a number is from zero.",
 "objectives": [
  "Use positive and negative integers to describe quantities with opposite directions and explain what zero means in each situation.",
  "Plot, order and compare integers on horizontal and vertical number lines.",
  "Find the opposite of an integer and recognize that opposites are the same distance from zero.",
  "Interpret absolute value as distance from zero and compare absolute values in real situations.",
  "Track a bank balance with deposits and withdrawals, and explain what a negative balance means."],
 "vocab": [
  ["integer", "A whole number or its opposite: ..., −3, −2, −1, 0, 1, 2, 3, ..."],
  ["negative number", "A number less than zero, written with a minus sign, such as −8."],
  ["opposites", "Two numbers the same distance from zero on opposite sides, such as 6 and −6."],
  ["absolute value", "A number's distance from zero, written |−6| = 6. Distance is never negative."],
  ["deposit", "Money put into a bank account; it increases the balance."],
  ["withdrawal", "Money taken out of a bank account; it decreases the balance."],
  ["balance", "The amount of money in an account. A negative balance means you owe the bank money."]],
 "reconnect": {
  "title": "Unit 3: Rates and percents",
  "intro": "Integers are new, but you will still use the money skills from Unit 3. Warm up.",
  "items": [
   {"t":"num","q":"A $40 jacket is 15% off. What is the sale price?","a":34,"unit":"dollars","show":"$34","pts":2,"why":"Pay 85%: 0.85 × $40 = $34."},
   {"t":"num","q":"A 12-ounce bag of rice costs $3.60. What is the price per ounce?","a":0.30,"tol":0.001,"unit":"dollars","show":"$0.30","pts":2,"why":"$3.60 ÷ 12 = $0.30 per ounce, a unit rate from Unit 3."},
   {"t":"num","q":"A savings account pays 2% of the balance once a year. How much does $300 earn in a year?","a":6,"unit":"dollars","show":"$6","pts":2,"why":"0.02 × $300 = $6."},
   {"t":"open","key":"rc_check","q":"Name one way you checked whether an answer was reasonable in Unit 3.","min":10,"rows":2,"rubric":["A real strategy: compare with a benchmark (10%, 50%), ask whether the number should be bigger or smaller, estimate first"],"model":"I compared my answer with 10% or 50% to see whether it was in the right range, and I asked whether a converted number should get bigger or smaller."}]},
 "hook": {
  "title": "Below Zero",
  "visual": ELEV,
  "html": "<p>Florida's highest point, Britton Hill, is only 345 feet above sea level, the lowest high point of any state. Death Valley in California sinks 282 feet below sea level. On a cold January morning in Tallahassee the thermometer can drop below 32°F, and in Minneapolis it can fall below 0°F. And when someone spends more money than is in their bank account, the balance drops below zero.</p><p>Each of these needs numbers that measure in two directions from a starting point. Those are <b>negative numbers</b>, and together with zero and the positive whole numbers they make the <b>integers</b>.</p><div class='callout'><b>Big idea:</b> Zero is a starting point. Positive and negative numbers measure in opposite directions from it.</div>"},
 "learn": [
  {"title": "What Zero Means",
   "html": "<p>Every situation with negative numbers has a meaning for <b>zero</b>:</p><ul><li><b>Elevation:</b> zero is sea level; positive is above, negative is below.</li><li><b>Temperature:</b> zero is 0 degrees on the scale (on the Fahrenheit scale, 0°F is very cold but not \"no temperature\").</li><li><b>Money:</b> zero is an empty account; positive is money you have, negative is money you owe.</li><li><b>Football:</b> zero is where the play started; a gain of 6 yards is +6, a loss of 4 yards is −4.</li></ul><p>To write a situation as an integer, decide which direction is positive, then use a minus sign for the opposite direction.</p>",
   "checks": [
    {"t":"num","q":"A submarine is 120 feet below the surface of the ocean. Write its elevation as an integer.","a":-120,"unit":"feet","pts":2,"why":"Below sea level is negative: −120."},
    {"t":"num","q":"A quarterback is sacked for a loss of 9 yards. Write the change as an integer.","a":-9,"unit":"yards","pts":2,"why":"A loss is negative: −9."},
    {"t":"blanks","q":"Write each as an integer.","sent":"A deposit of $75: ___ &nbsp; 18 degrees below zero: ___ &nbsp; A hawk 200 feet above the ground: ___","blanks":[["^75"],["-18","−18"],["^200"]],"show":"75; −18; 200","pts":3,"why":"Deposits and heights above are positive; below zero is negative."},
    {"t":"open","key":"zero","q":"On the Fahrenheit scale, 0°F does not mean \"no heat at all.\" Explain why zero is just a starting point on a temperature scale.","min":20,"rows":2,"rubric":["Zero is a chosen reference point on the scale","Temperatures can go below 0°F (there is still some heat), so zero does not mean nothing"],"model":"Zero on the Fahrenheit scale is just where people decided to start counting. Temperatures can go below 0°F, so there is still heat there; zero is a reference point, not \"nothing.\""}]},
  {"title": "Ordering and Comparing Integers",
   "visual": numline(-10, 10, [(-7, "−7", "#DB2F30"), (-2, "−2", "#DB2F30"), (4, "4", "#0047BA")], "Comparing integers on a number line"),
   "html": "<p>On a horizontal number line, numbers increase from left to right. So any number to the right is greater. That means:</p><ul><li>Every positive number is greater than every negative number.</li><li>Among negative numbers, the one closer to zero is greater: −2 &gt; −7, because −2 is to the right of −7.</li></ul><p>On a vertical number line, like a thermometer or an elevation chart, numbers increase going up.</p><p>Use &lt; (is less than) and &gt; (is greater than). The small pointed end always points to the smaller number: −7 &lt; −2.</p>",
   "checks": [
    {"t":"blanks","q":"Type less or greater in each blank.","sent":"−9 is ___ than −3. &nbsp; 0 is ___ than −5. &nbsp; −1 is ___ than 1.","blanks":[[{"all":[["less","smaller"]],"none":["greater","not"]}],[{"all":[["greater","bigger","more"]],"none":["less","not"]}],[{"all":[["less","smaller"]],"none":["greater","not"]}]],"show":"less; greater; less","pts":3,"why":"−9 is left of −3; 0 is right of −5; −1 is left of 1."},
    {"t":"order","q":"Order these morning temperatures from coldest to warmest.","items":["−8°F (Minneapolis)","−3°F (Chicago)","0°F (Denver)","14°F (Boston)","41°F (Tallahassee)"],"pts":3,"why":"Coldest means least: −8 < −3 < 0 < 14 < 41."},
    {"t":"open","key":"colder","q":"Malia says −15°F is warmer than −5°F because 15 is bigger than 5. Explain her mistake using a thermometer or number line.","min":20,"rows":2,"rubric":["−15 is farther below zero, so it is colder (less)","On a thermometer, −15 is lower than −5"],"model":"On a thermometer, −15 is lower than −5 because it is farther below zero. Lower means colder, so −15°F is colder, even though 15 is a bigger number than 5."}]},
  {"title": "Opposites and Absolute Value",
   "html": "<p><b>Opposites</b> are the same distance from zero on opposite sides: 8 and −8 are opposites. The opposite of 0 is 0. A minus sign can be read \"the opposite of\": −(−8) is the opposite of −8, which is 8.</p><p><b>Absolute value</b> is a number's distance from zero, and distance is never negative. It is written with straight bars: |−8| = 8 and |8| = 8.</p><p>Absolute value is useful when only the size matters, not the direction. A diver at −30 feet and a hiker at 30 feet are the same distance from sea level. A balance of −$25 is a debt of $25.</p>",
   "checks": [
    {"t":"num","q":"What is |−23|?","a":23,"pts":2,"why":"−23 is 23 units from zero."},
    {"t":"num","q":"What is the opposite of −14?","a":14,"pts":2,"why":"14 is the same distance from zero on the other side."},
    {"t":"text","q":"A fish swims at −45 feet. A pelican flies at 38 feet. Which is farther from sea level? Type fish or pelican.","a":[{"all":[["fish"]],"none":["not fish","pelican is"]}],"show":"the fish (|−45| = 45 > 38)","pts":2,"why":"Compare absolute values: 45 > 38."},
    {"t":"open","key":"absneg","q":"Ravi says, \"The absolute value of a number is always positive.\" Is he exactly right? Explain, using the number 0.","min":20,"rows":2,"rubric":["Almost: absolute value is never negative","|0| = 0, which is neither positive nor negative"],"model":"Not exactly. Absolute value is never negative, but |0| = 0, and zero is neither positive nor negative. So it is more accurate to say absolute value is always positive or zero."}]},
  {"title": "Money: Bank Balances, Deposits and Withdrawals",
   "html": "<p>A bank account <b>balance</b> goes up with every <b>deposit</b> and down with every <b>withdrawal</b> or purchase. If you spend more than you have, the balance becomes negative. This is called an <b>overdraft</b>, and many banks charge an <b>overdraft fee</b>, often around $35, each time it happens, though some banks now charge less or nothing.</p><div class='card' style='font-family:Courier New,monospace;font-size:14px'>Date &nbsp;&nbsp; Description &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Amount &nbsp;&nbsp; Balance<br>Oct 1 &nbsp; Starting balance &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;$40<br>Oct 3 &nbsp; Lawn-mowing pay &nbsp;&nbsp;&nbsp; +$25 &nbsp;&nbsp;&nbsp;&nbsp; $65<br>Oct 6 &nbsp; Bike tire &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; −$30 &nbsp;&nbsp;&nbsp;&nbsp; $35<br>Oct 9 &nbsp; Concert ticket &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; −$50 &nbsp;&nbsp;&nbsp;&nbsp; −$15</div><p>A balance of −$15 means the account owner owes the bank $15 (plus any fee). The absolute value, $15, is the size of the debt.</p><p><b>To find a new balance</b> this week, start at the old balance on a number line and count left for money out or right for money in, crossing zero if needed. (In Week 18 you will learn to add and subtract integers directly.)</p>",
   "checks": [
    {"t":"num","q":"Starting with the −$15 balance, the account owner deposits $40 from babysitting. What is the new balance?","a":25,"unit":"dollars","show":"$25","pts":2,"why":"Owing $15 and adding $40 leaves $25."},
    {"t":"num","q":"A different account has $12. The owner buys a $30 game with a debit card. What is the balance now? Write a negative number if needed.","a":-18,"unit":"dollars","show":"−$18","pts":2,"why":"$12 − $30 = −$18: the owner is $18 below zero."},
    {"t":"text","q":"Which balance shows the bigger debt: −$42 or −$27? Type the balance.","a":[{"all":[["-42","^42","- 42"]],"none":["27 is","not 42"]}],"show":"−$42","pts":2,"why":"|−42| = 42 > 27, so it is the bigger debt, even though −42 is the smaller number."},
    {"t":"open","key":"overdraft","q":"A bank charges a $35 fee each time an account goes below zero. Why is it smart to track your balance before every purchase? Use the concert ticket example.","min":25,"rows":3,"rubric":["Going below zero triggers a fee, which makes the debt bigger","In the example, −$15 would become −$50 with a $35 fee; tracking first could have prevented it"],"model":"In the example, the ticket took the balance to −$15. With a $35 fee, the owner would owe $50, more than three times as much. Checking the balance before buying the ticket would have shown there wasn't enough money and saved the fee."}]}],
 "handson": {
  "title": "The Human Number Line",
  "intro": "Build a giant number line on the floor or sidewalk and move along it to feel how integers work.",
  "materials": ["Painter's tape, sidewalk chalk or 21 sticky notes", "A marker", "A family member", "Paper and pencil", "Optional: a thermometer (indoor/outdoor)"],
  "steps": [
   "Make a number line from −10 to 10 on the floor (tape) or a sidewalk (chalk), with about one foot between numbers. Mark 0 clearly.",
   "Stand on 0. A family member calls out a situation (\"a loss of 6 yards,\" \"a deposit of $4,\" \"3 degrees below zero\"). Walk to the integer and say it aloud.",
   "Opposites: two people stand on 7 and −7. Count steps to zero. What do you notice?",
   "Comparing: stand on two different negative numbers. The person on the right always has the greater number. Test it five times.",
   "Bank balance walk: start at 5 (dollars). Walk the transactions on a card: −8, +6, −9, +4. Record your balance after each one.",
   "Optional: check the real outdoor temperature and plot it.", "If you use chalk outdoors, choose a sidewalk or patio away from the street and driveway."],
  "record": [
   {"t":"num","q":"In the bank balance walk, you started at 5 and moved −8, +6, −9, +4. Where did you end?","a":-2,"pts":2,"why":"5 − 8 = −3; −3 + 6 = 3; 3 − 9 = −6; −6 + 4 = −2."},
   {"t":"open","key":"humanline","q":"Describe what you noticed about opposites when you counted steps to zero, and what you noticed when comparing two negative numbers. Use at least one example from your walk.","min":30,"rows":3,"rubric":["Opposites take the same number of steps to zero (same absolute value)","The person on the right (closer to zero, for negatives) has the greater number","A specific example"],"model":"When my mom stood on −7 and I stood on 7, we each took 7 steps to zero, so opposites have the same absolute value. When I stood on −2 and she stood on −6, I was on the right, so −2 was greater, even though 6 is bigger than 2."}]},
 "think": {
  "intro": "Explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"debt","q":"Two friends compare accounts. Jordan's balance is −$60. Kai's balance is $45. Kai says, \"Jordan has more money, because 60 is bigger.\" Explain who is better off and how much money Jordan would need to deposit to have the same balance as Kai.","min":60,"rows":5,"rubric":["Kai is better off: $45 > −$60 (Jordan owes money)","Jordan needs $60 to reach zero plus $45 more: $105","Uses absolute value or a number line correctly"],"model":"Kai is better off, because $45 is money he has, while −$60 means Jordan owes $60. Jordan would need $60 just to get back to zero, plus $45 more to match Kai, so he would need to deposit $105."},
   {"t":"open","key":"invent","q":"Invent a real-world situation (not money or temperature) where both positive and negative numbers make sense. Explain what zero means, give one positive and one negative example, and compare their absolute values.","min":60,"rows":5,"rubric":["A new, sensible situation","Clear meaning of zero","Correct positive and negative examples","Correct comparison of absolute values"],"model":"Golf scores compare strokes to \"par.\" Zero means you finished exactly at par. A score of +3 means 3 strokes over par, and −2 means 2 strokes under par, which is better. |+3| = 3 is greater than |−2| = 2, so the +3 score is farther from par."}]},
 "exit": [
  {"t":"num","q":"What is |−37|?","a":37,"pts":2,"why":"Distance from zero."},
  {"t":"blanks","q":"Type less or greater.","sent":"−12 is ___ than −20.","blanks":[[{"all":[["greater","bigger","more"]],"none":["less","not"]}]],"show":"greater","pts":2,"why":"−12 is closer to zero, to the right of −20."},
  {"t":"num","q":"A balance is $20. The owner spends $35. What is the new balance?","a":-15,"unit":"dollars","show":"−$15","pts":2,"why":"20 − 35 = −15."},
  {"t":"open","key":"exit_zero","q":"In a bank account, what does a balance of zero mean, and what does a negative balance mean?","min":10,"rows":2,"rubric":["Zero: no money in the account and nothing owed","Negative: the owner owes the bank money"],"model":"Zero means the account is empty and nothing is owed. A negative balance means the owner has spent more than they had and owes the bank money."}],
 "next": "Week 17: the four-quadrant coordinate plane, and mapping a business route."
}

TEACHER = {
 "standards": [
  "MA.6.NSO.1.1: Extend previous understanding of numbers to define rational numbers. Plot, order and compare rational numbers.",
  "MA.6.NSO.1.2: Given a mathematical or real-world context, represent quantities that have opposite direction using rational numbers. Compare them on a number line and explain the meaning of zero within its context.",
  "MA.6.NSO.1.3: Given a mathematical or real-world context, interpret the absolute value of a number as the distance from zero on a number line. Find the absolute value of rational numbers.",
  "MA.6.NSO.1.4: Solve mathematical and real-world problems involving absolute value, including the comparison of absolute value.",
  "Financial literacy: bank balances, deposits, withdrawals and overdraft fees (Jump$tart Saving and Spending)."],
 "materials": ["The interactive lesson", "Painter's tape or sidewalk chalk, a marker", "Paper and pencil", "Optional: a thermometer", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Unit 3 warm-up questions."],
  [5, "Hook", "Show the elevation chart. Ask where else numbers below zero appear."],
  [10, "What zero means", "Write integers for situations; discuss zero as a reference point."],
  [12, "Ordering and comparing", "Use the number line and a thermometer; fix Malia's mistake."],
  [10, "Opposites and absolute value", "Model distance from zero; compare a diver and a hiker."],
  [11, "Bank balances", "Walk through the account register; discuss overdraft fees."],
  [6, "Assign", "Tape the human number line together; assign the walks, Think Deeper and the Exit Check."]],
 "key_questions": ["What does zero mean here?", "Which direction is positive?", "Which number is farther from zero?", "Is a bigger absolute value always a bigger number?"],
 "misconceptions": ["−15 is greater than −5 because 15 > 5.", "Absolute value \"makes a number positive\" without meaning distance.", "Zero degrees means no temperature.", "A negative bank balance means the account is simply empty."],
 "support": ["Use a vertical thermometer drawing for comparisons.", "Color negative numbers red and positive numbers blue.", "Keep the human number line taped up all week."],
 "challenge": ["Research the lowest and highest points on each continent and order them.", "Find your bank's or a local credit union's real overdraft fee and compare it with $35."],
 "background": "<p>Britton Hill (345 feet) is the lowest state high point in the United States. Death Valley's Badwater Basin is about 282 feet below sea level. Overdraft fees vary; many large U.S. banks have historically charged about $35, though several have reduced or eliminated them since 2022. Grade 6 B.E.S.T. absolute-value work begins with integers and extends to all rational numbers (MA.6.NSO.1.3). Integer operations (MA.6.NSO.4.1 and 4.2) are taught in Weeks 18 and 19; this week's balance problems use movement on a number line only, as a preview.</p>",
 "sources": ["U.S. Geological Survey, Elevations and Distances in the United States.", "National Park Service, Death Valley: Badwater Basin.", "Consumer Financial Protection Bureau, Overdraft and NSF fees.", "CPALMS, MA.6.NSO.1 benchmarks."]
}

PRINT = {
 "directions": "Show your work or explain your thinking.",
 "items": [
  {"q":"Write an integer for each: a $60 deposit; 25 feet below sea level; a gain of 8 yards; 4 degrees below zero.","a":"60; −25; 8; −4.","lines":2},
  {"q":"Order from least to greatest: 3, −11, 0, −4, 7, −1.","a":"−11, −4, −1, 0, 3, 7.","lines":1},
  {"q":"Find |−19|, |6| and the opposite of −30.","a":"19; 6; 30.","lines":1},
  {"q":"A diver is at −52 feet and a bird is at 47 feet. Which is farther from sea level, and by how many feet?","a":"The diver, by 5 feet (52 vs. 47).","lines":2},
  {"q":"A balance of $18 has transactions of −$25, +$10 and −$7. Find the balance after each.","a":"−$7; $3; −$4.","lines":2},
  {"q":"Explain why −2 is greater than −9.","a":"−2 is closer to zero, to the right of −9 on the number line.","lines":2}]
}
