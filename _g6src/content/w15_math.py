FLOW = ('<svg viewBox="0 0 660 250" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Decision chart for choosing a strategy in rate, percent and conversion problems">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Unit 3 toolkit: what is the question asking?</text>'
  + ''.join(f'<rect x="{x}" y="40" width="150" height="190" rx="12" fill="{c}"/><text x="{x+75}" y="64" text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">{h}</text>'
            + ''.join(f'<text x="{x+10}" y="{90+j*22}" fill="#fff" font-size="11">{line}</text>' for j, line in enumerate(lines))
            for x, h, c, lines in [
              (12, "\"per one\"?", "#0047BA", ["UNIT RATE", "divide: total ÷ units", "$4.80 for 24 oz", "→ $0.20 per oz", "compare deals with", "the same unit"]),
              (176, "\"percent of\"?", "#3d9a2f", ["PERCENT", "part = % × whole", "whole = part ÷ %", "tax, tip: add", "discount: pay what", "is left (1 − rate)"]),
              (340, "\"cost vs price\"?", "#C9A84C", ["MARKUP", "markup % is of", "the COST", "price = cost × (1 + rate)", "profit = price − cost", ""]),
              (504, "\"different units\"?", "#DB2F30", ["CONVERT", "smaller unit: multiply", "larger unit: divide", "metric: powers of 10", "money: × rate out,", "÷ rate back"])]) +
  '<text x="330" y="246" text-anchor="middle" font-size="11" fill="#5b6676">Always check: is the answer reasonable compared with a benchmark?</text></svg>')

LESSON = {
 "unit": "Unit 3: Rates and Percents",
 "title": "Unit 3 Review and Checkpoint",
 "subtitle": "Pull together unit rates, percents, discounts, tips, markups, conversions and currency to plan a real care package, then show what you know on the Unit 3 checkpoint.",
 "objectives": [
  "Choose the right strategy for rate, percent, markup and conversion problems.",
  "Find and compare unit rates.",
  "Solve percent problems: a percent of a number, the whole from a part, sales tax, tips, discounts and markups.",
  "Convert units within a measurement system and convert between currencies.",
  "Plan a multi-step budget that combines all of these skills."],
 "vocab": [
  ["unit rate", "A rate for one unit, such as $0.20 per ounce."],
  ["percent", "A rate per 100."],
  ["discount and markup", "An amount taken off a price, and an amount added to a cost."],
  ["conversion factor", "A ratio of equal amounts in different units."],
  ["flat rate", "One price no matter the weight or amount, such as a flat-rate shipping box."]],
 "reconnect": {
  "title": "Weeks 11 to 14: Unit 3 warm-up",
  "intro": "One question from each week of the unit.",
  "items": [
   {"t":"num","q":"Week 11: a 32-ounce bottle of laundry detergent costs $5.12. What is the unit price in cents per ounce? (Type the number of cents.)","a":[16,0.16],"unit":"cents per ounce","pts":2,"why":"$5.12 ÷ 32 = $0.16 = 16 cents per ounce."},
   {"t":"num","q":"Week 12: 21 is 35% of what number?","a":60,"pts":2,"why":"35% → 21, so 5% → 3, so 100% → 60."},
   {"t":"num","q":"Week 13: a $70 sleeping bag is 30% off. What is the sale price?","a":49,"unit":"dollars","show":"$49","pts":2,"why":"Pay 70%: 0.7 × $70 = $49."},
   {"t":"num","q":"Week 14: how many ounces are in 4 pounds?","a":64,"unit":"ounces","pts":2,"why":"4 × 16 = 64 ounces."}]},
 "hook": {
  "title": "A Care Package to a Pen Pal",
  "visual": FLOW,
  "html": "<p>Zuri's homeschool co-op has pen pals at a school in Kingston, Jamaica. Each family is sending a care package: books, school supplies and a few treats. The co-op has a budget, items are on sale, Florida charges sales tax, shipping depends on weight, and the pen pals will want to know what things cost in Jamaican dollars.</p><p>Every skill from Unit 3 shows up in one real job. Today you will review each tool, plan your own care package and then take the checkpoint.</p><div class='callout'><b>Big idea:</b> Before you calculate, ask what the question is really asking: a rate per one, a percent of something, a cost compared with a price, or a change of units.</div>"},
 "learn": [
  {"title": "Review: Unit Rates and Comparing Deals",
   "html": "<p>A <b>unit rate</b> compares a quantity to 1 of another quantity. To find it, divide: total ÷ number of units. Compare deals only when the unit rates use the same unit.</p><p>Example: crayons cost $3.60 for 24 or $5.40 for 48. Unit prices: $0.15 and about $0.11 per crayon, so the 48-pack is the better buy, if you will use them.</p>",
   "checks": [
    {"t":"num","q":"A 12-pack of pencils costs $3.00 and a 30-pack costs $6.00. What is the unit price of the 30-pack in cents per pencil? (Type the number of cents.)","a":[20,0.2],"unit":"cents per pencil","pts":2,"why":"$6.00 ÷ 30 = $0.20; the 12-pack is $0.25 each."},
    {"t":"num","q":"A mail carrier drives 84 miles in 3 1/2 hours. What is the average speed in miles per hour?","a":24,"unit":"miles per hour","pts":2,"why":"84 ÷ 3.5 = 24."},
    {"t":"open","key":"rv_deal","q":"The 30-pack of pencils is the better unit price. Give one reason a family might still buy the 12-pack.","min":15,"rows":2,"rubric":["A sensible reason: they only need a few, limited budget today, storage, the extra would go to waste"],"model":"If they only need 10 pencils, the 12-pack costs less money overall, and the extra 18 pencils might just get lost."}]},
  {"title": "Review: Percents, Discounts, Tax, Tips and Markups",
   "html": "<p>Every percent problem is a percent of some whole. Ask: <b>a percent of what?</b></p><ul><li>Part = percent × whole. 15% of $60 = $9.</li><li>Whole = part ÷ percent. If $18 is 40%, the whole is $45.</li><li>Tax or tip: add a percent of the price. Discount: pay the percent that is left.</li><li>Markup: a percent of the <b>cost</b>; price = cost + markup.</li></ul>",
   "checks": [
    {"t":"num","q":"A $36 box of chapter books is 25% off. Then 7.5% sales tax is added to the sale price. What is the total? Round to the nearest cent.","a":29.03,"unit":"dollars","show":"$29.03","pts":3,"why":"Sale: 0.75 × $36 = $27. Tax: $27 × 0.075 = $2.025, about $2.03. Total $29.03."},
    {"t":"num","q":"A bookstore buys a dictionary for $16 and sells it for $28. What is the markup percent?","a":75,"unit":"%","pts":2,"why":"Markup $12; $12 ÷ $16 = 0.75 = 75%."},
    {"t":"num","q":"After a 20% discount, a microscope kit costs $32. What was the original price?","a":40,"unit":"dollars","show":"$40","pts":3,"why":"$32 is 80%: 80% → 32, 10% → 4, 100% → 40."},
    {"t":"num","q":"The co-op parents' lunch bill is $86 before tax. They leave an 18% tip on that amount. How much is the tip?","a":15.48,"unit":"dollars","show":"$15.48","pts":2,"why":"0.18 × $86 = $15.48."}]},
  {"title": "Review: Converting Units and Currency",
   "html": "<p>Going to a smaller unit, multiply; going to a larger unit, divide. Metric conversions move the decimal point. For money, multiply by the exchange rate to convert dollars into the other currency, and divide to convert back.</p><div class='card' style='font-family:Georgia,serif'>Example rate for this lesson: 1 U.S. dollar = 155 Jamaican dollars (JMD). Real rates change daily.</div>",
   "checks": [
    {"t":"num","q":"The care package box is 18 inches long. How many feet is that? Write a decimal.","a":1.5,"unit":"feet","pts":2,"why":"18 ÷ 12 = 1.5 feet."},
    {"t":"num","q":"A package weighs 5 pounds 6 ounces. How many ounces is that in all?","a":86,"unit":"ounces","pts":2,"why":"5 × 16 = 80; 80 + 6 = 86 ounces."},
    {"t":"num","q":"A storybook costs $12 in Florida. At 1 USD = 155 JMD, how many Jamaican dollars is that?","a":1860,"unit":"Jamaican dollars","pts":2,"why":"12 × 155 = 1,860 JMD."},
    {"t":"open","key":"rv_convert","q":"Tomás converts 2,400 grams to kilograms and gets 2,400,000. Explain his mistake and give the correct answer.","min":15,"rows":2,"rubric":["Kilograms are larger, so he should divide by 1,000, not multiply","Correct answer: 2.4 kg"],"model":"A kilogram is bigger than a gram, so there should be fewer kilograms. He should divide by 1,000: 2,400 g = 2.4 kg."}]},
  {"title": "Money: Mid-Year Money Review",
   "html": "<p>Shipping companies often offer two choices:</p><ul><li><b>By weight:</b> a starting fee plus a price per pound. (Real carriers often round up to the next whole pound; this lesson uses exact weights.)</li><li><b>Flat rate:</b> one price for a box, whatever it weighs, as long as everything fits.</li></ul><p>Example: international shipping to Jamaica costs $9.50 plus $3.25 per pound, or a flat-rate box costs $44. For a 6-pound package, the weight price is $9.50 + 6 × $3.25 = $29. The flat rate is better only for heavy packages.</p>",
   "checks": [
    {"t":"num","q":"Using the example prices ($9.50 plus $3.25 per pound), what does it cost to ship a 10-pound package by weight?","a":42,"unit":"dollars","show":"$42","pts":2,"why":"$9.50 + 10 × $3.25 = $9.50 + $32.50 = $42."},
    {"t":"num","q":"At what weight in pounds does shipping by weight cost the same as the $44 flat-rate box? Round to the nearest tenth of a pound.","a":10.6,"unit":"pounds","pts":3,"why":"$44 − $9.50 = $34.50; $34.50 ÷ $3.25 ≈ 10.6 pounds."},
    {"t":"open","key":"rv_ship","q":"A family's package weighs 12 pounds. Which shipping choice should they pick, and how much do they save? Show your work.","min":20,"rows":2,"rubric":["By weight: $9.50 + 12 × $3.25 = $48.50","Flat rate $44 is cheaper by $4.50"],"model":"By weight: $9.50 + 12 × $3.25 = $9.50 + $39 = $48.50. The flat-rate box is $44, so they should use it and save $4.50."}]}],
 "handson": {
  "title": "Pack and Price a Care Package",
  "intro": "Plan a real care package for a pen pal, using every Unit 3 skill.",
  "materials": ["5 or 6 items you could send (books, school supplies, a small toy); you will return them afterward", "A kitchen or bathroom scale, or the weights printed on packages", "A ruler or tape measure", "A store flyer or website with prices (with a parent)", "Paper and pencil", "A calculator for checking only"],
  "steps": [
   "Choose 5 or 6 items and find a price for each from a flyer or store website. Mark any that are on sale and find their sale prices.",
   "Add 7.5% sales tax to your subtotal (or your county's rate). Stay within a $60 budget.",
   "Weigh each item in ounces (or use the package weight). Add the weights, convert to pounds and ounces, then to pounds as a decimal.",
   "Measure the length of your box in inches and convert to feet.",
   "Using the lesson's example shipping prices, compare shipping by weight with the $44 flat-rate box. Choose the cheaper option.",
   "Convert the cost of your two favorite items into Jamaican dollars at 1 USD = 155 JMD, to tell your pen pal."],
  "record": [
   {"t":"open","key":"packbudget","q":"Show your item list with prices, sale prices, subtotal, tax and total. Did you stay within $60?","min":40,"rows":6,"rubric":["Items with prices; sale prices correct","Correct subtotal, tax and total","Compared with the $60 budget"],"model":"Book $12, notebook set $8 (25% off: $6), colored pencils $9, word-search book $7, card game $10 (20% off: $8), stickers $4. Subtotal: $46. Tax: $46 × 0.075 = $3.45. Total: $49.45, under $60."},
   {"t":"open","key":"packship","q":"Show the total weight in ounces, pounds and ounces, and pounds as a decimal; your box length in feet; both shipping prices; your choice; and two items in Jamaican dollars.","min":40,"rows":6,"rubric":["Weight converted correctly","Box length converted","Both shipping options calculated; correct choice","Two currency conversions correct"],"model":"Weights: 14 + 10 + 9 + 8 + 6 + 1 = 48 oz = 3 lb 0 oz = 3 pounds. Box: 14 in ÷ 12 ≈ 1.17 ft. By weight: $9.50 + 3 × $3.25 = $19.25; flat rate $44; I choose by weight and save $24.75. Book $12 × 155 = 1,860 JMD; card game $8 × 155 = 1,240 JMD."}]},
 "think": {
  "intro": "Show your work and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"coop","q":"The co-op has $500 for 8 care packages. Each package's items cost $46 before tax (7.5%), and each ships for $22. Can they afford all 8? If not, how many can they send, and how much money is left? Show every step.","min":70,"rows":6,"rubric":["Items with tax: $46 × 1.075 = $49.45","Per package with shipping: $49.45 + $22 = $71.45","8 packages = $571.60, over $500","They can send 6 ($428.70) with $71.30 left (or explains 7 = $500.15, just over)"],"model":"Items with tax: $46 × 1.075 = $49.45. With shipping: $49.45 + $22 = $71.45 per package. Eight packages cost 8 × $71.45 = $571.60, which is over $500. Seven would cost $500.15, just 15 cents over, so they can send 6 for $428.70 and have $71.30 left, unless they find a small discount to afford the seventh."},
   {"t":"open","key":"errorfind","q":"Rafael says: \"A $50 jacket is 20% off, and then 7.5% tax is added. That's like 12.5% off, so I pay $43.75.\" Is he right? Calculate the real total and explain his mistake.","min":60,"rows":5,"rubric":["Real total: $50 × 0.8 = $40; $40 × 1.075 = $43.00","Explains that the tax percent is of the sale price, so you cannot just subtract percents; his $43.75 is wrong"],"model":"No. The sale price is 80% of $50 = $40. Tax is 7.5% of $40 = $3, so the total is $43.00, not $43.75. The 20% and 7.5% are percents of different amounts ($50 and $40), so he cannot just subtract them."}]},
 "checkpoint": {
  "title": "Unit 3 Checkpoint: Rates and Percents",
  "intro": "This checkpoint covers Weeks 11 to 15. Work each problem on paper, then type your answer. Use a calculator only for checking money arithmetic if your teacher allows it. Type money without the dollar sign if you like. Mastery is 85 or higher. If you score below 85, your teacher will review with you, then you will retake it.",
  "parts": [
   {"title": "Part A: Unit rates", "items": [
    {"t":"num","q":"A farm stand sells 5 pounds of oranges for $6.25. What is the price per pound?","a":1.25,"unit":"dollars per pound","show":"$1.25","pts":3,"why":"$6.25 ÷ 5 = $1.25."},
    {"t":"num","q":"A cyclist rides 27 miles in 1 1/2 hours. What is her speed in miles per hour?","a":18,"unit":"miles per hour","pts":3,"why":"27 ÷ 1.5 = 18."},
    {"t":"text","q":"Which is the better buy: A) 20 ounces of rice for $2.40 or B) 32 ounces for $3.52? Type A or B.","a":["^b","option b","choice b"],"show":"B ($0.11 per ounce vs. $0.12)","pts":3,"why":"A: $2.40 ÷ 20 = $0.12 per ounce. B: $3.52 ÷ 32 = $0.11 per ounce."}]},
   {"title": "Part B: Percents", "items": [
    {"t":"blanks","q":"Complete the conversions.","sent":"0.35 = ___% &nbsp; 5/8 = ___%","blanks":[["35"],["62.5","62 1/2"]],"show":"35; 62.5","pts":3,"why":"0.35 × 100 = 35%; 5 ÷ 8 = 0.625 = 62.5%."},
    {"t":"num","q":"What is 45% of 80?","a":36,"pts":3,"why":"0.45 × 80 = 36 (or 10% = 8, 40% = 32, 5% = 4)."},
    {"t":"num","q":"27 is 60% of what number?","a":45,"pts":3,"why":"60% → 27, 20% → 9, 100% → 45."},
    {"t":"num","q":"Nadia answered 42 out of 48 questions correctly. What percent is that?","a":87.5,"unit":"%","pts":3,"why":"42 ÷ 48 = 0.875 = 87.5%."}]},
   {"title": "Part C: Discounts, tax, tips and markups", "items": [
    {"t":"num","q":"A $64 pair of hiking boots is 35% off. What is the sale price?","a":41.6,"unit":"dollars","show":"$41.60","pts":3,"why":"Pay 65%: 0.65 × $64 = $41.60."},
    {"t":"num","q":"Find the total cost of a $48 item with 7.5% sales tax.","a":51.6,"unit":"dollars","show":"$51.60","pts":3,"why":"Tax $3.60; total $51.60."},
    {"t":"num","q":"A sporting goods store pays $40 for a soccer ball and uses a 45% markup. What is the selling price?","a":58,"unit":"dollars","show":"$58","pts":3,"why":"45% of $40 = $18; $40 + $18 = $58 (or 1.45 × $40)."},
    {"t":"num","q":"A sale price of $63 is 30% off the original. What was the original price?","a":90,"unit":"dollars","show":"$90","pts":3,"why":"$63 is 70%: 10% → $9, 100% → $90."},
    {"t":"open","key":"cp_tip","q":"A family's restaurant bill is $54 before tax. Explain how to find a 15% tip using mental math, and give the tip.","pts":3,"min":15,"rows":2,"rubric":["10% = $5.40, 5% = half of that = $2.70","Tip = $8.10"],"model":"10% of $54 is $5.40. Half of that is 5%, $2.70. Add them: 15% is $8.10."}]},
   {"title": "Part D: Converting units and currency", "items": [
    {"t":"num","q":"How many inches are in 3 1/2 feet?","a":42,"unit":"inches","pts":3,"why":"3.5 × 12 = 42."},
    {"t":"num","q":"How many quarts are in 7 1/2 gallons?","a":30,"unit":"quarts","pts":3,"why":"Smaller unit, so multiply: 7.5 × 4 = 30 quarts."},
    {"t":"num","q":"Convert 875 centimeters to meters.","a":8.75,"unit":"meters","pts":3,"why":"875 ÷ 100 = 8.75 m."},
    {"t":"num","q":"At 1 USD = 18 Mexican pesos, how many U.S. dollars is 630 pesos?","a":35,"unit":"dollars","show":"$35","pts":3,"why":"630 ÷ 18 = $35."},
    {"t":"open","key":"cp_reason","q":"The co-op needs 5 liters of fruit punch for a picnic. Each packet of mix makes 750 milliliters and costs $1.20. How many packets must they buy, and what is the cost? Explain each step.","pts":4,"min":25,"rows":3,"rubric":["5 L = 5,000 mL","5,000 ÷ 750 ≈ 6.7, so 7 packets (6 packets make only 4,500 mL)","7 × $1.20 = $8.40"],"model":"5 liters = 5,000 milliliters. 5,000 ÷ 750 is about 6.7, and 6 packets make only 4,500 mL, which is not enough, so they must buy 7 packets. Cost: 7 × $1.20 = $8.40."}]}]},
 "next": "Unit 4: integers and the coordinate plane, starting with integers, opposites and absolute value."
}

TEACHER = {
 "standards": [
  "MA.6.AR.3.4: Apply ratio relationships to solve mathematical and real-world problems involving percentages using the relationship between two quantities.",
  "MA.6.AR.3.5: Solve mathematical and real-world problems involving ratios, rates and unit rates, including comparisons, mixtures, ratios of lengths and conversions within the same measurement system.",
  "MA.K12.MTR.5.1: Use patterns and structure to help understand and connect mathematical concepts.",
  "MA.K12.MTR.7.1: Apply mathematics to real-world contexts.",
  "Financial literacy: budgeting, comparing shipping costs, sales tax and exchange rates (Jump$tart Spending)."],
 "materials": ["The interactive lesson", "5 or 6 household items, a scale or package weights, a ruler", "A store flyer or website with prices", "Paper, pencil, a calculator for checking only", "The Unit 3 checkpoint (in the lesson)"],
 "flow": [
  [6, "Reconnect", "Run one question from each week of the unit."],
  [4, "Hook", "Introduce the care package and the toolkit chart."],
  [9, "Unit rates", "Compare pencil packs; review speed with a mixed number."],
  [12, "Percents", "Work the discount-then-tax, markup, original price and tip problems."],
  [9, "Conversions and currency", "Review multiply-or-divide; fix Tomás's mistake."],
  [6, "Money review", "Compare shipping by weight with a flat rate; find the break-even weight."],
  [4, "Assign", "Assign the care package plan and Think Deeper."],
  [10, "Checkpoint preview", "Explain that the checkpoint is completed after class, independently, one try per item, with no answers shown until you review it. Mastery is 85; below 85 means a review lesson and a retake."]],
 "key_questions": ["A rate per one, a percent of what, cost or price, or which units?", "Is the answer reasonable?", "Which shipping choice is cheaper for this weight?", "Did you round money correctly?"],
 "misconceptions": ["Subtracting percents of different wholes (discount minus tax).", "Taking markup as a percent of the selling price.", "Multiplying when converting to a larger unit.", "Rounding down when you must buy whole rolls or boxes."],
 "support": ["Keep the toolkit chart visible.", "Allow ratio tables for every percent and conversion problem.", "Break the care package into one step per line."],
 "challenge": ["Find a real shipping rate to Jamaica online with a parent and redo the comparison.", "Write two checkpoint-style problems of your own, with answer keys."],
 "background": "<p>Shipping prices, the $60 budget and the 155 JMD exchange rate are illustrative examples, not real carrier rates or current market rates. Checkpoint total: 52 points (Parts A to D). Rounding: Florida carries sales tax to the third decimal place and rounds up to the next whole cent when the third decimal place is greater than 4, so $2.025 becomes $2.03.</p>",
 "sources": ["Florida Department of Revenue, Florida Sales and Use Tax (GT-800013).", "NIST Handbook 44, Appendix C.", "Jump$tart Coalition, National Standards for Personal Financial Education."]
}

PRINT = {
 "directions": "Mid-year review. Show your work.",
 "items": [
  {"q":"Find the unit price: 18 ounces of cereal for $4.14.","a":"$0.23 per ounce.","lines":1},
  {"q":"What is 35% of $140? 28 is 70% of what number?","a":"$49; 40.","lines":2},
  {"q":"A $90 telescope is 40% off, and 7.5% tax is added to the sale price. What is the total?","a":"Sale $54; tax $4.05; total $58.05.","lines":2},
  {"q":"A shop buys a board game for $25 and sells it for $35. What is the markup percent?","a":"$10 ÷ $25 = 40%.","lines":1},
  {"q":"Convert: 5 yards to inches; 2.6 kilograms to grams; 10 quarts to gallons.","a":"180 inches; 2,600 grams; 2.5 gallons.","lines":2},
  {"q":"At 1 USD = 1.40 Canadian dollars (CAD), how many Canadian dollars is $150? How many U.S. dollars is 84 CAD?","a":"150 × 1.40 = 210 CAD; 84 ÷ 1.40 = $60.","lines":2}]
}
