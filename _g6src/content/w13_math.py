def tape(total, pct, title, label_left, label_right):
    parts = 10; w = 52; x0 = 60
    each = total / parts; shaded = int(pct / 10)
    s = (f'<svg viewBox="0 0 640 200" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="{title}">'
         f'<text x="320" y="22" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">{title}</text>'
         f'<text x="{x0 + parts*w/2}" y="50" text-anchor="middle" font-weight="bold">Original price: ${total:g} = 100%</text>'
         f'<path d="M{x0} 58 v-6 h{parts*w} v6" fill="none" stroke="#0A1F3D"/>')
    for i in range(parts):
        fill = "#DB2F30" if i < shaded else "#cfe0f7"
        s += f'<rect x="{x0+i*w}" y="62" width="{w}" height="46" fill="{fill}" stroke="#0A1F3D"/><text x="{x0+i*w+w/2}" y="90" text-anchor="middle" font-size="12" fill="{"#fff" if i < shaded else "#0A1F3D"}">${each:g}</text>'
    s += (f'<path d="M{x0} 114 v6 h{shaded*w} v-6" fill="none" stroke="#DB2F30"/><text x="{x0+shaded*w/2}" y="138" text-anchor="middle" fill="#DB2F30" font-weight="bold">{label_left}</text>'
          f'<path d="M{x0+shaded*w} 114 v6 h{(parts-shaded)*w} v-6" fill="none" stroke="#0047BA"/><text x="{x0+shaded*w+(parts-shaded)*w/2}" y="138" text-anchor="middle" fill="#0047BA" font-weight="bold">{label_right}</text>'
          f'<text x="320" y="176" text-anchor="middle" font-size="12" fill="#5b6676">Each block is 10% of the price. Two ways: subtract the discount, or pay the percent that is left.</text></svg>')
    return s

MARKUP = ('<svg viewBox="0 0 640 200" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Markup bar model: cost plus markup equals selling price">'
  '<text x="320" y="22" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Markup: from what it costs to what it sells for</text>'
  + ''.join(f'<rect x="{60+i*48}" y="50" width="48" height="44" fill="#3d9a2f" stroke="#0A1F3D"/><text x="{84+i*48}" y="77" text-anchor="middle" fill="#fff" font-size="12">25%</text>' for i in range(4))
  + ''.join(f'<rect x="{252+i*48}" y="50" width="48" height="44" fill="#C9A84C" stroke="#0A1F3D"/><text x="{276+i*48}" y="77" text-anchor="middle" font-size="12">25%</text>' for i in range(3)) +
  '<path d="M60 100 v6 h192 v-6" fill="none" stroke="#3d9a2f"/><text x="156" y="124" text-anchor="middle" font-weight="bold" fill="#2c6e22">Cost: $8 (100%)</text>'
  '<path d="M252 100 v6 h144 v-6" fill="none" stroke="#8a6d1f"/><text x="324" y="124" text-anchor="middle" font-weight="bold" fill="#8a6d1f">Markup: 75% = $6</text>'
  '<path d="M60 40 v-6 h336 v6" fill="none" stroke="#0A1F3D"/><text x="228" y="30" text-anchor="middle" font-weight="bold">Selling price: $14 (175% of cost)</text>'
  '<text x="420" y="62" font-size="12">Each block = 25% of $8 = $2</text><text x="420" y="80" font-size="12">Cost: 4 blocks = $8</text><text x="420" y="98" font-size="12">Markup: 3 blocks = $6</text>'
  '<text x="320" y="164" text-anchor="middle" font-size="12" fill="#5b6676">The markup percent is always a percent of the COST, not of the selling price.</text>'
  '<text x="320" y="182" text-anchor="middle" font-size="12" fill="#5b6676">Kiara\'s crocheted plant hanger: $8 of supplies, sold for $14.</text></svg>')

TIPS = ('<svg viewBox="0 0 640 210" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Tip shortcuts built from 10 percent">'
  '<text x="320" y="22" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Tip shortcuts on a $48 bill: start with 10%</text>'
  + ''.join(f'<rect x="{40+i*150}" y="44" width="134" height="112" rx="10" fill="{c}"/><text x="{107+i*150}" y="74" text-anchor="middle" fill="#fff" font-weight="bold" font-size="18">{p}</text><text x="{107+i*150}" y="100" text-anchor="middle" fill="#fff" font-size="12">{how}</text><text x="{107+i*150}" y="138" text-anchor="middle" fill="#fff" font-weight="bold" font-size="18">{amt}</text>'
            for i, (p, how, amt, c) in enumerate([("10%", "move the decimal left", "$4.80", "#0A1F3D"), ("5%", "half of 10%", "$2.40", "#0047BA"), ("15%", "10% + 5%", "$7.20", "#3d9a2f"), ("20%", "double 10%", "$9.60", "#DB2F30")])) +
  '<text x="320" y="184" text-anchor="middle" font-size="12" fill="#5b6676">In the United States, diners usually tip 15% to 20% of the bill before tax at a sit-down restaurant.</text>'
  '<text x="320" y="200" text-anchor="middle" font-size="12" fill="#5b6676">Estimate first, then calculate.</text></svg>')

LESSON = {
 "unit": "Unit 3: Rates and Percents",
 "title": "Percents in Real Life: Discounts, Markups and Tips",
 "subtitle": "Stores mark prices up and then mark them down, and restaurants expect a tip. Knowing how these percents work lets you spot a real deal, price your own product and pay fairly.",
 "objectives": [
  "Find a sale price after a percent discount in two ways: by subtracting the discount and by paying the percent that is left.",
  "Find an original price from a sale price and a discount percent.",
  "Find a selling price from a cost and a markup percent, and find a markup percent from a cost and a price.",
  "Calculate tips with mental-math shortcuts built from 10%.",
  "Compare deals (percent off, dollars off, buy one get one) and explain which saves more and when."],
 "vocab": [
  ["discount", "An amount taken off a price, often written as a percent off."],
  ["sale price", "The price after the discount is subtracted."],
  ["original price", "The regular price before a discount."],
  ["cost", "What a seller pays to make or buy an item."],
  ["markup", "The amount a seller adds to the cost to set the selling price; markup percent is a percent of the cost."],
  ["profit", "The money left after costs are paid: selling price minus cost."],
  ["tip (gratuity)", "Extra money given to a server or worker for good service, usually a percent of the bill."]],
 "reconnect": {
  "title": "Week 12: Understanding percents",
  "intro": "Every problem today starts with the percent skills from last week.",
  "items": [
   {"t":"num","q":"What is 30% of $70?","a":21,"unit":"dollars","show":"$21","pts":2,"why":"10% = $7, so 30% = 3 × $7 = $21."},
   {"t":"num","q":"18 is 45% of what number?","a":40,"pts":2,"why":"45% → 18, so 5% → 2, so 100% → 40."},
   {"t":"blanks","q":"Complete the conversions.","sent":"0.08 = ___% &nbsp; 3/5 = ___%","blanks":[["8"],["60"]],"show":"8; 60","pts":2,"why":"0.08 × 100 = 8%; 3/5 = 60/100 = 60%."},
   {"t":"num","q":"Find the sales tax on a $36 purchase at 7.5%.","a":2.7,"unit":"dollars","show":"$2.70","pts":2,"why":"$36 × 0.075 = $2.70."}]},
 "hook": {
  "title": "Is It Really the Same Deal?",
  "html": "<p>Two shoe stores are having sales. <b>Store A:</b> 25% off everything. <b>Store B:</b> Buy one pair, get the second pair 50% off.</p><p>You need two pairs of running shoes that each cost $40. At Store A you pay 75% of $80, which is $60. At Store B you pay $40 for the first pair and $20 for the second, also $60. Same deal!</p><p>But now suppose one pair costs $50 and the other costs $30. Stores almost always take the 50% off the cheaper pair. Is it still the same deal? And what if you only need one pair? By the end of this lesson you will be able to answer like a smart shopper.</p><div class='callout'><b>Big idea:</b> Every deal is a percent of some whole. Ask: a percent of what?</div>"},
 "learn": [
  {"title": "Discounts and Sale Prices",
   "visual": tape(60, 30, "A $60 jacket at 30% off", "Discount: 30% = $18", "You pay: 70% = $42"),
   "html": "<p>A <b>discount</b> is money taken off the price. To find a sale price, you can:</p><ul><li><b>Subtract the discount:</b> 30% of $60 is $18, and $60 − $18 = $42.</li><li><b>Pay the percent that is left:</b> 30% off means you pay 70%. 70% of $60 = 0.7 × $60 = $42.</li></ul><p>The second way is one step, and it is the way most cashiers' registers think.</p><p><b>Working backward:</b> if you know the sale price and the percent off, you can find the original price. A sale price of $36 at 40% off means $36 is 60% of the original. 60% → $36, so 10% → $6, so 100% → $60.</p>",
   "checks": [
    {"t":"num","q":"A $45 bike helmet is 20% off. What is the sale price?","a":36,"unit":"dollars","show":"$36","pts":2,"why":"You pay 80%: 0.8 × $45 = $36."},
    {"t":"num","q":"A $24 book is 35% off. What do you pay? Use the pay-what-is-left method.","a":15.6,"unit":"dollars","show":"$15.60","pts":2,"why":"You pay 65%: 0.65 × $24 = $15.60."},
    {"t":"num","q":"A telescope is on sale for $54, which is 25% off. What was the original price?","a":72,"unit":"dollars","show":"$72","pts":3,"why":"$54 is 75% of the original. 75% → $54, 25% → $18, 100% → $72."},
    {"t":"num","q":"A $100 rain jacket is 30% off. At the register you get an extra 20% off the sale price. What do you pay?","a":56,"unit":"dollars","show":"$56","pts":3,"why":"70% of $100 = $70. Then 80% of $70 = $56."},
    {"t":"open","key":"stack","q":"Sofia says 30% off and then an extra 20% off is the same as 50% off. Use the rain jacket to explain whether she is right.","min":25,"rows":3,"rubric":["Not right: 50% off would be $50, but the price is $56 (44% off)","The extra 20% is a percent of the smaller sale price, not of the original price"],"model":"She is not right. 50% off $100 would be $50, but you actually pay $56, which is 44% off. The extra 20% is taken from the $70 sale price, not from the original $100, so it saves only $14, not $20."}]},
  {"title": "Markups: How Sellers Set Prices",
   "visual": MARKUP,
   "html": "<p>A store or a small business pays a <b>cost</b> for each item. To pay for rent, workers, shipping and its own time, and to earn a <b>profit</b>, it adds a <b>markup</b>.</p><p>Kiara, a homeschooled 12-year-old, crochets plant hangers and sells them online. The yarn and wooden rings for one hanger cost $8. She uses a 75% markup: 75% of $8 is $6, so she sells each hanger for $8 + $6 = $14. Her profit on each one is $6.</p><p>To find a <b>markup percent</b>, compare the markup to the cost: a book that costs a shop $12 and sells for $18 has a $6 markup. $6 ÷ $12 = 0.5 = 50%.</p><div class='callout'>Markup percent is a percent of the <b>cost</b>. Discount percent is a percent of the <b>original price</b>. Always ask: a percent of what?</div>",
   "checks": [
    {"t":"num","q":"A bike shop pays $250 for a bike and uses a 40% markup. What is the selling price?","a":350,"unit":"dollars","show":"$350","pts":2,"why":"40% of $250 = $100; $250 + $100 = $350 (or 1.4 × $250)."},
    {"t":"num","q":"A shop buys a puzzle for $15 and sells it for $24. What is the markup percent?","a":60,"unit":"%","pts":3,"why":"Markup $9; $9 ÷ $15 = 0.6 = 60%."},
    {"t":"num","q":"Kiara's supplies for a set of coasters cost $6. She sells the set for $15. What is her profit?","a":9,"unit":"dollars","show":"$9","pts":2,"why":"$15 − $6 = $9."},
    {"t":"open","key":"whymarkup","q":"A shopper says, \"The store buys this lamp for $20 and sells it for $35. That's a rip-off!\" Explain why stores need a markup, using at least two costs from the lesson.","min":25,"rows":3,"rubric":["The store must pay for more than the item: rent, workers, shipping","Some profit is needed to stay in business"],"model":"The $15 markup is not all profit. The store has to pay rent for the building, wages for workers and shipping to get the lamp there. If it sold the lamp for $20, it would lose money and close."}]},
  {"title": "Tips: Paying for Good Service",
   "visual": TIPS,
   "html": "<p>At a sit-down restaurant in the United States, diners usually leave a <b>tip</b> of 15% to 20% of the bill, figured on the amount before tax. Tips are a large part of servers' pay; in Florida, restaurants may pay tipped workers a lower hourly wage because tips are expected to make up the difference.</p><p>You can find most tips in your head by starting with 10%:</p><ul><li>10%: move the decimal point one place left. 10% of $48 = $4.80.</li><li>5%: half of 10%. 5% of $48 = $2.40.</li><li>15% = 10% + 5% = $7.20.</li><li>20% = double 10% = $9.60.</li></ul><p>Many people round a tip to a convenient amount, such as $7.25 or $10.</p>",
   "checks": [
    {"t":"num","q":"Find a 20% tip on a $45 bill.","a":9,"unit":"dollars","show":"$9","pts":2,"why":"10% = $4.50; double it: $9."},
    {"t":"num","q":"Find a 15% tip on a $38 bill.","a":5.7,"unit":"dollars","show":"$5.70","pts":2,"why":"10% = $3.80; 5% = $1.90; total $5.70."},
    {"t":"num","q":"A family's bill is $62.40 before tax. They leave a 20% tip. How much is the tip?","a":12.48,"unit":"dollars","show":"$12.48","pts":2,"why":"10% = $6.24; double it: $12.48."},
    {"t":"open","key":"tipest","q":"Explain how you would estimate an 18% tip on a $51 bill in your head. Give your estimate.","min":25,"rows":3,"rubric":["A sensible strategy (round $51 to $50; 20% of $50 = $10, then a little less; or 10% + 5% + a bit)","An estimate near $9.18 (about $9)"],"model":"I would round $51 to $50. 20% of $50 is $10, and 18% is a little less, so about $9. The exact tip is $9.18."}]},
  {"title": "Money: Which Deal Is Better?",
   "html": "<p>Smart shoppers compare deals by working out the dollars, not by trusting the biggest number on the sign.</p><p><b>Percent off or dollars off?</b> A $10-off coupon saves $10 no matter the price. A 20%-off coupon saves more on expensive items and less on cheap ones. On a $40 item, 20% is $8, so $10 off is better. On a $70 item, 20% is $14, so 20% off is better.</p><p><b>Discount and tax:</b> in Florida, sales tax is figured on the sale price. Shoes for $80 at 25% off cost $60, plus 7.5% tax ($4.50), for $64.50.</p>",
   "checks": [
    {"t":"num","q":"A $10-off coupon and a 20%-off coupon save the same amount at one price. What is that price?","a":50,"unit":"dollars","show":"$50","pts":3,"why":"$10 is 20% of the price. 20% → $10, so 100% → $50."},
    {"t":"num","q":"A $90 tent is 30% off. Sales tax is 7.5% of the sale price. What is the total cost? Round to the nearest cent.","a":67.73,"unit":"dollars","show":"$67.73","pts":3,"why":"Sale price: 0.7 × $90 = $63. Tax: $63 × 0.075 = $4.725, about $4.73. Total: $67.73."},
    {"t":"open","key":"order","q":"For the $80 shoes, Malik adds the 7.5% tax first ($86) and then takes 25% off. Does he get the same total, $64.50? Calculate, then explain why.","min":30,"rows":3,"rubric":["Calculates 75% of $86 = $64.50, the same total","Explains that both orders multiply $80 by 0.75 and by 1.075, and the order of multiplication does not change the product"],"model":"Yes: 75% of $86 is $64.50, the same total. Both ways multiply $80 by 0.75 and by 1.075, and you can multiply numbers in any order and get the same product."}]}],
 "handson": {
  "title": "Run a Sale: The Price-Tag Store",
  "intro": "Turn a table into a store. You set the prices and the sale signs, a family member shops, and you are the cashier.",
  "materials": ["8 safe household items (a book, a mug, a stuffed animal, a cap, a game and so on)", "Sticky notes or paper slips and a marker for price tags and sale signs", "Paper and pencil for the cashier's work", "Optional: play money or paper slips for $1, $5, $10 and $20", "A calculator for checking only"],
  "steps": [
   "Make a price tag for each item with a whole-dollar \"regular price\" between $4 and $40.",
   "Put sale signs on four items: 10% off, 25% off, 40% off and $5 off.",
   "A family member shops with a $60 budget and chooses items. As the cashier, work out each sale price on paper and keep a running total. Tell the shopper if they go over budget.",
   "Switch roles: the family member sets new sale signs, and you shop. Try to buy as many items as you can for $60 or less.",
   "Challenge: add 7.5% sales tax to your final total. Do you still fit the budget?"],
  "record": [
   {"t":"open","key":"storerec","q":"Write each item the shopper bought, its regular price, its sale sign and its sale price, and the total. Show your work for two of the sale prices.","min":40,"rows":5,"rubric":["Items with regular and sale prices listed","Correct sale prices","Correct total compared with the $60 budget","Work shown for two items"],"model":"Book $20, 25% off: pay 75% = $15. Mug $12, $5 off: $7. Cap $18, 10% off: pay 90% = $16.20. Game $30, 40% off: pay 60% = $18. Total: $56.20, which is under $60."},
   {"t":"open","key":"storesign","q":"Which sale sign saved the shopper the most money? Was it the sign with the biggest number? Explain.","min":25,"rows":3,"rubric":["Names the sign with the largest dollar savings","Explains that savings depend on the regular price as well as the percent"],"model":"40% off the $30 game saved $12, the most. But $5 off the mug saved more than 10% off the cap, which saved only $1.80, so the size of the savings depends on the price, not just on the number on the sign."}]},
 "think": {
  "intro": "Show your calculations, then explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"bogo","q":"Return to the hook. You need running shoes costing $50 and $30. Store A has 25% off everything. Store B has buy one, get the second 50% off (taken off the cheaper pair). Which store is cheaper, and by how much? Then explain when Store B's deal would be just as good as Store A's.","min":70,"rows":6,"rubric":["Store A: 75% of $80 = $60","Store B: $50 + $15 = $65","Store A is cheaper by $5","Store B matches only when both pairs cost the same (or explains that the discount shrinks when the cheaper pair costs less)"],"model":"Store A: 75% of $80 = $60. Store B: $50 + half of $30 = $50 + $15 = $65. Store A is $5 cheaper. Store B's deal is only as good when both pairs cost the same, because then the 50% off one pair equals 25% off the total. When the second pair is cheaper, Store B's discount is smaller."},
   {"t":"open","key":"profit","q":"Kiara sells 20 plant hangers a month at $14 each (supplies $8 each). If she raises her markup to 100%, she expects to sell only 14 a month. Which markup earns her more profit each month? Show your work and say what else she might consider.","min":70,"rows":6,"rubric":["75% markup: $6 profit × 20 = $120","100% markup: price $16, $8 profit × 14 = $112","The 75% markup earns more","A thoughtful extra consideration (time spent crocheting, customers, materials, demand changes)"],"model":"At a 75% markup, her profit is $6 each, and $6 × 20 = $120. At a 100% markup, the price is $16, her profit is $8 each, and $8 × 14 = $112. The 75% markup earns $8 more. But at 100% she crochets 6 fewer hangers, so she saves time and yarn; she might decide that free time is worth $8."}]},
 "exit": [
  {"t":"num","q":"A $56 game is 25% off. What is the sale price?","a":42,"unit":"dollars","show":"$42","pts":2,"why":"You pay 75%: 0.75 × $56 = $42."},
  {"t":"num","q":"Find a 20% tip on a $35 bill.","a":7,"unit":"dollars","show":"$7","pts":2,"why":"10% = $3.50; double it: $7."},
  {"t":"num","q":"An item costs a store $20. The store uses a 60% markup. What is the selling price?","a":32,"unit":"dollars","show":"$32","pts":2,"why":"60% of $20 = $12; $20 + $12 = $32."},
  {"t":"num","q":"After 25% off, a backpack costs $27. What was the original price?","a":36,"unit":"dollars","show":"$36","pts":2,"why":"$27 is 75% of the original: 75% → $27, 25% → $9, 100% → $36."}],
 "next": "Week 14: converting units with ratios, and currency exchange."
}

TEACHER = {
 "standards": [
  "MA.6.AR.3.4: Apply ratio relationships to solve mathematical and real-world problems involving percentages using the relationship between two quantities.",
  "MA.6.AR.3.5: Solve mathematical and real-world problems involving ratios, rates and unit rates, including comparisons, mixtures, ratios of lengths and conversions within the same measurement system.",
  "MA.K12.MTR.2.1: Demonstrate understanding by representing problems in multiple ways.",
  "MA.K12.MTR.7.1: Apply mathematics to real-world contexts.",
  "Financial literacy: discounts, markups, profit and tipping; comparing deals (Jump$tart Spending)."],
 "materials": ["The interactive lesson", "8 household items, sticky notes and a marker", "Paper and pencil; optional play money", "A calculator for checking only", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 12 Reconnect questions."],
  [5, "Hook", "Pose the two shoe stores. Let the student predict before calculating the $40 + $40 case."],
  [12, "Discounts", "Build the tape diagram. Practice both methods; work one original-price problem backward. Discuss the stacked discount."],
  [12, "Markups", "Walk through Kiara's hanger. Find a markup percent. Contrast \"percent of the cost\" with \"percent of the price.\""],
  [9, "Tips", "Practice the 10%, 5%, 15% and 20% shortcuts mentally before writing."],
  [10, "Which deal is better?", "Compare $10 off with 20% off. Show that discount-then-tax equals tax-then-discount."],
  [6, "Assign", "Set up the price-tag store together; assign the shopping rounds, Think Deeper and the Exit Check."]],
 "key_questions": ["A percent of what?", "Which method is faster: subtract the discount, or pay what is left?", "Does the biggest number on a sign always save the most?", "Why is 30% off and then 20% off not 50% off?"],
 "misconceptions": ["Adding successive discounts (30% + 20% = 50%).", "Finding an original price by adding the discount percent to the sale price (for example, $54 + 25% of $54).", "Figuring markup as a percent of the selling price instead of the cost.", "Thinking a bigger percent always means bigger savings."],
 "support": ["Use 10-block tape diagrams for every discount.", "Start each problem by writing \"percent of ___.\"", "Practice tips only with 10% and 20% before adding 15%."],
 "challenge": ["Find the single discount equal to 25% off followed by 20% off (40%), and explain why.", "Research the tip credit for tipped workers in Florida and calculate a server's hourly pay with and without tips for one evening."],
 "background": "<p>Discount: sale price = original × (1 − rate). Markup: price = cost × (1 + rate); markup percent is based on cost (retailers sometimes quote margin, a percent of price, instead; this lesson uses markup on cost only). Successive discounts multiply: 0.7 × 0.8 = 0.56, a 44% total discount. Discount and tax commute because both are multiplications: 80 × 0.75 × 1.075 = 80 × 1.075 × 0.75 = 64.5. In Florida, sales tax applies to the price after a store discount; manufacturers' coupons are handled differently, which this lesson does not address. U.S. tipping convention at sit-down restaurants is about 15% to 20% of the pre-tax bill. Florida allows employers a tip credit, so tipped employees may be paid a lower direct hourly wage than the state minimum, with tips making up the difference.</p>",
 "sources": ["Florida Department of Revenue, Sales and Use Tax on retail sales (discounts and coupons).", "Florida Department of Economic Opportunity, Florida Minimum Wage notice (tipped employees).", "Jump$tart Coalition, National Standards for Personal Financial Education (Spending)."]
}

PRINT = {
 "directions": "Show your work.",
 "items": [
  {"q":"A $80 scooter is 15% off. Find the sale price in two ways.","a":"Discount $12, $80 − $12 = $68; or 85% of $80 = $68.","lines":2},
  {"q":"A sale price of $42 is 30% off. What was the original price?","a":"$42 is 70%; 10% = $6; original $60.","lines":2},
  {"q":"A shop pays $30 for a lamp and uses a 50% markup. Find the selling price and the profit.","a":"Price $45; profit $15.","lines":2},
  {"q":"A craft fair seller buys supplies for $5 and sells the item for $8. What is the markup percent?","a":"$3 ÷ $5 = 60%.","lines":2},
  {"q":"Find 15% and 20% tips on a $64 bill.","a":"15%: $9.60; 20%: $12.80.","lines":2},
  {"q":"Which saves more on a $35 sweater: $8 off or 20% off? Explain.","a":"20% = $7, so $8 off saves more.","lines":2}]
}
