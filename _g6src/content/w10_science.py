MAP = ('<svg viewBox="0 0 660 270" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Concept map of Unit 2 cell ideas">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Unit 2 concept map: how the big ideas connect</text>'
  '<defs><marker id="cm" viewBox="0 0 10 10" markerWidth="5" markerHeight="5" refX="9" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="#0A1F3D"/></marker></defs>'
  + ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="40" rx="8" fill="{c}"/><text x="{x+w/2}" y="{y+17}" text-anchor="middle" fill="#fff" font-weight="bold">{t1}</text><text x="{x+w/2}" y="{y+32}" text-anchor="middle" fill="#fff" font-size="11">{t2}</text>'
            for x, y, w, c, t1, t2 in [(250, 34, 160, "#0A1F3D", "CELL THEORY", "Week 6"),
                                       (40, 120, 170, "#0047BA", "Organelles do jobs", "Week 7"),
                                       (245, 120, 170, "#3d9a2f", "Plant cells: wall,", "chloroplasts, vacuole (Wk 8)"),
                                       (450, 120, 170, "#C9A84C", "Membrane controls", "what crosses (Week 9)"),
                                       (40, 210, 170, "#6b3fa0", "Mitochondria release", "energy from glucose"),
                                       (245, 210, 170, "#3d9a2f", "Photosynthesis makes", "glucose and oxygen"),
                                       (450, 210, 170, "#C9A84C", "Diffusion, osmosis,", "active transport")]) +
  ''.join(f'<path d="M{a} {b} L{c} {d}" stroke="#0A1F3D" stroke-width="1.5" marker-end="url(#cm)"/>' for a, b, c, d in [(300, 74, 140, 118), (330, 74, 330, 118), (360, 74, 520, 118), (125, 160, 125, 208), (330, 160, 330, 208), (535, 160, 535, 208)]) +
  '<path d="M245 230 L212 230" stroke="#DB2F30" stroke-width="2" marker-end="url(#cm)"/><text x="228" y="204" text-anchor="middle" font-size="10" fill="#DB2F30">fuel</text>'
  '<path d="M450 230 L417 230" stroke="#DB2F30" stroke-width="2" marker-end="url(#cm)"/><text x="433" y="196" text-anchor="middle" font-size="10" fill="#DB2F30">CO₂ and</text><text x="433" y="207" text-anchor="middle" font-size="10" fill="#DB2F30">water in</text>'
  '<text x="330" y="266" text-anchor="middle" font-size="11" fill="#5b6676">Red arrows show how processes depend on each other.</text></svg>')

ENDO = ('<svg viewBox="0 0 640 215" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Endosymbiosis: a large cell takes in a smaller cell that becomes a mitochondrion">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Endosymbiosis: one cell living inside another</text>'
  '<ellipse cx="110" cy="105" rx="80" ry="58" fill="#e8f4fb" stroke="#0047BA" stroke-width="2"/><circle cx="95" cy="100" r="18" fill="#e8d7f5" stroke="#6b3fa0"/>'
  '<ellipse cx="215" cy="70" rx="20" ry="10" fill="#f4b183" stroke="#a5552a"/><path d="M232 70 h14" stroke="#0A1F3D" stroke-width="2"/><path d="M200 76 l-18 14" stroke="#0A1F3D" stroke-width="2" marker-end="url(#ea)"/>'
  '<defs><marker id="ea" viewBox="0 0 10 10" markerWidth="5" markerHeight="5" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="#0A1F3D"/></marker></defs>'
  '<text x="130" y="186" text-anchor="middle" font-weight="bold">1. A large cell takes in a</text><text x="130" y="200" text-anchor="middle" font-weight="bold" font-size="11">smaller bacterium</text>'
  '<path d="M262 105 h40" stroke="#0A1F3D" stroke-width="2" marker-end="url(#ea)"/>'
  '<ellipse cx="400" cy="105" rx="80" ry="58" fill="#e8f4fb" stroke="#0047BA" stroke-width="2"/><circle cx="385" cy="100" r="18" fill="#e8d7f5" stroke="#6b3fa0"/><ellipse cx="430" cy="125" rx="20" ry="10" fill="#f4b183" stroke="#a5552a"/><ellipse cx="430" cy="125" rx="25" ry="14" fill="none" stroke="#0047BA" stroke-dasharray="3 2"/>'
  '<text x="400" y="186" text-anchor="middle" font-weight="bold">2. It is not digested;</text><text x="400" y="200" text-anchor="middle" font-weight="bold" font-size="11">it lives inside and makes energy</text>'
  '<path d="M490 105 h30" stroke="#0A1F3D" stroke-width="2" marker-end="url(#ea)"/>'
  '<text x="580" y="80" text-anchor="middle" font-weight="bold" fill="#a5552a">3. Over time it</text><text x="580" y="96" text-anchor="middle" font-weight="bold" fill="#a5552a">becomes a</text><text x="580" y="112" text-anchor="middle" font-weight="bold" fill="#a5552a">mitochondrion</text><text x="580" y="134" text-anchor="middle" font-size="11">(chloroplasts formed</text><text x="580" y="148" text-anchor="middle" font-size="11">the same way)</text></svg>')

LESSON = {'unit': 'Unit 2: Cells, the Building Blocks of Life',
 'title': 'Unit 2 Checkpoint and Cell Model Project',
 'subtitle': 'Connect the big ideas of Unit 2, investigate a surprising idea about where mitochondria came from, build a cell model and show what you know on the checkpoint.',
 'objectives': ['Explain how cell theory, organelles, plant cells and membrane transport connect.',
                'Evaluate the evidence that mitochondria and chloroplasts were once free-living bacteria.',
                'Plan a scale-minded cell model with an analogy and a key.',
                'Show mastery of Unit 2 on the checkpoint (85 or higher).'],
 'vocab': [['concept map', 'A diagram that shows how ideas connect, with arrows and linking words.'],
           ['endosymbiosis', 'The idea that some organelles began as bacteria living inside another cell.'],
           ['model', 'A representation that helps explain something too small, large or complex to see directly.'],
           ['analogy', 'A comparison that explains something by showing how it is like something familiar.'],
           ['key (legend)', 'A list that explains what each part or color of a model stands for.']],
 'reconnect': {'title': 'Week 9: Moving in and out of cells',
               'intro': 'Start with last week, then sweep back through the unit.',
               'items': [{'t': 'text', 'q': 'What is the name for the diffusion of water across a membrane?', 'a': ['osmosis'], 'show': 'osmosis', 'pts': 2, 'why': 'Osmosis.'},
                         {'t': 'text',
                          'q': 'A potato strip is placed in very salty water. Will it get longer or shorter?',
                          'a': [{'all': [['short']], 'none': ['long', 'not']}],
                          'show': 'shorter',
                          'pts': 2,
                          'why': 'The strip gets shorter. You will explain why on the checkpoint.'},
                         {'t': 'open',
                          'key': 'rc_active',
                          'q': 'Which kind of transport needs energy, and which organelle supplies that energy?',
                          'min': 10,
                          'rows': 2,
                          'rubric': ['Names the energy-using kind of transport and the organelle that releases energy from glucose'],
                          'model': 'Active transport needs energy, and the mitochondria supply it by releasing energy from glucose.'},
                         {'t': 'open',
                          'key': 'rc_mito',
                          'q': 'Week 8: Plant cells have chloroplasts. Do they also have mitochondria? Explain.',
                          'min': 12,
                          'rows': 2,
                          'rubric': ['Yes; plants also release energy from glucose in mitochondria'],
                          'model': 'Yes. Chloroplasts make glucose, but plant cells still need mitochondria to release the energy stored in it.'}]},
 'hook': {'title': 'One Big Connected Story',
          'visual': '<svg viewBox="0 0 660 270" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Concept map of Unit 2 cell ideas"><text x="330" y="20" '
                    'text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Unit 2 concept map: how the big ideas connect</text><defs><marker id="cm" viewBox="0 0 10 10" '
                    'markerWidth="5" markerHeight="5" refX="9" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="#0A1F3D"/></marker></defs><rect x="250" y="34" width="160" height="40" rx="8" '
                    'fill="#0A1F3D"/><text x="330.0" y="51" text-anchor="middle" fill="#fff" font-weight="bold">CELL THEORY</text><text x="330.0" y="66" text-anchor="middle" fill="#fff" '
                    'font-size="11">Week 6</text><rect x="40" y="120" width="170" height="40" rx="8" fill="#0047BA"/><text x="125.0" y="137" text-anchor="middle" fill="#fff" '
                    'font-weight="bold">Organelles do jobs</text><text x="125.0" y="152" text-anchor="middle" fill="#fff" font-size="11">Week 7</text><rect x="245" y="120" width="170" height="40" '
                    'rx="8" fill="#3d9a2f"/><text x="330.0" y="137" text-anchor="middle" fill="#fff" font-weight="bold">Plant cells: wall,</text><text x="330.0" y="152" text-anchor="middle" '
                    'fill="#fff" font-size="11">chloroplasts, vacuole (Wk 8)</text><rect x="450" y="120" width="170" height="40" rx="8" fill="#C9A84C"/><text x="535.0" y="137" text-anchor="middle" '
                    'fill="#fff" font-weight="bold">Membrane controls</text><text x="535.0" y="152" text-anchor="middle" fill="#fff" font-size="11">what crosses (Week 9)</text><rect x="40" y="210" '
                    'width="170" height="40" rx="8" fill="#6b3fa0"/><text x="125.0" y="227" text-anchor="middle" fill="#fff" font-weight="bold">Mitochondria release</text><text x="125.0" y="242" '
                    'text-anchor="middle" fill="#fff" font-size="11">energy from glucose</text><rect x="245" y="210" width="170" height="40" rx="8" fill="#3d9a2f"/><text x="330.0" y="227" '
                    'text-anchor="middle" fill="#fff" font-weight="bold">Photosynthesis makes</text><text x="330.0" y="242" text-anchor="middle" fill="#fff" font-size="11">glucose and '
                    'oxygen</text><rect x="450" y="210" width="170" height="40" rx="8" fill="#C9A84C"/><text x="535.0" y="227" text-anchor="middle" fill="#fff" font-weight="bold">Diffusion, '
                    'osmosis,</text><text x="535.0" y="242" text-anchor="middle" fill="#fff" font-size="11">active transport</text><path d="M300 74 L140 118" stroke="#0A1F3D" stroke-width="1.5" '
                    'marker-end="url(#cm)"/><path d="M330 74 L330 118" stroke="#0A1F3D" stroke-width="1.5" marker-end="url(#cm)"/><path d="M360 74 L520 118" stroke="#0A1F3D" stroke-width="1.5" '
                    'marker-end="url(#cm)"/><path d="M125 160 L125 208" stroke="#0A1F3D" stroke-width="1.5" marker-end="url(#cm)"/><path d="M330 160 L330 208" stroke="#0A1F3D" stroke-width="1.5" '
                    'marker-end="url(#cm)"/><path d="M535 160 L535 208" stroke="#0A1F3D" stroke-width="1.5" marker-end="url(#cm)"/><path d="M245 230 L212 230" stroke="#DB2F30" stroke-width="2" '
                    'marker-end="url(#cm)"/><text x="228" y="204" text-anchor="middle" font-size="10" fill="#DB2F30">fuel</text><path d="M450 230 L417 230" stroke="#DB2F30" stroke-width="2" '
                    'marker-end="url(#cm)"/><text x="433" y="196" text-anchor="middle" font-size="10" fill="#DB2F30">CO₂ and</text><text x="433" y="207" text-anchor="middle" font-size="10" '
                    'fill="#DB2F30">water in</text><text x="330" y="266" text-anchor="middle" font-size="11" fill="#5b6676">Red arrows show how processes depend on each other.</text></svg>',
          'html': '<p>Over the last four weeks, you learned that all living things are made of cells (Week 6), that organelles inside cells do jobs (Week 7), that plant cells make food from light '
                  '(Week 8) and that the membrane controls what crosses (Week 9). These are not four separate topics. They are one connected story.</p><p>Follow a single carbon atom: it enters a '
                  'leaf as carbon dioxide by diffusion, becomes part of glucose in a chloroplast, travels to a mitochondrion where its energy is released, and leaves the cell again as carbon '
                  "dioxide. Every week of this unit is part of that journey.</p><div class='callout'><b>This week:</b> connect the ideas, build a cell model, and take the Unit 2 checkpoint.</div>"},
 'learn': [{'title': 'Connecting the Big Ideas',
            'html': '<p>A <b>concept map</b> shows how ideas connect. Each arrow should be readable as a sentence. For example: "Cell theory says organelles do jobs" is weak. "Cells are the basic '
                    'unit of life, so the jobs that keep an organism alive are carried out by the parts inside its cells" explains the link.</p><p>Look at the red arrows in the map. Photosynthesis '
                    'makes glucose, which mitochondria use as fuel. Diffusion and osmosis bring in the carbon dioxide and water that photosynthesis needs. Remove any one process and the others '
                    'fail.</p>',
            'checks': [{'t': 'open',
                        'key': 'carbon',
                        'q': 'Trace a carbon atom through a plant cell from the air and back to the air. Name at least four steps and the cell part or process involved in each.',
                        'min': 45,
                        'rows': 5,
                        'rubric': ['Enters the leaf as CO₂ through stomata and diffuses into cells',
                                   'Chloroplast uses it in photosynthesis to make glucose',
                                   'Glucose is used by mitochondria to release energy',
                                   'Carbon leaves as CO₂ by diffusion'],
                        'model': 'Carbon dioxide enters the leaf through the stomata and diffuses into a leaf cell. In a chloroplast, photosynthesis uses it to make glucose. The glucose goes to a '
                                 'mitochondrion, which releases its energy, and the carbon is given off as carbon dioxide. That carbon dioxide diffuses out of the cell and back to the air.'},
                       {'t': 'open',
                        'key': 'link',
                        'q': 'Write one linking sentence that connects osmosis (Week 9) to the central vacuole (Week 8).',
                        'min': 12,
                        'rows': 2,
                        'rubric': ['Osmosis moves water into or out of the central vacuole, making the cell firm or wilted'],
                        'model': 'Osmosis moves water into the central vacuole, which swells and keeps the plant cell firm, and out of it, which makes the plant wilt.'},
                       {'t': 'open',
                        'key': 'whatif',
                        'q': 'What would happen to a plant cell if its mitochondria stopped working, even though its chloroplasts were fine? Explain.',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['It could still make glucose but could not release its energy', 'Active transport and other work needing energy would stop, so the cell would die'],
                        'model': 'The chloroplasts could still make glucose, but the cell could not release the energy stored in it. Active transport and other jobs that need energy would stop, so '
                                 'the cell would eventually die.'}]},
           {'title': 'A Bold Idea: Organelles That Were Once Bacteria',
            'visual': '<svg viewBox="0 0 640 215" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Endosymbiosis: a large cell takes in a smaller cell '
                      'that becomes a mitochondrion"><text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Endosymbiosis: one cell living inside '
                      'another</text><ellipse cx="110" cy="105" rx="80" ry="58" fill="#e8f4fb" stroke="#0047BA" stroke-width="2"/><circle cx="95" cy="100" r="18" fill="#e8d7f5" '
                      'stroke="#6b3fa0"/><ellipse cx="215" cy="70" rx="20" ry="10" fill="#f4b183" stroke="#a5552a"/><path d="M232 70 h14" stroke="#0A1F3D" stroke-width="2"/><path d="M200 76 l-18 14" '
                      'stroke="#0A1F3D" stroke-width="2" marker-end="url(#ea)"/><defs><marker id="ea" viewBox="0 0 10 10" markerWidth="5" markerHeight="5" refX="8" refY="5" orient="auto"><path d="M0 '
                      '0 L10 5 L0 10Z" fill="#0A1F3D"/></marker></defs><text x="130" y="186" text-anchor="middle" font-weight="bold">1. A large cell takes in a</text><text x="130" y="200" '
                      'text-anchor="middle" font-weight="bold" font-size="11">smaller bacterium</text><path d="M262 105 h40" stroke="#0A1F3D" stroke-width="2" marker-end="url(#ea)"/><ellipse '
                      'cx="400" cy="105" rx="80" ry="58" fill="#e8f4fb" stroke="#0047BA" stroke-width="2"/><circle cx="385" cy="100" r="18" fill="#e8d7f5" stroke="#6b3fa0"/><ellipse cx="430" '
                      'cy="125" rx="20" ry="10" fill="#f4b183" stroke="#a5552a"/><ellipse cx="430" cy="125" rx="25" ry="14" fill="none" stroke="#0047BA" stroke-dasharray="3 2"/><text x="400" y="186" '
                      'text-anchor="middle" font-weight="bold">2. It is not digested;</text><text x="400" y="200" text-anchor="middle" font-weight="bold" font-size="11">it lives inside and makes '
                      'energy</text><path d="M490 105 h30" stroke="#0A1F3D" stroke-width="2" marker-end="url(#ea)"/><text x="580" y="80" text-anchor="middle" font-weight="bold" fill="#a5552a">3. '
                      'Over time it</text><text x="580" y="96" text-anchor="middle" font-weight="bold" fill="#a5552a">becomes a</text><text x="580" y="112" text-anchor="middle" font-weight="bold" '
                      'fill="#a5552a">mitochondrion</text><text x="580" y="134" text-anchor="middle" font-size="11">(chloroplasts formed</text><text x="580" y="148" text-anchor="middle" '
                      'font-size="11">the same way)</text></svg>',
            'html': '<p>Earlier scientists, such as Konstantin Mereschkowski in 1905, had guessed at this idea, but in 1967 American biologist <b>Lynn Margulis</b> brought it back with evidence. She '
                    'argued that mitochondria and chloroplasts were once free-living bacteria. Long ago, a large cell took in smaller cells but did not digest them. The small cells lived inside, '
                    'making energy or food, and the partnership helped both. Over a very long time, they became organelles. This is called <b>endosymbiosis</b> ("living together inside").</p><p>Many '
                    'scientists rejected her paper at first; it was turned down by many journals before one published it. But evidence piled up:</p><ul><li>Mitochondria and chloroplasts have their '
                    '<b>own DNA</b>, in a loop like the DNA of bacteria.</li><li>They make new copies of themselves by <b>dividing in two</b>, the way bacteria do.</li><li>They are about the <b>same '
                    'size</b> as bacteria and have their own ribosomes, which are like bacterial ribosomes.</li><li>They are wrapped in <b>two membranes</b>, as if one cell had been wrapped inside '
                    "another.</li></ul><p>Today endosymbiosis is accepted by nearly all biologists. Margulis's story shows that science changes when new evidence supports a new explanation, even one "
                    'that seemed strange at first.</p>',
            'checks': [{'t': 'open',
                        'key': 'endoev',
                        'q': 'Choose the two pieces of evidence for endosymbiosis that you find most convincing, and explain why each one supports the idea.',
                        'min': 35,
                        'rows': 4,
                        'rubric': ['Two accurate pieces of evidence (own DNA, divide like bacteria, bacterial size and ribosomes, two membranes)', 'Explains how each points to a bacterial origin'],
                        'model': 'The strongest evidence is that mitochondria have their own loop of DNA, like bacteria, which would make sense if they were once separate living things. Also, they '
                                 'divide in two the way bacteria do, instead of being built by the cell from scratch.'},
                       {'t': 'open',
                        'key': 'margulis',
                        'q': "Margulis's idea was rejected by many scientists before it was accepted. Using her story, explain how scientific knowledge changes.",
                        'min': 30,
                        'rows': 3,
                        'rubric': ['New ideas are tested against evidence; when evidence builds up, explanations change', 'Science is open to revision; peer review can be slow to accept new ideas'],
                        'model': 'Scientific knowledge changes when new evidence supports a better explanation. At first many scientists doubted Margulis, but as studies found DNA, ribosomes and '
                                 'double membranes that matched bacteria, the evidence became strong enough that most scientists changed their minds.'},
                       {'t': 'text',
                        'q': 'Which American biologist argued in 1967, with evidence, that mitochondria and chloroplasts began as bacteria?',
                        'a': ['lynn margulis', 'margulis', 'lynn sagan'],
                        'show': 'Lynn Margulis',
                        'pts': 2,
                        'why': 'Lynn Margulis. Her paper was published under the name Lynn Sagan.'}]},
           {'title': 'Planning Your Cell Model Project',
            'html': '<p>Your Unit 2 project is a <b>three-dimensional model</b> of a plant cell or an animal cell. A model is not just a craft. It must teach someone how a cell works.</p><div '
                    "class='callout'><b>Your model must include:</b><br>1. At least 8 labeled parts (for a plant cell: cell wall, cell membrane, nucleus, cytoplasm, mitochondria, chloroplasts, "
                    'central vacuole, ribosomes; for an animal cell: cell membrane, nucleus, cytoplasm, mitochondria, ribosomes, ER, Golgi apparatus, lysosomes).<br>2. A key that tells what each '
                    'material stands for and the job of each part.<br>3. An analogy card: "A cell is like a ___ because..." with at least five matched parts (different from the city model in Week '
                    '7).<br>4. One process shown with arrows or movable pieces: photosynthesis, active transport or osmosis.<br>5. A limits note: one way your model is not like a real '
                    'cell.</div><p>Use materials you have at home: a shoebox, a plastic bag of hair gel, clay, cardboard, buttons, yarn, pasta or dried beans. Edible models (gelatin, cake) are fine '
                    'if you photograph them before eating.</p><p><b>Safety:</b> never taste non-food materials (hair gel, clay, glue, dried beans used for crafts); keep small pieces and gel away '
                    'from pets and young children; check for food allergies before making an edible model; an adult cuts foam balls or cardboard with a knife.</p>',
            'checks': [{'t': 'open',
                        'key': 'plan',
                        'q': 'Plan your model: which cell type, what material will stand for each of at least five parts, and why you chose each material.',
                        'min': 40,
                        'rows': 5,
                        'rubric': ['Cell type chosen', 'At least five parts matched to materials', 'Reasons tie the material to the structure or job (e.g. stiff cardboard for the wall)'],
                        'model': 'Plant cell in a shoebox. Cell wall: the stiff shoebox, because the wall is rigid. Membrane: plastic wrap lining the box, because it is thin and flexible. Central '
                                 'vacuole: a water-filled zipper bag, because it stores water. Chloroplasts: green lima beans. Nucleus: a purple clay ball with a smaller ball inside for the '
                                 'nucleolus.'},
                       {'t': 'open',
                        'key': 'analogy',
                        'q': 'Draft your analogy: "A cell is like a ___ because..." Match at least five parts to parts of your choice, and explain one match fully.',
                        'min': 40,
                        'rows': 5,
                        'rubric': ['A new analogy (not a city)', 'Five matched parts', 'One match explained by job'],
                        'model': "A plant cell is like a school. The nucleus is the principal's office, the mitochondria are the cafeteria that gives energy, the cell membrane is the front door with "
                                 'a security desk, the cell wall is the fence, and the chloroplasts are the school garden. The cell membrane is like the security desk because it decides who comes in '
                                 'and who leaves.'},
                       {'t': 'open',
                        'key': 'limits',
                        'q': 'Every model has limits. Name one way your planned model will not be like a real cell.',
                        'min': 12,
                        'rows': 2,
                        'rubric': ['A real limit: scale, number of organelles, a real cell is 3D and moving, organelles are not solid, colors are not real'],
                        'model': "A real cell has hundreds of mitochondria and thousands of ribosomes, but my model shows only a few, and a real cell's parts are always moving."}]}],
 'handson': {'title': 'Build Your Cell Model',
             'intro': 'Build the cell model you planned. You will present it to your family like a museum guide. Safety: never taste craft materials, keep small pieces and gel away from pets and '
                      'young children, check food allergies before an edible model, and let an adult do any cutting with a knife.',
             'materials': ['A base: shoebox, paper plate, foam ball cut in half or zipper bag',
                           'Craft or kitchen materials: clay, yarn, buttons, beans, pasta, cardboard, hair gel or gelatin',
                           'Index cards for labels, the key and the analogy card',
                           'Glue, tape and markers',
                           'A phone or camera for a photo'],
             'steps': ['Build the cell base and cell boundary first (wall and membrane, or membrane only).',
                       'Add the organelles. Place the nucleus first, then the others.',
                       'Label every part with a small flag or numbered tag.',
                       'Make the key, the analogy card and the limits note.',
                       'Add arrows or movable pieces to show one process (photosynthesis, active transport or osmosis).',
                       "Photograph your model, then give a 2-minute tour to a family member, explaining each part's job and the process."],
             'record': [{'t': 'open',
                         'key': 'tour',
                         'q': 'Write the script for your 2-minute tour: name each part, its job, and walk through the process you showed.',
                         'min': 79,
                         'rows': 10,
                         'rubric': ['All labeled parts named with correct jobs', 'Process explained step by step with accurate science', 'Uses Unit 2 vocabulary', 'Organized like a tour'],
                         'model': 'Welcome to my plant cell. The shoebox is the cell wall, which supports and protects the cell. Inside it, plastic wrap is the cell membrane, which controls what '
                                  'enters and leaves. The purple clay ball is the nucleus, which holds the DNA and directs the cell. The water bag is the central vacuole, which stores water and '
                                  'keeps the cell firm. The green beans are chloroplasts. Follow the arrows: carbon dioxide diffuses in, the chloroplast uses light to make glucose and oxygen, and '
                                  'the glucose travels to the orange mitochondria, which release its energy...'},
                        {'t': 'open',
                         'key': 'feedback',
                         'q': 'What question did your family member ask during the tour, and how did you answer it? What would you improve if you built the model again?',
                         'min': 30,
                         'rows': 3,
                         'rubric': ['Reports a real question and answer', 'Names a specific improvement'],
                         'model': 'My brother asked why the vacuole is so big. I said it stores water and pushes on the wall to keep the plant standing. Next time I would make the ribosomes smaller '
                                  'and add more of them.'}]},
 'think': {'intro': 'Use evidence and explain your reasoning. Your teacher scores these.',
           'items': [{'t': 'open',
                      'key': 'bigq',
                      'q': "Answer the unit's big question in a paragraph: How do the parts of a cell work together to keep it alive? Use at least six Unit 2 vocabulary words correctly and give at "
                           'least two examples of parts depending on each other.',
                      'min': 89,
                      'rows': 10,
                      'rubric': ['Six or more vocabulary words used correctly',
                                 'Two or more accurate examples of interdependence',
                                 'Clear explanation of how the cell stays alive',
                                 'Organized paragraph'],
                      'model': 'A cell stays alive because its parts work as a team. The cell membrane controls what enters and leaves, letting oxygen and carbon dioxide in and out by diffusion and '
                               'water by osmosis. In a plant cell, chloroplasts use light to make glucose by photosynthesis, and the mitochondria release the energy in that glucose. That energy '
                               'powers active transport, which pumps minerals into the cell. The nucleus holds the DNA, which directs the ribosomes as they build proteins, and the Golgi apparatus '
                               'packages and ships them. If any one part stopped, the others would fail, so the cell depends on all of them working together.'},
                     {'t': 'open',
                      'key': 'cellshow',
                      'q': 'A friend says, "Cells are just tiny blobs. Nothing important happens in them." Write a respectful reply using three facts from Unit 2 to change their mind.',
                      'min': 60,
                      'rows': 5,
                      'rubric': ['Respectful tone', 'Three accurate, specific facts from Unit 2', 'Persuasive reasoning'],
                      'model': "I used to think so too, but cells are amazing. Every living thing is made of them, and all of your body's cells came from other cells. Inside each one, mitochondria "
                               'release energy from food, and in plants, chloroplasts turn sunlight into the sugar that feeds almost every living thing. Even drinking seawater shows how important '
                               'cells are: it pulls water out of them by osmosis. Cells are where life actually happens.'}]},
 'checkpoint': {'title': 'Unit 2 Checkpoint: Cells, the Building Blocks of Life',
                'intro': 'This checkpoint covers Weeks 6 to 9. Mastery is 85 or higher. If you score below 85, your teacher will review with you, then you will retake it.',
                'parts': [{'title': 'Part A: Cell theory and microscopes',
                           'items': [{'t': 'num',
                                      'q': 'A microscope has a 15× eyepiece and a 40× objective lens. What is the total magnification?',
                                      'a': 600,
                                      'unit': '×',
                                      'pts': 3,
                                      'why': '15 × 40 = 600×.'},
                                     {'t': 'open',
                                      'key': 'cp_theory',
                                      'q': 'State the three parts of cell theory.',
                                      'min': 15,
                                      'rows': 2,
                                      'pts': 3,
                                      'rubric': ['All living things are made of cells', 'The cell is the basic unit of life', 'All cells come from existing cells'],
                                      'model': 'All living things are made of cells, the cell is the basic unit of life, and all cells come from existing cells.'},
                                     {'t': 'text',
                                      'q': 'Which scientist, in the 1670s, was the first to see living single-celled organisms through a microscope he made himself?',
                                      'a': ['leeuwenhoek',
                                            'van leeuwenhoek',
                                            'antonie van leeuwenhoek',
                                            'anton van leeuwenhoek',
                                            'leewenhoek',
                                            'leeuwenhook',
                                            'leuwenhoek',
                                            'lewenhoek',
                                            'leeuwenhoeck'],
                                      'show': 'Antonie van Leeuwenhoek',
                                      'pts': 2,
                                      'why': 'Antonie van Leeuwenhoek.'}]},
                          {'title': 'Part B: Organelles',
                           'items': [{'t': 'text',
                                      'q': 'Which organelle builds proteins?',
                                      'a': [{'all': [['ribosome']], 'none': ['not']}],
                                      'show': 'ribosomes',
                                      'pts': 2,
                                      'why': 'Ribosomes build proteins.'},
                                     {'t': 'text',
                                      'q': 'Which organelle packages and ships proteins?',
                                      'a': [{'all': [['golgi']], 'none': ['not']}],
                                      'show': 'Golgi apparatus',
                                      'pts': 2,
                                      'why': 'The Golgi apparatus.'},
                                     {'t': 'text',
                                      'q': "Which organelle holds the cell's DNA and directs its activities?",
                                      'a': [{'all': [['nucleus']], 'none': ['not']}],
                                      'show': 'nucleus',
                                      'pts': 2,
                                      'why': 'The nucleus.'},
                                     {'t': 'open',
                                      'key': 'cp_lacks',
                                      'q': "Explain why Henrietta Lacks's story matters for how scientists treat people today.",
                                      'min': 20,
                                      'rows': 2,
                                      'pts': 3,
                                      'rubric': ['Her cells were taken without consent and used widely', 'Shows the importance of informed consent and respect for patients and families'],
                                      'model': 'Her cells were taken in 1951 without her permission and used in research around the world. Her story shows why scientists must get informed consent '
                                               'and respect patients and their families.'}]},
                          {'title': 'Part C: Plant cells and photosynthesis',
                           'items': [{'t': 'open',
                                      'key': 'cp_three',
                                      'q': 'Name the three parts plant cells have that animal cells lack, with the job of each.',
                                      'min': 15,
                                      'rows': 3,
                                      'pts': 3,
                                      'rubric': ['Cell wall: support and protection', 'Chloroplasts: photosynthesis', 'Central vacuole: stores water, keeps cell firm'],
                                      'model': 'The cell wall supports and protects the cell, chloroplasts carry out photosynthesis, and the central vacuole stores water and keeps the cell firm.'},
                                     {'t': 'text',
                                      'q': 'What is the green pigment in chloroplasts that captures light energy for photosynthesis?',
                                      'a': ['chlorophyll', 'chlorophyl'],
                                      'show': 'chlorophyll',
                                      'pts': 2,
                                      'why': 'Chlorophyll (Week 8).'},
                                     {'t': 'open',
                                      'key': 'cp_mass',
                                      'q': "Where does most of a tree's mass come from? Explain.",
                                      'min': 15,
                                      'rows': 2,
                                      'pts': 3,
                                      'rubric': ['Carbon dioxide from the air (plus water)', 'Photosynthesis builds glucose and then wood from those atoms'],
                                      'model': 'Mostly from carbon dioxide in the air, plus water. Photosynthesis builds those atoms into glucose, which the tree turns into wood.'}]},
                          {'title': 'Part D: Moving in and out of cells',
                           'items': [{'t': 'text',
                                      'q': 'A plant cell is placed in fresh water. Will water move into the cell or out of it?',
                                      'a': [{'all': [['into', 'in', 'enter', 'inward', 'inside']], 'none': ['out', 'not', 'balance', 'equilibrium', 'neither', 'same', 'nothing', 'both']}],
                                      'show': 'into the cell',
                                      'pts': 2,
                                      'why': 'The cell has more dissolved particles than fresh water, so water moves in.'},
                                     {'t': 'text',
                                      'q': 'Which kind of transport moves particles from low to high concentration?',
                                      'a': [{'all': [['active']], 'none': ['passive', 'not']}],
                                      'show': 'active transport',
                                      'pts': 2,
                                      'why': 'Active transport, which uses energy.'},
                                     {'t': 'open',
                                      'key': 'cp_cer',
                                      'q': 'Data: cucumber slices started at 8.0 g. After 1 hour, slices in fresh water had a mass of 8.6 g, and slices in salt water had a mass of 6.9 g. Write a CER '
                                           'conclusion.',
                                      'min': 40,
                                      'rows': 4,
                                      'pts': 4,
                                      'rubric': ['Claim: water moved into cells in fresh water and out in salt water',
                                                 'Evidence: +0.6 g in fresh water, −1.1 g in salt water',
                                                 'Reasoning: osmosis; water moves toward the side with more dissolved particles'],
                                      'model': 'Claim: Water moved into the cucumber cells in fresh water and out of them in salt water. Evidence: The fresh-water slices gained 0.6 g (8.0 to 8.6 g), '
                                               'and the salt-water slices lost 1.1 g (8.0 to 6.9 g). Reasoning: By osmosis, water moves toward the side with more dissolved particles. The cucumber '
                                               'cells had more than fresh water, so water moved in; the salt water had more than the cells, so water moved out.'}]}]},
 'next': 'Unit 3: the diversity of life, starting with the characteristics of living things.'}

TEACHER = {
 "standards": [
  "SC.6.L.14.2: Investigate and explain the components of the scientific theory of cells (cell theory): all organisms are composed of cells (single-celled or multi-cellular), all cells come from pre-existing cells, and cells are the basic unit of life.",
  "SC.6.L.14.3: Recognize and explore how cells of all organisms undergo similar processes to maintain homeostasis, including extracting energy from food, getting rid of waste, and reproducing.",
  "SC.6.L.14.4: Compare and contrast the structure and function of major organelles of plant and animal cells, including cell wall, cell membrane, nucleus, cytoplasm, chloroplasts, mitochondria, and vacuoles.",
  "SC.6.N.2.2: Explain that scientific knowledge is durable because it is open to change as new evidence or interpretations are encountered.",
  "SC.6.N.3.4: Identify the role of models in the context of the sixth grade science benchmarks."],
 "materials": ["The interactive lesson", "Cell model materials (shoebox or plate, clay, beans, yarn, buttons, gel or gelatin), index cards, glue, tape, markers", "A phone or camera", "Paper and pencil for the checkpoint"],
 "flow": [
  [6, "Reconnect", "Run the Reconnect questions across the unit."],
  [6, "Hook", "Walk through the concept map and trace the carbon atom aloud."],
  [10, "Connections", "The student writes linking sentences for two arrows."],
  [12, "Endosymbiosis", "Tell Lynn Margulis's story. Weigh the four pieces of evidence."],
  [12, "Project plan", "Review the project requirements, safety notes and rubric. Approve the materials list and analogy."],
  [4, "Assign", "Assign building the model and the tour."],
  [10, "Checkpoint preview", "Explain that the checkpoint is completed after class, independently, one try per item, with no answers shown until you review it. Mastery is 85; below 85 means a review lesson and a retake."]],
 "key_questions": ["How does this part depend on another part?", "What evidence would convince you that an organelle was once a bacterium?", "What does your model show well, and what can it not show?"],
 "misconceptions": ["Unit topics are separate rather than connected.", "Endosymbiosis means organelles are still bacteria today.", "A model is a craft rather than an explanation.", "Plants do not have mitochondria."],
 "support": ["Provide a partly completed concept map.", "Give a model planning sheet with spaces for each part and material.", "Offer analogy starters: a school, a farm, a kitchen, a sports team."],
 "challenge": ["Research the other evidence for endosymbiosis, such as bacteria found living inside other cells today.", "Make a second model at a consistent scale: if a cell were the size of your room, how big would a mitochondrion be?"],
 "background": "<p>The checkpoint covers Weeks 6 to 9. Lynn Margulis (1938 to 2011) published \"On the origin of mitosing cells\" in the Journal of Theoretical Biology in 1967 under the name Lynn Sagan, after rejections by about fifteen journals; endosymbiotic origin of mitochondria and chloroplasts is now the consensus view, supported by circular organelle DNA, binary fission, 70S-like ribosomes and double membranes. The Cell Model Project rubric is on the Unit 2 Projects page.</p>",
 "sources": ["Sagan, L. (1967), On the origin of mitosing cells, Journal of Theoretical Biology 14.", "University of California Museum of Paleontology, Understanding Evolution: Endosymbiosis.", "CPALMS, SC.6.L.14 benchmarks."]
}

PRINT = {
 "directions": "Use complete sentences.",
 "items": [
  {"q":"State the three parts of cell theory.","a":"All living things are made of cells; the cell is the basic unit of life; all cells come from existing cells.","lines":2},
  {"q":"Match: nucleus, mitochondria, chloroplast, cell membrane, ribosome.","a":"DNA and control; release energy; photosynthesis; controls what enters and leaves; builds proteins.","lines":2},
  {"q":"Write the word equation for photosynthesis.","a":"carbon dioxide + water + light energy → glucose + oxygen","lines":1},
  {"q":"What happens to a plant cell in very salty water, and why?","a":"Water moves out by osmosis, so the vacuole shrinks and the cell wilts.","lines":2},
  {"q":"Give two pieces of evidence that mitochondria were once bacteria.","a":"Their own loop of DNA; they divide like bacteria (also bacterial-size ribosomes, two membranes).","lines":2},
  {"q":"Name one limit of a cell model.","a":"Not to scale; too few organelles; parts do not move as in a real cell.","lines":2}]
}
