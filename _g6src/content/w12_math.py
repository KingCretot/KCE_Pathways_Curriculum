def grid(n, title, color="#0047BA"):
    s = (f'<svg viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="{title}">'
         f'<text x="150" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="14">{title}</text>')
    for i in range(100):
        r, c = divmod(i, 10)
        s += f'<rect x="{40+c*22}" y="{34+r*22}" width="22" height="22" fill="{color if i < n else "#fff"}" stroke="#0A1F3D" stroke-width=".6"/>'
    return s + '</svg>'

def three():
    s = '<svg viewBox="0 0 640 300" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Three hundred-square grids: 25, 60 and 7.5 percent">'
    for k, (n, t, c) in enumerate([(25, "25% = 25/100 = 1/4", "#0047BA"), (60, "60% = 60/100 = 3/5", "#3d9a2f"), (7.5, "7.5% = 0.075", "#DB2F30")]):
        ox = 10 + k * 212
        s += f'<text x="{ox+100}" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D">{t}</text>'
        for i in range(100):
            r, c2 = divmod(i, 10); fill = c if i < int(n) else "#fff"
            s += f'<rect x="{ox+c2*20}" y="{34+r*20}" width="20" height="20" fill="{fill}" stroke="#0A1F3D" stroke-width=".6"/>'
        if n % 1:
            i = int(n); r, c2 = divmod(i, 10)
            s += f'<rect x="{ox+c2*20}" y="{34+r*20}" width="10" height="20" fill="{c}"/>'
    s += '<text x="320" y="262" text-anchor="middle" font-size="12">Each grid is 100 squares. Percent means \"out of 100.\"</text>'
    s += '<text x="320" y="280" text-anchor="middle" font-size="11" fill="#5b6676">7.5% is 7 and a half squares: DeSoto County\'s total sales tax rate.</text></svg>'
    return s

def dnl_pct():
    s = ('<svg viewBox="0 0 640 140" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Percent double number line for 40 dollars">'
         '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Finding a percent of $40 with a double number line</text>'
         '<line x1="80" y1="60" x2="600" y2="60" stroke="#0A1F3D" stroke-width="2"/><line x1="80" y1="100" x2="600" y2="100" stroke="#0A1F3D" stroke-width="2"/>'
         '<text x="10" y="65" font-weight="bold" fill="#0047BA">Dollars</text><text x="10" y="105" font-weight="bold" fill="#DB2F30">Percent</text>')
    for i, (d, p) in enumerate([("$0", "0%"), ("$4", "10%"), ("$10", "25%"), ("$20", "50%"), ("$30", "75%"), ("$40", "100%")]):
        x = 80 + [0, 52, 130, 260, 390, 520][i]
        s += f'<line x1="{x}" y1="54" x2="{x}" y2="106" stroke="#0A1F3D"/><text x="{x}" y="46" text-anchor="middle">{d}</text><text x="{x}" y="124" text-anchor="middle">{p}</text>'
    return s + '</svg>'

RECEIPT = ('<svg viewBox="0 0 640 260" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Store receipt with sales tax">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">A cash-register slip in DeSoto County (7.5% sales tax)</text>'
  '<rect x="180" y="34" width="280" height="216" fill="#fff" stroke="#8a8f99"/>'
  '<text x="320" y="56" text-anchor="middle" font-weight="bold" font-family="Courier New, monospace">PEACE RIVER HARDWARE</text>'
  + ''.join(f'<text x="196" y="{y}" font-family="Courier New, monospace">{a}</text><text x="444" y="{y}" text-anchor="end" font-family="Courier New, monospace">{b}</text>' for y, a, b in [(84, "Paint brush set", "$12.00"), (104, "Garden hose", "$24.00"), (124, "Work gloves", "$4.00")]) +
  '<line x1="196" y1="136" x2="444" y2="136" stroke="#8a8f99" stroke-dasharray="4 3"/>'
  '<text x="196" y="156" font-family="Courier New, monospace">SUBTOTAL</text><text x="444" y="156" text-anchor="end" font-family="Courier New, monospace">$40.00</text>'
  '<text x="196" y="178" font-family="Courier New, monospace">TAX 7.5%</text><text x="444" y="178" text-anchor="end" font-family="Courier New, monospace" fill="#DB2F30">$ ?</text>'
  '<text x="196" y="204" font-family="Courier New, monospace" font-weight="bold">TOTAL</text><text x="444" y="204" text-anchor="end" font-family="Courier New, monospace" font-weight="bold" fill="#DB2F30">$ ?</text>'
  '<text x="320" y="236" text-anchor="middle" font-size="10" fill="#5b6676">Store name and prices invented for practice.</text></svg>')

LESSON = {
 "unit": "Unit 3: Rates and Percents",
 "title": "Understanding Percents",
 "subtitle": "A percent is a rate per 100. Percents let you compare test scores, batteries, sales and taxes on the same scale, and they show up on almost every receipt.",
 "objectives": [
  "Explain a percent as a rate per 100 and model it on a hundred grid.",
  "Convert among percents, fractions and decimals.",
  "Find a percent of a number using benchmarks, double number lines and multiplication.",
  "Find the whole when a part and a percent are known.",
  "Calculate sales tax and total cost, including Florida's state and county rates."],
 "vocab": [
  ["percent", "A rate per 100; the symbol % means \"out of 100.\" 45% = 45/100."],
  ["benchmark percent", "An easy percent to use for estimating, such as 10%, 25%, 50% and 1%."],
  ["part, whole, percent", "In \"30 is 60% of 50,\" 30 is the part, 50 is the whole and 60% is the percent."],
  ["sales tax", "Money a state or county adds to the price of many purchases, a percent of the price."],
  ["subtotal", "The total price of items before tax is added."],
  ["exempt", "Not required to pay; in Florida, most groceries are exempt from sales tax."]],
 "reconnect": {
  "title": "Week 11: Unit rates",
  "intro": "A percent is a special unit rate: a rate per 100. Warm up first.",
  "items": [
   {"t":"num","q":"A car travels 210 miles in 3 1/2 hours. What is its speed in miles per hour?","a":60,"unit":"miles per hour","pts":2,"why":"210 ÷ 3 1/2 = 210 ÷ 7/2 = 210 × 2/7 = 60."},
   {"t":"num","q":"A 24-ounce bag of granola costs $4.80. What is the unit price in cents per ounce? (Type the number of cents.)","a":20,"unit":"cents per ounce","pts":2,"why":"$4.80 ÷ 24 = $0.20, which is 20 cents per ounce."},
   {"t":"open","key":"rc_pace","q":"Explain why a pace of 12 minutes per mile is slower than a pace of 9 minutes per mile.","min":12,"rows":2,"rubric":["More minutes for each mile means it takes longer to cover the same distance"],"model":"At 12 minutes per mile, each mile takes 3 more minutes than at 9, so the runner covers the same distance more slowly."},
   {"t":"blanks","q":"Complete the ratio table: 3 out of every 5 students walk to the park.","sent":"Walkers: 3, 6, ___, 60. Students: 5, 10, 50, ___.","blanks":[["30"],["100"]],"show":"30; 100","pts":2,"why":"3 : 5 = 30 : 50 = 60 : 100. 60 out of 100 is today's topic: a percent."}]},
 "hook": {
  "title": "Which Score Is Better?",
  "html": "<p>Jamal got 21 out of 25 on a spelling test. Nia got 34 out of 40 on hers. Who did better? You can't tell from the raw scores, because the tests had different numbers of questions.</p><p>Change both to a rate per 100. Jamal: 21/25 = 84/100. Nia: 34/40 = 85/100. Nia did slightly better: <b>85 percent</b> versus <b>84 percent</b>. Percents put every comparison on the same scale, out of 100.</p><p>You see percents everywhere: a phone battery at 37%, a 30% chance of rain, a 25% off sale and the sales tax on a receipt.</p><div class='callout'><b>Big idea:</b> Percent means \"per hundred.\" A percent is a ratio that compares a number to 100.</div>"},
 "learn": [
  {"title": "What a Percent Means",
   "visual": three(),
   "html": "<p>The word <b>percent</b> comes from Latin <i>per centum</i>, \"for each hundred.\" On a hundred grid, 25% means 25 of the 100 squares are shaded. That is the same as the fraction 25/100, which simplifies to 1/4, and the decimal 0.25.</p><div class='callout'><b>Percent to decimal:</b> divide by 100 (move the decimal point two places left): 60% = 0.60 = 0.6; 7.5% = 0.075.<br><b>Decimal to percent:</b> multiply by 100: 0.38 = 38%; 1.2 = 120%.<br><b>Fraction to percent:</b> make the denominator 100, or divide: 3/5 = 60/100 = 60%; 1/8 = 0.125 = 12.5%.</div><p>Percents can be greater than 100% (a plant that grew to 150% of its height) or less than 1% (0.5% is half of one square).</p>",
   "checks": [
    {"t":"blanks","q":"Complete the conversions.","sent":"40% = ___ (decimal). &nbsp; 0.07 = ___% &nbsp; 3/4 = ___%","blanks":[["0.4","0.40",".4",".40"],["7"],["75"]],"show":"0.4; 7; 75","pts":3,"why":"40 ÷ 100 = 0.4; 0.07 × 100 = 7; 3/4 = 75/100."},
    {"t":"text","q":"Write 35% as a fraction in simplest form.","a":["7/20","7 / 20"],"show":"7/20","pts":2,"why":"35/100; the GCF is 5, so 7/20."},
    {"t":"num","q":"Rosa scored 27 out of 30 on a quiz. What percent is that?","a":90,"unit":"%","pts":2,"why":"27/30 = 9/10 = 90/100 = 90%."},
    {"t":"open","key":"over100","q":"A sunflower was 40 inches tall in June and 60 inches tall in August. Its August height is 150% of its June height. Explain how a percent can be more than 100.","min":20,"rows":2,"rubric":["100% is the whole original amount (40 inches); more than 100% means more than the original","60 is 1 1/2 times 40, which is 150%"],"model":"100% means the whole June height, 40 inches. The plant grew taller than that, to 60 inches, which is 1 1/2 times as tall, so it is 150% of its June height."}]},
  {"title": "Finding a Percent of a Number",
   "visual": dnl_pct(),
   "html": "<p>To find a percent of a number, you can use three tools:</p><ul><li><b>Benchmarks:</b> 50% is half, 25% is a fourth, 10% is a tenth (move the decimal one place left), 1% is a hundredth. 10% of $40 is $4, so 30% is 3 × $4 = $12.</li><li><b>A double number line</b> or <b>ratio table</b>: line up percents with amounts, as in Unit 2.</li><li><b>Multiplication:</b> change the percent to a decimal or fraction and multiply. 35% of 80 = 0.35 × 80 = 28.</li></ul><p>Use benchmarks to check: 35% of 80 should be a bit more than 25% (20) and less than 50% (40). 28 makes sense.</p>",
   "checks": [
    {"t":"num","q":"What is 10% of $65?","a":6.5,"unit":"dollars","show":"$6.50","pts":2,"why":"Move the decimal one place left: $6.50."},
    {"t":"num","q":"What is 15% of $60? (Hint: 10% plus half of 10%.)","a":9,"unit":"dollars","show":"$9","pts":2,"why":"10% = $6; 5% = $3; 15% = $9."},
    {"t":"num","q":"A phone battery holds 4,000 units of charge. It shows 35%. How many units are left?","a":1400,"unit":"units","pts":3,"why":"0.35 × 4,000 = 1,400."},
    {"t":"num","q":"A family's monthly income is $3,200. They save 12% of it. How much do they save each month?","a":384,"unit":"dollars","show":"$384","pts":3,"why":"0.12 × $3,200 = $384 (or 10% = $320 plus 2% = $64)."}]},
  {"title": "Finding the Whole",
   "html": "<p>Sometimes you know the part and the percent, and you need the whole.</p><div class='callout'><b>Example:</b> 18 students in a co-op are in the band. That is 30% of the co-op. How many students are in the co-op?<br>30% → 18. So 10% → 6 (divide both by 3). So 100% → 60 (multiply by 10). There are 60 students.</div><p>A ratio table makes this easy: find 10% or 1% first, then scale up to 100%.</p>",
   "checks": [
    {"t":"num","q":"Amara has saved $45, which is 25% of the cost of a bike. How much does the bike cost?","a":180,"unit":"dollars","show":"$180","pts":3,"why":"25% → $45, so 100% → 4 × $45 = $180."},
    {"t":"num","q":"A water tank is 40% full and holds 120 gallons right now. How many gallons does it hold when full?","a":300,"unit":"gallons","pts":3,"why":"40% → 120, 10% → 30, 100% → 300."},
    {"t":"open","key":"wholecheck","q":"Priya says, \"If 20 is 50% of a number, the number is 10.\" Explain her mistake and give the correct answer.","min":15,"rows":2,"rubric":["She took 50% of 20 instead of finding the whole","20 is half of the number, so the number is 40"],"model":"She found 50% of 20 instead of finding the whole. If 20 is half of the number, the whole number is 40."}]},
  {"title": "Money: Sales Tax",
   "visual": RECEIPT,
   "html": "<p><b>Sales tax</b> is a percent of the price added at the register. Florida's state sales tax is 6%. Most Florida counties add a small county tax (called a discretionary sales surtax). In DeSoto County it is 1.5%, so the total is <b>7.5%</b>. Across Florida, the total ranges from 6% to 8%, depending on the county.</p><p>To find the tax, multiply the subtotal by the rate as a decimal: $40.00 × 0.075 = $3.00. The total is $40.00 + $3.00 = $43.00. A shortcut: multiply by 1.075 to find the total in one step.</p><p>Not everything is taxed. In Florida, most groceries and prescription medicines are exempt. And every August, Florida holds a <b>back-to-school sales tax holiday</b>: school supplies priced at $50 or less, clothing at $100 or less, learning aids at $30 or less and personal computers at $1,500 or less can be bought without sales tax.</p>",
   "checks": [
    {"t":"num","q":"Find the tax on the paint brush set alone ($12.00) at 7.5%.","a":0.9,"unit":"dollars","show":"$0.90","pts":2,"why":"$12 × 0.075 = $0.90."},
    {"t":"num","q":"A $24 garden hose is bought in a county with 7% total sales tax. What is the total cost?","a":25.68,"unit":"dollars","show":"$25.68","pts":3,"why":"Tax: $24 × 0.07 = $1.68. Total: $24 + $1.68 = $25.68 (or $24 × 1.07)."},
    {"t":"num","q":"In August, a family buys $90 of school supplies (every item under $50) and a $120 pair of shoes in DeSoto County. How much sales tax do they pay?","a":9,"unit":"dollars","show":"$9.00","pts":3,"why":"Supplies under $50 each are tax-free in August. The $120 shoes are over the $100 clothing limit, so the whole price is taxed: $120 × 0.075 = $9.00."},
    {"t":"open","key":"taxwhy","q":"Sales tax pays for things like roads, schools and emergency services. Why do you think Florida exempts most groceries from sales tax?","min":20,"rows":2,"rubric":["Gives a reason linked to food being a basic need or to fairness for families","A reasonable explanation"],"model":"Food is a basic need that every family must buy. Taxing groceries would take a bigger share of the money of families who earn less, so exempting them makes the tax fairer."}]}],
 "handson": {
  "title": "Percent Hunt and Tax-Holiday Planner",
  "intro": "Find percents in the real world, then plan a back-to-school list and see how much Florida's August tax holiday saves.",
  "materials": ["A store flyer or website with school supplies (with a parent)", "Packages, ads or labels at home (food labels, cleaning products, clothing tags)", "A calculator for checking only", "Paper and pencil", "Optional: 1 cup of dry beans or rice and a 10 by 10 grid drawn on paper"],
  "steps": [
   "Percent hunt: find five percents at home (nutrition labels show % Daily Value; clothing tags show 100% cotton; ads show % off). Write each one, what it is a percent of, and what it means.",
   "Tax-holiday planner: with a parent, use a store flyer or website to plan a back-to-school list of about $150. Mark which items would be tax-free in August under Florida's limits, then calculate the tax on the same list in October at 7.5% and how much the holiday saves.",
   "Which item on your list is taxed even in August, and why?",
   "Optional: shade or cover squares on a 10 by 10 grid with beans to model three of the percents you found."],
  "record": [
   {"t":"open","key":"hunt","q":"List the five percents you found, what each is a percent of, and what it means in your own words.","min":40,"rows":6,"rubric":["Five real percents","Correct whole identified for each","Clear meaning in own words"],"model":"1. Cereal: 25% Daily Value of iron: one bowl gives a fourth of the iron I need in a day. 2. T-shirt: 60% cotton: 60 of every 100 parts of the fabric are cotton. 3. Phone: 82% battery: 82 of every 100 parts of a full charge are left. 4. Sign: 30% off shoes: you pay $30 less for every $100 of the price. 5. Juice: 100% juice: all of the drink is fruit juice, not a juice drink with added sugar."},
   {"t":"open","key":"receipt","q":"Show your list with prices, mark each item tax-free or taxed in August, and calculate the August tax, the October tax at 7.5% and the savings.","min":40,"rows":5,"rubric":["A list with prices","Each item correctly marked using the August limits","August and October tax calculated correctly","Savings found"],"model":"Backpack $28, notebooks and pens $12, sneakers $110 = $150. August: only the sneakers are taxed (over the $100 clothing limit): $110 × 0.075 = $8.25. October: $150 × 0.075 = $11.25. Savings: $3.00."}]},
 "think": {
  "intro": "Show your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"budgettax","q":"You have exactly $50 to spend at a store in a county with 7.5% sales tax. What is the most expensive item you can buy so that the total with tax is $50 or less? Explain your method and check your answer.","min":50,"rows":5,"rubric":["Price × 1.075 ≤ $50, so price ≤ $50 ÷ 1.075 ≈ $46.51","Check: $46.51 × 1.075 ≈ $50.00 (and $46.52 goes over)","Clear explanation"],"model":"The total is the price times 1.075, so the price can be at most $50 ÷ 1.075 ≈ $46.51. Check: $46.51 × 0.075 = $3.49 in tax, and $46.51 + $3.49 = $50.00. A $46.52 item would go just over $50."},
   {"t":"open","key":"rain","q":"A forecast says there is a 30% chance of rain on Saturday and a 30% chance on Sunday. Mateo says that means a 60% chance of rain this weekend. Is he right? Explain using what a percent means.","min":45,"rows":4,"rubric":["Not right: you cannot simply add the two percents","Each percent is a chance out of 100 for its own day; the chance of rain on at least one day is more than 30% but less than 60%","Reasoning about what each percent refers to"],"model":"No. Each 30% is a chance out of 100 for its own day, so you can't just add them. If you could, two days of 60% would make 120%, which is impossible. The chance of rain on at least one day is higher than 30% but less than 60%."}]},
 "exit": [
  {"t":"blanks","q":"Complete.","sent":"0.6 = ___% &nbsp; 45% = ___ (decimal)","blanks":[["60"],["0.45",".45"]],"show":"60; 0.45","pts":2,"why":"0.6 × 100 = 60%; 45 ÷ 100 = 0.45."},
  {"t":"num","q":"What is 25% of 64?","a":16,"pts":2,"why":"25% is one fourth: 64 ÷ 4 = 16."},
  {"t":"num","q":"12 is 40% of what number?","a":30,"pts":2,"why":"40% → 12, so 10% → 3, so 100% → 30."},
  {"t":"num","q":"Find the total cost of a $30 item with 6% sales tax.","a":31.8,"unit":"dollars","show":"$31.80","pts":2,"why":"$30 × 0.06 = $1.80; $30 + $1.80 = $31.80."}],
 "next": "Week 13: percents in real life: discounts, tips and markups."
}

TEACHER = {
 "standards": [
  "MA.6.AR.3.4: Apply ratio relationships to solve mathematical and real-world problems involving percentages using the relationship between two quantities.",
  "MA.6.AR.3.5: Solve mathematical and real-world problems involving ratios, rates and unit rates, including comparisons, mixtures, ratios of lengths and conversions within the same measurement system.",
  "MA.K12.MTR.2.1: Demonstrate understanding by representing problems in multiple ways.",
  "MA.K12.MTR.7.1: Apply mathematics to real-world contexts.",
  "Financial literacy: sales tax, tax-exempt items and sales tax holidays (Jump$tart Spending)."],
 "materials": ["The interactive lesson", "A hundred grid (drawn or printed) and dry beans", "A store flyer or website with school supplies", "Food labels, clothing tags and ads", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 11 Reconnect questions."],
  [5, "Hook", "Compare the two spelling scores. Ask the student to guess before converting."],
  [10, "What a percent means", "Shade hundred grids. Convert among percents, fractions and decimals."],
  [12, "Percent of a number", "Build the double number line for $40. Practice benchmark shortcuts."],
  [8, "Finding the whole", "Use a ratio table: find 10% first, then 100%."],
  [12, "Sales tax", "Complete the receipt. Discuss DeSoto County's 7.5%, groceries and the August holiday."],
  [7, "Assign", "Start the percent hunt together; assign the tax-holiday planner, Think Deeper and the Exit Check."]],
 "key_questions": ["Percent of what? What is the whole?", "Is your answer reasonable compared with a benchmark?", "Is this item taxed?", "Can a percent be more than 100? When?"],
 "misconceptions": ["Adding percents that refer to different wholes.", "Moving the decimal point the wrong way.", "Confusing finding the part with finding the whole.", "Thinking percents can never exceed 100."],
 "support": ["Keep a benchmark card: 50% = 1/2, 25% = 1/4, 10% = 1/10, 1% = 1/100.", "Use hundred grids for every conversion at first.", "Use a percent ratio table template."],
 "challenge": ["Find the tax rates in two other Florida counties and compare the tax on a $500 purchase.", "Show that finding 7.5% of $40 and finding 40% of $7.50 give the same answer, and explain why."],
 "background": "<p>Florida's state sales tax is 6%; county discretionary sales surtaxes bring combined rates to 6% to 8% (2026). DeSoto County's surtax is 1.5%, for a combined 7.5%. Most groceries and prescription drugs are exempt. Florida's permanent back-to-school sales tax holiday (HB 7031, 2025) runs every August 1 to 31 and exempts clothing and bags $100 or less, school supplies $50 or less, learning aids $30 or less and personal computers $1,500 or less. The rain item: P(rain at least one day) = 1 − 0.7 × 0.7 = 0.51 if the days are independent.</p>",
 "sources": ["Florida Department of Revenue, Sales and Use Tax; Discretionary Sales Surtax Information (DR-15DSS).", "Florida Department of Revenue, Back-to-School Sales Tax Holiday.", "CPALMS, MA.6.AR.3 benchmarks.", "Jump$tart Coalition, National Standards for Personal Financial Education."]
}

PRINT = {
 "directions": "Show your work.",
 "items": [
  {"q":"Write 65% as a decimal and as a fraction in simplest form.","a":"0.65; 13/20","lines":1},
  {"q":"Write 3/8 as a percent.","a":"37.5%","lines":1},
  {"q":"What is 30% of $90?","a":"$27","lines":1},
  {"q":"24 is 60% of what number?","a":"40","lines":2},
  {"q":"Find the tax and total on a $56 purchase at 7.5%.","a":"Tax $4.20; total $60.20","lines":2},
  {"q":"Lena scored 18 out of 24. Marco scored 22 out of 30. Who scored the higher percent?","a":"Lena 75%, Marco about 73.3%; Lena","lines":2}]
}
