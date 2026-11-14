def table_svg(title, head, rows, ops=None, w=560):
    n = len(rows[0]); cw = min(80, (w - 170) // n); x0 = 150
    h = 46 + 36 * len(head) + (32 if ops else 0); ay = 38 + 36 * len(head)
    s = (f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="14" role="img" aria-label="{title}">'
         f'<text x="{w/2}" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">{title}</text>')
    for r, (lab, vals) in enumerate(zip(head, rows)):
        y = 36 + r * 36
        s += f'<rect x="10" y="{y}" width="{x0-14}" height="34" fill="#0A1F3D"/><text x="{(x0-4)/2+5}" y="{y+22}" text-anchor="middle" fill="#fff" font-size="12">{lab}</text>'
        for c, v in enumerate(vals):
            fill = "#fff8e1" if v == "?" else "#fff"
            s += f'<rect x="{x0+c*cw}" y="{y}" width="{cw}" height="34" fill="{fill}" stroke="#0A1F3D"/><text x="{x0+c*cw+cw/2}" y="{y+22}" text-anchor="middle" font-weight="{"bold" if v=="?" else "normal"}" fill="{"#DB2F30" if v=="?" else "#0A1F3D"}">{v}</text>'
    if ops:
        for c, t in ops:
            x = x0 + c * cw + cw
            s += f'<path d="M{x-cw/2+6} {ay} q{cw/2-6} 18 {cw-12} 0" fill="none" stroke="#DB2F30" stroke-width="1.5"/><text x="{x}" y="{ay+26}" text-anchor="middle" font-size="11" fill="#DB2F30">{t}</text>'
    return s + '</svg>'

DOUGH = table_svg("Salt dough ratio table: flour to salt is 2 : 1", ["Cups of flour", "Cups of salt"], [["2", "4", "6", "8", "10", "1", "?"], ["1", "2", "3", "4", "5", "1/2", "7"]], ops=[(0, "×2"), (1, "add 2 : 1"), (4, "÷10")])

def plot():
    s = ('<svg viewBox="0 0 560 280" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Graph of equivalent ratios on a coordinate grid">'
         '<text x="280" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Graphing a ratio table: limes and cost</text>')
    ox, oy, sx, sy = 70, 240, 28, 32
    for i in range(0, 17, 4):
        x = ox + i * 24
        s += f'<line x1="{x}" y1="{oy}" x2="{x}" y2="{oy-6*sy}" stroke="#e1e5ec"/><text x="{x}" y="{oy+16}" text-anchor="middle" font-size="11">{i}</text>'
    for j in range(0, 7):
        y = oy - j * sy
        s += f'<line x1="{ox}" y1="{y}" x2="{ox+16*24}" y2="{y}" stroke="#e1e5ec"/><text x="{ox-8}" y="{y+4}" text-anchor="end" font-size="11">${j}</text>'
    s += f'<line x1="{ox}" y1="{oy}" x2="{ox+16*24+10}" y2="{oy}" stroke="#0A1F3D" stroke-width="2"/><line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy-6*sy-10}" stroke="#0A1F3D" stroke-width="2"/>'
    s += f'<line x1="{ox}" y1="{oy}" x2="{ox+16*24}" y2="{oy-4*sy}" stroke="#C9A84C" stroke-width="2" stroke-dasharray="5 4"/>'
    s += f'<line x1="{ox}" y1="{oy}" x2="{ox+15*24}" y2="{oy-6*sy}" stroke="#0047BA" stroke-width="2" stroke-dasharray="5 4"/>'
    for q in (4, 8, 12, 16):
        s += f'<circle cx="{ox+q*24}" cy="{oy-q/4*sy}" r="5" fill="#C9A84C"/>'
    for q in (5, 10, 15):
        s += f'<circle cx="{ox+q*24}" cy="{oy-q*2/5*sy}" r="5" fill="#0047BA"/>'
    s += (f'<text x="{ox+16*24/2}" y="{oy+34}" text-anchor="middle" font-weight="bold">Number of limes</text>'
          f'<text x="18" y="{oy-3*sy}" text-anchor="middle" font-weight="bold" transform="rotate(-90 18 {oy-3*sy})">Cost</text>'
          f'<circle cx="100" cy="52" r="5" fill="#C9A84C"/><text x="110" y="56">Market: 4 for $1</text><circle cx="100" cy="72" r="5" fill="#0047BA"/><text x="110" y="76">Store: 5 for $2</text></svg>')
    return s

LESSON = {
 "unit": "Unit 2: Fractions and Ratios",
 "title": "Ratio Tables and Equivalent Ratios",
 "subtitle": "A ratio table organizes equivalent ratios so you can scale recipes, find missing amounts and compare prices at a glance.",
 "objectives": [
  "Build ratio tables using multiplication, division and addition of columns.",
  "Find missing values in a ratio table.",
  "Decide whether two ratios are equivalent using a table.",
  "Graph the pairs in a ratio table and describe the pattern.",
  "Use price tables to compare deals and choose a better buy."],
 "vocab": [
  ["ratio table", "A table that lists equivalent ratios in columns."],
  ["scale factor", "The number you multiply (or divide) both quantities by to get an equivalent ratio."],
  ["equivalent ratios", "Ratios that make the same comparison, such as 2 : 1 and 6 : 3."],
  ["price table", "A ratio table that pairs a quantity of an item with its cost."],
  ["ordered pair", "A pair of numbers (x, y) that locates a point on a graph."],
  ["origin", "The point (0, 0) where the axes of a graph meet."]],
 "reconnect": {
  "title": "Week 8: Ratios and ratio language",
  "intro": "Ratio tables are equivalent ratios lined up in a row. Warm up first.",
  "items": [
   {"t":"text","q":"Write 16 : 24 in simplest form.","a":["2:3","2 to 3","2/3"],"show":"2 : 3","pts":2,"why":"The GCF of 16 and 24 is 8: 16 ÷ 8 = 2 and 24 ÷ 8 = 3."},
   {"t":"num","q":"Hummingbird nectar is 1 cup of sugar for every 4 cups of water. How many cups of water go with 3 cups of sugar?","a":12,"unit":"cups","pts":2,"why":"1 : 4 = 3 : 12. Multiply both parts by 3."},
   {"t":"open","key":"rc_add","q":"Week 8 warned that adding the same number to both parts of a ratio does not keep it equivalent. Explain why, using 1 : 4.","min":15,"rows":2,"rubric":["Adding changes the comparison; e.g. 1 : 4 to 2 : 5 has more sugar per cup of water","Multiplying (2 : 8) keeps the comparison"],"model":"If you add 1 to each part, 1 : 4 becomes 2 : 5, which has more sugar for each cup of water, so it is sweeter. Multiplying both by 2 gives 2 : 8, which keeps the same comparison."},
   {"t":"num","q":"Which costs less for 12 cans: 4 for $3 or 6 for $5? Type the lower price for 12 cans.","a":9,"unit":"dollars","show":"$9","pts":2,"why":"4 for $3 × 3 = 12 for $9; 6 for $5 × 2 = 12 for $10. Today, price tables make comparisons like this faster."}]},
 "hook": {
  "title": "Enough Dough for Everyone",
  "html": "<p>This week in Social Studies you will mint Aksumite coins from salt dough. The recipe is 2 cups of flour for 1 cup of salt, plus water. But what if your whole homeschool co-op wants to make coins? Or you only want a tiny batch?</p><p>You could scale the recipe one step at a time, but a <b>ratio table</b> lets you see many equivalent ratios at once and jump straight to the amount you need.</p><div class='callout'><b>Big idea:</b> In a ratio table, every column is equivalent to every other column. Whatever you do to the top number, you must do to the bottom number.</div>"},
 "learn": [
  {"title": "Building a Ratio Table",
   "visual": DOUGH,
   "html": "<p>Each column of a ratio table is a ratio equivalent to the first. You can make new columns three ways:</p><ul><li><b>Multiply</b> both numbers by the same number: 2 : 1 × 2 = 4 : 2.</li><li><b>Divide</b> both numbers by the same number: 10 : 5 ÷ 10 = 1 : 1/2.</li><li><b>Add two columns</b> together: 4 : 2 + 6 : 3 = 10 : 5. (This works because both columns already have the same ratio.)</li></ul><p>To find a missing value, look for the scale factor. In the last column, salt is 7. Since 7 = 1 × 7, flour is 2 × 7 = 14 cups.</p><p>Notice the difference from Week 8: adding the same <b>number</b> to both parts breaks the ratio, but adding two equivalent <b>columns</b> keeps it.</p>",
   "checks": [
    {"t":"num","q":"In the salt dough table, how many cups of flour go with 7 cups of salt?","a":14,"unit":"cups","pts":2,"why":"Flour is always 2 times the salt: 2 × 7 = 14."},
    {"t":"blanks","q":"Complete the ratio table for fertilizer: 3 tablespoons for every 2 gallons of water.","sent":"Tablespoons: 3, 6, ___, 15, ___. Gallons: 2, 4, 6, ___, 14.","blanks":[["9"],["21"],["10"]],"show":"9; 21; 10","pts":3,"why":"Each column is a multiple of 3 : 2. 3 × 3 = 9; 3 × 7 = 21 (since 14 = 2 × 7); 2 × 5 = 10 (since 15 = 3 × 5)."},
    {"t":"num","q":"A ratio table for a smoothie shows 6 bananas : 4 cups of milk. Divide to find how much milk goes with 3 bananas.","a":2,"unit":"cups","pts":2,"why":"Divide both by 2: 6 : 4 = 3 : 2."},
    {"t":"open","key":"addcol","q":"Explain why adding the columns 4 : 2 and 6 : 3 gives an equivalent ratio, but adding 2 to each part of 4 : 2 does not.","min":20,"rows":3,"rubric":["Both columns already have the same 2 : 1 relationship, so their sum (10 : 5) does too","Adding 2 to each part (6 : 4) changes the relationship"],"model":"4 : 2 and 6 : 3 both have flour twice the salt, so together, 10 : 5, flour is still twice the salt. Adding 2 to each part of 4 : 2 gives 6 : 4, and 6 is not twice 4, so the relationship changes."}]},
  {"title": "Are These Ratios Equivalent?",
   "html": "<p>To test whether two ratios are equivalent, scale one to match a number in the other, or simplify both.</p><div class='callout'><b>Example:</b> Is 9 : 12 equivalent to 15 : 20?<br>Simplify: 9 : 12 = 3 : 4 and 15 : 20 = 3 : 4. Yes, they are equivalent.<br><b>Example:</b> Is 4 : 6 equivalent to 10 : 14?<br>Scale 4 : 6 so the first number is 10? 10 is not a whole-number multiple of 4, so use simplest form: 4 : 6 = 2 : 3, but 10 : 14 = 5 : 7. Not equivalent.</div><p>A ratio table can also help: build the table for one ratio and see whether the other appears in it.</p>",
   "checks": [
    {"t":"text","q":"Is 6 : 8 equivalent to 15 : 20? Type yes or no.","a":[{"all":[["yes"]],"none":["no","not"]}],"show":"yes","pts":2,"why":"6 : 8 = 3 : 4 and 15 : 20 = 3 : 4."},
    {"t":"text","q":"Is 5 : 3 equivalent to 12 : 8? Type yes or no.","a":[{"all":[["no"]],"none":["yes"]}],"show":"no","pts":2,"why":"12 : 8 = 3 : 2, but 5 : 3 is already in simplest form, and 5 : 3 is not 3 : 2."},
    {"t":"open","key":"paint","q":"Kwame mixes 3 cans of yellow paint with 2 cans of blue. Ama mixes 9 cans of yellow with 5 cans of blue. Will their greens be the same shade? Use a ratio table to explain.","min":25,"rows":3,"rubric":["Table for 3 : 2 shows 9 : 6, not 9 : 5","Not the same; Ama's has less blue for the same yellow, so it is a lighter, more yellow green"],"model":"A ratio table for 3 : 2 goes 3 : 2, 6 : 4, 9 : 6. Ama used 9 : 5, not 9 : 6, so the ratios are not equivalent. Her green has less blue for the same amount of yellow, so it will be lighter and more yellow."}]},
  {"title": "Graphing a Ratio Table",
   "visual": plot(),
   "html": "<p>Each column of a ratio table is an <b>ordered pair</b> you can graph. The market sells limes at 4 for $1, so its table gives (4, 1), (8, 2), (12, 3), (16, 4). Graphed, the points line up in a straight line that would pass through the <b>origin</b> (0, 0), because 0 limes cost $0.</p><p>The store's limes, 5 for $2, make a <b>steeper</b> line. Steeper means the cost climbs faster as you buy more, so the store's limes are more expensive. You can see the better buy just by comparing the lines.</p>",
   "checks": [
    {"t":"open","key":"pairs","q":"Write the ordered pairs (limes, cost) for the store's first three columns: 5 for $2, 10 for ?, 15 for ?.","min":8,"rows":1,"rubric":["(5, 2), (10, 4), (15, 6)"],"model":"(5, 2), (10, 4), (15, 6)"},
    {"t":"open","key":"steep","q":"Explain how you can tell from the graph which store has the better price, without doing any arithmetic.","min":20,"rows":2,"rubric":["The less steep line is cheaper: for the same number of limes, its point is lower (costs less)"],"model":"The market's line is less steep, so for the same number of limes its points are lower on the graph, which means they cost less."},
    {"t":"open","key":"origin","q":"Why does the line for a price table pass through (0, 0)? Would that be true if the store charged a $1 bag fee no matter how many limes you bought?","min":20,"rows":3,"rubric":["0 items cost $0, so (0, 0) fits the ratio","With a fixed fee, 0 limes would cost $1, so the line would not pass through the origin and the table would not show equivalent ratios"],"model":"Zero limes cost zero dollars, so (0, 0) is on the line. With a $1 bag fee, even 0 limes would cost $1, so the line would start at $1 instead of the origin, and the costs would not be equivalent ratios anymore."}]},
  {"title": "Money: Price Tables and Better Buys",
   "html": "<p>A <b>price table</b> lets you compare deals at many quantities at once. Suppose you are buying chicken thighs for a family cookout:</p>" + table_svg("Two price tables for chicken thighs", ["Pounds (Butcher)", "Cost (Butcher)", "Pounds (Grocery)", "Cost (Grocery)"], [["3", "6", "9", "12"], ["$7", "$14", "$21", "$28"], ["4", "8", "12", "16"], ["$10", "$20", "$30", "$40"]]) + "<p>Find a quantity that appears in both tables: 12 pounds. The butcher charges $28, and the grocery store charges $30. The butcher is the better buy.</p><p>Before choosing, check the whole picture: Is the cheaper store far away, so you would spend more on gas? Is the quality the same? Will you use all 12 pounds? A smart shopper weighs price and needs together.</p>",
   "checks": [
    {"t":"num","q":"Using the butcher's table, how much would 15 pounds of chicken cost?","a":35,"unit":"dollars","show":"$35","pts":2,"why":"15 = 3 × 5, so the cost is $7 × 5 = $35 (or add the 3-pound and 12-pound columns: $7 + $28)."},
    {"t":"num","q":"How much would a family save on 24 pounds by buying from the butcher instead of the grocery store?","a":4,"unit":"dollars","show":"$4","pts":3,"why":"Butcher: 24 lb = 8 × 3 lb, so 8 × $7 = $56. Grocery: 24 lb = 6 × 4 lb, so 6 × $10 = $60. Savings: $60 − $56 = $4."},
    {"t":"open","key":"gas","q":"The butcher is 20 miles farther away than the grocery store, round trip. Should the family drive there to save $2 on 12 pounds? Explain what else they should consider.","min":25,"rows":3,"rubric":["Considers the cost of gas and time for the extra miles (likely more than $2)","Concludes with reasoning: probably not worth it just for chicken, unless combined with other errands or quality matters"],"model":"Probably not. Driving 20 extra miles uses gas that likely costs more than the $2 saved, plus extra time. It might be worth it if they were going that way anyway or if the butcher's chicken is better quality."}]}],
 "handson": {
  "title": "Scale the Salt Dough",
  "intro": "Use a ratio table to plan and mix exactly enough salt dough for the Social Studies coin activity.",
  "materials": ["Flour, table salt and water", "Measuring cups (including 1/4 and 1/2 cup)", "A large bowl and spoon", "Paper and pencil", "A jar lid about 6 cm wide (for cutting coin circles)"],
  "steps": [
   "The recipe is 2 cups flour : 1 cup salt : 1 cup water. Make a ratio table that shows batches for 1/2, 1, 2 and 3 times the recipe.",
   "Make one tiny test batch (1/4 of the recipe). Count how many 6 cm coins it makes.",
   "Use the test result and your table to decide what size batch your family needs for everyone to make two coins (front and back count as one coin).",
   "Mix the batch you chose and check: did you make enough? Too much?"],
  "record": [
   {"t":"open","key":"doughtable","q":"Copy your ratio table for flour, salt and water at 1/4, 1/2, 1, 2 and 3 batches.","min":20,"rows":4,"rubric":["Correct amounts: 1/4 batch = 1/2 c flour, 1/4 c salt, 1/4 c water; 1/2 batch = 1, 1/2, 1/2; 1 = 2, 1, 1; 2 = 4, 2, 2; 3 = 6, 3, 3"],"model":"1/4 batch: 1/2 cup flour, 1/4 cup salt, 1/4 cup water. 1/2 batch: 1, 1/2, 1/2. 1 batch: 2, 1, 1. 2 batches: 4, 2, 2. 3 batches: 6, 3, 3."},
   {"t":"open","key":"doughplan","q":"How many coins did your test batch make? Show how you used that number and your table to decide how much dough your family needed. Did it work?","min":40,"rows":4,"rubric":["Reports test result","Uses ratio reasoning to scale up to the number needed","Reflects on the outcome"],"model":"The 1/4 batch made 3 coins. Our family of 4 needs 8 coins. 1/2 batch makes 6 coins and 1 batch makes 12, so I made 1 batch to be safe. We had dough for 4 extra coins, so 3/4 of a batch would have been closer."}]},
 "think": {
  "intro": "Show your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"recipe9","q":"A family recipe for fufu-style plantain balls uses 6 plantains for every 4 servings. Make a ratio table to find how many plantains are needed for 2, 10 and 18 servings. Explain each step and the operation you used.","min":50,"rows":6,"rubric":["Correct values: 2 servings 3 plantains; 10 servings 15; 18 servings 27","Names operations (divide by 2, multiply, add columns)","Clear table"],"model":"Start: 6 plantains : 4 servings. Divide both by 2: 3 plantains : 2 servings. Multiply 3 : 2 by 5: 15 plantains : 10 servings. Multiply 3 : 2 by 9: 27 plantains : 18 servings. I could also add the columns for 10 and 8 servings (15 + 12 = 27) to check."},
   {"t":"open","key":"phone","q":"Two phone plans: Plan A costs $15 for every 3 GB of data. Plan B costs $24 for every 4 GB. Make a price table for each up to 12 GB, decide which is the better buy for 12 GB, and explain one reason a family might still pick the other plan.","min":50,"rows":6,"rubric":["Plan A: 3, 6, 9, 12 GB = $15, $30, $45, $60","Plan B: 4, 8, 12 GB = $24, $48, $72","Plan A is cheaper for 12 GB ($60 vs $72)","Reasonable reason for B (better coverage, comes in different bundle sizes, other features)"],"model":"Plan A: 3 GB $15, 6 GB $30, 9 GB $45, 12 GB $60. Plan B: 4 GB $24, 8 GB $48, 12 GB $72. Plan A is the better buy for 12 GB by $12. A family might still pick Plan B if it has better coverage where they live, since cheap data does not help if the phone has no signal."}]},
 "exit": [
  {"t":"blanks","q":"Complete the ratio table for 5 : 2.","sent":"Top row: 5, 10, ___, 25. Bottom row: 2, ___, 8, 10.","blanks":[["20"],["4"]],"show":"20; 4","pts":2,"why":"5 × 4 = 20 (because 8 = 2 × 4); 2 × 2 = 4 (because 10 = 5 × 2)."},
  {"t":"text","q":"Is 4 : 10 equivalent to 6 : 15? Type yes or no.","a":[{"all":[["yes"]],"none":["no","not"]}],"show":"yes","pts":2,"why":"Both simplify to 2 : 5."},
  {"t":"num","q":"Bananas are 6 for $2. Using a price table, how much do 21 bananas cost?","a":7,"unit":"dollars","show":"$7","pts":2,"why":"3 bananas cost $1 (divide by 2), and 21 = 3 × 7, so $7."},
  {"t":"open","key":"exit_graph","q":"Two price tables are graphed. Line A is steeper than Line B. Which shows the better buy, and why?","min":12,"rows":2,"rubric":["Line B","Less steep: lower cost for the same quantity"],"model":"Line B, because it is less steep, so the same amount costs less."}],
 "next": "Week 10: the Unit 2 review and checkpoint, plus a budget review."
}

TEACHER = {
 "standards": [
  "MA.6.AR.3.1: Given a real-world context, write and interpret ratios to show the relative sizes of two quantities using appropriate notation: a/b, a to b, or a:b where b ≠ 0.",
  "MA.6.AR.3.5: Solve mathematical and real-world problems involving ratios, rates and unit rates, including comparisons, mixtures, ratios of lengths and conversions within the same measurement system.",
  "MA.K12.MTR.2.1: Demonstrate understanding by representing problems in multiple ways.",
  "MA.K12.MTR.6.1: Assess the reasonableness of solutions.",
  "Financial literacy: comparing prices and weighing costs such as travel (Jump$tart Spending)."],
 "materials": ["The interactive lesson", "Flour, salt, water, measuring cups, a bowl", "Graph paper and colored pencils", "A grocery ad or two receipts", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 8 Reconnect questions."],
  [4, "Hook", "Connect to the Social Studies coin activity and the dough recipe."],
  [12, "Ratio tables", "Build the dough table together using all three moves: multiply, divide, add columns."],
  [10, "Equivalent?", "Test pairs of ratios by simplifying. Mix two paint ratios with colored water if available."],
  [10, "Graphing", "Plot the market's limes on graph paper; then the store's. Compare steepness."],
  [12, "Price tables", "Compare the chicken tables and discuss gas and time."],
  [6, "Assign", "Assign the dough activity, Think Deeper and the Exit Check."]],
 "key_questions": ["What did you do to the top number? Did you do the same to the bottom?", "Which column can you add or multiply to reach the number you need?", "What does a steeper line mean?", "Is the cheaper price worth the extra trip?"],
 "misconceptions": ["Adding the same number to both rows of a table.", "Thinking ratio tables must go up by ones.", "Reading the steeper line as the better deal.", "Comparing prices at different quantities."],
 "support": ["Use a two-row blank table template.", "Have the student write the scale factor above each column.", "Use real measuring cups for the dough table."],
 "challenge": ["Graph the fertilizer table and the dough table on the same axes and compare the lines.", "Write your own price table problem from a real grocery ad."],
 "background": "<p>This lesson builds on MA.6.AR.3.1 and the ratio-reasoning parts of MA.6.AR.3.5 using ratio tables and graphs, without computing unit rates; unit rates (MA.6.AR.3.2) are taught in Unit 3. The graph section previews proportional relationships formally taught in Grade 7. The salt dough recipe (2 parts flour : 1 part salt : 1 part water) matches the Social Studies coin activity this week. Fertilizer ratios vary by product; the 3 tablespoons per 2 gallons figure is a made-up example for practice.</p>",
 "sources": ["CPALMS, MA.6.AR.3 benchmarks.", "Illustrative Mathematics Grade 6, Unit 2: Introducing Ratios (ratio tables and double number lines).", "Jump$tart Coalition, National Standards for Personal Financial Education (Spending)."]
}

PRINT = {
 "directions": "Show your work.",
 "items": [
  {"q":"Complete the ratio table for 4 : 3: top row 4, 8, ___, 20; bottom row 3, ___, 9, ___.","a":"12; 6; 15","lines":1},
  {"q":"A drink mix is 2 scoops for 3 cups of water. How many scoops for 15 cups?","a":"10 scoops","lines":2},
  {"q":"Is 12 : 18 equivalent to 10 : 15? Explain.","a":"Yes; both simplify to 2 : 3.","lines":2},
  {"q":"Write ordered pairs for 3 apples for $2 at 3, 6 and 9 apples.","a":"(3, 2), (6, 4), (9, 6)","lines":1},
  {"q":"Pasta: Store A, 2 boxes for $3. Store B, 3 boxes for $5. Use price tables to compare 6 boxes. Which is better?","a":"A: $9; B: $10. Store A.","lines":3},
  {"q":"Explain why adding two columns of a ratio table gives an equivalent ratio.","a":"Both columns have the same relationship, so their sum keeps it.","lines":2}]
}
