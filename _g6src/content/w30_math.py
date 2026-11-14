TOOLKIT = ('<svg viewBox="0 0 640 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Unit 6 toolkit: area, surface area and volume, statistical questions and displays, measures of center and spread">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Unit 6 toolkit</text>'
  + ''.join(f'<g transform="translate({16+i*156},36)"><rect width="144" height="180" rx="12" fill="{c}"/><text x="72" y="24" text-anchor="middle" fill="#fff" font-weight="bold" font-size="12">{a}</text>'
            + ''.join(f'<text x="72" y="{50+j*18}" text-anchor="middle" fill="#fff" font-size="11">{t}</text>' for j, t in enumerate(lines)) + '</g>'
            for i, (a, c, lines) in enumerate([
              ("Week 26: Area", "#0A1F3D", ["rectangle: b × h", "parallelogram: b × h", "triangle: ½ × b × h", "composite: split into", "rectangles and triangles", "height is perpendicular"]),
              ("Week 27: Solids", "#0047BA", ["net: unfold the faces", "surface area: add the", "areas of every face", "volume: l × w × h", "square units vs.", "cubic units"]),
              ("Week 28: Data", "#2c6e22", ["statistical question:", "answers vary", "fair sample", "dot plot", "histogram: intervals", "center, spread, shape"]),
              ("Week 29: Summaries", "#DB2F30", ["mean, median, mode", "range and IQR", "box plot:", "min, Q1, median, Q3, max", "outliers pull the mean", "median resists them"])])) +
  '</svg>')

LESSON = {
 "unit": "Unit 6: Geometry and Data",
 "title": "End-of-Year Review",
 "subtitle": "You made it to Week 30. This week you pull together Unit 6 (area, surface area and volume, data displays and measures of center), review the money skills you built all year, plan a summer business with every tool you've learned, and then show your mastery on the Unit 6 checkpoint.",
 "objectives": [
  "Choose the right geometry tool: area, surface area or volume.",
  "Choose and interpret the right data display and measure of center or spread.",
  "Apply the year's money skills: unit prices, percents, integers, interest and budgets.",
  "Plan a real summer business using math from all six units.",
  "Demonstrate mastery of Unit 6 on the checkpoint (85 or higher)."],
 "vocab": [
  ["area", "The number of square units that cover a flat figure."],
  ["surface area", "The total area of all the faces of a solid."],
  ["volume", "The number of cubic units that fill a solid."],
  ["statistical question", "A question that expects answers that vary."],
  ["measure of center", "One number that describes a typical value: the mean, median or mode."],
  ["interquartile range (IQR)", "Q3 minus Q1: the spread of the middle half of the data."]],
 "reconnect": {
  "title": "Unit 6, one question from each week",
  "intro": "Warm up with one question from each week of the unit.",
  "items": [
   {"t":"num","q":"Week 26: A triangle has a base of 10 inches and a height of 7 inches. What is its area?","a":35,"unit":"square inches","pts":2,"why":"½ × 10 × 7 = 35."},
   {"t":"num","q":"Week 27: What is the volume of a box 4 cm long, 3 cm wide and 5 cm tall?","a":60,"unit":"cubic centimeters","pts":2,"why":"4 × 3 × 5 = 60."},
   {"t":"text","q":"Week 28: You asked 30 people their ages and want to group the ages into intervals of 10 years. What display should you use?","a":[{"all":[["histogram"]],"none":["not"]}],"show":"a histogram","pts":2,"why":"Histograms group data into equal intervals."},
   {"t":"num","q":"Week 29: Find the median of 4, 9, 2, 7, 5.","a":5,"pts":2,"why":"In order: 2, 4, 5, 7, 9."}]},
 "hook": {
  "title": "Planning a Summer Business",
  "visual": TOOLKIT,
  "html": "<p>Summer is coming, and you and a sibling or friend want to run a small business: a lemonade stand, a bake sale table, a pet-sitting service or a craft booth at the farmers market. A real business plan uses every unit of math you learned this year: decimals and unit prices for supplies, ratios for recipes, percents for discounts and profit, integers for money owed, equations for prices, area for your sign, volume for your cooler and data for your customers.</p><div class='callout'><b>Big question:</b> How do I choose the right math tool for a real problem?</div>"},
 "learn": [
  {"title": "Review: Area",
   "html": "<p>Area counts square units. Rectangle and parallelogram: <b>A = b × h</b>. Triangle: <b>A = ½ × b × h</b>, because every triangle is half of a parallelogram. The height is always <b>perpendicular</b> to the base. For a composite figure, split it into rectangles and triangles, find each area and add (or subtract a missing piece).</p>",
   "checks": [
    {"t":"num","q":"A parallelogram-shaped garden bed has a base of 12 feet and a height of 5 feet. What is its area?","a":60,"unit":"square feet","pts":2,"why":"12 × 5 = 60."},
    {"t":"num","q":"A stand's sign is a 10-inch by 6-inch rectangle with a triangle on top that has a 6-inch base and a 4-inch height. What is the sign's total area?","a":72,"unit":"square inches","pts":2,"why":"60 + ½ × 6 × 4 = 60 + 12 = 72."}]},
  {"title": "Review: Surface Area and Volume",
   "html": "<p>A <b>net</b> unfolds a solid into flat faces. <b>Surface area</b> adds the areas of all faces (square units): use it for wrapping, painting or labeling. <b>Volume</b> = l × w × h for a rectangular prism (cubic units): use it for filling or packing. Lengths can be fractions or decimals.</p>",
   "checks": [
    {"t":"num","q":"A gift box is 6 inches long, 4 inches wide and 2 inches tall. How much wrapping paper covers it exactly (its surface area)?","a":88,"unit":"square inches","pts":2,"why":"2(24 + 12 + 8) = 88."},
    {"t":"num","q":"A cooler is 2.5 feet long, 2 feet wide and 1.5 feet tall. What is its volume?","a":7.5,"tol":0.001,"unit":"cubic feet","pts":2,"why":"2.5 × 2 × 1.5 = 7.5."},
    {"t":"open","key":"savchoose","q":"For each job, tell whether you need area, surface area or volume, and why: (a) painting a wooden toy chest, (b) filling a sandbox, (c) buying carpet for a bedroom.","min":20,"rows":3,"rubric":["A correct choice for each job","A reason for each choice"],"model":"(a) Surface area, because paint covers every face of the chest. (b) Volume, because sand fills the space inside. (c) Area, because carpet covers one flat floor."}]},
  {"title": "Review: Data",
   "html": "<p>Start with a <b>statistical question</b> and a <b>fair sample</b>. Display the data with a <b>dot plot</b> (few values) or a <b>histogram</b> (intervals). Summarize with a <b>measure of center</b> and a <b>measure of spread</b>. When there are outliers, the <b>median</b> and <b>IQR</b> describe the data better than the mean and range. A <b>box plot</b> shows the five-number summary.</p>",
   "checks": [
    {"t":"num","q":"Lemonade cups sold each day: 3, 5, 5, 6, 8, 9, 20. Find the mean.","a":8,"unit":"cups","pts":2,"why":"56 ÷ 7 = 8."},
    {"t":"num","q":"Find the median of the same data.","a":6,"unit":"cups","pts":2,"why":"The 4th of 7 values."},
    {"t":"open","key":"typicalday","q":"Which number better describes a typical day at the stand, the mean or the median? Explain.","min":15,"rows":2,"rubric":["Chooses a measure","Justifies it using the outlier"],"model":"The median, 6 cups, because the 20-cup day (maybe a holiday) is an outlier that pulls the mean up to 8."}]},
  {"title": "Money: End-of-Year Money Review",
   "html": "<p>All year you've built money skills. Here they are in one place:</p><ul><li><b>Unit price</b> (Units 1 and 3): divide price by quantity to find the better buy.</li><li><b>Ratios</b> (Unit 2): scale a recipe up or down.</li><li><b>Percents</b> (Unit 3): discounts, sales tax, tips and markups.</li><li><b>Integers</b> (Unit 4): money owed is negative; deposits are positive.</li><li><b>Interest and budgets</b> (Unit 5): I = P × r × t; inequalities keep spending within a limit.</li><li><b>Data</b> (Unit 6): survey customers and compare prices with the median.</li></ul>",
   "checks": [
    {"t":"num","q":"A 12-ounce bag of lemons costs $3.60, and an 18-ounce bag costs $4.86. What is the unit price of the better buy, in dollars per ounce?","a":0.27,"tol":0.001,"unit":"dollars per ounce","pts":2,"why":"3.60 ÷ 12 = 0.30; 4.86 ÷ 18 = 0.27; the 18-ounce bag is cheaper per ounce."},
    {"t":"num","q":"A $24 shirt is 25% off, and then 6% sales tax is added. What is the final price?","a":19.08,"tol":0.001,"unit":"dollars","pts":2,"why":"24 × 0.75 = 18; 18 × 1.06 = 19.08."},
    {"t":"num","q":"Your business owes your parents $15 for supplies (−15). Then you earn $40. What is your balance now?","a":25,"unit":"dollars","pts":2,"why":"−15 + 40 = 25."},
    {"t":"open","key":"profitplan","q":"Your lemonade recipe makes 8 cups for $2.40 in supplies. You plan to sell each cup for $0.75. Find your cost per cup, your profit per cup and how many cups you must sell to earn $27 in profit. Show your work.","min":25,"rows":3,"rubric":["Correct cost per cup","Correct profit per cup","Correct number of cups with an equation or explanation"],"model":"Cost per cup: 2.40 ÷ 8 = $0.30. Profit per cup: 0.75 − 0.30 = $0.45. Cups needed: 0.45c = 27, so c = 27 ÷ 0.45 = 60 cups."}]}],
 "handson": {
  "title": "Summer Business Plan",
  "intro": "Plan a real summer business, using at least one skill from each unit of the year.",
  "materials": ["Paper and pencil", "Graph paper and a ruler", "A measuring tape", "Grocery flyers or store websites (with a parent)", "A calculator for checking (optional)", "A family member", "At least 10 family members or friends to survey (a parent approves)"],
  "steps": [
   "Choose a business: a lemonade stand, bake sale table, pet-sitting service, craft booth or another idea your parent approves.",
   "Supplies (Units 1 to 3): list your supplies and find each unit price from flyers or websites. Use a ratio to scale one recipe or supply list for your expected customers.",
   "Pricing (Units 3 and 5): set a price, find your profit per item, and write and solve an equation for how many items you must sell to reach a goal.",
   "Space (Unit 6): measure your table, booth or sign with the measuring tape. Find the area of a sign and the volume of a cooler or storage box.",
   "Customers (Unit 6): ask at least 10 family members or friends a statistical question about your product, such as what price they'd pay, and find the median and range.",
   "Run any real business only with a parent's permission and supervision. Handle food only with clean hands, and never sell to or collect personal information from strangers without an adult."],
  "record": [
   {"t":"open","key":"planrec","q":"Share your business plan: supplies with unit prices, your price and profit per item, your sales-goal equation, one area or volume measurement and your survey results.","min":56,"rows":6,"rubric":["Supplies with correct unit prices","A price, profit per item and solved goal equation","An area or volume measurement with units","Survey results with a median and range"],"model":"Lemonade stand. Supplies: lemons $0.27 per ounce, sugar $0.05 per ounce, cups $0.06 each; one batch makes 8 cups for $2.40. Price $0.75; profit $0.45 per cup. Goal $45: 0.45c = 45, so c = 100 cups. Sign: 24 in by 18 in = 432 square inches. Cooler: 2.5 × 2 × 1.5 = 7.5 cubic feet. Survey of 12 people: median price $0.75, range $0.75."},
   {"t":"open","key":"planreflect","q":"Which unit's math was most useful for your plan, and what would you change after seeing your survey results?","min":30,"rows":3,"rubric":["Names a unit with a reason","A change based on the survey data"],"model":"Unit 3's percents and unit prices were most useful, because they decided whether I'd make a profit. My survey's median was $0.75, but three people would pay $1, so I might sell a large cup for $1."}]},
 "think": {
  "intro": "Your teacher scores this.",
  "items": [
   {"t":"open","key":"yearreflect","q":"Look back over the whole year: decimals, fractions and ratios, rates and percents, integers, expressions and equations, geometry and data. Which idea will you use most as an adult, and which was hardest for you? Give a real example for each and explain how you worked through the hard one.","min":57,"rows":6,"rubric":["Names an idea likely to be used as an adult, with a real example","Names the hardest idea, with an example","Explains a strategy that helped"],"model":"I'll use percents most, because every store sale, tip and loan uses them; at a restaurant I can find a 20% tip by taking 10% and doubling it. The hardest was dividing fractions. A $12 roll of ribbon cut into 3/4-yard pieces confused me until I drew the yards and counted the pieces, which showed me why dividing by 3/4 gives more pieces than the number of yards."}]},
 "checkpoint": {
  "title": "Unit 6 Checkpoint: Geometry and Data",
  "intro": "This checkpoint covers Weeks 26 to 29. Work each problem on paper, then type your answer. Type only the number for numeric answers. Mastery is 85 or higher. If you score below 85, your teacher will review with you, then you will retake it.",
  "parts": [
   {"title": "Part A: Area", "items": [
    {"t":"num","q":"A triangle has a base of 14 cm and a height of 9 cm. What is its area?","a":63,"unit":"square centimeters","pts":3,"why":"½ × 14 × 9 = 63."},
    {"t":"num","q":"A parallelogram has a base of 8.5 m and a height of 6 m. What is its area?","a":51,"unit":"square meters","pts":3,"why":"8.5 × 6 = 51."},
    {"t":"num","q":"A shed wall is a 12-foot by 8-foot rectangle with a triangle on top that has a 12-foot base and a 5-foot height. What is the wall's total area?","a":126,"unit":"square feet","pts":3,"why":"96 + 30 = 126."},
    {"t":"open","key":"cptriangle","q":"Explain why the area of a triangle is ½ × base × height. Use a sketch described in words or a rectangle or parallelogram in your explanation.","min":20,"rows":3,"pts":4,"rubric":["Relates the triangle to a rectangle or parallelogram with the same base and height","Explains why the triangle is half of it"],"model":"Two copies of the same triangle fit together to make a parallelogram with the same base and height. The parallelogram's area is base × height, so one triangle is half of that: ½ × base × height."}]},
   {"title": "Part B: Surface area and volume", "items": [
    {"t":"num","q":"Find the surface area of a rectangular prism 5 in long, 4 in wide and 3 in tall.","a":94,"unit":"square inches","pts":3,"why":"2(20 + 15 + 12) = 94."},
    {"t":"num","q":"Find the volume of a box 2.5 ft long, 4 ft wide and 6 ft tall.","a":60,"unit":"cubic feet","pts":3,"why":"2.5 × 4 × 6 = 60."},
    {"t":"num","q":"A cube has edges ½ foot long. What is its volume? Type a decimal.","a":0.125,"tol":0.0001,"unit":"cubic feet","pts":3,"why":"½ × ½ × ½ = ⅛ = 0.125."},
    {"t":"blanks","q":"A net of a square pyramid has how many squares and how many triangles?","sent":"Squares: ___ &nbsp; Triangles: ___","blanks":[["^1","^one"],["^4","^four"]],"show":"1; 4","pts":3,"why":"One square base and four triangular faces."},
    {"t":"open","key":"cpship","q":"A shipping box is 12 inches long, 10 inches wide and 8 inches tall. You want to cover it completely in decorative paper. Tell whether you need surface area or volume, explain why, and find the amount.","min":20,"rows":3,"pts":4,"rubric":["Chooses the correct measurement with a reason","Correct calculation with square units"],"model":"Surface area, because the paper covers the outside faces. SA = 2(12 × 10 + 12 × 8 + 10 × 8) = 2(120 + 96 + 80) = 2(296) = 592 square inches."}]},
   {"title": "Part C: Statistical questions and displays", "items": [
    {"t":"open","key":"cpstatq","q":"\"How tall am I?\" is not a statistical question. Rewrite it so it is one, and explain what makes your new question statistical.","min":15,"rows":2,"pts":3,"rubric":["A rewritten question that expects varied answers","Explains variability"],"model":"\"How tall are the students in my co-op?\" It's statistical because the students have different heights, so the answers vary."},
    {"t":"num","q":"A histogram shows books read this year by 20 students: 0 to 4 books: 3 students; 5 to 9: 7; 10 to 14: 6; 15 to 19: 4. How many students read 10 or more books?","a":10,"unit":"students","pts":3,"why":"6 + 4 = 10."},
    {"t":"num","q":"Using the same histogram, what percent of the students read fewer than 5 books?","a":15,"unit":"percent","pts":3,"why":"3 ÷ 20 = 0.15 = 15%."},
    {"t":"open","key":"cpbias","q":"To find the town's favorite sport, a student surveys only players at a soccer camp. Explain why the results may be biased and describe a fairer sample.","min":25,"rows":3,"pts":4,"rubric":["Explains the bias","Describes a fairer sample"],"model":"Soccer campers probably like soccer more than most people, so the results would favor soccer. A fairer sample would be people chosen at random from all over town, like every fifth shopper at the library and the grocery store."}]},
   {"title": "Part D: Measures of center and spread", "items": [
    {"t":"num","q":"Find the mean of 12, 15, 9, 18, 16.","a":14,"pts":3,"why":"70 ÷ 5 = 14."},
    {"t":"num","q":"Find the median of 7, 3, 10, 4, 8, 12.","a":7.5,"tol":0.001,"pts":3,"why":"In order: 3, 4, 7, 8, 10, 12; (7 + 8) ÷ 2 = 7.5."},
    {"t":"num","q":"Find the interquartile range of 2, 5, 6, 8, 10, 13, 15.","a":8,"pts":3,"why":"Median 8; Q1 = 5; Q3 = 13; 13 − 5 = 8."},
    {"t":"open","key":"cphouses","q":"Five houses on a street sold for $250,000, $260,000, $270,000, $280,000 and $1,400,000. Find the mean and median, and explain which better describes a typical house on the street.","min":25,"rows":3,"pts":4,"rubric":["Correct mean","Correct median","Chooses a measure and justifies it with the outlier"],"model":"Mean: 2,460,000 ÷ 5 = $492,000. Median: $270,000. The median is better, because the $1,400,000 house is an outlier that pulls the mean above what four of the five houses sold for."}]}]},
 "next": "Congratulations on finishing Grade 6! Next: the end-of-year comprehensive mastery test."
}

TEACHER = {
 "standards": [
  "MA.6.GR.2.1: Derive a formula for the area of a right triangle using a rectangle. Apply a formula to find the area of a triangle.",
  "MA.6.GR.2.2: Solve mathematical and real-world problems involving the area of quadrilaterals and composite figures by decomposing them into triangles or rectangles.",
  "MA.6.GR.2.3: Solve mathematical and real-world problems involving the volume of right rectangular prisms with positive rational number edge lengths using a visual model and a formula.",
  "MA.6.GR.2.4: Given a mathematical or real-world context, find the surface area of right rectangular prisms and right rectangular pyramids using the figure's net.",
  "MA.6.DP.1.1: Recognize and formulate a statistical question that would generate numerical data.",
  "MA.6.DP.1.2: Given a numerical data set within a real-world context, find and interpret mean, median, mode and range.",
  "MA.6.DP.1.3: Given a box plot within a real-world context, determine the minimum, the lower quartile, the median, the upper quartile and the maximum. Use this summary of the data to describe the spread and distribution of the data.",
  "MA.6.DP.1.5: Create box plots and histograms to represent sets of numerical data within real-world contexts.",
  "MA.6.DP.1.6: Given a real-world scenario, determine and describe how changes in data values impact measures of center and variation.",
  "Financial literacy: spending, saving, budgeting and earning income (Jump$tart National Standards)."],
 "materials": ["The interactive lesson", "Paper and pencil, graph paper and a ruler, a measuring tape, grocery flyers or store websites, optional calculator", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run one question from each week of the unit."],
  [4, "Hook", "The summer business and the toolkit chart."],
  [8, "Area", "Parallelogram bed; composite sign."],
  [8, "Surface area and volume", "Gift box, cooler; which measure for which job."],
  [8, "Data", "Lemonade cups: mean versus median."],
  [11, "Year-end money review", "Unit price, discount and tax, integers, profit equation."],
  [5, "Assign", "Set up the summer business plan; assign Think Deeper."],
  [10, "Checkpoint preview", "Explain that the checkpoint is completed after class, independently, one try per item, with no answers shown until you review it. Mastery is 85; below 85 means a review lesson and a retake. Remind the family that the end-of-year comprehensive mastery test follows this week."]],
 "key_questions": ["Am I covering, wrapping or filling?", "Is the height perpendicular to the base?", "Is there an outlier, and which measure handles it?", "Which unit of the year does this money problem use?"],
 "misconceptions": ["Surface area and volume use the same units.", "The slanted side of a triangle is its height.", "The mean is always the best measure of center.", "A percent off and then tax on can be found by subtracting the percents."],
 "support": ["Provide the toolkit chart as a reference card.", "Use centimeter cubes or sugar cubes to rebuild volume.", "Give a template for the business plan with one box per unit."],
 "challenge": ["Compare the surface areas of two boxes with the same volume and decide which uses less cardboard.", "Find the mean absolute deviation for the lemonade data."],
 "background": "<p>The Unit 6 checkpoint covers Weeks 26 to 29; the end-of-year comprehensive mastery test (per the scope, after Week 30) is separate. The money review spirals the year's financial-literacy thread. Verify MA.6.GR.2.1 to 2.4 and DP.1.1 to 1.6 wording against CPALMS before release.</p>",
 "sources": ["Florida Department of Education, B.E.S.T. Standards for Mathematics (2020).", "Jump$tart Coalition, National Standards for Personal Financial Education (2021)."]
}

PRINT = {
 "directions": "Show your work.",
 "items": [
  {"q":"Find the area of a triangle with base 18 m and height 7 m.","a":"63 square meters.","lines":2},
  {"q":"Find the surface area and volume of a box 8 cm by 5 cm by 3 cm.","a":"SA = 2(40 + 24 + 15) = 158 square cm; V = 120 cubic cm.","lines":3},
  {"q":"Data: 4, 6, 6, 7, 9, 10, 35. Find the mean, median and mode. Which measure best describes the data?","a":"Mean 11; median 7; mode 6; median, because 35 is an outlier.","lines":3},
  {"q":"Find the five-number summary of 1, 3, 4, 6, 7, 9, 12.","a":"1, 3, 6, 9, 12.","lines":2},
  {"q":"A $40 jacket is 30% off, with 7% sales tax added. Find the final price.","a":"40 × 0.70 = 28; 28 × 1.07 = $29.96.","lines":2}]
}
