def counters():
    s = ('<svg viewBox="0 0 560 150" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="A garden bed with 8 tomato plants and 12 pepper plants">'
         '<text x="280" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The garden bed: 8 tomato plants and 12 pepper plants</text>'
         '<rect x="20" y="34" width="520" height="86" rx="8" fill="#8a5a33"/>')
    for i in range(20):
        x = 50 + (i % 10) * 50; y = 58 + (i // 10) * 40
        if i < 8:
            s += f'<circle cx="{x}" cy="{y}" r="13" fill="#DB2F30"/><path d="M{x-4} {y-12} l4 -5 l4 5" fill="#2f7a2a"/>'
        else:
            s += f'<path d="M{x-7} {y-12} q-6 12 2 24 q5 3 10 0 q8 -12 2 -24 z" fill="#3d9a2f"/>'
    s += ('<circle cx="40" cy="138" r="6" fill="#DB2F30"/><text x="52" y="142">tomato</text>'
          '<path d="M128 132 q-4 6 1 12 q4 2 6 0 q4 -6 1 -12z" fill="#3d9a2f"/><text x="142" y="142">pepper</text></svg>')
    return s

def tape():
    s = ('<svg viewBox="0 0 560 170" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Tape diagram for a ratio of 2 to 3">'
         '<text x="280" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Tape diagram: tomatoes to peppers is 2 : 3</text>'
         '<text x="20" y="62" font-weight="bold" fill="#DB2F30">Tomatoes</text><text x="20" y="112" font-weight="bold" fill="#3d6b1f">Peppers</text>')
    for i in range(2):
        s += f'<rect x="{110+i*80}" y="42" width="80" height="32" fill="#f7c9c9" stroke="#DB2F30" stroke-width="2"/><text x="{150+i*80}" y="63" text-anchor="middle">4</text>'
    for i in range(3):
        s += f'<rect x="{110+i*80}" y="92" width="80" height="32" fill="#cfe8b0" stroke="#3d6b1f" stroke-width="2"/><text x="{150+i*80}" y="113" text-anchor="middle">4</text>'
    s += ('<text x="290" y="63">= 8</text><text x="370" y="113">= 12</text>'
          '<text x="280" y="150" text-anchor="middle" font-size="12">Each box is the same size. 5 boxes = 20 plants, so each box holds 4.</text></svg>')
    return s

DEALS = ('<svg viewBox="0 0 560 170" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Two price signs for mangoes">'
  '<text x="280" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Which deal is better?</text>'
  '<rect x="40" y="38" width="210" height="110" rx="8" fill="#fff8e1" stroke="#C9A84C" stroke-width="3"/><text x="145" y="64" text-anchor="middle" font-weight="bold" fill="#0A1F3D">Farmers market</text><text x="145" y="102" text-anchor="middle" font-size="26" font-weight="bold" fill="#DB2F30">3 for $4</text><text x="145" y="132" text-anchor="middle" font-size="12">mangoes</text>'
  '<rect x="310" y="38" width="210" height="110" rx="8" fill="#e8f0fb" stroke="#0047BA" stroke-width="3"/><text x="415" y="64" text-anchor="middle" font-weight="bold" fill="#0A1F3D">Grocery store</text><text x="415" y="102" text-anchor="middle" font-size="26" font-weight="bold" fill="#DB2F30">5 for $7</text><text x="415" y="132" text-anchor="middle" font-size="12">mangoes</text></svg>')

SCALE = ('<svg viewBox="0 0 560 190" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Scaling both deals to 15 mangoes">'
  '<text x="280" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Scale both deals to the same number of mangoes</text>'
  '<text x="30" y="58" font-weight="bold">Market</text><text x="30" y="128" font-weight="bold">Grocery</text>'
  + ''.join(f'<rect x="{110+i*88}" y="40" width="80" height="30" rx="5" fill="#fff8e1" stroke="#C9A84C"/><text x="{150+i*88}" y="60" text-anchor="middle">3 for $4</text>' for i in range(5)) +
  ''.join(f'<rect x="{110+i*147}" y="110" width="139" height="30" rx="5" fill="#e8f0fb" stroke="#0047BA"/><text x="{180+i*147}" y="130" text-anchor="middle">5 for $7</text>' for i in range(3)) +
  '<text x="280" y="92" text-anchor="middle" font-weight="bold" fill="#DB2F30">× 5 → 15 mangoes for $20</text><text x="280" y="162" text-anchor="middle" font-weight="bold" fill="#DB2F30">× 3 → 15 mangoes for $21</text>'
  '<text x="280" y="184" text-anchor="middle" font-size="12">Same number of mangoes, so compare the prices: $20 is less than $21.</text></svg>')

LESSON = {
 "unit": "Unit 2: Fractions and Ratios",
 "title": "Ratios and Ratio Language",
 "subtitle": "A ratio compares two amounts. Cooks, gardeners, builders and smart shoppers use ratios every day, and today you will too.",
 "objectives": [
  "Write a ratio three ways (a to b, a:b, a/b) and describe it in words.",
  "Tell the difference between part-to-part and part-to-whole ratios.",
  "Find equivalent ratios and write ratios in simplest form.",
  "Use a tape diagram to solve ratio problems.",
  "Compare two deals by scaling them to the same quantity."],
 "vocab": [
  ["ratio", "A comparison of two quantities, such as 2 cups of water for every 1 cup of rice."],
  ["part-to-part ratio", "A ratio that compares one part of a group to another part, like tomatoes to peppers."],
  ["part-to-whole ratio", "A ratio that compares one part to the whole group, like tomatoes to all plants."],
  ["equivalent ratios", "Ratios that show the same comparison, like 2:3 and 4:6."],
  ["simplest form", "A ratio whose two numbers have no common factor other than 1."],
  ["tape diagram", "A drawing of equal-sized boxes that shows the parts of a ratio."],
  ["scale", "To multiply (or divide) both quantities in a ratio by the same number."]],
 "reconnect": {
  "title": "Week 7: Dividing fractions",
  "intro": "Ratios use multiplication, division and common factors. Warm up first.",
  "items": [
   {"t":"num","q":"How many 3/4-cup servings are in 6 cups of rice?","a":8,"unit":"servings","pts":2,"why":"6 ÷ 3/4 = 6 × 4/3 = 24/3 = 8."},
   {"t":"text","q":"5/6 ÷ 2/3 = ? Type a mixed number.","a":["1 1/4"],"show":"1 1/4","pts":2,"why":"5/6 × 3/2 = 15/12 = 5/4 = 1 1/4."},
   {"t":"num","q":"What is the greatest common factor (GCF) of 18 and 24? (Week 5)","a":6,"pts":2,"why":"Factors of 18: 1, 2, 3, 6, 9, 18. Factors of 24: 1, 2, 3, 4, 6, 8, 12, 24. The greatest shared factor is 6. You will use the GCF to simplify ratios today."},
   {"t":"open","key":"rc_label","q":"Last week a 1/4-cup serving was on the rice label, but our family cooked 3/4 cup. In your own words, why is it important to compare the label serving with what your family really uses?","min":15,"rows":2,"rubric":["The real number of servings and the real cost per meal depend on the amount actually used"],"model":"Because the label's serving may be smaller than what we eat, so the bag gives fewer meals and each meal costs more than the label suggests."}]},
 "hook": {
  "title": "The Perfect Pot of Rice",
  "html": "<p>Many cooks make long-grain rice on the stove with <b>2 cups of water for every 1 cup of rice</b>. Cooking for a crowd? Use 4 cups of water for 2 cups of rice, or 6 for 3. The amounts change, but the comparison stays the same. That comparison is a <b>ratio</b>.</p><p>Ratios are everywhere: 1 can of juice concentrate to 3 cans of water, 3 parts sand to 1 part cement in mortar, 8 tomato plants to 12 peppers in a garden. Get the ratio wrong and the rice turns to mush or the mortar crumbles.</p><div class='callout'><b>Big idea:</b> A ratio is about the relationship between two amounts, not the amounts themselves.</div>"},
 "learn": [
  {"title": "Writing and Reading Ratios",
   "visual": counters(),
   "html": "<p>The garden bed has 8 tomato plants and 12 pepper plants. You can write the ratio of tomatoes to peppers three ways:</p><div class='callout'>8 to 12 &nbsp;&nbsp; 8 : 12 &nbsp;&nbsp; 8/12</div><p>Read each one as \"8 to 12.\" <b>Order matters.</b> Tomatoes to peppers is 8:12, but peppers to tomatoes is 12:8.</p><p>Ratio language also uses the words <b>for every</b> and <b>per</b>: \"For every 2 tomato plants there are 3 pepper plants.\"</p><p>There are two kinds of ratios:</p><ul><li><b>Part-to-part:</b> one part to another part. Tomatoes to peppers is 8:12.</li><li><b>Part-to-whole:</b> one part to the whole group. Tomatoes to all plants is 8:20.</li></ul><p>A part-to-whole ratio can also be written as a fraction of the group: 8/20 of the plants are tomatoes. A part-to-part ratio like 8/12 is <b>not</b> a fraction of the bed.</p>",
   "checks": [
    {"t":"blanks","q":"Use the garden bed to complete each ratio.","sent":"Peppers to tomatoes is ___ : ___. Peppers to all plants is ___ : ___.","blanks":[["12"],["8"],["12"],["20"]],"show":"12 : 8; 12 : 20","pts":4,"why":"Peppers come first in both. All plants = 8 + 12 = 20."},
    {"t":"open","key":"kind","q":"Is \"tomatoes to all plants\" a part-to-part or a part-to-whole ratio? Explain how you know.","min":12,"rows":2,"rubric":["Part-to-whole","It compares one group to the total of all groups"],"model":"Part-to-whole, because it compares the tomatoes (one part) to all the plants together (the whole)."},
    {"t":"open","key":"order","q":"Kofi says the ratio of tomatoes to peppers is 12:8. Explain his mistake.","min":12,"rows":2,"rubric":["He reversed the order; the first quantity named goes first, so it is 8:12"],"model":"He switched the order. Tomatoes are named first, so the tomato count comes first: 8:12."},
    {"t":"open","key":"notfrac","q":"The ratio of tomatoes to peppers is 8/12. Does that mean 8/12 of the plants are tomatoes? Explain.","min":15,"rows":2,"rubric":["No","8/12 compares part to part; the fraction of plants that are tomatoes is 8/20"],"model":"No. 8/12 compares tomatoes to peppers. The fraction of all the plants that are tomatoes is 8 out of 20, or 8/20."}]},
  {"title": "Equivalent Ratios and Simplest Form",
   "html": "<p>Ratios are equivalent when they make the same comparison. Multiply or divide <b>both</b> numbers by the same nonzero number:</p><div class='callout'>1 : 2 &nbsp;=&nbsp; 2 : 4 &nbsp;=&nbsp; 3 : 6 &nbsp;=&nbsp; 10 : 20 (rice : water)</div><p>To write a ratio in <b>simplest form</b>, divide both numbers by their GCF, just like simplifying a fraction. The GCF of 8 and 12 is 4, so 8 : 12 = 2 : 3. For every 2 tomato plants, there are 3 pepper plants.</p><p>Adding the same number to both parts does <b>not</b> make an equivalent ratio. 1 cup rice to 2 cups water is right; 2 cups rice to 3 cups water would make dry, crunchy rice.</p>",
   "checks": [
    {"t":"text","q":"Write 18 : 24 in simplest form.","a":["3:4","3 to 4","3/4"],"show":"3 : 4","pts":2,"why":"The GCF of 18 and 24 is 6. 18 ÷ 6 = 3 and 24 ÷ 6 = 4."},
    {"t":"text","q":"Write 45 : 30 in simplest form.","a":["3:2","3 to 2","3/2"],"show":"3 : 2","pts":2,"why":"The GCF is 15: 45 ÷ 15 = 3 and 30 ÷ 15 = 2. Keep it as 3:2; do not change it to a mixed number, because a ratio compares two amounts."},
    {"t":"num","q":"A juice label says to mix 1 can of concentrate with 3 cans of water. How many cans of water go with 4 cans of concentrate?","a":12,"unit":"cans","pts":2,"why":"1 : 3 = 4 : 12. Multiply both parts by 4."},
    {"t":"open","key":"addwrong","q":"Amara needs a bigger pot of rice. She changes 1 cup rice : 2 cups water to 2 cups rice : 3 cups water by adding 1 to each. Is her rice ratio the same? Explain and fix it.","min":20,"rows":3,"rubric":["Not the same; adding does not keep the comparison","Multiply both by 2: 2 cups rice to 4 cups water"],"model":"No. Adding 1 to each changes the comparison: 2:3 has less water per cup of rice than 1:2. She should multiply both by 2 to get 2 cups of rice and 4 cups of water."}]},
  {"title": "Solving Problems with Tape Diagrams",
   "visual": tape(),
   "html": "<p>A tape diagram uses equal boxes to show a ratio. Suppose a garden has tomatoes and peppers in the ratio 2 : 3 and 20 plants in all. Draw 2 boxes for tomatoes and 3 for peppers. That is 5 equal boxes for 20 plants, so each box is 20 ÷ 5 = 4 plants. Tomatoes: 2 × 4 = 8. Peppers: 3 × 4 = 12.</p><p>The same steps work for any ratio problem with a total: find the number of boxes, divide to find one box, then multiply.</p>",
   "checks": [
    {"t":"num","q":"A trail mix uses raisins and peanuts in the ratio 3 : 5. The bag holds 40 ounces. How many ounces are peanuts?","a":25,"unit":"ounces","pts":3,"why":"3 + 5 = 8 boxes. 40 ÷ 8 = 5 ounces per box. Peanuts: 5 × 5 = 25 ounces."},
    {"t":"num","q":"Mortar for a garden wall is 3 parts sand to 1 part cement. A builder uses 9 buckets of sand. How many buckets of cement are needed?","a":3,"unit":"buckets","pts":2,"why":"Sand is 3 boxes and cement is 1 box. 9 ÷ 3 = 3 buckets per box, so cement is 3 buckets."},
    {"t":"num","q":"The ratio of boys to girls in a homeschool co-op is 4 : 5. There are 12 boys. How many students are in the co-op in all?","a":27,"unit":"students","pts":3,"why":"4 boxes = 12 boys, so each box is 3. Girls: 5 × 3 = 15. Total: 12 + 15 = 27 (or 9 boxes × 3)."},
    {"t":"open","key":"tapeexplain","q":"Explain why, in a tape diagram, all the boxes must be the same size.","min":15,"rows":2,"rubric":["Each box stands for the same amount, so the ratio of box counts equals the ratio of amounts"],"model":"Each box has to stand for the same amount. If the boxes were different sizes, the number of boxes would not show the real ratio between the amounts."}]},
  {"title": "Money: Comparing Deals with Ratios",
   "visual": DEALS,
   "html": "<p>A price like \"3 for $4\" is a ratio: 3 mangoes to 4 dollars. To compare two deals fairly, make one of the quantities the <b>same</b> in both. The least common multiple of 3 and 5 is 15, so scale both deals to 15 mangoes.</p><div class='visual'>" + SCALE + "</div><p>The market sells 15 mangoes for $20 and the grocery store sells 15 for $21, so the farmers market is the better deal by $1 for every 15 mangoes. You did not have to find the price of one mango. Next week you will learn that shortcut, called the unit rate.</p><p>A better price is not always the better choice. If your family can eat only 3 mangoes before they spoil, buying 5 wastes food and money.</p>",
   "checks": [
    {"t":"open","key":"cans","q":"Store A sells 4 cans of beans for $3. Store B sells 6 cans for $5. Scale both deals to the same number of cans and decide which is the better deal. Show your work.","min":20,"rows":3,"rubric":["Common quantity 12 cans","A: 12 for $9; B: 12 for $10","Store A is the better deal"],"model":"The LCM of 4 and 6 is 12. Store A: 4 for $3 × 3 = 12 for $9. Store B: 6 for $5 × 2 = 12 for $10. Store A is the better deal."},
    {"t":"num","q":"Plantains are 2 for $1 at one stand and 7 for $4 at another. If you scale both to 14 plantains, how much do 14 cost at the cheaper stand?","a":7,"unit":"dollars","show":"$7","pts":3,"why":"2 for $1 × 7 = 14 for $7. 7 for $4 × 2 = 14 for $8. The cheaper price for 14 is $7."},
    {"t":"open","key":"notbetter","q":"A big box of 48 granola bars costs less per bar than a box of 12. Give two reasons a family might still choose the smaller box.","min":20,"rows":3,"rubric":["Two sensible reasons: they would expire or go stale before being eaten, not enough money now, no storage space, trying a new flavor, waste"],"model":"The bars might go stale before the family eats 48, and they might not have enough money right now or room in the pantry for the big box."}]}],
 "handson": {
  "title": "Mix and Taste: Do Equivalent Ratios Taste the Same?",
  "intro": "Make lemonade or juice from concentrate in different ratios and test whether equivalent ratios really taste the same.",
  "materials": ["Lemonade or juice concentrate (or lemon juice and sugar water)", "Water", "A measuring spoon or small cup used as a \"part\"", "Four clear cups labeled A to D", "A marker and paper"],
  "steps": [
   "Using the same scoop as one part, mix: Cup A 1 part concentrate : 3 parts water. Cup B 2 : 6. Cup C 1 : 5. Cup D 2 : 3.",
   "Before tasting, predict which cups will taste the same and which will be strongest and weakest.",
   "Have a family member set the cups in random order. Taste each one (rinse with water between sips) and rank them from strongest to weakest.",
   "Write each ratio in simplest form and compare with your ranking."],
  "record": [
   {"t":"open","key":"tastedata","q":"Record each cup's ratio, its simplest form, your prediction and your tasting rank. Did the results match your predictions?","min":30,"rows":5,"rubric":["Ratios and simplest forms recorded correctly (A 1:3, B 1:3, C 1:5, D 2:3)","Predictions and ranks recorded","Comparison of results with predictions"],"model":"A 1:3 and B 2:6 = 1:3 tasted the same, medium. C 1:5 was weakest. D 2:3 was strongest. My prediction was right except I thought C and D would be closer."},
   {"t":"open","key":"tastewhy","q":"Explain why Cup A and Cup B taste the same even though Cup B has more of everything. Then explain why Cup D is stronger.","min":30,"rows":3,"rubric":["A and B are equivalent (1:3 = 2:6): same amount of concentrate per part of water","D has 2 parts concentrate for only 3 parts water, which is more concentrate per part of water than 1:3 (2:6)"],"model":"Cup B has double the concentrate and double the water, so each sip has the same mix as Cup A: 1:3 and 2:6 are equivalent. Cup D has 2 parts concentrate for only 3 parts water. Compared with 2:6, it has the same concentrate but half the water, so it is stronger."}]},
 "think": {
  "intro": "Show your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"recipe","q":"A family recipe for jollof rice uses 3 cups of rice and 4 1/2 cups of broth for 6 people. You are cooking for 10. Use ratio reasoning to find how much rice and broth you need, and explain each step.","min":50,"rows":6,"rubric":["Finds rice for 1 or 2 people or uses a scale factor of 10/6","Rice: 5 cups; broth: 7 1/2 cups","Clear steps that keep the ratio of rice to broth the same"],"model":"For 6 people the recipe uses 3 cups of rice, so that is 1 cup for every 2 people. 10 people is 5 groups of 2, so I need 5 cups of rice. Broth is 4 1/2 cups for 6 people, which is 1 1/2 cups for every 2 people. 5 × 1 1/2 = 7 1/2 cups of broth. The ratio of rice to broth stays 3 : 4 1/2, or 2 : 3, because 5 : 7 1/2 is also 2 : 3."},
   {"t":"open","key":"dealpick","q":"Rice: Store A sells a 5-lb bag for $6. Store B sells a 2-lb bag for $3. Decide which is the better price per pound by scaling to the same number of pounds. Then name one situation where buying the other bag makes more sense.","min":45,"rows":5,"rubric":["Common quantity 10 lb: A $12, B $15","Store A is the better price","A sensible situation for buying the smaller bag (small family, limited money now, storage, trying a new kind)"],"model":"Scale to 10 pounds: Store A, 5 lb for $6 × 2 = 10 lb for $12. Store B, 2 lb for $3 × 5 = 10 lb for $15. Store A is the better price. But a person living alone who rarely cooks rice, or who has only $3 to spend today, might buy the 2-lb bag."}]},
 "exit": [
  {"t":"text","q":"A class has 9 girls and 6 boys. Write the ratio of boys to girls in simplest form.","a":["2:3","2 to 3","2/3"],"show":"2 : 3","pts":2,"why":"Boys come first: 6 : 9. The GCF is 3, so 6 : 9 = 2 : 3."},
  {"t":"text","q":"In the same class, write the ratio of girls to all students in simplest form.","a":["3:5","3 to 5","3/5"],"show":"3 : 5","pts":2,"why":"9 girls out of 15 students: 9 : 15 = 3 : 5. This is part-to-whole."},
  {"t":"num","q":"Paint is mixed 2 parts blue to 5 parts white. How much white paint goes with 6 cups of blue?","a":15,"unit":"cups","pts":2,"why":"2 : 5 = 6 : 15 (multiply both by 3)."},
  {"t":"open","key":"exit_deal","q":"Which is the better deal: 3 notebooks for $5 or 4 notebooks for $6? Show how you scaled.","min":12,"rows":2,"rubric":["12 notebooks: $20 versus $18","4 for $6 is the better deal"],"model":"Scale to 12: 3 for $5 × 4 = 12 for $20; 4 for $6 × 3 = 12 for $18. 4 for $6 is the better deal."}],
 "next": "Week 9: ratio tables and equivalent ratios, plus unit prices and better buys."
}

TEACHER = {
 "standards": [
  "MA.6.AR.4.1: Given a real-world context, write and interpret ratios to show the relationship between two quantities using appropriate notation: a/b, a to b, or a:b where b ≠ 0.",
  "MA.6.AR.4.3: Extend previous understanding of fractions and numbers to apply ratio and rate reasoning to solve real-world problems (tables, tape diagrams, double number lines).",
  "MA.6.NSO.3.1 (review): Given a mathematical or real-world context, find the greatest common factor and least common multiple of two whole numbers.",
  "MA.K12.MTR.2.1: Demonstrate understanding by representing problems in multiple ways.",
  "Financial literacy: comparing prices and making buying decisions (Jump$tart Spending)."],
 "materials": ["The interactive lesson", "20 counters or dry beans in two colors", "Juice or lemonade concentrate, water, a measuring scoop, four clear cups", "Two grocery ads or receipts with multi-buy prices (\"3 for $5\")", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 7 Reconnect questions."],
  [5, "Hook", "Rice and water. If possible, show a real bag's cooking directions."],
  [10, "Ratio language", "Lay out 8 red and 12 green beans. Name part-to-part and part-to-whole ratios aloud, in both orders."],
  [10, "Equivalent ratios", "Group the beans into 4 equal groups to show 8 : 12 = 2 : 3. Discuss why adding does not work."],
  [10, "Tape diagrams", "Draw the 2 : 3 tape for 20 plants, then the trail mix problem."],
  [10, "Deals", "Scale the mango deals to 15. Find a multi-buy price in a real ad and compare."],
  [9, "Mix and taste", "Start the taste test together; the student finishes the record."]],
 "key_questions": ["Which quantity comes first, and why does it matter?", "Is this part-to-part or part-to-whole?", "What did you multiply both parts by?", "Is the cheaper price always the better choice?"],
 "misconceptions": ["Reversing the order of a ratio.", "Treating a part-to-part ratio as a fraction of the whole.", "Adding the same number to both parts to make an equivalent ratio.", "Converting a ratio like 3 : 2 to a mixed number.", "Assuming the bigger package is always the better deal."],
 "support": ["Use two colors of beans for every problem.", "Provide a blank tape diagram template.", "Keep a GCF list for numbers up to 50 handy."],
 "challenge": ["Find three multi-buy deals in a grocery ad and rank them.", "A recipe uses flour, sugar and butter in the ratio 4 : 2 : 1. How much of each for a batch using 3 1/2 cups total?"],
 "background": "<p>Florida's B.E.S.T. benchmarks place ratio concepts in MA.6.AR.4. This lesson focuses on ratio notation and language (MA.6.AR.4.1) and on tape-diagram reasoning (part of MA.6.AR.4.3); unit rates (MA.6.AR.4.2) come next week, so deals are compared by scaling to a common quantity rather than by dividing. Verify exact benchmark wording on CPALMS before printing. The 1 : 2 rice-to-water ratio is a common stovetop guideline for long-grain white rice; package directions vary. Mortar mixes around 3 : 1 sand to cement are typical for general masonry. The juice concentrate ratio of 1 can concentrate to 3 cans water is standard on US frozen concentrate labels.</p>",
 "sources": ["CPALMS, MA.6.AR.4 benchmarks.", "Illustrative Mathematics Grade 6, Unit 2: Introducing Ratios.", "Jump$tart Coalition, National Standards for Personal Financial Education (Spending)."]
}

PRINT = {
 "directions": "Show your work.",
 "items": [
  {"q":"A fruit bowl has 6 bananas and 10 oranges. Write the ratio of oranges to bananas three ways.","a":"10 to 6, 10 : 6, 10/6 (simplest 5 : 3)","lines":2},
  {"q":"Write the ratio of bananas to all fruit in simplest form.","a":"6 : 16 = 3 : 8","lines":1},
  {"q":"Write 28 : 42 in simplest form.","a":"2 : 3 (GCF 14)","lines":1},
  {"q":"Soil mix is 3 parts potting soil to 2 parts compost. How much compost goes with 12 cups of soil?","a":"8 cups","lines":2},
  {"q":"Beads are red and gold in the ratio 5 : 3. There are 48 beads. How many are gold? Draw a tape diagram.","a":"8 boxes, 6 each; gold = 18","lines":3},
  {"q":"Which is the better deal: 6 eggs for $2 or 10 eggs for $3? Scale to the same number of eggs.","a":"30 eggs: $10 vs $9; 10 for $3 is better","lines":2}]
}
