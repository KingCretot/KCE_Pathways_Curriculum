EUPH = [(38.6, 38.4), (38.3, 37.0), (38.2, 36.0), (39.9, 35.3), (40.9, 34.5), (42.0, 34.4), (43.3, 33.4), (44.3, 32.6), (45.2, 31.9), (46.26, 31.05), (47.43, 31.0)]
TIG = [(40.2, 37.9), (41.7, 37.3), (42.7, 36.9), (43.13, 36.34), (43.3, 35.5), (43.8, 34.6), (44.37, 33.31), (45.0, 32.8), (45.8, 32.5), (46.9, 31.9), (47.43, 31.0)]
SHATT = [(47.43, 31.0), (47.8, 30.5), (48.5, 29.95)]
GULF = [(48.5, 29.95), (48.0, 29.4), (48.4, 28.5), (48.9, 28.0), (50.5, 28.0), (50.5, 29.6), (50.0, 30.1), (49.2, 30.2)]

def mesomap():
    k = 34.0; lon0, lon1, lat0, lat1 = 38.0, 50.5, 28.0, 38.5; ox = 20
    P = lambda lon, lat: (round((lon - lon0) * k + ox, 1), round((lat1 - lat) * k + 34, 1))
    pl = lambda L: ' '.join('%s,%s' % P(*p) for p in L)
    mw = (lon1 - lon0) * k; mh = (lat1 - lat0) * k; lx = ox + mw + 16
    W = int(lx + 170); H = int(mh + 56)
    s = (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Map of Mesopotamia with the Tigris and Euphrates rivers">'
         f'<text x="{W/2}" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Mesopotamia: the land between the rivers</text>'
         f'<rect x="{ox}" y="34" width="{mw}" height="{mh}" fill="#efe1bd"/>'
         f'<polygon points="{pl(GULF)}" fill="#bfe3f5"/>'
         f'<polyline points="{pl(EUPH)}" fill="none" stroke="#0047BA" stroke-width="3" stroke-linejoin="round"/>'
         f'<polyline points="{pl(TIG)}" fill="none" stroke="#0047BA" stroke-width="3" stroke-linejoin="round"/>'
         f'<polyline points="{pl(SHATT)}" fill="none" stroke="#0047BA" stroke-width="3"/>')
    for lon, lat, t, rot in [(40.6, 34.9, "Euphrates", 25), (43.6, 35.4, "Tigris", 70)]:
        x, y = P(lon, lat); s += f'<text x="{x}" y="{y}" font-size="11" fill="#0047BA" font-style="italic" transform="rotate({rot} {x} {y})">{t}</text>'
    x, y = P(48.9, 29.0); s += f'<text x="{x}" y="{y}" font-size="11" fill="#0047BA" font-style="italic">Persian Gulf</text>'
    for lon, lat, t in [(46.8, 35.6, "ZAGROS MOUNTAINS"), (38.6, 32.6, "SYRIAN DESERT")]:
        x, y = P(lon, lat); s += f'<text x="{x}" y="{y}" font-size="10" fill="#8a6d1f" font-weight="bold">{t}</text>'
    x, y = P(44.6, 32.0); s += f'<text x="{x}" y="{y}" font-size="12" font-weight="bold" fill="#DB2F30" style="paint-order:stroke;stroke:#efe1bd;stroke-width:4">SUMER</text>'
    marks = [(43.15, 36.36, "Nineveh"), (44.37, 33.31, "Baghdad (modern capital of Iraq)"), (44.42, 32.54, "Babylon"), (45.64, 31.32, "Uruk"), (46.41, 31.41, "Lagash"), (46.10, 30.96, "Ur")]
    last = -99
    for lon, lat, lab in sorted(marks, key=lambda m: -m[1]):
        x, y = P(lon, lat); ly = max(y, last + 19); last = ly
        fill = "#fff" if lab.startswith("Baghdad") else "#0A1F3D"
        s += f'<circle cx="{x}" cy="{y}" r="4" fill="{fill}" stroke="#0A1F3D" stroke-width="1.5"/><path d="M{x+5} {y} L{lx-4} {ly}" stroke="#8a8f99" stroke-width=".8"/><text x="{lx}" y="{ly+4}" font-size="11">{lab}</text>'
    s += f'<text x="{ox}" y="{H-6}" font-size="10" fill="#5b6676">Rivers follow their modern courses; in ancient times the Euphrates flowed closer to Ur and Uruk. Open circle: modern city.</text></svg>'
    return s

def evolution():
    s = ('<svg viewBox="0 0 640 210" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="How writing developed from tokens to cuneiform">'
         '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">From counting tokens to cuneiform</text>')
    # tokens
    s += '<g transform="translate(40,60)"><circle cx="20" cy="30" r="12" fill="#c98f58" stroke="#7a4a1f"/><path d="M50 42 l12 -24 l12 24z" fill="#c98f58" stroke="#7a4a1f"/><rect x="82" y="20" width="22" height="22" rx="3" fill="#c98f58" stroke="#7a4a1f"/></g>'
    s += '<text x="105" y="140" text-anchor="middle" font-weight="bold">1. Clay tokens</text><text x="105" y="156" text-anchor="middle" font-size="11">each shape = a good</text><text x="105" y="170" text-anchor="middle" font-size="11">(from about 8000 BCE)</text>'
    s += '<path d="M180 90 h30" stroke="#0A1F3D" stroke-width="2"/><path d="M206 85 l8 5 l-8 5" fill="#0A1F3D"/>'
    # envelope / tablet with pictures
    s += '<rect x="235" y="50" width="120" height="80" rx="10" fill="#d9a873" stroke="#7a4a1f" stroke-width="2"/><path d="M255 100 q10 -30 20 0 M262 90 h6" fill="none" stroke="#5a3a1a" stroke-width="2"/><circle cx="300" cy="80" r="5" fill="#5a3a1a"/><circle cx="315" cy="80" r="5" fill="#5a3a1a"/><circle cx="330" cy="80" r="5" fill="#5a3a1a"/><path d="M300 108 l8 -14 l8 14z" fill="none" stroke="#5a3a1a" stroke-width="2"/>'
    s += '<text x="295" y="150" text-anchor="middle" font-weight="bold">2. Pictures and numbers</text><text x="295" y="166" text-anchor="middle" font-size="11">pressed into tablets, Uruk,</text><text x="295" y="180" text-anchor="middle" font-size="11">about 3300 to 3200 BCE</text>'
    s += '<path d="M370 90 h30" stroke="#0A1F3D" stroke-width="2"/><path d="M396 85 l8 5 l-8 5" fill="#0A1F3D"/>'
    s += '<rect x="425" y="50" width="170" height="80" rx="10" fill="#d9a873" stroke="#7a4a1f" stroke-width="2"/>'
    for i, (x, y, r) in enumerate([(445, 70, 0), (470, 70, 0), (500, 70, 90), (530, 72, 0), (560, 70, 45), (450, 100, 90), (480, 100, 0), (510, 100, 0), (540, 102, 90), (570, 100, 0)]):
        s += f'<g transform="rotate({r} {x} {y})"><path d="M{x-6} {y-8} l12 0 l-6 10z" fill="#5a3a1a"/><path d="M{x} {y+2} v12" stroke="#5a3a1a" stroke-width="2"/></g>'
    s += '<text x="510" y="150" text-anchor="middle" font-weight="bold">3. Cuneiform</text><text x="510" y="166" text-anchor="middle" font-size="11">wedges pressed with a reed;</text><text x="510" y="180" text-anchor="middle" font-size="11">used for about 3,000 years</text>'
    s += '<text x="320" y="204" text-anchor="middle" font-size="10" fill="#5b6676">Signs simplified for the drawing. The token idea is a respected theory that some scholars question.</text></svg>'
    return s

NUMS = ('<svg viewBox="0 0 640 172" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" xmlns:xlink="http://www.w3.org/1999/xlink" role="img" aria-label="Babylonian cuneiform numbers">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Writing numbers in cuneiform</text>'
  '<defs><g id="one"><path d="M-6 0 l12 0 l-6 9z" fill="#5a3a1a"/><path d="M0 8 v18" stroke="#5a3a1a" stroke-width="2.5"/></g>'
  '<g id="ten"><path d="M8 -9 l-14 9 l14 9" fill="none" stroke="#5a3a1a" stroke-width="3"/><path d="M8 -9 l-4 9 l4 9z" fill="#5a3a1a"/></g></defs>'
  '<rect x="20" y="36" width="600" height="96" rx="8" fill="#f3e2c3"/>'
  '<use xlink:href="#one" href="#one" x="70" y="62"/><text x="70" y="118" text-anchor="middle" font-weight="bold">1</text>'
  '<use xlink:href="#one" href="#one" x="140" y="62"/><use xlink:href="#one" href="#one" x="155" y="62"/><use xlink:href="#one" href="#one" x="170" y="62"/><text x="155" y="118" text-anchor="middle" font-weight="bold">3</text>'
  '<use xlink:href="#ten" href="#ten" x="250" y="74"/><text x="250" y="118" text-anchor="middle" font-weight="bold">10</text>'
  '<use xlink:href="#ten" href="#ten" x="320" y="74"/><use xlink:href="#ten" href="#ten" x="340" y="74"/><use xlink:href="#one" href="#one" x="368" y="62"/><use xlink:href="#one" href="#one" x="383" y="62"/><text x="350" y="118" text-anchor="middle" font-weight="bold">22</text>'
  '<use xlink:href="#one" href="#one" x="460" y="62"/><use xlink:href="#ten" href="#ten" x="490" y="74"/><use xlink:href="#one" href="#one" x="518" y="62"/><use xlink:href="#one" href="#one" x="533" y="62"/><text x="495" y="118" text-anchor="middle" font-weight="bold">72 = one 60 + 12</text>'
  '<text x="320" y="150" text-anchor="middle" font-size="11">A vertical wedge means 1. A corner wedge means 10. Mesopotamians counted in groups of 60,</text>'
  '<text x="320" y="164" text-anchor="middle" font-size="11">which is why an hour has 60 minutes. In 72, the wedge on the left stands for one group of 60.</text></svg>')

LESSON = {'unit': 'Unit 3: Ancient Asia',
 'title': 'Mesopotamia and the First Writing',
 'subtitle': "Between the Tigris and Euphrates rivers, the people of Sumer built some of the world's first cities, created cuneiform writing and gave us the 60-minute hour.",
 'objectives': ['Locate Mesopotamia, the Tigris and Euphrates rivers and the cities of Sumer on a map.',
                'Compare how Mesopotamians and Egyptians lived with their rivers.',
                'Explain how writing developed in Mesopotamia from record keeping to literature.',
                'Describe the contributions of Enheduanna, Hammurabi and the Epic of Gilgamesh.',
                "Write numbers in cuneiform and explain Mesopotamia's base-60 legacy."],
 'vocab': [['Mesopotamia', 'Greek for "land between the rivers"; the region of the Tigris and Euphrates, mostly in today\'s Iraq.'],
           ['Sumer', "The southern part of Mesopotamia, home to some of the world's earliest cities."],
           ['city-state', 'A city and the farmland around it with its own ruler and government.'],
           ['cuneiform', 'Writing made of wedge-shaped marks pressed into clay; from the Latin cuneus, "wedge."'],
           ['scribe', 'A person trained to read and write, who kept records.'],
           ['ziggurat', 'A stepped temple tower built of mud brick at the center of a Mesopotamian city.'],
           ['code of law', 'A written set of laws that applies to everyone in a society.'],
           ['base 60', 'A number system that counts in groups of 60.']],
 'reconnect': {'title': "Week 10: The Nile Valley's gifts",
               'intro': 'Unit 3 moves east to Asia. First, connect back to the Nile Valley.',
               'items': [{'t': 'text',
                          'q': 'Which Egyptian hieroglyph became the letter A: an ox head, a reed or an eye?',
                          'a': [{'all': [['ox']], 'none': ['not', 'reed', 'eye']}],
                          'show': 'an ox head',
                          'pts': 2,
                          'why': "The ox-head sign became Proto-Sinaitic 'alp, Phoenician aleph, Greek alpha and Latin A."},
                         {'t': 'num',
                          'q': "Kemet's civil calendar had 12 months of 30 days. How many days were in those 12 months, before the 5 extra days?",
                          'a': 360,
                          'unit': 'days',
                          'pts': 2,
                          'why': '12 × 30 = 360. Today you will meet another people who loved the numbers 60 and 360.'},
                         {'t': 'open',
                          'key': 'rc_nile',
                          'q': "In Week 6, you learned that the Nile flooded at about the same time every year. Why was that regular, predictable flood helpful to Kemet's farmers?",
                          'min': 15,
                          'rows': 2,
                          'rubric': ['Farmers could plan planting and harvest; the flood brought water and silt on schedule'],
                          'model': 'Farmers knew when the water and fresh silt would come, so they could plan when to plant and harvest.'},
                         {'t': 'open',
                          'key': 'rc_diffusion',
                          'q': 'In your own words, what is cultural diffusion? Give an example from Unit 2.',
                          'min': 15,
                          'rows': 2,
                          'rubric': ['Ideas spreading between cultures and being adapted', 'An accurate example (the alphabet; Kush borrowing Egyptian gods)'],
                          'model': 'Cultural diffusion is when ideas spread from one culture to another and change along the way, like the alphabet moving from Egypt to the Phoenicians and '
                                   'Greeks.'}]},
 'hook': {'title': 'A Receipt from 5,000 Years Ago',
          'visual': '<svg viewBox="0 0 631 413" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Map of Mesopotamia with the Tigris and Euphrates '
                    'rivers"><text x="315.5" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Mesopotamia: the land between the rivers</text><rect x="20" y="34" '
                    'width="425.0" height="357.0" fill="#efe1bd"/><polygon points="377.0,324.7 360.0,343.4 373.6,374.0 390.6,391.0 445.0,391.0 445.0,336.6 428.0,319.6 400.8,316.2" '
                    'fill="#bfe3f5"/><polyline points="40.4,37.4 30.2,85.0 26.8,119.0 84.6,142.8 118.6,170.0 156.0,173.4 200.2,207.4 234.2,234.6 264.8,258.4 300.8,287.3 340.6,289.0" fill="none" '
                    'stroke="#0047BA" stroke-width="3" stroke-linejoin="round"/><polyline points="94.8,54.4 145.8,74.8 179.8,88.4 194.4,107.4 200.2,136.0 217.2,166.6 236.6,210.5 258.0,227.8 '
                    '285.2,238.0 322.6,258.4 340.6,289.0" fill="none" stroke="#0047BA" stroke-width="3" stroke-linejoin="round"/><polyline points="340.6,289.0 353.2,306.0 377.0,324.7" fill="none" '
                    'stroke="#0047BA" stroke-width="3"/><text x="108.4" y="156.4" font-size="11" fill="#0047BA" font-style="italic" transform="rotate(25 108.4 156.4)">Euphrates</text><text x="210.4" '
                    'y="139.4" font-size="11" fill="#0047BA" font-style="italic" transform="rotate(70 210.4 139.4)">Tigris</text><text x="390.6" y="357.0" font-size="11" fill="#0047BA" '
                    'font-style="italic">Persian Gulf</text><text x="319.2" y="132.6" font-size="10" fill="#8a6d1f" font-weight="bold">ZAGROS MOUNTAINS</text><text x="40.4" y="234.6" font-size="10" '
                    'fill="#8a6d1f" font-weight="bold">SYRIAN DESERT</text><text x="244.4" y="255.0" font-size="12" font-weight="bold" fill="#DB2F30" '
                    'style="paint-order:stroke;stroke:#efe1bd;stroke-width:4">SUMER</text><circle cx="195.1" cy="106.8" r="4" fill="#0A1F3D" stroke="#0A1F3D" stroke-width="1.5"/><path d="M200.1 '
                    '106.8 L457.0 106.8" stroke="#8a8f99" stroke-width=".8"/><text x="461.0" y="110.8" font-size="11">Nineveh</text><circle cx="236.6" cy="210.5" r="4" fill="#fff" stroke="#0A1F3D" '
                    'stroke-width="1.5"/><path d="M241.6 210.5 L457.0 210.5" stroke="#8a8f99" stroke-width=".8"/><text x="461.0" y="214.5" font-size="11">Baghdad (modern capital of '
                    'Iraq)</text><circle cx="238.3" cy="236.6" r="4" fill="#0A1F3D" stroke="#0A1F3D" stroke-width="1.5"/><path d="M243.3 236.6 L457.0 236.6" stroke="#8a8f99" stroke-width=".8"/><text '
                    'x="461.0" y="240.6" font-size="11">Babylon</text><circle cx="305.9" cy="275.1" r="4" fill="#0A1F3D" stroke="#0A1F3D" stroke-width="1.5"/><path d="M310.9 275.1 L457.0 275.1" '
                    'stroke="#8a8f99" stroke-width=".8"/><text x="461.0" y="279.1" font-size="11">Lagash</text><circle cx="279.8" cy="278.1" r="4" fill="#0A1F3D" stroke="#0A1F3D" '
                    'stroke-width="1.5"/><path d="M284.8 278.1 L457.0 294.1" stroke="#8a8f99" stroke-width=".8"/><text x="461.0" y="298.1" font-size="11">Uruk</text><circle cx="295.4" cy="290.4" '
                    'r="4" fill="#0A1F3D" stroke="#0A1F3D" stroke-width="1.5"/><path d="M300.4 290.4 L457.0 313.1" stroke="#8a8f99" stroke-width=".8"/><text x="461.0" y="317.1" '
                    'font-size="11">Ur</text><text x="20" y="407" font-size="10" fill="#5b6676">Rivers follow their modern courses; in ancient times the Euphrates flowed closer to Ur and Uruk. Open '
                    'circle: modern city.</text></svg>',
          'html': '<p>Around 3100 BCE, in the city of Uruk in what is now southern Iraq, an official pressed a reed into a soft clay tablet. The marks recorded how much barley had been given out to '
                  "workers. A tablet like this may be one of the world's first written documents. It was not a poem or a story. It was a receipt.</p><p>The people of <b>Sumer</b> lived in "
                  '<b>Mesopotamia</b>, "the land between the rivers," the Tigris and the Euphrates. There, they built some of the world\'s first cities, temple towers called ziggurats and a system '
                  "of writing that lasted about 3,000 years.</p><div class='callout'><b>Big question:</b> Why did people first start to write, and how did writing change their world?</div>"},
 'learn': [{'title': 'Two Rivers, Two Ways of Life',
            'html': '<p>Like Kemet, Mesopotamia depended on rivers in a dry land. But the Tigris and Euphrates behaved very differently from the Nile. They flooded in spring, often violently and '
                    'unpredictably, sometimes washing away fields and villages. Farmers had to dig and constantly repair long <b>irrigation canals</b> and levees to control the water and carry it to '
                    "their fields.</p><p>All that digging and repair required people to work together, which helped build some of the world's first cities, such as Uruk, Ur and Lagash. By about 2900 "
                    'BCE, Uruk may have held tens of thousands of people. Each <b>city-state</b> had its own ruler and its own god, and the cities often fought over water and land.</p><p>Mesopotamia '
                    'also had few natural resources besides mud, reeds and fertile soil: no good stone, little timber and no metal ores. Its people traded grain and cloth for copper, tin, timber and '
                    'stone from distant lands, including the Indus Valley, which you will study next week.</p>',
            'checks': [{'t': 'open',
                        'key': 'rivers',
                        'q': 'Compare the floods of the Nile with the floods of the Tigris and Euphrates. How did each shape the way people farmed and lived?',
                        'min': 35,
                        'rows': 4,
                        'rubric': ['Nile: regular, predictable yearly flood that farmers could plan around',
                                   'Tigris and Euphrates: unpredictable, often violent spring floods',
                                   'Mesopotamians built and repaired canals and levees, which required cooperation and helped create cities'],
                        'model': 'The Nile flooded gently at about the same time every year, so Egyptian farmers could plan around it. The Tigris and Euphrates flooded unpredictably and sometimes '
                                 'violently, so Mesopotamian farmers had to build and constantly repair canals and levees. That shared work brought people together and helped create cities.'},
                       {'t': 'open',
                        'key': 'trade',
                        'q': 'Mesopotamia had plenty of mud and reeds but little stone, timber or metal. How did that shortage lead to trade, and what did Mesopotamians build with instead?',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Traded grain and cloth for copper, tin, timber and stone from distant lands', 'Built with mud brick and reeds (ziggurats, houses); wrote on clay'],
                        'model': 'Because they lacked stone, timber and metal, they traded their extra grain and cloth for those goods from faraway places. At home they built with mud brick and '
                                 'reeds, even their giant ziggurats, and they wrote on clay.'},
                       {'t': 'text',
                        'q': 'What does the Greek name Mesopotamia mean?',
                        'a': [{'all': [['between'], ['river']], 'none': ['not']}],
                        'show': 'land between the rivers',
                        'pts': 2,
                        'why': 'meso (middle, between) + potamos (river).'}]},
           {'title': 'How Writing Began',
            'visual': '<svg viewBox="0 0 640 210" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="How writing developed from tokens to cuneiform"><text '
                      'x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">From counting tokens to cuneiform</text><g transform="translate(40,60)"><circle cx="20" '
                      'cy="30" r="12" fill="#c98f58" stroke="#7a4a1f"/><path d="M50 42 l12 -24 l12 24z" fill="#c98f58" stroke="#7a4a1f"/><rect x="82" y="20" width="22" height="22" rx="3" '
                      'fill="#c98f58" stroke="#7a4a1f"/></g><text x="105" y="140" text-anchor="middle" font-weight="bold">1. Clay tokens</text><text x="105" y="156" text-anchor="middle" '
                      'font-size="11">each shape = a good</text><text x="105" y="170" text-anchor="middle" font-size="11">(from about 8000 BCE)</text><path d="M180 90 h30" stroke="#0A1F3D" '
                      'stroke-width="2"/><path d="M206 85 l8 5 l-8 5" fill="#0A1F3D"/><rect x="235" y="50" width="120" height="80" rx="10" fill="#d9a873" stroke="#7a4a1f" stroke-width="2"/><path '
                      'd="M255 100 q10 -30 20 0 M262 90 h6" fill="none" stroke="#5a3a1a" stroke-width="2"/><circle cx="300" cy="80" r="5" fill="#5a3a1a"/><circle cx="315" cy="80" r="5" '
                      'fill="#5a3a1a"/><circle cx="330" cy="80" r="5" fill="#5a3a1a"/><path d="M300 108 l8 -14 l8 14z" fill="none" stroke="#5a3a1a" stroke-width="2"/><text x="295" y="150" '
                      'text-anchor="middle" font-weight="bold">2. Pictures and numbers</text><text x="295" y="166" text-anchor="middle" font-size="11">pressed into tablets, Uruk,</text><text x="295" '
                      'y="180" text-anchor="middle" font-size="11">about 3300 to 3200 BCE</text><path d="M370 90 h30" stroke="#0A1F3D" stroke-width="2"/><path d="M396 85 l8 5 l-8 5" '
                      'fill="#0A1F3D"/><rect x="425" y="50" width="170" height="80" rx="10" fill="#d9a873" stroke="#7a4a1f" stroke-width="2"/><g transform="rotate(0 445 70)"><path d="M439 62 l12 0 '
                      'l-6 10z" fill="#5a3a1a"/><path d="M445 72 v12" stroke="#5a3a1a" stroke-width="2"/></g><g transform="rotate(0 470 70)"><path d="M464 62 l12 0 l-6 10z" fill="#5a3a1a"/><path '
                      'd="M470 72 v12" stroke="#5a3a1a" stroke-width="2"/></g><g transform="rotate(90 500 70)"><path d="M494 62 l12 0 l-6 10z" fill="#5a3a1a"/><path d="M500 72 v12" stroke="#5a3a1a" '
                      'stroke-width="2"/></g><g transform="rotate(0 530 72)"><path d="M524 64 l12 0 l-6 10z" fill="#5a3a1a"/><path d="M530 74 v12" stroke="#5a3a1a" stroke-width="2"/></g><g '
                      'transform="rotate(45 560 70)"><path d="M554 62 l12 0 l-6 10z" fill="#5a3a1a"/><path d="M560 72 v12" stroke="#5a3a1a" stroke-width="2"/></g><g transform="rotate(90 450 '
                      '100)"><path d="M444 92 l12 0 l-6 10z" fill="#5a3a1a"/><path d="M450 102 v12" stroke="#5a3a1a" stroke-width="2"/></g><g transform="rotate(0 480 100)"><path d="M474 92 l12 0 l-6 '
                      '10z" fill="#5a3a1a"/><path d="M480 102 v12" stroke="#5a3a1a" stroke-width="2"/></g><g transform="rotate(0 510 100)"><path d="M504 92 l12 0 l-6 10z" fill="#5a3a1a"/><path '
                      'd="M510 102 v12" stroke="#5a3a1a" stroke-width="2"/></g><g transform="rotate(90 540 102)"><path d="M534 94 l12 0 l-6 10z" fill="#5a3a1a"/><path d="M540 104 v12" '
                      'stroke="#5a3a1a" stroke-width="2"/></g><g transform="rotate(0 570 100)"><path d="M564 92 l12 0 l-6 10z" fill="#5a3a1a"/><path d="M570 102 v12" stroke="#5a3a1a" '
                      'stroke-width="2"/></g><text x="510" y="150" text-anchor="middle" font-weight="bold">3. Cuneiform</text><text x="510" y="166" text-anchor="middle" font-size="11">wedges pressed '
                      'with a reed;</text><text x="510" y="180" text-anchor="middle" font-size="11">used for about 3,000 years</text><text x="320" y="204" text-anchor="middle" font-size="10" '
                      'fill="#5b6676">Signs simplified for the drawing. The token idea is a respected theory that some scholars question.</text></svg>',
            'html': '<p>Why did people start writing? In Mesopotamia, the first reason was <b>keeping track</b>. Temples collected and handed out huge amounts of grain, beer, sheep and cloth, and '
                    'officials needed records.</p><p>Archaeologist <b>Denise Schmandt-Besserat</b> proposed that writing grew out of small clay <b>tokens</b>, each shape standing for a good, used '
                    'for counting for thousands of years. Around 3300 to 3200 BCE, scribes in Uruk began pressing pictures and number signs into clay tablets. Over centuries, the pictures became '
                    'simpler groups of wedge-shaped marks, made by pressing a cut reed into clay. We call this <b>cuneiform</b>.</p><p>Writing soon did much more than count. Scribes recorded laws, '
                    'letters, prayers, medicine, astronomy and stories. Cuneiform was used for about 3,000 years and adapted to write more than a dozen languages, including Sumerian, Akkadian and '
                    'Hittite.</p><p>At almost the same time, Egyptians were developing hieroglyphs, and the earliest Egyptian writing may be just as old. Most scholars think the two systems were '
                    'invented separately: two peoples solving the same problem. Writing was later invented independently in China and in Mesoamerica too.</p>',
            'checks': [{'t': 'open',
                        'key': 'whywrite',
                        'q': 'Why did writing begin in Mesopotamia? What does that tell you about what early cities needed?',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['To keep records of goods (grain, beer, sheep, cloth) collected and handed out by temples',
                                   'Cities had large economies and many people to organize, so they needed records'],
                        'model': 'Writing began as a way to keep records of grain, beer, sheep and cloth that temples collected and gave out. That shows early cities had so many people and goods '
                                 'that no one could remember everything, so they needed a reliable way to keep track.'},
                       {'t': 'open',
                        'key': 'first',
                        'q': 'Who invented writing first, Mesopotamia or Egypt? Explain why historians are careful with this question.',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Both developed writing at about the same time (about 3300 to 3200 BCE); the evidence is close',
                                   'Dating is uncertain and new finds can change the picture; most think they were invented independently'],
                        'model': 'Historians are not sure, because the earliest writing from both places dates to about the same time, and dates for clay tablets and labels are uncertain. A new '
                                 'discovery could change the answer. Most scholars think each invented writing on its own.'},
                       {'t': 'text',
                        'q': 'From which Latin word, meaning "wedge," does cuneiform get its name?',
                        'a': ['cuneus'],
                        'show': 'cuneus',
                        'pts': 2,
                        'why': 'Cuneus means wedge: cuneiform is "wedge-shaped" writing.'}]},
           {'title': 'Voices in Clay: Enheduanna, Gilgamesh and Hammurabi',
            'html': '<p><b>Enheduanna</b>, the daughter of King Sargon of Akkad, served as high priestess of the moon god at Ur around 2300 BCE. She wrote hymns to the goddess Inanna and signed her '
                    'name to them. She is often called the earliest author in history known by name, more than 1,500 years before Homer. The copies of her hymns that survive were made centuries '
                    'after she lived, so scholars still debate how many she wrote herself.</p><p>The <b>Epic of Gilgamesh</b> tells of a proud king of Uruk who loses his best friend, Enkidu, and '
                    "travels to the ends of the earth searching for a way to live forever. He fails, but returns home wiser. Its oldest parts are about 4,000 years old, making it one of the world's "
                    'oldest great works of literature.</p><p>Around 1754 BCE, King <b>Hammurabi</b> of Babylon had 282 laws carved on a tall black stone pillar and set up for people to see. The laws '
                    'covered trade, wages, farming, families and crimes. Some punishments followed the rule "an eye for an eye," but punishments were harsher or lighter depending on whether a person '
                    "was a noble, a free commoner or enslaved. Hammurabi's code was not the first. An older law code, of King Ur-Nammu of Ur, is about 300 years earlier. But Hammurabi's pillar, now "
                    "in the Louvre museum in Paris, is the most complete. An Elamite king carried the pillar off to Susa, in today's Iran, around 1150 BCE, and French archaeologists dug it up there "
                    'in 1901. Today Iraqi archaeologists and the Iraq Museum in Baghdad care for many Mesopotamian treasures, and in 2021 the United States returned the stolen Gilgamesh Dream Tablet '
                    'to Iraq.</p><div class=\'card\'><b>Primary source: three of Hammurabi\'s laws</b> (translated by L. W. King, 1910; King\'s "freed man" means a free commoner)<br>196. If a man '
                    'put out the eye of another man, his eye shall be put out.<br>198. If he put out the eye of a freed man, or break the bone of a freed man, he shall pay one gold mina.<br>199. If '
                    "he put out the eye of a man's slave, or break the bone of a man's slave, he shall pay one-half of its value.</div>",
            'checks': [{'t': 'open',
                        'key': 'enhed',
                        'q': 'Why is Enheduanna important in world history? What does her story tell us about women in early Mesopotamia?',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Earliest known named author; wrote hymns to Inanna; high priestess at Ur', 'At least some elite women held religious power and were educated writers'],
                        'model': 'Enheduanna is the earliest author whose name we know. As high priestess at Ur, she wrote hymns to Inanna, which shows that at least some royal women in Mesopotamia '
                                 'were educated and held real religious power.'},
                       {'t': 'open',
                        'key': 'laws',
                        'q': 'Read Laws 196, 198 and 199. What happens to the attacker in each case, and what do the three laws show about how Babylon treated people of different classes?',
                        'min': 30,
                        'rows': 3,
                        'rubric': ["196: eye for an eye (equal noble); 198: pays one gold mina (commoner victim); 199: pays half the slave's value (to the owner)",
                                   "The punishment depended on the victim's class; enslaved people were treated as property"],
                        'model': 'If the victim was a noble, the attacker lost his own eye. If the victim was a commoner, the attacker paid one gold mina. If the victim was enslaved, the attacker '
                                 "paid half the slave's value, as if the person were property. The laws show that a person's class decided how much the law protected them."},
                       {'t': 'open',
                        'key': 'hammurabi',
                        'q': "Writing laws down and displaying them publicly was a big change. Give one way this made life fairer and one way Hammurabi's laws were still unequal.",
                        'min': 30,
                        'rows': 3,
                        'rubric': ['Fairer: people could know the laws; judges could not simply make up rules; same law for everyone in a class',
                                   'Unequal: punishments depended on social class (noble, commoner, enslaved)'],
                        'model': 'Because the laws were written and displayed, people could know the rules ahead of time, and judges could not just invent them. But the laws were still unequal: the '
                                 'punishment for the same crime depended on whether the victim was a noble, a commoner or an enslaved person.'},
                       {'t': 'open',
                        'key': 'gilgamesh',
                        'q': 'Gilgamesh searches for a way to live forever and fails, but comes home wiser. What theme might this ancient story share with stories today?',
                        'min': 20,
                        'rows': 2,
                        'rubric': ['A theme statement (not a topic): e.g. accepting that life ends and making it meaningful; friendship and loss; wisdom comes from struggle'],
                        'model': 'The theme might be that no one can escape death, so what matters is how we live and the good we leave behind. Many modern stories share that idea.'}]},
           {'title': 'Counting by 60',
            'visual': '<svg viewBox="0 0 640 172" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" xmlns:xlink="http://www.w3.org/1999/xlink" role="img" aria-label="Babylonian '
                      'cuneiform numbers"><text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Writing numbers in cuneiform</text><defs><g id="one"><path d="M-6 '
                      '0 l12 0 l-6 9z" fill="#5a3a1a"/><path d="M0 8 v18" stroke="#5a3a1a" stroke-width="2.5"/></g><g id="ten"><path d="M8 -9 l-14 9 l14 9" fill="none" stroke="#5a3a1a" '
                      'stroke-width="3"/><path d="M8 -9 l-4 9 l4 9z" fill="#5a3a1a"/></g></defs><rect x="20" y="36" width="600" height="96" rx="8" fill="#f3e2c3"/><use xlink:href="#one" href="#one" '
                      'x="70" y="62"/><text x="70" y="118" text-anchor="middle" font-weight="bold">1</text><use xlink:href="#one" href="#one" x="140" y="62"/><use xlink:href="#one" href="#one" '
                      'x="155" y="62"/><use xlink:href="#one" href="#one" x="170" y="62"/><text x="155" y="118" text-anchor="middle" font-weight="bold">3</text><use xlink:href="#ten" href="#ten" '
                      'x="250" y="74"/><text x="250" y="118" text-anchor="middle" font-weight="bold">10</text><use xlink:href="#ten" href="#ten" x="320" y="74"/><use xlink:href="#ten" href="#ten" '
                      'x="340" y="74"/><use xlink:href="#one" href="#one" x="368" y="62"/><use xlink:href="#one" href="#one" x="383" y="62"/><text x="350" y="118" text-anchor="middle" '
                      'font-weight="bold">22</text><use xlink:href="#one" href="#one" x="460" y="62"/><use xlink:href="#ten" href="#ten" x="490" y="74"/><use xlink:href="#one" href="#one" x="518" '
                      'y="62"/><use xlink:href="#one" href="#one" x="533" y="62"/><text x="495" y="118" text-anchor="middle" font-weight="bold">72 = one 60 + 12</text><text x="320" y="150" '
                      'text-anchor="middle" font-size="11">A vertical wedge means 1. A corner wedge means 10. Mesopotamians counted in groups of 60,</text><text x="320" y="164" text-anchor="middle" '
                      'font-size="11">which is why an hour has 60 minutes. In 72, the wedge on the left stands for one group of 60.</text></svg>',
            'html': '<p>Mesopotamian scribes counted in groups of 60 instead of groups of 10. This is called <b>base 60</b>. A vertical wedge meant 1 and a corner-shaped wedge meant 10. To write 22, '
                    'a scribe pressed two tens and two ones. To write 72, a scribe wrote one 60 in the next place, then 12.</p><p>Why 60? It can be divided evenly by 1, 2, 3, 4, 5, 6, 10, 12, 15, 20 '
                    'and 30, which makes fractions easy. You still use their system every day: 60 seconds in a minute, 60 minutes in an hour, and 360 degrees in a circle.</p>',
            'checks': [{'t': 'num',
                        'q': 'How many corner wedges (tens) and vertical wedges (ones) does it take to write 47? Type the total number of wedges.',
                        'a': 11,
                        'unit': 'wedges',
                        'pts': 2,
                        'why': '47 = 4 tens + 7 ones: 4 corner wedges and 7 vertical wedges, 11 wedges in all.'},
                       {'t': 'num', 'q': 'A scribe writes one wedge in the 60s place and 2 tens and 5 ones in the ones place. What number is it?', 'a': 85, 'pts': 3, 'why': '1 × 60 + 25 = 85.'},
                       {'t': 'open',
                        'key': 'why60',
                        'q': 'Explain why 60 is a useful number for dividing things fairly, using an example of sharing 60 loaves of bread.',
                        'min': 20,
                        'rows': 2,
                        'rubric': ['60 has many factors (2, 3, 4, 5, 6, 10, 12, 15, 20, 30)', 'Example: 60 loaves can be shared evenly among 2, 3, 4, 5 or 6 people'],
                        'model': '60 has many factors, so 60 loaves can be shared evenly among 2, 3, 4, 5, 6, 10 or 12 families without breaking a loaf. With 10 loaves, only 2, 5 or 10 families '
                                 'could share evenly.'}]}],
 'handson': {'title': 'Write a Clay Receipt in Cuneiform',
             'intro': 'Become a Sumerian scribe. Use a reed-like tool to press wedges into clay, just as scribes did 5,000 years ago.',
             'materials': ['Air-dry clay, modeling clay or play dough (a piece the size of your palm)',
                           'A square-ended chopstick or the corner of a ruler (press a corner in at an angle to make a wedge). For a sharper wedge, an adult trims a popsicle stick to a point with a '
                           'craft knife or sandpaper; the student does not use the knife.',
                           'A rolling pin or a smooth glass',
                           'Paper and pencil',
                           'Optional: a phone to photograph your tablet'],
             'steps': ['Roll the clay into a flat tablet about the size of your palm and 1 cm thick.',
                       "Practice the two wedges on the edge: press the tool's corner straight in for a vertical wedge (1), and at an angle for a corner wedge (10).",
                       'Write a receipt: choose three goods your family uses (for example, eggs, apples and bread) and record a real or made-up quantity of each in cuneiform numbers, with a small '
                       'picture sign for each good.',
                       "On the back, press a symbol to stand for your name, like a scribe's seal.",
                       'Trade tablets with a family member and see if they can read the numbers using the number chart.',
                       'Clay and play dough are not food: do not taste them, wash your hands afterward, and keep play dough away from pets (salty dough can make dogs very sick).'],
             'record': [{'t': 'open',
                         'key': 'tabletrec',
                         'q': 'What three goods and amounts did you record? Draw or describe how you wrote each number in wedges.',
                         'min': 19,
                         'rows': 4,
                         'rubric': ['Three goods with amounts', 'Correct tens and ones wedges for each number'],
                         'model': 'Eggs, 24: two corner wedges and four vertical wedges. Apples, 13: one corner wedge and three vertical wedges. Bread, 6: six vertical wedges.'},
                        {'t': 'open',
                         'key': 'tabletreflect',
                         'q': 'What was hard about writing in clay? Why do you think scribes trained for years, and why might writing have given scribes power?',
                         'min': 37,
                         'rows': 4,
                         'rubric': ['A real difficulty (clay dries, wedges smudge, small space, signs must be precise)',
                                    'Writing took years to learn; few people could read, so scribes controlled records, laws and messages'],
                         'model': 'The wedges smudged when I touched the clay, and it was hard to fit everything. Scribes needed years of school to learn hundreds of signs. Since very few people '
                                  'could read, scribes controlled the records, letters and laws, which gave them power and respect.'}]},
 'think': {'intro': 'Use evidence and explain your reasoning. Your teacher scores these.',
           'items': [{'t': 'open',
                      'key': 'writingchange',
                      'q': 'Write a paragraph explaining how writing changed Mesopotamian society. Include at least three different uses of writing from the lesson and explain why each mattered.',
                      'min': 78,
                      'rows': 10,
                      'rubric': ['Three accurate uses (record keeping, laws, literature, religion, letters, science)',
                                 'Explains why each mattered',
                                 'Organized paragraph with a topic sentence and transitions'],
                      'model': 'Writing changed Mesopotamia from a world that depended on memory into one that could keep records forever. First, scribes kept track of grain, beer and sheep, which '
                               'helped temples and cities organize thousands of people. Next, rulers like Hammurabi wrote laws on public pillars, so people could know the rules and judges had a '
                               "standard to follow. Writing also preserved literature and religion, from Enheduanna's hymns to the Epic of Gilgamesh, so ideas could pass from one generation to the "
                               'next. Because of writing, knowledge no longer disappeared when a person died.'},
                     {'t': 'open',
                      'key': 'compare',
                      'q': 'Compare Mesopotamia and Kemet. Give two similarities and two differences, using evidence from Unit 2 and this lesson.',
                      'min': 52,
                      'rows': 7,
                      'rubric': ['Two accurate similarities (river valleys, writing around the same time, temples and kings, farming with irrigation)',
                                 'Two accurate differences (flood patterns, building materials, many city-states versus a unified kingdom, natural resources)',
                                 'Specific evidence'],
                      'model': 'Both civilizations grew along rivers in dry lands, and both developed writing around 3200 BCE. However, the Nile flooded predictably, while the Tigris and Euphrates '
                               'flooded unpredictably and needed constant canal work. Kemet was united under one king around 3100 BCE, while Sumer was made up of rival city-states. Kemet also had '
                               'good stone for pyramids, while Mesopotamia built with mud brick.'}]},
 'exit': [{'t': 'text',
           'q': 'Name the two rivers of Mesopotamia.',
           'a': [{'all': [['tigris', 'tigres'], ['euphrat', 'eufrat', 'euphret']], 'none': ['not']}],
           'show': 'the Tigris and the Euphrates',
           'pts': 2,
           'why': 'The Tigris and the Euphrates.'},
          {'t': 'open',
           'key': 'exit_first',
           'q': 'What was the first purpose of writing in Mesopotamia?',
           'min': 8,
           'rows': 2,
           'rubric': ['Keeping records of goods (grain, beer, sheep, cloth)'],
           'model': 'To keep records of goods like grain, beer and sheep.'},
          {'t': 'text',
           'q': 'Who is often called the earliest author in history known by name?',
           'a': ['enheduanna', 'enheduana', 'en-hedu-anna'],
           'show': 'Enheduanna',
           'pts': 2,
           'why': 'Enheduanna, high priestess at Ur, about 2300 BCE.'},
          {'t': 'open',
           'key': 'exit_60',
           'q': 'Name one way you still use the Mesopotamian base-60 system today.',
           'min': 5,
           'rows': 1,
           'rubric': ['60 seconds in a minute, 60 minutes in an hour, or 360 degrees in a circle'],
           'model': 'There are 60 minutes in an hour.'}],
 'next': 'Week 12: the Indus Valley, with its planned cities, drains and a script no one has yet deciphered.'}

TEACHER = {
 "standards": [
  "SS.6.W.2.4: Compare the economic, political, social, and religious institutions of ancient river civilizations.",
  "SS.6.W.2.7: Summarize the important achievements of Mesopotamian civilization.",
  "SS.6.W.2.8: Determine the impact of key figures from ancient Mesopotamian civilizations.",
  "SS.6.G.2.1: Explain how major physical characteristics, natural resources, climate, and absolute and relative locations have influenced settlement, interactions, and the economies of ancient civilizations of the world.",
  "SS.6.W.1.3: Interpret primary and secondary sources."],
 "materials": ["The interactive lesson", "A world map or globe", "Air-dry clay or play dough, a chopstick or popsicle stick with a triangular end, a rolling pin or glass", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 10 Reconnect questions."],
  [5, "Hook", "Show the map. Find Iraq on a globe. Tell the story of the barley receipt."],
  [10, "Two rivers", "Compare the Nile's flood with the Tigris and Euphrates. Discuss canals and cooperation."],
  [12, "How writing began", "Walk through tokens, pictures and cuneiform. Discuss who invented writing first."],
  [12, "Voices in clay", "Enheduanna, Gilgamesh and Hammurabi. Debate whether Hammurabi's laws were fair."],
  [10, "Base 60", "Write numbers in wedges on paper. Connect to clocks and circles."],
  [5, "Assign", "Assign the clay tablet, Think Deeper and the Exit Check."]],
 "key_questions": ["Why did people need writing?", "How did the rivers shape the way people lived?", "Were Hammurabi's laws fair? Fair to whom?", "Where do you see Mesopotamia in your own life?"],
 "misconceptions": ["Writing was invented to tell stories (it began with record keeping).", "Hammurabi's code was the first law code (Ur-Nammu's is older).", "Mesopotamia and Egypt were the same kind of civilization.", "Mesopotamia is a modern country (it is a region, mostly in Iraq)."],
 "support": ["Provide a labeled map to keep.", "Give a cuneiform number chart for 1 to 59.", "Use a T-chart to compare the Nile and the Tigris and Euphrates."],
 "challenge": ["Read a short translated passage from the Epic of Gilgamesh (the flood story) and compare it with another flood story you know.", "Write 1 minute 25 seconds as seconds, then convert 85 seconds to minutes and seconds, and explain how base 60 helps."],
 "background": "<p>Proto-cuneiform tablets appear at Uruk (Uruk IV and III levels) about 3300 to 3000 BCE, chiefly administrative. Schmandt-Besserat's token theory (Before Writing, 1992) is influential but debated. Egyptian writing at Abydos tomb U-j dates to about 3250 BCE; independent invention is the mainstream view. Cuneiform was used until about the 1st century CE. Enheduanna (about 2285 to 2250 BCE), daughter of Sargon of Akkad, was en-priestess of Nanna at Ur. Hammurabi's stele (Louvre Sb 8, about 1754 BCE) has 282 laws by the conventional count; penalties vary by class (awilum, mushkenum, wardum). Ur-Nammu's code dates to about 2100 to 2050 BCE. The Gilgamesh texts include Old Babylonian versions (about 1800 BCE) and the Standard Babylonian version found at Nineveh. Babylonian numerals: vertical wedge 1, Winkelhaken 10, place value base 60.</p>",
 "sources": ["Schmandt-Besserat, D. (1996), How Writing Came About, University of Texas Press.", "The British Museum, Writing in Mesopotamia.", "Louvre Museum, Law Code of Hammurabi.", "Metropolitan Museum of Art, Heilbrunn Timeline: Uruk and Enheduanna.", "Finkel, I. and Taylor, J. (2015), Cuneiform, British Museum Press."]
}

PRINT = {
 "directions": "Use complete sentences and evidence.",
 "items": [
  {"q":"Sketch Mesopotamia: draw the Tigris and Euphrates and the Persian Gulf, and label Ur, Uruk and Babylon.","a":"Two rivers flowing southeast into the Persian Gulf; Ur and Uruk in the south (Sumer); Babylon farther north on the Euphrates.","lines":2},
  {"q":"How were the floods of the Tigris and Euphrates different from the Nile's?","a":"Unpredictable and often violent, so farmers built and repaired canals and levees.","lines":2},
  {"q":"Explain how writing developed in Mesopotamia.","a":"From counting tokens to pictures on clay tablets (about 3300 to 3200 BCE) to wedge-shaped cuneiform.","lines":2},
  {"q":"Who was Enheduanna?","a":"High priestess at Ur, daughter of Sargon, the earliest known named author.","lines":2},
  {"q":"Give one fair and one unfair feature of Hammurabi's code.","a":"Fair: written and public. Unfair: punishments depended on social class.","lines":2},
  {"q":"Write 34 in cuneiform (describe the wedges).","a":"3 corner wedges (30) and 4 vertical wedges (4).","lines":1}]
}
