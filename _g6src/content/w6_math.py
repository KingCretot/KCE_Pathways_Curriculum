def area(rows=3, cols=4, shade_r=2, shade_c=3, title="2/3 × 3/4"):
    W, H, x0, y0, cw, ch = 560, 250, 160, 40, 60, 50
    s = (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Area model for {title}">'
         f'<text x="280" y="22" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Area model: {title}</text>')
    for r in range(rows):
        for c in range(cols):
            fill = "#0047BA" if (r < shade_r and c < shade_c) else ("#9ec3f0" if c < shade_c else ("#f3d9a0" if r < shade_r else "#fff"))
            s += f'<rect x="{x0+c*cw}" y="{y0+r*ch}" width="{cw}" height="{ch}" fill="{fill}" stroke="#0A1F3D"/>'
    s += f'<text x="{x0+shade_c*cw/2}" y="{y0+rows*ch+20}" text-anchor="middle">{shade_c} of {cols} columns = {shade_c}/{cols}</text>'
    s += f'<text x="{x0-10}" y="{y0+shade_r*ch/2+4}" text-anchor="end">{shade_r} of {rows} rows</text><text x="{x0-10}" y="{y0+shade_r*ch/2+20}" text-anchor="end">= {shade_r}/{rows}</text>'
    s += f'<text x="{x0+cols*cw+16}" y="{y0+40}" font-weight="bold" fill="#0047BA">Dark overlap:</text><text x="{x0+cols*cw+16}" y="{y0+58}">{shade_r*shade_c} of {rows*cols} parts</text>'
    s += f'<text x="{x0+cols*cw+16}" y="{y0+76}">= {shade_r*shade_c}/{rows*cols} = 1/2</text></svg>'
    return s

PAN = ('<svg viewBox="0 0 560 190" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Pan of cornbread cut into fractions">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">3/4 of the pan is left. Kwame takes 1/3 of what is left.</text>'
  '<rect x="60" y="36" width="440" height="120" fill="#fff" stroke="#0A1F3D" stroke-width="2"/>'
  + ''.join(f'<rect x="{60+i*110}" y="36" width="110" height="120" fill="{"#eee" if i == 3 else "#f2c14e"}" stroke="#8a6d1f"/>' for i in range(4)) +
  ''.join(f'<line x1="60" y1="{36+j*40}" x2="390" y2="{36+j*40}" stroke="#8a6d1f" stroke-dasharray="4 3"/>' for j in (1, 2)) +
  '<rect x="60" y="36" width="330" height="40" fill="#DB2F30" opacity=".55"/>'
  '<text x="445" y="100" text-anchor="middle" fill="#5b6676">eaten</text><text x="225" y="62" text-anchor="middle" fill="#fff" font-weight="bold">Kwame\'s share</text>'
  '<text x="280" y="178" text-anchor="middle">1/3 of 3/4 = 3/12 = 1/4 of the whole pan</text></svg>')

LESSON = {
 "unit": "Unit 2: Fractions and Ratios",
 "title": "Multiplying Fractions",
 "subtitle": "\"Of\" means multiply. Fractions help families scale recipes and split costs fairly.",
 "objectives": [
  "Find a fraction of a whole number and of a fraction, using models and the algorithm.",
  "Simplify before multiplying using common factors (the GCF from Unit 1).",
  "Multiply mixed numbers by changing them to improper fractions.",
  "Predict whether a product will be greater or less than a factor.",
  "Split a shared cost fairly using fractions."],
 "vocab": [
  ["numerator", "The top number of a fraction: how many parts are counted."],
  ["denominator", "The bottom number: how many equal parts make the whole."],
  ["improper fraction", "A fraction whose numerator is greater than or equal to its denominator, such as 7/4."],
  ["mixed number", "A whole number and a fraction together, such as 1 3/4."],
  ["simplest form", "A fraction whose numerator and denominator have no common factor except 1."],
  ["reciprocal", "Two numbers whose product is 1, such as 3/4 and 4/3 (used next week)."],
  ["fair share", "A portion that matches each person's agreed part of the use or the cost."]],
 "reconnect": {
  "title": "Unit 1: factors, multiples and decimals",
  "intro": "The GCF you learned in Week 5 is the secret tool for simplifying fractions.",
  "items": [
   {"t":"num","q":"What is the GCF of 18 and 30?","a":6,"pts":2,"why":"18 = 2 × 3 × 3, 30 = 2 × 3 × 5. Shared: 2 × 3 = 6."},
   {"t":"num","q":"Use the GCF to write 18/30 in simplest form. Type it as a fraction, like 2/7.","a":0.6,"show":"3/5","pts":3,"why":"Divide both by 6: 18/30 = 3/5."},
   {"t":"num","q":"What is the LCM of 4 and 6?","a":12,"pts":2,"why":"Multiples of 6: 6, 12. 12 is also a multiple of 4."},
   {"t":"num","q":"Write 0.75 as a fraction in simplest form.","a":0.75,"show":"3/4","pts":2,"why":"0.75 = 75/100 = 3/4 (divide both by 25)."},
   {"t":"open","key":"rc_gcflcm","q":"Explain the difference between a problem that needs the GCF and one that needs the LCM. Give a one-sentence example of each.","min":20,"rows":3,"rubric":["GCF: splitting into the largest equal groups, with an example","LCM: when things line up again or the smallest shared amount, with an example"],"model":"The GCF splits things into the largest equal groups, like packing 36 muffins and 48 cookies into identical bags. The LCM finds when things line up, like two buses that leave every 15 and 20 minutes leaving together again."}]},
 "hook": {
  "title": "The Family Reunion Cookout",
  "visual": PAN,
  "html": "<p>Amara and Kwame's family is hosting a reunion at a park in Lakeland. Their grandmother's cornbread recipe makes one pan, but they need two and a half pans. Three households are splitting the $96.00 cost of the pavilion and food, but they are not all the same size. And after lunch, only 3/4 of a pan of cornbread is left, and Kwame wants 1/3 of what is left.</p><p>Every one of these questions is a fraction multiplication problem.</p><div class='callout'><b>Big idea:</b> To find a fraction <b>of</b> something, multiply. Multiply the numerators, multiply the denominators, and simplify.</div>"},
 "learn": [
  {"title": "A Fraction of a Whole Number",
   "html": "<p>To find 3/4 of 24, divide 24 into 4 equal groups (6 each), then take 3 groups: 18. That is the same as 3/4 × 24 = 72/4 = 18.</p><div class='example'>2/3 of the $96 cookout budget goes to food. 2/3 × 96 = 192/3 = <b>$64</b>.</div>",
   "checks": [
    {"t":"num","q":"3/8 of the 40 relatives at the reunion are children. How many children are there?","a":15,"unit":"children","pts":2,"why":"40 ÷ 8 = 5, and 3 × 5 = 15."},
    {"t":"num","q":"Grandma's punch recipe uses 5/6 of a gallon of juice per batch. How many gallons are needed for 9 batches? Type a mixed number like 7 1/2.","a":7.5,"show":"7 1/2 gallons","pts":3,"why":"5/6 × 9 = 45/6 = 15/2 = 7 1/2 gallons."},
    {"t":"open","key":"predict","q":"Without calculating, is 7/8 × 56 more or less than 56? Explain using what multiplying by a fraction less than 1 means.","min":12,"rows":2,"rubric":["Less","Explains that 7/8 is less than 1, so the product is only part of 56"],"model":"Less, because 7/8 is less than 1, so I am taking only part of 56 (it is 49)."}]},
  {"title": "A Fraction of a Fraction",
   "visual": area(),
   "html": "<p>In the area model, shade 3/4 of a rectangle with columns, then shade 2/3 of that with rows. The overlap is 6 of the 12 equal parts. So 2/3 × 3/4 = 6/12 = 1/2.</p><p><b>The rule:</b> multiply the numerators, multiply the denominators, then simplify.</p><p><b>Shortcut:</b> simplify first. In 4/9 × 3/8, the 4 and the 8 share a factor of 4, and the 3 and the 9 share a factor of 3: (1 × 1)/(3 × 2) = 1/6. Smaller numbers mean fewer mistakes.</p>",
   "checks": [
    {"t":"num","q":"Kwame takes 1/3 of the 3/4 pan of cornbread that is left. What fraction of the whole pan does he take?","a":0.25,"show":"1/4","pts":2,"why":"1/3 × 3/4 = 3/12 = 1/4."},
    {"t":"num","q":"5/6 × 9/10 = ? Type the answer in simplest form.","a":0.75,"show":"3/4","pts":3,"why":"Simplify first: 5 and 10 share 5; 9 and 6 share 3. (1 × 3)/(2 × 2) = 3/4."},
    {"t":"num","q":"4/9 × 3/8 = ? Type the answer in simplest form.","a":0.16666666666666666,"tol":0.0005,"show":"1/6","pts":3,"why":"Simplify first: (1 × 1)/(3 × 2) = 1/6."},
    {"t":"open","key":"overlap","q":"Draw (or describe) an area model for 3/5 × 1/2. How many parts are in the whole, how many are in the overlap, and what is the product?","min":15,"rows":3,"rubric":["Whole has 10 parts","Overlap has 3 parts","Product 3/10"],"model":"I split a rectangle into 5 columns and shaded 3, then split it into 2 rows and shaded 1. The whole has 10 parts and the overlap has 3, so 3/5 × 1/2 = 3/10."}]},
  {"title": "Multiplying Mixed Numbers",
   "html": "<p>Change each mixed number to an improper fraction, multiply, simplify, and change back.</p><div class='example'>Grandma's recipe uses 1 3/4 cups of cornmeal per pan. For 2 1/2 pans: 1 3/4 × 2 1/2 = 7/4 × 5/2 = 35/8 = <b>4 3/8 cups</b>.<br>Estimate first: about 2 × 2 1/2 = 5 cups, so 4 3/8 is reasonable.</div><div class='callout'>Do not multiply the whole numbers and the fractions separately: 1 × 2 + 3/4 × 1/2 = 2 3/8 is wrong.</div>",
   "checks": [
    {"t":"num","q":"The recipe uses 2/3 cup of buttermilk per pan. How much for 2 1/2 pans? Type a mixed number.","a":1.6666666666666667,"tol":0.0005,"show":"1 2/3 cups","pts":3,"why":"2/3 × 5/2 = 10/6 = 5/3 = 1 2/3 cups."},
    {"t":"num","q":"2 1/4 × 1 1/3 = ?","a":3,"pts":3,"why":"9/4 × 4/3 = 36/12 = 3."},
    {"t":"num","q":"A rectangular picnic blanket is 2 1/2 yards long and 1 3/5 yards wide. What is its area in square yards?","a":4,"unit":"square yards","pts":3,"why":"5/2 × 8/5 = 40/10 = 4 square yards."},
    {"t":"open","key":"jada","q":"Jada says 2 1/2 × 2 1/2 = 4 1/4 because 2 × 2 = 4 and 1/2 × 1/2 = 1/4. Find her mistake, give the correct product, and explain how an estimate could have warned her.","min":30,"rows":3,"rubric":["Correct product 6 1/4","Explains she skipped the cross parts (2 × 1/2 twice) or should use improper fractions","Estimate: 2 1/2 × 2 1/2 is more than 2 × 3 = 6"],"model":"She multiplied only the whole parts and only the fraction parts, so she left out 2 × 1/2 and 1/2 × 2. Using improper fractions: 5/2 × 5/2 = 25/4 = 6 1/4. An estimate warns her: 2 1/2 × 2 1/2 is more than 2 × 3 = 6, so 4 1/4 is far too small."}]},
  {"title": "Splitting Costs Fairly",
   "html": "<p>The three households agree to split the $96.00 cookout cost by how many people each brings. Amara's household brings 1/2 of the guests, Uncle Desmond's brings 1/3, and Aunt Lena's brings the rest.</p><table class='t'><tr><th>Household</th><th>Fraction of guests</th><th>Share of $96</th></tr><tr><td>Amara's</td><td>1/2</td><td>1/2 × 96 = $48</td></tr><tr><td>Uncle Desmond's</td><td>1/3</td><td>?</td></tr><tr><td>Aunt Lena's</td><td>?</td><td>?</td></tr></table><p>Splitting by use is one kind of fair. Splitting equally is another. Families also think about who can afford what, and who did the cooking.</p>",
   "checks": [
    {"t":"num","q":"How much does Uncle Desmond's household pay?","a":32,"unit":"dollars","show":"$32","pts":2,"why":"1/3 × 96 = $32."},
    {"t":"num","q":"What fraction of the guests does Aunt Lena's household bring?","a":0.16666666666666666,"tol":0.0005,"show":"1/6","pts":3,"why":"1 − 1/2 − 1/3 = 6/6 − 3/6 − 2/6 = 1/6."},
    {"t":"num","q":"How much does Aunt Lena's household pay?","a":16,"unit":"dollars","show":"$16","pts":2,"why":"1/6 × 96 = $16. Check: 48 + 32 + 16 = 96."},
    {"t":"open","key":"fair","q":"Aunt Lena cooked all the food and spent 6 hours doing it. Is splitting only by number of guests still fair? Suggest a fairer plan and explain it with numbers.","min":35,"rows":4,"rubric":["Takes a reasoned position","Proposes a specific plan with numbers that still total $96","Explains why it is fairer"],"model":"Not completely, because her work is worth something too. One plan: count her cooking as worth $16, so she pays $0, and the other two households split her $16 by their guest fractions. Amara's household pays 3/5 of it ($9.60) and Uncle Desmond's pays 2/5 ($6.40), for totals of $57.60 and $38.40, which still add to $96."}]}],
 "handson": {
  "title": "Scale a Family Recipe",
  "intro": "Real recipes are full of fractions. Scale one for your own family, then cook or measure it.",
  "materials": ["A family recipe or a simple recipe card with at least four fractional amounts", "Measuring cups and spoons (1 cup, 1/2, 1/3, 1/4)", "Paper and pencil", "Dry rice, beans or water for practice measuring (if not cooking)"],
  "steps": [
   "Choose a recipe and write each ingredient amount.",
   "Decide how much to make: 1 1/2 times, 2 1/2 times, or 2/3 of the recipe.",
   "Multiply every amount by your scale factor. Show your work and simplify.",
   "Measure each scaled amount with real measuring cups (rice or water is fine), using combinations like 1 cup + 1/3 cup.",
   "If an adult agrees, cook the scaled recipe together."],
  "record": [
   {"t":"open","key":"recipe","q":"Type the original amounts, your scale factor, and each scaled amount with the work shown.","min":40,"rows":7,"rubric":["At least four ingredients","Correct multiplication with improper fractions","Simplified answers","Units included"],"model":"Scale factor: 2 1/2. Flour 1 3/4 cups × 5/2 = 35/8 = 4 3/8 cups. Sugar 1/3 cup × 5/2 = 5/6 cup. Milk 3/4 cup × 5/2 = 15/8 = 1 7/8 cups. Salt 1/2 teaspoon × 5/2 = 5/4 = 1 1/4 teaspoons."},
   {"t":"open","key":"recipe2","q":"Which scaled amount was hardest to measure with real cups, and how did you do it?","min":20,"rows":3,"rubric":["Names a hard amount","Explains a real measuring strategy"],"model":"5/6 cup was hardest because I have no 1/6 cup. I used 1/2 cup plus 1/3 cup, because 3/6 + 2/6 = 5/6."}]},
 "think": {
  "intro": "Explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"why","q":"Explain why multiplying the numerators and the denominators works, using an area model or an example from the lesson. Then explain why 3/4 × 2/3 gives the same answer as 2/3 × 3/4.","min":45,"rubric":["Explains the denominators make the size of each small part","Explains the numerators count the overlapping parts","Explains the commutative property with the model rotated"],"model":"In the area model, multiplying the denominators (3 × 4 = 12) tells how many equal small parts the whole is cut into. Multiplying the numerators (2 × 3 = 6) counts the parts in the overlap, so the product is 6/12. If I switch the order, I am just turning the rectangle sideways, so the overlap is still 6 of 12 parts. That is the commutative property."},
   {"t":"open","key":"budget","q":"The reunion committee has $240. They spend 3/8 on food and 1/4 on renting the pavilion, and save 1/5 of what is left for next year. How much is saved? Show every step.","min":30,"rubric":["Food $90 and pavilion $60","Left $90","Saved 1/5 of 90 = $18","Clear steps"],"model":"Food: 3/8 × 240 = $90. Pavilion: 1/4 × 240 = $60. Spent: $150, so $90 is left. Saved: 1/5 × 90 = $18."}]},
 "exit": [
  {"t":"num","q":"5/8 of $72 = ?","a":45,"unit":"dollars","show":"$45","pts":2,"why":"72 ÷ 8 = 9, and 5 × 9 = 45."},
  {"t":"num","q":"7/12 × 3/14 = ? Type in simplest form.","a":0.125,"show":"1/8","pts":3,"why":"Simplify first: 7 and 14 share 7; 3 and 12 share 3. (1 × 1)/(4 × 2) = 1/8."},
  {"t":"num","q":"3 1/3 × 1 1/5 = ?","a":4,"pts":3,"why":"10/3 × 6/5 = 60/15 = 4."},
  {"t":"num","q":"A trail is 4 1/2 miles long. Dev has hiked 2/3 of it. How many miles has he hiked?","a":3,"unit":"miles","pts":3,"why":"2/3 × 9/2 = 18/6 = 3 miles."},
  {"t":"num","q":"Three roommates split a $1,350 rent. One has the big room and pays 2/5. The other two split the rest equally. How much does each of the other two pay?","a":405,"unit":"dollars","show":"$405","pts":3,"why":"2/5 × 1,350 = $540. 1,350 − 540 = $810, and 810 ÷ 2 = $405 each."}],
 "next": "Week 7: dividing fractions and mixed numbers, and how recipes and servings turn into grocery costs."
}

TEACHER = {
 "standards": [
  "MA.6.NSO.2.2: Extend previous understanding of multiplication and division to compute products and quotients of positive fractions by positive fractions, including mixed numbers, with procedural fluency.",
  "MA.6.NSO.2.3: Solve multi-step real-world problems involving any of the four operations with positive multi-digit decimals or positive fractions, including mixed numbers.",
  "MA.K12.MTR.2.1: Demonstrate understanding by representing problems in multiple ways (area models).",
  "MA.K12.MTR.7.1: Apply mathematics to real-world contexts.",
  "Financial literacy: sharing costs fairly and budgeting for a group (Jump$tart Spending and Saving)."],
 "materials": ["The interactive lesson", "Graph paper or a printed rectangle for area models", "Measuring cups (1, 1/2, 1/3, 1/4) and dry rice", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Unit 1 Reconnect questions. Stress that the GCF simplifies fractions."],
  [4, "Hook", "Present the reunion problems and ask which operation each needs."],
  [10, "Fraction of a whole", "Model 3/4 of 24 with groups, then the algorithm."],
  [12, "Fraction of a fraction", "Draw the area model for 2/3 × 3/4 together. Teach simplifying first."],
  [12, "Mixed numbers", "Work the cornmeal problem with an estimate first. Analyze Jada's error."],
  [10, "Splitting costs", "Complete the cost table. Discuss different kinds of fair."],
  [6, "Assign", "Assign the recipe activity, Think Deeper and the Exit Check."]],
 "key_questions": ["What is the whole?", "Will the answer be more or less than the starting amount? Why?", "Can you simplify before you multiply?", "What does fair mean in this situation?"],
 "misconceptions": ["Multiplying whole parts and fraction parts of mixed numbers separately.", "Thinking multiplication always makes numbers bigger.", "Forgetting to simplify, or simplifying across addition.", "Adding denominators when multiplying."],
 "support": ["Use fraction strips or paper folding for fraction-of-a-fraction.", "Provide a step card: change, simplify, multiply, change back.", "Begin with unit fractions (1/3 of 1/2) before others."],
 "challenge": ["Find two different fractions whose product is 3/8.", "Plan a reunion budget of $500 using at least four fractional categories that total the whole."],
 "background": "<p>Engine note: fraction answers may be typed as fractions (3/4), mixed numbers (7 1/2) or exact decimals (0.75). All names and amounts are illustrative. This week begins the Unit 2 money thread on splitting costs fairly; Week 7 connects fractions to recipes, servings and grocery costs.</p>",
 "sources": ["CPALMS: MA.6.NSO.2.2 and MA.6.NSO.2.3.", "Jump$tart Coalition National Standards for Personal Financial Education."]
}

PRINT = {
 "directions": "Show your work. Simplify every answer.",
 "items": [
  {"q":"4/5 of 35 = ____     2/7 of 63 = ____","a":"28; 18","lines":2},
  {"q":"3/8 × 4/9 = ____     6/7 × 14/15 = ____","a":"1/6; 4/5","lines":2},
  {"q":"1 1/2 × 2 2/3 = ____     3 3/4 × 1 3/5 = ____","a":"4; 6","lines":2},
  {"q":"Draw an area model for 2/5 × 3/4 and write the product.","a":"5 rows by 4 columns = 20 parts; overlap 6; 6/20 = 3/10","lines":4},
  {"q":"Four friends rent a beach cabin for $360. Two of them stay the whole time and agree to pay 1/3 each. The other two split the rest. How much does each pay?","a":"1/3 × 360 = $120 each for the first two; $120 left, so $60 each for the other two.","lines":3},
  {"q":"Without calculating, circle the products less than 12: 3/4 × 12, 5/4 × 12, 1 1/2 × 12, 2/3 × 12. Explain your rule.","a":"3/4 × 12 and 2/3 × 12; multiplying by a fraction less than 1 gives less than 12.","lines":2}]
}
