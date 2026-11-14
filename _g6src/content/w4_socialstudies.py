from geo import world_map

CENTERS = world_map([(40, 36, 'Fertile Crescent', 6, -4), (112, 34, 'China', 6, -9), (145, -5.5, 'New Guinea', -6, 14), (-98, 19, 'Mesoamerica', -6, -4),
                     (-72, -13, 'Andes', 6, 4), (-86, 37, 'Eastern N. America', -6, -8), (-2, 14, 'West African Sahel', -6, 12), (36, 15.5, 'Sudan', -8, -8),
                     (39, 9, 'Ethiopian Highlands', 6, 20), (68, 29, 'Indus (Mehrgarh)', 6, 12)],
                    'Where people began farming, independently or early')

HOUSE = ('<svg viewBox="0 0 560 240" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Cutaway drawing of a Catalhoyuk house">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Çatalhöyük: houses packed wall to wall, entered through the roof</text>'
  '<rect x="20" y="80" width="520" height="140" fill="#e8d3a8" stroke="#8a6d1f"/>'
  + ''.join(f'<rect x="{x}" y="80" width="130" height="140" fill="{c}" stroke="#8a6d1f" stroke-width="3"/>' for x, c in [(20, '#e8d3a8'), (150, '#f1e0bd'), (280, '#e8d3a8'), (410, '#f1e0bd')]) +
  '<rect x="20" y="70" width="520" height="12" fill="#a9824a"/><circle cx="80" cy="52" r="5" fill="#0A1F3D"/><path d="M80 57 v8 M80 65 l-5 5 M80 65 l5 5 M74 60 h12" stroke="#0A1F3D" stroke-width="2"/><rect x="195" y="70" width="30" height="12" fill="#3b2a12"/>'
  '<line x1="205" y1="75" x2="185" y2="215" stroke="#5b3a12" stroke-width="3"/><line x1="220" y1="75" x2="200" y2="215" stroke="#5b3a12" stroke-width="3"/>'
  + ''.join(f'<line x1="{205-i*3}" y1="{95+i*20}" x2="{220-i*3}" y2="{95+i*20}" stroke="#5b3a12" stroke-width="2"/>' for i in range(6)) +
  '<rect x="240" y="180" width="30" height="34" fill="#c45c2a"/><text x="255" y="232" text-anchor="middle" font-size="10">oven</text>'
  '<rect x="160" y="196" width="28" height="18" fill="#cdb48a" stroke="#8a6d1f"/><text x="174" y="232" text-anchor="middle" font-size="10">platform</text>'
  '<path d="M290 120 q10 -20 20 0 q10 20 20 0" fill="none" stroke="#DB2F30" stroke-width="2"/><text x="345" y="112" font-size="10">wall paintings</text>'
  '<text x="110" y="40" text-anchor="middle" font-size="11">no streets: people walked</text><text x="110" y="54" text-anchor="start" font-size="11" dx="-20">across the rooftops</text>'
  '<text x="420" y="60" text-anchor="middle" font-size="11">ladder through a roof hole</text><path d="M360 62 L226 76" stroke="#0A1F3D"/></svg>')

FLOW = ('<svg viewBox="0 0 560 180" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Chain of effects from farming">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">One change leads to another</text>'
  + ''.join(f'<rect x="{10+i*110}" y="50" width="100" height="70" rx="10" fill="{c}"/><text x="{60+i*110}" y="80" text-anchor="middle" fill="#fff" font-weight="bold">{a}</text><text x="{60+i*110}" y="98" text-anchor="middle" fill="#fff" font-size="11">{b}</text>'
            + (f'<path d="M{110+i*110} 85 h10" stroke="#0A1F3D" stroke-width="2"/><path d="M{120+i*110} 85 l-5 -4 v8z" fill="#0A1F3D"/>' if i < 4 else '')
            for i, (a, b, c) in enumerate([("Farming", "planting, herding", "#0A1F3D"), ("Surplus", "extra food stored", "#0047BA"), ("More people", "villages grow", "#2f5a91"), ("Specialists", "potters, builders", "#C9A84C"), ("Trade and rules", "towns, leaders", "#DB2F30")])) +
  '<text x="280" y="150" text-anchor="middle" font-size="12">Every arrow is a cause and an effect. Historians ask which links were strongest, and who gained or lost.</text></svg>')

LESSON = {'unit': 'Unit 1: How We Know the Past',
 'title': 'Farming, Villages and the First Towns',
 'subtitle': 'For most of human history, people gathered and hunted their food. Then, in at least seven places on Earth, and perhaps more than a dozen, people began to farm on their own.',
 'objectives': ['Explain what domestication is and how it differs from gathering and hunting.',
                'Locate the places where farming began and recognize that it started independently on several continents, including Africa.',
                'Compare the lifestyles of hunter-gatherers and early farmers.',
                'Describe early towns such as Jericho and Çatalhöyük and the evidence historians use to study them.',
                'Analyze the chain of effects of farming, including its costs, and argue whether it was a good trade.'],
 'vocab': [['domestication', 'Changing plants or animals over many generations, by choosing which ones to grow or breed, so they become more useful to people.'],
           ['agriculture', 'Growing crops and raising animals for food and other products.'],
           ['Neolithic', 'The New Stone Age, when many people began farming and living in permanent villages.'],
           ['surplus', 'More than is needed right away; extra food that can be stored or traded.'],
           ['specialization', 'When people do one kind of work, such as making pottery, instead of all producing their own food.'],
           ['pastoralist', 'A person who raises herds of animals, often moving with them to find grass and water.'],
           ['settlement', 'A place where people live permanently.'],
           ['independent invention', 'When different groups develop the same idea on their own, without learning it from each other.']],
 'reconnect': {'title': 'Week 3: human beginnings in Africa',
               'intro': "This week's farmers were the descendants of the people you studied last week, so start by reviewing what you learned.",
               'items': [{'t': 'text',
                          'q': 'On which continent did <i>Homo sapiens</i> first appear?',
                          'a': ['africa'],
                          'pts': 2,
                          'why': 'The oldest known Homo sapiens fossils, from Jebel Irhoud in Morocco, are about 300,000 years old.'},
                         {'t': 'num', 'q': 'About how many years old are the Jebel Irhoud fossils?', 'a': 300000, 'unit': 'years', 'pts': 2, 'why': 'About 300,000 years.'},
                         {'t': 'text',
                          'q': 'In undisturbed layers of earth, are deeper layers usually older or younger?',
                          'a': ['older', 'older layers'],
                          'pts': 2,
                          'why': 'Layers pile up over time, so deeper usually means older (the law of superposition).'},
                         {'t': 'num',
                          'q': 'All humans share about what percent of their DNA?',
                          'a': 99.9,
                          'unit': '%',
                          'pts': 2,
                          'why': 'About 99.9%, which is why races are not separate biological groups.'},
                         {'t': 'open',
                          'key': 'rc_hunter',
                          'q': 'Describe how people got food for almost all of human history before farming. Give two specific examples.',
                          'min': 15,
                          'rows': 2,
                          'rubric': ['Gathering and hunting (or fishing)', 'Two concrete examples'],
                          'model': 'They gathered and hunted. For example, they collected wild seeds, fruits and shellfish, and hunted animals like antelope or fished in rivers and lakes.'},
                         {'t': 'open',
                          'key': 'rc_evidence',
                          'q': 'Name one kind of evidence from Week 3 that tells us early humans planned and made art, and explain what it shows.',
                          'min': 15,
                          'rows': 2,
                          'rubric': ['Names real evidence (Blombos ochre or beads, tools)', 'Explains what it shows about thinking'],
                          'model': 'At Blombos Cave in South Africa, people carved patterns into ochre about 75,000 years ago, which shows they used symbols and planned ahead.'}]},
 'hook': {'title': 'One Day in Two Worlds',
          'html': '<p>Imagine two families 10,000 years ago. The first family moves with the seasons, gathering wild grains, fruits and roots, hunting, and fishing. They carry everything they own. '
                  'The second family has stayed in one valley for years. They plant seeds, weed fields, guard their goats, and store grain in clay jars.</p><p>Which family works harder? Which eats '
                  "better? Which is healthier? The answers surprised historians and archaeologists, and they are still debated.</p><div class='callout'><b>Big idea:</b> Farming changed almost "
                  'everything about human life, but it was a trade, with real gains and real costs.</div>'},
 'learn': [{'title': 'Domestication: Changing Plants and Animals',
            'html': '<p>Wild wheat drops its seeds to the ground when ripe, which is perfect for the plant and terrible for a harvester. Over many generations, people kept replanting seeds from '
                    'plants whose seeds stayed on the stalk. Slowly, the plants changed. That is <b>domestication</b>.</p><p>The same happened with animals. People kept and bred the calmest goats, '
                    'sheep and cattle. In northeast Africa, some researchers argue that people were managing cattle at sites like Nabta Playa (from Week 1) as early as about 9,000 years ago, though '
                    'scientists still debate when those cattle became fully domesticated. As the Green Sahara dried after about 5,000 years ago, many archaeologists think herders from places like '
                    'Nabta Playa moved toward the Nile, where their descendants helped build Kemet and Nubia, which you will study in Unit 2.</p><p>Wild teosinte in Mexico had tiny ears with a '
                    'handful of hard kernels. Thousands of years of selection by farmers in Mesoamerica turned it into maize (corn).</p>',
            'checks': [{'t': 'open',
                        'key': 'select',
                        'q': 'Explain in your own words how farmers changed wild wheat without any modern science. Use the word <b>generations</b>.',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Farmers chose seeds from useful plants', 'Replanted those seeds again and again', 'The plant changed over many generations'],
                        'model': 'Farmers kept seeds from the wheat plants that held on to their seeds and planted them the next year. They did this again and again for many generations, so the '
                                 'wheat slowly changed into a plant that keeps its seeds until harvest.'},
                       {'t': 'text', 'q': 'What wild plant in Mexico did farmers turn into maize?', 'a': ['teosinte'], 'pts': 2, 'why': 'Teosinte, a wild grass with tiny ears.'},
                       {'t': 'open',
                        'key': 'calm',
                        'q': 'Why would early herders breed the calmest animals instead of the biggest or strongest? Give one reason.',
                        'min': 12,
                        'rows': 2,
                        'rubric': ['Calm animals are safer and easier to manage, gather and keep'],
                        'model': 'Calm animals are easier and safer to keep in a pen and lead to water, so they are less likely to run away or hurt someone.'}]},
           {'title': 'Farming Began in Many Places',
            'visual': '<svg viewBox="0 0 560 248" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="World map: Where people began farming, independently or '
                      'early"><text x="280.0" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Where people began farming, independently or early</text><rect x="0" y="28" '
                      'width="560" height="220" fill="#eaf4fb"/><polygon points="23.3,56.0 31.1,43.6 77.8,43.6 132.2,40.4 155.6,38.9 183.6,59.1 194.4,71.6 178.9,82.4 163.3,93.3 155.6,102.7 '
                      '154.0,113.6 149.3,105.8 140.0,107.3 129.1,112.0 129.1,121.3 144.7,119.8 143.1,129.1 150.9,138.4 160.2,140.0 155.6,140.0 147.8,135.3 136.9,129.1 116.7,121.3 108.9,116.7 '
                      '101.1,105.8 96.4,99.6 87.1,90.2 87.1,77.8 77.8,68.4 62.2,59.1 43.6,62.2 23.3,66.9" fill="#f3e7c9" stroke="#8a6d1f" stroke-width="1"/><polygon points="160.2,140.0 168.0,133.8 '
                      '183.6,136.9 199.1,144.7 225.6,160.2 219.3,174.2 216.2,186.7 205.3,192.9 197.6,205.3 189.8,211.6 178.9,216.2 175.8,224.0 172.7,233.3 166.4,230.2 164.9,217.8 169.6,199.1 '
                      '169.6,180.4 161.8,174.2 154.0,161.8 155.6,152.4 158.7,143.1" fill="#f3e7c9" stroke="#8a6d1f" stroke-width="1"/><polygon points="266.0,93.3 266.0,85.6 276.9,84.0 272.2,77.8 '
                      '283.1,73.1 292.4,68.4 295.6,63.8 287.8,62.2 287.8,56.0 303.3,45.1 323.6,42.0 342.2,48.2 373.3,45.1 404.4,38.9 443.3,32.7 497.8,38.9 544.4,43.6 560.0,49.8 544.4,59.1 533.6,62.2 '
                      '522.7,73.1 497.8,70.0 490.0,85.6 480.7,98.0 469.8,90.2 465.1,98.0 469.8,105.8 463.6,115.1 451.1,119.8 448.0,127.6 449.6,133.8 443.3,138.4 435.6,132.2 440.2,150.9 432.4,140.0 '
                      '430.9,127.6 423.1,119.8 416.9,118.2 404.4,129.1 399.8,140.0 393.6,126.0 388.9,118.2 382.7,113.6 368.7,113.6 367.1,110.4 357.8,105.8 354.7,107.3 360.9,115.1 367.1,115.1 '
                      '371.8,118.2 365.6,126.0 360.9,127.6 346.9,133.8 340.7,119.8 334.4,108.9 332.9,104.2 336.0,96.4 326.7,94.9 320.4,90.2 315.8,94.9 314.2,90.2 309.6,87.1 300.2,82.4 304.9,88.7 '
                      '308.0,90.2 298.7,84.0 292.4,84.0 284.7,85.6 278.4,94.9 270.7,96.4" fill="#f3e7c9" stroke="#8a6d1f" stroke-width="1"/><polygon points="271.0,96.8 284.7,95.2 295.9,94.9 '
                      '297.1,100.3 300.2,101.3 304.1,103.4 311.1,105.0 311.1,102.4 318.9,103.1 326.5,103.9 330.2,103.8 330.6,105.9 334.4,115.1 337.9,122.0 341.4,128.3 347.4,134.4 359.6,134.1 '
                      '356.2,141.6 350.5,149.3 343.8,154.8 341.8,158.7 341.1,163.0 343.0,168.8 343.3,175.8 335.1,189.6 330.7,192.9 328.2,199.0 323.4,203.8 319.8,205.3 311.1,206.6 308.6,205.3 '
                      '306.4,198.6 302.6,188.1 298.4,178.9 300.5,166.1 299.1,161.8 294.5,153.5 294.8,146.2 290.1,145.8 285.3,142.5 279.7,143.9 273.8,144.2 268.3,145.6 263.2,142.6 259.5,139.2 '
                      '253.9,132.2 252.9,129.6 255.1,122.9 253.6,119.8 259.8,109.7 265.1,105.2 269.4,99.6" fill="#f3e7c9" stroke="#8a6d1f" stroke-width="1"/><polygon points="348.9,191.3 353.1,191.3 '
                      '357.0,176.6 358.4,176.4 356.7,171.1 354.7,173.4 348.4,178.9 347.4,186.7" fill="#f3e7c9" stroke="#8a6d1f" stroke-width="1"/><polygon points="457.3,186.7 457.3,205.3 463.6,206.9 '
                      '482.2,202.2 494.7,206.9 499.3,211.6 513.3,210.0 518.0,196.0 518.0,191.3 507.1,182.0 500.9,169.6 491.6,171.1 483.8,169.6 474.4,174.2 469.8,180.4" fill="#f3e7c9" '
                      'stroke="#8a6d1f" stroke-width="1"/><polygon points="194.4,59.1 210.0,59.1 248.9,43.6 248.9,28.0 186.7,24.9 171.1,32.7 189.8,43.6" fill="#f3e7c9" stroke="#8a6d1f" '
                      'stroke-width="1"/><polygon points="272.2,74.7 281.6,73.1 276.9,65.3 272.2,62.2 270.7,66.9" fill="#f3e7c9" stroke="#8a6d1f" stroke-width="1"/><polygon points="483.8,154.0 '
                      '499.3,155.6 513.3,161.8 508.7,168.0 499.3,166.4 494.7,164.9 485.3,158.7" fill="#f3e7c9" stroke="#8a6d1f" stroke-width="1"/><polygon points="482.2,104.2 490.0,99.6 497.8,98.0 '
                      '500.9,90.2 499.3,82.4 496.2,90.2 490.0,98.0 483.8,99.6" fill="#f3e7c9" stroke="#8a6d1f" stroke-width="1"/><line x1="0.0" y1="152.4" x2="560.0" y2="152.4" stroke="#DB2F30" '
                      'stroke-dasharray="4 4" stroke-width=".8"/><circle cx="342.2" cy="96.4" r="4.5" fill="#C9A84C" stroke="#0A1F3D" stroke-width="1.3"/><text x="348.2" y="92.4" text-anchor="start" '
                      'font-size="10.5" font-weight="bold" fill="#0A1F3D">Fertile Crescent</text><circle cx="454.2" cy="99.6" r="4.5" fill="#C9A84C" stroke="#0A1F3D" stroke-width="1.3"/><text '
                      'x="460.2" y="90.6" text-anchor="start" font-size="10.5" font-weight="bold" fill="#0A1F3D">China</text><circle cx="504.0" cy="161.8" r="4.5" fill="#C9A84C" stroke="#0A1F3D" '
                      'stroke-width="1.3"/><text x="498.0" y="175.8" text-anchor="end" font-size="10.5" font-weight="bold" fill="#0A1F3D">New Guinea</text><circle cx="127.6" cy="122.9" r="4.5" '
                      'fill="#C9A84C" stroke="#0A1F3D" stroke-width="1.3"/><text x="121.6" y="118.9" text-anchor="end" font-size="10.5" font-weight="bold" fill="#0A1F3D">Mesoamerica</text><circle '
                      'cx="168.0" cy="172.7" r="4.5" fill="#C9A84C" stroke="#0A1F3D" stroke-width="1.3"/><text x="174.0" y="176.7" text-anchor="start" font-size="10.5" font-weight="bold" '
                      'fill="#0A1F3D">Andes</text><circle cx="146.2" cy="94.9" r="4.5" fill="#C9A84C" stroke="#0A1F3D" stroke-width="1.3"/><text x="140.2" y="86.9" text-anchor="end" font-size="10.5" '
                      'font-weight="bold" fill="#0A1F3D">Eastern N. America</text><circle cx="276.9" cy="130.7" r="4.5" fill="#C9A84C" stroke="#0A1F3D" stroke-width="1.3"/><text x="270.9" y="142.7" '
                      'text-anchor="end" font-size="10.5" font-weight="bold" fill="#0A1F3D">West African Sahel</text><circle cx="329.8" cy="130.7" r="4.5" fill="#C9A84C" stroke="#0A1F3D" '
                      'stroke-width="1.3"/><text x="321.8" y="122.69999999999999" text-anchor="end" font-size="10.5" font-weight="bold" fill="#0A1F3D">Sudan</text><circle cx="340.7" cy="138.4" '
                      'r="4.5" fill="#C9A84C" stroke="#0A1F3D" stroke-width="1.3"/><text x="346.7" y="152.4" text-anchor="start" font-size="10.5" font-weight="bold" fill="#0A1F3D">Ethiopian '
                      'Highlands</text><circle cx="385.8" cy="107.3" r="4.5" fill="#C9A84C" stroke="#0A1F3D" stroke-width="1.3"/><text x="391.8" y="119.3" text-anchor="start" font-size="10.5" '
                      'font-weight="bold" fill="#0A1F3D">Indus (Mehrgarh)</text></svg>',
            'html': '<p>Farming was not invented once and spread from one place. Scientists count at least seven, and perhaps more than a dozen, regions where people began farming on their own, with '
                    "different crops. Here are nine of them. Dates are approximate and are revised as new evidence is found.</p><table class='t'><tr><th>Region</th><th>Early crops or "
                    'animals</th><th>About how long ago</th></tr><tr><td>Fertile Crescent (Southwest Asia)</td><td>wheat, barley, goats, sheep</td><td>11,000 '
                    'years</td></tr><tr><td>China</td><td>millet (north), rice (south)</td><td>9,000 to 10,000 years</td></tr><tr><td>Indigenous Peoples of Mesoamerica</td><td>squash, then maize, '
                    'beans</td><td>9,000 to 10,000 years</td></tr><tr><td>Indigenous Peoples of the Andes (South America)</td><td>potatoes, quinoa, llamas</td><td>about 8,000 '
                    'years</td></tr><tr><td>New Guinea</td><td>taro, bananas</td><td>about 7,000 years or more</td></tr><tr><td>Sudan and the eastern Sahel (Africa)</td><td>sorghum</td><td>about '
                    '5,000 years</td></tr><tr><td>West African Sahel</td><td>pearl millet, later African rice and yams</td><td>about 4,500 years</td></tr><tr><td>Ethiopian Highlands '
                    '(Africa)</td><td>teff, enset, finger millet</td><td>debated; thousands of years</td></tr><tr><td>Indigenous Peoples of eastern North America</td><td>sunflower, squash, '
                    'goosefoot, marshelder</td><td>about 5,000 years</td></tr></table><p>The farmers of the Americas were the ancestors of many Indigenous nations today, such as the Quechua in the '
                    'Andes. African farmers domesticated crops the world still eats: sorghum, pearl millet, African rice, yams, okra, watermelon and teff. Coffee also comes from Africa: it grew wild '
                    'in Ethiopia and was first cultivated about 500 to 600 years ago.</p>',
            'checks': [{'t': 'num', 'q': 'About how many years ago did farming begin in the Fertile Crescent?', 'a': 11000, 'unit': 'years', 'pts': 2, 'why': 'About 11,000 years ago.'},
                       {'t': 'blanks',
                        'q': 'Name the region where each crop was first domesticated.',
                        'sent': 'Potatoes: ___. Sorghum: ___ (in Africa). Rice: ___.',
                        'blanks': [['andes', 'the andes', 'south america', 'peru', 'bolivia'],
                                   ['sudan', 'eastern sahel', 'sahel', 'sudan and the eastern sahel', 'northeast africa'],
                                   ['china', 'southern china', 'yangtze', 'yangtze river']],
                        'show': 'Andes; Sudan (eastern Sahel); China',
                        'pts': 3,
                        'why': 'Potatoes in the Andes, sorghum in Sudan and the eastern Sahel, rice in southern China.'},
                       {'t': 'open',
                        'key': 'independent',
                        'q': 'Why is it important that farming began independently in many places, instead of being invented once and spread? What does this tell us about people around the world?',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Explains independent invention', 'Concludes that people everywhere were inventive and solved problems', 'Avoids the idea that one group taught everyone'],
                        'model': 'It shows that people in Africa, Asia, the Americas and New Guinea all figured out farming on their own, using the plants around them. No single group was the only '
                                 'inventor; people everywhere were smart problem solvers.'},
                       {'t': 'blanks',
                        'q': 'Name two different crops first domesticated in Africa.',
                        'sent': 'Crop 1: ___   Crop 2: ___',
                        'blanks': [['sorghum', 'pearl millet', 'african rice', 'yams', 'coffee', 'okra', 'watermelon', 'teff', 'enset', 'finger millet'],
                                   ['sorghum', 'pearl millet', 'african rice', 'yams', 'coffee', 'okra', 'watermelon', 'teff', 'enset', 'finger millet']],
                        'distinct': True,
                        'show': 'For example: sorghum and coffee',
                        'pts': 2,
                        'why': 'Sorghum, pearl millet, African rice, yams, coffee, okra, watermelon and teff all come from Africa.'}]},
           {'title': 'The First Towns',
            'visual': '<svg viewBox="0 0 560 240" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Cutaway drawing of a Catalhoyuk house"><text x="280" '
                      'y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Çatalhöyük: houses packed wall to wall, entered through the roof</text><rect x="20" y="80" '
                      'width="520" height="140" fill="#e8d3a8" stroke="#8a6d1f"/><rect x="20" y="80" width="130" height="140" fill="#e8d3a8" stroke="#8a6d1f" stroke-width="3"/><rect x="150" y="80" '
                      'width="130" height="140" fill="#f1e0bd" stroke="#8a6d1f" stroke-width="3"/><rect x="280" y="80" width="130" height="140" fill="#e8d3a8" stroke="#8a6d1f" '
                      'stroke-width="3"/><rect x="410" y="80" width="130" height="140" fill="#f1e0bd" stroke="#8a6d1f" stroke-width="3"/><rect x="150" y="70" width="130" height="12" '
                      'fill="#a9824a"/><rect x="195" y="70" width="30" height="12" fill="#3b2a12"/><line x1="205" y1="75" x2="185" y2="215" stroke="#5b3a12" stroke-width="3"/><line x1="220" y1="75" '
                      'x2="200" y2="215" stroke="#5b3a12" stroke-width="3"/><line x1="205" y1="95" x2="220" y2="95" stroke="#5b3a12" stroke-width="2"/><line x1="202" y1="115" x2="217" y2="115" '
                      'stroke="#5b3a12" stroke-width="2"/><line x1="199" y1="135" x2="214" y2="135" stroke="#5b3a12" stroke-width="2"/><line x1="196" y1="155" x2="211" y2="155" stroke="#5b3a12" '
                      'stroke-width="2"/><line x1="193" y1="175" x2="208" y2="175" stroke="#5b3a12" stroke-width="2"/><line x1="190" y1="195" x2="205" y2="195" stroke="#5b3a12" '
                      'stroke-width="2"/><rect x="240" y="180" width="30" height="34" fill="#c45c2a"/><text x="255" y="232" text-anchor="middle" font-size="10">oven</text><rect x="160" y="196" '
                      'width="28" height="18" fill="#cdb48a" stroke="#8a6d1f"/><text x="174" y="232" text-anchor="middle" font-size="10">platform</text><path d="M290 120 q10 -20 20 0 q10 20 20 0" '
                      'fill="none" stroke="#DB2F30" stroke-width="2"/><text x="345" y="112" font-size="10">wall paintings</text><text x="85" y="60" text-anchor="middle" font-size="11">no streets: '
                      'people walked</text><text x="85" y="74" text-anchor="middle" font-size="11">across the rooftops</text><path d="M140 64 L190 72" stroke="#0A1F3D"/><text x="420" y="60" '
                      'text-anchor="middle" font-size="11">ladder through a roof hole</text><path d="M360 62 L226 76" stroke="#0A1F3D"/></svg>',
            'html': '<p><b>Göbekli Tepe</b> (southeastern Türkiye), built beginning about 11,500 years ago, has huge carved stone pillars arranged in circles. It was built by people who still mostly '
                    'gathered and hunted their food, which surprised archaeologists: big shared projects may have come <i>before</i> farming, not only after.</p><p><b>Jericho</b> (in the West Bank, '
                    'near the Jordan River) had a stone wall and a tall stone tower about 10,000 years ago, beside the spring of Ein es-Sultan, which still flows today.</p><p><b>Çatalhöyük</b> '
                    '(central Türkiye), lived in from about 9,100 to 8,000 years ago, may have held several thousand people. Its mud-brick houses were packed together with no streets. People walked '
                    'across the roofs and climbed down ladders into their homes, which had ovens, platforms for sleeping and working, and wall paintings.</p>',
            'checks': [{'t': 'text',
                        'q': 'How did people get into their homes at Çatalhöyük?',
                        'a': [{'all': [['roof', 'ladder', 'top']]}],
                        'show': 'through a hole in the roof, by ladder',
                        'pts': 2,
                        'why': 'Houses had no front doors on streets; people climbed down ladders through roof openings.'},
                       {'t': 'open',
                        'key': 'gobekli',
                        'q': 'Göbekli Tepe was built by people who mostly gathered and hunted. Why did this surprise archaeologists, and what new question did it raise?',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Archaeologists expected big building only after farming', 'New question: did gathering for building or ceremonies help lead to farming?'],
                        'model': 'Archaeologists thought people needed farming and stored food before they could build huge stone monuments. Göbekli Tepe raised a new question: maybe gathering in '
                                 'large groups to build and hold ceremonies helped lead people toward farming.'},
                       {'t': 'open',
                        'key': 'nostreet',
                        'q': 'Look at the drawing of Çatalhöyük. Give one advantage and one disadvantage of building houses wall to wall with roof entrances.',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['A reasonable advantage (protection, warmth, shared walls save material)', 'A reasonable disadvantage (fire spreads, hard to carry things, crowded, disease)'],
                        'model': 'An advantage is protection: with no doors at ground level, animals and raiders could not easily get in, and shared walls saved mud bricks. A disadvantage is that '
                                 'carrying heavy loads up and down ladders would be hard, and a fire or disease could spread quickly.'}]},
           {'title': 'Was Farming a Good Trade?',
            'visual': '<svg viewBox="0 0 560 180" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Chain of effects from farming"><text x="280" y="18" '
                      'text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">One change leads to another</text><rect x="10" y="50" width="100" height="70" rx="10" '
                      'fill="#0A1F3D"/><text x="60" y="80" text-anchor="middle" fill="#fff" font-weight="bold">Farming</text><text x="60" y="98" text-anchor="middle" fill="#fff" '
                      'font-size="11">planting, herding</text><path d="M110 85 h10" stroke="#0A1F3D" stroke-width="2"/><path d="M120 85 l-5 -4 v8z" fill="#0A1F3D"/><rect x="120" y="50" width="100" '
                      'height="70" rx="10" fill="#0047BA"/><text x="170" y="80" text-anchor="middle" fill="#fff" font-weight="bold">Surplus</text><text x="170" y="98" text-anchor="middle" '
                      'fill="#fff" font-size="11">extra food stored</text><path d="M220 85 h10" stroke="#0A1F3D" stroke-width="2"/><path d="M230 85 l-5 -4 v8z" fill="#0A1F3D"/><rect x="230" y="50" '
                      'width="100" height="70" rx="10" fill="#2f5a91"/><text x="280" y="80" text-anchor="middle" fill="#fff" font-weight="bold">More people</text><text x="280" y="98" '
                      'text-anchor="middle" fill="#fff" font-size="11">villages grow</text><path d="M330 85 h10" stroke="#0A1F3D" stroke-width="2"/><path d="M340 85 l-5 -4 v8z" fill="#0A1F3D"/><rect '
                      'x="340" y="50" width="100" height="70" rx="10" fill="#C9A84C"/><text x="390" y="80" text-anchor="middle" fill="#fff" font-weight="bold">Specialists</text><text x="390" y="98" '
                      'text-anchor="middle" fill="#fff" font-size="11">potters, builders</text><path d="M440 85 h10" stroke="#0A1F3D" stroke-width="2"/><path d="M450 85 l-5 -4 v8z" '
                      'fill="#0A1F3D"/><rect x="450" y="50" width="100" height="70" rx="10" fill="#DB2F30"/><text x="500" y="80" text-anchor="middle" fill="#fff" font-weight="bold">Trade and '
                      'rules</text><text x="500" y="98" text-anchor="middle" fill="#fff" font-size="11">towns, leaders</text><text x="280" y="150" text-anchor="middle" font-size="12">Every arrow is '
                      'a cause and an effect. Historians ask which links were strongest, and who gained or lost.</text></svg>',
            'html': '<p>Farming produced a <b>surplus</b>. Stored food let more people live in one place, and not everyone had to farm. Some became <b>specialists</b>: potters, toolmakers, builders, '
                    'traders, religious leaders. Over time this led to towns, trade networks and, eventually, cities and governments.</p><p>But there were costs. Skeletons from many early farming '
                    'villages show people who were shorter than earlier foragers, with more tooth decay and signs of poor nutrition, because they ate a few crops instead of many wild foods. Living '
                    'close to animals and to one another spread disease. A single drought or crop disease could cause famine. Some people stored more than others, so differences between rich and '
                    'poor began to grow.</p>',
            'checks': [{'t': 'text', 'q': 'What is the word for extra food that can be stored or traded?', 'a': ['surplus', 'a surplus'], 'pts': 2, 'why': 'A surplus made specialization possible.'},
                       {'t': 'open',
                        'key': 'specialist',
                        'q': 'Explain why a surplus made it possible for some people to become potters or builders.',
                        'min': 15,
                        'rows': 2,
                        'rubric': ['Others produced enough food for them', 'So they could spend time on other work'],
                        'model': 'If farmers grew more food than their families needed, they could trade some to the potter, so the potter did not have to grow food and could spend the day making '
                                 'pots.'},
                       {'t': 'open',
                        'key': 'health',
                        'q': 'Give two pieces of evidence that early farmers were sometimes less healthy than foragers, and explain why.',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Two pieces of skeletal or other evidence (height, teeth, disease)', 'Explains the cause (less varied diet, crowding, animals)'],
                        'model': 'Skeletons show many early farmers were shorter and had more tooth decay than foragers. They ate mostly a few starchy crops instead of many wild foods, and living '
                                 'crowded together with animals spread disease.'}]}],
 'handson': {'title': 'Grind It Like the First Farmers',
             'intro': 'Early farmers ground grain into flour by hand between two stones. Feel the work for yourself, then do the math.',
             'materials': ['A flat stone or a sturdy cutting board, plus a smooth fist-sized stone (washed) or a mortar and pestle',
                           '1/4 cup of dry whole grain (wheat berries, uncooked rice, popcorn kernels or dried corn, or oats)',
                           'A timer',
                           'A tablespoon measuring spoon, a fine-mesh strainer or sieve and a small bowl',
                           'A clean towel underneath to catch spills'],
             'steps': ['Spread a spoonful of grain on the flat stone. Kneel and push the hand stone back and forth over it, the way people used a grinding stone, called a saddle quern.',
                       'Set a timer for 5 minutes and grind. Sift out what is fine enough to call flour and measure it.',
                       'Repeat once more and record your total.',
                       'Calculate: a family loaf of bread needs about 3 cups of flour. At your rate, how long would it take to grind enough flour for one loaf?',
                       'Save a spoonful of your flour in a labeled bag and photograph your grinding setup. These become an artifact for your Week 5 museum exhibit.',
                       'Talk with a parent: who in an early village probably did this work every day, and how might it have shaped their life?'],
             'record': [{'t': 'open',
                         'key': 'grind',
                         'q': 'Record how much flour you made in 10 minutes, then calculate how long it would take to grind 3 cups (48 tablespoons). Show your math.',
                         'min': 22,
                         'rows': 4,
                         'rubric': ['Records the amount ground with units', 'Correctly sets up the rate calculation', 'Gives an answer in minutes or hours'],
                         'model': 'I made 2 tablespoons in 10 minutes, which is 5 minutes per tablespoon. 48 tablespoons × 5 minutes = 240 minutes, or 4 hours for one loaf.'},
                        {'t': 'open',
                         'key': 'grind2',
                         'q': 'At Abu Hureyra in Syria, archaeologists found skeletons of early farming women with worn toes, knees and lower backs. Using your experience, explain what might have '
                              'caused this.',
                         'min': 25,
                         'rows': 3,
                         'rubric': ['Connects kneeling and pushing to the injuries', 'Notes the daily hours of grinding', 'Uses the skeleton as evidence about daily life'],
                         'model': 'Grinding meant kneeling with toes bent and pushing forward with the back and arms for hours every day. After years, this would wear down the toes, knees and lower '
                                  'back, so the skeletons are evidence of how hard daily grinding was.'}]},
 'think': {'intro': 'Make an argument and support it with evidence. Your teacher scores these. Your argument can become the label text for your Week 5 museum exhibit.',
           'items': [{'t': 'open',
                      'key': 'argue',
                      'q': 'Was the switch to farming a good trade for ordinary people in the first villages? Take a side. Give at least two pieces of evidence for your side and answer one argument '
                           'from the other side.',
                      'min': 90,
                      'rows': 10,
                      'rubric': ['Clear claim', 'Two pieces of accurate evidence', 'Responds to a counterargument', 'Organized paragraph with a conclusion'],
                      'model': 'For ordinary people in the first villages, farming was not a good trade at first. Skeletons show farmers were often shorter and had more tooth decay than foragers, '
                               'because they ate a few crops instead of many wild foods. Farming also meant hours of hard work, like grinding grain on knees every day, and one drought could cause '
                               'hunger. Some people argue farming was worth it because a surplus let villages grow and specialists like potters appear. That is true for society over thousands of '
                               'years, but the first farmers paid the cost in their health and work. So farming helped humanity in the long run, but it was a hard deal for the first people who made '
                               'it.'},
                     {'t': 'open',
                      'key': 'compare',
                      'q': 'Compare a day in the life of a forager family and an early farming family. Write at least two similarities and three differences.',
                      'min': 56,
                      'rows': 7,
                      'rubric': ['Two accurate similarities', 'Three accurate differences (food, housing, possessions, work, group size)', 'Specific details'],
                      'model': 'Both families needed water, made stone tools and shared food with their group. Foragers moved with the seasons and carried few belongings, while farmers lived in one '
                               'place in mud-brick houses with stored grain. Foragers ate many kinds of wild food, but farmers ate mostly a few crops. Farmers worked long hours weeding and grinding, '
                               'and they lived in larger groups with more chance of disease.'}]},
 'exit': [{'t': 'text',
           'q': 'What does domestication mean?',
           'a': [{'all': [['chang', 'breed', 'select', 'choos', 'generation'], ['plant', 'animal', 'crop', 'seed']]}],
           'show': 'changing plants or animals over generations to be more useful to people',
           'pts': 2,
           'why': 'Domestication is changing plants or animals over generations by choosing which to grow or breed.'},
          {'t': 'blanks',
           'q': 'Name three different regions where farming began independently.',
           'sent': '___, ___ and ___',
           'blanks': [['andes',
                       'china',
                       'fertile crescent',
                       'mesoamerica',
                       'mexico',
                       'new guinea',
                       'sudan',
                       'sahel',
                       'west african sahel',
                       'eastern sahel',
                       'ethiopia',
                       'ethiopian highlands',
                       'eastern north america',
                       'southwest asia'],
                      ['andes',
                       'china',
                       'fertile crescent',
                       'mesoamerica',
                       'mexico',
                       'new guinea',
                       'sudan',
                       'sahel',
                       'west african sahel',
                       'eastern sahel',
                       'ethiopia',
                       'ethiopian highlands',
                       'eastern north america',
                       'southwest asia'],
                      ['andes',
                       'china',
                       'fertile crescent',
                       'mesoamerica',
                       'mexico',
                       'new guinea',
                       'sudan',
                       'sahel',
                       'west african sahel',
                       'eastern sahel',
                       'ethiopia',
                       'ethiopian highlands',
                       'eastern north america',
                       'southwest asia']],
           'distinct': True,
           'show': 'For example: the Fertile Crescent, the Andes and the West African Sahel',
           'pts': 3,
           'why': 'Regions include the Fertile Crescent, China, Mesoamerica, the Andes, New Guinea, Sudan and the eastern Sahel, the West African Sahel, the Ethiopian Highlands and eastern North '
                  'America.'},
          {'t': 'text',
           'q': 'Name one crop first domesticated in Africa.',
           'a': ['sorghum', 'pearl millet', 'millet', 'african rice', 'yams', 'yam', 'coffee', 'okra', 'watermelon', 'teff', 'enset'],
           'show': 'sorghum (or pearl millet, coffee, yams, okra, teff)',
           'pts': 2,
           'why': 'Africa gave the world sorghum, pearl millet, African rice, yams, coffee, okra, watermelon and teff.'},
          {'t': 'text',
           'q': 'Which early town had houses with no streets, entered through the roof?',
           'a': ['catalhoyuk', 'çatalhöyük', 'catal huyuk', 'catalhuyuk', 'çatalhöyuk', 'catal hoyuk', 'catalhoyuk'],
           'show': 'Çatalhöyük',
           'pts': 2,
           'why': 'Çatalhöyük, in central Türkiye.'},
          {'t': 'open',
           'key': 'exit_cost',
           'q': 'Name one benefit and one cost of farming for early villages.',
           'min': 12,
           'rows': 2,
           'rubric': ['A real benefit (surplus, specialists, larger groups)', 'A real cost (poorer diet, disease, hard labor, famine risk, inequality)'],
           'model': 'A benefit was a surplus of stored food that let villages grow. A cost was a less varied diet that made many people shorter and less healthy.'}],
 'next': 'Week 5: the Unit 1 checkpoint and your museum exhibit project. Then Unit 2 travels to the Nile Valley: Kemet, Nubia and Kush.'}

TEACHER = {
 "standards": [
  "SS.6.W.2.1: Compare the lifestyles of hunter-gatherers with those of settlers of early agricultural communities.",
  "SS.6.W.2.2: Describe how the developments of agriculture and metallurgy related to settlement, population growth, and the emergence of civilization.",
  "SS.6.W.2.3 (preview): Identify the characteristics of civilization.",
  "SS.6.G.2.4 (preview): Explain how the geographical location of ancient civilizations contributed to the culture and politics of those societies.",
  "C3 Framework D2.His.14.6-8: Explain multiple causes and effects of events and developments in the past."],
 "materials": ["The interactive lesson", "A world map or globe", "A flat stone or cutting board, a smooth stone or mortar and pestle, and 1/4 cup of dry grain", "A timer, a tablespoon, a fine strainer and a towel", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 3 Reconnect questions."],
  [5, "Hook", "Read the two families. Ask the student to predict which family was healthier before teaching."],
  [10, "Domestication", "Explain seed selection with wheat and teosinte. If possible, show a picture of teosinte beside an ear of corn."],
  [12, "Many centers", "Find each center on the map. Emphasize independent invention and the African crops the student eats today."],
  [10, "First towns", "Study the Çatalhöyük drawing. Discuss why Göbekli Tepe changed archaeologists' thinking."],
  [12, "Costs and benefits", "Trace the chain of effects. Present the skeletal evidence. Ask the student to take a side and defend it."],
  [5, "Assign", "Assign the grinding activity, Think Deeper and the Exit Check."]],
 "key_questions": ["What evidence do we have for this, and how sure are scientists?", "Who gained from farming, and who paid the costs?", "Why did farming start in so many places in roughly the same era?", "What foods on your table today came from Africa, the Americas or Asia?"],
 "misconceptions": ["Farming was invented once in the Middle East and spread everywhere.", "Farming was an obvious improvement that made everyone healthier.", "Early towns looked like modern towns with streets and stores.", "Africa had no role in early agriculture."],
 "support": ["Provide the crop table as a printed card.", "Give sentence starters for the argument: I believe... One piece of evidence is... Some people argue... However...", "Let the student talk through the argument aloud before writing."],
 "challenge": ["Research the Green Sahara: how did people in the Sahara live when it was grassland about 10,000 to 5,000 years ago, and what happened when it dried?", "Investigate one crop's journey, such as coffee from Ethiopia (cultivated much later, about 500 to 600 years ago), and map how it spread around the world."],
 "background": "<p>Archaeologists generally recognize somewhere between about seven and more than a dozen independent or early centers of plant domestication, depending on definitions. The dates in the table are rounded and represent current estimates. Early dates for cattle management at Nabta Playa and Bir Kiseiba (around 9,000 or more years ago) are argued by Fred Wendorf and colleagues and remain debated. Sorghum domestication in eastern Sudan is supported by finds at Butana Group site KG23 near Kassala around 5,000 years ago. Pearl millet domestication in the West African Sahel is dated to about 4,500 years ago. Göbekli Tepe's earliest construction is about 9500 BCE; recent work has found evidence of more permanent occupation than first thought, but its builders did not yet rely on domesticated crops. Çatalhöyük was occupied roughly 7100 to 5950 BCE. The evidence that early farming populations often show reduced stature and increased dental disease comes from bioarchaeological studies across several regions, though patterns vary.</p>",
 "sources": ["Smithsonian National Museum of Natural History: The Origins of Agriculture.", "Çatalhöyük Research Project (catalhoyuk.com).", "German Archaeological Institute (DAI): Göbekli Tepe project.", "Winchell, F., Stevens, C., Murphy, C., Champion, L. and Fuller, D. (2017), Evidence for Sorghum Domestication in Fourth Millennium BC Eastern Sudan, Current Anthropology 58(5).", "Manning, K. et al. (2011), 4500-year-old domesticated pearl millet from Mali, Journal of Archaeological Science.", "Larsen, C.S. (2006), The agricultural revolution as environmental catastrophe, Quaternary International.", "Molleson, T. (1994), The Eloquent Bones of Abu Hureyra, Scientific American."]
}

PRINT = {
 "directions": "Use complete sentences and evidence from the lesson.",
 "items": [
  {"q":"Define domestication and give one plant and one animal example.","a":"Changing plants or animals over generations by choosing which to grow or breed. Examples: wheat, maize; goats, cattle.","lines":2},
  {"q":"List four regions where farming began independently and one crop from each.","a":"For example: Fertile Crescent, wheat; China, rice; Andes, potatoes; Sudan, sorghum.","lines":3},
  {"q":"Name three crops first domesticated in Africa.","a":"For example: sorghum, pearl millet, coffee (also yams, okra, watermelon, teff, African rice).","lines":1},
  {"q":"Describe one feature of Çatalhöyük and one of Göbekli Tepe.","a":"Çatalhöyük: houses packed together, entered through the roof. Göbekli Tepe: huge carved stone pillars built by people who mostly foraged.","lines":2},
  {"q":"Fill in the chain: Farming → ________ → More people → ________ → Trade and rules","a":"Surplus; Specialists","lines":1},
  {"q":"Give two costs of early farming and explain one.","a":"For example: poorer diet (fewer kinds of food), more disease (crowding and animals), hard labor, famine risk, inequality.","lines":3}]
}
