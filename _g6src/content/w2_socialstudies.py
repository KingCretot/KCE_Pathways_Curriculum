GRID = '''<svg viewBox="0 0 540 300" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Latitude and longitude grid with four cities">
<text x="270" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Latitude and longitude</text>
<rect x="40" y="30" width="480" height="240" fill="#eaf4fb" stroke="#0A1F3D"/>
<g stroke="#b9cfe0">''' + ''.join(f'<line x1="40" y1="{30+i*40}" x2="520" y2="{30+i*40}"/>' for i in range(1,6)) + ''.join(f'<line x1="{40+i*40}" y1="30" x2="{40+i*40}" y2="270"/>' for i in range(1,12)) + '''</g>
<line x1="40" y1="150" x2="520" y2="150" stroke="#DB2F30" stroke-width="2.5"/><text x="515" y="145" text-anchor="end" fill="#DB2F30" font-weight="bold">Equator 0°</text>
<line x1="280" y1="30" x2="280" y2="270" stroke="#0047BA" stroke-width="2.5"/><text x="284" y="44" fill="#0047BA" font-weight="bold">Prime Meridian 0°</text>
<g fill="#5b6676" font-size="10"><text x="36" y="73" text-anchor="end">60°N</text><text x="36" y="113" text-anchor="end">30°N</text><text x="36" y="193" text-anchor="end">30°S</text><text x="36" y="233" text-anchor="end">60°S</text>
<text x="40" y="285" text-anchor="middle">180°</text><text x="160" y="285" text-anchor="middle">90°W</text><text x="280" y="285" text-anchor="middle">0°</text><text x="400" y="285" text-anchor="middle">90°E</text><text x="520" y="285" text-anchor="middle">180°</text></g>
<g font-size="11"><circle cx="171" cy="113" r="5" fill="#C9A84C" stroke="#0A1F3D"/><text x="176" y="106">A</text>
<circle cx="320" cy="110" r="5" fill="#C9A84C" stroke="#0A1F3D"/><text x="326" y="104">B</text>
<circle cx="276" cy="127" r="5" fill="#C9A84C" stroke="#0A1F3D"/><text x="262" y="122">C</text>
<circle cx="328" cy="151" r="5" fill="#C9A84C" stroke="#0A1F3D"/><text x="334" y="166">D</text></g>
<text x="270" y="298" text-anchor="middle" font-size="11" fill="#0A1F3D">Each grid square is 30° tall and 30° wide.</text></svg>'''

TRUESIZE = '''<svg viewBox="0 0 540 250" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="True area comparison squares">
<text x="270" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">True area, drawn to scale (millions of square kilometers)</text>
<rect x="20" y="40" width="190" height="190" fill="#C9A84C"/><text x="115" y="140" text-anchor="middle" font-size="16" font-weight="bold" fill="#0A1F3D">Africa 30.4</text>
<rect x="230" y="40" width="108" height="108" fill="#0047BA"/><text x="284" y="98" text-anchor="middle" fill="#fff">U.S. 9.8</text>
<rect x="350" y="40" width="107" height="107" fill="#DB2F30"/><text x="403" y="98" text-anchor="middle" fill="#fff">China 9.6</text>
<rect x="230" y="160" width="63" height="63" fill="#0A1F3D"/><text x="261" y="196" text-anchor="middle" fill="#fff" font-size="11">India 3.3</text>
<rect x="305" y="160" width="51" height="51" fill="#7a8796"/><text x="331" y="190" text-anchor="middle" fill="#fff" font-size="10">Greenland</text><text x="331" y="225" text-anchor="middle" font-size="11">2.2</text>
<text x="470" y="185" font-size="11" fill="#5b6676">Square size shows</text><text x="470" y="200" font-size="11" fill="#5b6676">true land area.</text></svg>'''

LESSON = {
 "unit": "Unit 1: How We Know the Past",
 "title": "Maps, Projections and the True Size of the World",
 "subtitle": "Every flat map is a choice. Some choices change how we see the world.",
 "objectives": [
  "Locate places using latitude and longitude, and name the hemispheres.",
  "Explain why every flat map of a round Earth distorts size, shape, distance or direction.",
  "Compare the Mercator, Gall-Peters, Robinson and Winkel Tripel projections and what each is good for.",
  "Use real land-area data to describe the true size of Africa.",
  "Analyze a map as a source with a point of view."],
 "vocab": [
  ["latitude", "Imaginary lines that run east and west around Earth, measuring distance north or south of the equator in degrees."],
  ["longitude", "Imaginary lines that run from pole to pole, measuring distance east or west of the prime meridian in degrees."],
  ["equator", "The line of 0° latitude, dividing Earth into the Northern and Southern Hemispheres."],
  ["prime meridian", "The line of 0° longitude, which runs through Greenwich, England, dividing the Eastern and Western Hemispheres."],
  ["hemisphere", "Half of Earth: Northern, Southern, Eastern or Western."],
  ["map projection", "A method of showing the round Earth on a flat surface. Every projection distorts something."],
  ["distortion", "A change in the true size, shape, distance or direction of places on a map."],
  ["Mercator projection", "A 1569 map made for sailors that keeps directions and local shapes true but greatly enlarges places near the poles."],
  ["equal-area projection", "A projection, such as Gall-Peters, that shows every place at its true relative size but stretches shapes."]],
 "reconnect": {
  "title": "Week 1: sources, evidence and time",
  "intro": "Maps are sources too, and they have points of view. First, show what you remember about how historians work.",
  "items": [
   {"t":"text","q":"A map drawn by a Spanish sailor in 1529. Primary or secondary source?","a":["primary"],"pts":2,"why":"It was created at the time by someone who was there."},
   {"t":"text","q":"What do we call West African keepers of oral history?","a":["griot","griots","jeli","djeli"],"show":"griots","pts":2,"why":"Griots preserve history through speech and song."},
   {"t":"num","q":"How many years passed from 2600 BCE to 1300 BCE?","a":1300,"show":"1,300","unit":"years","pts":3,"why":"Both BCE: 2600 − 1300 = 1,300 years."},
   {"t":"text","q":"In what century was the year 1619?","a":["17th","17th century","seventeenth","seventeenth century","the 17th century"],"show":"17th century","pts":2,"why":"The 1600s are the 17th century."},
   {"t":"text","q":"In Week 1, which word revealed bias in the Spanish account of Florida?","a":["discovered","discover"],"show":"discovered","pts":2,"why":"\"Discovered\" ignored the Calusa and other nations who already lived there."},
   {"t":"text","q":"What does it mean to <b>corroborate</b> evidence?","a":[{"all":[["confirm","check","compare","agree","another source","other sources","verify","support","match"]]}],"show":"To confirm it with another source that agrees","pts":2,"why":"Corroborating means confirming with an independent source."}]},
 "hook": {
  "title": "The Map on the Wall",
  "html": "<p>Look at almost any classroom world map in the United States and find Greenland, the big white island near the top. Now find Africa. On many of those maps, Greenland looks about as big as Africa.</p><p>In reality, Africa is about <b>14 times larger</b> than Greenland. You could fit the United States, China and India inside Africa and still have room left over.</p><p>How can so many maps be so wrong? The answer is not a mistake. It is a choice, made in 1569 for a very different purpose, and copied for over 450 years.</p><div class='callout'><b>Big idea:</b> You cannot flatten a ball without stretching or tearing it. Every flat map distorts something, and the mapmaker chooses what to distort.</div>"},
 "learn": [
  {"title": "Latitude and Longitude",
   "visual": GRID,
   "html": "<p><b>Latitude</b> lines run east and west and measure how far north or south a place is from the <b>equator</b> (0°), up to 90° at each pole. <b>Longitude</b> lines run from pole to pole and measure how far east or west a place is from the <b>prime meridian</b> (0°), up to 180°.</p><p>Write a location with latitude first, then longitude: Cairo, Egypt is about <b>30°N, 31°E</b>. Lakeland, Florida is about <b>28°N, 82°W</b>.</p>",
   "checks": [
    {"t":"text","q":"Point <b>A</b> on the grid is a city at about 28°N, 82°W. Which hemispheres is it in? Type them like this: Northern and Western.","a":[{"all":[["north"],["west"]]}],"show":"Northern and Western","pts":3,"why":"N means north of the equator; W means west of the prime meridian."},
    {"t":"label","q":"Match each point to its city. Type the letter's city: choose from Cairo (30°N, 31°E), Timbuktu (17°N, 3°W) and Nairobi (1°S, 37°E).","labels":[["B",["cairo"]],["C",["timbuktu"]],["D",["nairobi"]]],"pts":4,"why":"B is north and east (Cairo). C is just west of the prime meridian and north of the equator (Timbuktu). D is just south of the equator and east (Nairobi)."},
    {"t":"num","q":"What is the latitude of the equator, in degrees?","a":0,"unit":"degrees","pts":2,"why":"The equator is 0° latitude."},
    {"t":"text","q":"Timbuktu, in Mali, is at about 17°N, 3°W. In which hemispheres is it located?","a":[{"all":[["north"],["west"]]}],"show":"Northern and Western","pts":3,"why":"North of the equator and just west of the prime meridian. Much of West Africa is in the Western Hemisphere."}]},
  {"title": "Why Every Flat Map Is Wrong Somewhere",
   "html": "<p>Earth is a sphere. A globe is accurate, but you cannot fold one into a book. Flattening a sphere always distorts at least one of four things: <b>size (area), shape, distance or direction</b>.</p><table class='t'><tr><th>Projection</th><th>Keeps true</th><th>Distorts</th><th>Best for</th></tr><tr><td><b>Mercator</b> (1569)</td><td>Direction and local shapes</td><td>Size: places near the poles look huge</td><td>Sailing and online street maps</td></tr><tr><td><b>Gall-Peters</b></td><td>Area (true relative size)</td><td>Shape: continents look stretched</td><td>Comparing sizes of countries</td></tr><tr><td><b>Robinson</b> (1963)</td><td>A balance; nothing perfect</td><td>A little of everything</td><td>General wall maps</td></tr><tr><td><b>Winkel Tripel</b></td><td>A balance with less size distortion</td><td>A little of everything</td><td>World maps (used by National Geographic since 1998)</td></tr></table><p>Gerardus Mercator, a Flemish mapmaker, designed his map for sailors. A straight line on it is a constant compass direction, which made navigation much easier. He was not trying to show the true size of continents.</p>",
   "checks": [
    {"t":"text","q":"What four things can a flat map distort? Name at least three.","a":[{"all":[["size","area","shape","distance","direction"],["size","area","shape","distance","direction"],["size","area","shape","distance","direction"]]}],"show":"size (area), shape, distance and direction","pts":3,"why":"Every projection distorts at least one of size, shape, distance and direction."},
    {"t":"text","q":"What was the Mercator projection originally designed for?","a":[{"all":[["sail","navigat","ship","sea","compass"]]}],"show":"Navigation by sailors","pts":2,"why":"Straight lines on it are constant compass directions, which helped sailors."},
    {"t":"text","q":"Which projection would you use to compare the true sizes of Brazil and Alaska?","a":["gall-peters","gall peters","peters","equal-area","equal area","an equal-area projection"],"show":"Gall-Peters (an equal-area projection)","pts":3,"why":"An equal-area projection shows true relative size."},
    {"t":"text","q":"Why does Greenland look so large on the Mercator map?","a":[{"all":[["pole","north","far from the equator","stretch","enlarg","bigger","near the top","latitude"]]}],"show":"It is near the North Pole, and Mercator stretches places more the farther they are from the equator.","pts":3,"why":"Mercator enlarges areas more and more toward the poles."}]},
  {"title": "The True Size of Africa",
   "visual": TRUESIZE,
   "html": "<p>Land area data, in millions of square kilometers (rounded): <b>Africa 30.4</b>, United States 9.8, China 9.6, India 3.3, Greenland 2.2.</p><p>Africa has 54 countries and more than 1.4 billion people. It stretches about 8,000 kilometers from Tunisia in the north to South Africa in the south. On a Mercator map, all of this shrinks, while Europe and North America swell.</p><div class='callout'>Use the numbers to check the claims, not just the pictures. Data is evidence.</div>",
   "checks": [
    {"t":"num","q":"What is the total area of the United States, China and India together, in millions of square kilometers?","a":22.7,"unit":"million km²","pts":3,"why":"9.8 + 9.6 + 3.3 = 22.7 million km² (a decimal skill from Math Week 2)."},
    {"t":"num","q":"After fitting those three countries inside Africa, how much area is left over?","a":7.7,"unit":"million km²","pts":3,"why":"30.4 − 22.7 = 7.7 million km²."},
    {"t":"num","q":"About how many times larger than Greenland is Africa? Divide and round to the nearest whole number.","a":14,"tol":0.5,"unit":"times","pts":3,"why":"30.4 ÷ 2.2 ≈ 13.8, which rounds to 14."},
    {"t":"text","q":"Many people looking at a Mercator map assume Greenland and Africa are about the same size. Based on the data, are they? Type yes or no.","a":["no"],"pts":2,"why":"Africa is about 14 times larger."}]},
  {"title": "Maps Have a Point of View",
   "html": "<p>A map is a <b>source</b>, made by people who make choices: which projection, what to put in the center, what to label, and which direction is up.</p><ul><li>Most world maps in the United States and Europe put Europe near the center and north at the top. That is a tradition, not a law of nature. In space there is no up.</li><li>In 1979, Australian Stuart McArthur published a world map with south at the top to challenge the idea that the Northern Hemisphere belongs \"on top.\"</li><li>In 2017, Boston Public Schools began adding Gall-Peters maps to classrooms so students would see the true sizes of Africa and South America.</li></ul><div class='callout'>A map that makes some continents look small, and puts others in the center, can quietly shape how people think about who is important. Global thinkers ask: who made this map, and why?</div>",
   "checks": [
    {"t":"text","q":"Is it scientifically required for north to be at the top of a map? Type yes or no.","a":["no"],"pts":2,"why":"North-up is a tradition. Earth has no up or down in space."},
    {"t":"num","q":"In what year did Boston Public Schools begin adding Gall-Peters maps to classrooms?","a":2017,"pts":2,"why":"2017, to show students the true relative sizes of continents."},
    {"t":"text","q":"Using what you learned about bias in Week 1, explain how a map can show a point of view.","a":[{"all":[["choice","choose","center","size","small","big","projection","top","label","important","decid","show"]]}],"show":"The mapmaker chooses the projection, center and labels, which can make some places look more important or bigger than others.","pts":3,"why":"Like word choice in a written source, the choices on a map can favor some places over others."}]}],
 "handson": {
  "title": "The Orange Peel Projection",
  "intro": "Feel the problem every mapmaker faces with your own hands.",
  "materials": ["An orange (or clementine)", "A fine-tip permanent marker", "A paper plate", "A ruler"],
  "steps": [
   "Draw an equator around the middle of the orange, and a prime meridian from top to bottom. Draw a few rough continent shapes, or simply draw a smiley face that crosses the equator.",
   "Measure and write down the length of your equator line with a strip of paper and a ruler.",
   "Carefully peel the orange in as few pieces as you can.",
   "Try to press the peel completely flat on the plate without tearing it more.",
   "Look at what happened to your drawings near the top and bottom (the poles) compared with the middle."],
  "record": [
   {"t":"open","key":"orange","q":"Describe what happened when you flattened the peel. Where did it tear or stretch the most? How does this explain why the Mercator map enlarges Greenland?","min":50,"rows":6}]},
 "think": {
  "items": [
   {"t":"open","key":"buy","q":"Your homeschool co-op has money for one large world map for its classroom. Which projection should it buy: Mercator, Gall-Peters or Winkel Tripel? Make a claim and support it with at least two pieces of evidence from this lesson. Then name one weakness of your choice.","min":90,"rows":8,"rubric":["Clear claim naming one projection","At least two pieces of evidence from the lesson (data, purpose of the projection, distortion)","Acknowledges a weakness of the chosen projection","Considers what students should learn from the map"]},
   {"t":"open","key":"impact","q":"How might growing up with maps that shrink Africa affect the way people think about Africa and its history? Connect your answer to the Week 1 idea that sources have a point of view.","min":60,"rows":6,"rubric":["Explains a possible effect on how people view Africa's importance","Connects to point of view and bias","Uses the true-size data as evidence"]}]},
 "exit": [
  {"t":"text","q":"What is the name of the line of 0° latitude?","a":["equator","the equator"],"pts":2,"why":"The equator divides the Northern and Southern Hemispheres."},
  {"t":"text","q":"What is the name of the line of 0° longitude?","a":["prime meridian","the prime meridian"],"pts":2,"why":"The prime meridian divides the Eastern and Western Hemispheres."},
  {"t":"text","q":"Nairobi, Kenya is at about 1°S, 37°E. Which two hemispheres is it in?","a":[{"all":[["south"],["east"]]}],"show":"Southern and Eastern","pts":3,"why":"S means south of the equator; E means east of the prime meridian."},
  {"t":"text","q":"Which projection keeps compass directions true but greatly enlarges places near the poles?","a":["mercator","the mercator","mercator projection"],"show":"Mercator","pts":2,"why":"Mercator was built for navigation."},
  {"t":"num","q":"Africa is about 30.4 million km² and India is about 3.3 million km². About how many times larger is Africa? Round to the nearest whole number.","a":9,"tol":0.5,"unit":"times","pts":3,"why":"30.4 ÷ 3.3 ≈ 9.2, which rounds to 9."},
  {"t":"text","q":"Why can't a flat map show the whole Earth perfectly?","a":[{"all":[["sphere","round","ball","curve","globe"]]}],"show":"Because Earth is a sphere, and flattening a curved surface always stretches or tears it.","pts":3,"why":"Like the orange peel, a sphere cannot lie flat without distortion."}],
 "next": "Week 3: human beginnings in Africa. You will use fossils and archaeology to trace where every human on Earth comes from."
}

TEACHER = {
 "standards": [
  "SS.6.G.1.1: Use latitude and longitude coordinates to understand the relationship between people and places on the Earth.",
  "SS.6.G.1.2: Analyze the purposes of map projections (political, physical, special purpose) and explain the applications of various types of maps.",
  "SS.6.G.1.4: Utilize tools geographers use to study the world.",
  "SS.6.W.1.3: Interpret primary and secondary sources.",
  "C3 Framework D2.Geo.3.6-8: Use paper-based and electronic mapping to explain relationships between locations and the characteristics of places."],
 "materials": ["The interactive lesson", "A globe if you have one", "An orange and a permanent marker", "Optional: thetruesize.com, a free website that lets students drag countries to compare true sizes", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 1 Reconnect questions."],
  [6, "Hook", "Put a Mercator world map on screen. Ask the student to guess how many Greenlands fit in Africa before revealing about 14."],
  [12, "Latitude and longitude", "Use the grid. Practice reading coordinates for Lakeland, Cairo, Timbuktu and Nairobi. Emphasize latitude first."],
  [10, "Projections", "Compare the four projections. If possible, show images of each side by side. Ask what each is good and bad for."],
  [10, "True size", "Work the area problems together. If online, have the student drag Greenland to the equator on thetruesize.com and watch it shrink."],
  [10, "Maps have a point of view", "Show a south-up map. Ask how it feels and why. Connect to bias from Week 1."],
  [6, "Orange peel live", "Do the orange peel together on camera, or start it and let the student finish after class."]],
 "key_questions": ["Who made this map, when and why?", "What does this projection keep true, and what does it give up?", "Why is the Mercator map still used for online street maps?", "What might a student in Nigeria or Brazil think of a map centered on Europe?", "What would change if the map put the Pacific Ocean in the center?"],
 "misconceptions": ["Thinking Mercator is simply wrong. It is accurate for direction and was built for navigation.", "Mixing up latitude and longitude. Latitude lines are flat like the rungs of a ladder (latitude, ladder).", "Thinking north-up is a scientific fact.", "Believing Africa is a country rather than a continent of 54 countries."],
 "support": ["Use a globe with the orange-peel activity to make the distortion concrete.", "Provide a coordinate practice card with four cities.", "Memory trick: latitude rungs are flat like a ladder; longitude lines are long, from pole to pole."],
 "challenge": ["Have the student find the coordinates of their own home and of a place where their family has roots.", "Ask the student to research the AuthaGraph projection (Japan, 2016) and compare it with Winkel Tripel."],
 "background": "<p>Land areas (approximate): Africa 30.37 million km², United States 9.83 million km² (including water), China 9.6 million km², India 3.29 million km², Greenland 2.17 million km². Gerardus Mercator published his projection in 1569. Arthur Robinson's projection dates to 1963; National Geographic used it from 1988 and adopted Winkel Tripel in 1998. Stuart McArthur's Universal Corrective Map of the World (south-up) was published in 1979. Boston Public Schools began introducing Peters projection maps in 2017.</p>",
 "sources": ["National Geographic Education: Map projections.", "U.S. Geological Survey: Map Projections poster.", "The Guardian (March 19, 2017): Boston public schools map switch aims to amend 500 years of distortion.", "CIA World Factbook: country area figures."]
}

PRINT = {
 "directions": "Answer in complete sentences. Show any math.",
 "items": [
  {"q":"Explain the difference between latitude and longitude, and name the 0° line of each.","a":"Latitude measures north and south of the equator (0°); longitude measures east and west of the prime meridian (0°).","lines":3},
  {"q":"Write the hemispheres for each place:  Cairo (30°N, 31°E) ________  Lakeland (28°N, 82°W) ________  Lima, Peru (12°S, 77°W) ________","a":"Northern and Eastern; Northern and Western; Southern and Western","lines":2},
  {"q":"Name one thing the Mercator projection keeps true and one thing it distorts.","a":"Keeps direction (and local shape) true; distorts size near the poles.","lines":2},
  {"q":"Africa is about 30.4 million km². The United States is about 9.8 million km². About how many United States would fit inside Africa? Show your work.","a":"30.4 ÷ 9.8 ≈ 3.1, so about 3","lines":2},
  {"q":"Why did your orange peel tear and stretch when you tried to flatten it? What does that show about flat maps?","a":"A curved surface cannot lie flat without stretching or tearing; every flat map distorts something.","lines":3},
  {"q":"Explain how a world map can have a point of view. Give one example.","a":"Mapmakers choose the projection, center and orientation; for example, Mercator enlarges Europe and North America and shrinks Africa, or maps put Europe in the center.","lines":3}]
}
