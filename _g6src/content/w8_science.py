def plantcell():
    s = ('<svg viewBox="0 0 700 330" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="A plant cell with lettered parts">'
         '<text x="350" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">A plant cell (lettered parts)</text>'
         '<rect x="150" y="40" width="400" height="270" rx="10" fill="#cfe8b0" stroke="#3d6b1f" stroke-width="9"/>'
         '<rect x="166" y="56" width="368" height="238" rx="6" fill="none" stroke="#0A1F3D" stroke-width="2" stroke-dasharray="5 3"/>'
         '<rect x="240" y="90" width="220" height="160" rx="40" fill="#bfe3f5" stroke="#0047BA" stroke-width="2"/>'
         '<circle cx="495" cy="110" r="32" fill="#e8d7f5" stroke="#6b3fa0" stroke-width="2"/><circle cx="490" cy="106" r="9" fill="#6b3fa0"/>')
    for cx, cy in [(195, 90), (200, 200), (210, 270), (490, 270), (505, 200), (300, 280), (390, 75)]:
        s += f'<ellipse cx="{cx}" cy="{cy}" rx="20" ry="10" fill="#3d9a2f" stroke="#1f5c17"/><path d="M{cx-12} {cy} h24 M{cx-12} {cy-4} h24 M{cx-12} {cy+4} h24" stroke="#1f5c17" stroke-width=".7"/>'
    s += '<ellipse cx="200" cy="150" rx="17" ry="9" fill="#f4b183" stroke="#a5552a"/><path d="M188 150 q4 -6 8 0 q4 6 8 0 q4 -6 8 0" fill="none" stroke="#a5552a"/>'
    tags = [("A", 150, 175, 100, 175), ("B", 166, 250, 100, 300), ("C", 220, 200, 100, 238), ("D", 460, 170, 600, 170), ("E", 527, 110, 600, 110), ("F", 183, 150, 100, 130)]
    for t, x1, y1, x2, y2 in tags:
        s += f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#0A1F3D" stroke-width="1.2"/><circle cx="{x1}" cy="{y1}" r="2.5" fill="#0A1F3D"/><circle cx="{x2}" cy="{y2}" r="13" fill="#0A1F3D"/><text x="{x2}" y="{y2+5}" text-anchor="middle" fill="#fff" font-weight="bold">{t}</text>'
    s += '<text x="350" y="326" text-anchor="middle" font-size="11" fill="#5b6676">Not to scale. Real plant cells have many more chloroplasts and mitochondria.</text></svg>'
    return s

PHOTO = ('<svg viewBox="0 0 700 260" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Diagram of photosynthesis in a leaf">'
  '<text x="350" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Photosynthesis: what goes in, what comes out</text>'
  '<circle cx="80" cy="70" r="28" fill="#F7C948"/>' + ''.join(f'<line x1="{80+36*c}" y1="{70+36*s_}" x2="{80+48*c}" y2="{70+48*s_}" stroke="#F7C948" stroke-width="3"/>' for c, s_ in [(1,0),(-1,0),(0,1),(0,-1),(.7,.7),(-.7,.7),(.7,-.7),(-.7,-.7)]) +
  '<text x="80" y="125" text-anchor="middle" font-weight="bold">light energy</text><path d="M120 95 L265 135" stroke="#C9A84C" stroke-width="3" marker-end="url(#ah)"/>'
  '<defs><marker id="ah" viewBox="0 0 10 10" markerWidth="4" markerHeight="4" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="#0A1F3D"/></marker></defs>'
  '<path d="M270 150 Q350 60 440 150 Q350 240 270 150Z" fill="#3d9a2f" stroke="#1f5c17" stroke-width="2"/><path d="M270 150 H440" stroke="#1f5c17"/>'
  '<text x="355" y="140" text-anchor="middle" fill="#fff" font-weight="bold">chloroplasts</text><text x="355" y="168" text-anchor="middle" fill="#fff" font-size="11">in leaf cells</text>'
  '<text x="80" y="185" text-anchor="middle" font-weight="bold" fill="#0047BA">carbon dioxide</text><text x="80" y="201" text-anchor="middle" font-size="11">from the air, through stomata</text><path d="M150 185 L265 160" stroke="#0047BA" stroke-width="3" marker-end="url(#ah)"/>'
  '<text x="355" y="252" text-anchor="middle" font-weight="bold" fill="#0047BA">water from the roots</text><path d="M355 236 L355 205" stroke="#0047BA" stroke-width="3" marker-end="url(#ah)"/>'
  '<path d="M445 130 L560 95" stroke="#DB2F30" stroke-width="3" marker-end="url(#ah)"/><text x="620" y="90" text-anchor="middle" font-weight="bold" fill="#DB2F30">oxygen</text><text x="620" y="106" text-anchor="middle" font-size="11">released into the air</text>'
  '<path d="M445 170 L560 200" stroke="#DB2F30" stroke-width="3" marker-end="url(#ah)"/><text x="620" y="205" text-anchor="middle" font-weight="bold" fill="#DB2F30">glucose (sugar)</text><text x="620" y="221" text-anchor="middle" font-size="11">food the plant uses and stores</text></svg>')

COMPARE = ('<svg viewBox="0 0 640 295" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Venn diagram comparing plant and animal cells">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Plant cells and animal cells</text>'
  '<circle cx="245" cy="160" r="128" fill="#3d9a2f" fill-opacity=".18" stroke="#3d6b1f" stroke-width="2"/><circle cx="395" cy="160" r="128" fill="#DB2F30" fill-opacity=".12" stroke="#DB2F30" stroke-width="2"/>'
  '<text x="185" y="88" text-anchor="middle" font-weight="bold" font-size="13">Plant only</text><text x="455" y="88" text-anchor="middle" font-weight="bold" font-size="13">Animal only</text><text x="320" y="78" text-anchor="middle" font-weight="bold" font-size="13">Both</text>'
  + ''.join(f'<text x="185" y="{y}" text-anchor="middle">{t}</text>' for y, t in [(125, "cell wall"), (148, "chloroplasts"), (171, "one large central"), (186, "vacuole"), (209, "fixed, boxy shape")]) +
  '<text x="320" y="112" text-anchor="middle" font-size="11">cell membrane</text>' + ''.join(f'<text x="320" y="{y}" text-anchor="middle">{t}</text>' for y, t in [(134, "nucleus"), (156, "cytoplasm"), (178, "mitochondria"), (200, "ribosomes"), (222, "ER, Golgi")]) +
  ''.join(f'<text x="455" y="{y}" text-anchor="middle">{t}</text>' for y, t in [(125, "no cell wall"), (148, "small vacuoles,"), (163, "if any"), (186, "lysosomes"), (201, "common"), (224, "flexible shape")]) +
  '</svg>')

LESSON = {'unit': 'Unit 2: Cells, the Building Blocks of Life',
 'title': 'Plant Cells and Photosynthesis',
 'subtitle': 'Plant cells have three parts animal cells lack. One of them, the chloroplast, captures sunlight and makes the food that nearly every living thing depends on.',
 'objectives': ['Identify the cell wall, chloroplasts and central vacuole and explain the job of each.',
                'Compare and contrast plant and animal cells.',
                'Describe photosynthesis: its inputs, outputs and where it happens.',
                'Plan and run a controlled leaf-disk investigation and explain the results with evidence.',
                'Explain why photosynthesis matters for food webs and the air we breathe.'],
 'vocab': [['cell wall', 'A stiff layer outside the cell membrane of a plant cell that supports and protects it.'],
           ['chloroplast', 'The organelle where photosynthesis happens; it contains the green pigment chlorophyll.'],
           ['chlorophyll', 'The green pigment in chloroplasts that absorbs light energy.'],
           ['central vacuole', 'A large sac in a plant cell that stores water and keeps the cell firm.'],
           ['photosynthesis', 'The process plants, algae and some bacteria use to turn light energy, carbon dioxide and water into glucose and oxygen.'],
           ['glucose', 'A sugar that stores energy; the food made by photosynthesis.'],
           ['stomata', 'Tiny openings, mostly on the underside of leaves, that let carbon dioxide in and oxygen and water vapor out.'],
           ['producer', 'A living thing that makes its own food, such as a plant.']],
 'reconnect': {'title': 'Week 7: Inside an animal cell',
               'intro': 'Plant cells share most of the parts you learned last week. Review them first.',
               'items': [{'t': 'text',
                          'q': 'Which organelle releases energy from food for the cell?',
                          'a': ['mitochondria', 'mitochondrion', 'the mitochondria'],
                          'show': 'mitochondria',
                          'pts': 2,
                          'why': 'Mitochondria release the energy stored in food (glucose). Today you will learn where that glucose comes from.'},
                         {'t': 'text',
                          'q': 'Which part controls what enters and leaves every cell?',
                          'a': [{'all': [['cell membrane', 'plasma membrane', 'membrane']], 'none': ['nuclear', 'wall', 'not', 'vacuole']}],
                          'show': 'cell membrane',
                          'pts': 2,
                          'why': 'The cell membrane. Plant cells have one too, inside their cell wall.'},
                         {'t': 'open',
                          'key': 'rc_chain',
                          'q': "In last week's cell-as-a-city model, name the organelle that builds proteins and the one that packages and ships them.",
                          'min': 10,
                          'rows': 2,
                          'rubric': ['Ribosomes build proteins', 'Golgi apparatus packages and ships'],
                          'model': 'Ribosomes build proteins, and the Golgi apparatus packages and ships them.'},
                         {'t': 'open',
                          'key': 'rc_lacks',
                          'q': "What did Henrietta Lacks's story teach about how scientists must treat people who give cells or tissue?",
                          'min': 15,
                          'rows': 2,
                          'rubric': ['Informed consent: ask permission and explain how cells will be used'],
                          'model': 'Scientists must ask for permission, explain how the cells will be used and respect the person and their family.'}]},
 'hook': {'title': 'Who Feeds the Manatees?',
          'html': "<p>In 2021, more than 1,000 manatees died in Florida, the most ever recorded in one year. Many of them starved in the Indian River Lagoon on Florida's east coast. Why? Pollution "
                  'fed huge blooms of algae that clouded the water. Sunlight could no longer reach the seagrass on the bottom, so the seagrass died, and manatees eat mostly seagrass.</p><p>The chain '
                  'is simple: no light, no seagrass; no seagrass, no food for manatees. Today you will see why. Seagrass, like every green plant, makes its own food from light, and it does that '
                  "inside tiny green parts of its cells.</p><div class='callout'><b>Big question:</b> How can a living thing make its own food out of light, air and water?</div>"},
 'learn': [{'title': 'Three Parts That Make Plant Cells Different',
            'visual': '<svg viewBox="0 0 700 330" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="A plant cell with lettered parts"><text x="350" y="20" '
                      'text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">A plant cell (lettered parts)</text><rect x="150" y="40" width="400" height="270" rx="10" fill="#cfe8b0" '
                      'stroke="#3d6b1f" stroke-width="9"/><rect x="166" y="56" width="368" height="238" rx="6" fill="none" stroke="#0A1F3D" stroke-width="2" stroke-dasharray="5 3"/><rect x="240" '
                      'y="90" width="220" height="160" rx="40" fill="#bfe3f5" stroke="#0047BA" stroke-width="2"/><circle cx="495" cy="110" r="32" fill="#e8d7f5" stroke="#6b3fa0" '
                      'stroke-width="2"/><circle cx="490" cy="106" r="9" fill="#6b3fa0"/><ellipse cx="195" cy="90" rx="20" ry="10" fill="#3d9a2f" stroke="#1f5c17"/><path d="M183 90 h24 M183 86 h24 '
                      'M183 94 h24" stroke="#1f5c17" stroke-width=".7"/><ellipse cx="200" cy="200" rx="20" ry="10" fill="#3d9a2f" stroke="#1f5c17"/><path d="M188 200 h24 M188 196 h24 M188 204 h24" '
                      'stroke="#1f5c17" stroke-width=".7"/><ellipse cx="210" cy="270" rx="20" ry="10" fill="#3d9a2f" stroke="#1f5c17"/><path d="M198 270 h24 M198 266 h24 M198 274 h24" '
                      'stroke="#1f5c17" stroke-width=".7"/><ellipse cx="490" cy="270" rx="20" ry="10" fill="#3d9a2f" stroke="#1f5c17"/><path d="M478 270 h24 M478 266 h24 M478 274 h24" '
                      'stroke="#1f5c17" stroke-width=".7"/><ellipse cx="505" cy="200" rx="20" ry="10" fill="#3d9a2f" stroke="#1f5c17"/><path d="M493 200 h24 M493 196 h24 M493 204 h24" '
                      'stroke="#1f5c17" stroke-width=".7"/><ellipse cx="300" cy="280" rx="20" ry="10" fill="#3d9a2f" stroke="#1f5c17"/><path d="M288 280 h24 M288 276 h24 M288 284 h24" '
                      'stroke="#1f5c17" stroke-width=".7"/><ellipse cx="390" cy="75" rx="20" ry="10" fill="#3d9a2f" stroke="#1f5c17"/><path d="M378 75 h24 M378 71 h24 M378 79 h24" stroke="#1f5c17" '
                      'stroke-width=".7"/><ellipse cx="200" cy="150" rx="17" ry="9" fill="#f4b183" stroke="#a5552a"/><path d="M188 150 q4 -6 8 0 q4 6 8 0 q4 -6 8 0" fill="none" '
                      'stroke="#a5552a"/><path d="M150 175 L100 175" stroke="#0A1F3D" stroke-width="1.2"/><circle cx="150" cy="175" r="2.5" fill="#0A1F3D"/><circle cx="100" cy="175" r="13" '
                      'fill="#0A1F3D"/><text x="100" y="180" text-anchor="middle" fill="#fff" font-weight="bold">A</text><path d="M166 250 L100 300" stroke="#0A1F3D" stroke-width="1.2"/><circle '
                      'cx="166" cy="250" r="2.5" fill="#0A1F3D"/><circle cx="100" cy="300" r="13" fill="#0A1F3D"/><text x="100" y="305" text-anchor="middle" fill="#fff" '
                      'font-weight="bold">B</text><path d="M220 200 L100 238" stroke="#0A1F3D" stroke-width="1.2"/><circle cx="220" cy="200" r="2.5" fill="#0A1F3D"/><circle cx="100" cy="238" r="13" '
                      'fill="#0A1F3D"/><text x="100" y="243" text-anchor="middle" fill="#fff" font-weight="bold">C</text><path d="M460 170 L600 170" stroke="#0A1F3D" stroke-width="1.2"/><circle '
                      'cx="460" cy="170" r="2.5" fill="#0A1F3D"/><circle cx="600" cy="170" r="13" fill="#0A1F3D"/><text x="600" y="175" text-anchor="middle" fill="#fff" '
                      'font-weight="bold">D</text><path d="M527 110 L600 110" stroke="#0A1F3D" stroke-width="1.2"/><circle cx="527" cy="110" r="2.5" fill="#0A1F3D"/><circle cx="600" cy="110" r="13" '
                      'fill="#0A1F3D"/><text x="600" y="115" text-anchor="middle" fill="#fff" font-weight="bold">E</text><path d="M183 150 L100 130" stroke="#0A1F3D" stroke-width="1.2"/><circle '
                      'cx="183" cy="150" r="2.5" fill="#0A1F3D"/><circle cx="100" cy="130" r="13" fill="#0A1F3D"/><text x="100" y="135" text-anchor="middle" fill="#fff" '
                      'font-weight="bold">F</text><text x="350" y="326" text-anchor="middle" font-size="11" fill="#5b6676">Not to scale. Real plant cells have many more chloroplasts and '
                      'mitochondria.</text></svg>',
            'html': '<p>A plant cell has the same parts you learned last week: a cell membrane, cytoplasm, a nucleus, mitochondria, ribosomes, ER and Golgi. It also has three parts animal cells '
                    'lack.</p><ul><li><b>Cell wall:</b> a stiff layer outside the membrane, made mostly of cellulose. It supports the cell and protects it. Wood, cotton and paper are made of plant '
                    'cell walls.</li><li><b>Chloroplasts:</b> green organelles that capture light energy and make food. Their green pigment is <b>chlorophyll</b>.</li><li><b>Central vacuole:</b> one '
                    'large sac that can fill much of the cell. It stores water. When it is full, it presses outward against the wall and keeps the plant firm. When a plant goes too long without '
                    'water, the vacuoles shrink and the plant wilts. Next week you will learn how water moves into those vacuoles, a process called osmosis.</li></ul><p>Notice that plant cells still '
                    'have mitochondria. Plants make food in chloroplasts, then release its energy in mitochondria, just as you do.</p>',
            'checks': [{'t': 'label',
                        'q': 'Name each lettered part of the plant cell. Choose from: cell wall, cell membrane, chloroplast, central vacuole, nucleus, mitochondrion.',
                        'labels': [['A', ['cell wall', 'wall']],
                                   ['B', [{'all': [['cell membrane', 'plasma membrane', 'membrane']], 'none': ['nuclear', 'vacuole', 'wall', 'not']}]],
                                   ['C', ['chloroplast', 'chloroplasts']],
                                   ['D', ['central vacuole', 'vacuole']],
                                   ['E', ['nucleus']],
                                   ['F', ['mitochondrion', 'mitochondria']]],
                        'pts': 6,
                        'why': 'A is the thick outer wall. B is the membrane just inside it. C is a green chloroplast. D is the large central vacuole. E is the nucleus. F is a mitochondrion, the '
                               'orange bean shape with folds.'},
                       {'t': 'open',
                        'key': 'wilt',
                        'q': 'A potted basil plant droops on a hot afternoon. An hour after watering, it stands up again. Explain what happened inside its cells.',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Without water the central vacuoles shrank and stopped pressing on the cell walls, so the plant wilted',
                                   'Water refilled the vacuoles, which pushed against the walls and made the cells firm again'],
                        'model': 'Without enough water, the central vacuoles shrank and stopped pushing on the cell walls, so the cells went soft and the plant drooped. After watering, the vacuoles '
                                 'filled up again, pressed against the stiff walls and made the cells firm, so the plant stood up.'},
                       {'t': 'open',
                        'key': 'mitoplant',
                        'q': 'A classmate says, "Plants have chloroplasts instead of mitochondria." Correct the statement and explain why plants need both.',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Plants have both chloroplasts and mitochondria', 'Chloroplasts make food (glucose); mitochondria release energy from that food'],
                        'model': 'That is not right: plants have both. Chloroplasts use light to make glucose, and mitochondria release the energy stored in that glucose so the cell can use it, day '
                                 'and night.'}]},
           {'title': 'Plant and Animal Cells Compared',
            'visual': '<svg viewBox="0 0 640 295" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Venn diagram comparing plant and animal cells"><text '
                      'x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Plant cells and animal cells</text><circle cx="245" cy="160" r="128" fill="#3d9a2f" '
                      'fill-opacity=".18" stroke="#3d6b1f" stroke-width="2"/><circle cx="395" cy="160" r="128" fill="#DB2F30" fill-opacity=".12" stroke="#DB2F30" stroke-width="2"/><text x="185" '
                      'y="88" text-anchor="middle" font-weight="bold" font-size="13">Plant only</text><text x="455" y="88" text-anchor="middle" font-weight="bold" font-size="13">Animal '
                      'only</text><text x="320" y="78" text-anchor="middle" font-weight="bold" font-size="13">Both</text><text x="185" y="125" text-anchor="middle">cell wall</text><text x="185" '
                      'y="148" text-anchor="middle">chloroplasts</text><text x="185" y="171" text-anchor="middle">one large central</text><text x="185" y="186" '
                      'text-anchor="middle">vacuole</text><text x="185" y="209" text-anchor="middle">fixed, boxy shape</text><text x="320" y="112" text-anchor="middle" font-size="11">cell '
                      'membrane</text><text x="320" y="134" text-anchor="middle">nucleus</text><text x="320" y="156" text-anchor="middle">cytoplasm</text><text x="320" y="178" '
                      'text-anchor="middle">mitochondria</text><text x="320" y="200" text-anchor="middle">ribosomes</text><text x="320" y="222" text-anchor="middle">ER, Golgi</text><text x="455" '
                      'y="125" text-anchor="middle">no cell wall</text><text x="455" y="148" text-anchor="middle">small vacuoles,</text><text x="455" y="163" text-anchor="middle">if any</text><text '
                      'x="455" y="186" text-anchor="middle">lysosomes</text><text x="455" y="201" text-anchor="middle">common</text><text x="455" y="224" text-anchor="middle">flexible '
                      'shape</text></svg>',
            'html': '<p>Plant and animal cells share most of their parts because both are eukaryotic cells: their DNA is kept inside a nucleus. The differences match how each organism lives. A plant '
                    'cannot walk to find food or shelter, so it makes its own food and builds stiff walls to stand tall toward the light. An animal moves and eats other living things, so its cells '
                    'have flexible membranes without a wall.</p><p>Under a microscope, plant cells often look like neat bricks in rows, because of the walls. Animal cells, like the ones in last '
                    "week's diagrams, look rounder and more irregular.</p>",
            'checks': [{'t': 'open',
                        'key': 'which',
                        'q': 'A scientist looks at an unknown cell. It has a nucleus, mitochondria and a cell membrane, but no cell wall and no chloroplasts. Is it more likely a plant cell or an '
                             'animal cell? Give two pieces of evidence.',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Animal cell', 'Evidence: no cell wall and no chloroplasts (parts both share do not decide it)'],
                        'model': 'It is more likely an animal cell, because it has no cell wall and no chloroplasts, which plant cells have. The nucleus, mitochondria and membrane do not help '
                                 'decide, because both kinds of cells have them.'},
                       {'t': 'open',
                        'key': 'roots',
                        'q': 'Root cells deep in the soil are plant cells, but they have few or no chloroplasts. Why does that make sense?',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Roots get no light underground, so chloroplasts would not help', 'Roots can get food made in other parts of the plant, such as the leaves (reasoned inference)'],
                        'model': 'Chloroplasts need light, and roots are underground in the dark, so chloroplasts would be useless there. Roots get sugar made in the leaves, and their job is to take '
                                 'in water and minerals.'},
                       {'t': 'open',
                        'key': 'shape',
                        'q': 'Explain how the cell wall and the central vacuole work together to help a plant stand up without a skeleton.',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['The full vacuole pushes outward', 'The stiff wall pushes back, so the cell stays firm, like an inflated tire or a water balloon in a box'],
                        'model': 'The full vacuole pushes outward like an inflated balloon, and the stiff wall pushes back. Together they make each cell firm, and millions of firm cells hold the '
                                 'plant up.'}]},
           {'title': 'Photosynthesis: Making Food from Light',
            'visual': '<svg viewBox="0 0 700 260" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Diagram of photosynthesis in a leaf"><text x="350" '
                      'y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Photosynthesis: what goes in, what comes out</text><circle cx="80" cy="70" r="28" '
                      'fill="#F7C948"/><line x1="116" y1="70" x2="128" y2="70" stroke="#F7C948" stroke-width="3"/><line x1="44" y1="70" x2="32" y2="70" stroke="#F7C948" stroke-width="3"/><line '
                      'x1="80" y1="106" x2="80" y2="118" stroke="#F7C948" stroke-width="3"/><line x1="80" y1="34" x2="80" y2="22" stroke="#F7C948" stroke-width="3"/><line x1="105.2" y1="95.2" '
                      'x2="113.6" y2="103.6" stroke="#F7C948" stroke-width="3"/><line x1="54.8" y1="95.2" x2="46.400000000000006" y2="103.6" stroke="#F7C948" stroke-width="3"/><line x1="105.2" '
                      'y1="44.8" x2="113.6" y2="36.400000000000006" stroke="#F7C948" stroke-width="3"/><line x1="54.8" y1="44.8" x2="46.400000000000006" y2="36.400000000000006" stroke="#F7C948" '
                      'stroke-width="3"/><text x="80" y="125" text-anchor="middle" font-weight="bold">light energy</text><path d="M120 95 L265 135" stroke="#C9A84C" stroke-width="3" '
                      'marker-end="url(#ah)"/><defs><marker id="ah" viewBox="0 0 10 10" markerWidth="4" markerHeight="4" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10Z" '
                      'fill="#0A1F3D"/></marker></defs><path d="M270 150 Q350 60 440 150 Q350 240 270 150Z" fill="#3d9a2f" stroke="#1f5c17" stroke-width="2"/><path d="M270 150 H440" '
                      'stroke="#1f5c17"/><text x="355" y="140" text-anchor="middle" fill="#fff" font-weight="bold">chloroplasts</text><text x="355" y="168" text-anchor="middle" fill="#fff" '
                      'font-size="11">in leaf cells</text><text x="80" y="185" text-anchor="middle" font-weight="bold" fill="#0047BA">carbon dioxide</text><text x="80" y="201" text-anchor="middle" '
                      'font-size="11">from the air, through stomata</text><path d="M150 185 L265 160" stroke="#0047BA" stroke-width="3" marker-end="url(#ah)"/><text x="355" y="252" '
                      'text-anchor="middle" font-weight="bold" fill="#0047BA">water from the roots</text><path d="M355 236 L355 205" stroke="#0047BA" stroke-width="3" marker-end="url(#ah)"/><path '
                      'd="M445 130 L560 95" stroke="#DB2F30" stroke-width="3" marker-end="url(#ah)"/><text x="620" y="90" text-anchor="middle" font-weight="bold" fill="#DB2F30">oxygen</text><text '
                      'x="620" y="106" text-anchor="middle" font-size="11">released into the air</text><path d="M445 170 L560 200" stroke="#DB2F30" stroke-width="3" marker-end="url(#ah)"/><text '
                      'x="620" y="205" text-anchor="middle" font-weight="bold" fill="#DB2F30">glucose (sugar)</text><text x="620" y="221" text-anchor="middle" font-size="11">food the plant uses and '
                      'stores</text></svg>',
            'html': '<p>Inside chloroplasts, plants carry out <b>photosynthesis</b>. They take in <b>carbon dioxide</b> from the air through tiny openings called <b>stomata</b>, and <b>water</b> '
                    'from the soil through their roots. Chlorophyll absorbs <b>light energy</b>, and the chloroplast uses that energy to turn the carbon dioxide and water into <b>glucose</b>, a '
                    "sugar that stores energy. <b>Oxygen</b> is released as a by-product.</p><div class='callout'><b>In words:</b> carbon dioxide + water + light energy → glucose + oxygen<br><b>In "
                    'symbols:</b> 6CO<sub>2</sub> + 6H<sub>2</sub>O + light → C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + 6O<sub>2</sub></div><p>The plant uses glucose for energy, builds it into '
                    'cellulose for its walls and stores it as starch in seeds, roots and fruit. Sugar made in the leaves travels through tubes to the stems, roots and fruit. When you eat rice, '
                    'cassava, bread or a mango, you are eating energy that a plant captured from sunlight. Even the meat and milk you eat came from animals that ate plants. That is why plants are '
                    'called <b>producers</b>.</p><p>Notice that the mass of a tree comes mostly from the <b>air</b>. Each carbon atom in its wood was once in carbon dioxide gas.</p>',
            'checks': [{'t': 'blanks',
                        'q': 'Complete the summary of photosynthesis.',
                        'sent': 'Plants take in carbon dioxide and ___. Using ___ energy, they make the sugar ___ and release ___.',
                        'blanks': [['water', 'h2o'], ['light', 'sunlight', 'solar', 'sun'], ['glucose', 'c6h12o6'], ['oxygen', 'o2']],
                        'show': 'water; light; glucose; oxygen',
                        'pts': 4,
                        'why': 'carbon dioxide + water + light energy → glucose + oxygen.'},
                       {'t': 'num',
                        'q': 'Count the atoms. How many oxygen atoms are on the left side of the equation 6CO<sub>2</sub> + 6H<sub>2</sub>O?',
                        'a': 18,
                        'unit': 'atoms',
                        'pts': 3,
                        'why': '6CO<sub>2</sub> has 6 × 2 = 12 oxygen atoms and 6H<sub>2</sub>O has 6 × 1 = 6, so 12 + 6 = 18. The right side also has 18: 6 in glucose and 12 in 6O<sub>2</sub>. '
                               'Atoms are rearranged, never lost.'},
                       {'t': 'open',
                        'key': 'treemass',
                        'q': "A seedling grows into a tree weighing thousands of kilograms, but the soil around it barely changes in mass. Where did most of the tree's mass come from? Use what you "
                             'know about photosynthesis.',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Mostly from carbon dioxide in the air (plus water)',
                                   'Photosynthesis builds glucose and then cellulose and wood from those atoms; soil supplies only small amounts of minerals'],
                        'model': 'Most of the mass came from carbon dioxide in the air, along with water. Photosynthesis joins those atoms into glucose, which the tree builds into cellulose and '
                                 'wood. The soil only gives small amounts of minerals.'},
                       {'t': 'open',
                        'key': 'manatee',
                        'q': 'Return to the manatees. Explain the chain from algae blooms to starving manatees, using the words light, photosynthesis and producer.',
                        'min': 35,
                        'rows': 4,
                        'rubric': ['Algae clouded the water and blocked light', 'Seagrass could not carry out photosynthesis and died', 'Seagrass is the producer manatees depend on, so they starved'],
                        'model': 'Algae blooms clouded the water and blocked the light. Without light, the seagrass could not carry out photosynthesis to make food, so it died. Seagrass is the '
                                 "producer at the base of the manatees' food chain, so with no seagrass the manatees starved."}]},
           {'title': 'How Scientists Discovered It',
            'html': '<p>People once thought plants grew by "eating" soil. In the early 1600s, Flemish scientist Jan Baptist van Helmont grew a willow tree in a pot for five years (his results were '
                    'published in 1648, after his death). The tree gained about 74 kilograms, but the soil lost only about 57 grams. He concluded the mass came from water. He was partly right; he '
                    'did not know about carbon dioxide yet.</p><p>In 1771, English chemist <b>Joseph Priestley</b> placed a burning candle in a sealed jar until it went out. Then he put a sprig of '
                    'mint in the jar. After several days, a candle could burn in that air again. The plant had "restored" the air; today we know it released oxygen.</p><p>In 1779, Dutch scientist '
                    '<b>Jan Ingenhousz</b> repeated these experiments and found the key piece: plants restore the air only in <b>light</b>, and only their green parts do it. Each scientist built on '
                    'the one before, which is how science works.</p>',
            'checks': [{'t': 'open',
                        'key': 'helmont',
                        'q': "Van Helmont's willow gained about 74 kg while the soil lost only 57 g. What did this evidence disprove, and what did he miss?",
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Disproved that plants get their mass mostly from soil', 'Missed carbon dioxide from the air (he credited water only)'],
                        'model': 'It disproved the idea that plants grow by eating soil. He concluded the mass came from water, but he missed that most of it comes from carbon dioxide in the air.'},
                       {'t': 'open',
                        'key': 'ingen',
                        'q': "How did Ingenhousz's discovery add to Priestley's? What variable did Ingenhousz test?",
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Priestley showed plants restore air; Ingenhousz showed this needs light and green parts', 'Variable tested: light (and green versus non-green parts)'],
                        'model': 'Priestley showed that plants restore the air. Ingenhousz tested light and found plants do it only in light and only with their green parts, which showed that light '
                                 'is needed.'}]}],
 'handson': {'title': 'Floating Leaf Disks: Watch Photosynthesis Happen',
             'intro': 'Leaf disks sink when the air inside them is replaced by water. As photosynthesis makes oxygen, bubbles collect and the disks float. Counting floating disks lets you measure '
                      'photosynthesis.',
             'materials': ['Fresh spinach leaves',
                           'A drinking straw or a single-hole paper punch',
                           'Baking soda (adds carbon dioxide to the water)',
                           'Dish soap',
                           "A plastic syringe without a needle (10 mL or larger, from a pharmacy or a children's medicine kit)",
                           'Two clear cups and water',
                           'A bright lamp or a sunny window',
                           'Aluminum foil or a box (for the dark trial)',
                           'A timer, paper and pencil'],
             'steps': ['Mix 1/8 teaspoon of baking soda and one small drop of dish soap into 1 cup of water. Pour half into Cup A. Fill Cup B with plain water and a drop of soap only (no baking '
                       'soda).',
                       'Punch 20 disks from the spinach, avoiding the big veins.',
                       'Put 10 disks in the syringe, draw in some baking-soda water, cover the tip with your finger and pull the plunger back gently to pull the air out of the disks. Repeat until '
                       'they sink. Do the same with the other 10 disks using the plain water.',
                       'Put the sunk disks in their cups and place both cups under the same bright light. Keep the lamp at least 30 cm from the cups so the water does not heat up.',
                       'Every minute for 15 minutes, count how many disks are floating in each cup and record it.',
                       'Extra trial: prepare 10 more sunk disks in baking-soda water, cover that cup with foil or a box to keep it dark, and compare.'],
             'record': [{'t': 'open',
                         'key': 'diskdata',
                         'q': 'Make a data table with the minute and the number of floating disks in Cup A and Cup B. What pattern do you see?',
                         'min': 30,
                         'rows': 6,
                         'rubric': ['Complete table for both cups', 'Clear description of the pattern'],
                         'model': 'Minute 5: A 1, B 0. Minute 10: A 6, B 0. Minute 15: A 10, B 1. Disks in the baking-soda cup floated much faster than disks in plain water.'},
                        {'t': 'open',
                         'key': 'diskcer',
                         'q': 'Write a claim, evidence and reasoning (CER) explaining your results. Name the independent variable, the dependent variable and one variable you kept the same.',
                         'min': 60,
                         'rows': 6,
                         'rubric': ['Claim: photosynthesis needs carbon dioxide (or light, for the dark trial)',
                                    'Evidence: specific counts from the data table',
                                    'Reasoning: photosynthesis made oxygen, which collected in the disks and made them float',
                                    'Independent variable: baking soda (carbon dioxide) or light; dependent: number of floating disks; controlled: same light, leaves, water amount, soap, time'],
                         'model': 'Claim: Spinach disks carry out photosynthesis faster when carbon dioxide is available. Evidence: After 15 minutes, all 10 disks floated in the baking-soda cup, but '
                                  'only 1 floated in plain water. Reasoning: Baking soda adds carbon dioxide to the water. Photosynthesis used it to make oxygen, and the oxygen bubbles filled the '
                                  'disks and made them float. Without carbon dioxide, little photosynthesis happened. The independent variable was baking soda, the dependent variable was the number '
                                  'of floating disks, and I kept the light, the spinach and the amount of water the same.'}]},
 'think': {'intro': 'Use evidence and explain your reasoning. Your teacher scores these.',
           'items': [{'t': 'open',
                      'key': 'breakfast',
                      'q': 'Trace the energy in your breakfast back to the Sun. Pick two foods (one from a plant and one from an animal) and explain each chain step by step.',
                      'min': 80,
                      'rows': 8,
                      'rubric': ['Plant food traced to photosynthesis capturing light',
                                 'Animal food traced through the animal eating plants back to photosynthesis',
                                 'Uses producer and glucose or stored energy correctly',
                                 'Clear step-by-step reasoning'],
                      'model': 'My oatmeal comes from oats. The oat plant used light energy in photosynthesis to make glucose, which it stored as starch in its seeds, and I ate the seeds. My egg '
                               'came from a chicken. The chicken ate corn and seeds, and those plants made their food through photosynthesis using sunlight. So the energy in the egg passed from the '
                               'Sun to the plants, which are producers, to the chicken, and then to me.'},
                     {'t': 'open',
                      'key': 'design',
                      'q': 'Design your own leaf-disk experiment to test whether light color (for example red, green or blue cellophane) changes the rate of photosynthesis. Write a question, a '
                           'hypothesis, your variables and how you would measure the results.',
                      'min': 70,
                      'rows': 7,
                      'rubric': ['Testable question and hypothesis with reasoning',
                                 'Independent variable (light color), dependent variable (disks floating over time), controlled variables',
                                 'Clear measurement plan with repeated trials'],
                      'model': 'Question: Does light color change how fast spinach disks float? Hypothesis: Disks under green light will float slowest, because leaves look green when they reflect '
                               'green light instead of absorbing it. Independent variable: the color of cellophane over each cup. Dependent variable: the number of floating disks each minute for 15 '
                               'minutes. Controlled: same lamp and distance, same baking-soda solution, same number of disks, same spinach. I would repeat each color three times and compare the '
                               'averages.'}]},
 'exit': [{'t': 'open',
           'key': 'exit_three',
           'q': 'Name the three parts plant cells have that animal cells lack, with one job for each.',
           'min': 15,
           'rows': 3,
           'rubric': ['Cell wall: support and protection', 'Chloroplast: photosynthesis, makes food', 'Central vacuole: stores water, keeps cell firm'],
           'model': 'The cell wall supports and protects the cell, chloroplasts make food by photosynthesis, and the central vacuole stores water and keeps the cell firm.'},
          {'t': 'text',
           'q': 'Through what tiny openings does carbon dioxide enter a leaf?',
           'a': ['stomata', 'stoma', 'stomates'],
           'show': 'stomata',
           'pts': 2,
           'why': 'Stomata, mostly on the underside of leaves, let carbon dioxide in and oxygen and water vapor out.'},
          {'t': 'text',
           'q': 'Which green pigment in chloroplasts absorbs light energy?',
           'a': ['chlorophyll'],
           'show': 'chlorophyll',
           'pts': 2,
           'why': 'Chlorophyll absorbs light and reflects green, which is why leaves look green.'},
          {'t': 'open',
           'key': 'exit_dark',
           'q': 'Predict what would happen to a cup of leaf disks kept completely dark, and explain why.',
           'min': 15,
           'rows': 2,
           'rubric': ['Few or no disks float', 'No light means no photosynthesis, so no oxygen is made'],
           'model': 'Few or none would float, because without light photosynthesis cannot happen, so no oxygen bubbles form in the disks.'}],
 'next': 'Week 9: how water, oxygen and food move in and out of cells through the membrane, by diffusion and osmosis.'}

TEACHER = {
 "standards": [
  "SC.6.L.14.4: Compare and contrast the structure and function of major organelles of plant and animal cells, including cell wall, cell membrane, nucleus, cytoplasm, chloroplasts, mitochondria, and vacuoles.",
  "SC.8.L.18.1 (preview): Describe and investigate the process of photosynthesis, such as the roles of light, carbon dioxide, water and chlorophyll; production of food; release of oxygen.",
  "SC.6.N.1.1: Define a problem from the sixth grade curriculum, use appropriate reference materials to support scientific understanding, plan and carry out scientific investigation of various types, such as systematic observations or experiments, identify variables, collect and organize data, interpret data in charts, tables, and graphics, analyze information, make predictions, and defend conclusions.",
  "SC.6.N.2.2: Explain that scientific knowledge is durable because it is open to change as new evidence or interpretations are encountered.",
  "NGSS MS-LS1-6: Construct a scientific explanation based on evidence for the role of photosynthesis in the cycling of matter and flow of energy into and out of organisms."],
 "materials": ["The interactive lesson", "Fresh spinach, a straw or hole punch, baking soda, dish soap, a needle-free plastic syringe, two clear cups, a bright lamp, a timer", "Optional: red, green and blue cellophane for the challenge design", "Optional: a microscope and an onion skin or Elodea leaf", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 7 Reconnect questions."],
  [6, "Hook", "Tell the manatee story and pose the big question."],
  [10, "Plant cell parts", "Label the diagram together. Wilt and revive a plant or a celery stalk if you have one."],
  [8, "Compare", "Build the Venn diagram. If a microscope is available, look at onion skin again (Week 6) and compare it with last week's animal cell diagram: now the student can explain the boxes."],
  [12, "Photosynthesis", "Work through the inputs and outputs and count atoms. Return to the manatees."],
  [6, "History", "Van Helmont, Priestley and Ingenhousz: how each built on the last."],
  [12, "Leaf disks", "Set up the investigation together (the syringe step is fiddly). Counting continues for 15 minutes after the lesson; the student records."]],
 "key_questions": ["What would happen to this plant cell without its wall? Without its vacuole?", "Where does a tree's mass come from?", "How do we know the oxygen came from photosynthesis?", "Which variable did we change, and which did we keep the same?"],
 "misconceptions": ["Plants get their food from the soil.", "Plants have chloroplasts instead of mitochondria.", "Plants carry out photosynthesis, and animals carry out respiration (plants respire too).", "A tree's mass comes from the soil.", "The cell wall replaces the cell membrane."],
 "support": ["Give a labeled plant cell card to keep.", "Provide a fill-in inputs and outputs chart.", "Count the floating disks together for the first five minutes."],
 "challenge": ["Run the light-color design from Think Deeper.", "Research the Florida seagrass and manatee recovery work since 2021 and explain what reducing pollution does for light levels."],
 "background": "<p>Florida Fish and Wildlife Conservation Commission recorded a record 1,101 manatee deaths in 2021, many from starvation linked to seagrass loss in the Indian River Lagoon after repeated algal blooms reduced light. The leaf-disk assay is a standard classroom protocol: sodium bicarbonate supplies dissolved carbon dioxide, soap wets the hydrophobic leaf surface, and oxygen from photosynthesis accumulates in the spongy mesophyll, making disks buoyant; respiration also uses some oxygen, so results reflect net photosynthesis. In Florida, photosynthesis is formally a Grade 8 benchmark (SC.8.L.18.1); it is included here because plant cell organelles (SC.6.L.14.4) cannot be understood without the chloroplast's job. Van Helmont's willow experiment (published 1648): about 164 lb (74 kg) gained versus about 2 oz (57 g) of soil lost. Priestley (1771) and Ingenhousz (Experiments upon Vegetables, 1779).</p>",
 "sources": ["Florida Fish and Wildlife Conservation Commission, Manatee Mortality Event Along the East Coast, 2020-2022.", "Science Buddies and BSCS, Floating Leaf Disk Assay for Investigating Photosynthesis.", "Ingenhousz, J. (1779), Experiments upon Vegetables.", "Priestley, J. (1772), Observations on Different Kinds of Air, Philosophical Transactions.", "CK-12 Life Science, Photosynthesis."]
}

PRINT = {
 "directions": "Use complete sentences.",
 "items": [
  {"q":"Draw a plant cell and label the cell wall, cell membrane, chloroplast, central vacuole, nucleus and a mitochondrion.","a":"Wall outside the membrane; green chloroplasts; one large central vacuole; nucleus; mitochondrion.","lines":2},
  {"q":"Name two parts both plant and animal cells have and two parts only plant cells have.","a":"Both: nucleus, cell membrane, mitochondria, cytoplasm. Plant only: cell wall, chloroplasts, central vacuole.","lines":2},
  {"q":"Write the word equation for photosynthesis.","a":"carbon dioxide + water + light energy → glucose + oxygen","lines":2},
  {"q":"Why do roots have few or no chloroplasts?","a":"Roots are in the dark underground, so chloroplasts would not help.","lines":2},
  {"q":"In the leaf-disk activity, why did the disks float?","a":"Photosynthesis made oxygen, which collected in the disks.","lines":2},
  {"q":"How did Ingenhousz build on Priestley's work?","a":"He showed that plants restore the air only in light and only with their green parts.","lines":2}]
}
