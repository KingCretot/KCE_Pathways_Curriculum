from geo import NILE, BLUE_NILE

def nilemap():
    # Schematic Nile Valley map, north at the top. Labels sit in a right-hand column with leader lines.
    k = 12.5
    P = lambda lon, lat: (round((lon - 26) * k + 20, 1), round((33 - lat) * k + 34, 1))
    pts = lambda L: ' '.join('%s,%s' % P(*p) for p in L)
    mapw = 18 * k; W = int(mapw + 40 + 210); H = int(36 * k + 50)
    s = (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Map of the Nile Valley from Lake Victoria to the Mediterranean">'
         f'<text x="{W/2}" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The Nile flows north</text>'
         f'<rect x="20" y="34" width="{mapw}" height="{36*k}" fill="#efe1bd"/>')
    s += f'<polygon points="{pts([(26,33),(44,33),(44,31.4),(34.2,31.2),(32,31.5),(30,31.6),(28,31.0),(26,31.3)])}" fill="#bcd9ef"/>'
    west = [(32.6,29.9),(33.6,27.5),(35.4,24),(37.2,21),(38.6,18),(39.7,15.5),(41.5,13.3),(43,12.5)]
    east = [(44,12.6),(42.6,14.5),(41.2,17.5),(39.6,20.5),(38,24),(36.2,27),(34.9,29.5)]
    s += f'<polygon points="{pts(west + east)}" fill="#bcd9ef"/>'
    s += f'<ellipse cx="{P(33,-1)[0]}" cy="{P(33,-1)[1]}" rx="30" ry="16" fill="#bcd9ef"/><ellipse cx="{P(37.3,12)[0]}" cy="{P(37.3,12)[1]}" rx="7" ry="8" fill="#bcd9ef"/>'
    s += f'<polyline points="{pts(NILE[-6:])}" fill="none" stroke="#7fb06a" stroke-width="13" stroke-linejoin="round" opacity=".85"/>'
    s += f'<polygon points="{pts([(31.2,30),(29.8,31.4),(32.4,31.4)])}" fill="#7fb06a"/>'
    s += f'<polyline points="{pts(NILE)}" fill="none" stroke="#0047BA" stroke-width="3"/><polyline points="{pts(BLUE_NILE)}" fill="none" stroke="#0047BA" stroke-width="3"/>'
    marks = [(31, 31.0, 'Delta'), (31.2, 29.85, 'Memphis'), (31.9, 26.2, 'Abydos'), (32.6, 25.7, 'Thebes (Waset)'), (32.8, 25.1, 'Hierakonpolis (Nekhen)'),
             (32.9, 24.1, 'Aswan: First Cataract'), (32.5, 15.6, 'Khartoum: the two Niles meet'), (37.3, 12, 'Lake Tana: Blue Nile source'), (33, -1, 'Lake Victoria: White Nile source')]
    lx = mapw + 34; last = -99
    for lon, lat, lab in marks:
        x, y = P(lon, lat); ly = max(y, last + 17); last = ly
        s += f'<circle cx="{x}" cy="{y}" r="4" fill="#DB2F30" stroke="#fff"/><path d="M{x+4} {y} L{lx-4} {ly}" stroke="#8a8f99" stroke-width=".8"/><text x="{lx}" y="{ly+4}" font-size="11">{lab}</text>'
    a, b = P(26.6, 31.2), P(26.6, 29.3); c, d = P(26.6, 29.0), P(26.6, 24.0)
    s += (f'<path d="M{a[0]} {a[1]} v{b[1]-a[1]}" stroke="#0A1F3D" stroke-width="3"/><text x="{a[0]+6}" y="{(a[1]+b[1])/2}" font-weight="bold" fill="#0A1F3D" font-size="11" style="paint-order:stroke;stroke:#efe1bd;stroke-width:4">LOWER EGYPT</text><text x="{a[0]+6}" y="{(a[1]+b[1])/2+13}" font-size="10" style="paint-order:stroke;stroke:#efe1bd;stroke-width:4">north, downstream</text>'
          f'<path d="M{c[0]} {c[1]} v{d[1]-c[1]}" stroke="#0A1F3D" stroke-width="3"/><text x="{c[0]+6}" y="{(c[1]+d[1])/2}" font-weight="bold" fill="#0A1F3D" font-size="11" style="paint-order:stroke;stroke:#efe1bd;stroke-width:4">UPPER EGYPT</text><text x="{c[0]+6}" y="{(c[1]+d[1])/2+13}" font-size="10" style="paint-order:stroke;stroke:#efe1bd;stroke-width:4">south, upstream</text>'
          f'<text x="{P(27,19.5)[0]}" y="{P(27,19.5)[1]}" font-weight="bold" fill="#5b4a1c">NUBIA</text><text x="{P(39,7)[0]}" y="{P(39,7)[1]}" font-weight="bold" fill="#5b4a1c" text-anchor="middle">ETHIOPIA</text>'
          f'<path d="M{mapw} 54 v34" stroke="#0A1F3D" stroke-width="2"/><path d="M{mapw} 46 l-6 12 h12z" fill="#0A1F3D"/><text x="{mapw}" y="102" text-anchor="middle" font-weight="bold">N</text>'
          f'<text x="{P(27,32.4)[0]}" y="{P(27,32.4)[1]}" font-size="11" fill="#0A1F3D">Mediterranean Sea</text><text x="{P(38.6,21.5)[0]}" y="{P(38.6,21.5)[1]}" font-size="10" fill="#0A1F3D" transform="rotate(-55 {P(38.6,21.5)[0]} {P(38.6,21.5)[1]})">Red Sea</text></svg>')
    return s

SEASONS = ('<svg viewBox="0 0 560 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="The three seasons of the Egyptian year">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Three seasons, set by the river</text>'
  + ''.join(f'<g transform="translate({20+i*180} 34)"><rect width="160" height="180" rx="12" fill="{c}"/><text x="80" y="34" text-anchor="middle" fill="#fff" font-family="Georgia" font-size="22" font-weight="bold">{n}</text>'
            f'<text x="80" y="56" text-anchor="middle" fill="#fff" font-size="12">{m}</text><text x="80" y="74" text-anchor="middle" fill="#fff" font-size="11">{mo}</text>'
            + ''.join(f'<text x="80" y="{104+j*17}" text-anchor="middle" fill="#fff" font-size="11">{t}</text>' for j, t in enumerate(lines)) + '</g>'
            for i, (n, m, mo, c, lines) in enumerate([("Akhet", "Inundation", "about June to September", "#0047BA", ["The river floods the", "valley. Farmers repair", "tools and work on", "building projects."]),
                                                      ("Peret", "Emergence", "about October to February", "#2e7d32", ["Water drains away and", "leaves black silt.", "Farmers plow and", "plant wheat and barley."]),
                                                      ("Shemu", "Harvest", "about March to May", "#C9A84C", ["Crops ripen. Farmers", "harvest, store grain", "and fix canals before", "the next flood."])])) + '</svg>')

def crosssection():
    s = ('<svg viewBox="0 0 560 200" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Cross-section of the Nile valley showing black land and red land">'
         '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Kemet and Deshret: the Black Land and the Red Land</text>'
         '<path d="M0 70 L120 70 L150 120 L410 120 L440 70 L560 70 L560 200 L0 200Z" fill="#d9a066"/>'
         '<path d="M150 120 L410 120 L410 132 L150 132Z" fill="#3b2a1a"/>'
         '<path d="M260 120 Q280 150 300 120Z" fill="#0047BA"/>'
         '<path d="M150 104 L410 104" stroke="#0047BA" stroke-dasharray="6 4" stroke-width="2"/><text x="280" y="98" text-anchor="middle" fill="#0047BA" font-weight="bold">flood level in Akhet</text>'
         '<path d="M175 120 v-10 M205 120 v-10 M235 120 v-10 M325 120 v-10 M355 120 v-10 M385 120 v-10" stroke="#5c8a3a" stroke-width="3"/>'
         '<text x="60" y="60" text-anchor="middle" fill="#8a3b12" font-weight="bold">Deshret</text><text x="60" y="160" text-anchor="middle" fill="#fff">red desert</text>'
         '<text x="500" y="60" text-anchor="middle" fill="#8a3b12" font-weight="bold">Deshret</text><text x="500" y="160" text-anchor="middle" fill="#fff">red desert</text>'
         '<text x="200" y="152" text-anchor="middle" fill="#fff" font-weight="bold">Kemet</text><text x="200" y="168" text-anchor="middle" fill="#fff" font-size="11">black silt fields</text>'
         '<text x="360" y="152" text-anchor="middle" fill="#fff" font-weight="bold">Kemet</text><text x="360" y="168" text-anchor="middle" fill="#fff" font-size="11">black silt fields</text>'
         '<text x="280" y="190" text-anchor="middle" fill="#fff" font-size="11">the Nile</text></svg>')
    return s

CROWNS = ('<svg viewBox="0 0 560 190" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="The white crown, red crown and double crown">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Two lands, one king</text>'
  '<g transform="translate(70 40)"><path d="M10 110 Q0 60 25 20 Q40 0 55 20 Q80 60 70 110Z" fill="#f4f1ea" stroke="#0A1F3D" stroke-width="2"/><text x="40" y="132" text-anchor="middle" font-weight="bold">White Crown</text><text x="40" y="148" text-anchor="middle" font-size="11">Upper Egypt (south)</text></g>'
  '<g transform="translate(240 40)"><path d="M0 110 L0 50 L45 50 L45 0 L62 0 L62 110Z" fill="#DB2F30" stroke="#0A1F3D" stroke-width="2"/><path d="M10 55 Q-6 30 22 28" fill="none" stroke="#C9A84C" stroke-width="3"/><text x="32" y="132" text-anchor="middle" font-weight="bold">Red Crown</text><text x="32" y="148" text-anchor="middle" font-size="11">Lower Egypt (north)</text></g>'
  '<g transform="translate(400 40)"><path d="M0 110 L0 50 L52 50 L52 0 L70 0 L70 110Z" fill="#DB2F30" stroke="#0A1F3D" stroke-width="2"/><path d="M14 110 Q8 70 26 36 Q37 20 48 36 Q62 70 56 110Z" fill="#f4f1ea" stroke="#0A1F3D" stroke-width="2"/><text x="36" y="132" text-anchor="middle" font-weight="bold">Double Crown</text><text x="36" y="148" text-anchor="middle" font-size="11">the Two Lands united</text></g></svg>')

LESSON = {
 "unit": "Unit 2: The Nile Valley and Ancient Africa",
 "title": "The Nile: Geography and the Rise of Kemet (Egypt)",
 "subtitle": "One river, flowing north through the desert, made one of the world's longest-lasting civilizations possible.",
 "objectives": [
  "Locate the Nile, its two main sources, the cataracts, Upper and Lower Egypt and Nubia on a map.",
  "Explain how the yearly flood created the Black Land and shaped the farming year.",
  "Describe how people used basin irrigation and the nilometer to manage the flood.",
  "Explain how the drying of the Sahara brought peoples to the Nile Valley.",
  "Describe how the kingdom of Kemet was unified from the south around 3100 BCE."],
 "vocab": [
  ["Kemet", "The ancient Egyptians' own name for their country, meaning the Black Land."],
  ["Deshret", "The Red Land: the desert on either side of the Nile Valley."],
  ["inundation", "The yearly flood of the Nile."],
  ["silt", "Fine, rich soil carried by flowing water and left behind when a flood goes down."],
  ["cataract", "A stretch of rocky rapids in a river. The Nile has six main cataracts between Aswan and Khartoum."],
  ["basin irrigation", "Trapping floodwater in walled fields (basins) so it soaks into the soil."],
  ["nilometer", "A staircase or marked pillar used to measure the height of the Nile's flood."],
  ["delta", "The wide, triangle-shaped area where a river splits into branches before reaching the sea."],
  ["unification", "Joining separate regions into one country under one government."]],
 "reconnect": {
  "title": "Unit 1: farming, maps and evidence",
  "intro": "Unit 2 builds on everything from Unit 1. The first farmers, the drying Sahara and map skills all lead to the Nile.",
  "items": [
   {"t":"text","q":"What word means extra food that can be stored or traded, which allowed some people to become specialists?","a":["surplus","a surplus"],"pts":2,"why":"A surplus lets some people do work other than farming."},
   {"t":"open","key":"rc_sahara","q":"In Week 4 you read that the Green Sahara dried after about 5,000 years ago. Predict what herders living there would have done, and why.","min":15,"rows":2,"rubric":["They moved toward water: the Nile, oases or the Sahel","Because grass and water disappeared"],"model":"They probably moved toward reliable water, like the Nile Valley or farther south, because the grass for their cattle and the lakes dried up."},
   {"t":"text","q":"On a map, which direction is usually at the top?","a":["north"],"pts":2,"why":"Most maps put north at the top, which matters for this week's surprise."},
   {"t":"open","key":"rc_source","q":"The Narmer Palette is a carved stone object from about 3100 BCE. Is it a primary or secondary source, and what is one question a historian should ask about it?","min":15,"rows":2,"rubric":["Primary source","A good historian's question (who made it, for whom, what message, is it propaganda)"],"model":"It is a primary source because it was made at the time. A historian should ask who made it and what message the king wanted people to believe."}]},
 "hook": {
  "title": "A River Backwards?",
  "visual": nilemap(),
  "html": "<p>Look at the map. The Nile begins in the heart of Africa, near Lake Victoria and in the highlands of Ethiopia, and flows <b>north</b> about 6,650 kilometers (about 4,130 miles) to the Mediterranean Sea. That means \"up\" the river is south. The ancient Egyptians called the southern part of their country <b>Upper Egypt</b>, because it was upstream, and the northern part <b>Lower Egypt</b>.</p><p>Almost no rain falls in most of Egypt. Yet for thousands of years, millions of people lived there, fed by one river. How?</p><div class='callout'><b>Big idea:</b> The Nile's yearly flood turned a desert into the Black Land, and people who learned to manage that flood built the kingdom of Kemet.</div>"},
 "learn": [
  {"title": "Where the Water Comes From",
   "html": "<p>The Nile has two main branches. The <b>White Nile</b> flows from the Lake Victoria region in East Africa. The <b>Blue Nile</b> flows from Lake Tana in the highlands of Ethiopia. They meet at Khartoum, in today's Sudan.</p><p>Every summer, heavy monsoon rains fall on the Ethiopian Highlands. The Blue Nile and the Atbara River carry this water, and tons of dark soil, north. Most of the floodwater that reached Egypt came from Ethiopia. In other words, Egypt's farms depended on rain that fell more than 1,500 kilometers away in another part of Africa.</p><p>Between Aswan and Khartoum the river crosses six rocky <b>cataracts</b>. The First Cataract at Aswan was the traditional southern border of Egypt; south of it was <b>Nubia</b>.</p>",
   "checks": [
    {"t":"blanks","q":"Name the two main branches of the Nile and where each begins.","sent":"The ___ Nile begins near Lake Victoria. The ___ Nile begins in the Ethiopian Highlands.","blanks":[["white"],["blue"]],"pts":3,"why":"The White Nile comes from the Lake Victoria region; the Blue Nile from Lake Tana in Ethiopia."},
    {"t":"open","key":"ethiopia","q":"Explain why a rainy summer in Ethiopia mattered so much to a farmer in Egypt, more than 1,500 kilometers away.","min":20,"rows":3,"rubric":["Ethiopian monsoon rains fed the Blue Nile and the flood","The flood watered Egypt's fields and brought fertile silt","Egypt itself gets almost no rain"],"model":"Almost no rain falls in Egypt, so farmers depended on the flood. The flood came from monsoon rains in the Ethiopian Highlands, which filled the Blue Nile and carried water and black silt all the way to Egypt's fields."},
    {"t":"text","q":"If you sail from Aswan to Memphis, are you traveling upstream or downstream?","a":["downstream"],"pts":2,"why":"Memphis is north of Aswan, and the Nile flows north, so you go downstream."}]},
  {"title": "The Black Land and the Red Land",
   "visual": crosssection(),
   "html": "<p>When the flood went down, it left a layer of black <b>silt</b> on the fields. The Egyptians called their country <b>Kemet</b>, the Black Land, and the desert beyond it <b>Deshret</b>, the Red Land. The line between them was so sharp that a person could stand with one foot on green farmland and the other on desert sand.</p><p>Most Egyptologists connect the name Kemet to the color of the soil. The Senegalese historian and scientist Cheikh Anta Diop argued that it also described the people themselves. You will study his ideas and the evidence next week.</p><p>The Greek historian Herodotus, who visited around 450 BCE, called Egypt \"the gift of the river.\" But the river did not give food for free. People had to work together to capture the flood.</p>",
   "checks": [
    {"t":"blanks","q":"Complete the sentence.","sent":"The Egyptians called their farmland ___, the Black Land, and the desert ___, the Red Land.","blanks":[["kemet","kmt"],["deshret"]],"pts":3,"why":"Kemet was the dark, silt-covered farmland; Deshret was the desert."},
    {"t":"open","key":"giftriver","q":"Herodotus called Egypt \"the gift of the river.\" Agree or disagree: was the Nile's wealth a free gift? Use one piece of evidence from the lesson.","min":25,"rows":3,"rubric":["Takes a position","Explains the role of the flood","Explains the human work needed (irrigation, planning, measuring)"],"model":"I partly disagree. The flood brought water and silt for free, but people had to build basin walls, dig canals, measure the flood and plan their planting to turn that gift into food."}]},
  {"title": "Managing the Flood",
   "visual": SEASONS,
   "html": "<p>The Egyptian year had three seasons, all named for the river. Farmers built <b>basin irrigation</b>: earthen walls that trapped floodwater in fields so it soaked deep into the soil before draining back. They dug canals to carry water farther from the river.</p><p>To predict the harvest, officials measured the flood with <b>nilometers</b>, stone staircases or pillars marked in cubits (a cubit was about 52 centimeters). The nilometer on Elephantine Island at Aswan was among the most important, because the flood reached it first. A flood that was too low meant hunger. A flood that was too high could wash away villages. Officials also used nilometer readings to estimate the harvest and set taxes.</p><p>Managing all this required planning, record keeping and many people working together, which helped lead to strong leaders and a government.</p>",
   "checks": [
    {"t":"text","q":"In which season did farmers plant their crops in the black silt?","a":["peret","emergence","peret (emergence)"],"show":"Peret (Emergence)","pts":2,"why":"After the flood drained, farmers planted in Peret."},
    {"t":"num","q":"A nilometer reading shows a flood of 16 cubits. If one cubit is about 52 centimeters, about how many meters is that? Round to the nearest tenth.","a":8.3,"tol":0.051,"unit":"m","pts":3,"why":"16 × 52 = 832 cm = 8.32 m, about 8.3 meters."},
    {"t":"open","key":"toolow","q":"Explain why both a very low flood and a very high flood were dangerous, and why measuring the flood helped the government.","min":30,"rows":3,"rubric":["Low flood: not enough water for fields, hunger","High flood: destroyed villages, walls and canals","Measuring helped predict harvests, store food and set taxes"],"model":"A low flood could not reach the higher fields, so crops failed and people went hungry. A very high flood washed away mud-brick villages and canals. Measuring the flood let officials predict the harvest, store extra grain and set fair taxes."}]},
  {"title": "From Villages to a Kingdom",
   "visual": CROWNS,
   "html": "<p>As the Sahara dried, many herders and farmers moved into the Nile Valley. In Upper Egypt in the south, farming cultures archaeologists call the <b>Badarian</b> and <b>Naqada</b> grew into towns with powerful leaders. Their pottery, cattle traditions and burial customs were closely related to those of peoples in Nubia and the eastern Sahara.</p><p>Around 3100 BCE, a ruler from the south, remembered as <b>Narmer</b>, is believed to have united Upper and Lower Egypt. The <b>Narmer Palette</b>, found at Hierakonpolis (Nekhen) in Upper Egypt, shows him wearing the White Crown of the south on one side and the Red Crown of the north on the other. Later kings wore both together as the Double Crown, and called themselves \"Lord of the Two Lands.\"</p><p>Notice the direction: Egypt was unified from the <b>south</b>, from the part of the country closest to the rest of Africa.</p>",
   "checks": [
    {"t":"text","q":"Which crown stood for Upper Egypt, in the south?","a":["white","the white crown","white crown"],"show":"the White Crown","pts":2,"why":"The White Crown stood for Upper Egypt; the Red Crown for Lower Egypt."},
    {"t":"num","q":"How many years ago was 3100 BCE, counting to the year 2026?","a":[5126,5125],"unit":"years","show":"about 5,125 years (5,126 by simple adding)","pts":3,"why":"3,100 + 2,026 = 5,126, or 5,125 exactly because there is no year 0."},
    {"t":"open","key":"palette","q":"The Narmer Palette was made for a king. What message did it send to people who saw it? Why should a historian be careful using it as evidence?","min":30,"rows":3,"rubric":["Message: the king is powerful, has united the Two Lands, defeated enemies","Caution: made to praise the king (propaganda); may exaggerate or be symbolic"],"model":"It told people the king was powerful, had defeated his enemies and now ruled both lands. A historian should be careful because it was made to praise the king, so it shows his side and may exaggerate or be symbolic rather than an exact record."}]}],
 "handson": {
  "title": "Build a Nile Floodplain and Nilometer",
  "intro": "Model how the flood created the Black Land, and measure it like an Egyptian official.",
  "materials": ["A baking pan or plastic storage bin", "Sand or light soil for the desert", "Dark potting soil or coffee grounds for silt", "A cup or pitcher of water", "A clear plastic cup and a ruler (for the nilometer)", "A marker and a towel", "Optional: a few seeds such as beans or grass seed"],
  "steps": [
   "Shape sand in the pan into a valley with a channel down the middle. Tilt the pan slightly so water flows toward one end (the north).",
   "Mix a handful of dark soil into the water. Slowly pour it into the high end so it overflows the channel. This is the inundation.",
   "Let it sit 10 minutes, then gently tip off the extra water. Observe where the dark layer settled.",
   "Make a nilometer: mark the clear cup every 1 cm and label the marks. Pour in three different amounts of water and record each flood level.",
   "Optional: plant seeds in the dark layer and in the sand, keep both damp, and compare growth over a week."],
  "record": [
   {"t":"open","key":"flood","q":"Describe where the dark silt settled in your model and explain how this connects to the names Kemet and Deshret.","min":30,"rows":4,"rubric":["Silt settled on the flat floodplain near the channel","Sand away from the channel stayed light","Connects to Black Land and Red Land"],"model":"The dark soil settled in a strip along both sides of the channel where the water spread out and slowed down. The higher sand stayed light. That is just like Kemet, the black farmland along the river, and Deshret, the red desert beyond it."},
   {"t":"open","key":"nilo","q":"Record your three nilometer readings. If 1 cm on your cup stood for 1 cubit, which flood would be best for farming, and why?","min":25,"rows":3,"rubric":["Three readings with units","Chooses a middle reading","Explains too low and too high"],"model":"My readings were 4 cm, 8 cm and 12 cm. The 8 cm flood would be best: 4 cm would be too low to reach the higher fields, and 12 cm might wash away the basin walls and villages."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"geoarg","q":"Some people say geography made Egyptian civilization; others say the people did. Write a paragraph arguing which mattered more. Use at least three pieces of evidence from this lesson and answer the other side.","min":90,"rows":10,"rubric":["Clear claim","Three accurate pieces of evidence (flood, silt, Ethiopia rains, irrigation, nilometers, unification)","Answers the opposing view","Organized with a conclusion"],"model":"Geography gave the opportunity, but people made Egyptian civilization. The Nile flood, fed by rains in Ethiopia, brought water and black silt to a desert. Yet the flood alone did not feed millions: people built basin walls and canals, measured the flood with nilometers, and planned the farming year around Akhet, Peret and Shemu. Leaders from the south then united the valley around 3100 BCE. Some argue the river did everything, and without the Nile there would be no Kemet. That is true, but other rivers flood too, and not every river valley produced a kingdom that lasted 3,000 years. It took organization, knowledge and cooperation to turn the gift of the river into a civilization."},
   {"t":"open","key":"today","q":"Today the Aswan High Dam (finished in 1970) stops the yearly flood. Predict one benefit and one problem this might cause for farmers, and explain your reasoning.","min":40,"rows":4,"rubric":["A plausible benefit (no destructive floods, water stored for dry years, electricity, year-round irrigation)","A plausible problem (no new silt, need for fertilizer, salt buildup, people displaced)","Reasoning connects to the flood's role"],"model":"One benefit is that farmers can get water all year and no longer fear a destructive flood. One problem is that the silt now stays behind the dam, so fields no longer get new black soil each year, and farmers must buy fertilizer to replace it."}]},
 "exit": [
  {"t":"text","q":"In which direction does the Nile flow?","a":["north","northward","to the north","south to north"],"show":"north","pts":2,"why":"From Central and East Africa north to the Mediterranean."},
  {"t":"blanks","q":"Complete the sentence.","sent":"Upper Egypt is in the ___, and Lower Egypt is in the ___.","blanks":[["south"],["north"]],"pts":2,"why":"Upper means upstream, which is south on the Nile."},
  {"t":"text","q":"What did the ancient Egyptians call their country?","a":["kemet","kmt"],"show":"Kemet","pts":2,"why":"Kemet, the Black Land."},
  {"t":"open","key":"exit_silt","q":"Explain in one or two sentences how the flood made farming possible in a desert.","min":15,"rows":2,"rubric":["Flood brought water","Left fertile silt"],"model":"The flood soaked the fields with water and left a layer of rich black silt, so crops could grow even though almost no rain fell."},
  {"t":"open","key":"exit_unify","q":"Who is believed to have united Egypt around 3100 BCE, and from which part of Egypt did he come?","min":10,"rows":2,"rubric":["Narmer","From Upper Egypt (the south), Hierakonpolis"],"model":"Narmer, a ruler from Upper Egypt in the south, around Hierakonpolis."}],
 "next": "Week 7: Kemet as an African civilization. What the Egyptians said about themselves, what the evidence shows, and why some historians tried to separate Egypt from Africa."
}

TEACHER = {
 "standards": [
  "SS.6.G.2.4: Explain how the geographical location of ancient civilizations contributed to the culture and politics of those societies.",
  "SS.6.G.2.1: Explain how major physical characteristics, natural resources, climate, and absolute and relative locations have influenced settlement, interactions, and the economies of ancient civilizations of the world.",
  "SS.6.W.2.2: Describe how the developments of agriculture and metallurgy related to settlement, population growth, and the emergence of civilization.",
  "SS.6.W.2.4: Compare the economic, political, social, and religious institutions of ancient river civilizations (preview).",
  "C3 Framework D2.Geo.4.6-8: Explain how cultural patterns and economic decisions influence environments and the daily lives of people in both nearby and distant places."],
 "materials": ["The interactive lesson", "A baking pan, sand, dark soil and water", "A clear cup, ruler and marker", "A world map or globe", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Unit 1 Reconnect questions."],
  [6, "Hook", "Show the map. Ask: which way does the Nile flow? Why would the south be called Upper Egypt?"],
  [10, "Sources of the water", "Trace the White and Blue Niles. Stress that the flood began with rain in Ethiopia."],
  [8, "Black Land and Red Land", "Show the cross-section. Introduce Kemet and Deshret and note that Diop's view comes next week."],
  [12, "Managing the flood", "Walk through the three seasons, basin irrigation and the nilometer. Do the cubit calculation together."],
  [12, "Unification", "Discuss the Badarian and Naqada cultures and their ties to Nubia and the Sahara. Examine the crowns and the Narmer Palette as a source."],
  [6, "Assign", "Assign the floodplain model, Think Deeper and the Exit Check."]],
 "key_questions": ["Why is the south called Upper Egypt?", "Where did the floodwater come from?", "What work did people do to turn the flood into food?", "Why might a king want to be shown wearing both crowns?"],
 "misconceptions": ["Thinking Upper Egypt is in the north because it is at the top of the map.", "Believing the flood came from rain in Egypt.", "Picturing Egypt as separate from the rest of Africa.", "Treating the Narmer Palette as an exact news report rather than royal art."],
 "support": ["Give a blank Nile map to label while teaching.", "Use a seasons card with pictures.", "Pair the cubit problem with a ruler: about two hand-spans."],
 "challenge": ["Research how ancient Egyptians used the rising of the star Sirius to predict the flood.", "Compare the Nile with the Mississippi or the Ganges: how does each river's flood affect farming?"],
 "background": "<p>The Nile is about 6,650 km long. The Blue Nile and Atbara supply most of the floodwater and sediment reaching Egypt. The Egyptian civil year had three seasons: Akhet (inundation), Peret (emergence) and Shemu (harvest), with approximate modern months given in the lesson. The cubit used for nilometer readings is the royal cubit, about 52.3 to 52.5 cm. Kmt (Kemet) is attested as a name for Egypt; most Egyptologists relate it to the dark Nile soil, while Cheikh Anta Diop argued it referred to the people; Week 7 examines this debate with evidence. Archaeologists such as Maria Gatto and Stuart Tyson Smith describe close cultural ties between predynastic Upper Egypt, Lower Nubia and the eastern Sahara. Narmer is generally dated to about 3100 BCE; the Narmer Palette, discovered at Hierakonpolis in 1897 to 1898 by James Quibell and Frederick Green, is in the Egyptian Museum in Cairo. Its scenes may record a historical conquest or express the idea of unification symbolically.</p>",
 "sources": ["Egyptian Ministry of Tourism and Antiquities: Narmer Palette.", "Smarthistory / Khan Academy: The Palette of King Narmer.", "Gatto, M. (2014) and Smith, S. T. (2018) on predynastic Egyptian and Nubian cultural connections.", "UNESCO General History of Africa, Volume II: Ancient Civilizations of Africa."]
}

PRINT = {
 "directions": "Use complete sentences and the map.",
 "items": [
  {"q":"Label on a sketch map: the White Nile, the Blue Nile, Khartoum, Aswan, Memphis, the Delta, Upper Egypt and Lower Egypt.","a":"White Nile from Lake Victoria; Blue Nile from Ethiopia; they meet at Khartoum; Aswan at the First Cataract; Memphis near the Delta; Upper Egypt in the south, Lower Egypt in the north.","lines":4},
  {"q":"Explain why the south of Egypt is called Upper Egypt.","a":"The Nile flows north, so the south is upstream, or up the river.","lines":2},
  {"q":"Name the three seasons of the Egyptian year and what farmers did in each.","a":"Akhet: flood, repair tools and build; Peret: plant in the silt; Shemu: harvest and store grain.","lines":3},
  {"q":"A flood reaches 14 cubits. About how many meters is that if a cubit is 52 cm?","a":"14 × 52 = 728 cm, about 7.3 m.","lines":2},
  {"q":"What do the White Crown, the Red Crown and the Double Crown stand for?","a":"White: Upper Egypt; Red: Lower Egypt; Double: the two lands united under one king.","lines":2},
  {"q":"Why did Egyptian farmers in the north depend on rain that fell in Ethiopia?","a":"The monsoon rains in the Ethiopian Highlands fed the Blue Nile, which caused the flood that watered Egypt's fields.","lines":2}]
}
