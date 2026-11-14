DOTPLOT = ('<svg viewBox="0 0 660 220" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Dot plot of how many loaves 20 customers bought per month, from 0 to 6">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Dot plot: loaves bought per month by 20 customers</text>'
  '<path d="M80 170 H580" stroke="#0A1F3D" stroke-width="2"/>'
  + ''.join(f'<path d="M{100+i*75} 165 v10" stroke="#0A1F3D" stroke-width="2"/><text x="{100+i*75}" y="192" text-anchor="middle" fill="#0A1F3D">{i}</text>' for i in range(7)) +
  ''.join(f'<circle cx="{100+v*75}" cy="{156-k*16}" r="6.5" fill="#0047BA"/>' for v, n in [(0, 1), (1, 3), (2, 6), (3, 5), (4, 3), (5, 1), (6, 1)] for k in range(n)) +
  '<text x="330" y="212" text-anchor="middle" fill="#5b6676" font-size="11">loaves per month (each dot is one customer)</text></svg>')

HIST = ('<svg viewBox="0 0 660 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Histogram of customers&apos; ages in intervals of 10 years: 10 to 19: 2, 20 to 29: 5, 30 to 39: 8, 40 to 49: 6, 50 to 59: 3, 60 to 69: 1">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Histogram: ages of 25 customers</text>'
  '<path d="M100 190 H560 M100 190 V40" stroke="#0A1F3D" stroke-width="2"/>'
  + ''.join(f'<path d="M95 {190-k*18} H100" stroke="#0A1F3D"/><text x="88" y="{194-k*18}" text-anchor="end" fill="#0A1F3D" font-size="11">{k}</text>' for k in range(0, 9, 2)) +
  ''.join(f'<rect x="{100+i*75}" y="{190-n*18}" width="75" height="{n*18}" fill="#C9A84C" stroke="#8a6d1f"/><text x="{137+i*75}" y="{184-n*18}" text-anchor="middle" fill="#0A1F3D" font-size="11">{n}</text><text x="{137+i*75}" y="208" text-anchor="middle" fill="#0A1F3D" font-size="11">{lab}</text>'
          for i, (lab, n) in enumerate([("10-19", 2), ("20-29", 5), ("30-39", 8), ("40-49", 6), ("50-59", 3), ("60-69", 1)])) +
  '<text x="330" y="226" text-anchor="middle" fill="#5b6676" font-size="11">age in years (bars touch because the intervals are continuous)</text><text x="40" y="120" fill="#5b6676" font-size="11" transform="rotate(-90 40 120)" text-anchor="middle">number of customers</text></svg>')

LESSON = {
 "unit": "Unit 6: Geometry and Data",
 "title": "Statistical Questions and Data Displays",
 "subtitle": "Businesses, scientists and governments make decisions with data. This week you learn what makes a question statistical, how to collect fair data with a survey, and how to organize it in frequency tables, dot plots and histograms so patterns jump out, starting with a survey of a small business's customers.",
 "objectives": [
  "Recognize and write statistical questions that anticipate variability.",
  "Design a fair survey and identify sources of bias in sampling and wording.",
  "Organize data in frequency tables, dot plots and histograms.",
  "Describe a data set's center, spread and overall shape from a display.",
  "Use survey data to make a business decision."],
 "vocab": [
  ["statistical question", "A question that expects many different answers (variability) and is answered by collecting data."],
  ["variability", "How much data values differ from one another."],
  ["frequency", "How many times a value or interval appears in a data set."],
  ["dot plot", "A display that shows each data value as a dot above a number line."],
  ["histogram", "A bar graph of data grouped into equal intervals, with no gaps between bars."],
  ["sample", "The part of a group that is surveyed to learn about the whole group."],
  ["bias", "Anything in a survey that pushes results away from the truth."]],
 "reconnect": {
  "title": "Week 27: Surface area and volume",
  "intro": "Last week you measured boxes. This week you measure people's answers.",
  "items": [
   {"t":"num","q":"Find the volume of a box 8 in by 5 in by 4 in.","a":160,"unit":"cubic inches","pts":2,"why":"8 × 5 × 4 = 160."},
   {"t":"num","q":"Find the surface area of the same box.","a":184,"unit":"square inches","pts":2,"why":"2(40) + 2(32) + 2(20) = 80 + 64 + 40 = 184."},
   {"t":"num","q":"Maya saves $4.20 per order with a smaller box. How much does she save on 40 orders?","a":168,"unit":"dollars","pts":2,"why":"40 × 4.20 = 168."},
   {"t":"open","key":"rc_choice","q":"Maya wondered whether her customers would pay more for a bigger box with a gift card. How could she find out what her customers want instead of guessing?","min":12,"rows":2,"rubric":["A practical way to get information from customers"],"model":"She could survey her customers, asking a sample of them whether they'd pay extra for a gift box, and use their answers to decide."}]},
 "hook": {
  "title": "Ask Your Customers",
  "visual": DOTPLOT,
  "html": "<p>Maya wants to grow her bakery. Should she offer a monthly subscription? To decide, she needs to know how many loaves her customers usually buy each month. One customer buys 6, another buys none, most buy 2 or 3. That spread is <b>variability</b>, and it's exactly what statistics is for.</p><p>The dot plot shows the answers from 20 customers. In one glance you can see where most answers cluster and how far they spread.</p><div class='callout'><b>Big question:</b> How do we ask good questions, collect fair data and display it so the story shows?</div>"},
 "learn": [
  {"title": "Statistical Questions",
   "html": "<p>A <b>statistical question</b> expects many different answers and is answered with data. \"How tall am I?\" has one answer. \"How tall are the students in my co-op?\" expects <b>variability</b>, so it's statistical.</p><ul><li>Not statistical: How many loaves did Mrs. Lee buy in May? What is 12 × 9?</li><li>Statistical: How many loaves do Maya's customers buy each month? How many hours do sixth graders sleep on school nights?</li></ul>",
   "checks": [
    {"t":"open","key":"makestat","q":"Change this into a statistical question: \"How many books did I read this summer?\"","min":10,"rows":2,"rubric":["A question expecting many different answers from a group"],"model":"How many books did the students in my homeschool co-op read this summer?"},
    {"t":"open","key":"whystat","q":"Explain why \"What is the temperature in Arcadia right now?\" is not a statistical question but \"How did the daily high temperature in Arcadia vary in July?\" is.","min":20,"rows":2,"rubric":["Explains one answer versus many expected answers"],"model":"The first has one answer at one moment. The second expects many different values, 31 daily highs that vary, so it needs data to answer."}]},
  {"title": "Fair Surveys and Bias",
   "html": "<p>To learn about a big group (the <b>population</b>), we usually survey a <b>sample</b>. A good sample is <b>random</b> and large enough. <b>Bias</b> can sneak in:</p><ul><li><b>Sampling bias:</b> asking only some kinds of people, like surveying only customers who come to the farmers market on Saturday.</li><li><b>Wording bias:</b> leading questions such as \"Don't you love our delicious new rye bread?\"</li><li><b>Voluntary response:</b> only people with strong feelings choose to answer.</li></ul><p>A fair question: \"Which bread would you most like to buy: sourdough, rye or whole wheat?\"</p>",
   "checks": [
    {"t":"open","key":"fixleading","q":"Rewrite this leading question so it is fair: \"Wouldn't a monthly bread subscription be a great deal?\"","min":10,"rows":2,"rubric":["A neutral question with no loaded words","Still asks about the subscription"],"model":"Would you be interested in a monthly bread subscription? Yes, no or not sure."},
    {"t":"open","key":"samplebias","q":"Maya surveyed only customers who follow her on Instagram. Explain why her results might be biased and suggest a better sample.","min":25,"rows":3,"rubric":["Explains who is left out and why that matters","Suggests a more representative sample"],"model":"Instagram followers might be younger and more excited about her bakery than other customers, so the results might overstate interest. A better sample would randomly choose 25 customers from her full order list, including people who buy at the market."}]},
  {"title": "Frequency Tables and Dot Plots",
   "html": "<p>A <b>frequency table</b> counts how often each value appears. A <b>dot plot</b> draws a dot above a number line for each value.</p><p>From Maya's dot plot: 20 customers; most bought 2 or 3 loaves; values range from 0 to 6; the data cluster in the middle with a few customers far to the right. When describing a display, talk about its <b>center</b> (where most data are), its <b>spread</b> (how far apart) and its <b>shape</b> (clusters, gaps, peaks, symmetry).</p>",
   "checks": [
    {"t":"num","q":"From the dot plot, how many customers bought 2 loaves?","a":6,"pts":2,"why":"Count the dots above 2."},
    {"t":"num","q":"How many customers bought 4 or more loaves?","a":5,"pts":2,"why":"3 + 1 + 1 = 5."},
    {"t":"open","key":"describedot","q":"Describe the dot plot's center, spread and shape in two or three sentences.","min":25,"rows":3,"rubric":["Describes the center","Describes the spread","Describes the shape"],"model":"Most customers bought 2 or 3 loaves, so the center is around 2 or 3. The data spread from 0 to 6. The shape has a peak at 2 and trails off to the right, with just a couple of customers buying 5 or 6."}]},
  {"title": "Histograms",
   "visual": HIST,
   "html": "<p>When data have many different values, such as ages or heights, group them into equal <b>intervals</b> and draw a <b>histogram</b>. Each bar's height shows the frequency of that interval. The bars touch because the intervals are continuous.</p><p>A histogram shows shape but hides individual values: you can tell that 8 customers are in their 30s, but not their exact ages.</p>",
   "checks": [
    {"t":"num","q":"From the histogram, how many customers are 40 or older?","a":10,"pts":2,"why":"6 + 3 + 1 = 10."},
    {"t":"num","q":"What percent of the 25 customers are in their 30s?","a":32,"unit":"percent","pts":2,"why":"8 ÷ 25 = 0.32."},
    {"t":"open","key":"dotvshist","q":"When is a histogram better than a dot plot? Give an example of data that fit each display best.","min":25,"rows":3,"rubric":["Explains histograms for many different values grouped into intervals","An example for each display"],"model":"A histogram is better when there are many different values, like customers' ages from 12 to 68, so grouping them into intervals shows the shape. A dot plot works better for a few whole-number values, like loaves bought per month from 0 to 6."}]}],
 "handson": {
  "title": "Customer Survey for a Home Business",
  "intro": "Design and run a real survey, then display the results to make a decision.",
  "materials": ["Paper and pencil, or a phone or tablet to record answers", "Graph paper", "Colored pencils", "A ruler", "At least 15 people to survey (family, friends, co-op members, neighbors, with a parent's permission)"],
  "steps": [
   "Imagine a small business you could run (a bake sale, a dog-walking service, a lemonade stand, a craft shop) or use a real family business.",
   "Write two statistical survey questions: one with a number answer (for example, \"How much would you pay for a dozen cookies?\") and one choice question (for example, \"Which flavor would you buy most?\"). Check both for wording bias.",
   "Survey at least 15 people, trying to include different ages and people who don't usually buy from you.",
   "Make a frequency table for each question. Draw a dot plot or histogram for the number question and a bar graph for the choice question.",
   "Describe the center, spread and shape, and use the results to make one business decision.",
   "Survey only people you know or that a parent approves, and never collect personal information such as addresses or phone numbers."],
  "record": [
   {"t":"open","key":"surveyrec","q":"Write your two survey questions, who you surveyed and your frequency tables. What display did you choose for the number question, and why?","min":45,"rows":5,"rubric":["Two statistical, unbiased questions","Describes the sample","Frequency tables","Justifies the display choice"],"model":"Questions: \"How much would you pay for a dozen cookies?\" and \"Which flavor would you buy most: chocolate chip, oatmeal or sugar?\" I surveyed 18 people: family, co-op friends and neighbors from age 8 to 70. Prices: $3 (2), $4 (3), $5 (7), $6 (4), $8 (2). Flavors: chocolate chip 10, oatmeal 5, sugar 3. I used a dot plot for price because there were only five different values."},
   {"t":"open","key":"decisionrec","q":"Describe your number data's center, spread and shape, and explain the business decision you would make based on your survey.","min":34,"rows":4,"rubric":["Describes center, spread and shape","A decision clearly based on the data"],"model":"Most people would pay $5, with prices spread from $3 to $8 and a peak at $5. I'd sell a dozen chocolate chip cookies for $5, since that's the most common price and chocolate chip was the favorite flavor by far."}]},
 "think": {
  "intro": "Explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"pollbias","q":"A cereal company's website reports that \"9 out of 10 kids prefer our cereal!\" based on an online poll on its own website. Explain at least two reasons to be skeptical, connecting to Week 27 ELA's SIFT moves.","min":50,"rows":4,"rubric":["At least two sources of bias in the poll", "Connects to judging sources"],"model":"First, the company made the poll and wants to sell cereal, so it has a reason to report good results. Second, people visiting the company's own site probably already like the cereal, which is sampling bias, and anyone can answer, so it's a voluntary response. Like we learned with SIFT in Week 27 ELA, I'd look for an independent survey before trusting the claim."},
   {"t":"open","key":"designq","q":"Design a statistical question you could investigate about your homeschool or community, explain how you'd choose a fair sample, and which display you'd use and why.","min":47,"rows":4,"rubric":["A real statistical question","A fair sampling plan","A justified display choice"],"model":"Question: How many minutes do families at our co-op spend reading together each week? I'd randomly pick 20 families from the co-op directory by drawing names, so I don't only ask my friends. I'd use a histogram, because the minutes would vary widely, from 0 to 400, and grouping by 60 minutes would show the shape."}]},
 "exit": [
  {"t":"open","key":"exit_stat","q":"Write one statistical question about pets.","min":6,"rows":2,"rubric":["A question that expects many different answers from a group"],"model":"How many pets do the families in our neighborhood have?"},
  {"t":"text","q":"What display groups data into equal intervals, with bars that touch?","a":[{"all":[["histogram"]],"none":["not"]}],"show":"a histogram","pts":2,"why":"For many different values."},
  {"t":"open","key":"exit_bias","q":"Give one way a survey can become biased.","min":6,"rows":2,"rubric":["A valid source of bias"],"model":"Asking a leading question, like \"Don't you love our new bread?\""}],
 "next": "Week 29: mean, median, mode and range."
}

TEACHER = {
 "standards": [
  "MA.6.DP.1.1: Recognize and formulate a statistical question that would generate numerical data.",
  "MA.6.DP.1.4: Given a histogram or line plot within a real-world context, qualitatively describe and interpret the spread and distribution of the data, including any symmetry, skewness, gaps, clusters, outliers and the range.",
  "MA.6.DP.1.5: Create box plots and histograms to represent sets of numerical data within real-world contexts.",
  "Financial literacy: using data to make business decisions (Jump$tart Spending and Saving)."],
 "materials": ["The interactive lesson", "Paper, graph paper, colored pencils, a ruler", "At least 15 survey respondents (with parent permission)", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 27 warm-up questions."],
  [4, "Hook", "Maya's customers; read the dot plot."],
  [10, "Statistical questions", "Make questions statistical; one answer versus many."],
  [11, "Fair surveys", "Fix leading questions; sampling bias."],
  [11, "Dot plots", "Count and describe center, spread and shape."],
  [12, "Histograms", "Intervals; percents; choose a display."],
  [6, "Assign", "Set up the customer survey; assign Think Deeper and the Exit Check."]],
 "key_questions": ["Does this question expect many different answers?", "Who is left out of this sample?", "Is this question pushing people toward an answer?", "Where is the center, and how spread out are the data?"],
 "misconceptions": ["Any question is a statistical question.", "A bigger sample always fixes bias.", "Histogram bars should have gaps like bar graphs.", "A histogram shows each individual value."],
 "support": ["Provide a frequency table template.", "Build a dot plot with sticky notes first.", "Offer sentence frames for center, spread and shape."],
 "challenge": ["Compare two dot plots, such as loaves bought by subscribers and non-subscribers.", "Find a real survey in the news and evaluate its sample and question wording."],
 "background": "<p>Florida's Grade 6 data benchmarks are MA.6.DP.1.1 to 1.6; Florida's benchmarks call dot plots &quot;line plots.&quot; Box plots are introduced in Week 29 with the median. Maya's data are practice figures; the hands-on uses real survey data.</p>",
 "sources": ["Florida Department of Education, B.E.S.T. Standards for Mathematics (2020).", "American Statistical Association, GAISE II: Pre-K–12 Guidelines for Assessment and Instruction in Statistics Education (2020)."]
}

PRINT = {
 "directions": "Show your work.",
 "items": [
  {"q":"Label each as statistical or not: (a) How old is my dog? (b) How old are the dogs at the shelter? (c) How many hours do teens in Florida sleep on school nights?","a":"(a) not (b) statistical (c) statistical","lines":2},
  {"q":"Rewrite fairly: \"Don't you agree our park needs a new playground?\"","a":"Model: Should our park get a new playground? Yes, no or not sure.","lines":2},
  {"q":"Make a frequency table and dot plot for these quiz scores: 7, 8, 8, 9, 10, 8, 7, 9, 8, 10, 6, 8.","a":"6: 1, 7: 2, 8: 5, 9: 2, 10: 2; dot plot from 6 to 10 with a peak at 8.","lines":4},
  {"q":"Group these ages into intervals of 10 and make a histogram: 12, 15, 22, 27, 28, 31, 33, 35, 38, 41, 44, 52.","a":"10-19: 2, 20-29: 3, 30-39: 4, 40-49: 2, 50-59: 1.","lines":4},
  {"q":"Describe a fair way to survey customers about a new product.","a":"Randomly choose customers from the whole list and ask a neutral question.","lines":2}]
}
