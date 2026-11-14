INDUS = [(77.5, 34.3), (75.9, 35.1), (74.7, 35.6), (73.6, 35.2), (72.8, 34.4), (72.24, 33.9), (71.6, 33.0), (71.3, 31.8), (70.9, 30.6), (70.6, 29.3), (69.6, 28.4), (68.86, 27.7), (68.4, 26.6), (68.3, 25.4), (67.9, 24.6), (67.6, 24.0)]
RAVI = [(76.0, 32.4), (74.3, 31.6), (73.3, 30.9), (72.4, 30.4), (71.6, 29.9), (71.0, 29.35)]
SUTLEJ = [(77.0, 31.3), (75.6, 31.1), (74.6, 30.6), (73.0, 29.9), (71.0, 29.35)]
HAKRA = [(77.2, 30.6), (75.6, 29.9), (74.2, 29.3), (72.8, 28.8), (71.4, 28.1), (70.3, 27.6)]
SEA = [(62.0, 25.2), (66.5, 25.4), (67.2, 24.8), (67.6, 23.9), (68.4, 23.6), (69.3, 23.0), (70.3, 22.9), (70.1, 22.4), (69.1, 22.3), (69.0, 21.6), (70.0, 20.9), (71.0, 20.7), (72.2, 21.2), (72.6, 21.9), (72.9, 21.0), (72.85, 19.5), (62.0, 19.5)]
KUTCH_RANN = [(68.8, 24.3), (70.8, 24.3), (71.2, 23.7), (70.0, 23.5), (68.9, 23.7)]

def indusmap():
    k = 30.0; lon0, lon1, lat0, lat1 = 64.0, 78.5, 20.0, 35.8; ox = 20
    P = lambda lon, lat: (round((lon - lon0) * k + ox, 1), round((lat1 - lat) * k + 34, 1))
    pl = lambda L: ' '.join('%s,%s' % P(*p) for p in L)
    clip = lambda L: [(max(lon0, min(lon1, a)), max(lat0, min(lat1, b))) for a, b in L]
    mw = (lon1 - lon0) * k; mh = (lat1 - lat0) * k; lx = ox + mw + 16
    W = int(lx + 190); H = int(mh + 58)
    s = (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Map of the Indus Valley civilization">'
         f'<text x="{W/2}" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The Indus Valley civilization (about 2600 to 1900 BCE)</text>'
         f'<rect x="{ox}" y="34" width="{mw}" height="{mh}" fill="#efe1bd"/>'
         f'<polygon points="{pl(clip(SEA))}" fill="#bfe3f5"/><polygon points="{pl(KUTCH_RANN)}" fill="#e6dccb" stroke="#bba" stroke-dasharray="3 2"/>'
         f'<polyline points="{pl(INDUS)}" fill="none" stroke="#0047BA" stroke-width="3" stroke-linejoin="round"/>'
         f'<polyline points="{pl(RAVI)}" fill="none" stroke="#0047BA" stroke-width="2"/><polyline points="{pl(SUTLEJ)}" fill="none" stroke="#0047BA" stroke-width="2"/>'
         f'<polyline points="{pl(HAKRA)}" fill="none" stroke="#0047BA" stroke-width="2" stroke-dasharray="6 4"/>')
    for lon, lat, t, rot in [(69.9, 29.6, "Indus", 62), (74.6, 31.9, "Ravi", 25), (73.0, 28.7, "Ghaggar-Hakra (now mostly dry)", 22)]:
        x, y = P(lon, lat); s += f'<text x="{x}" y="{y}" font-size="11" fill="#0047BA" font-style="italic" transform="rotate({rot} {x} {y})">{t}</text>'
    x, y = P(64.6, 22.4); s += f'<text x="{x}" y="{y}" font-size="12" fill="#0047BA" font-style="italic">Arabian Sea</text>'
    x, y = P(74.8, 34.7); s += f'<text x="{x}" y="{y}" font-size="10" fill="#8a6d1f" font-weight="bold">HIMALAYA</text>'
    x, y = P(71.6, 26.4); s += f'<text x="{x}" y="{y}" font-size="10" fill="#8a6d1f" font-weight="bold">THAR DESERT</text>'
    marks = [(72.86, 30.63, "Harappa"), (76.11, 29.28, "Rakhigarhi"), (68.14, 27.33, "Mohenjo-daro"), (70.21, 23.89, "Dholavira"), (72.25, 22.52, "Lothal")]
    last = -99
    for lon, lat, lab in sorted(marks, key=lambda m: -m[1]):
        x, y = P(lon, lat); ly = max(y, last + 19); last = ly
        s += f'<circle cx="{x}" cy="{y}" r="4" fill="#DB2F30" stroke="#fff"/><path d="M{x+5} {y} L{lx-4} {ly}" stroke="#8a8f99" stroke-width=".8"/><text x="{lx}" y="{ly+4}" font-size="11">{lab}</text>'
    s += (f'<text x="{lx}" y="{H-36}" font-size="10" fill="#5b6676">Today: Pakistan and</text><text x="{lx}" y="{H-24}" font-size="10" fill="#5b6676">northwest India</text>'
          f'<text x="{ox}" y="{H-6}" font-size="10" fill="#5b6676">Rivers simplified. The dashed river is the Ghaggar-Hakra, which once flowed more strongly.</text></svg>')
    return s

CITY = ('<svg viewBox="0 0 640 260" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Plan of a planned Indus city with grid streets and drains">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">A planned city: grid streets, brick houses and covered drains</text>'
  '<rect x="20" y="34" width="420" height="210" fill="#e3c99a"/>'
  + ''.join(f'<rect x="{30+c*104}" y="{44+r*68}" width="90" height="56" fill="#c98f58" stroke="#8a5a33"/><rect x="{40+c*104}" y="{54+r*68}" width="28" height="22" fill="#e9d2a6"/>' for r in range(3) for c in range(4)) +
  ''.join(f'<line x1="20" y1="{105+r*68}" x2="440" y2="{105+r*68}" stroke="#0047BA" stroke-width="3" stroke-dasharray="8 4"/>' for r in range(2)) +
  ''.join(f'<line x1="{127+c*104}" y1="34" x2="{127+c*104}" y2="244" stroke="#0047BA" stroke-width="2" stroke-dasharray="4 4"/>' for c in range(3)) +
  '<rect x="58" y="67" width="10" height="10" fill="#0047BA"/>'
  '<text x="460" y="60" font-weight="bold">Key</text>'
  '<rect x="460" y="72" width="20" height="14" fill="#c98f58" stroke="#8a5a33"/><text x="488" y="84">baked-brick houses</text>'
  '<rect x="460" y="94" width="20" height="14" fill="#e9d2a6"/><text x="488" y="106">courtyard</text>'
  '<line x1="460" y1="124" x2="480" y2="124" stroke="#0047BA" stroke-width="3" stroke-dasharray="8 4"/><text x="488" y="128">covered main drain</text>'
  '<line x1="460" y1="146" x2="480" y2="146" stroke="#0047BA" stroke-width="2" stroke-dasharray="4 4"/><text x="488" y="150">side drain</text>'
  '<rect x="460" y="160" width="10" height="10" fill="#0047BA"/><text x="488" y="170">a private well or bath</text>'
  '<text x="460" y="198" font-size="11" fill="#5b6676">Main streets ran roughly</text><text x="460" y="212" font-size="11" fill="#5b6676">north-south and east-west.</text>'
  '<text x="460" y="232" font-size="11" fill="#5b6676">Simplified drawing.</text></svg>')

SEAL = ('<svg viewBox="0 0 640 214" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Drawing of an Indus seal and standard weights">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Clues from Indus objects</text>'
  '<rect x="60" y="40" width="130" height="130" rx="8" fill="#e8dcc4" stroke="#8a6d1f" stroke-width="3"/>'
  '<g fill="none" stroke="#5a3a1a" stroke-width="2.5"><path d="M88 140 q8 -40 40 -46 q30 -2 34 20 q2 18 -8 26 M100 140 v18 M116 140 v18 M140 140 v18 M152 140 v18"/><path d="M162 108 l14 -22"/><path d="M80 120 q-6 -10 2 -16"/></g>'
  '<g fill="#5a3a1a"><rect x="80" y="54" width="4" height="16"/><path d="M95 54 l8 8 l-8 8z"/><rect x="112" y="54" width="10" height="4"/><rect x="112" y="64" width="10" height="4"/><circle cx="140" cy="62" r="6" fill="none" stroke="#5a3a1a" stroke-width="2"/><path d="M156 54 v16 M152 58 h8"/></g>'
  '<text x="125" y="188" text-anchor="middle" font-weight="bold">A seal: an animal and signs</text>'
  + ''.join(f'<rect x="{300+i*52 - w/2 + 20}" y="{170-w}" width="{w}" height="{w}" rx="3" fill="#b9b2a6" stroke="#5b6676"/><text x="{320+i*52}" y="{186}" text-anchor="middle" font-size="11">{t}</text>' for i, (w, t) in enumerate([(10, "1"), (14, "2"), (18, "4"), (24, "8"), (30, "16"), (38, "32")])) +
  '<text x="460" y="62" text-anchor="middle" font-weight="bold">Stone weights</text><text x="460" y="78" text-anchor="middle" font-size="11">each about double the last:</text><text x="460" y="92" text-anchor="middle" font-size="11">the same sizes in cities</text><text x="460" y="106" text-anchor="middle" font-size="11">hundreds of miles apart</text>'
  '<text x="320" y="208" text-anchor="middle" font-size="10" fill="#5b6676">Simplified drawings; signs shown are invented shapes, not real Indus signs.</text></svg>')

LESSON = {
 "unit": "Unit 3: Ancient Asia",
 "title": "The Indus Valley",
 "subtitle": "On the plains of today's Pakistan and northwest India, people built carefully planned brick cities with drains, wells and public baths, and left behind a script that no one has yet been able to read.",
 "objectives": [
  "Locate the Indus River, its major cities and the modern countries of the region.",
  "Describe the planned cities of the Indus civilization: grid streets, baked bricks, drains and the Great Bath.",
  "Explain how standardized weights, seals and trade connected the Indus Valley to Mesopotamia.",
  "Explain why the Indus script has not been deciphered and what that means for historians.",
  "Evaluate competing explanations for how the Indus cities were governed and why they declined."],
 "vocab": [
  ["Harappan civilization", "Another name for the Indus Valley civilization, after Harappa, the first city excavated."],
  ["urban planning", "Designing a city's layout, streets and services before or while it is built."],
  ["citadel", "A raised, walled area of a city, often holding important buildings."],
  ["standardized", "Made to the same size or rule everywhere."],
  ["seal", "A small carved stone pressed into clay to mark ownership or trade goods."],
  ["decipher", "To figure out the meaning of a writing system or code."],
  ["monsoon", "Seasonal winds that bring heavy summer rains to South Asia."]],
 "reconnect": {
  "title": "Week 11: Mesopotamia",
  "intro": "This week's civilization traded with Mesopotamia. Review first.",
  "items": [
   {"t":"open","key":"rc_writing","q":"Why did writing first develop in Mesopotamia?","min":10,"rows":2,"rubric":["To keep records of goods (grain, beer, sheep) for temples and cities"],"model":"To keep records of goods like grain, beer and sheep that temples collected and gave out."},
   {"t":"text","q":"What is the name of the wedge-shaped writing of Mesopotamia?","a":[{"all":[["cuneiform"]],"none":["not"]}],"show":"cuneiform","pts":2,"why":"Cuneiform. Scholars can read it today. This week's script is still a mystery."},
   {"t":"open","key":"rc_trade","q":"Mesopotamia had plenty of mud and grain but lacked stone, timber and metal. How did Mesopotamians get those goods?","min":10,"rows":2,"rubric":["Trade with distant lands, exchanging grain and cloth"],"model":"They traded their grain and cloth for stone, timber and metal from faraway lands."},
   {"t":"num","q":"In base 60, a scribe writes one 60 and then 2 tens and 3 ones. What number is it?","a":83,"pts":2,"why":"60 + 23 = 83."}]},
 "hook": {
  "title": "A City with Plumbing, 4,500 Years Ago",
  "visual": indusmap(),
  "html": "<p>In the 1920s, archaeologists digging near the Indus River in what is now Pakistan uncovered something astonishing: a city laid out in a grid, built of millions of baked bricks all made to the same proportions, with covered drains running beneath the streets and wells in hundreds of homes. It was about 4,500 years old.</p><p>The city was <b>Mohenjo-daro</b>. Together with <b>Harappa</b> and more than a thousand other sites, it belonged to the <b>Indus Valley civilization</b>, which at its height covered more land than ancient Egypt and Mesopotamia combined.</p><div class='callout'><b>Big question:</b> What can we learn about a civilization whose writing we cannot read?</div>"},
 "learn": [
  {"title": "A River Civilization in South Asia",
   "html": "<p>The Indus River begins in the snowy mountains of Tibet, flows through the Himalaya and crosses the dry plains of Pakistan to the Arabian Sea. Like the Nile, it flooded every summer, when melting snow and <b>monsoon</b> rains swelled it, spreading fertile silt. Farmers grew wheat, barley, peas and cotton. The Indus people may have been among the first in the world to grow cotton and weave cotton cloth.</p><p>The civilization flourished from about 2600 to 1900 BCE, around the same time as Kemet's Old and Middle Kingdoms and Mesopotamia's city-states. Its cities included Harappa and Mohenjo-daro in today's Pakistan and Dholavira, Lothal and Rakhigarhi in today's India. Today, these sites lie in two different countries, and both Pakistan and India are proud of this shared heritage.</p>",
   "checks": [
    {"t":"open","key":"compareriver","q":"How was the Indus River similar to the Nile and the Tigris and Euphrates? Give two similarities.","min":20,"rows":2,"rubric":["Flowed through a dry region; flooded each year; brought water and fertile silt for farming"],"model":"Like the Nile and the Tigris and Euphrates, the Indus flowed through dry land and flooded every year, bringing water and fertile silt that let farmers grow crops."},
    {"t":"text","q":"In which two modern countries are the main Indus Valley sites found?","a":[{"all":[["pakistan"],["india"]]}],"show":"Pakistan and India","pts":2,"why":"Harappa and Mohenjo-daro are in Pakistan; Dholavira, Lothal and Rakhigarhi are in India."},
    {"t":"open","key":"cotton","q":"The Indus people may have been among the first to grow cotton. Why might that matter for trade and daily life?","min":15,"rows":2,"rubric":["Cotton cloth for clothing in a hot climate","A valuable good to trade"],"model":"Cotton makes light, cool cloth for a hot climate, and cotton cloth would have been a valuable good to trade with other peoples."}]},
  {"title": "Planned Cities",
   "visual": CITY,
   "html": "<p>Indus cities show careful <b>urban planning</b>. Main streets ran roughly north-south and east-west in a grid. Houses were built of <b>baked bricks</b> made in standard proportions, about 1 : 2 : 4 (thickness : width : length), in cities hundreds of miles apart.</p><p>Many houses had their own bathing areas and toilets connected to <b>covered drains</b> made of brick that ran along the streets, with openings where workers could clean them. Mohenjo-daro had hundreds of wells. On a raised area called the citadel stood the <b>Great Bath</b>, a waterproof brick pool about 12 meters long, 7 meters wide and almost 2.5 meters deep, sealed with a layer of natural tar. Archaeologists think it may have been used for ritual bathing.</p><p>Many cities in the world did not have covered drains like these until thousands of years later.</p>",
   "checks": [
    {"t":"open","key":"planning","q":"What do grid streets, standard bricks and city-wide drains suggest about how Indus society was organized? Explain your reasoning.","min":30,"rows":3,"rubric":["Someone or some group planned and coordinated building across cities","Shared rules or standards; organized labor; concern for cleanliness and public health"],"model":"They suggest that someone, or some group, planned the cities and made rules that builders followed everywhere. Building drains for a whole city takes organized workers and shared standards, and it shows people cared about cleanliness and health."},
    {"t":"num","q":"An Indus brick follows the ratio 1 : 2 : 4 (thickness : width : length). If a brick is 7 cm thick, how long is it?","a":28,"unit":"cm","pts":2,"why":"Thickness 1 part = 7 cm, so length 4 parts = 28 cm. (You used ratios in Unit 2.)"},
    {"t":"open","key":"bath","q":"The Great Bath was waterproofed with layers of fitted bricks and natural tar. What does this suggest about the builders' knowledge and the importance of the Bath?","min":20,"rows":2,"rubric":["Builders understood waterproofing and engineering","A lot of effort went into it, so it was important (possibly religious or civic use)"],"model":"The builders understood how to keep water from leaking, which takes real engineering skill. Spending so much effort suggests the Bath was important, perhaps for religious ceremonies."}]},
  {"title": "Seals, Weights and a Mystery Script",
   "visual": SEAL,
   "html": "<p>Archaeologists have found thousands of small carved stone <b>seals</b>. Most show an animal, often a unicorn-like bull, along with a short line of signs. Merchants probably pressed seals into clay to mark goods. Indus seals have even been found in Mesopotamian cities such as Ur, and Mesopotamian texts mention trade with a land called <b>Meluhha</b>, which most scholars identify as the Indus region. Indus carnelian beads were prized in Mesopotamia.</p><p>The Indus people also used <b>standardized weights</b> of polished stone. Smaller weights doubled in size (1, 2, 4, 8, 16, 32, 64), and the same weights appear in cities far apart, which made fair trade possible.</p><p>The signs on the seals are the <b>Indus script</b>, with roughly 400 to 600 different signs. No one has deciphered it. Most inscriptions are very short, about five signs, and no \"Rosetta Stone\" with the same text in a known language has been found. So we do not know what language the Indus people spoke or what they called themselves.</p>",
   "checks": [
    {"t":"open","key":"decipher","q":"Give two reasons the Indus script is so hard to decipher.","min":20,"rows":2,"rubric":["Inscriptions are very short (about five signs)","No bilingual text (like the Rosetta Stone); unknown language"],"model":"Most inscriptions have only about five signs, which is too little to find patterns, and no one has found a text that gives the same words in a known language, like the Rosetta Stone did for hieroglyphs."},
    {"t":"blanks","q":"Continue the pattern of Indus weights.","sent":"1, 2, 4, 8, 16, ___, ___","blanks":[["32"],["64"]],"show":"32; 64","pts":2,"why":"Each weight is double the last."},
    {"t":"open","key":"meluhha","q":"What evidence shows that the Indus Valley traded with Mesopotamia? Name two kinds.","min":20,"rows":2,"rubric":["Indus seals found in Mesopotamian cities (Ur)","Mesopotamian texts mention Meluhha; carnelian beads"],"model":"Indus seals have been found in Mesopotamian cities like Ur, and Mesopotamian writings mention trade with Meluhha, which scholars identify as the Indus region."}]},
  {"title": "Questions Historians Still Debate",
   "html": "<p>Because we cannot read the Indus script, historians must rely on archaeology, and some big questions remain open.</p><p><b>Who was in charge?</b> Unlike Egypt and Mesopotamia, Indus cities have no obvious royal palaces, giant tombs or statues of kings, and few weapons have been found. Some scholars think Indus cities were run by councils of merchants or priests, or that power was shared more evenly than in other early civilizations. Others think rulers existed but did not show off in the same way.</p><p><b>Why did the cities decline?</b> After about 1900 BCE, the large cities were slowly abandoned and people moved to smaller villages. Older books claimed invaders destroyed the cities, but archaeologists have found no evidence of a great war. Most now think climate change weakened the monsoon rains and that rivers shifted course or dried up, like the Ghaggar-Hakra on the map, making city life hard to sustain.</p><p>The Indus people did not vanish. Their descendants became part of the populations of South Asia, and some Indus traditions, such as certain farming methods and ornaments, continued.</p>",
   "checks": [
    {"t":"open","key":"rulers","q":"What evidence makes historians unsure who ruled Indus cities? Give your own hypothesis and explain what evidence would test it.","min":35,"rows":4,"rubric":["Evidence: no clear palaces, royal tombs or king statues; few weapons","A reasonable hypothesis (councils, shared power, hidden rulers)","Evidence that could test it (deciphered texts, palace remains, burial differences)"],"model":"Archaeologists have not found clear palaces, royal tombs or statues of kings, and there are few weapons. My hypothesis is that groups of merchants ran the cities together. If the script were deciphered and it named councils instead of kings, that would support my idea."},
    {"t":"open","key":"decline","q":"Compare the old \"invasion\" explanation of the decline with the climate explanation. Which has more support, and why?","min":30,"rows":3,"rubric":["Invasion: no evidence of a great war or destruction","Climate: weaker monsoons and shifting or drying rivers; gradual abandonment fits","The climate explanation has more evidence"],"model":"The invasion idea has little support, because archaeologists have found no signs of a great war. The climate explanation fits the evidence better: monsoon rains weakened and rivers like the Ghaggar-Hakra dried up or shifted, and the cities were abandoned slowly, not destroyed all at once."},
    {"t":"open","key":"unread","q":"Return to the big question: list three things we know about the Indus people without reading their writing, and one thing we cannot know yet.","min":30,"rows":3,"rubric":["Three things known from archaeology (planning, drains, trade, weights, cotton, seals)","One unknown (language, names, beliefs, rulers)"],"model":"We know they planned their cities with grids and drains, traded with Mesopotamia and used standard weights. We do not yet know what language they spoke or what they called themselves."}]}],
 "handson": {
  "title": "Engineer an Indus Drain",
  "intro": "Build a model street with and without a covered drain, and test how well each handles a \"monsoon.\"",
  "materials": ["A shallow baking pan or plastic storage lid", "Sand or soil", "Drinking straws, aluminum foil or a cut-open paper towel tube", "Small blocks, dominoes or LEGO bricks for houses", "A cup or watering can of water", "Towels (do this outdoors or in a sink if you can)"],
  "steps": [
   "Press sand into the pan to make a street with a slight slope. Line one side with block \"houses.\"",
   "Test 1 (no drain): pour a cup of water slowly at the high end, like monsoon rain. Watch where it goes and what happens to the street and houses.",
   "Rebuild. Make a drain channel along the street with foil or a split tube, and cover parts of it with flat blocks or cardboard, the way Indus drains were covered with bricks.",
   "Test 2 (covered drain): pour the same amount of water the same way. Compare.",
   "Clean up the water and sand carefully; wipe spills so no one slips."],
  "record": [
   {"t":"open","key":"draindata","q":"Describe what happened in Test 1 and Test 2. Which variables did you keep the same?","min":30,"rows":4,"rubric":["Clear comparison of both tests","Controlled variables named (amount of water, slope, pouring speed)"],"model":"In Test 1, the water spread across the street, washed sand away and pooled around the houses. In Test 2, most of the water ran into the drain and out the end, and the street stayed in shape. I kept the amount of water, the slope and the pouring speed the same."},
   {"t":"open","key":"drainwhy","q":"Why would covered drains have mattered so much in a crowded Indus city during the monsoon? Think about health, streets and homes.","min":30,"rows":3,"rubric":["Prevented flooding and damage to streets and homes","Kept waste water away from people, reducing disease","Covering kept drains from clogging and kept streets usable"],"model":"Covered drains carried rain and waste water away so streets and homes did not flood or wash away. Keeping dirty water away from people helped prevent disease, and covering the drains kept trash out and let people walk on the streets."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"rivercivs","q":"You have now studied three river civilizations: Kemet, Mesopotamia and the Indus Valley. Write a paragraph comparing them on two features (for example, rivers, writing, cities, government or trade). Use specific evidence for each civilization.","min":120,"rows":10,"rubric":["Two clear features compared","Specific, accurate evidence for all three civilizations","Explains a similarity and a difference","Organized paragraph"],"model":"Kemet, Mesopotamia and the Indus Valley all depended on rivers, but they organized their societies differently. All three grew along rivers that flooded and brought fertile silt, though the Nile was predictable while the Tigris and Euphrates were not, and the Indus floods came with the monsoon. Their governments also differed. Kemet was united under a powerful pharaoh who built pyramids, and Mesopotamian city-states had kings like Hammurabi who wrote laws. In the Indus Valley, however, archaeologists have found no royal palaces or tombs, so power may have been shared differently. These differences show that people solved similar problems in different ways."},
   {"t":"open","key":"heritage","q":"Harappa and Mohenjo-daro are in Pakistan, while Dholavira and Lothal are in India. Why might it matter that people in both countries see the Indus civilization as part of their heritage?","min":50,"rows":4,"rubric":["Shared history connects people across a modern border","Thoughtful reasoning about heritage, identity, cooperation or preservation"],"model":"Pakistan and India have often been in conflict, but the Indus civilization is older than both countries and belongs to the history of people on both sides of the border. Seeing it as shared heritage can remind people of their common past and encourage them to work together to protect these sites."}]},
 "exit": [
  {"t":"text","q":"Name one of the two largest and best-known Indus cities.","a":[{"all":[["harappa","mohenjo","mohenjodaro"]],"none":["not"]}],"show":"Harappa or Mohenjo-daro","pts":2,"why":"Harappa and Mohenjo-daro."},
  {"t":"open","key":"exit_plan","q":"Name two features that show Indus cities were carefully planned.","min":10,"rows":2,"rubric":["Grid streets; standard bricks; covered drains; wells; the Great Bath"],"model":"Grid streets and covered drains along the streets."},
  {"t":"open","key":"exit_script","q":"Why can't historians read the Indus script?","min":10,"rows":2,"rubric":["Short inscriptions; no bilingual text; unknown language"],"model":"The inscriptions are very short, and no text has been found that gives the same words in a known language."},
  {"t":"open","key":"exit_decline","q":"What do most archaeologists now think caused the Indus cities to decline?","min":10,"rows":2,"rubric":["Climate change: weaker monsoon rains; rivers shifting or drying up"],"model":"Climate change weakened the monsoon rains and rivers shifted or dried up, so the cities were slowly abandoned."}],
 "next": "Week 13: ancient China, its dynasties, the Mandate of Heaven and the ideas of Confucius."
}

TEACHER = {
 "standards": [
  "SS.6.W.2.4: Compare the economic, political, social, and religious institutions of ancient river civilizations.",
  "SS.6.W.2.3: Identify the characteristics of civilization.",
  "SS.6.G.2.1: Explain how major physical characteristics, natural resources, climate, and absolute and relative locations have influenced settlement, interactions, and the economies of ancient civilizations of the world.",
  "SS.6.G.2.6: Explain the concept of cultural diffusion, and identify the influences of different ancient cultures on one another.",
  "SS.6.W.1.4: Describe the methods of historical inquiry and how history relates to the other social sciences."],
 "materials": ["The interactive lesson", "A world map or globe", "A baking pan, sand, straws or foil, small blocks, water, towels", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 11 Reconnect questions."],
  [5, "Hook", "Show the map. Find Pakistan and India on a globe. Describe the 1920s discovery."],
  [8, "River civilization", "Compare the Indus with the Nile and the Tigris and Euphrates."],
  [12, "Planned cities", "Study the city plan. Discuss what planning reveals. Work the brick ratio."],
  [10, "Seals, weights and script", "Look at the seal and weights. Discuss why the script is unread."],
  [12, "Debates", "Weigh the evidence on rulers and decline. Write a hypothesis."],
  [7, "Assign", "Start the drain model together; assign the tests, Think Deeper and the Exit Check."]],
 "key_questions": ["What can objects tell us when we cannot read the writing?", "What does planning reveal about a society?", "What evidence supports each explanation?", "What would change our minds?"],
 "misconceptions": ["The Indus civilization was part of Mesopotamia or Egypt.", "Invaders destroyed the Indus cities (little evidence).", "Ancient people did not have plumbing or planning.", "The Indus script has been deciphered."],
 "support": ["Provide a labeled map with modern borders.", "Use a three-column chart: Kemet, Mesopotamia, Indus.", "Pre-build the drain model base."],
 "challenge": ["Research recent efforts to decipher the Indus script, including computer analysis, and evaluate one claim.", "Compare Mohenjo-daro's drains with how your town handles stormwater today."],
 "background": "<p>The Mature Harappan phase dates to about 2600 to 1900 BCE (broader Indus tradition about 3300 to 1300 BCE). Harappa was first excavated by Daya Ram Sahni (1921) and Mohenjo-daro by R. D. Banerji (1922); John Marshall announced the civilization in 1924. Over 1,000 sites are known; the area exceeds that of Egypt and Mesopotamia combined. Bricks follow roughly 1 : 2 : 4 proportions. The Great Bath measures about 12 by 7 m and 2.4 m deep, sealed with bitumen. Weights follow a binary series for smaller units, then decimal multiples. The script has roughly 400 to 600 signs; average inscription length is about five signs. Meluhha appears in Mesopotamian texts from the Akkadian period; Indus seals and carnelian beads are found in Mesopotamia. Decline after about 1900 BCE is now attributed mainly to climate change (weaker monsoons) and river shifts; the older Aryan invasion explanation (Mortimer Wheeler) is not supported by the archaeological evidence.</p>",
 "sources": ["Kenoyer, J. M. (1998), Ancient Cities of the Indus Valley Civilization, Oxford University Press.", "Harappa.com (J. M. Kenoyer and colleagues), Indus Valley archaeology.", "Metropolitan Museum of Art, Heilbrunn Timeline: Indus Valley Civilization.", "Giosan, L. et al. (2012), Fluvial landscapes of the Harappan civilization, PNAS 109."]
}

PRINT = {
 "directions": "Use complete sentences and evidence.",
 "items": [
  {"q":"Where was the Indus Valley civilization, and which modern countries are there today?","a":"Along the Indus River in South Asia; today Pakistan and northwest India.","lines":2},
  {"q":"Describe two features of Indus city planning.","a":"Grid streets; standard baked bricks; covered drains; wells; the Great Bath.","lines":2},
  {"q":"How do we know the Indus Valley traded with Mesopotamia?","a":"Indus seals found in Ur; Mesopotamian texts mention Meluhha; carnelian beads.","lines":2},
  {"q":"Why hasn't the Indus script been deciphered?","a":"Very short inscriptions; no bilingual text; unknown language.","lines":2},
  {"q":"What do historians debate about Indus government?","a":"No clear palaces, royal tombs or king statues, so they are unsure who ruled.","lines":2},
  {"q":"Explain the leading theory for the decline of the Indus cities.","a":"Climate change weakened monsoons and rivers shifted or dried up; no evidence of a great invasion.","lines":2}]
}
