def grid(points, title, segs=(), lo=-8, hi=8, w=440, extra=""):
    """Four-quadrant grid. points: (x, y, label, color). segs: ((x1,y1),(x2,y2),color)."""
    pad = 34; n = hi - lo; u = (w - 2 * pad) / n
    X = lambda x: pad + (x - lo) * u
    Y = lambda y: pad + 16 + (hi - y) * u
    h = int(Y(lo) + pad - 6)
    s = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="{title}">',
         f'<text x="{w/2}" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="14">{title}</text>']
    for i in range(lo, hi + 1):
        s.append(f'<line x1="{X(i)}" y1="{Y(lo)}" x2="{X(i)}" y2="{Y(hi)}" stroke="#d6dde6"/>')
        s.append(f'<line x1="{X(lo)}" y1="{Y(i)}" x2="{X(hi)}" y2="{Y(i)}" stroke="#d6dde6"/>')
        if i and i % 2 == 0:
            s.append(f'<text x="{X(i)}" y="{Y(0)+13}" text-anchor="middle" font-size="9" fill="#5b6676">{str(i).replace("-", "−")}</text>')
            s.append(f'<text x="{X(0)-5}" y="{Y(i)+3}" text-anchor="end" font-size="9" fill="#5b6676">{str(i).replace("-", "−")}</text>')
    s.append(f'<line x1="{X(lo)}" y1="{Y(0)}" x2="{X(hi)}" y2="{Y(0)}" stroke="#0A1F3D" stroke-width="2"/><line x1="{X(0)}" y1="{Y(lo)}" x2="{X(0)}" y2="{Y(hi)}" stroke="#0A1F3D" stroke-width="2"/>')
    s.append(f'<text x="{X(hi)+4}" y="{Y(0)+4}" font-weight="bold" fill="#0A1F3D">x</text><text x="{X(0)}" y="{Y(hi)-6}" text-anchor="middle" font-weight="bold" fill="#0A1F3D">y</text>')
    for (a, b), (c, d), col in segs:
        s.append(f'<line x1="{X(a)}" y1="{Y(b)}" x2="{X(c)}" y2="{Y(d)}" stroke="{col}" stroke-width="3"/>')
    for x, y, lab, col in points:
        s.append(f'<circle cx="{X(x)}" cy="{Y(y)}" r="5" fill="{col}"/><text x="{X(x)+7}" y="{Y(y)-6}" font-weight="bold" font-size="11" fill="{col}">{lab}</text>')
    s.append(extra.format(**{f"x{i}": X(i) for i in range(lo, hi + 1) if i >= 0}, **{f"y{i}": Y(i) for i in range(lo, hi + 1) if i >= 0}) if extra else "")
    s.append('</svg>')
    return "".join(s)

QUADS = grid([(3, 5, "A (3, 5)", "#0047BA"), (-4, 2, "B (−4, 2)", "#DB2F30"), (-6, -3, "C (−6, −3)", "#2c6e22"), (5, -6, "D (5, −6)", "#8a6d1f")],
             "Four quadrants: signs of (x, y)",
             extra='<text x="{x4}" y="{y7}" font-size="12" font-weight="bold" fill="#0A1F3D">I (+, +)</text>')
QUADS = QUADS.replace('</svg>', '<text x="70" y="78" font-size="12" font-weight="bold" fill="#0A1F3D">II (−, +)</text><text x="70" y="420" font-size="12" font-weight="bold" fill="#0A1F3D">III (−, −)</text><text x="330" y="420" font-size="12" font-weight="bold" fill="#0A1F3D">IV (+, −)</text></svg>')

REFLECT = grid([(2, 5, "P (2, 5)", "#0047BA"), (-2, 5, "Q (−2, 5)", "#DB2F30"), (2, -5, "R (2, −5)", "#2c6e22")],
               "Reflections across the axes",
               segs=(((2, 5), (-2, 5), "#f0b8b8"), ((2, 5), (2, -5), "#b9dcb2")))

ROUTE = grid([(0, 0, "Home kitchen (0, 0)", "#0A1F3D"), (4, 3, "Farmers market", "#2c6e22"), (-5, 3, "Library", "#0047BA"), (-5, -4, "Ms. Ortiz", "#DB2F30"), (6, -4, "Mr. Bell", "#8a6d1f")],
             "Maya's Bread Delivery Map (1 unit = 1 block)",
             segs=(((-5, 3), (-5, -4), "#9fb7da"), ((-5, -4), (6, -4), "#e2b8b8")), lo=-7, hi=7)

LESSON = {
 "unit": "Unit 4: Integers and the Coordinate Plane",
 "title": "The Four-Quadrant Coordinate Plane",
 "subtitle": "In Week 9 you graphed ratio tables in the first quadrant, where every number is positive. Now that you know negative numbers, the grid opens in all four directions, and you can map a whole neighborhood with your home at the center.",
 "objectives": [
  "Name the parts of the coordinate plane: the x-axis, y-axis, origin and four quadrants.",
  "Plot and name ordered pairs, including negative numbers, fractions and decimals, in all four quadrants and on the axes.",
  "Identify the quadrant of a point from the signs of its coordinates.",
  "Recognize that points whose coordinates differ only in sign are reflections across an axis, and name the axis.",
  "Find horizontal and vertical distances between points to plan a business delivery route."],
 "vocab": [
  ["coordinate plane", "A flat grid formed by a horizontal number line (the x-axis) and a vertical number line (the y-axis)."],
  ["origin", "The point (0, 0), where the axes cross."],
  ["ordered pair", "Two numbers (x, y) that locate a point: x tells left or right, y tells up or down."],
  ["quadrant", "One of the four regions the axes divide the plane into, numbered I to IV counterclockwise from the upper right."],
  ["reflection", "A mirror image of a point across a line, such as an axis."],
  ["x-coordinate", "The first number in an ordered pair: the horizontal position."],
  ["y-coordinate", "The second number in an ordered pair: the vertical position."]],
 "reconnect": {
  "title": "Week 16: Integers and absolute value",
  "intro": "Every axis of today's grid is a number line like the ones you used last week.",
  "items": [
   {"t":"num","q":"What is |−9|?","a":9,"pts":2,"why":"Absolute value is distance from zero."},
   {"t":"text","q":"Which is greater, −4 or −11? Type the number.","a":["-4","−4"],"show":"−4","pts":2,"why":"−4 is to the right of −11 on a number line."},
   {"t":"text","q":"A bank statement shows a balance of −$15. Does the owner have money in the account or owe the bank? Type have or owe.","a":[{"all":[["owe"]],"none":["not owe","have"]}],"show":"owe","pts":2,"why":"A negative balance means the account is overdrawn by $15."},
   {"t":"open","key":"rc_vertical","q":"Last week's elevation chart was a vertical number line. Which direction was positive on it, and which was negative?","min":10,"rows":2,"rubric":["Up (above sea level) is positive; down (below sea level) is negative"],"model":"Up, above sea level, was positive, and down, below sea level, was negative."}]},
 "hook": {
  "title": "Maya's Bread Business Goes Local",
  "html": "<p>Maya is 12 and bakes sourdough loaves in her family's home kitchen to sell to neighbors. Her mom drives the deliveries, and every Saturday they waste time zigzagging. Maya has an idea: draw the neighborhood as a grid with <b>home at the center</b>. East is right, west is left, north is up and south is down. Every customer gets an address like (−5, −4): five blocks west, four blocks south.</p><p>To do that, Maya needs a grid where numbers go negative in two directions. That is the <b>four-quadrant coordinate plane</b>, the same system pilots, ship captains, video game designers and mapmakers use.</p><div class='callout'><b>Big question:</b> How can two numbers pin down any location, and how do they help a business save time?</div>"},
 "learn": [
  {"title": "Axes, Origin and Quadrants",
   "visual": QUADS,
   "html": "<p>The <b>x-axis</b> is a horizontal number line and the <b>y-axis</b> is a vertical one. They cross at the <b>origin</b>, (0, 0). To plot (x, y), start at the origin, move <b>x</b> units right (positive) or left (negative), then <b>y</b> units up (positive) or down (negative). Order matters: (3, 5) and (5, 3) are different points.</p><p>The axes split the plane into four <b>quadrants</b>, numbered with Roman numerals counterclockwise starting at the upper right:</p><ul><li>Quadrant I: (+, +)</li><li>Quadrant II: (−, +)</li><li>Quadrant III: (−, −)</li><li>Quadrant IV: (+, −)</li></ul><p>A point on an axis, like (0, −4) or (6, 0), is not in any quadrant.</p><p>Coordinates don't have to be whole numbers: (−2.5, 1½) is halfway between −3 and −2 across, and halfway between 1 and 2 up.</p>",
   "checks": [
    {"t":"blanks","q":"Use the grid. Name the quadrant of each point with a Roman numeral (I, II, III or IV).","sent":"B (−4, 2) is in Quadrant ___. C (−6, −3) is in Quadrant ___. D (5, −6) is in Quadrant ___.","blanks":[[{"all":[["ii","2"]],"none":["iii","iv"]}],[{"all":[["iii","3"]],"none":["iv"]}],[{"all":[["iv","4"]],"none":["iii"]}]],"show":"II; III; IV","pts":3,"why":"Signs: (−, +) is II, (−, −) is III, (+, −) is IV."},
    {"t":"text","q":"Without plotting, which quadrant is (−7.5, −0.5) in? Type the Roman numeral.","a":["iii","3","quadrant iii"],"show":"III","pts":2,"why":"Both coordinates are negative."},
    {"t":"text","q":"Where is the point (0, −4)? Type the name of the axis it lies on.","a":[{"all":[["y"]],"none":["not","x axis","x-axis"]}],"show":"on the y-axis","pts":2,"why":"x = 0 means no movement left or right, so the point is on the y-axis."},
    {"t":"open","key":"orderswap","q":"Ravi plotted (−3, 6) by going up 3 and left 6. Explain his mistake and where he should have gone.","min":20,"rows":2,"rubric":["He swapped the order: x comes first (left/right), y second (up/down)","Correct move: 3 left, then 6 up, ending in Quadrant II"],"model":"He mixed up the order. The first number, −3, is x, so he should go 3 left; the second number, 6, is y, so then 6 up. The point is in Quadrant II."}]},
  {"title": "Reflections Across the Axes",
   "visual": REFLECT,
   "html": "<p>Look at P (2, 5) and Q (−2, 5). Their y-coordinates match, and their x-coordinates are <b>opposites</b>. Q is the mirror image of P across the <b>y-axis</b>, the same distance from it on the other side.</p><p>Now look at P (2, 5) and R (2, −5). The x-coordinates match, and the y-coordinates are opposites. R is the reflection of P across the <b>x-axis</b>.</p><p>A quick rule: <b>the coordinate that changes sign tells you which way the point flips.</b> Changing x flips the point left-right, across the y-axis. Changing y flips it up-down, across the x-axis. Changing both sends it to the opposite quadrant.</p>",
   "checks": [
    {"t":"text","q":"Reflect (−6, 1) across the x-axis. Type the new ordered pair.","a":[{"all":[["-6"],["-1"]],"none":["not"]}],"show":"(−6, −1)","pts":2,"why":"Across the x-axis, the y-coordinate changes sign."},
    {"t":"text","q":"The points (4, −7) and (−4, −7) are reflections across which axis? Type x or y.","a":[{"all":[["y"]],"none":["x axis","x-axis","not"]}],"show":"the y-axis","pts":2,"why":"The x-coordinates are opposites, so the flip is left-right, across the y-axis."},
    {"t":"open","key":"bothsigns","q":"Amara says (3, 8) and (−3, −8) are reflections across one axis. Is she right? Explain, and describe how to get from one point to the other.","min":25,"rows":3,"rubric":["Not a reflection across a single axis: both coordinates changed sign","Reflect across one axis, then the other (ending in the opposite quadrant)"],"model":"She is not right. Both signs changed, so it isn't a single reflection. You would reflect (3, 8) across the y-axis to (−3, 8), then across the x-axis to (−3, −8). The point ends up in the opposite quadrant, III instead of I."}]},
  {"title": "Distance on the Grid",
   "html": "<p>On the coordinate plane, when two points share an x-coordinate or a y-coordinate, the distance between them is easy to find with what you learned last week:</p><ul><li><b>Same sign</b> (same side of the axis): subtract the absolute values. From (2, 7) to (2, 3): 7 − 3 = 4 units.</li><li><b>Opposite signs</b> (opposite sides of the axis): add the absolute values. From (−5, 3) to (4, 3): |−5| + |4| = 9 units.</li></ul><p>Why add? To travel from −5 to 4 you go 5 units to reach zero, then 4 more. Absolute value measures each piece.</p>",
   "checks": [
    {"t":"num","q":"How many units apart are (−6, −2) and (−6, 5)?","a":7,"unit":"units","pts":2,"why":"Opposite sides of the x-axis: |−2| + |5| = 7."},
    {"t":"num","q":"How many units apart are (−8, 4) and (−3, 4)?","a":5,"unit":"units","pts":2,"why":"Same side of the y-axis: |−8| − |−3| = 8 − 3 = 5."},
    {"t":"open","key":"addorsub","q":"Explain how to decide whether to add or subtract absolute values when finding the distance between (−4, 9) and (−4, −2). Then find the distance.","min":25,"rows":3,"rubric":["The y-coordinates have opposite signs (opposite sides of the x-axis), so add","Distance: 9 + 2 = 11 units"],"model":"The y-coordinates, 9 and −2, are on opposite sides of the x-axis, so I add their absolute values: 9 + 2 = 11 units."}]},
  {"title": "Money: Mapping a Delivery Route",
   "visual": ROUTE,
   "html": "<p>Maya's mom can only drive along streets, which run east-west and north-south, so they travel in straight horizontal and vertical lines. Each block of driving costs about <b>$0.25</b> in gas. Maya charges $9 per loaf.</p><p>This Saturday's stops: the library at (−5, 3), Ms. Ortiz at (−5, −4) and Mr. Bell at (6, −4). The colored lines show the drive from the library to Ms. Ortiz and on to Mr. Bell.</p>",
   "checks": [
    {"t":"num","q":"How many blocks is it from the library (−5, 3) to Ms. Ortiz (−5, −4)?","a":7,"unit":"blocks","pts":2,"why":"|3| + |−4| = 7 blocks."},
    {"t":"num","q":"How many blocks is it from Ms. Ortiz (−5, −4) to Mr. Bell (6, −4)?","a":11,"unit":"blocks","pts":2,"why":"|−5| + |6| = 11 blocks."},
    {"t":"num","q":"Each block costs about $0.25 in gas. What is the gas cost for those two legs together?","a":4.5,"unit":"dollars","tol":0.01,"pts":2,"why":"7 + 11 = 18 blocks; 18 × $0.25 = $4.50."},
    {"t":"open","key":"routeplan","q":"Maya sells Ms. Ortiz 2 loaves and Mr. Bell 3 loaves at $9 each. After the $4.50 for gas, how much does she earn from these two customers? Should she offer delivery to a customer 20 blocks away who buys just 1 loaf? Show your reasoning.","min":40,"rows":4,"rubric":["Earnings: 5 × $9 = $45; $45 − $4.50 = $40.50","Far customer: 20 blocks there (and possibly back) at $0.25 = $5 to $10, against $9 of sales","A reasoned decision (charge a delivery fee, require a minimum order, or combine with other stops)"],"model":"5 loaves × $9 = $45, and $45 − $4.50 = $40.50. A customer 20 blocks away costs $5 in gas one way and $10 round trip, while 1 loaf brings in $9, and that's before flour and her time. She should only deliver that far if the customer orders more loaves, pays a delivery fee, or lives near another stop."}]}],
 "handson": {
  "title": "Life-Size Coordinate Plane and Neighborhood Map",
  "intro": "Turn the floor or driveway into a coordinate plane, walk ordered pairs, then map your own neighborhood.",
  "materials": ["Painter's tape (indoors) or sidewalk chalk (outdoors)", "About 33 sticky notes or index cards and a marker", "A family member", "Graph paper or plain paper and a ruler", "Colored pencils", "Optional: a printed or phone map of your neighborhood"],
  "steps": [
   "Tape or chalk two long lines that cross in a plus sign. Mark −8 to 8 on each with sticky notes or chalk, about one foot apart. Label the x-axis and y-axis and stand on the origin.",
   "A family member calls out ordered pairs, such as (−3, 5), (6, −2), (0, −7) and (−4.5, −4.5). Walk to each one: x first, then y. Say the quadrant out loud.",
   "Reflection game: stand on a point. Your partner says \"flip across the x-axis\" or \"flip across the y-axis.\" Walk to the reflection and say its coordinates.",
   "On graph paper, make a neighborhood map with your home at the origin and one square as one block (or one house). Plot at least five real places you visit and write their coordinates.",
   "Plan a route that visits three places using only horizontal and vertical moves. Find the total blocks.",
   "Outdoors, chalk only on your own driveway or sidewalk, away from traffic, with an adult nearby."],
  "record": [
   {"t":"open","key":"walkrec","q":"List four ordered pairs you walked, the quadrant (or axis) of each, and one reflection you made with its starting and ending coordinates.","min":30,"rows":4,"rubric":["Four ordered pairs with correct quadrants or axes","One reflection with correct before and after coordinates and the axis named"],"model":"(−3, 5): Quadrant II. (6, −2): Quadrant IV. (0, −7): on the y-axis. (−4.5, −4.5): Quadrant III. Reflection: I stood on (6, −2), flipped across the x-axis and walked to (6, 2)."},
   {"t":"open","key":"maprec","q":"Describe your neighborhood map: list your five places with coordinates, your three-stop route, and the total number of blocks. Show how you found each leg's distance.","min":40,"rows":5,"rubric":["Five places with coordinates","A three-stop route using horizontal and vertical legs","Each leg's distance computed correctly with absolute value (add or subtract)","A correct total"],"model":"Home (0, 0), park (3, 2), grandma's house (−4, 2), church (−4, −3), grocery store (5, −3). Route: home to park: 3 right + 2 up = 5 blocks. Park to grandma's: |3| + |−4| = 7 blocks. Grandma's to church: |2| + |−3| = 5 blocks. Total: 17 blocks."}]},
 "think": {
  "intro": "Explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"rectangle","q":"Three corners of a rectangle are at (−4, 3), (5, 3) and (5, −2). Find the fourth corner, the length of each side, and the perimeter. Explain how you know.","min":60,"rows":5,"rubric":["Fourth corner (−4, −2)","Side lengths 9 and 5, found with absolute value","Perimeter 28 units","Clear reasoning (matching coordinates of opposite sides)"],"model":"The fourth corner is (−4, −2): it lines up with (−4, 3) vertically and with (5, −2) horizontally. The top side, from (−4, 3) to (5, 3), is |−4| + |5| = 9 units. The right side, from (5, 3) to (5, −2), is |3| + |−2| = 5 units. Perimeter = 9 + 5 + 9 + 5 = 28 units."},
   {"t":"open","key":"newstop","q":"Maya wants to rent a stall at a second market. Option A is at (−6, −6); option B is at (3, 6). Her current customers are at (−5, 3), (−5, −4) and (6, −4). Which location is closer to more of her customers if she drives only along streets? Show the block distances and give a business reason for your choice.","min":80,"rows":6,"rubric":["Correct street distances (horizontal + vertical) from each option to each customer","Comparison of totals or closeness","A business reason (gas cost, time, new customers)"],"model":"Street distance = horizontal blocks + vertical blocks. Option A (−6, −6): to (−5, 3) is 1 + 9 = 10; to (−5, −4) is 1 + 2 = 3; to (6, −4) is 12 + 2 = 14; total 27 blocks. Option B (3, 6): to (−5, 3) is 8 + 3 = 11; to (−5, −4) is 8 + 10 = 18; to (6, −4) is 3 + 10 = 13; total 42 blocks. Option A is closer to all three customers' total, so delivering from there saves gas and time, about 15 blocks or $3.75 per round of stops."}]},
 "exit": [
  {"t":"text","q":"Which quadrant has points with a negative x-coordinate and a positive y-coordinate? Type the Roman numeral.","a":[{"all":[["ii","2"]],"none":["iii","iv"]}],"show":"Quadrant II","pts":2,"why":"(−, +)."},
  {"t":"text","q":"Reflect (5, −3) across the y-axis. Type the new ordered pair.","a":[{"all":[["-5"],["-3"]],"none":["not"]}],"show":"(−5, −3)","pts":2,"why":"Across the y-axis, x changes sign."},
  {"t":"num","q":"How many units apart are (−7, 2) and (3, 2)?","a":10,"unit":"units","pts":2,"why":"|−7| + |3| = 10."},
  {"t":"open","key":"exit_origin","q":"What is the origin, and why do both of its coordinates equal 0?","min":12,"rows":2,"rubric":["The point where the axes cross","You move 0 left/right and 0 up/down from it"],"model":"The origin is where the x-axis and y-axis cross. Both coordinates are 0 because it is the starting point: zero steps across and zero steps up or down."}],
 "next": "Week 18: adding and subtracting integers, and balancing a business budget."
}

TEACHER = {
 "standards": [
  "MA.6.GR.1.1: Extend previous understanding of the coordinate plane to plot rational number ordered pairs in all four quadrants and on both axes. Identify the x- or y-axis as the line of reflection when two ordered pairs have an opposite x- or y-coordinate.",
  "MA.6.GR.1.2: Find distances between ordered pairs, limited to the same x-coordinate or the same y-coordinate, represented on the coordinate plane.",
  "MA.6.NSO.1.3: Given a mathematical or real-world context, interpret the absolute value of a number as the distance from zero on a number line. Find the absolute value of rational numbers.",
  "Financial literacy: estimating business costs (fuel) and pricing decisions (Jump$tart Earning Income)."],
 "materials": ["The interactive lesson", "Painter's tape or sidewalk chalk, about 33 sticky notes or index cards, a marker", "Graph paper, a ruler, colored pencils", "Optional: a neighborhood map", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 16 warm-up questions."],
  [4, "Hook", "Introduce Maya's delivery problem."],
  [12, "Axes, origin, quadrants", "Plot points in all four quadrants; quadrant signs; points on axes; fractional coordinates."],
  [10, "Reflections", "Compare P, Q and R; build the rule about which coordinate changes sign."],
  [10, "Distance", "Add or subtract absolute values; connect to the number line."],
  [12, "Delivery route", "Compute legs, gas cost and earnings; discuss a delivery fee."],
  [6, "Assign", "Walk a few ordered pairs on the floor grid; assign the neighborhood map, Think Deeper and the Exit Check."]],
 "key_questions": ["Which number tells left or right?", "How do the signs tell you the quadrant?", "Which coordinate changed sign, and which way did the point flip?", "Same side or opposite sides: add or subtract?"],
 "misconceptions": ["Swapping x and y.", "Numbering quadrants clockwise.", "Thinking points on an axis belong to a quadrant.", "Subtracting coordinates directly when they have opposite signs (5 − 3 instead of 5 + 3)."],
 "support": ["Use the phrase \"walk before you climb\" (x, then y).", "Color the four quadrants on the floor grid.", "Allow counting squares before using absolute value."],
 "challenge": ["Find all points that are exactly 5 street blocks from the origin on whole-number coordinates.", "Reflect a triangle across both axes and describe the final position."],
 "background": "<p>MA.6.GR.1.2 limits distances to points sharing an x- or y-coordinate; the Think Deeper question uses horizontal plus vertical street distance (taxicab distance), which is a sum of two such distances and stays within Grade 6. The gas estimate of $0.25 a block is a practice figure. The quadrant numbering convention (counterclockwise from the upper right) goes back to Descartes's analytic geometry as later standardized in textbooks.</p>",
 "sources": ["Florida Department of Education, B.E.S.T. Standards for Mathematics (2020), Grade 6 Geometric Reasoning.", "Jump$tart Coalition, National Standards for Personal Financial Education (2021)."]
}

PRINT = {
 "directions": "Show your work. Use graph paper if needed.",
 "items": [
  {"q":"Name the quadrant or axis for each point: (−2, 7), (4, −1), (0, 3), (−5.5, −2).","a":"II; IV; y-axis; III.","lines":2},
  {"q":"Reflect (−3, 8) across the x-axis and across the y-axis.","a":"Across x: (−3, −8). Across y: (3, 8).","lines":2},
  {"q":"Find the distance between (−9, −1) and (−9, 6).","a":"|−1| + |6| = 7 units.","lines":2},
  {"q":"Find the distance between (2, −4) and (10, −4).","a":"10 − 2 = 8 units.","lines":2},
  {"q":"A rectangle has corners (−3, 4), (6, 4), (6, −1) and (−3, −1). Find its perimeter.","a":"Sides 9 and 5; perimeter 28 units.","lines":3},
  {"q":"A delivery goes from (−4, 5) to (−4, −2) to (3, −2). How many blocks is that? At $0.25 a block, what is the gas cost?","a":"7 + 7 = 14 blocks; $3.50.","lines":3}]
}
