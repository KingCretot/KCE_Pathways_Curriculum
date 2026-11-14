PV = '''<svg viewBox="0 0 540 150" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="14" role="img" aria-label="Place value chart for 47.385">
<text x="270" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Place value: 47.385</text>
<g text-anchor="middle">
<rect x="20" y="34" width="95" height="40" fill="#0A1F3D"/><text x="67" y="59" fill="#fff">Tens</text>
<rect x="115" y="34" width="95" height="40" fill="#0A1F3D"/><text x="162" y="59" fill="#fff">Ones</text>
<rect x="210" y="34" width="30" height="40" fill="#DB2F30"/><text x="225" y="59" fill="#fff">.</text>
<rect x="240" y="34" width="95" height="40" fill="#0047BA"/><text x="287" y="59" fill="#fff">Tenths</text>
<rect x="335" y="34" width="95" height="40" fill="#0047BA"/><text x="382" y="59" fill="#fff">Hundredths</text>
<rect x="430" y="34" width="95" height="40" fill="#0047BA"/><text x="477" y="59" fill="#fff">Thousandths</text>
<g font-size="30" font-family="Georgia"><text x="67" y="112">4</text><text x="162" y="112">7</text><text x="225" y="112" fill="#DB2F30">.</text><text x="287" y="112">3</text><text x="382" y="112">8</text><text x="477" y="112">5</text></g>
<g font-size="12" fill="#5b6676"><text x="67" y="138">40</text><text x="162" y="138">7</text><text x="287" y="138">0.3</text><text x="382" y="138">0.08</text><text x="477" y="138">0.005</text></g></g></svg>'''

RECEIPT = '''<svg viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg" font-family="Courier New, monospace" font-size="14" role="img" aria-label="Grocery receipt">
<rect x="10" y="5" width="280" height="290" fill="#fff" stroke="#999"/>
<text x="150" y="30" text-anchor="middle" font-weight="bold">FRESH MARKET</text><text x="150" y="48" text-anchor="middle" font-size="11">Lakeland, FL</text>
<text x="25" y="80">Bananas (3 lb)</text><text x="275" y="80" text-anchor="end">4.89</text>
<text x="25" y="102">Butter (2 lb)</text><text x="275" y="102" text-anchor="end">12.50</text>
<text x="25" y="124">Baking soda</text><text x="275" y="124" text-anchor="end">2.35</text>
<line x1="25" y1="136" x2="275" y2="136" stroke="#999" stroke-dasharray="4 3"/>
<text x="25" y="158">SUBTOTAL</text><text x="275" y="158" text-anchor="end">?</text>
<text x="25" y="180">TAX</text><text x="275" y="180" text-anchor="end">1.38</text>
<text x="25" y="204" font-weight="bold">TOTAL</text><text x="275" y="204" text-anchor="end" font-weight="bold">?</text>
<text x="25" y="236">CASH</text><text x="275" y="236" text-anchor="end">25.00</text>
<text x="25" y="258">CHANGE</text><text x="275" y="258" text-anchor="end">?</text>
<text x="150" y="284" text-anchor="middle" font-size="11">THANK YOU</text></svg>'''

LESSON = {
 "unit": "Unit 1: Number Power",
 "title": "Adding and Subtracting Decimals",
 "subtitle": "Every price tag, receipt and measurement you will ever read uses decimals.",
 "objectives": [
  "Read, compare and order decimals to the thousandths using place value.",
  "Add and subtract decimals by lining up place values and using zeros as placeholders.",
  "Estimate decimal sums and differences to check reasonableness.",
  "Check a receipt for accuracy and make correct change using the counting-up method."],
 "vocab": [
  ["decimal point", "The dot that separates the whole-number part of a number from the part less than one."],
  ["tenths", "The first place to the right of the decimal point. 0.3 is three tenths."],
  ["hundredths", "The second place to the right of the decimal point. 0.08 is eight hundredths. A cent is one hundredth of a dollar."],
  ["thousandths", "The third place to the right of the decimal point. 0.005 is five thousandths."],
  ["placeholder zero", "A zero written to keep digits in the correct place, such as writing 8.6 as 8.60 when adding to 12.75."],
  ["subtotal", "The total of the items before tax is added."],
  ["sales tax", "Money added to a purchase that goes to the government."],
  ["change", "The money returned when you pay more than the total."]],
 "reconnect": {
  "title": "Week 1: whole numbers, division and budgets",
  "intro": "Decimals follow the same place-value rules as whole numbers. First make sure last week's skills are solid.",
  "items": [
   {"t":"num","q":"4,128 ÷ 16 = ?","a":258,"pts":3,"why":"41 ÷ 16 = 2 R9, 92 ÷ 16 = 5 R12, 128 ÷ 16 = 8. Check: 16 × 258 = 4,128."},
   {"t":"num","q":"306 × 27 = ?","a":8262,"show":"8,262","pts":3,"why":"306 × 7 = 2,142 and 306 × 20 = 6,120. 2,142 + 6,120 = 8,262."},
   {"t":"num","q":"130 guests are coming to a co-op dinner. Each table seats 8. How many tables are needed?","a":17,"unit":"tables","pts":3,"why":"130 ÷ 8 = 16 R2. Sixteen tables leave 2 guests standing, so round up to 17."},
   {"t":"num","q":"A lawn-care business earned $520 in income and had $346 in expenses. What was its profit?","a":174,"unit":"dollars","show":"$174","pts":2,"why":"Profit = income − expenses = 520 − 346 = $174."},
   {"t":"num","q":"Estimate 6,290 ÷ 7 using compatible numbers. What is your estimate?","a":900,"pts":2,"why":"6,290 is close to 6,300, and 6,300 ÷ 7 = 900."},
   {"t":"blanks","q":"Vocabulary from Week 1.","sent":"In 72 ÷ 9 = 8, the number 9 is the ___ and 8 is the ___. A plan for money coming in and going out is a ___.","blanks":[["divisor"],["quotient"],["budget"]],"pts":3,"why":"Divisor, quotient, budget."}]},
 "hook": {
  "title": "The Receipt That Did Not Add Up",
  "html": "<p>Amara's banana bread business is growing, so this week she shops for supplies herself. At the checkout, the cashier hands her a receipt and her change. On the drive home, her mom asks, \"Did you check it?\"</p><p>Stores make mistakes: a price scans twice, a sale price does not ring up, a cashier counts change wrong. People who can work with decimals quickly catch those mistakes and keep their money.</p><div class='callout'><b>Big idea:</b> Decimals are place value continued to the right. If you line up the places, adding and subtracting decimals works exactly like whole numbers.</div>"},
 "learn": [
  {"title": "Decimal Place Value",
   "visual": PV,
   "html": "<p>Each place to the right of the decimal point is <b>ten times smaller</b> than the place to its left. In money, the tenths place is dimes and the hundredths place is cents.</p><div class='example'><b>Comparing decimals.</b> Which is greater, 0.6 or 0.58? Line them up: 0.60 and 0.58. Compare place by place from the left: 6 tenths is more than 5 tenths, so <b>0.6 is greater</b>, even though 58 looks bigger than 6.</div>",
   "checks": [
    {"t":"num","q":"In 47.385, what digit is in the <b>hundredths</b> place?","a":8,"pts":2,"why":"Tenths 3, hundredths 8, thousandths 5."},
    {"t":"text","q":"Which is greater: <b>0.7</b> or <b>0.69</b>? Type the number.","a":["0.7",".7","0.70"],"show":"0.7","pts":2,"why":"Write 0.70 and 0.69: 7 tenths beats 6 tenths."},
    {"t":"order","q":"Order from <b>least</b> to <b>greatest</b>.","items":["2.05","2.459","2.5","2.51"],"pts":3,"why":"Write each to the thousandths: 2.050, 2.459, 2.500, 2.510."},
    {"t":"text","q":"Write <b>three and forty-two thousandths</b> as a decimal.","a":["3.042"],"pts":3,"why":"Forty-two thousandths fills three places: 0.042. So the number is 3.042."}]},
  {"title": "Adding Decimals",
   "html": "<p>Line up the <b>decimal points</b> so each place is in the same column. Fill empty places with <b>placeholder zeros</b>. Then add like whole numbers and bring the decimal point straight down.</p><div class='example'><pre style='font-size:18px;margin:0'>  12.75\n+  8.60   (8.6 written as 8.60)\n-------\n  21.35</pre></div><p>Estimate to check: 13 + 9 = 22, so 21.35 is reasonable.</p>",
   "checks": [
    {"t":"num","q":"4.37 + 12.8 = ?","a":17.17,"pts":3,"why":"4.37 + 12.80 = 17.17. Estimate: 4 + 13 = 17."},
    {"t":"num","q":"0.95 + 3.408 + 7 = ?","a":11.358,"pts":3,"hint":"Write 7 as 7.000 and 0.95 as 0.950.","why":"0.950 + 3.408 + 7.000 = 11.358."},
    {"t":"num","q":"Amara buys 2.25 kg of flour, 0.75 kg of sugar and 1.5 kg of bananas. What is the total mass?","a":4.5,"unit":"kg","pts":3,"why":"2.25 + 0.75 = 3.00, and 3.00 + 1.50 = 4.50 kg."},
    {"t":"num","q":"Estimate first, then add: $19.99 + $4.89 + $0.65","a":25.53,"unit":"dollars","show":"$25.53","pts":3,"why":"Estimate 20 + 5 + 1 = 26. Exact: 19.99 + 4.89 = 24.88, plus 0.65 = $25.53."}]},
  {"title": "Subtracting Decimals",
   "html": "<p>Subtracting works the same way: line up the decimal points, add placeholder zeros, and regroup when you need to.</p><div class='example'><pre style='font-size:18px;margin:0'>  20.00   (20 written as 20.00)\n-  7.46\n-------\n  12.54</pre></div><p>Check by adding back: 12.54 + 7.46 = 20.00.</p>",
   "checks": [
    {"t":"num","q":"50 − 23.68 = ?","a":26.32,"pts":3,"why":"50.00 − 23.68 = 26.32. Check: 26.32 + 23.68 = 50."},
    {"t":"num","q":"8.3 − 2.755 = ?","a":5.545,"pts":3,"hint":"Write 8.3 as 8.300.","why":"8.300 − 2.755 = 5.545."},
    {"t":"num","q":"Tampa got 6.42 inches of rain in June and 4.9 inches in May. How many more inches fell in June?","a":1.52,"unit":"inches","pts":3,"why":"6.42 − 4.90 = 1.52 inches."},
    {"t":"num","q":"A runner's times were 58.47 seconds and 61.2 seconds. What is the difference?","a":2.73,"unit":"seconds","pts":3,"why":"61.20 − 58.47 = 2.73 seconds."}]},
  {"title": "Check the Receipt, Count the Change",
   "visual": RECEIPT,
   "html": "<p>Find the <b>subtotal</b> by adding the items. Add the <b>tax</b> to get the <b>total</b>. Subtract the total from the cash paid to get the <b>change</b>.</p><div class='example'><b>Counting up to make change.</b> Cashiers count up from the total to the amount paid. For a total of $21.12 paid with $25: start at $21.12, add 3 pennies to reach $21.15, add a dime to reach $21.25, add 3 quarters to reach $22.00, then add $3 to reach $25.00. The change is $0.03 + $0.10 + $0.75 + $3.00 = <b>$3.88</b>.</div>",
   "checks": [
    {"t":"num","q":"What is the subtotal on Amara's receipt?","a":19.74,"unit":"dollars","show":"$19.74","pts":3,"why":"4.89 + 12.50 + 2.35 = $19.74."},
    {"t":"num","q":"What is the total after tax?","a":21.12,"unit":"dollars","show":"$21.12","pts":3,"why":"19.74 + 1.38 = $21.12."},
    {"t":"num","q":"Amara paid with $25.00. How much change should she get?","a":3.88,"unit":"dollars","show":"$3.88","pts":3,"why":"25.00 − 21.12 = $3.88."},
    {"t":"num","q":"Later, Amara buys pans for $36.47 and pays with a $50 bill. What is her change?","a":13.53,"unit":"dollars","show":"$13.53","pts":3,"why":"50.00 − 36.47 = $13.53. Count up: 3¢ to $36.50, 50¢ to $37, $3 to $40, $10 to $50."}]}],
 "handson": {
  "title": "Open the KCE Store",
  "intro": "Run a pretend store at home and practice being the cashier. You will handle real coins and bills, which builds number sense that paper alone cannot.",
  "materials": ["Real coins and bills, or play money (cut paper bills work)", "5 household items with price tags you write, using cents (for example $3.79)", "A family member to be the customer", "Paper for receipts"],
  "steps": [
   "Price 5 items with decimal prices. At least two prices should end in amounts like .47 or .99.",
   "Your customer buys 2 or 3 items. Write a receipt: list the items, add them to find the subtotal, and add $0.50 tax for every $10 (or simply add $1.00 tax to keep it simple).",
   "Your customer pays with a bill larger than the total. Count up out loud to make change using coins and bills.",
   "Your customer checks your receipt and change with a calculator. Switch roles for one more transaction, and make one deliberate mistake on the receipt for them to catch.",
   "Complete at least three transactions."],
  "record": [
   {"t":"open","key":"store","q":"Write out two of your receipts (items, subtotal, tax, total, cash paid, change) and describe how you counted up the change.","min":40,"rows":6},
   {"t":"open","key":"mistake","q":"What mistake did you plant on a receipt, and did your customer catch it? What is the best way to catch receipt mistakes in real life?","min":25,"rows":3}]},
 "think": {
  "items": [
   {"t":"num","q":"Devon added 3.5 + 1.25 and got 1.60. What is the correct sum?","a":4.75,"pts":3,"why":"Lining up the decimal points: 3.50 + 1.25 = 4.75."},
   {"t":"open","key":"devon","q":"Explain Devon's mistake and how an estimate would have warned him.","min":25,"rubric":["Identifies that he lined up the last digits instead of the decimal points","Shows the correct alignment 3.50 + 1.25","Uses an estimate (about 3 + 1 = 4) to show 1.60 is impossible"]},
   {"t":"open","key":"younger","q":"Your younger cousin insists 0.45 is bigger than 0.5 because 45 is bigger than 5. Explain why they are wrong in a way a 9-year-old would understand. Use money or a drawing in words.","min":35,"rubric":["Uses place value or a money comparison (50 cents versus 45 cents)","Rewrites 0.5 as 0.50 to compare","Explanation is clear for a younger child"]}]},
 "exit": [
  {"t":"num","q":"In 6.209, what digit is in the thousandths place?","a":9,"pts":2,"why":"Tenths 2, hundredths 0, thousandths 9."},
  {"t":"num","q":"15.6 + 4.375 = ?","a":19.975,"pts":3,"why":"15.600 + 4.375 = 19.975."},
  {"t":"num","q":"30 − 12.84 = ?","a":17.16,"pts":3,"why":"30.00 − 12.84 = 17.16."},
  {"t":"num","q":"9.07 − 3.6 = ?","a":5.47,"pts":3,"why":"9.07 − 3.60 = 5.47."},
  {"t":"order","q":"Order from least to greatest.","items":["0.307","0.37","0.703","0.73"],"pts":3,"why":"0.307, 0.370, 0.703, 0.730."},
  {"t":"num","q":"A receipt shows $8.49, $3.75 and $11.20, plus $1.64 tax. What is the total?","a":25.08,"unit":"dollars","show":"$25.08","pts":3,"why":"8.49 + 3.75 + 11.20 = 23.44. 23.44 + 1.64 = $25.08."},
  {"t":"num","q":"You pay for that $25.08 total with $40. What is your change?","a":14.92,"unit":"dollars","show":"$14.92","pts":3,"why":"40.00 − 25.08 = $14.92."}],
 "next": "Week 3: multiplying decimals, using hourly pay and hours worked."
}

TEACHER = {
 "standards": [
  "MA.6.NSO.2.1: Multiply and divide positive multi-digit numbers with decimals to the thousandths (addition and subtraction fluency this week supports it).",
  "Review of MA.5.NSO.2.3 and MA.5.NSO.1.4: add and subtract multi-digit numbers with decimals to the thousandths; compare decimals.",
  "MA.K12.MTR.6.1: Assess the reasonableness of solutions.",
  "MA.K12.MTR.7.1: Apply mathematics to real-world contexts.",
  "Financial literacy: reading receipts, sales tax, making change (Jump$tart Spending and Saving)."],
 "materials": ["The interactive lesson", "Coins and bills or play money", "A real receipt", "Grid paper for lining up digits", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 1 Reconnect questions. If long division is still shaky, schedule five minutes of extra practice; it returns in Week 4 with decimals."],
  [5, "Hook", "Show a real receipt on camera. Ask: how would you know if this is wrong?"],
  [10, "Place value", "Build 47.385 on the place-value chart. Use money: tenths are dimes, hundredths are pennies. Compare 0.6 and 0.58 with dimes and pennies."],
  [12, "Add and subtract", "Model lining up decimal points on grid paper. Have the student explain why placeholder zeros do not change a number's value. Work two of each type with estimates first."],
  [15, "Receipts and change", "Complete the receipt together. Role-play the counting-up method live: you are the customer and the student is the cashier."],
  [8, "Error analysis", "Present Devon's mistake. Have the student find and explain it before seeing the answer."],
  [4, "Assign", "Assign the KCE Store activity, Think Deeper and the Exit Check."]],
 "key_questions": ["Why do we line up decimal points instead of the last digits?", "Does writing 8.6 as 8.60 change its value? How do you know?", "What is your estimate, and is your answer close?", "How does counting up help a cashier avoid mistakes?"],
 "misconceptions": ["Thinking longer decimals are larger (0.45 > 0.5).", "Right-aligning digits instead of decimal points.", "Forgetting to regroup across a zero in 20.00 − 7.46.", "Dropping the decimal point in the answer."],
 "support": ["Use grid paper so each digit sits in one square.", "Model with real coins: $0.50 versus $0.45.", "Have the student write every number to the same number of decimal places before calculating."],
 "challenge": ["Ask the student to find a receipt at home with tax and work out what percent the tax was (preview of Unit 3).", "Have the student create a receipt with an error that is hard to spot and trade with you."],
 "background": "<p>In Florida the state sales tax rate is 6 percent, and many counties add a local surtax; groceries such as most food items are exempt. The receipt in the lesson uses a fixed tax amount to keep the focus on decimal operations.</p>"
}

PRINT = {
 "directions": "Line up decimal points. Estimate first, then solve. No calculator.",
 "items": [
  {"q":"Write the value of the 7 in each number:  3.72 ______   0.017 ______   7.4 ______","a":"7 tenths (0.7); 7 thousandths (0.007); 7 ones (7)","lines":1},
  {"q":"Order from greatest to least: 4.09, 4.9, 4.099, 4.19","a":"4.9, 4.19, 4.099, 4.09","lines":1},
  {"q":"23.6 + 8.47","a":"32.07","lines":2},
  {"q":"5.08 + 12 + 0.993","a":"18.073","lines":2},
  {"q":"40 − 18.25","a":"21.75","lines":2},
  {"q":"7.2 − 4.836","a":"2.364","lines":2},
  {"q":"A receipt lists $14.29, $6.50 and $2.88 with $1.42 tax. Find the subtotal, the total, and the change from $30.","a":"Subtotal $23.67; total $25.09; change $4.91","lines":3},
  {"q":"Jada says 0.8 − 0.25 = 0.63. Is she right? Explain and correct her.","a":"No. 0.80 − 0.25 = 0.55. She did not line up the places (or did not write 0.8 as 0.80).","lines":2}]
}
