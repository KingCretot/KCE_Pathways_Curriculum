AREAS = ('<svg viewBox="0 0 660 250" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="A parallelogram rearranged into a rectangle, and a triangle shown as half of a parallelogram">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Every area formula comes from the rectangle</text>'
  '<rect x="30" y="60" width="160" height="90" fill="#eaf0fb" stroke="#0047BA" stroke-width="2"/><text x="110" y="110" text-anchor="middle" fill="#0047BA" font-weight="bold">A = b × h</text><text x="110" y="172" text-anchor="middle" fill="#0A1F3D">rectangle</text>'
  '<path d="M250 150 L290 60 L430 60 L390 150Z" fill="#fbf3df" stroke="#8a6d1f" stroke-width="2"/><path d="M290 60 L290 150" stroke="#DB2F30" stroke-width="2" stroke-dasharray="5 3"/><path d="M250 150 L290 150 L290 60Z" fill="#DB2F30" fill-opacity="0.2"/>'
  '<text x="340" y="110" text-anchor="middle" fill="#8a6d1f" font-weight="bold">A = b × h</text><text x="340" y="172" text-anchor="middle" fill="#0A1F3D">parallelogram: slide the red</text><text x="340" y="187" text-anchor="middle" fill="#0A1F3D">triangle to the right side</text><text x="296" y="100" fill="#DB2F30" font-size="11">h</text>'
  '<path d="M470 150 L500 60 L600 150Z" fill="#e8f3ec" stroke="#2c6e22" stroke-width="2"/><path d="M500 60 L630 60 L600 150" fill="none" stroke="#2c6e22" stroke-dasharray="5 3"/><path d="M500 60 L500 150" stroke="#DB2F30" stroke-width="2" stroke-dasharray="4 3"/><text x="506" y="100" fill="#DB2F30" font-size="11">h</text>'
  '<text x="565" y="48" text-anchor="middle" fill="#2c6e22" font-weight="bold">A = ½ × b × h</text><text x="560" y="172" text-anchor="middle" fill="#0A1F3D">triangle: half of a</text><text x="560" y="187" text-anchor="middle" fill="#0A1F3D">parallelogram</text>'
  '<text x="330" y="232" text-anchor="middle" fill="#5b6676">The height is always perpendicular (at a right angle) to the base, not the slanted side.</text></svg>')

ROOM = ('<svg viewBox="0 0 660 256" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="An L-shaped room floor plan split into two rectangles: 14 by 10 feet and 8 by 6 feet">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Decompose a composite figure: an L-shaped room</text>'
  '<rect x="160" y="40" width="280" height="140" fill="#eaf0fb" stroke="#0047BA" stroke-width="2"/><rect x="160" y="180" width="160" height="50" fill="#fbf3df" stroke="#8a6d1f" stroke-width="2"/>'
  '<text x="300" y="115" text-anchor="middle" fill="#0047BA" font-weight="bold">A: 14 ft × 7 ft</text><text x="240" y="210" text-anchor="middle" fill="#8a6d1f" font-weight="bold">B: 8 ft × 2.5 ft</text>'
  '<text x="300" y="34" text-anchor="middle" fill="#0A1F3D">14 ft</text><text x="452" y="115" fill="#0A1F3D">7 ft</text><text x="130" y="140" fill="#0A1F3D" text-anchor="end">9.5 ft</text><text x="240" y="244" text-anchor="middle" fill="#0A1F3D" font-size="11">8 ft</text>'
  '<text x="560" y="100" text-anchor="middle" fill="#0A1F3D">A = 14 × 7 = 98 ft²</text><text x="560" y="122" text-anchor="middle" fill="#0A1F3D">B = 8 × 2.5 = 20 ft²</text><text x="560" y="148" text-anchor="middle" fill="#DB2F30" font-weight="bold">Total = 118 ft²</text></svg>')

LESSON = {
 "unit": "Unit 6: Geometry and Data",
 "title": "Area of Triangles, Quadrilaterals and Composite Figures",
 "subtitle": "How much carpet covers a bedroom, how much paint coats a wall, how much sod fills a yard? This week you discover where the area formulas come from, find the area of triangles, parallelograms, trapezoids and composite figures, and price a real room makeover.",
 "objectives": [
  "Explain how the formulas for parallelograms and triangles come from the rectangle.",
  "Find the area of right and non-right triangles using A = ½bh.",
  "Find the area of parallelograms, trapezoids and other quadrilaterals by decomposing them.",
  "Find the area of composite figures by breaking them into rectangles and triangles.",
  "Use area to estimate the cost of flooring, paint or sod."],
 "vocab": [
  ["area", "The amount of surface a flat figure covers, measured in square units."],
  ["base", "A side of a figure chosen as the bottom for measuring."],
  ["height", "The perpendicular distance from the base to the opposite side or vertex."],
  ["perpendicular", "Meeting at a right angle (90°)."],
  ["composite figure", "A figure made of two or more simpler shapes."],
  ["decompose", "To break a figure into simpler parts."]],
 "reconnect": {
  "title": "Week 25: Expressions and equations review",
  "intro": "Area formulas are expressions. Use last unit's skills to warm up.",
  "items": [
   {"t":"num","q":"Evaluate b × h when b = 12 and h = 7.5.","a":90,"pts":2,"why":"12 × 7.5 = 90."},
   {"t":"num","q":"Evaluate ½ × b × h when b = 10 and h = 9.","a":45,"pts":2,"why":"½ × 90 = 45."},
   {"t":"num","q":"A rectangle has area 84 square feet and a length of 12 feet. Solve 12w = 84 for the width.","a":7,"unit":"feet","pts":2,"why":"Divide by 12."},
   {"t":"open","key":"rc_paint","q":"Last unit you planned a budget. If paint costs $32 a gallon and one gallon covers 350 square feet, what would you need to know about a room to plan the paint budget?","min":15,"rows":2,"rubric":["Names what must be measured","Explains how it connects to gallons and cost"],"model":"I'd need the area of the walls, the length times the height of each wall minus doors and windows, so I could figure out how many gallons to buy and multiply by $32."}]},
 "hook": {
  "title": "The Bedroom Makeover",
  "visual": ROOM,
  "html": "<p>Jada's family is redoing her bedroom, an L-shaped room. Vinyl plank flooring costs $3.29 a square foot, and they have $450 for the floor. Will it fit the budget? To answer, they need the room's <b>area</b>, but no single formula covers an L shape.</p><p>The trick is to <b>decompose</b> it: split the room into rectangles, find each area and add. This week you learn to find the area of almost any flat shape by connecting it to the rectangle.</p><div class='callout'><b>Big question:</b> How can one simple idea, length times width, find the area of almost any shape?</div>"},
 "learn": [
  {"title": "From Rectangles to Parallelograms",
   "visual": AREAS,
   "html": "<p>A rectangle's area is <b>base × height</b>. Cut a triangle off one side of a parallelogram and slide it to the other side: you get a rectangle with the same base and height. So a parallelogram's area is also <b>A = b × h</b>.</p><p>The key is the <b>height</b>: it must be <b>perpendicular</b> to the base. The slanted side of a parallelogram is not its height.</p>",
   "checks": [
    {"t":"num","q":"A parallelogram has a base of 15 cm, a height of 8 cm and a slanted side of 10 cm. What is its area?","a":120,"unit":"square cm","pts":2,"why":"15 × 8 = 120. The slanted side is not used."},
    {"t":"open","key":"slantmistake","q":"Ravi found the area of that parallelogram as 15 × 10 = 150 cm². Explain his mistake.","min":20,"rows":2,"rubric":["Identifies that he used the slanted side","Explains that the height must be perpendicular to the base"],"model":"Ravi used the slanted side, 10 cm, instead of the height. The height has to be perpendicular to the base, which is 8 cm, so the area is 15 × 8 = 120 cm²."}]},
  {"title": "Triangles: Half a Parallelogram",
   "html": "<p>Draw a diagonal in a rectangle and you get two identical right triangles, so each is ½ × b × h. In the same way, two identical triangles of any shape fit together to make a parallelogram. So a triangle is half of a parallelogram with the same base and height: <b>A = ½ × b × h</b>.</p><p>For a <b>right triangle</b>, the two sides that meet at the right angle are the base and height. For other triangles, the height may be inside the triangle or even outside it, drawn as a dashed line to an extension of the base.</p>",
   "checks": [
    {"t":"num","q":"A triangular sail has a base of 6 feet and a height of 11 feet. What is its area?","a":33,"unit":"square feet","pts":2,"why":"½ × 6 × 11 = 33."},
    {"t":"num","q":"A right triangle has legs of 9 m and 14 m. What is its area?","a":63,"unit":"square meters","pts":2,"why":"½ × 9 × 14 = 63."},
    {"t":"open","key":"whyhalf","q":"Explain, using a drawing in words, why the triangle formula has ½ in it.","min":20,"rows":2,"rubric":["Describes two identical triangles forming a parallelogram or rectangle","Concludes that one triangle is half the area"],"model":"If you copy a triangle, flip it and fit it next to the original, the two make a parallelogram with the same base and height. Each triangle is half of that parallelogram, so its area is half of b × h."}]},
  {"title": "Trapezoids and Composite Figures",
   "html": "<p>A <b>trapezoid</b> has one pair of parallel sides. You can find its area by <b>decomposing</b> it into a rectangle and triangles, or by using A = ½ × (b₁ + b₂) × h, which comes from fitting two copies into a parallelogram.</p><p>For any <b>composite figure</b>, like Jada's L-shaped room:</p><ol><li>Split it into rectangles and triangles (draw the lines).</li><li>Find any missing side lengths by adding or subtracting.</li><li>Find each area and add them (or subtract a cut-out piece).</li></ol>",
   "checks": [
    {"t":"num","q":"A trapezoid has parallel bases of 10 inches and 16 inches and a height of 5 inches. What is its area?","a":65,"unit":"square inches","pts":2,"why":"½ × (10 + 16) × 5 = 65."},
    {"t":"num","q":"A yard is a 30-foot by 20-foot rectangle with a 6-foot by 4-foot shed on it. How many square feet of grass are there?","a":576,"unit":"square feet","pts":2,"why":"600 − 24 = 576 (subtract the cut-out)."},
    {"t":"open","key":"twoways","q":"Describe two different ways to split Jada's L-shaped room into rectangles. Do both ways give the same total? Explain why.","min":30,"rows":3,"rubric":["Two different valid decompositions","Explains that the total area stays the same however you split it"],"model":"I could cut it with a horizontal line into a 14 × 7 rectangle and an 8 × 2.5 rectangle, or with a vertical line into an 8 × 9.5 rectangle and a 6 × 7 rectangle. Both give 118 square feet, because the floor's area doesn't change; only the way I break it up changes."}]},
  {"title": "Money: Pricing a Room Makeover",
   "html": "<p>Flooring, paint, wallpaper and sod are all priced by area. Find the area, then multiply by the price per square unit. Real projects also need extra: flooring installers usually buy about 10 percent more to allow for cuts and mistakes.</p><p>Jada's room: 118 ft² × $3.29 = $388.22. With 10 percent extra: 118 × 1.10 = 129.8, so about 130 ft², or $427.70. Within the $450 budget.</p>",
   "checks": [
    {"t":"num","q":"Carpet costs $2.75 per square foot. How much would it cost to carpet a 12-foot by 15-foot room (no extra)?","a":495,"unit":"dollars","pts":2,"why":"180 × 2.75 = 495."},
    {"t":"num","q":"A wall is 14 feet long and 8 feet high, with a 3-foot by 4-foot window. How many square feet will be painted?","a":100,"unit":"square feet","pts":2,"why":"112 − 12 = 100."},
    {"t":"open","key":"sodquote","q":"Sod costs $0.55 per square foot. A homeschool garden plot is a right triangle with legs of 18 feet and 12 feet. Find the cost, then explain whether you'd buy a little extra and why.","min":30,"rows":3,"rubric":["Correct area and cost","A reasoned decision about extra material"],"model":"Area = ½ × 18 × 12 = 108 ft², so 108 × $0.55 = $59.40. I'd buy about 10 percent extra, around 119 ft² for about $65, because sod pieces have to be cut to fit the triangle's corners."}]}],
 "handson": {
  "title": "Measure and Price a Real Room",
  "intro": "Measure a room in your home, draw it to scale, and price new flooring and paint.",
  "materials": ["A tape measure", "Graph paper and a ruler", "Colored pencils", "Scissors and a sheet of paper", "A calculator for checking (optional)", "A home improvement store website or flyer for prices"],
  "steps": [
   "Cut-and-move proof: draw a parallelogram on paper, cut along its height to remove a triangle, and slide the triangle to the other side to make a rectangle. Then cut a rectangle in half diagonally to see two equal triangles.",
   "Measure the length and width of a room in your home (or a porch or patio) to the nearest half foot. If it isn't a rectangle, measure every wall.",
   "Draw the floor plan on graph paper with each square standing for 1 square foot. Split it into rectangles and triangles and label every measurement.",
   "Find the total floor area. Then find the area of one wall, subtracting any windows or doors.",
   "Look up real prices for one flooring choice and one gallon of paint (and how many square feet a gallon covers). Price the floor with 10 percent extra and the paint for that wall.",
   "Keep scissors away from young children, and don't climb on furniture to measure; ask an adult to measure high walls."],
  "record": [
   {"t":"open","key":"roomrec","q":"Show your floor plan measurements, how you decomposed the shape, the total area, and your flooring cost with 10 percent extra.","min":39,"rows":5,"rubric":["Measurements and decomposition shown","Correct total area","Correct cost including 10 percent extra"],"model":"Our living room is an L shape: a 16 × 12 ft rectangle plus a 5 × 4 ft nook. Area: 192 + 20 = 212 ft². With 10 percent extra, 233.2 ft², about 234 ft². Luxury vinyl at $2.99 per ft²: 234 × 2.99 = $699.66."},
   {"t":"open","key":"paintrec","q":"Show your wall area (with windows or doors subtracted), how many gallons you'd need and the cost. What would you tell your family about the makeover budget?","min":35,"rows":4,"rubric":["Correct wall area with subtraction","Gallons and cost","A practical recommendation"],"model":"One wall is 16 × 8 = 128 ft², minus a 3 × 7 door = 21 ft², so 107 ft². One gallon covers 350 ft², so one gallon is enough even for two coats (214 ft²), at $34. I'd tell my family the paint is cheap, but the floor is the big expense, so we might start with paint."}]},
 "think": {
  "intro": "Explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"samearea","q":"Draw (in words) a rectangle, a parallelogram and a triangle that all have an area of 24 square units. Give their dimensions and explain how you made sure they matched.","min":34,"rows":4,"rubric":["Three correct figures with dimensions","Explains the reasoning, including the ½ for the triangle"],"model":"Rectangle: 6 by 4. Parallelogram: base 8, height 3. Triangle: base 8, height 6. For the rectangle and parallelogram I chose factors of 24. For the triangle I needed b × h = 48, because half of 48 is 24."},
   {"t":"open","key":"doubleh","q":"If you double the base of a triangle and also double its height, what happens to its area? Test with an example and explain why.","min":40,"rows":4,"rubric":["Correct conclusion about the new area", "A tested example", "An explanation"],"model":"The area becomes four times as large. A triangle with base 4 and height 6 has area 12; with base 8 and height 12 its area is 48, which is 4 × 12. Doubling both multiplies b × h by 2 × 2 = 4, and the ½ stays the same."}]},
 "exit": [
  {"t":"num","q":"Find the area of a triangle with base 16 cm and height 9 cm.","a":72,"unit":"square cm","pts":2,"why":"½ × 16 × 9 = 72."},
  {"t":"num","q":"Find the area of a parallelogram with base 11 m and height 6 m.","a":66,"unit":"square meters","pts":2,"why":"11 × 6 = 66."},
  {"t":"num","q":"Tile costs $4.50 per square foot. How much does it cost to tile a 6-foot by 8-foot bathroom floor?","a":216,"unit":"dollars","pts":2,"why":"48 × 4.50 = 216."},
  {"t":"open","key":"exit_height","q":"What must be true about the height you use in an area formula?","min":8,"rows":2,"rubric":["States the relationship between the height and the base"],"model":"It must be perpendicular to the base, meeting it at a right angle."}],
 "next": "Week 27: nets, surface area and volume."
}

TEACHER = {
 "standards": [
  "MA.6.GR.2.1: Derive a formula for the area of a right triangle using a rectangle. Apply a formula to find the area of a triangle.",
  "MA.6.GR.2.2: Solve mathematical and real-world problems involving the area of quadrilaterals and composite figures by decomposing them into triangles or rectangles.",
  "MA.6.AR.1.3: Evaluate algebraic expressions using substitution and order of operations.",
  "Financial literacy: estimating project costs (Jump$tart Spending and Saving)."],
 "materials": ["The interactive lesson", "A tape measure, graph paper, ruler, colored pencils, scissors and paper", "A store website or flyer for prices; optional calculator", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 25 warm-up questions."],
  [4, "Hook", "Jada's L-shaped room and the $450 budget."],
  [10, "Parallelograms", "Cut and slide; the height is perpendicular."],
  [11, "Triangles", "Half a parallelogram; right and non-right triangles."],
  [12, "Trapezoids and composites", "Decompose, add or subtract; two ways to split."],
  [11, "Room makeover", "Price by area; 10 percent extra."],
  [6, "Assign", "Set up the room measurement; assign Think Deeper and the Exit Check."]],
 "key_questions": ["Which length is the height?", "How could you split this shape?", "Do you add or subtract here?", "Why do installers buy extra?"],
 "misconceptions": ["Using the slanted side as the height.", "Forgetting the ½ for triangles.", "Writing area in plain units instead of square units.", "Double-counting an overlapping piece in a composite figure."],
 "support": ["Let students trace and cut shapes to see the formulas.", "Provide grid paper for counting squares.", "Color each piece of a composite figure."],
 "challenge": ["Find the area of a regular hexagon by splitting it into triangles.", "Price a full room with flooring, two coats of paint on four walls and a budget limit."],
 "background": "<p>Florida's MA.6.GR.2.1 and 2.2 cover triangles, quadrilaterals and composite figures; the trapezoid formula is shown as a shortcut but every problem can be solved by decomposing. Prices are practice figures except in the hands-on, which uses real local prices.</p>",
 "sources": ["Florida Department of Education, B.E.S.T. Standards for Mathematics (2020).", "Jump$tart Coalition, National Standards for Personal Financial Education (2021)."]
}

PRINT = {
 "directions": "Show your work and include square units.",
 "items": [
  {"q":"Find the area: (a) triangle, base 12 ft, height 7 ft (b) parallelogram, base 9 cm, height 4.5 cm","a":"(a) 42 ft² (b) 40.5 cm²","lines":2},
  {"q":"Find the area of a trapezoid with bases 8 m and 12 m and height 6 m.","a":"½ × 20 × 6 = 60 m².","lines":2},
  {"q":"An L-shaped patio is a 20 × 10 ft rectangle plus a 6 × 5 ft rectangle. Find its area.","a":"200 + 30 = 230 ft².","lines":2},
  {"q":"A 25 × 18 ft lawn has a 6 × 6 ft pool deck. Find the grass area.","a":"450 − 36 = 414 ft².","lines":2},
  {"q":"Flooring costs $3.10 per ft². Find the cost for a 10 × 12 ft room with 10 percent extra.","a":"120 × 1.1 = 132 ft²; 132 × 3.10 = $409.20.","lines":2},
  {"q":"Explain why the area of a triangle is half of base times height.","a":"Two identical triangles make a parallelogram with the same base and height.","lines":2}]
}
