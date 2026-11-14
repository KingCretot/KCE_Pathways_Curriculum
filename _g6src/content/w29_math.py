BOX = ('<svg viewBox="0 0 660 200" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Box plot of sourdough loaf prices at 11 bakeries: minimum 6, first quartile 7, median 8, third quartile 10, maximum 14">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Box plot: price of a sourdough loaf at 11 bakeries</text>'
  '<path d="M60 150 H620" stroke="#0A1F3D" stroke-width="2"/>'
  + ''.join(f'<path d="M{60+(p-5)*56} 145 v10" stroke="#0A1F3D" stroke-width="2"/><text x="{60+(p-5)*56}" y="172" text-anchor="middle" fill="#0A1F3D">${p}</text>' for p in range(5, 16)) +
  '<path d="M116 90 H172 M340 90 H508" stroke="#0A1F3D" stroke-width="2"/><path d="M116 76 V104 M508 76 V104" stroke="#0A1F3D" stroke-width="2"/>'
  '<rect x="172" y="66" width="168" height="48" fill="#C9A84C" fill-opacity="0.45" stroke="#8a6d1f" stroke-width="2"/><path d="M228 66 V114" stroke="#DB2F30" stroke-width="3"/>'
  '<text x="116" y="62" text-anchor="middle" fill="#0A1F3D" font-size="11">min $6</text><text x="172" y="128" text-anchor="middle" fill="#0A1F3D" font-size="11">Q1 $7</text><text x="228" y="58" text-anchor="middle" fill="#DB2F30" font-size="11" font-weight="bold">median $8</text><text x="340" y="128" text-anchor="middle" fill="#0A1F3D" font-size="11">Q3 $10</text><text x="508" y="62" text-anchor="middle" fill="#0A1F3D" font-size="11">max $14</text>'
  '<text x="330" y="192" text-anchor="middle" fill="#5b6676" font-size="11">The box holds the middle half of the prices; each whisker holds about a quarter.</text></svg>')

LESSON = {
 "unit": "Unit 6: Geometry and Data",
 "title": "Mean, Median, Mode and Range",
 "subtitle": "What's a fair price for a loaf of sourdough? What's a typical score? Last week you displayed data; this week you summarize it with one number for the center and one for the spread. You'll find the mean, median, mode and range, build a box plot, see how one extreme value can mislead, and use averages to compare prices like a smart shopper and business owner.",
 "objectives": [
  "Find the mean, median and mode of a data set and explain what each tells you.",
  "Find the range and interquartile range to describe spread.",
  "Create and interpret a box plot using the five-number summary.",
  "Explain how an outlier affects the mean and median, and choose the best measure of center.",
  "Compare prices and data sets using measures of center and spread."],
 "vocab": [
  ["mean", "The sum of the values divided by the number of values; the average."],
  ["median", "The middle value when the data are in order (or the mean of the two middle values)."],
  ["mode", "The value that appears most often (a data set may have no mode or more than one)."],
  ["range", "The difference between the greatest and least values."],
  ["outlier", "A value much greater or much less than the rest of the data."],
  ["interquartile range (IQR)", "The range of the middle half of the data: the third quartile minus the first quartile."],
  ["box plot", "A display showing the minimum, first quartile, median, third quartile and maximum."]],
 "reconnect": {
  "title": "Week 28: Data displays",
  "intro": "Last week you drew data. This week you summarize it.",
  "items": [
   {"t":"open","key":"rc_statq","q":"Write one statistical question about your homeschool or family.","min":6,"rows":2,"rubric":["A question that expects many different answers from a group"],"model":"How many minutes do the kids in my co-op read each day?"},
   {"t":"text","q":"What display groups data into equal intervals, with bars that touch?","a":[{"all":[["histogram"]],"none":["not"]}],"show":"a histogram","pts":2,"why":"For many different values."},
   {"t":"open","key":"rc_center","q":"Last week you described where data \"cluster.\" Why might it be useful to describe that center with a single number?","min":12,"rows":2,"rubric":["Explains that one number summarizes and makes comparison easy"],"model":"One number makes it easy to summarize the data and compare it with another group, like saying a typical customer buys 3 loaves."}]},
 "hook": {
  "title": "What's a Fair Price?",
  "visual": BOX,
  "html": "<p>Maya is setting the price of her sourdough. She checks 11 bakeries in her area: $6, $7, $7, $7.50, $8, $8, $8.50, $9.50, $10, $11 and $14 (a fancy downtown shop). What's a \"typical\" price? The average comes out to about $8.77, but the middle price is $8, and the most common is $7.</p><p>Three different answers! Each is a different <b>measure of center</b>, and choosing the right one matters, especially when one bakery charges $14.</p><div class='callout'><b>Big question:</b> How can one or two numbers describe a whole data set, and how can they mislead?</div>"},
 "learn": [
  {"title": "Mean, Median and Mode",
   "html": "<ul><li><b>Mean:</b> add all values and divide by how many. Bakery prices: 96.50 ÷ 11 ≈ $8.77. The mean is the \"fair share\" amount if everything were evened out.</li><li><b>Median:</b> put the values in order and find the middle. With 11 prices, the 6th is the middle: $8. With an even number of values, find the mean of the two middle ones.</li><li><b>Mode:</b> the most frequent value: $7 (it appears twice, as does $8; this set has two modes, $7 and $8).</li></ul>",
   "checks": [
    {"t":"num","q":"Find the mean of these quiz scores: 82, 90, 76, 88, 94.","a":86,"pts":2,"why":"430 ÷ 5 = 86."},
    {"t":"num","q":"Find the median of these hours of sleep: 9, 7, 8, 10, 8, 9.","a":8.5,"tol":0.001,"unit":"hours","pts":2,"why":"In order: 7, 8, 8, 9, 9, 10; middle two are 8 and 9; (8 + 9) ÷ 2 = 8.5."},
    {"t":"num","q":"Find the mode of these shoe sizes: 6, 7, 7, 8, 7, 9, 6.","a":7,"pts":2,"why":"7 appears three times."}]},
  {"title": "Spread: Range and Interquartile Range",
   "html": "<p>Two data sets can have the same center but different spreads. The <b>range</b> (greatest minus least) is quick but depends only on the two extremes: bakery range = $14 − $6 = $8.</p><p>The <b>interquartile range (IQR)</b> measures the spread of the middle half. Split the ordered data at the median; the median of the lower half is the <b>first quartile (Q1)</b> and of the upper half the <b>third quartile (Q3)</b>. Bakery lower half: 6, 7, 7, 7.50, 8, so Q1 = $7. Upper half: 8.50, 9.50, 10, 11, 14, so Q3 = $10. IQR = 10 − 7 = $3.</p>",
   "checks": [
    {"t":"num","q":"Find the range of these daily high temperatures: 88, 91, 85, 94, 90.","a":9,"unit":"degrees","pts":2,"why":"94 − 85 = 9."},
    {"t":"open","key":"samecenter","q":"Two homeschool families each read a median of 30 minutes a day. Family A's times range from 25 to 35 minutes; Family B's range from 0 to 90. Describe how their reading habits differ.","min":20,"rows":2,"rubric":["Uses spread to compare","Describes consistency versus variability"],"model":"Both read about 30 minutes on a typical day, but Family A is very consistent, always 25 to 35 minutes, while Family B varies wildly, from not reading at all to an hour and a half."}]},
  {"title": "Box Plots",
   "html": "<p>A <b>box plot</b> shows the <b>five-number summary</b>: minimum, Q1, median, Q3 and maximum. The box stretches from Q1 to Q3 (the middle half), a line marks the median, and whiskers reach to the minimum and maximum.</p><p>Box plots make it easy to compare groups and spot skew. In the bakery box plot, the right whisker is long because of the $14 shop.</p><p><i>Note: calculators and apps sometimes use slightly different methods for quartiles, so their answers can differ a little.</i></p>",
   "checks": [
    {"t":"blanks","q":"Find the five-number summary of: 2, 4, 5, 7, 8, 9, 12.","sent":"Min: ___ &nbsp; Q1: ___ &nbsp; Median: ___ &nbsp; Q3: ___ &nbsp; Max: ___","blanks":[["^2"],["^4"],["^7"],["^9"],["^12"]],"show":"2; 4; 7; 9; 12","pts":3,"why":"Median 7; lower half 2, 4, 5 (Q1 4); upper half 8, 9, 12 (Q3 9)."},
    {"t":"open","key":"readbox","q":"A box plot of game scores has a median of 15, Q1 of 10, Q3 of 18 and whiskers from 4 to 30. What fraction of scores were between 10 and 18, and what does the long right whisker suggest?","min":20,"rows":2,"rubric":["About half the scores","Explains that a few scores were much higher"],"model":"About half of the scores were between 10 and 18. The long right whisker means a few games had much higher scores than usual, up to 30."}]},
  {"title": "Outliers and Choosing a Measure; Money: Comparing Prices",
   "html": "<p>An <b>outlier</b> pulls the mean toward it but barely moves the median. Without the $14 shop, the mean price drops from $8.77 to $8.25, but the median stays at $8.</p><ul><li>Use the <b>median</b> when there are outliers or the data are lopsided (house prices, incomes, the bakery prices).</li><li>Use the <b>mean</b> when data are fairly balanced with no outliers (test scores in a consistent class).</li><li>Use the <b>mode</b> for the most popular choice (the most-ordered flavor or T-shirt size).</li></ul><p>Smart shoppers use averages too. A unit price below the median means a good deal; a price far above the median is an outlier you may want to skip.</p>",
   "checks": [
    {"t":"num","q":"Five friends earn weekly allowances of $10, $12, $10, $15 and $53. Find the mean.","a":20,"unit":"dollars","pts":2,"why":"100 ÷ 5 = 20."},
    {"t":"num","q":"Find the median of the same allowances.","a":12,"unit":"dollars","pts":2,"why":"In order: 10, 10, 12, 15, 53."},
    {"t":"open","key":"bestmeasure","q":"For the allowances above, which measure gives a fairer picture of a \"typical\" allowance, the mean or the median? Explain.","min":20,"rows":2,"rubric":["Chooses a measure","Justifies it using the outlier"],"model":"The median, $12, is fairer. The $53 allowance is an outlier that pulls the mean up to $20, which is more than four of the five friends actually get."},
    {"t":"open","key":"mayaprice","q":"Using the bakery data, recommend a price for Maya's sourdough. Use at least two measures (center or spread) in your reasoning.","min":30,"rows":3,"rubric":["A specific price","Uses at least two measures correctly","Considers the outlier or business factors"],"model":"I'd charge $8. That's the median, so half the bakeries charge less and half charge more, and it's inside the middle half of prices ($7 to $10). The mean of $8.77 is pulled up by the $14 shop, so it overstates what most customers expect to pay."}]}],
 "handson": {
  "title": "Price Detectives",
  "intro": "Collect real prices for one product, summarize them and decide on the best buy.",
  "materials": ["Grocery flyers, store websites or a store visit (with a parent)", "Paper and pencil", "Graph paper and a ruler", "A calculator for checking (optional)", "A family member"],
  "steps": [
   "Choose one product your family buys often (a gallon of milk, a loaf of bread, a box of cereal, a dozen eggs). Make sure you compare the same size.",
   "Find at least 9 prices from different stores or brands. Record them in a list.",
   "Put the prices in order and find the mean, median, mode, range, Q1, Q3 and IQR.",
   "Draw a box plot of the prices on graph paper.",
   "Identify any outlier and decide which measure of center best describes a typical price. Recommend where your family should buy it.",
   "Visit stores only with a parent, and don't open or handle products you're not buying."],
  "record": [
   {"t":"open","key":"pricerec","q":"List your prices and show your mean, median, mode, range and IQR. Was there an outlier?","min":32,"rows":5,"rubric":["At least 9 prices","Correct calculations","Identifies whether there is an outlier"],"model":"Gallon of milk: $3.19, $3.29, $3.49, $3.49, $3.59, $3.79, $3.99, $4.29, $6.49 (organic). Mean: 35.61 ÷ 9 ≈ $3.96. Median: $3.59. Mode: $3.49. Range: $3.30. Q1: $3.39, Q3: $4.14, IQR: $0.75. The $6.49 organic milk is an outlier."},
   {"t":"open","key":"buyrec","q":"Which measure best describes a typical price for your product, and where should your family buy it? Explain with your box plot.","min":30,"rows":3,"rubric":["Chooses a measure with a reason","A recommendation based on the data","Refers to the box plot"],"model":"The median, $3.59, is best because the $6.49 organic milk pulls the mean up. My box plot shows most prices between $3.39 and $4.14. I'd recommend the $3.19 store, which is below Q1, as long as it's convenient."}]},
 "think": {
  "intro": "Explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"misleadavg","q":"A real estate ad says, \"The average home price in our neighborhood is $650,000!\" but most homes sell for around $300,000. Explain how this can be true and why the ad might use the mean instead of the median.","min":40,"rows":4,"rubric":["Explains how a few very expensive homes raise the mean","Explains the seller's motive","Connects to judging sources (Week 27 ELA)"],"model":"A few mansions worth millions can pull the mean far above what most homes cost, while the median would stay near $300,000. A seller might report the mean to make the neighborhood sound more valuable. Like we learned in ELA, always ask who made a claim and why."},
   {"t":"open","key":"makedata","q":"Create a data set of 7 numbers with a mean of 10, a median of 8 and a mode of 6. Show that it works and explain your strategy.","min":40,"rows":4,"rubric":["A correct data set meeting all three conditions","Shows the checks","Explains the strategy"],"model":"6, 6, 6, 8, 12, 16, 16. Sum is 70, so the mean is 70 ÷ 7 = 10; the middle value is 8; 6 appears three times, the most. I started with the median in the middle and three 6s, then chose large numbers to raise the total to 70."}]},
 "exit": [
  {"t":"num","q":"Find the mean of 4, 7, 9, 10, 15.","a":9,"pts":2,"why":"45 ÷ 5 = 9."},
  {"t":"num","q":"Find the median of 3, 8, 1, 6, 9, 4.","a":5,"pts":2,"why":"In order: 1, 3, 4, 6, 8, 9; (4 + 6) ÷ 2 = 5."},
  {"t":"num","q":"Find the range of 12, 5, 19, 8, 14.","a":14,"pts":2,"why":"19 − 5 = 14."},
  {"t":"open","key":"exit_outlier","q":"Which measure of center is least affected by an outlier, and why?","min":10,"rows":2,"rubric":["Names the median","Explains why"],"model":"The median, because it depends only on the middle value, not on how extreme the largest or smallest values are."}],
 "next": "Week 30: end-of-year review."
}

TEACHER = {
 "standards": [
  "MA.6.DP.1.2: Given a numerical data set within a real-world context, find and interpret mean, median, mode and range.",
  "MA.6.DP.1.3: Given a box plot within a real-world context, determine the minimum, the lower quartile, the median, the upper quartile and maximum. Use this summary of the data to describe the spread and distribution of the data.",
  "MA.6.DP.1.4: Given a histogram or line plot within a real-world context, qualitatively describe and interpret the spread and distribution of the data, including any symmetry, skewness, gaps, clusters, outliers and the range.",
  "MA.6.DP.1.6: Given a real-world scenario, determine and describe how changes in data values impact measures of center and variation.",
  "Financial literacy: comparing prices to make spending decisions (Jump$tart Spending and Saving)."],
 "materials": ["The interactive lesson", "Grocery flyers or store websites, paper and pencil, graph paper and a ruler, optional calculator", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 28 warm-up questions."],
  [4, "Hook", "Maya's bakery prices: three different answers."],
  [11, "Mean, median, mode", "Compute each; even and odd counts."],
  [10, "Range and IQR", "Same center, different spread."],
  [11, "Box plots", "Five-number summary; read a box plot."],
  [12, "Outliers and prices", "Allowances; choose a measure; set Maya's price."],
  [6, "Assign", "Set up price detectives; assign Think Deeper and the Exit Check."]],
 "key_questions": ["Is there an outlier, and how does it affect the mean?", "Which measure best describes a typical value here?", "How spread out are the data?", "What does the box plot tell you at a glance?"],
 "misconceptions": ["The median is the middle of the unordered list.", "The mean is always the best average.", "Range tells you everything about spread.", "A data set must have exactly one mode."],
 "support": ["Have students write data in order on sticky notes and physically find the middle.", "Provide a five-number summary template.", "Use small data sets with whole numbers first."],
 "challenge": ["Compute the mean absolute deviation for the bakery prices.", "Compare box plots of prices at two different stores and decide which is more consistent."],
 "background": "<p>Quartile methods vary; this lesson uses the halves method that excludes the median for odd counts. With that method the bakery quartiles are $7 and $10. Verify MA.6.DP.1.2 to 1.6 wording against CPALMS. Prices are practice figures except in the hands-on.</p>",
 "sources": ["Florida Department of Education, B.E.S.T. Standards for Mathematics (2020).", "American Statistical Association, GAISE II (2020)."]
}

PRINT = {
 "directions": "Show your work.",
 "items": [
  {"q":"Find the mean, median, mode and range: 5, 8, 8, 10, 12, 15.","a":"Mean 58 ÷ 6 ≈ 9.67; median 9; mode 8; range 10.","lines":3},
  {"q":"Find the five-number summary and IQR: 3, 6, 7, 9, 11, 14, 20.","a":"3, 6, 9, 14, 20; IQR 8.","lines":3},
  {"q":"Test scores: 88, 92, 85, 90, 40. Find the mean and median. Which better describes a typical score?","a":"Mean 79; median 88; median, because 40 is an outlier.","lines":3},
  {"q":"Which measure would you use for the most popular shirt size in a class? Why?","a":"The mode, because it shows the most common choice.","lines":2},
  {"q":"Eight stores sell the same cereal for $3.99, $4.29, $3.79, $4.49, $3.99, $5.99, $4.19, $3.89. Find the median price.","a":"In order: 3.79, 3.89, 3.99, 3.99, 4.19, 4.29, 4.49, 5.99; median (3.99 + 4.19) ÷ 2 = $4.09.","lines":2}]
}
