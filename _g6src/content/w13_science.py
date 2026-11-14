def _box(x, y, w, h, t1, t2="", fill="#fff", stroke="#0A1F3D", tc="#0A1F3D", bold=False):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
    fw = ' font-weight="bold"' if bold else ''
    if t2:
        s += f'<text x="{x+w/2}" y="{y+h/2-3}" text-anchor="middle" font-size="11" fill="{tc}"{fw}>{t1}</text><text x="{x+w/2}" y="{y+h/2+11}" text-anchor="middle" font-size="11" fill="{tc}">{t2}</text>'
    else:
        s += f'<text x="{x+w/2}" y="{y+h/2+4}" text-anchor="middle" font-size="11" fill="{tc}"{fw}>{t1}</text>'
    return s

def keytree():
    s = ('<svg viewBox="0 0 660 400" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Dichotomous key for six Florida leaves drawn as a branching diagram">'
         '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">A dichotomous key for six Florida leaves</text>')
    line = lambda x1, y1, x2, y2: f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#5b6676" stroke-width="1.5" fill="none"/>'
    # step nodes (question, yes-left / no-right)
    s += _box(250, 34, 160, 34, "1. Is the leaf a needle?", fill="#0A1F3D", tc="#fff", bold=True)
    s += line(290, 68, 90, 92) + line(370, 68, 410, 92)
    s += _box(20, 92, 140, 38, "1a. Yes, needles", "in bundles", fill="#e6f2e1", stroke="#3d9a2f")
    s += _box(340, 92, 200, 34, "2. Is it a huge folded fan?", fill="#0A1F3D", tc="#fff", bold=True)
    s += line(380, 126, 230, 150) + line(500, 126, 520, 150)
    s += _box(150, 150, 150, 38, "2a. Yes: fan with", "a curved midrib", fill="#e6f2e1", stroke="#3d9a2f")
    s += _box(410, 150, 230, 34, "3. Several leaflets on one stalk?", fill="#0A1F3D", tc="#fff", bold=True)
    s += line(450, 184, 330, 208) + line(600, 184, 560, 208)
    s += _box(250, 208, 160, 38, "3a. Yes: compound,", "toothed leaflets", fill="#fde8e8", stroke="#DB2F30")
    s += _box(460, 208, 180, 34, "4. Is the leaf lobed?", fill="#0A1F3D", tc="#fff", bold=True)
    s += line(500, 242, 420, 266) + line(610, 242, 590, 266)
    s += _box(330, 266, 170, 34, "5. Deep, pointed lobes?", fill="#0A1F3D", tc="#fff", bold=True)
    s += _box(520, 266, 130, 38, "4b. No: oval,", "smooth edge", fill="#e6f2e1", stroke="#3d9a2f")
    s += line(370, 300, 300, 324) + line(460, 300, 480, 324)
    s += _box(220, 324, 160, 38, "5a. Yes: star-shaped,", "long pointed lobes", fill="#e6f2e1", stroke="#3d9a2f")
    s += _box(400, 324, 160, 38, "5b. No: short, shallow", "toothed lobes", fill="#e6f2e1", stroke="#3d9a2f")
    # answers
    for x, y, t in [(90, 146, "SLASH PINE"), (225, 204, "CABBAGE PALM"), (330, 262, "BRAZILIAN PEPPER (invasive)"), (585, 320, "LIVE OAK"), (300, 378, "SWEETGUM"), (480, 378, "RED MAPLE")]:
        s += f'<text x="{x}" y="{y}" text-anchor="middle" font-size="11" font-weight="bold" fill="{"#DB2F30" if "invasive" in t else "#2c6e22"}">{t}</text>'
    s += '<text x="20" y="394" font-size="10" fill="#5b6676">Left branch = yes; right branch = no. Each step has exactly two choices.</text></svg>'
    return s

TRAITS = ('<svg viewBox="0 0 660 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Leaf traits used in keys: simple, compound, lobed, toothed edge, smooth edge, parallel veins">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Leaf traits scientists use in keys</text>'
  '<g fill="#bfe0a8" stroke="#2c6e22" stroke-width="2">'
  # simple
  '<path d="M55 160 v-20 M55 140 q-28 -30 0 -86 q28 56 0 86z"/>'
  # compound
  '<path d="M160 165 v-110" fill="none"/>' + ''.join(f'<ellipse cx="{160+dx}" cy="{y}" rx="13" ry="7" transform="rotate({ang} {160+dx} {y})"/>' for dx, y, ang in [(-16, 75, 20), (16, 75, -20), (-16, 100, 20), (16, 100, -20), (-16, 125, 20), (16, 125, -20)]) + '<ellipse cx="160" cy="55" rx="7" ry="13"/>'
  # lobed (star)
  '<path d="M265 160 v-22 M265 138 L248 128 L222 132 L242 112 L232 82 L258 100 L265 62 L272 100 L298 82 L288 112 L308 132 L282 128 Z"/>'
  # toothed
  '<path d="M375 160 v-20"/><polygon points="375.0,140.0 370.9,136.1 367.7,132.2 363.0,128.3 360.9,124.4 356.0,120.5 355.4,116.5 350.6,112.6 351.3,108.7 347.2,104.8 349.3,100.9 346.0,97.0 349.3,93.1 347.2,89.2 351.3,85.3 350.6,81.4 355.4,77.5 356.0,73.5 360.9,69.6 363.0,65.7 367.7,61.8 370.9,57.9 375.0,54.0 375.0,54.0 379.1,57.9 382.3,61.8 387.0,65.7 389.1,69.6 394.0,73.5 394.6,77.5 399.4,81.4 398.7,85.3 402.8,89.2 400.7,93.1 404.0,97.0 400.7,100.9 402.8,104.8 398.7,108.7 399.4,112.6 394.6,116.5 394.0,120.5 389.1,124.4 387.0,128.3 382.3,132.2 379.1,136.1 375.0,140.0"/>'
  # parallel veins (grass-like)
  '<path d="M485 160 q-14 -50 0 -104 q14 54 0 104z"/>'
  '</g>'
  '<g stroke="#2c6e22" stroke-width="1" fill="none"><path d="M480 150 q-6 -45 3 -90 M490 150 q6 -45 -3 -90 M485 158 v-100"/><path d="M55 140 v-80 M55 120 l-10 -10 M55 120 l10 -10 M55 100 l-10 -10 M55 100 l10 -10"/></g>'
  '<path d="M600 160 v-20" stroke="#2c6e22" stroke-width="2"/><g stroke="#2c6e22" stroke-width="2.5">' + ''.join(f'<line x1="{600+dx}" y1="140" x2="{600+dx*2.4}" y2="{60+abs(dx)}"/>' for dx in (-10, -5, 0, 5, 10)) + '</g>'
  + ''.join(f'<text x="{x}" y="186" text-anchor="middle" font-weight="bold">{a}</text><text x="{x}" y="202" text-anchor="middle" font-size="11" fill="#5b6676">{b}</text>'
            for x, a, b in [(55, "simple", "one blade"), (160, "compound", "many leaflets"), (265, "lobed", "deep bulges"), (375, "toothed edge", "jagged margin"), (485, "parallel veins", "palms, grasses"), (600, "needles", "pines")]) +
  '<text x="330" y="224" text-anchor="middle" font-size="11" fill="#5b6676">Use traits you can see or measure on every leaf. Avoid color (it changes) and opinions (\"pretty\").</text></svg>')

LESSON = {
 "unit": "Unit 3: The Diversity of Life",
 "title": "Dichotomous Keys",
 "subtitle": "How do you figure out what a living thing is when you don't know its name? Scientists use dichotomous keys: a series of either-or questions that narrows millions of possibilities down to one.",
 "objectives": [
  "Explain what a dichotomous key is and how it uses paired, opposite statements.",
  "Use a dichotomous key to identify Florida leaves and animals.",
  "Describe leaf traits used in keys: simple or compound, lobed, toothed or smooth edges, vein patterns and needles.",
  "Write and test a dichotomous key for a real collection, and revise it using evidence.",
  "Explain how a key (for identifying) is different from classification (for showing relationships)."],
 "vocab": [
  ["dichotomous key", "A tool that identifies an organism through a series of paired, opposite choices."],
  ["couplet", "In a key, a pair of opposite statements; you choose the one that fits."],
  ["trait", "A feature you can observe or measure, such as leaf shape or number of legs."],
  ["simple leaf", "A leaf with one blade on its stalk."],
  ["compound leaf", "A leaf made of several smaller leaflets on one stalk."],
  ["margin", "The edge of a leaf: smooth (entire) or toothed."],
  ["invasive species", "A non-native species that spreads and harms native ecosystems."]],
 "reconnect": {
  "title": "Week 12: Classification and scientific names",
  "intro": "A key helps you find an organism's name. Review how names and groups work.",
  "items": [
   {"t":"blanks","q":"Complete the levels of classification, from broadest to most specific.","sent":"Domain, kingdom, ___, class, order, family, ___, species","blanks":[[{"all":[["phylum"]],"none":["not"]}],[{"all":[["genus"]],"none":["not"]}]],"show":"phylum; genus","pts":2,"why":"Dear King Philip Came Over For Good Soup."},
   {"t":"text","q":"In the scientific name Puma concolor, which word is the genus?","a":[{"all":[["puma"]],"none":["not","concolor"]}],"show":"Puma","pts":2,"why":"The genus comes first and is capitalized; the species name follows."},
   {"t":"open","key":"rc_names","q":"Why do scientists use scientific names instead of common names like \"panther\" or \"cougar\"?","min":12,"rows":2,"rubric":["Common names vary by place and language; one scientific name is used worldwide, so there is no confusion"],"model":"The same animal has many common names (panther, cougar, mountain lion), but it has only one scientific name, Puma concolor, which scientists everywhere understand."},
   {"t":"text","q":"Mushrooms and the yeast from Week 11 belong to which kingdom?","a":[{"all":[["fungi","fungus"]],"none":["not"]}],"show":"Fungi","pts":2,"why":"Fungi absorb their food."}]},
 "hook": {
  "title": "Native or Invader?",
  "html": "<p>A homeschool family in Florida notices a fast-growing shrub along their fence with shiny leaves and clusters of bright red berries. It looks pretty. Should they leave it, or pull it out?</p><p>It might be <b>Brazilian pepper</b>, one of the most harmful invasive plants in Florida. It crowds out native plants across hundreds of thousands of acres, and its sap can irritate skin. Or it might be a harmless native, like yaupon holly, which also has red berries. Guessing wrong could mean destroying a native plant or letting an invader spread.</p><p>Scientists, park rangers and gardeners solve problems like this with a <b>dichotomous key</b>. Last week you pressed leaves; this week you will learn to identify them and build a key of your own.</p><div class='callout'><b>Big question:</b> How can a series of simple either-or questions identify any living thing?</div>"},
 "learn": [
  {"title": "How a Dichotomous Key Works",
   "visual": keytree(),
   "html": "<p><i>Dichotomous</i> comes from Greek words meaning \"cut in two.\" A dichotomous key is a list of steps. Each step is a <b>couplet</b>: two opposite statements about a trait. You read both, choose the one that matches your organism, and follow it to the next step, until you reach a name.</p><p>Most keys are written as numbered lists, like this:</p><div class='card' style='font-family:Georgia,serif'>1a. Leaf is a needle ........ <b>slash pine</b><br>1b. Leaf is flat ........ go to 2<br>2a. Leaf is a huge folded fan with a curved midrib ........ <b>cabbage palm</b><br>2b. Leaf is not a folded fan ........ go to 3<br>3a. Leaf has several leaflets on one stalk ........ <b>Brazilian pepper</b><br>3b. Leaf has one blade ........ go to 4<br>4a. Leaf is lobed ........ go to 5<br>4b. Leaf is not lobed; oval with a smooth edge ........ <b>live oak</b><br>5a. Lobes are deep and pointed, cut more than halfway to the center (star-shaped) ........ <b>sweetgum</b><br>5b. Lobes are short and shallow, cut less than halfway to the center ........ <b>red maple</b></div>",
   "checks": [
    {"t":"num","q":"At each step of a dichotomous key, how many choices do you have?","a":2,"unit":"choices","pts":1,"why":"Dicho = in two: every couplet has exactly two statements."},
    {"t":"text","q":"Use the key. You find a flat, leathery leaf about 5 cm long. It is shaped like an egg, has no bulges, has no teeth along its edge, and grows alone on its stalk. What tree is it?","a":[{"all":[["live oak","oak"]],"none":["not","red"]}],"show":"live oak","pts":2,"why":"1b → 2b → 3b → 4b: live oak."},
    {"t":"text","q":"Use the key. A leaf has several leaflets on one stalk. What plant is it?","a":[{"all":[["brazilian pepper","pepper"]],"none":["not"]}],"show":"Brazilian pepper","pts":2,"why":"1b → 2b → 3a: Brazilian pepper, an invasive species."},
    {"t":"open","key":"twochoices","q":"Why do you think keys always give exactly two choices at each step, instead of five or ten?","min":20,"rows":2,"rubric":["Two opposite choices are easy to compare and hard to confuse","One clear decision at a time makes the key reliable and repeatable for any user"],"model":"Two opposite choices make each decision simple: the leaf either is a needle or it isn't. With five or ten choices, people could get confused or pick different answers, so the key would be less reliable."}]},
  {"title": "Reading a Leaf Like a Scientist",
   "visual": TRAITS,
   "html": "<p>Leaf keys use traits you can observe on every leaf:</p><ul><li><b>Simple or compound:</b> a simple leaf has one blade; a compound leaf has several <b>leaflets</b> on one stalk. Look for the bud where the stalk meets the twig: a whole compound leaf has one bud at its base, but single leaflets do not.</li><li><b>Lobed or unlobed:</b> lobes are deep bulges, like the points of a sweetgum star.</li><li><b>Margin:</b> the edge is <b>smooth</b> (also called entire) or <b>toothed</b> (jagged).</li><li><b>Veins:</b> most broad leaves have <b>net veins</b> that branch like a web. Palms, grasses and lilies have <b>parallel veins</b> that run side by side.</li><li><b>Needles and scales:</b> pines have needles, often in bundles; cypress trees have tiny, flat leaves.</li></ul><p>Good keys avoid color, because a leaf's color can change with the season, its age or the light. They also avoid opinions such as \"pretty\" or \"big,\" unless \"big\" is given as a measurement.</p>",
   "checks": [
    {"t":"blanks","q":"Use the leaf vocabulary.","sent":"A leaf made of several leaflets on one stalk is ___. A leaf edge with no teeth is called smooth or ___.","blanks":[[{"all":[["compound"]],"none":["not"]}],[{"all":[["entire"]],"none":["not"]}]],"show":"compound; entire","pts":2,"why":"Compound = many leaflets; entire = a smooth margin."},
    {"t":"text","q":"A cabbage palm's leaf has veins that run side by side. What is this vein pattern called?","a":[{"all":[["parallel"]],"none":["not","net"]}],"show":"parallel veins","pts":2,"why":"Palms and grasses have parallel veins; most broad leaves have net veins."},
    {"t":"open","key":"nocolor","q":"A student writes the couplet \"1a. Leaf is green / 1b. Leaf is red.\" Give two reasons this is a poor couplet for a red maple, using what you learned.","min":25,"rows":3,"rubric":["Color changes with the season, age or light (red maple leaves are green in summer, red in fall)","Not a measurable or permanent trait, so different users at different times would choose differently"],"model":"Red maple leaves are green most of the year and turn red in fall, so the same tree would key out two different ways depending on the month. Color also depends on the light and the leaf's age, so two people might disagree. A shape trait like lobes is better."}]},
  {"title": "Writing a Key That Works",
   "html": "<p>A key is only useful if someone else can follow it and get the right answer. Scientists follow these rules:</p><ol><li><b>Make each couplet opposite.</b> \"Leaf is lobed / Leaf is not lobed\" works. \"Leaf is lobed / Leaf is large\" does not, because a leaf could be both or neither.</li><li><b>Use observable or measurable traits</b>, such as shape, edges, number of parts or a length in centimeters.</li><li><b>Start with traits that split the group into big, clear halves</b>, then get more specific.</li><li><b>Test it.</b> Have someone who has never seen your collection use the key. Where they get stuck, revise.</li></ol><p>Notice a pattern: each couplet separates one group into two. So a key for 2 organisms needs 1 couplet, a key for 3 needs 2, and a key for 6 leaves needs 5.</p>",
   "checks": [
    {"t":"open","key":"badcouplet","q":"What is wrong with this couplet? \"1a. Leaf is lobed. / 1b. Leaf is longer than 8 cm.\" Rewrite it so it works.","min":25,"rows":3,"rubric":["The statements are not opposites: a leaf could be both lobed and longer than 8 cm, or neither","A correct rewrite: \"1a. Leaf is lobed / 1b. Leaf is not lobed\" (or a length pair)"],"model":"The two statements are not opposites. A sweetgum leaf could be lobed and longer than 8 cm, so it fits both, and a small oval leaf fits neither. A better couplet: \"1a. Leaf is lobed. / 1b. Leaf is not lobed.\""},
    {"t":"num","q":"How many couplets does a dichotomous key need to identify 8 different leaves?","a":7,"unit":"couplets","pts":2,"why":"Each couplet splits one group into two, so you always need one fewer couplet than organisms: 8 − 1 = 7."},
    {"t":"open","key":"opinion","q":"Explain why \"Leaf is pretty / Leaf is not pretty\" fails as a couplet, even though the two statements are opposites.","min":20,"rows":2,"rubric":["\"Pretty\" is an opinion, not an observable or measurable trait","Different people would choose differently, so the key would not give repeatable results"],"model":"\"Pretty\" is an opinion, not something you can observe or measure. Two people would choose differently, so the key would not give the same answer every time."}]},
  {"title": "Keys in Real Science",
   "html": "<p>Keys are used every day. Botanists use them in <b>herbaria</b>, collections of pressed plants like the 145,000 specimens Ynés Mexía gathered. Florida's University of Florida IFAS extension and the Florida Fish and Wildlife Conservation Commission publish keys and guides so residents can identify invasive species such as Brazilian pepper, which is illegal to sell or plant in Florida. Wildlife biologists use keys to identify fish, insects, snakes and animal tracks.</p><p>Phone apps that identify plants from a photo are popular too. They are fast, but they can be wrong, especially with a blurry photo or a plant with look-alikes, so scientists double-check an app's answer with a key or an expert.</p><p>A key is a tool for <b>identifying</b>, not for showing how organisms are related. A key might group bats with birds because both have wings, but in classification bats are mammals: they have fur and feed their young milk. A key just needs traits that are easy to see; classification looks for shared ancestry.</p>",
   "checks": [
    {"t":"open","key":"invasive","q":"Why is it important for Florida families and landowners to be able to identify Brazilian pepper correctly? Give two reasons.","min":25,"rows":3,"rubric":["It spreads and crowds out native plants and wildlife habitat","Correct ID avoids destroying native look-alikes (yaupon holly) or letting it spread; its sap can irritate skin"],"model":"Brazilian pepper spreads quickly and crowds out the native plants that wildlife need, so it should be removed. But if people guess wrong, they might destroy a harmless native plant like yaupon holly or leave the invader to spread. Knowing what it is also warns them to wear gloves, because its sap can irritate skin."},
    {"t":"text","q":"Fill in: a dichotomous key is a tool for ___ an organism, not for showing how organisms are related.","a":[{"all":[["identifying","identify","identification","naming"]],"none":["not"]}],"show":"identifying","pts":2,"why":"Keys identify; classification shows relationships."},
    {"t":"num","q":"A plant-ID app is correct about 85 out of every 100 times. If you use it on 40 plants, about how many will it identify wrongly?","a":6,"unit":"plants","pts":2,"why":"It is wrong 15% of the time: 0.15 × 40 = 6."},
    {"t":"open","key":"batbird","q":"A key puts bats and birds on the same branch because both have wings. Is that a mistake? Explain the difference between a key and classification.","min":25,"rows":3,"rubric":["Not a mistake for a key: it only needs easy-to-see traits to identify","Classification groups by shared ancestry and many traits, so bats are mammals (fur, milk), not birds"],"model":"It is not a mistake for a key, because a key only needs a trait that is easy to see to separate organisms. Classification is different: it groups organisms by shared ancestry and many traits, so bats go with mammals because they have fur and feed their young milk."}]}],
 "handson": {
  "title": "Key Your Leaf Collection",
  "intro": "Turn the leaves you pressed last week into a working dichotomous key, then test it on someone else.",
  "materials": ["Your 6 to 8 pressed leaves from Week 12", "A table or floor space", "Paper and pencil", "A ruler (centimeters)", "Optional: a magnifying glass", "Sticky notes or index cards (to number the leaves and to write couplets for the floor test)", "Optional: a Florida tree field guide (library)"],
  "steps": [
   "Lay out the leaves and give each a number. Wash your hands after handling leaves, and keep them away from your mouth and from pets. If a leaf might be Brazilian pepper, handle it only with gloves or a bag over your hand; its sap can irritate skin.",
   "Find one trait that splits all the leaves into two piles (for example, lobed / not lobed). Physically move them into two piles. Write it as couplet 1.",
   "Take one pile and split it again with a new trait. Keep splitting each pile until every leaf is alone. Write each split as a numbered couplet with \"go to\" steps.",
   "If you know a leaf's name, write it at the end of its path; if not, give it a descriptive name (\"leaf with three toothed lobes\") or look it up with an adult in a field guide.",
   "Floor test: write each couplet on its own index card and lay the cards on the floor as a branching path, with arrows to the next card. A family member picks a mystery leaf, stands at card 1, and steps to the a or b side at each card using only your key. Watch where they hesitate, then revise those couplets."],
  "record": [
   {"t":"open","key":"mykey","q":"Write your finished dichotomous key as a numbered list of couplets.","min":50,"rows":10,"rubric":["One fewer couplet than leaves","Each couplet is a pair of opposites","Observable or measurable traits only (no color or opinions)","Every leaf reached by exactly one path"],"model":"1a. Leaf is a needle ........ go to 2\n1b. Leaf is flat ........ go to 3\n2a. Needles in bundles of 2 or 3 ........ slash pine\n2b. Needles single ........ leaf A\n3a. Leaf is lobed ........ go to 4\n3b. Leaf is not lobed ........ go to 5\n4a. 5 to 7 long, pointed lobes ........ sweetgum\n4b. 3 shallow, toothed lobes ........ red maple\n5a. Edge is smooth ........ live oak\n5b. Edge is toothed ........ leaf B"},
   {"t":"open","key":"keytest","q":"Describe the test. Which leaf did your tester choose, did they reach the right answer, and what did you revise?","min":30,"rows":4,"rubric":["Describes the test and the result","Identifies a confusing couplet","Explains a specific revision based on the evidence"],"model":"My mom chose leaf 4. She got stuck at couplet 5, \"edge is smooth / edge is toothed,\" because the leaf had tiny teeth only near the tip. I changed it to \"teeth along most of the edge / no teeth or teeth only at the tip,\" and on the second try she reached the right answer."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"tencm","q":"A key's couplet reads \"Leaf longer than 10 cm / Leaf shorter than 10 cm.\" A student measures a leaf that is exactly 10 cm and gets stuck. How would you fix the couplet? What does this teach about writing scientific tools?","min":70,"rows":6,"rubric":["Fix: include the boundary in one choice (\"10 cm or longer / shorter than 10 cm\") or use a different trait","Notes that living things vary, so traits near the boundary are risky","Lesson: tools must be clear, cover every case, be tested and revised so anyone gets the same result"],"model":"I would rewrite it as \"Leaf 10 cm or longer / Leaf shorter than 10 cm,\" so every leaf fits exactly one choice. Even better, I might choose a different trait, because leaves on the same tree vary in size and one near 10 cm could go either way. This shows that scientific tools must cover every possible case and should be tested by other people, then revised, so everyone gets the same result."},
   {"t":"open","key":"appvskey","q":"You find a plant in your yard that might be Brazilian pepper. Would you trust a phone app or a dichotomous key more before removing it? Explain, and describe how you could use both.","min":70,"rows":6,"rubric":["A clear position with reasons","Strengths and weaknesses of apps (fast, but can be wrong with look-alikes or bad photos) and keys (slower, but checks traits step by step)","A sensible plan using both (app first, then confirm with a key, an expert or UF/IFAS extension)"],"model":"I would trust a key more, because it makes me check each trait myself, while an app can be fooled by a blurry photo or a look-alike such as yaupon holly. The app is still useful because it is fast. My plan: take a clear photo for the app, then confirm with a Florida key, checking for leaflets and toothed edges. If they disagree, I would ask the county extension office before removing the plant."}]},
 "exit": [
  {"t":"text","q":"Use the key from the lesson. A leaf is a needle. What tree is it?","a":[{"all":[["pine"]],"none":["not"]}],"show":"slash pine","pts":2,"why":"1a: needles in bundles → slash pine."},
  {"t":"text","q":"Use the key. A flat leaf about 12 cm across grows alone on its stalk. It has five deep, pointed sections that spread out like the fingers of a hand. What tree is it?","a":[{"all":[["sweetgum","sweet gum"]],"none":["not"]}],"show":"sweetgum","pts":2,"why":"1b → 2b → 3b → 4a → 5a."},
  {"t":"open","key":"exit_rule","q":"Give one rule for writing a good couplet and explain why it matters.","min":12,"rows":2,"rubric":["A correct rule (opposites; observable or measurable traits; no color or opinions)","Why: so anyone gets the same answer"],"model":"The two statements must be opposites, so every organism fits exactly one choice and anyone using the key gets the same answer."},
  {"t":"text","q":"A leaf has 9 small leaflets lined up along one stalk, with one bud where the stalk meets the twig. Is it one compound leaf or 9 simple leaves? Type compound or simple.","a":[{"all":[["compound"]],"none":["not","simple"]}],"show":"compound (one leaf)","pts":2,"why":"One bud at the base of the whole stalk means it is one compound leaf; single leaflets have no buds."}],
 "next": "Week 14: microorganisms, the living things too small to see."
}

TEACHER = {
 "standards": [
  "SC.6.L.15.1: Analyze and describe how and why organisms are classified according to shared characteristics with emphasis on the Linnaean system combined with the concept of Domains.",
  "SC.6.N.1.4: Discuss, compare and negotiate methods used, results obtained and explanations among groups of students conducting the same investigation (for a homeschool student: compare with a parent or a KCE classmate).",
  "SC.6.N.1.5: Recognize that science involves creativity, not just in designing experiments, but also in creating explanations that fit evidence.",
  "NGSS Science and Engineering Practices 2 and 6: developing and using models; constructing explanations and designing solutions."],
 "materials": ["The interactive lesson", "The student's 6 to 8 pressed leaves from Week 12", "Paper, pencil, a ruler in centimeters, sticky notes", "Optional: a magnifying glass and a Florida tree field guide", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 12 Reconnect questions."],
  [5, "Hook", "Pose the native-or-invader problem."],
  [12, "How a key works", "Walk through the six-leaf key together, aloud, with two practice identifications."],
  [10, "Leaf traits", "Examine the pressed leaves for simple or compound, lobes, margins and veins."],
  [10, "Writing a key", "Fix the bad couplets. Discover the couplets = organisms − 1 pattern."],
  [10, "Keys in real science", "Discuss invasive species, apps and the key-versus-classification difference."],
  [7, "Assign", "Make the first split of the leaf piles together; assign the rest of the key, the test, Think Deeper and the Exit Check."]],
 "key_questions": ["Is each couplet a true pair of opposites?", "Could someone who has never seen these leaves follow this key?", "Why avoid color?", "How is identifying different from classifying?"],
 "misconceptions": ["A key shows how organisms are related (it only identifies).", "Each leaflet of a compound leaf is a separate leaf.", "Color is a reliable trait.", "Phone apps are always right."],
 "support": ["Start with 4 leaves instead of 8.", "Give couplet frames: \"___a. Leaf is ___ / ___b. Leaf is not ___.\"", "Use only one trait type (shape) for the first key."],
 "challenge": ["Write a key for 8 Florida animals from Week 12 using only observable traits.", "Compare a free UF/IFAS invasive plant guide with your key: what traits do the experts use?"],
 "background": "<p>Leaf traits: slash pine (Pinus elliottii) needles in bundles of 2 and 3; cabbage palm (Sabal palmetto) leaves are costapalmate (a fan with a curved midrib); Brazilian pepper (Schinus terebinthifolia) has pinnately compound leaves with usually 3 to 13 leaflets, often toothed; it is on Florida's state Noxious Weed List and is prohibited from sale and planting, and as a relative of poison ivy in the cashew family its sap can irritate skin. Live oak (Quercus virginiana): simple, oval, leathery, usually smooth-edged, evergreen. Sweetgum (Liquidambar styraciflua): star-shaped, 5 to 7 pointed lobes, finely toothed. Red maple (Acer rubrum): 3 to 5 shallow lobes, toothed margins, often a red petiole. Yaupon holly (Ilex vomitoria) is a native red-berried shrub. A key with n end points has n − 1 couplets. Florida's invasive plant information: UF/IFAS Center for Aquatic and Invasive Plants and the Florida Invasive Species Council.</p>",
 "sources": ["University of Florida IFAS, Center for Aquatic and Invasive Plants: Brazilian peppertree.", "Florida Department of Agriculture and Consumer Services, Noxious Weed List (5B-57.007, F.A.C.).", "University of Florida IFAS Extension, Florida trees fact sheets (live oak, sweetgum, red maple, slash pine, cabbage palm).", "Florida Invasive Species Council, plant list."]
}

PRINT = {
 "directions": "Use the six-leaf key from the lesson, and answer in complete sentences.",
 "items": [
  {"q":"What is a dichotomous key, and what is a couplet?","a":"A tool that identifies organisms through paired opposite choices; a couplet is one pair of opposite statements.","lines":2},
  {"q":"Trace the path for a red maple leaf through the key (for example, 1b → ...).","a":"1b → 2b → 3b → 4a → 5b.","lines":1},
  {"q":"Explain the difference between a simple and a compound leaf.","a":"Simple: one blade on the stalk. Compound: several leaflets on one stalk.","lines":2},
  {"q":"Rewrite this couplet so it works: \"1a. Leaf has teeth / 1b. Leaf is long.\"","a":"1a. Leaf edge has teeth / 1b. Leaf edge is smooth (no teeth).","lines":2},
  {"q":"How many couplets does a key for 12 organisms need? Explain.","a":"11, because each couplet splits one group into two.","lines":2},
  {"q":"Why should a key avoid color as a trait?","a":"Color changes with season, age and light, so the same organism could key out differently.","lines":2}]
}
