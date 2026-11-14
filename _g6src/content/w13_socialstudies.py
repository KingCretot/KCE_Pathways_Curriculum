HUANG = [(96.0, 35.5), (99.5, 36.0), (102.5, 36.5), (103.8, 36.1), (105.2, 37.4), (106.5, 39.3), (107.5, 40.8), (109.5, 40.6), (111.0, 40.2), (111.3, 38.5), (110.4, 36.0), (110.3, 34.6), (112.5, 34.7), (114.3, 34.9), (116.0, 35.6), (117.5, 36.8), (118.9, 37.7)]
YANGTZE = [(95.0, 33.5), (98.5, 32.0), (100.0, 28.5), (102.0, 26.5), (103.5, 28.6), (104.6, 28.8), (106.5, 29.6), (108.5, 30.8), (111.3, 30.7), (112.5, 30.0), (114.3, 30.6), (116.0, 29.8), (117.3, 30.5), (118.8, 32.0), (120.5, 31.8), (121.8, 31.4)]
COAST = [(118.9, 37.7), (119.8, 37.2), (121.0, 37.8), (122.5, 37.4), (120.6, 36.1), (119.3, 35.0), (120.3, 34.3), (120.9, 32.6), (121.8, 31.4), (121.9, 30.5), (121.0, 28.4), (119.8, 26.4), (118.0, 24.5), (116.0, 22.9), (113.5, 22.2), (110.5, 21.2)]
WALL = [(98.3, 39.8), (100.4, 38.9), (102.6, 37.9), (104.1, 37.4), (105.2, 37.6), (106.2, 38.4), (107.4, 37.8), (108.8, 37.6), (109.7, 38.3), (110.5, 38.8), (111.1, 39.0), (111.5, 39.4), (113.3, 40.3), (114.9, 40.8), (116.0, 40.4), (117.2, 40.6), (118.3, 40.4), (119.8, 40.0)]

def chinamap():
    k = 22.0; lon0, lon1, lat0, lat1 = 94.0, 124.0, 20.0, 43.0; ox = 20
    P = lambda lon, lat: (round((lon - lon0) * k + ox, 1), round((lat1 - lat) * k + 34, 1))
    pl = lambda L: ' '.join('%s,%s' % P(*p) for p in L)
    mw = (lon1 - lon0) * k; mh = (lat1 - lat0) * k; lx = ox + mw + 16
    W = int(lx + 235); H = int(mh + 56)
    sea = COAST + [(110.5, 20.0), (124.0, 20.0), (124.0, 39.9), (122.3, 39.4), (121.2, 38.8), (121.9, 39.6), (122.2, 40.5), (121.8, 40.9), (121.0, 40.8), (119.6, 39.9), (118.5, 39.1), (117.7, 38.9), (117.9, 38.2), (118.9, 37.7)]
    s = (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Map of ancient China with the Yellow and Yangtze rivers">'
         f'<text x="{W/2}" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Ancient China: two great rivers</text>'
         f'<rect x="{ox}" y="34" width="{mw}" height="{mh}" fill="#efe1bd"/><polygon points="{pl(sea)}" fill="#bfe3f5"/>'
         f'<polyline points="{pl(HUANG)}" fill="none" stroke="#C9A84C" stroke-width="3.5" stroke-linejoin="round"/>'
         f'<polyline points="{pl(YANGTZE)}" fill="none" stroke="#0047BA" stroke-width="3" stroke-linejoin="round"/>'
         f'<polyline points="{pl(WALL)}" fill="none" stroke="#DB2F30" stroke-width="2.5" stroke-dasharray="7 3"/>')
    for lon, lat, t, c in [(96.3, 34.9, "Yellow River (Huang He)", "#8a6d1f"), (101.5, 30.6, "Yangtze (Chang Jiang)", "#0047BA"), (100.6, 40.4, "Great Wall (Ming line, later)", "#DB2F30")]:
        x, y = P(lon, lat); s += f'<text x="{x}" y="{y}" font-size="11" fill="{c}" font-style="italic" style="paint-order:stroke;stroke:#efe1bd;stroke-width:3">{t}</text>'
    for lon, lat, t in [(94.4, 28.0, "TIBETAN PLATEAU"), (104.0, 41.8, "GOBI DESERT")]:
        x, y = P(lon, lat); s += f'<text x="{x}" y="{y}" font-size="10" fill="#8a6d1f" font-weight="bold">{t}</text>'
    x, y = P(122.2, 27.0); s += f'<text x="{x}" y="{y}" font-size="11" fill="#0047BA" font-style="italic">Pacific</text>'
    marks = [(116.4, 39.9, "Beijing (modern capital)"), (114.3, 36.1, "Anyang (Shang capital)"), (108.9, 34.3, "Xi'an (Qin and Han capital; tomb nearby)"), (116.98, 35.6, "Qufu (Confucius's hometown)")]
    last = -99
    for lon, lat, lab in sorted(marks, key=lambda m: -m[1]):
        x, y = P(lon, lat); ly = max(y, last + 19); last = ly
        fill = "#fff" if "modern" in lab else "#0A1F3D"
        s += f'<circle cx="{x}" cy="{y}" r="4" fill="{fill}" stroke="#0A1F3D" stroke-width="1.5"/><path d="M{x+5} {y} L{lx-4} {ly}" stroke="#8a8f99" stroke-width=".8"/><text x="{lx}" y="{ly+4}" font-size="11">{lab}</text>'
    s += f'<text x="{ox}" y="{H-6}" font-size="10" fill="#5b6676">Rivers and coast simplified. Open circle: modern city. The wall line shown is the later Ming wall; Qin walls lay farther north.</text></svg>'
    return s

CYCLE = ('<svg viewBox="0 0 640 260" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="The dynastic cycle and the Mandate of Heaven">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The dynastic cycle and the Mandate of Heaven</text>'
  '<defs><marker id="dc" viewBox="0 0 10 10" markerWidth="5" markerHeight="5" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="#0A1F3D"/></marker></defs>'
  + ''.join(f'<rect x="{x-85}" y="{y-24}" width="170" height="48" rx="10" fill="{c}"/><text x="{x}" y="{y-4}" text-anchor="middle" fill="#fff" font-weight="bold">{t1}</text><text x="{x}" y="{y+12}" text-anchor="middle" fill="#fff" font-size="11">{t2}</text>'
            for x, y, c, t1, t2 in [(320, 64, "#3d9a2f", "1. A new dynasty rises", "claims the Mandate of Heaven"),
                                    (520, 140, "#0047BA", "2. Peace and prosperity", "roads, canals, harvests"),
                                    (320, 220, "#C9A84C", "3. Decline", "corruption, high taxes, disasters"),
                                    (120, 140, "#DB2F30", "4. Rebellion", "people say the Mandate is lost")]) +
  '<path d="M410 76 Q500 90 520 112" stroke="#0A1F3D" stroke-width="2" fill="none" marker-end="url(#dc)"/>'
  '<path d="M520 168 Q500 205 410 214" stroke="#0A1F3D" stroke-width="2" fill="none" marker-end="url(#dc)"/>'
  '<path d="M230 214 Q140 205 120 168" stroke="#0A1F3D" stroke-width="2" fill="none" marker-end="url(#dc)"/>'
  '<path d="M120 112 Q140 90 230 76" stroke="#0A1F3D" stroke-width="2" fill="none" marker-end="url(#dc)"/>'
  '<text x="320" y="146" text-anchor="middle" font-size="11" fill="#5b6676">Heaven grants the right to rule</text><text x="320" y="160" text-anchor="middle" font-size="11" fill="#5b6676">only to a just ruler.</text></svg>')

CHARS = ('<svg viewBox="0 0 640 190" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="How some Chinese characters began as pictures">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Some Chinese characters began as pictures</text>'
  + ''.join(f'<g transform="translate({40+i*150},0)">{pic}<text x="55" y="132" text-anchor="middle" font-size="40" fill="#0A1F3D">{ch}</text><text x="55" y="160" text-anchor="middle" font-weight="bold">{en}</text><text x="55" y="176" text-anchor="middle" font-size="11" fill="#5b6676">{py}</text></g>'
            for i, (pic, ch, en, py) in enumerate([
              ('<circle cx="55" cy="60" r="22" fill="none" stroke="#C9A84C" stroke-width="3"/><circle cx="55" cy="60" r="3" fill="#C9A84C"/>', '日', 'sun', 'rì'),
              ('<path d="M62 36 A24 24 0 0 0 62 84 A30 30 0 0 1 62 36 Z" fill="#0047BA"/>', '月', 'moon', 'yuè'),
              ('<path d="M20 82 l20 -36 l15 22 l15 -30 l20 44z" fill="none" stroke="#3d9a2f" stroke-width="3"/>', '山', 'mountain', 'shān'),
              ('<path d="M55 36 v50 M55 50 l-22 -12 M55 50 l22 -12 M55 86 l-22 10 M55 86 l22 10" stroke="#8a5a33" stroke-width="3" fill="none"/>', '木', 'tree, wood', 'mù')])) +
  '</svg>')

LESSON = {
 "unit": "Unit 3: Ancient Asia",
 "title": "Ancient China: Dynasties and Ideas",
 "subtitle": "Along the Yellow and Yangtze rivers, Chinese dynasties rose and fell for thousands of years, guided by the idea of the Mandate of Heaven and by thinkers like Confucius whose ideas still shape East Asia today.",
 "objectives": [
  "Locate the Yellow and Yangtze rivers and explain how geography shaped and protected early China.",
  "Describe the Shang dynasty's oracle bones and the beginnings of Chinese writing.",
  "Explain the Mandate of Heaven and the dynastic cycle.",
  "Compare Confucianism, Daoism and Legalism, using primary sources.",
  "Evaluate the achievements and costs of the Qin and Han dynasties."],
 "vocab": [
  ["dynasty", "A series of rulers from the same family."],
  ["oracle bone", "A bone or turtle shell carved with questions to the ancestors, then cracked with heat to read an answer."],
  ["Mandate of Heaven", "The Chinese belief that Heaven gives a just ruler the right to rule and takes it away from an unjust one."],
  ["dynastic cycle", "The pattern of dynasties rising, flourishing, declining and being replaced."],
  ["Confucianism", "Teachings of Confucius about good behavior, respect, family duty and wise government."],
  ["Daoism", "Teachings, linked to Laozi, about living in harmony with nature and the Dao (the Way)."],
  ["Legalism", "Teachings, best known from Han Feizi, that strict laws and harsh punishments are needed to keep order."],
  ["civil service", "Government jobs filled by trained officials; in Han China, often chosen for learning and merit."]],
 "reconnect": {
  "title": "Week 12: The Indus Valley",
  "intro": "China is the fourth of the great early river civilizations. Review the third.",
  "items": [
   {"t":"blanks","q":"Recall how Indus cities were planned.","sent":"Streets were laid out in a ___ pattern, and covered brick ___ carried wastewater away under the streets.","blanks":[["grid","grid pattern","checkerboard"],["drains","drain","sewers","sewer"]],"show":"grid; drains","pts":2,"why":"Grid streets and covered drains show city-wide planning."},
   {"t":"open","key":"rc_script","q":"Why can't historians read the Indus script yet?","min":10,"rows":2,"rubric":["Very short inscriptions; no bilingual text; unknown language"],"model":"The inscriptions are very short, and no text gives the same words in a known language."},
   {"t":"blanks","q":"Complete the pattern of Indus weights.","sent":"1, 2, 4, 8, ___","blanks":[["16","sixteen"]],"show":"16","pts":2,"why":"Each weight doubles."},
   {"t":"blanks","q":"Name the rivers of the three river civilizations you have studied.","sent":"Kemet: the ___ &nbsp; Mesopotamia: the Tigris and the ___ &nbsp; Harappa and Mohenjo-daro: the ___","blanks":[[{"all":[["nile"]],"none":["not"]}],[{"all":[["euphrates"]],"none":["not"]}],[{"all":[["indus"]],"none":["not"]}]],"show":"Nile; Euphrates; Indus","pts":3,"why":"Kemet grew on the Nile, Mesopotamia between the Tigris and Euphrates, and the Indus cities on the Indus."}]},
 "hook": {
  "title": "Questions Carved in Bone",
  "visual": chinamap(),
  "html": "<p>Over 3,000 years ago, a king of the Shang dynasty wanted to know: Will the harvest be good? Will the queen's child be born safely? Should we go to war? A priest carved the question onto the flat underside of a turtle shell or the shoulder bone of an ox. Then he pressed a hot metal rod into a hollow in the bone until it cracked. The shape of the cracks was read as the ancestors' answer, and sometimes the result was carved beside it.</p><p>These <b>oracle bones</b>, buried for thousands of years near the city of Anyang, were rediscovered around 1899. Their carvings are the oldest known Chinese writing, and many of the characters are ancestors of characters that millions of people still read today.</p><div class='callout'><b>Big question:</b> What ideas held China together across thousands of years of changing dynasties?</div>"},
 "learn": [
  {"title": "Rivers, Mountains and Deserts",
   "html": "<p>Chinese civilization grew along two great rivers. The <b>Yellow River</b> (Huang He) in the north carries so much fine yellow soil, called loess, that it colors the water. That soil made farmland rich, but the river also flooded so destructively that it earned the name \"China's Sorrow.\" To the south, the <b>Yangtze</b> (Chang Jiang), one of the longest rivers in the world, watered rice fields.</p><p>China was ringed by natural barriers: the Himalaya and the Tibetan Plateau to the west, the Gobi Desert to the north, thick forests and mountains to the south, and the Pacific Ocean to the east. These barriers protected China and kept it somewhat separate, so Chinese culture developed in its own way, while the open northern plains made it vulnerable to horse-riding peoples from the steppes.</p>",
   "checks": [
    {"t":"open","key":"sorrow","q":"Why was the Yellow River called both a gift and \"China's Sorrow\"?","min":20,"rows":2,"rubric":["Gift: fertile loess soil for farming","Sorrow: destructive floods that killed people and destroyed fields"],"model":"Its fertile yellow soil made the farmland rich, but its floods were so destructive that they killed many people and wiped out fields, so it brought both life and sorrow."},
    {"t":"open","key":"barriers","q":"How did China's natural barriers both help and limit it?","min":20,"rows":2,"rubric":["Helped: protection from invasion; independent culture","Limited: less contact and trade with other civilizations; northern plains still open to steppe peoples"],"model":"Mountains, deserts and the ocean protected China and let its culture develop independently, but they also limited contact and trade with other civilizations, and the northern plains were still open to raiders."},
    {"t":"text","q":"What is the name of the fine yellow soil carried by the Yellow River?","a":[{"all":[["loess","loes"]],"none":["not"]}],"show":"loess","pts":2,"why":"Loess, wind-blown silt that colors the river."}]},
  {"title": "The Shang and the Zhou: Writing and the Mandate of Heaven",
   "visual": CYCLE,
   "html": "<p>The <b>Shang dynasty</b> (about 1600 to 1046 BCE) ruled the Yellow River valley. Shang kings led armies with bronze weapons and chariots, and Shang craftworkers cast magnificent bronze vessels for ceremonies honoring ancestors. Their writing on oracle bones includes about 4,000 different characters.</p><p>Around 1046 BCE, the <b>Zhou</b> overthrew the Shang. To explain why, the Zhou said that Heaven had given them the <b>Mandate of Heaven</b>, the right to rule, because the last Shang king was cruel and unjust. If a ruler governed badly, Heaven could take the Mandate away. Floods, famines and rebellions were seen as signs that a dynasty had lost it.</p><p>This idea created the <b>dynastic cycle</b>: a new dynasty rises, brings peace, slowly declines, faces rebellion and is replaced by a new dynasty that claims the Mandate. China would see this cycle repeat for more than 3,000 years.</p>",
   "checks": [
    {"t":"open","key":"mandate","q":"Explain the Mandate of Heaven in your own words. How could it be used both to support a ruler and to justify overthrowing one?","min":30,"rows":3,"rubric":["Heaven gives a just ruler the right to rule","Supports a good ruler; a disaster or bad rule could be taken as proof the Mandate was lost, justifying rebellion"],"model":"The Mandate of Heaven means Heaven gives the right to rule only to a just ruler. A good king could point to peace and good harvests as proof he had it. But floods, famine or cruelty could be taken as signs he had lost it, so rebels could say they had the right to overthrow him."},
    {"t":"open","key":"modern","q":"Is there any idea in your own country's government that is similar to the Mandate of Heaven, the idea that leaders must govern well or lose their right to lead? Explain.","min":25,"rows":3,"rubric":["A reasonable comparison (elections, impeachment, the Declaration of Independence's idea that governments get power from the people)","Notes a difference (Heaven versus the people)"],"model":"In the United States, leaders can be voted out or impeached if they govern badly, and the Declaration of Independence says governments get their power from the people. The difference is that the Mandate came from Heaven, while American leaders get power from voters."}]},
  {"title": "Three Ways to Bring Order: Confucius, Laozi and the Legalists",
   "html": "<p>From 770 BCE the Zhou kings slowly lost control, and from about 475 to 221 BCE, in the Warring States period, rival states fought each other. In this troubled time, thinkers asked: How can we bring back peace and order?</p><p><b>Confucius</b> (Kongzi, 551 to 479 BCE) taught that society would be peaceful if everyone behaved rightly in their relationships: rulers and subjects, parents and children, older and younger siblings, husbands and wives, and friends. Rulers should lead by good example, and children should respect their parents (<b>filial piety</b>). His students recorded his sayings in the <i>Analects</i>.</p><div class='card'><b>From the Analects</b> (translated by James Legge, 1861; spelling Americanized)<br>\"What you do not want done to yourself, do not do to others.\" (Book 15)<br>\"Learning without thought is labor lost; thought without learning is perilous.\" (Book 2)</div><p><b>Daoism</b>, linked to the teacher <b>Laozi</b>, taught that people should live simply and in harmony with nature and the <i>Dao</i>, or Way, instead of struggling for power.</p><div class='card'><b>From the Dao De Jing</b> (translated by James Legge, 1891), chapter 8<br>\"The highest excellence is like (that of) water. The excellence of water appears in its benefiting all things, and in its occupying, without striving (to the contrary), the low place which all men dislike.\"</div><p>The <b>Legalists</b>, whose best-known writer was <b>Han Feizi</b> (Han Fei Zi, died 233 BCE), disagreed with both: they believed people are naturally selfish, so a ruler needs strict laws, harsh punishments and rewards to keep order.</p>",
   "checks": [
    {"t":"open","key":"golden","q":"Explain Confucius's saying, \"What you do not want done to yourself, do not do to others,\" and give an example from daily life. Does it remind you of a rule from another culture or religion?","min":30,"rows":3,"rubric":["Meaning: treat others as you would want to be treated (avoid harming others)","A daily-life example","A connection (the Golden Rule in many traditions)"],"model":"It means you should not treat people in a way you would not want to be treated. If I would not want someone to laugh at my mistake, I should not laugh at theirs. It reminds me of the Golden Rule found in many religions and cultures."},
    {"t":"open","key":"learning","q":"\"Learning without thought is labor lost; thought without learning is perilous.\" What do you think Confucius meant? Use an example from school.","min":25,"rows":3,"rubric":["Memorizing without thinking is wasted effort","Having opinions without knowledge is dangerous","A school example"],"model":"He meant that memorizing facts without thinking about them is wasted effort, but forming opinions without learning facts is dangerous. For example, memorizing the steps for dividing fractions without understanding them doesn't help me solve new problems, but guessing an answer without learning the method leads to mistakes."},
    {"t":"blanks","q":"Match each belief to its school of thought: Confucianism, Daoism or Legalism.","sent":"Strict laws and harsh punishments keep order: ___. Live simply in harmony with nature and the Way: ___. Respect your parents and lead by good example: ___.","blanks":[[{"all":[["legal"]],"none":["not"]}],[{"all":[["dao","tao"]],"none":["not"]}],[{"all":[["confuci"]],"none":["not"]}]],"show":"Legalism; Daoism; Confucianism","pts":3,"why":"Legalism: laws and punishment. Daoism: harmony with nature. Confucianism: relationships, respect and example."}]},
  {"title": "Qin and Han: Unity at a Cost",
   "visual": CHARS,
   "html": "<p>In 221 BCE, the ruler of the Qin state conquered his rivals and named himself <b>Qin Shi Huang</b>, \"First Emperor of Qin.\" (The name China may come from Qin.) Using Legalist ideas, he standardized writing, weights, measures, coins and even the width of cart axles so goods could move across the empire. He linked earlier walls into a long northern defense, the start of the Great Wall. (Most of the stone wall visitors see today was built much later, by the Ming dynasty, 1368 to 1644 CE.) But he ruled harshly: hundreds of thousands of people were forced to labor on walls, roads and his tomb, and books that disagreed with Legalism were burned.</p><p>Near his tomb, outside today's Xi'an, farmers digging a well in 1974 found the <b>Terracotta Army</b>: thousands of life-size clay soldiers, each with its own face, buried to guard the emperor after death.</p><p>Rebellions broke out soon after the First Emperor died in 210 BCE, and the Qin dynasty collapsed. The <b>Han dynasty</b> (206 BCE to 220 CE) kept Qin's unity but made Confucianism the official philosophy. Han officials were increasingly chosen for their learning, the beginning of China's civil service. The Han era brought papermaking (paper is recorded by about 105 CE, though earlier paper has been found), an earthquake detector (Zhang Heng's seismoscope) and advances in medicine, and the Han began the trade routes you will study next week, the Silk Road.</p>",
   "checks": [
    {"t":"open","key":"standard","q":"Qin Shi Huang standardized writing, money, weights and cart axles. Choose two and explain how each helped unite the empire.","min":30,"rows":3,"rubric":["Writing: officials across regions could read the same documents","Money, weights or axles: easier trade, fair exchange, carts fit the same road ruts"],"model":"A single writing system meant officials everywhere could read the same laws and orders. Standard coins and weights made trade fair and simple across the empire, because a coin or a pound meant the same thing everywhere."},
    {"t":"blanks","q":"Use the dynastic cycle diagram from the Shang and Zhou section. Write the stage number (1 to 4) for each event in Qin history.","sent":"Forced labor, harsh punishments and book burning turn people against the Qin: stage ___. Qin Shi Huang conquers his rivals and unites China: stage ___. Rebellions break out after the First Emperor dies: stage ___. Standard coins, weights and roads help goods move across the empire: stage ___.","blanks":[["3","three"],["1","one"],["4","four"],["2","two"]],"show":"3; 1; 4; 2","pts":3,"why":"Rise (unification), prosperity (standards and roads), decline (cruelty), rebellion. Then the Han claimed the Mandate and the cycle began again."},
    {"t":"open","key":"cost","q":"Was the Qin dynasty's unity worth its cost? Give one achievement and one cost, then state your opinion with a reason.","min":35,"rows":3,"rubric":["Achievement (unification, standardization, Great Wall, roads)","Cost (forced labor, harsh punishments, book burning, short dynasty)","A reasoned opinion"],"model":"Qin united China and standardized writing and money, which lasted for centuries. But it forced hundreds of thousands of people to labor and burned books it disagreed with. I think the unity was important, but it did not have to be so cruel; the Han showed that unity could last with fairer rule."},
    {"t":"text","q":"Which dynasty made Confucianism the official philosophy and began choosing officials for their learning?","a":[{"all":[["han"]],"none":["not","qin","shang","zhou","fei","hanfei"]}],"show":"the Han dynasty","pts":2,"why":"The Han (206 BCE to 220 CE)."}]}],
 "handson": {
  "title": "Brush Writing: Characters That Began as Pictures",
  "intro": "Try brush writing the way Chinese students have for centuries, and see how some characters grew from pictures. Only a small share of Chinese characters began as pictures; most combine a part that hints at meaning with a part that hints at sound.",
  "materials": ["A soft paintbrush (a watercolor brush works)", "A cup of water (or washable black paint thinned with water)", "Newspaper, brown paper bags or paper towels to write on", "Paper and pencil", "Optional: a printed character chart or a free online stroke-order guide"],
  "steps": [
   "Study the four characters in the diagram: sun (日), moon (月), mountain (山) and tree (木). Notice how each began as a picture.",
   "With water or thinned paint, practice each character five times with the brush, holding the brush upright. Chinese characters follow a stroke order, usually top to bottom and left to right. Cover the table, rinse the brush in a separate cup, and never drink the rinse water; keep paint away from pets.",
   "Two characters can combine to make new meanings. 日 (sun) + 月 (moon) = 明 (bright). 木 + 木 = 林 (grove of trees). Write both and guess why they mean what they do.",
   "Invent your own picture-character for something in your home, then show how it might become simpler over time, the way 日 changed from a circle to a box."],
  "record": [
   {"t":"open","key":"brushrec","q":"Which character was hardest to write with a brush, and why? How did the brush change the way you wrote compared with a pencil?","min":30,"rows":3,"rubric":["Names a character and a real difficulty","Compares brush and pencil (thick and thin strokes, pressure, slower, more careful)"],"model":"木 was hardest because the two slanting strokes kept turning into blobs. The brush makes lines thick or thin depending on how hard I press, so I had to slow down and be much more careful than with a pencil."},
   {"t":"open","key":"mychar","q":"Describe or draw your invented character, its meaning, and how it became simpler. Why do you think writing systems simplify pictures over time?","min":30,"rows":3,"rubric":["Describes an invented character and its simplification","Reasonable explanation (faster to write, easier to learn, fits the writing tool)"],"model":"I drew a cup with steam lines for \"coffee,\" then simplified it to a square with two short lines. Writing systems simplify pictures because simple shapes are faster to write and fit the tools, like brushes or carving."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"debate","q":"Imagine you are an adviser to a new emperor after years of war. Write a speech recommending Confucianism, Daoism or Legalism as the way to rule. Explain why your choice will bring peace and respond to one argument from another school.","min":120,"rows":10,"rubric":["Clear recommendation","Accurate description of the chosen school's ideas","Reasons it would bring peace","Responds to a rival school's argument","Persuasive organization"],"model":"Your Majesty, after so many years of war, I recommend you rule by the teachings of Confucius. If you lead by good example, treat your people fairly and choose officials for their learning and honesty, your people will respect you instead of fearing you. Families that honor their parents will raise children who respect the law. A Legalist adviser would say that people are selfish and only harsh punishment keeps order. But the Qin used harsh laws, and their dynasty fell within years of the First Emperor's death. Respect lasts longer than fear. Rule with virtue, and you will keep the Mandate of Heaven."},
   {"t":"open","key":"fourcivs","q":"Compare ancient China with one other river civilization you have studied (Kemet, Mesopotamia or the Indus Valley). Give one similarity and two differences.","min":70,"rows":6,"rubric":["Accurate similarity (rivers, early writing, bronze, kings, irrigation)","Two accurate differences (writing still readable vs. Indus; Mandate of Heaven vs. divine pharaoh; natural barriers; philosophy)","Specific evidence"],"model":"Like Mesopotamia, China grew along rivers that flooded dangerously, and both developed writing early. But Chinese writing has continued in a direct line to today, while cuneiform stopped being used about 2,000 years ago. Also, China's rulers claimed the Mandate of Heaven, which could be lost if they ruled badly, while Mesopotamian kings relied on written law codes like Hammurabi's."}]},
 "exit": [
  {"t":"text","q":"What are the two great rivers of ancient China? (Use either their English or Chinese names.)","a":[{"all":[["yellow","huang"],["yangtze","chang jiang","changjiang","yangzi"]],"none":["not"]}],"show":"the Yellow River and the Yangtze","pts":2,"why":"The Yellow River (Huang He) and the Yangtze (Chang Jiang)."},
  {"t":"text","q":"A dynasty's rivers flood three years in a row, crops fail and officials take bribes. Rebels say Heaven is on their side. According to the Mandate of Heaven, what do many people believe has happened to the emperor's right to rule?","a":[{"all":[["lost","lose","losing","taken","withdrawn","gone","removed"]],"none":["not lost","kept","still has"]}],"show":"He has lost the Mandate of Heaven.","pts":2,"why":"Disasters and bad government were read as signs that Heaven had taken the Mandate away."},
  {"t":"text","q":"Qin Shi Huang ruled with strict laws and harsh punishments. Whose writings best match his way of ruling?","a":[{"all":[["han fei","hanfei"]],"none":["not"]}],"show":"Han Feizi (Legalism)","pts":2,"why":"Han Feizi was the best-known Legalist writer, and the Qin ruled with Legalist ideas."},
  {"t":"open","key":"exit_qin","q":"Name one achievement and one cost of Qin Shi Huang's rule.","min":10,"rows":2,"rubric":["Achievement: unification, standardization, Great Wall, roads","Cost: forced labor, harsh laws, book burning"],"model":"He united China and standardized writing and money, but he forced hundreds of thousands of people to labor on his projects."}],
 "next": "Week 14: the Silk Road, the trade routes that connected China, India, Persia, Africa and Rome."
}

TEACHER = {
 "standards": [
  "SS.6.W.4.6: Describe the concept of the Mandate of Heaven and its connection to the Zhou and later dynasties.",
  "SS.6.W.4.7: Explain the basic teachings of Laozi, Confucius, and Han Fei Zi.",
  "SS.6.W.4.8: Describe the contributions of classical and post classical China.",
  "SS.6.W.4.9: Identify key figures from classical and post classical China.",
  "SS.6.W.2.4: Compare the economic, political, social, and religious institutions of ancient river civilizations.",
  "SS.6.G.2.1: Explain how major physical characteristics, natural resources, climate, and absolute and relative locations have influenced settlement, interactions, and the economies of ancient civilizations of the world.",
  "SS.6.W.1.3: Interpret primary and secondary sources."],
 "materials": ["The interactive lesson", "A world map or globe", "A soft paintbrush, water or thinned washable paint, newspaper or paper bags", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 12 Reconnect questions."],
  [5, "Hook", "Describe how oracle bones were used. Find China on a globe."],
  [8, "Geography", "Discuss the two rivers and the natural barriers."],
  [12, "Shang and Zhou", "Oracle bones and bronze; the Mandate of Heaven; walk through the dynastic cycle."],
  [13, "Three schools", "Read the two Analects sayings aloud. Compare Confucianism, Daoism and Legalism."],
  [10, "Qin and Han", "Weigh Qin's achievements and costs. The Terracotta Army; Han civil service and paper."],
  [6, "Assign", "Start brush writing together; assign the rest, Think Deeper and the Exit Check."]],
 "key_questions": ["How did geography shape China?", "What made a ruler legitimate?", "Which philosophy would you choose, and why?", "Was Qin's unity worth its cost?"],
 "misconceptions": ["China was always one unified country.", "The Great Wall was built all at once by one emperor (most of today's wall is from the later Ming dynasty).", "Confucianism is the same as a religion with gods (it is mainly a philosophy of ethics and government).", "Chinese characters are all pictures (most combine meaning and sound parts)."],
 "support": ["Provide a labeled map.", "Use a three-column chart for Confucianism, Daoism and Legalism.", "Pre-teach the dynastic cycle with the diagram."],
 "challenge": ["Read more of the Analects in Legge's translation (public domain) and choose a saying to explain.", "Research how archaeologists are preserving the painted colors of the Terracotta Army."],
 "background": "<p>Shang dynasty about 1600 to 1046 BCE; oracle bones rediscovered around 1899 and excavated at Anyang (Yinxu) from 1928; about 4,000 distinct characters attested, of which about a third are deciphered. The Zhou conquest about 1046 BCE; the Mandate of Heaven appears in early Zhou texts. Warring States period 475 to 221 BCE (Eastern Zhou from 770 BCE). Confucius 551 to 479 BCE; the Analects quotations are from James Legge's 1861 translation (public domain): Analects 15.23 and 2.15 in Legge's numbering (15.23 is 15.24 in many modern editions). Qin unification 221 BCE; the Terracotta Army was found by farmers in March 1974; estimates of about 8,000 figures. The name China is often traced to Qin, though this is debated. Han 206 BCE to 220 CE; Cai Lun's papermaking report is dated 105 CE, but earlier paper fragments have been found; Zhang Heng's seismoscope 132 CE. Han Feizi died 233 BCE; Legalism's 'two handles' of government are reward and punishment. Benchmarks SS.6.W.4.6 to 4.9 checked word for word on CPALMS.</p>",
 "sources": ["Legge, J., trans. (1861), The Chinese Classics: Confucian Analects (public domain).", "Metropolitan Museum of Art, Heilbrunn Timeline: Shang, Zhou, Qin and Han dynasties.", "British Museum, Oracle bones.", "Smithsonian National Museum of Asian Art, Ancient Chinese bronzes.", "UNESCO World Heritage Centre, Mausoleum of the First Qin Emperor."]
}

PRINT = {
 "directions": "Use complete sentences and evidence.",
 "items": [
  {"q":"Why was the Yellow River called \"China's Sorrow\"?","a":"Its floods were very destructive, even though its soil made farmland rich.","lines":2},
  {"q":"What were oracle bones used for, and why are they important?","a":"To ask the ancestors questions; they hold the oldest known Chinese writing.","lines":2},
  {"q":"Explain the Mandate of Heaven and the dynastic cycle.","a":"Heaven gives a just ruler the right to rule; dynasties rise, prosper, decline, face rebellion and are replaced.","lines":3},
  {"q":"Compare the teachings of Confucius and Han Feizi.","a":"Confucius (Confucianism: good example, respect, relationships); Han Feizi (Legalism): strict laws, rewards and harsh punishments.","lines":2},
  {"q":"Name two things Qin Shi Huang standardized.","a":"Writing, money, weights and measures, cart axles.","lines":1},
  {"q":"Name two achievements of the Han dynasty.","a":"Confucian civil service; paper; seismoscope; beginning the Silk Road.","lines":2}]
}
