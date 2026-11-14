def grid(cols, rows):
    sq = ''
    for r in range(10):
        for c in range(10):
            a = c < cols; b = r < rows
            fill = '#7a5cb8' if a and b else ('#9ec3f0' if a else ('#f2d58a' if b else '#fff'))
            sq += f'<rect x="{60+c*22}" y="{40+r*22}" width="22" height="22" fill="{fill}" stroke="#c9c2b0"/>'
    return ('<svg viewBox="0 0 400 290" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Hundredths grid showing 0.3 times 0.4">'
            '<text x="200" y="22" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">0.3 × 0.4 on a hundredths grid</text>' + sq +
            '<text x="300" y="80" fill="#2a5aa0">blue: 3 tenths</text><text x="300" y="100" fill="#8a6d1f">gold: 4 tenths</text>'
            '<text x="300" y="130" fill="#5a3f99" font-weight="bold">overlap:</text><text x="300" y="148" fill="#5a3f99" font-weight="bold">12 hundredths</text><text x="300" y="166" fill="#5a3f99" font-weight="bold">= 0.12</text></svg>')

LESSON = {
 "unit": "Unit 1: Number Power",
 "title": "Multiplying Decimals",
 "subtitle": "Paychecks, prices by the pound and measurements all depend on multiplying decimals correctly.",
 "objectives": [
  "Model decimal multiplication on a hundredths grid and explain why 0.3 × 0.4 = 0.12.",
  "Multiply multi-digit decimals with the standard algorithm and place the decimal point correctly.",
  "Predict whether a product will be greater or less than a factor.",
  "Multiply by powers of ten (10, 100, 1,000, 0.1, 0.01) by reasoning about place value.",
  "Calculate earnings from an hourly wage and round money to the nearest cent."],
 "vocab": [
  ["factor", "A number being multiplied. In 2.4 × 1.35, both numbers are factors."],
  ["product", "The answer to a multiplication problem."],
  ["decimal places", "The number of digits to the right of the decimal point. 1.35 has two decimal places."],
  ["power of ten", "A number such as 10, 100, 1,000 or 0.1 made by multiplying or dividing 1 by 10 again and again."],
  ["hourly wage", "The amount of money a worker earns for each hour of work."],
  ["gross pay", "Total earnings before anything, such as taxes, is taken out."],
  ["unit price", "The cost for one unit, such as one pound or one ounce."]],
 "reconnect": {
  "title": "Week 2: decimal place value, adding and subtracting",
  "intro": "Multiplying decimals depends on knowing place value and lining up decimals correctly. Warm up last week's skills.",
  "items": [
   {"t":"num","q":"14.6 + 3.85 = ?","a":18.45,"pts":2,"why":"14.60 + 3.85 = 18.45."},
   {"t":"num","q":"20 − 6.37 = ?","a":13.63,"pts":2,"why":"20.00 − 6.37 = 13.63."},
   {"t":"order","q":"Order from least to greatest.","items":["0.054","0.405","0.45","0.5"],"pts":3,"why":"Write each to thousandths: 0.054, 0.405, 0.450, 0.500."},
   {"t":"num","q":"In 3.142, which digit is in the thousandths place?","a":2,"pts":2,"why":"Tenths 1, hundredths 4, thousandths 2."},
   {"t":"num","q":"A receipt shows $7.89 and $12.40 plus $1.22 tax. You pay with $30. What is your change?","a":8.49,"unit":"dollars","show":"$8.49","pts":3,"why":"7.89 + 12.40 + 1.22 = $21.51. 30.00 − 21.51 = $8.49."},
   {"t":"num","q":"From Week 1: 1,764 ÷ 42 = ?","a":42,"pts":3,"why":"42 × 42 = 1,764. Long division keeps coming back, including next week with decimals."},
   {"t":"num","q":"Which is greater, 0.6 or 0.58? Type the greater number.","a":0.6,"pts":2,"why":"0.6 = 0.60, and 60 hundredths is more than 58 hundredths (6 tenths is more than 5 tenths)."}]},
 "hook": {
  "title": "Kwame's First Paycheck",
  "html": "<p>Amara's older brother Kwame is 16 and just got his first job at a garden center in Lakeland. He earns <b>$15.75 an hour</b>. His first week he worked 6.5 hours on Saturday and 4.25 hours on Sunday. When his paycheck arrived, he wanted to know: is this right?</p><p>To check, Kwame has to multiply decimals: dollars and cents times hours and parts of hours. One misplaced decimal point would make his pay look ten times too big or ten times too small.</p><div class='callout'><b>Big idea:</b> Multiply decimals like whole numbers, then use place value (and an estimate) to put the decimal point in the right place.</div>"},
 "learn": [
  {"title": "Seeing Decimal Multiplication",
   "visual": grid(3, 4),
   "html": "<p>On a hundredths grid, each small square is 0.01. Shade 3 columns for 0.3 and 4 rows for 0.4. The overlap, the part that is <i>both</i>, is 12 small squares: <b>0.3 × 0.4 = 0.12</b>.</p><p>Notice the product, 0.12, is <b>smaller</b> than both factors. Multiplying by a number less than 1 means taking <i>part of</i> something, so the result shrinks.</p><div class='callout'>Tenths × tenths = hundredths. That is why the product has two decimal places.</div>",
   "checks": [
    {"t":"num","q":"Use the grid idea: 0.6 × 0.7 = ?","a":0.42,"pts":3,"why":"6 tenths × 7 tenths = 42 hundredths = 0.42."},
    {"t":"num","q":"0.2 × 0.5 = ?","a":0.1,"pts":3,"hint":"How many hundredths overlap? Then simplify.","why":"2 tenths × 5 tenths = 10 hundredths = 0.10 = 0.1."},
    {"t":"open","key":"predict48","q":"Without calculating, will 48 × 0.75 be more or less than 48? Explain using what multiplying by a number less than 1 means.","min":12,"rows":2,"rubric":["Says less","Explains that 0.75 is less than 1, so the product is only part of 48"],"model":"Less, because multiplying by 0.75 means taking three fourths of 48, which is only part of it (36)."},
    {"t":"text","q":"Will 48 × 1.5 be greater than or less than 48?","a":["greater","greater than","greater than 48","more"],"show":"greater","pts":2,"why":"1.5 is greater than 1, so the product is more than 48 (it is 72)."}]},
  {"title": "The Standard Algorithm",
   "html": "<p>Step 1: Ignore the decimal points and multiply as whole numbers. Step 2: Count the total decimal places in both factors. Step 3: Give the product that many decimal places.</p><div class='example'><b>2.4 × 1.35</b><br>Multiply 24 × 135 = 3,240.<br>2.4 has 1 decimal place and 1.35 has 2: that is 3 in total.<br>3,240 becomes <b>3.240</b>, or 3.24.<br>Estimate to check: 2 × 1 = 2 and 3 × 1.5 = 4.5, so 3.24 is reasonable.</div><p>You do not line up decimal points when you multiply. That rule is only for adding and subtracting.</p>",
   "checks": [
    {"t":"num","q":"3.6 × 2.5 = ?","a":9,"pts":3,"why":"36 × 25 = 900, with 2 decimal places: 9.00 = 9."},
    {"t":"num","q":"0.08 × 4.5 = ?","a":0.36,"pts":3,"hint":"8 × 45 = 360. How many decimal places in total?","why":"8 × 45 = 360, with 3 decimal places: 0.360 = 0.36."},
    {"t":"num","q":"12.5 × 0.04 = ?","a":0.5,"pts":3,"why":"125 × 4 = 500, with 3 decimal places: 0.500 = 0.5."},
    {"t":"num","q":"6.25 × 3.2 = ?","a":20,"pts":3,"why":"625 × 32 = 20,000, with 3 decimal places: 20.000 = 20."},
    {"t":"num","q":"1.8 × 2.05 = ?","a":3.69,"pts":3,"why":"18 × 205 = 3,690, with 3 decimal places: 3.690 = 3.69."}]},
  {"title": "Earning an Hourly Wage",
   "html": "<p><b>Gross pay = hourly wage × hours worked.</b> Money is rounded to the nearest cent (hundredth).</p><table class='t'><tr><th>Kwame's week</th><th>Hours</th></tr><tr><td>Saturday</td><td>6.5</td></tr><tr><td>Sunday</td><td>4.25</td></tr><tr><td>Wage</td><td>$15.75 per hour</td></tr></table><div class='example'><b>Saturday:</b> 15.75 × 6.5 = 102.375, which rounds to <b>$102.38</b>.</div>",
   "checks": [
    {"t":"num","q":"How many hours did Kwame work in total?","a":10.75,"unit":"hours","pts":2,"why":"6.5 + 4.25 = 10.75 hours."},
    {"t":"num","q":"What was his pay for Sunday (4.25 hours)? Round to the nearest cent.","a":66.94,"tol":0.001,"unit":"dollars","show":"$66.94","pts":3,"why":"15.75 × 4.25 = 66.9375, which rounds to $66.94."},
    {"t":"num","q":"Kwame adds his rounded daily amounts. What total does he get?","a":169.32,"tol":0.001,"unit":"dollars","show":"$169.32","pts":2,"why":"$102.38 + $66.94 = $169.32."},
    {"t":"open","key":"paycheck","q":"Kwame's paycheck says $169.31, one cent less than his total. The company multiplied his wage by his total hours: 15.75 × 10.75. Calculate it, then explain who is right and why the two answers differ.","min":30,"rows":4,"rubric":["Calculates 15.75 × 10.75 = 169.3125, which rounds to $169.31","Explains that rounding each day separately added extra fractions of a cent","Concludes the paycheck is correct (or that both methods are reasonable but the company rounds once)"],"model":"15.75 × 10.75 = 169.3125, which rounds to $169.31. When I rounded each day first, Saturday went up 0.5 cent and Sunday went up 0.25 cent, and those small bits added up to an extra cent. The company rounded only once at the end, so the paycheck is correct."},
    {"t":"num","q":"Kwame fills the family car with 12.6 gallons of gas at $3.459 per gallon. What does it cost, to the nearest cent?","a":43.58,"tol":0.001,"unit":"dollars","show":"$43.58","pts":3,"why":"3.459 × 12.6 = 43.5834, which rounds to $43.58. Gas prices go to the thousandths of a dollar."},
    {"t":"num","q":"Ground turkey costs $4.80 per pound. A package weighs 2.375 pounds. What does it cost?","a":11.4,"tol":0.001,"unit":"dollars","show":"$11.40","pts":3,"why":"4.80 × 2.375 = 11.4000, so $11.40. Deli and meat scales often weigh to the thousandths of a pound."},
    {"t":"num","q":"A store sells cheese at $9.85 per pound. A piece weighs 3.25 pounds. What does it cost, rounded to the nearest cent?","a":32.01,"tol":0.001,"unit":"dollars","show":"$32.01","pts":3,"why":"9.85 × 3.25 = 32.0125, which rounds to $32.01."}]},
  {"title": "Multiplying by Powers of Ten",
   "html": "<p>Multiplying by 10, 100 or 1,000 makes every digit move <b>left</b> into a bigger place value: one place for 10, two for 100, three for 1,000. Multiplying by 0.1 or 0.01 moves digits <b>right</b> into smaller place values.</p><table class='t'><tr><th>Problem</th><th>Product</th></tr><tr><td>4.56 × 10</td><td>45.6</td></tr><tr><td>4.56 × 100</td><td>456</td></tr><tr><td>4.56 × 1,000</td><td>4,560</td></tr><tr><td>4.56 × 0.1</td><td>0.456</td></tr><tr><td>4.56 × 0.01</td><td>0.0456</td></tr></table><p>This is the math behind the metric system: 1 meter = 100 centimeters, so 2.5 m = 2.5 × 100 = 250 cm.</p>",
   "checks": [
    {"t":"num","q":"A hardware store sells screws for $0.035 each. What do 1,000 screws cost?","a":35,"unit":"dollars","show":"$35","pts":2,"why":"0.035 × 1,000: each digit moves three places left, so $35.00."},
    {"t":"num","q":"A coupon takes 0.1 of the bill off a $34.50 order. How much money does the coupon save?","a":3.45,"unit":"dollars","show":"$3.45","pts":2,"why":"34.50 × 0.1: each digit moves one place right, so $3.45."},
    {"t":"num","q":"A shelf is 1.85 meters long. How many centimeters is that? (1 m = 100 cm)","a":185,"unit":"cm","pts":3,"why":"1.85 × 100 = 185 cm."},
    {"t":"num","q":"A garden center sells mulch for $3.99 a bag. What do 100 bags cost?","a":399,"unit":"dollars","show":"$399","pts":2,"why":"3.99 × 100 = $399."}]}],
 "handson": {
  "title": "Price by the Pound",
  "intro": "Many grocery items are priced by weight. Use real weights to find real costs.",
  "materials": ["A kitchen scale that shows pounds (or ounces), or produce bags labeled with weights", "3 fruits or vegetables at home (or a store flyer showing prices per pound)", "Paper and pencil; a calculator only for checking at the end"],
  "steps": [
   "Find or set a price per pound for each item. Use a flyer, a receipt, or these prices: bananas $0.59/lb, apples $1.29/lb, potatoes $0.89/lb.",
   "Weigh each item. If your scale shows pounds and ounces, use this table to change ounces to a decimal: 2 oz = 0.125 lb, 4 oz = 0.25 lb, 6 oz = 0.375 lb, 8 oz = 0.5 lb, 10 oz = 0.625 lb, 12 oz = 0.75 lb, 14 oz = 0.875 lb. Round to the nearest even number of ounces (so 1 lb 5 oz becomes 1 lb 6 oz = 1.375 lb).",
   "Estimate each cost first. Then multiply price × weight with the standard algorithm, and round to the nearest cent.",
   "Add the three costs to find the total.",
   "Check every calculation with a calculator. Circle any mistakes and explain them."],
  "record": [
   {"t":"open","key":"pound","q":"Make a table with each item, its price per pound, its weight, your estimate and the exact cost. Show the work for one multiplication.","min":40,"rows":6},
   {"t":"open","key":"pound2","q":"Which estimate was closest to the exact cost, and which was farthest? Why do you think so?","min":20,"rows":3}]},
 "think": {
  "intro": "Explain your reasoning. These answers go to your teacher.",
  "items": [
   {"t":"num","q":"Maya says 0.4 × 0.2 = 0.8. What is the correct product?","a":0.08,"pts":3,"why":"4 × 2 = 8, with 2 decimal places: 0.08."},
   {"t":"open","key":"maya","q":"Explain Maya's mistake, and use a hundredths grid or an estimate to prove your answer.","min":30,"rubric":["Names the mistake: she counted only one decimal place, or added instead of multiplying","Explains that tenths × tenths = hundredths","Uses a grid, estimate or reasoning (0.4 of 0.2 must be less than 0.2)"],"model":"Maya only gave her answer one decimal place, but tenths times tenths makes hundredths, so the product needs two places: 0.08. Also, 0.4 × 0.2 means four tenths of 0.2, which must be less than 0.2, so 0.8 is impossible."},
   {"t":"open","key":"bigger","q":"Your friend says, \"Multiplying always makes a number bigger.\" Write a response that explains when this is true and when it is false, with an example of each and a real-life situation.","min":45,"rubric":["Explains that factors greater than 1 increase the product","Explains that factors between 0 and 1 decrease it","Gives a correct numeric example of each","Connects to a real situation such as discounts or half portions"],"model":"It is only true when you multiply by a number greater than 1, like 20 × 1.5 = 30. When you multiply by a number between 0 and 1, you take only part, so the product shrinks: 20 × 0.5 = 10. In real life, if a $20 shirt is on sale for 0.75 of its price, you pay $15, which is less."}]},
 "exit": [
  {"t":"num","q":"4.7 × 0.6 = ?","a":2.82,"pts":3,"why":"47 × 6 = 282, with 2 decimal places: 2.82."},
  {"t":"num","q":"15.25 × 2.4 = ?","a":36.6,"pts":3,"why":"1,525 × 24 = 36,600, with 3 decimal places: 36.600 = 36.6."},
  {"t":"num","q":"0.35 × 0.2 = ?","a":0.07,"pts":3,"why":"35 × 2 = 70, with 3 decimal places: 0.070 = 0.07."},
  {"t":"num","q":"2.08 × 1,000 = ?","a":2080,"show":"2,080","pts":2,"why":"Each digit moves three places left: 2,080."},
  {"t":"num","q":"A worker earns $15.50 an hour and works 12.4 hours. What is her gross pay?","a":192.2,"unit":"dollars","show":"$192.20","pts":3,"why":"15.50 × 12.4 = $192.20."},
  {"t":"num","q":"Grapes cost $2.49 per pound. Ade buys 2.5 pounds. What does he pay, rounded to the nearest cent?","a":6.23,"tol":0.001,"unit":"dollars","show":"$6.23","pts":3,"why":"2.49 × 2.5 = 6.225, which rounds to $6.23."},
  {"t":"num","q":"A $2.125-per-pound bag of onions weighs 3.2 pounds. What does it cost?","a":6.8,"tol":0.001,"unit":"dollars","show":"$6.80","pts":3,"why":"2.125 × 3.2 = 6.8000, so $6.80."}],
 "next": "Week 4: dividing decimals, using unit prices to find the better buy."
}

TEACHER = {
 "standards": [
  "MA.6.NSO.2.1: Multiply and divide positive multi-digit numbers with decimals to the thousandths, including using a standard algorithm with procedural fluency.",
  "MA.5.NSO.2.4 and MA.5.NSO.2.5 (review): explore multiplying decimals with models; multiply by powers of ten.",
  "MA.K12.MTR.2.1: Demonstrate understanding by representing problems in multiple ways (grid models and the algorithm).",
  "MA.K12.MTR.6.1: Assess the reasonableness of solutions.",
  "Financial literacy: earning income, hourly wages and gross pay; unit pricing (Jump$tart Earning Income)."],
 "materials": ["The interactive lesson", "Hundredths grid paper or a printed 10 by 10 grid", "Colored pencils", "A kitchen scale and three pieces of produce", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 2 Reconnect questions."],
  [5, "Hook", "Read Kwame's paycheck situation. Ask the student to estimate his Saturday pay before calculating (about 16 × 6 = 96)."],
  [12, "Grid model", "Shade 0.3 × 0.4 on a hundredths grid together. Then the student shades 0.6 × 0.7. Discuss why the product is smaller than both factors."],
  [12, "Algorithm", "Model 2.4 × 1.35. Stress estimating to check the decimal point. The student works 6.25 × 3.2 and explains each step."],
  [10, "Hourly wage", "Calculate Kwame's pay for both days. Practice rounding money to the nearest cent."],
  [10, "Powers of ten", "Use a place-value chart to show digits moving. Connect to converting meters to centimeters, which returns in Science Week 3."],
  [5, "Assign", "Assign the Price by the Pound activity, Think Deeper and the Exit Check."]],
 "key_questions": ["Before you calculate, will the product be bigger or smaller than this factor? How do you know?", "Why don't we line up the decimal points when we multiply?", "How does your estimate tell you where the decimal point goes?", "Why do we round money to two decimal places?"],
 "misconceptions": ["Lining up decimal points as in addition.", "Counting decimal places in only one factor.", "Believing multiplication always makes numbers bigger.", "Dropping placeholder zeros needed in products like 0.08."],
 "support": ["Use hundredths grids for every tenths × tenths problem.", "Have the student write the estimate first in a box beside each problem.", "Provide a place-value chart for powers of ten."],
 "challenge": ["Kwame's employer withholds about 7.65 percent for Social Security and Medicare. Estimate his take-home pay for 10.75 hours (preview of percents in Unit 3).", "Find the cost of 0.375 pounds of a $14.80-per-pound spice and round to the nearest cent ($5.55)."],
 "background": "<p>The federal minimum wage has been $7.25 an hour since 2009. Florida's minimum wage reached $15.00 an hour on September 30, 2026, and is adjusted for inflation after that, so every wage in this lesson is $15.00 or more. Kwame's $15.75 is a realistic first-job wage. The paycheck puzzle shows why employers round once, at the end.</p>"
}

PRINT = {
 "directions": "Estimate first. Then multiply and place the decimal point. No calculator.",
 "items": [
  {"q":"Shade a hundredths grid in your head or on scrap paper: 0.5 × 0.8 = ____. Explain what the overlap represents.","a":"0.40 = 0.4; the overlap is 40 hundredths.","lines":2},
  {"q":"3.4 × 2.6","a":"8.84","lines":2},
  {"q":"0.07 × 5.2","a":"0.364","lines":2},
  {"q":"14.5 × 0.06","a":"0.87","lines":2},
  {"q":"9.3 × 100 = ______   0.42 × 1,000 = ______   56 × 0.1 = ______","a":"930; 420; 5.6","lines":1},
  {"q":"Lena earns $15.20 an hour and works 15.5 hours. Find her gross pay.","a":"15.20 × 15.5 = $235.60","lines":2},
  {"q":"Tomatoes cost $1.79 per pound. Find the cost of 3.6 pounds, rounded to the nearest cent.","a":"1.79 × 3.6 = 6.444, so $6.44","lines":2},
  {"q":"Without calculating, circle the products less than 60: 60 × 0.8   60 × 1.2   60 × 0.05   60 × 2.5. Explain your rule.","a":"60 × 0.8 and 60 × 0.05; multiplying by a number less than 1 makes the product less than 60.","lines":2}]
}
