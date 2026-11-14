NET = ('<svg viewBox="0 0 660 260" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="A shipping box 12 by 8 by 6 inches and its unfolded net of six rectangles, three matching pairs">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Unfold a box into a net: six faces, three matching pairs</text>'
  '<path d="M40 110 L160 110 L160 190 L40 190Z" fill="#eaf0fb" stroke="#0047BA" stroke-width="2"/><path d="M40 110 L80 80 L200 80 L160 110Z" fill="#fbf3df" stroke="#8a6d1f" stroke-width="2"/><path d="M160 110 L200 80 L200 160 L160 190Z" fill="#e8f3ec" stroke="#2c6e22" stroke-width="2"/>'
  '<text x="100" y="208" text-anchor="middle" fill="#0A1F3D">12 in</text><text x="186" y="186" fill="#0A1F3D">8 in</text><text x="206" y="125" fill="#0A1F3D">6 in</text>'
  '<text x="120" y="236" text-anchor="middle" fill="#5b6676" font-size="11">12 in long, 8 in wide, 6 in tall</text>'
  + ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}" stroke="#0A1F3D" stroke-width="1.5"/><text x="{x+w/2}" y="{y+h/2+4}" text-anchor="middle" fill="#0A1F3D" font-size="11">{t}</text>'
            for x, y, w, h, c, t in [(330, 40, 84, 56, "#fbf3df", "top 12×8"), (274, 96, 56, 42, "#e8f3ec", "8×6"), (330, 96, 84, 42, "#eaf0fb", "front 12×6"), (414, 96, 56, 42, "#e8f3ec", "8×6"),
                                     (330, 138, 84, 56, "#fbf3df", "bottom 12×8"), (330, 194, 84, 42, "#eaf0fb", "back 12×6")]) +
  '<text x="590" y="110" text-anchor="middle" fill="#0A1F3D">2(12×8) = 192</text><text x="590" y="130" text-anchor="middle" fill="#0A1F3D">2(12×6) = 144</text><text x="590" y="150" text-anchor="middle" fill="#0A1F3D">2(8×6) = 96</text><text x="590" y="176" text-anchor="middle" fill="#DB2F30" font-weight="bold">SA = 432 in²</text></svg>')

CUBES = ('<svg viewBox="0 0 660 200" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="A rectangular prism filled with unit cubes in layers: 4 by 3 base, 2 layers, 24 cubes">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Volume counts the cubes that fill a prism: V = l × w × h</text>'
  + ''.join(f'<path d="M{x} {y} l24 0 l12 -10 l-24 0Z" fill="#C9A84C" stroke="#8a6d1f"/><path d="M{x} {y} l24 0 l0 24 l-24 0Z" fill="#fbf3df" stroke="#8a6d1f"/><path d="M{x+24} {y} l12 -10 l0 24 l-12 10Z" fill="#e6dcc0" stroke="#8a6d1f"/>'
            for layer in (0, 1) for row in (2, 1, 0) for col in range(4) for x, y in [(120 + col*24 + row*12, 140 - layer*24 - row*10)]) +
  '<text x="380" y="90" fill="#0A1F3D">base: 4 × 3 = 12 cubes per layer</text><text x="380" y="112" fill="#0A1F3D">2 layers</text><text x="380" y="134" fill="#DB2F30" font-weight="bold">V = 4 × 3 × 2 = 24 cubic units</text>'
  '<text x="330" y="190" text-anchor="middle" fill="#5b6676" font-size="11">Surface area is wrapping paper (square units). Volume is what fits inside (cubic units).</text></svg>')

LESSON = {
 "unit": "Unit 6: Geometry and Data",
 "title": "Nets, Surface Area and Volume",
 "subtitle": "Every package you've ever opened was once a flat sheet of cardboard. This week you unfold boxes into nets, find surface area to know how much material wraps a prism and volume to know how much fits inside, and use both to choose the cheapest way to ship a homemade product.",
 "objectives": [
  "Represent a right rectangular prism with a net and identify matching faces.",
  "Find the surface area of a rectangular prism using a net.",
  "Find the volume of a rectangular prism with whole-number and fraction or decimal edges, using V = l × w × h.",
  "Explain the difference between surface area and volume and choose the right one for a problem.",
  "Compare packaging and shipping costs using surface area, volume and price."],
 "vocab": [
  ["rectangular prism", "A solid with six rectangular faces, like a box."],
  ["face", "A flat surface of a solid figure."],
  ["edge", "A line segment where two faces meet."],
  ["net", "A flat pattern that folds up to make a solid figure."],
  ["surface area", "The total area of all the faces of a solid, in square units."],
  ["volume", "The amount of space a solid takes up, in cubic units."]],
 "reconnect": {
  "title": "Week 26: Area",
  "intro": "Surface area is just several areas added together. Warm up with last week's skills.",
  "items": [
   {"t":"num","q":"Find the area of a 12-inch by 8-inch rectangle.","a":96,"unit":"square inches","pts":2,"why":"12 × 8 = 96."},
   {"t":"num","q":"Find the area of a triangle with base 10 cm and height 7 cm.","a":35,"unit":"square cm","pts":2,"why":"½ × 10 × 7 = 35."},
   {"t":"num","q":"Flooring costs $3.00 per square foot. What does it cost for a 9-foot by 10-foot room?","a":270,"unit":"dollars","pts":2,"why":"90 × 3 = 270."},
   {"t":"open","key":"rc_composite","q":"Last week you found the area of an L-shaped room by splitting it into rectangles. How might that same idea help you find the total area of all the sides of a box?","min":15,"rows":2,"rubric":["Connects splitting a figure into parts with adding the areas of a box's faces"],"model":"A box is made of six rectangles, so I can find the area of each one and add them, just like adding the two rectangles of the L-shaped room."}]},
 "hook": {
  "title": "Maya Ships Her First Order",
  "visual": NET,
  "html": "<p>Maya's sourdough business is growing: a customer in Georgia wants three loaves shipped. Maya needs a box big enough to hold the loaves (that's <b>volume</b>) and wants to know how much cardboard and wrapping it takes (that's <b>surface area</b>). Shipping companies charge by weight and box size, so a box that's too big wastes money.</p><div class='callout'><b>Big question:</b> How do you measure the outside of a box, and how do you measure what fits inside?</div>"},
 "learn": [
  {"title": "Faces, Edges and Nets",
   "html": "<p>A <b>rectangular prism</b> has 6 rectangular <b>faces</b>, 12 <b>edges</b> and 8 vertices. Its faces come in three matching pairs: top and bottom, front and back, left and right.</p><p>A <b>net</b> is the prism unfolded flat. Cut along some edges of a cereal box and lay it flat, and you'll see a net. Different nets can fold into the same box, but every net of a rectangular prism has six rectangles in three matching pairs.</p>",
   "checks": [
    {"t":"num","q":"How many faces does a rectangular prism have?","a":6,"pts":2,"why":"Three matching pairs."},
    {"t":"open","key":"netcheck","q":"Someone drew a \"net\" for a 12 × 8 × 6 box with two 12 × 8 rectangles, two 12 × 6 rectangles and two 12 × 12 rectangles. Explain why it can't fold into the box and fix it.","min":20,"rows":2,"rubric":["Identifies the wrong pair","Names the correct dimensions of that pair"],"model":"The left and right faces must match the box's width and height, so they should be 8 × 6, not 12 × 12. Two 12 × 12 squares would stick out and wouldn't fold to close the box."}]},
  {"title": "Surface Area",
   "html": "<p><b>Surface area</b> is the total area of all six faces, measured in square units. Use the net: find the area of each pair and add.</p><p>For the 12 × 8 × 6 box: top and bottom 2(12 × 8) = 192; front and back 2(12 × 6) = 144; left and right 2(8 × 6) = 96. Total: <b>432 in²</b>.</p><p>Surface area answers questions about covering the outside: cardboard, wrapping paper, paint, labels.</p><p>A <b>pyramid</b> with a rectangular base works the same way: its net is the base plus triangles. Add the base's area and each triangle's area (½ × b × h, from Week 26).</p>",
   "checks": [
    {"t":"num","q":"Find the surface area of a box 10 cm long, 5 cm wide and 4 cm tall.","a":220,"unit":"square cm","pts":2,"why":"2(50) + 2(40) + 2(20) = 100 + 80 + 40 = 220."},
    {"t":"num","q":"A cube has edges of 3 inches. What is its surface area?","a":54,"unit":"square inches","pts":2,"why":"6 faces × 9 = 54."},
    {"t":"num","q":"A gift box is a pyramid with a 6 in × 6 in square base and four triangular faces, each with a base of 6 in and a height of 5 in. Find its surface area using its net.","a":96,"unit":"square inches","pts":2,"why":"Base 36 + 4 triangles × (½ × 6 × 5 = 15) = 36 + 60 = 96."},
    {"t":"num","q":"A box has a volume of 480 cubic inches and a base 10 in by 8 in. How tall is it?","a":6,"unit":"inches","pts":2,"why":"10 × 8 × h = 480, so h = 6."},
    {"t":"open","key":"wrapgift","q":"You're wrapping a 14 × 10 × 3 inch board game. Find the surface area, then explain why you'd cut a little more wrapping paper than that.","min":25,"rows":3,"rubric":["Correct surface area","A sensible reason for extra paper"],"model":"2(14 × 10) + 2(14 × 3) + 2(10 × 3) = 280 + 84 + 60 = 424 in². I'd cut a bit more because the paper needs to overlap at the seams and fold over the ends."}]},
  {"title": "Volume",
   "visual": CUBES,
   "html": "<p><b>Volume</b> is the number of unit cubes that fill a solid, measured in cubic units. For a rectangular prism, find the cubes in one layer (the base, l × w) and multiply by the number of layers (h): <b>V = l × w × h</b>.</p><p>Edges don't have to be whole numbers. A box 4½ inches by 3 inches by 2 inches holds 4.5 × 3 × 2 = <b>27 in³</b>. You can picture it filled with cubes ½ inch on a side: each tiny cube is ⅛ in³, and 216 of them fill the box.</p>",
   "checks": [
    {"t":"num","q":"Find the volume of the 12 × 8 × 6 inch shipping box.","a":576,"unit":"cubic inches","pts":2,"why":"12 × 8 × 6 = 576."},
    {"t":"num","q":"A planter box is 2.5 feet long, 1.5 feet wide and 1 foot deep. How many cubic feet of soil fill it?","a":3.75,"tol":0.001,"unit":"cubic feet","pts":2,"why":"2.5 × 1.5 × 1 = 3.75."},
    {"t":"open","key":"savssv","q":"For each job, say whether you need surface area or volume, and why: (a) painting a toy chest, (b) filling a fish tank, (c) buying cardboard for boxes, (d) buying mulch for a garden bed.","min":26,"rows":3,"rubric":["Four correct choices","A reason for each based on covering versus filling"],"model":"(a) Surface area, because paint covers the outside. (b) Volume, because water fills the inside. (c) Surface area, because cardboard covers the faces. (d) Volume, because mulch fills the bed's space."}]},
  {"title": "Money: Packaging and Shipping Costs",
   "html": "<p>Businesses balance box size and cost. Bigger boxes use more cardboard and often cost more to ship; many carriers charge by <b>dimensional weight</b>, so a large light box can cost as much as a small heavy one.</p><p>Maya's loaves need about 400 in³. Two box choices:</p><ul><li>Box A: 10 × 8 × 6 in. Volume 480 in³. Surface area 376 in². Costs $1.10; shipping $14.50.</li><li>Box B: 12 × 10 × 8 in. Volume 960 in³. Surface area 592 in². Costs $1.60; shipping $18.20.</li></ul><p>Box A holds the loaves and saves $4.20 per order.</p>",
   "checks": [
    {"t":"num","q":"How much does Maya save per order using Box A instead of Box B (box plus shipping)?","a":4.2,"tol":0.001,"unit":"dollars","pts":2,"why":"(1.60 + 18.20) − (1.10 + 14.50) = 19.80 − 15.60 = 4.20."},
    {"t":"num","q":"If Maya ships 25 orders a month, how much does she save in a month with Box A?","a":105,"unit":"dollars","pts":2,"why":"25 × 4.20 = 105."},
    {"t":"open","key":"boxchoice","q":"Box C is 9 × 9 × 5 in and costs $1.05 with $14.10 shipping. Can it hold Maya's 400 in³ of loaves? Should she switch? Show your work and consider more than the price.","min":35,"rows":3,"rubric":["Correct volume of Box C","A decision based on volume and cost","Considers another factor such as the loaves' shape or padding"],"model":"Box C's volume is 9 × 9 × 5 = 405 in³, just over 400, so it barely fits, with no room for padding. It saves $0.45 an order over Box A, but I'd stay with Box A because loaves squashed in a tight box would disappoint customers."}]}],
 "handson": {
  "title": "Box Factory",
  "intro": "Unfold a real box into a net, then design a custom box for a product in your home.",
  "materials": ["An empty cereal or cracker box", "Scissors", "A ruler or tape measure", "Graph paper or cardstock", "Tape", "About 24 identical small cubes or sugar cubes (optional)", "A small product to package (a mug, a book, a set of cards)", "Paper and pencil"],
  "steps": [
   "Measure the cereal box's length, width and height to the nearest quarter inch. Predict its surface area and volume.",
   "Carefully cut along the edges to unfold it into a net (an adult helps with thick cardboard). Measure each face and check your surface area prediction.",
   "Optional: fill a small box or a paper tray with cubes to see volume as layers.",
   "Choose a small product in your home. Design a box on graph paper or cardstock that fits it with about ½ inch to spare on every side. Draw the net, cut it out (leaving small tabs) and tape it together.",
   "Find your box's surface area and volume, and compare it with the product's volume.",
   "Keep scissors away from young children, and keep sugar cubes away from pets."],
  "record": [
   {"t":"open","key":"cerealrec","q":"Report the cereal box's dimensions, your predicted and measured surface area, and its volume. How close was your prediction, and what caused any difference?","min":35,"rows":4,"rubric":["Dimensions and calculations shown", "Compares prediction with measurement", "Explains a likely cause of any difference"],"model":"The box was 7.5 × 2.5 × 11 in. I predicted surface area 2(7.5 × 2.5) + 2(7.5 × 11) + 2(2.5 × 11) = 37.5 + 165 + 55 = 257.5 in². The unfolded cardboard was a little more because of the glued flaps. Volume: 7.5 × 2.5 × 11 = 206.25 in³."},
   {"t":"open","key":"designrec","q":"Describe the product you packaged, your box's dimensions, its surface area and volume, and how much empty space was left around the product.","min":35,"rows":4,"rubric":["Product and box dimensions","Correct surface area and volume","Explains the empty space and whether it's a good design"],"model":"I packaged a mug that measures 4 × 3.5 × 4.5 in (including the handle). My box is 5 × 4.5 × 5.5 in: surface area 2(22.5) + 2(27.5) + 2(24.75) = 149.5 in², volume 123.75 in³. The mug's bounding box is 63 in³, so about 60 in³ is left for padding, which is good for something breakable."}]},
 "think": {
  "intro": "Explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"samevolume","q":"Two boxes both hold 64 cubic inches: a 4 × 4 × 4 cube and a 16 × 2 × 2 box. Find the surface area of each. Which uses less cardboard, and what does that suggest about designing packages?","min":38,"rows":4,"rubric":["Correct surface area for each box", "Identifies which uses less material", "Draws a design conclusion"],"model":"The cube's surface area is 6 × 16 = 96 in². The long box's is 2(32) + 2(32) + 2(4) = 136 in². The cube uses less cardboard for the same volume, so boxes closer to cube-shaped waste less material, which saves money and trees."},
   {"t":"open","key":"doubleedges","q":"If you double every edge of a box, what happens to its surface area and its volume? Test with a 2 × 3 × 4 box and explain.","min":45,"rows":4,"rubric":["Correct calculations for both boxes", "States how many times larger the surface area and the volume become", "An explanation"],"model":"The 2 × 3 × 4 box has surface area 52 and volume 24. The 4 × 6 × 8 box has surface area 208 (4 times) and volume 192 (8 times). Area uses two dimensions, so it multiplies by 2 × 2; volume uses three, so it multiplies by 2 × 2 × 2."}]},
 "exit": [
  {"t":"num","q":"Find the volume of a box 6 cm by 5 cm by 3 cm.","a":90,"unit":"cubic cm","pts":2,"why":"6 × 5 × 3 = 90."},
  {"t":"num","q":"Find the surface area of the same box.","a":126,"unit":"square cm","pts":2,"why":"2(30) + 2(18) + 2(15) = 60 + 36 + 30 = 126."},
  {"t":"text","q":"Which measure tells how much wrapping paper covers a box?","a":[{"all":[["surface area"]],"none":["not surface"]}],"show":"surface area","pts":2,"why":"It measures the outside, in square units."},
  {"t":"open","key":"exit_units","q":"Why is volume measured in cubic units but surface area in square units?","min":11,"rows":2,"rubric":["Connects square units to flat faces and cubic units to filling space"],"model":"Surface area covers flat faces, measured with squares; volume fills space, measured with cubes."}],
 "next": "Week 28: statistical questions and data displays."
}

TEACHER = {
 "standards": [
  "MA.6.GR.2.3: Solve mathematical and real-world problems involving the volume of right rectangular prisms with positive rational number edge lengths using a visual model and a formula.",
  "MA.6.GR.2.4: Given a mathematical or real-world context, find the surface area of right rectangular prisms and right rectangular pyramids using the figure's net.",
  "Financial literacy: comparing costs to make business decisions (Jump$tart Spending and Saving)."],
 "materials": ["The interactive lesson", "An empty cereal box, scissors, ruler, graph paper or cardstock, tape, optional cubes, a small product to package", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 26 warm-up questions."],
  [4, "Hook", "Maya ships her first order; unfold the net."],
  [9, "Faces and nets", "Matching pairs; fix the bad net."],
  [12, "Surface area", "Add the pairs; wrap a game."],
  [12, "Volume", "Layers of cubes; fraction edges; surface area or volume?"],
  [11, "Shipping costs", "Compare boxes; monthly savings; Box C decision."],
  [6, "Assign", "Set up the box factory; assign Think Deeper and the Exit Check."]],
 "key_questions": ["Are you covering the outside or filling the inside?", "Which faces match?", "What units does your answer need?", "Is the cheapest box the best box?"],
 "misconceptions": ["Surface area and volume are the same thing.", "Counting only three faces for surface area.", "Using square units for volume.", "A bigger box is always better."],
 "support": ["Let students handle and unfold real boxes.", "Color-code the three pairs of faces.", "Provide a surface area table with three rows."],
 "challenge": ["Find the dimensions of the box with the least surface area that holds 1,000 cubic inches.", "Research how a real carrier calculates dimensional weight and apply it to Maya's boxes."],
 "background": "<p>MA.6.GR.2.4 asks for surface area of right rectangular prisms and pyramids using nets (pyramids are practiced in the Surface Area section); MA.6.GR.2.3 includes fractional and decimal edges. Box prices and shipping charges are practice figures.</p>",
 "sources": ["Florida Department of Education, B.E.S.T. Standards for Mathematics (2020).", "Jump$tart Coalition, National Standards for Personal Financial Education (2021)."]
}

PRINT = {
 "directions": "Show your work with units.",
 "items": [
  {"q":"Find the surface area and volume of a box 9 in by 4 in by 5 in.","a":"SA = 2(36) + 2(45) + 2(20) = 202 in²; V = 180 in³.","lines":3},
  {"q":"Find the volume of a box 3½ ft by 2 ft by 1½ ft.","a":"3.5 × 2 × 1.5 = 10.5 ft³.","lines":2},
  {"q":"A cube has 5-cm edges. Find its surface area and volume.","a":"SA = 150 cm²; V = 125 cm³.","lines":2},
  {"q":"Surface area or volume? (a) gift wrap (b) sand in a sandbox (c) labels on a box","a":"(a) surface area (b) volume (c) surface area","lines":2},
  {"q":"Box A costs $1.20 + $12.80 shipping; Box B costs $0.95 + $13.40. Which is cheaper per order, and by how much?","a":"A: $14.00; B: $14.35; A is cheaper by $0.35.","lines":2}]
}
