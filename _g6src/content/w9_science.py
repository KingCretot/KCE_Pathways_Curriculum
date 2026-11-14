def diffusion():
    import random
    random.seed(7)
    s = ('<svg viewBox="0 0 640 210" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Diffusion of dye particles over time">'
         '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Diffusion: particles spread from high concentration to low</text>')
    for i, (lab, spread) in enumerate([("Start", 0.12), ("A few minutes later", 0.45), ("Later: evenly spread", 1.0)]):
        x0 = 20 + i * 210
        s += f'<rect x="{x0}" y="36" width="190" height="140" rx="6" fill="#e8f4fb" stroke="#0047BA" stroke-width="2"/>'
        for _ in range(40):
            cx = x0 + 95 + (random.random() - .5) * 180 * spread; cy = 106 + (random.random() - .5) * 130 * spread
            s += f'<circle cx="{round(cx,1)}" cy="{round(cy,1)}" r="3.5" fill="#DB2F30"/>'
        s += f'<text x="{x0+95}" y="196" text-anchor="middle" font-weight="bold">{lab}</text>'
        if i < 2:
            s += f'<path d="M{x0+193} 106 h12" stroke="#0A1F3D" stroke-width="2"/><path d="M{x0+205} 101 l6 5 l-6 5" fill="#0A1F3D"/>'
    return s + '</svg>'

OSMO = ('<svg viewBox="0 0 660 250" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Plant cells in three kinds of water">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Osmosis: which way does water move?</text>'
  + ''.join(
    f'<rect x="{x}" y="36" width="200" height="150" rx="8" fill="{bg}"/>'
    f'<rect x="{x+45}" y="66" width="110" height="90" rx="6" fill="#cfe8b0" stroke="#3d6b1f" stroke-width="5"/>'
    f'<rect x="{x+100-vw/2}" y="{111-vh/2}" width="{vw}" height="{vh}" rx="8" fill="#bfe3f5" stroke="#0047BA" stroke-width="1.5"/>'
    + ''.join(f'<path d="M{ax} {ay} l{dx} {dy}" stroke="#0047BA" stroke-width="2.5" marker-end="url(#oa)"/>' for ax, ay, dx, dy in arr) +
    f'<text x="{x+100}" y="206" text-anchor="middle" font-weight="bold">{t1}</text><text x="{x+100}" y="222" text-anchor="middle" font-size="11">{t2}</text>'
    for x, bg, vw, vh, arr, t1, t2 in [
      (14, "#eaf6ff", 92, 72, [(30, 111, 18, 0), (190, 111, -18, 0)], "Fresh water", "water moves IN: cell is firm"),
      (230, "#f2f2f2", 70, 52, [(246, 100, 18, 0), (304, 122, -18, 0), (412, 100, -18, 0), (354, 122, 18, 0)], "Balanced", "water in = water out"),
      (446, "#fdecec", 36, 26, [(520, 111, -22, 0), (580, 111, 22, 0)], "Very salty water", "water moves OUT: cell wilts")]) +
  '<defs><marker id="oa" viewBox="0 0 10 10" markerWidth="5" markerHeight="5" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="#0047BA"/></marker></defs>'
  '<text x="330" y="244" text-anchor="middle" font-size="11" fill="#5b6676">The blue sac is the central vacuole. The cell wall keeps the cell from bursting in fresh water.</text></svg>')

MEMBRANE = ('<svg viewBox="0 0 640 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Three ways materials cross a cell membrane">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Crossing the membrane: three ways</text>'
  '<rect x="10" y="96" width="620" height="34" fill="#f7e3a8"/><text x="18" y="88" font-size="11" fill="#5b6676">OUTSIDE the cell</text><text x="18" y="150" font-size="11" fill="#5b6676">INSIDE the cell</text>'
  + ''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="#C9A84C"/>' for x in range(16, 630, 14) for y in (101, 125)) +
  '<circle cx="110" cy="60" r="5" fill="#DB2F30"/><circle cx="125" cy="72" r="5" fill="#DB2F30"/><circle cx="96" cy="74" r="5" fill="#DB2F30"/><circle cx="118" cy="160" r="5" fill="#DB2F30"/>'
  '<path d="M112 80 v70" stroke="#0A1F3D" stroke-width="2" stroke-dasharray="4 3"/><path d="M107 145 l5 8 l5 -8" fill="#0A1F3D"/>'
  '<text x="112" y="186" text-anchor="middle" font-weight="bold">Diffusion</text><text x="112" y="202" text-anchor="middle" font-size="11">small particles like oxygen</text><text x="112" y="216" text-anchor="middle" font-size="11">slip through; no energy</text>'
  '<rect x="300" y="92" width="16" height="42" fill="#0047BA"/><rect x="324" y="92" width="16" height="42" fill="#0047BA"/>'
  '<circle cx="320" cy="62" r="5" fill="#2a8fd6"/><circle cx="334" cy="70" r="5" fill="#2a8fd6"/><circle cx="310" cy="74" r="5" fill="#2a8fd6"/><circle cx="320" cy="160" r="5" fill="#2a8fd6"/><path d="M320 80 v70" stroke="#0A1F3D" stroke-width="2" stroke-dasharray="4 3"/><path d="M315 145 l5 8 l5 -8" fill="#0A1F3D"/>'
  '<text x="320" y="186" text-anchor="middle" font-weight="bold">Osmosis</text><text x="320" y="202" text-anchor="middle" font-size="11">water through channel</text><text x="320" y="216" text-anchor="middle" font-size="11">proteins; no energy</text>'
  '<path d="M510 92 h36 v42 h-36z" fill="#6b3fa0"/><text x="528" y="118" text-anchor="middle" fill="#fff" font-size="10">pump</text>'
  '<circle cx="528" cy="160" r="5" fill="#3d9a2f"/><circle cx="528" cy="60" r="5" fill="#3d9a2f"/><circle cx="514" cy="70" r="5" fill="#3d9a2f"/><circle cx="542" cy="68" r="5" fill="#3d9a2f"/><circle cx="528" cy="78" r="5" fill="#3d9a2f"/>'
  '<path d="M490 152 v-84" stroke="#6b3fa0" stroke-width="2"/><path d="M485 74 l5 -8 l5 8" fill="#6b3fa0"/><text x="482" y="74" text-anchor="end" font-size="10" fill="#6b3fa0">uses</text><text x="482" y="86" text-anchor="end" font-size="10" fill="#6b3fa0">energy</text>'
  '<text x="528" y="196" text-anchor="middle" font-weight="bold">Active transport</text><text x="528" y="212" text-anchor="middle" font-size="11">pumps move particles from</text><text x="528" y="226" text-anchor="middle" font-size="11">low to high; needs energy</text></svg>')

LESSON = {'unit': 'Unit 2: Cells, the Building Blocks of Life',
 'title': 'How Things Move In and Out of Cells',
 'subtitle': 'Every cell must take in water, oxygen and food and get rid of wastes. The cell membrane decides what crosses, using diffusion, osmosis and active transport.',
 'objectives': ['Explain diffusion as the movement of particles from higher to lower concentration.',
                'Explain osmosis as the diffusion of water across a membrane, and predict which way water will move.',
                'Distinguish passive transport from active transport.',
                'Run a controlled osmosis investigation with potato strips and explain the results.',
                'Apply osmosis to real situations such as wilting plants and drinking seawater.'],
 'vocab': [['concentration', 'How much of a substance is packed into a certain space or amount of liquid.'],
           ['diffusion', 'The movement of particles from an area of higher concentration to an area of lower concentration.'],
           ['osmosis', 'The diffusion of water across a membrane that lets water through but blocks some other particles.'],
           ['selectively permeable', 'Letting some substances pass through but not others; the cell membrane is selectively permeable.'],
           ['passive transport', 'Movement across a membrane that needs no energy from the cell (diffusion and osmosis).'],
           ['active transport', "Movement across a membrane that uses the cell's energy, often to move particles from lower to higher concentration."],
           ['aquaporin', 'A protein channel in the membrane that lets water pass through quickly.']],
 'reconnect': {'title': 'Week 8: Plant cells and photosynthesis',
               'intro': 'Last week you saw a basil plant wilt and recover. Today you learn why. Review first.',
               'items': [{'t': 'text',
                          'q': 'Which large plant organelle stores water and keeps the cell firm?',
                          'a': [{'all': [['vacuole']], 'none': ['not']}],
                          'show': 'central vacuole',
                          'pts': 2,
                          'why': 'The central vacuole. Today you will see how water moves into and out of it.'},
                         {'t': 'text',
                          'q': 'Through what tiny openings does carbon dioxide enter a leaf?',
                          'a': ['stomata', 'stoma', 'stomates'],
                          'show': 'stomata',
                          'pts': 2,
                          'why': "Stomata. Carbon dioxide reaches the leaf cells by diffusion, one of today's processes."},
                         {'t': 'open',
                          'key': 'rc_wilt',
                          'q': 'In your own words, explain why a drooping basil plant stood up again after it was watered.',
                          'min': 15,
                          'rows': 2,
                          'rubric': ['Water refilled the central vacuoles, which pushed against the cell walls and made the cells firm'],
                          'model': 'The water filled the central vacuoles again, and they pushed against the stiff cell walls, so the cells became firm and the plant stood up.'},
                         {'t': 'open',
                          'key': 'rc_disks',
                          'q': 'In the leaf-disk investigation, why did the disks float, and what was the independent variable?',
                          'min': 15,
                          'rows': 2,
                          'rubric': ['Oxygen from photosynthesis collected in the disks', 'Independent variable: baking soda (carbon dioxide) or light'],
                          'model': 'Photosynthesis made oxygen, which filled the disks and made them float. The independent variable was the baking soda, which supplied carbon dioxide.'}]},
 'hook': {'title': 'Water, Water Everywhere, Nor Any Drop to Drink',
          'html': '<p>In <i>The Rime of the Ancient Mariner</i> (first published in 1798, revised in 1817), the poet Samuel Taylor Coleridge described sailors stranded on a calm sea: <i>"Water, '
                  'water, every where, / Nor any drop to drink."</i> Sailors knew that drinking seawater makes thirst worse and can kill. But why? It is water, after all.</p><p>The answer happens in '
                  'your cells. Seawater is nearly four times as salty as your blood. When you drink it, water is pulled <b>out</b> of your cells, and your kidneys must use even more water to get rid '
                  'of the extra salt. You end up drier than before.</p><p>The same process explains why a salad goes limp under salty dressing, why limp celery firms up in a glass of water, and why '
                  "salt water seeping into Florida's coastal wells and soil can kill trees and gardens.</p><div class='callout'><b>Big question:</b> How does a cell decide what goes in and what "
                  'comes out?</div>'},
 'learn': [{'title': 'Diffusion: From Crowded to Spread Out',
            'visual': '<svg viewBox="0 0 640 210" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Diffusion of dye particles over time"><text x="320" '
                      'y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Diffusion: particles spread from high concentration to low</text><rect x="20" y="36" width="190" '
                      'height="140" rx="6" fill="#e8f4fb" stroke="#0047BA" stroke-width="2"/><circle cx="111.2" cy="100.6" r="3.5" fill="#DB2F30"/><circle cx="118.3" cy="99.3" r="3.5" '
                      'fill="#DB2F30"/><circle cx="115.8" cy="103.9" r="3.5" fill="#DB2F30"/><circle cx="105.5" cy="106.1" r="3.5" fill="#DB2F30"/><circle cx="105.0" cy="105.0" r="3.5" '
                      'fill="#DB2F30"/><circle cx="105.7" cy="99.6" r="3.5" fill="#DB2F30"/><circle cx="113.4" cy="111.1" r="3.5" fill="#DB2F30"/><circle cx="106.9" cy="101.7" r="3.5" '
                      'fill="#DB2F30"/><circle cx="117.8" cy="113.0" r="3.5" fill="#DB2F30"/><circle cx="116.7" cy="104.4" r="3.5" fill="#DB2F30"/><circle cx="125.3" cy="98.9" r="3.5" '
                      'fill="#DB2F30"/><circle cx="122.7" cy="102.7" r="3.5" fill="#DB2F30"/><circle cx="107.3" cy="100.0" r="3.5" fill="#DB2F30"/><circle cx="110.9" cy="110.9" r="3.5" '
                      'fill="#DB2F30"/><circle cx="108.1" cy="107.3" r="3.5" fill="#DB2F30"/><circle cx="118.0" cy="104.0" r="3.5" fill="#DB2F30"/><circle cx="116.0" cy="99.2" r="3.5" '
                      'fill="#DB2F30"/><circle cx="105.5" cy="101.4" r="3.5" fill="#DB2F30"/><circle cx="118.9" cy="104.9" r="3.5" fill="#DB2F30"/><circle cx="111.0" cy="107.3" r="3.5" '
                      'fill="#DB2F30"/><circle cx="114.0" cy="102.9" r="3.5" fill="#DB2F30"/><circle cx="121.4" cy="109.1" r="3.5" fill="#DB2F30"/><circle cx="109.5" cy="107.2" r="3.5" '
                      'fill="#DB2F30"/><circle cx="115.5" cy="111.9" r="3.5" fill="#DB2F30"/><circle cx="120.0" cy="102.7" r="3.5" fill="#DB2F30"/><circle cx="125.4" cy="100.0" r="3.5" '
                      'fill="#DB2F30"/><circle cx="113.2" cy="110.0" r="3.5" fill="#DB2F30"/><circle cx="107.5" cy="105.8" r="3.5" fill="#DB2F30"/><circle cx="105.0" cy="108.6" r="3.5" '
                      'fill="#DB2F30"/><circle cx="120.7" cy="107.1" r="3.5" fill="#DB2F30"/><circle cx="123.1" cy="103.1" r="3.5" fill="#DB2F30"/><circle cx="119.2" cy="107.5" r="3.5" '
                      'fill="#DB2F30"/><circle cx="116.7" cy="105.3" r="3.5" fill="#DB2F30"/><circle cx="122.3" cy="112.9" r="3.5" fill="#DB2F30"/><circle cx="114.4" cy="108.6" r="3.5" '
                      'fill="#DB2F30"/><circle cx="105.5" cy="109.1" r="3.5" fill="#DB2F30"/><circle cx="118.2" cy="113.7" r="3.5" fill="#DB2F30"/><circle cx="122.0" cy="102.6" r="3.5" '
                      'fill="#DB2F30"/><circle cx="112.5" cy="108.6" r="3.5" fill="#DB2F30"/><circle cx="104.7" cy="105.4" r="3.5" fill="#DB2F30"/><text x="115" y="196" text-anchor="middle" '
                      'font-weight="bold">Start</text><path d="M213 106 h12" stroke="#0A1F3D" stroke-width="2"/><path d="M225 101 l6 5 l-6 5" fill="#0A1F3D"/><rect x="230" y="36" width="190" '
                      'height="140" rx="6" fill="#e8f4fb" stroke="#0047BA" stroke-width="2"/><circle cx="298.1" cy="83.6" r="3.5" fill="#DB2F30"/><circle cx="289.3" cy="121.7" r="3.5" '
                      'fill="#DB2F30"/><circle cx="295.0" cy="91.2" r="3.5" fill="#DB2F30"/><circle cx="316.2" cy="127.7" r="3.5" fill="#DB2F30"/><circle cx="291.0" cy="103.0" r="3.5" '
                      'fill="#DB2F30"/><circle cx="329.0" cy="128.4" r="3.5" fill="#DB2F30"/><circle cx="350.9" cy="127.3" r="3.5" fill="#DB2F30"/><circle cx="307.1" cy="101.0" r="3.5" '
                      'fill="#DB2F30"/><circle cx="313.6" cy="128.5" r="3.5" fill="#DB2F30"/><circle cx="362.1" cy="85.6" r="3.5" fill="#DB2F30"/><circle cx="298.8" cy="90.3" r="3.5" '
                      'fill="#DB2F30"/><circle cx="303.4" cy="105.1" r="3.5" fill="#DB2F30"/><circle cx="332.2" cy="92.1" r="3.5" fill="#DB2F30"/><circle cx="284.8" cy="101.3" r="3.5" '
                      'fill="#DB2F30"/><circle cx="314.4" cy="109.9" r="3.5" fill="#DB2F30"/><circle cx="361.7" cy="117.1" r="3.5" fill="#DB2F30"/><circle cx="326.3" cy="112.9" r="3.5" '
                      'fill="#DB2F30"/><circle cx="339.3" cy="79.9" r="3.5" fill="#DB2F30"/><circle cx="357.4" cy="122.4" r="3.5" fill="#DB2F30"/><circle cx="355.3" cy="123.4" r="3.5" '
                      'fill="#DB2F30"/><circle cx="316.3" cy="100.1" r="3.5" fill="#DB2F30"/><circle cx="292.9" cy="113.9" r="3.5" fill="#DB2F30"/><circle cx="289.5" cy="80.7" r="3.5" '
                      'fill="#DB2F30"/><circle cx="301.4" cy="86.2" r="3.5" fill="#DB2F30"/><circle cx="312.0" cy="79.8" r="3.5" fill="#DB2F30"/><circle cx="284.5" cy="85.6" r="3.5" '
                      'fill="#DB2F30"/><circle cx="292.7" cy="98.0" r="3.5" fill="#DB2F30"/><circle cx="286.6" cy="127.9" r="3.5" fill="#DB2F30"/><circle cx="334.2" cy="85.4" r="3.5" '
                      'fill="#DB2F30"/><circle cx="304.9" cy="97.1" r="3.5" fill="#DB2F30"/><circle cx="314.0" cy="83.9" r="3.5" fill="#DB2F30"/><circle cx="353.3" cy="134.8" r="3.5" '
                      'fill="#DB2F30"/><circle cx="322.2" cy="105.1" r="3.5" fill="#DB2F30"/><circle cx="291.5" cy="82.7" r="3.5" fill="#DB2F30"/><circle cx="312.3" cy="92.2" r="3.5" '
                      'fill="#DB2F30"/><circle cx="351.6" cy="86.2" r="3.5" fill="#DB2F30"/><circle cx="286.4" cy="132.4" r="3.5" fill="#DB2F30"/><circle cx="327.3" cy="85.3" r="3.5" '
                      'fill="#DB2F30"/><circle cx="328.5" cy="78.3" r="3.5" fill="#DB2F30"/><circle cx="327.3" cy="134.0" r="3.5" fill="#DB2F30"/><text x="325" y="196" text-anchor="middle" '
                      'font-weight="bold">A few minutes later</text><path d="M423 106 h12" stroke="#0A1F3D" stroke-width="2"/><path d="M435 101 l6 5 l-6 5" fill="#0A1F3D"/><rect x="440" y="36" '
                      'width="190" height="140" rx="6" fill="#e8f4fb" stroke="#0047BA" stroke-width="2"/><circle cx="600.4" cy="131.5" r="3.5" fill="#DB2F30"/><circle cx="492.0" cy="88.7" r="3.5" '
                      'fill="#DB2F30"/><circle cx="475.1" cy="141.4" r="3.5" fill="#DB2F30"/><circle cx="540.9" cy="142.3" r="3.5" fill="#DB2F30"/><circle cx="504.3" cy="70.0" r="3.5" '
                      'fill="#DB2F30"/><circle cx="591.1" cy="169.0" r="3.5" fill="#DB2F30"/><circle cx="598.5" cy="145.8" r="3.5" fill="#DB2F30"/><circle cx="592.3" cy="137.2" r="3.5" '
                      'fill="#DB2F30"/><circle cx="485.8" cy="108.3" r="3.5" fill="#DB2F30"/><circle cx="509.0" cy="44.8" r="3.5" fill="#DB2F30"/><circle cx="450.0" cy="77.3" r="3.5" '
                      'fill="#DB2F30"/><circle cx="491.7" cy="131.0" r="3.5" fill="#DB2F30"/><circle cx="617.2" cy="99.1" r="3.5" fill="#DB2F30"/><circle cx="613.7" cy="169.4" r="3.5" '
                      'fill="#DB2F30"/><circle cx="616.9" cy="88.4" r="3.5" fill="#DB2F30"/><circle cx="484.7" cy="70.5" r="3.5" fill="#DB2F30"/><circle cx="480.4" cy="67.6" r="3.5" '
                      'fill="#DB2F30"/><circle cx="557.3" cy="158.0" r="3.5" fill="#DB2F30"/><circle cx="596.3" cy="103.3" r="3.5" fill="#DB2F30"/><circle cx="562.5" cy="145.0" r="3.5" '
                      'fill="#DB2F30"/><circle cx="460.3" cy="126.9" r="3.5" fill="#DB2F30"/><circle cx="608.8" cy="142.7" r="3.5" fill="#DB2F30"/><circle cx="580.0" cy="103.1" r="3.5" '
                      'fill="#DB2F30"/><circle cx="477.1" cy="143.6" r="3.5" fill="#DB2F30"/><circle cx="504.9" cy="145.1" r="3.5" fill="#DB2F30"/><circle cx="619.9" cy="92.5" r="3.5" '
                      'fill="#DB2F30"/><circle cx="517.2" cy="164.1" r="3.5" fill="#DB2F30"/><circle cx="575.5" cy="63.1" r="3.5" fill="#DB2F30"/><circle cx="467.9" cy="60.6" r="3.5" '
                      'fill="#DB2F30"/><circle cx="607.9" cy="145.8" r="3.5" fill="#DB2F30"/><circle cx="471.3" cy="148.4" r="3.5" fill="#DB2F30"/><circle cx="621.5" cy="126.4" r="3.5" '
                      'fill="#DB2F30"/><circle cx="508.1" cy="112.3" r="3.5" fill="#DB2F30"/><circle cx="468.6" cy="42.9" r="3.5" fill="#DB2F30"/><circle cx="619.8" cy="125.5" r="3.5" '
                      'fill="#DB2F30"/><circle cx="539.8" cy="162.4" r="3.5" fill="#DB2F30"/><circle cx="523.1" cy="154.3" r="3.5" fill="#DB2F30"/><circle cx="593.7" cy="68.4" r="3.5" '
                      'fill="#DB2F30"/><circle cx="490.3" cy="79.1" r="3.5" fill="#DB2F30"/><circle cx="488.3" cy="117.2" r="3.5" fill="#DB2F30"/><text x="535" y="196" text-anchor="middle" '
                      'font-weight="bold">Later: evenly spread</text></svg>',
            'html': '<p>Particles of liquids and gases are always moving and bumping into each other. Over time, they spread out from where they are crowded (high <b>concentration</b>) to where they '
                    'are less crowded (low concentration). This is <b>diffusion</b>. Spray perfume in one corner of a room, and soon you can smell it everywhere. Drop food coloring in water, and it '
                    'slowly spreads until the color is even.</p><p>Diffusion needs no push and no energy. It is faster when the particles are warmer, because warm particles move faster. It continues '
                    'until the particles are evenly spread. Particles still move after that, but just as many move one way as the other.</p><p>Your cells depend on diffusion. Oxygen is more '
                    "concentrated in your blood than in your cells, so it diffuses into them. Carbon dioxide is more concentrated in your cells, so it diffuses out. Last week's leaves worked the "
                    'same way: carbon dioxide diffused in through the stomata.</p>',
            'checks': [{'t': 'open',
                        'key': 'perfume',
                        'q': 'Someone opens a jar of garlic in the kitchen. A few minutes later, you smell it in the living room. Explain this using the words particles, concentration and diffusion.',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Garlic particles move from high concentration (near the jar) to low concentration (living room)', 'This spreading is diffusion'],
                        'model': 'Garlic particles were crowded near the jar, where the concentration was high. They moved and spread out toward the living room, where the concentration was low, '
                                 'until I could smell them. That is diffusion.'},
                       {'t': 'open',
                        'key': 'temp',
                        'q': 'Predict: will food coloring spread faster in hot water or cold water? Explain why.',
                        'min': 15,
                        'rows': 2,
                        'rubric': ['Hot water', 'Particles move faster at higher temperature, so diffusion is faster'],
                        'model': 'Hot water, because particles move faster when they are warmer, so the coloring spreads more quickly.'},
                       {'t': 'text',
                        'q': 'Oxygen is more concentrated in your blood than inside your muscle cells. Will oxygen diffuse into the cells or out of them?',
                        'a': [{'all': [['into', 'in to', 'inside', 'enter', 'in']], 'none': ['out', 'not', 'stay', 'in the blood', 'in blood', 'into the blood', 'into blood']}],
                        'show': 'into the cells',
                        'pts': 2,
                        'why': 'Particles diffuse from high to low concentration: from the blood into the cells.'}]},
           {'title': 'Osmosis: When Water Moves',
            'visual': '<svg viewBox="0 0 660 250" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Plant cells in three kinds of water"><text x="330" '
                      'y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Osmosis: which way does water move?</text><rect x="14" y="36" width="200" height="150" rx="8" '
                      'fill="#eaf6ff"/><rect x="59" y="66" width="110" height="90" rx="6" fill="#cfe8b0" stroke="#3d6b1f" stroke-width="5"/><rect x="68.0" y="75.0" width="92" height="72" rx="8" '
                      'fill="#bfe3f5" stroke="#0047BA" stroke-width="1.5"/><path d="M30 111 l18 0" stroke="#0047BA" stroke-width="2.5" marker-end="url(#oa)"/><path d="M190 111 l-18 0" '
                      'stroke="#0047BA" stroke-width="2.5" marker-end="url(#oa)"/><text x="114" y="206" text-anchor="middle" font-weight="bold">Fresh water</text><text x="114" y="222" '
                      'text-anchor="middle" font-size="11">water moves IN: cell is firm</text><rect x="230" y="36" width="200" height="150" rx="8" fill="#f2f2f2"/><rect x="275" y="66" width="110" '
                      'height="90" rx="6" fill="#cfe8b0" stroke="#3d6b1f" stroke-width="5"/><rect x="295.0" y="85.0" width="70" height="52" rx="8" fill="#bfe3f5" stroke="#0047BA" '
                      'stroke-width="1.5"/><path d="M246 100 l18 0" stroke="#0047BA" stroke-width="2.5" marker-end="url(#oa)"/><path d="M304 122 l-18 0" stroke="#0047BA" stroke-width="2.5" '
                      'marker-end="url(#oa)"/><path d="M412 100 l-18 0" stroke="#0047BA" stroke-width="2.5" marker-end="url(#oa)"/><path d="M354 122 l18 0" stroke="#0047BA" stroke-width="2.5" '
                      'marker-end="url(#oa)"/><text x="330" y="206" text-anchor="middle" font-weight="bold">Balanced</text><text x="330" y="222" text-anchor="middle" font-size="11">water in = water '
                      'out</text><rect x="446" y="36" width="200" height="150" rx="8" fill="#fdecec"/><rect x="491" y="66" width="110" height="90" rx="6" fill="#cfe8b0" stroke="#3d6b1f" '
                      'stroke-width="5"/><rect x="528.0" y="98.0" width="36" height="26" rx="8" fill="#bfe3f5" stroke="#0047BA" stroke-width="1.5"/><path d="M520 111 l-22 0" stroke="#0047BA" '
                      'stroke-width="2.5" marker-end="url(#oa)"/><path d="M580 111 l22 0" stroke="#0047BA" stroke-width="2.5" marker-end="url(#oa)"/><text x="546" y="206" text-anchor="middle" '
                      'font-weight="bold">Very salty water</text><text x="546" y="222" text-anchor="middle" font-size="11">water moves OUT: cell wilts</text><defs><marker id="oa" viewBox="0 0 10 10" '
                      'markerWidth="5" markerHeight="5" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="#0047BA"/></marker></defs><text x="330" y="238" text-anchor="middle" '
                      'font-size="11" fill="#5b6676">The blue sac is the central vacuole. The cell wall keeps the cell from bursting in fresh water.</text></svg>',
            'html': '<p>The cell membrane is <b>selectively permeable</b>: it lets some things through, like water and oxygen, and blocks others, like salt and sugar unless the cell lets them in. '
                    '<b>Osmosis</b> is the diffusion of water across such a membrane.</p><p>Here is the rule: <b>water moves toward the side with more dissolved particles</b> (salt or sugar), '
                    'because that side has a lower concentration of water. So:</p><ul><li>In <b>fresh water</b>, water moves into a plant cell. The central vacuole swells and presses on the cell '
                    'wall, so the cell is firm. That is why celery stiffens in a glass of water.</li><li>In <b>very salty water</b>, water moves out. The vacuole shrinks, the membrane pulls away '
                    'from the wall and the plant wilts.</li><li>When the water inside and outside is balanced, water moves in and out at the same rate.</li></ul><p>Animal cells have no cell wall, so '
                    'in pure water they can swell until they burst, and in salty water they shrivel. That is why medical IV bags contain water with just the right amount of salt, matched to your '
                    'blood.</p><p>How does water get through the oily membrane so fast? In 1992, American scientist <b>Peter Agre</b> and his team discovered <b>aquaporins</b>, protein channels that '
                    'let water flow through, and won the 2003 Nobel Prize in Chemistry.</p>',
            'checks': [{'t': 'text',
                        'q': 'A plant cell is placed in very salty water. Will water move into the cell or out of it?',
                        'a': [{'all': [['out']], 'none': ['into', 'not out', 'outside in', 'outside to inside', 'goes in', 'moves in', 'comes in', 'flows in', 'enter']}],
                        'show': 'out of the cell',
                        'pts': 2,
                        'why': 'There are more dissolved particles outside, so water moves out toward the salty side, and the cell shrinks.'},
                       {'t': 'open',
                        'key': 'celery',
                        'q': 'Limp celery is put in a glass of fresh water overnight and becomes crisp. Explain what happened, using osmosis, vacuole and cell wall.',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Fresh water has fewer dissolved particles than the cells, so water moved into the cells by osmosis',
                                   'The vacuoles filled and pressed against the cell walls, making the cells firm'],
                        'model': 'The cells had more dissolved particles than the fresh water, so water moved into them by osmosis. The central vacuoles filled up and pushed against the cell walls, '
                                 'which made the cells firm and the celery crisp.'},
                       {'t': 'open',
                        'key': 'seawater',
                        'q': 'Return to the sailors. Explain why drinking seawater makes a person more dehydrated, not less.',
                        'min': 30,
                        'rows': 3,
                        'rubric': ['Seawater is saltier than body fluids, so water moves out of cells by osmosis',
                                   'The kidneys need extra water to remove the salt, so the body loses more water than it gained'],
                        'model': 'Seawater is nearly four times as salty as blood, so the salty fluid around the cells pulls water out of them by osmosis. The kidneys also need extra water to get '
                                 'rid of all that salt, so the person loses more water than they drank.'},
                       {'t': 'open',
                        'key': 'iv',
                        'q': "Why would it be dangerous to put pure water directly into a person's bloodstream instead of an IV solution with the right amount of salt?",
                        'min': 20,
                        'rows': 2,
                        'rubric': ['Pure water has fewer dissolved particles, so water would rush into blood cells', 'Animal cells have no wall, so they could swell and burst'],
                        'model': 'Pure water has fewer dissolved particles than the blood cells, so water would rush into them by osmosis. Blood cells have no cell wall, so they could swell and '
                                 'burst.'}]},
           {'title': 'Active Transport: Pumping Uphill',
            'visual': '<svg viewBox="0 0 640 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Three ways materials cross a cell membrane"><text '
                      'x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Crossing the membrane: three ways</text><rect x="10" y="96" width="620" height="34" '
                      'fill="#f7e3a8"/><text x="18" y="88" font-size="11" fill="#5b6676">OUTSIDE the cell</text><text x="18" y="150" font-size="11" fill="#5b6676">INSIDE the cell</text><circle '
                      'cx="16" cy="101" r="5" fill="#C9A84C"/><circle cx="16" cy="125" r="5" fill="#C9A84C"/><circle cx="30" cy="101" r="5" fill="#C9A84C"/><circle cx="30" cy="125" r="5" '
                      'fill="#C9A84C"/><circle cx="44" cy="101" r="5" fill="#C9A84C"/><circle cx="44" cy="125" r="5" fill="#C9A84C"/><circle cx="58" cy="101" r="5" fill="#C9A84C"/><circle cx="58" '
                      'cy="125" r="5" fill="#C9A84C"/><circle cx="72" cy="101" r="5" fill="#C9A84C"/><circle cx="72" cy="125" r="5" fill="#C9A84C"/><circle cx="86" cy="101" r="5" '
                      'fill="#C9A84C"/><circle cx="86" cy="125" r="5" fill="#C9A84C"/><circle cx="100" cy="101" r="5" fill="#C9A84C"/><circle cx="100" cy="125" r="5" fill="#C9A84C"/><circle cx="114" '
                      'cy="101" r="5" fill="#C9A84C"/><circle cx="114" cy="125" r="5" fill="#C9A84C"/><circle cx="128" cy="101" r="5" fill="#C9A84C"/><circle cx="128" cy="125" r="5" '
                      'fill="#C9A84C"/><circle cx="142" cy="101" r="5" fill="#C9A84C"/><circle cx="142" cy="125" r="5" fill="#C9A84C"/><circle cx="156" cy="101" r="5" fill="#C9A84C"/><circle '
                      'cx="156" cy="125" r="5" fill="#C9A84C"/><circle cx="170" cy="101" r="5" fill="#C9A84C"/><circle cx="170" cy="125" r="5" fill="#C9A84C"/><circle cx="184" cy="101" r="5" '
                      'fill="#C9A84C"/><circle cx="184" cy="125" r="5" fill="#C9A84C"/><circle cx="198" cy="101" r="5" fill="#C9A84C"/><circle cx="198" cy="125" r="5" fill="#C9A84C"/><circle '
                      'cx="212" cy="101" r="5" fill="#C9A84C"/><circle cx="212" cy="125" r="5" fill="#C9A84C"/><circle cx="226" cy="101" r="5" fill="#C9A84C"/><circle cx="226" cy="125" r="5" '
                      'fill="#C9A84C"/><circle cx="240" cy="101" r="5" fill="#C9A84C"/><circle cx="240" cy="125" r="5" fill="#C9A84C"/><circle cx="254" cy="101" r="5" fill="#C9A84C"/><circle '
                      'cx="254" cy="125" r="5" fill="#C9A84C"/><circle cx="268" cy="101" r="5" fill="#C9A84C"/><circle cx="268" cy="125" r="5" fill="#C9A84C"/><circle cx="282" cy="101" r="5" '
                      'fill="#C9A84C"/><circle cx="282" cy="125" r="5" fill="#C9A84C"/><circle cx="296" cy="101" r="5" fill="#C9A84C"/><circle cx="296" cy="125" r="5" fill="#C9A84C"/><circle '
                      'cx="310" cy="101" r="5" fill="#C9A84C"/><circle cx="310" cy="125" r="5" fill="#C9A84C"/><circle cx="324" cy="101" r="5" fill="#C9A84C"/><circle cx="324" cy="125" r="5" '
                      'fill="#C9A84C"/><circle cx="338" cy="101" r="5" fill="#C9A84C"/><circle cx="338" cy="125" r="5" fill="#C9A84C"/><circle cx="352" cy="101" r="5" fill="#C9A84C"/><circle '
                      'cx="352" cy="125" r="5" fill="#C9A84C"/><circle cx="366" cy="101" r="5" fill="#C9A84C"/><circle cx="366" cy="125" r="5" fill="#C9A84C"/><circle cx="380" cy="101" r="5" '
                      'fill="#C9A84C"/><circle cx="380" cy="125" r="5" fill="#C9A84C"/><circle cx="394" cy="101" r="5" fill="#C9A84C"/><circle cx="394" cy="125" r="5" fill="#C9A84C"/><circle '
                      'cx="408" cy="101" r="5" fill="#C9A84C"/><circle cx="408" cy="125" r="5" fill="#C9A84C"/><circle cx="422" cy="101" r="5" fill="#C9A84C"/><circle cx="422" cy="125" r="5" '
                      'fill="#C9A84C"/><circle cx="436" cy="101" r="5" fill="#C9A84C"/><circle cx="436" cy="125" r="5" fill="#C9A84C"/><circle cx="450" cy="101" r="5" fill="#C9A84C"/><circle '
                      'cx="450" cy="125" r="5" fill="#C9A84C"/><circle cx="464" cy="101" r="5" fill="#C9A84C"/><circle cx="464" cy="125" r="5" fill="#C9A84C"/><circle cx="478" cy="101" r="5" '
                      'fill="#C9A84C"/><circle cx="478" cy="125" r="5" fill="#C9A84C"/><circle cx="492" cy="101" r="5" fill="#C9A84C"/><circle cx="492" cy="125" r="5" fill="#C9A84C"/><circle '
                      'cx="506" cy="101" r="5" fill="#C9A84C"/><circle cx="506" cy="125" r="5" fill="#C9A84C"/><circle cx="520" cy="101" r="5" fill="#C9A84C"/><circle cx="520" cy="125" r="5" '
                      'fill="#C9A84C"/><circle cx="534" cy="101" r="5" fill="#C9A84C"/><circle cx="534" cy="125" r="5" fill="#C9A84C"/><circle cx="548" cy="101" r="5" fill="#C9A84C"/><circle '
                      'cx="548" cy="125" r="5" fill="#C9A84C"/><circle cx="562" cy="101" r="5" fill="#C9A84C"/><circle cx="562" cy="125" r="5" fill="#C9A84C"/><circle cx="576" cy="101" r="5" '
                      'fill="#C9A84C"/><circle cx="576" cy="125" r="5" fill="#C9A84C"/><circle cx="590" cy="101" r="5" fill="#C9A84C"/><circle cx="590" cy="125" r="5" fill="#C9A84C"/><circle '
                      'cx="604" cy="101" r="5" fill="#C9A84C"/><circle cx="604" cy="125" r="5" fill="#C9A84C"/><circle cx="618" cy="101" r="5" fill="#C9A84C"/><circle cx="618" cy="125" r="5" '
                      'fill="#C9A84C"/><circle cx="110" cy="60" r="5" fill="#DB2F30"/><circle cx="125" cy="72" r="5" fill="#DB2F30"/><circle cx="96" cy="74" r="5" fill="#DB2F30"/><circle cx="118" '
                      'cy="160" r="5" fill="#DB2F30"/><path d="M112 80 v70" stroke="#0A1F3D" stroke-width="2" stroke-dasharray="4 3"/><path d="M107 145 l5 8 l5 -8" fill="#0A1F3D"/><text x="112" '
                      'y="186" text-anchor="middle" font-weight="bold">Diffusion</text><text x="112" y="202" text-anchor="middle" font-size="11">small particles like oxygen</text><text x="112" '
                      'y="216" text-anchor="middle" font-size="11">slip through; no energy</text><rect x="300" y="92" width="16" height="42" fill="#0047BA"/><rect x="324" y="92" width="16" '
                      'height="42" fill="#0047BA"/><circle cx="320" cy="62" r="5" fill="#2a8fd6"/><circle cx="334" cy="70" r="5" fill="#2a8fd6"/><circle cx="310" cy="74" r="5" '
                      'fill="#2a8fd6"/><circle cx="320" cy="160" r="5" fill="#2a8fd6"/><path d="M320 80 v70" stroke="#0A1F3D" stroke-width="2" stroke-dasharray="4 3"/><path d="M315 145 l5 8 l5 -8" '
                      'fill="#0A1F3D"/><text x="320" y="186" text-anchor="middle" font-weight="bold">Osmosis</text><text x="320" y="202" text-anchor="middle" font-size="11">water through '
                      'channel</text><text x="320" y="216" text-anchor="middle" font-size="11">proteins; no energy</text><path d="M510 92 h36 v42 h-36z" fill="#6b3fa0"/><text x="528" y="118" '
                      'text-anchor="middle" fill="#fff" font-size="10">pump</text><circle cx="528" cy="160" r="5" fill="#3d9a2f"/><circle cx="528" cy="60" r="5" fill="#3d9a2f"/><circle cx="514" '
                      'cy="70" r="5" fill="#3d9a2f"/><circle cx="542" cy="68" r="5" fill="#3d9a2f"/><circle cx="528" cy="78" r="5" fill="#3d9a2f"/><path d="M490 152 v-84" stroke="#6b3fa0" '
                      'stroke-width="2"/><path d="M485 74 l5 -8 l5 8" fill="#6b3fa0"/><text x="482" y="74" text-anchor="end" font-size="10" fill="#6b3fa0">uses</text><text x="482" y="86" '
                      'text-anchor="end" font-size="10" fill="#6b3fa0">energy</text><text x="528" y="196" text-anchor="middle" font-weight="bold">Active transport</text><text x="528" y="212" '
                      'text-anchor="middle" font-size="11">pumps move particles from</text><text x="528" y="226" text-anchor="middle" font-size="11">low to high; needs energy</text></svg>',
            'html': '<p>Diffusion and osmosis are <b>passive transport</b>: particles move from high to low concentration without the cell spending energy, like a ball rolling '
                    'downhill.</p><p>Sometimes a cell needs to move particles the other way, from low concentration to high, like pushing a ball uphill. That takes energy and special protein '
                    '<b>pumps</b> in the membrane. This is <b>active transport</b>. The energy comes from the mitochondria, which release energy from glucose (Week 7).</p><p>Your nerve cells pump '
                    'certain particles in and out constantly so they can send signals. Root cells use active transport to pull minerals from the soil, even when the root already holds more minerals '
                    "than the soil around it. Mangrove trees on Florida's coasts use membranes and pumps in their roots and leaves to keep out or get rid of extra salt, so they can live in seawater "
                    'that would kill most plants.</p>',
            'checks': [{'t': 'open',
                        'key': 'passive',
                        'q': 'Explain the difference between passive and active transport. Use the hill comparison and the word energy.',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Passive: high to low concentration, no energy, like rolling downhill (diffusion, osmosis)', 'Active: low to high, needs energy and pumps, like pushing uphill'],
                        'model': 'Passive transport moves particles from high to low concentration, like a ball rolling downhill, so it needs no energy. Active transport moves particles from low to '
                                 'high concentration, like pushing a ball uphill, so the cell must use energy and protein pumps.'},
                       {'t': 'blanks',
                        'q': 'A root cell already holds more of a mineral than the soil around it, yet it keeps taking more in.',
                        'sent': 'This is ___ transport. Its energy is released from glucose by the ___.',
                        'blanks': [[{'all': [['active']], 'none': ['passive', 'not']}], ['mitochondria', 'mitochondrion']],
                        'show': 'active; mitochondria',
                        'pts': 2,
                        'why': 'Moving from low to high concentration needs energy from the mitochondria.'},
                       {'t': 'open',
                        'key': 'mangrove',
                        'q': 'Most garden plants die when salty seawater floods their soil, but mangroves thrive. Use osmosis to explain why salt kills garden plants, and explain how mangroves '
                             'survive.',
                        'min': 30,
                        'rows': 3,
                        'rubric': ['Salty soil pulls water out of root cells (or stops them from taking water in) by osmosis, so plants wilt and die',
                                   'Mangroves use membranes and pumps (active transport) to keep out or remove salt'],
                        'model': 'In salty soil there are more dissolved particles outside the roots, so osmosis pulls water out of the root cells instead of in, and the plant wilts and dies. '
                                 'Mangroves use special membranes and pumps in their roots and leaves to keep salt out or get rid of it, which takes energy.'}]}],
 'handson': {'title': 'The Potato Osmosis Test',
             'intro': 'Find out what happens to plant cells in fresh water and salt water, and measure the change.',
             'materials': ['One raw potato',
                           'A knife and cutting board (with an adult)',
                           'A ruler with millimeters',
                           'Two cups labeled Fresh and Salty, and a dry plate labeled Air',
                           'Water and table salt (about 2 tablespoons for 1 cup of water)',
                           'Paper towels',
                           'A timer, paper and pencil',
                           'Optional: a kitchen scale'],
             'steps': ["With an adult, cut six potato strips the same size, about 6 cm long and 1 cm thick. Measure and record each strip's length (and mass, if you have a scale).",
                       'Put two strips in fresh water, two in salt water, and two on a dry plate (Air) as a control.',
                       'Predict what will happen to each pair and write it down.',
                       'After 30 minutes, take the strips out, pat them dry, and measure their length again. Gently bend each one and describe how stiff or floppy it is.',
                       'Calculate the change in length for each strip and find the average for each cup.'],
             'record': [{'t': 'open',
                         'key': 'potdata',
                         'q': 'Make a data table: cup, starting length, ending length, change, and how stiff or floppy each strip felt. What pattern do you see?',
                         'min': 30,
                         'rows': 6,
                         'rubric': ['Complete table with measurements for all three conditions', 'Change calculated', 'Clear description of the pattern'],
                         'model': 'Fresh: 60 mm to 62 mm (+2), stiff and snappy. Salty: 60 mm to 56 mm (−4), soft and bendy. Air: 60 mm to 60 mm (0), a little dry. Fresh-water strips grew and got '
                                  'stiff; salt-water strips shrank and went floppy.'},
                        {'t': 'open',
                         'key': 'potcer',
                         'q': 'Write a claim, evidence and reasoning (CER) explaining your results. Name your independent variable, dependent variable and control.',
                         'min': 60,
                         'rows': 6,
                         'rubric': ['Claim: water moved into cells in fresh water and out of cells in salt water',
                                    'Evidence: specific measurements and stiffness from the table',
                                    'Reasoning: osmosis; water moves toward the side with more dissolved particles; vacuoles filled or shrank',
                                    'Variables: independent = type of water; dependent = change in length (or stiffness); control = air strips (or same size, same time)'],
                         'model': 'Claim: Water moved into the potato cells in fresh water and out of them in salt water. Evidence: The fresh-water strips grew from 60 to 62 mm and became stiff, '
                                  'while the salt-water strips shrank from 60 to 56 mm and went floppy. Reasoning: By osmosis, water moves toward the side with more dissolved particles. The potato '
                                  'cells had more dissolved particles than fresh water, so water moved in, filling the vacuoles. The salt water had more dissolved particles than the cells, so water '
                                  'moved out and the vacuoles shrank. The independent variable was the type of water, the dependent variable was the change in length, and the strips on the dry plate '
                                  'were the control.'}]},
 'think': {'intro': 'Use evidence and explain your reasoning. Your teacher scores these.',
           'items': [{'t': 'open',
                      'key': 'pickles',
                      'q': "Cucumbers become pickles by soaking in salty brine. Pickles are shrunken and wrinkly compared with fresh cucumbers. Explain what happens to the cucumber's cells during "
                           'pickling, then explain why salting meat or fish helped people preserve food for thousands of years before refrigerators.',
                      'min': 70,
                      'rows': 7,
                      'rubric': ['Brine is saltier than the cells, so water moves out by osmosis, and the cucumber shrinks',
                                 'Salt also pulls water out of bacteria and mold cells, so they cannot grow, which preserves food',
                                 'Uses osmosis and concentration correctly'],
                      'model': "The brine has many more dissolved particles than the cucumber's cells, so water moves out of the cells by osmosis. The cells shrink, so the pickle becomes smaller and "
                               'wrinkly. Salting meat or fish works the same way on bacteria and mold: the salt pulls water out of their cells by osmosis, so they cannot grow and spoil the food. '
                               'That is why people have used salt to preserve food for thousands of years.'},
                     {'t': 'open',
                      'key': 'design2',
                      'q': 'Design an investigation to find the salt concentration at which a potato strip neither gains nor loses length. Describe the solutions you would make, what you would '
                           'measure and how you would find the answer.',
                      'min': 60,
                      'rows': 6,
                      'rubric': ['Several solutions with increasing salt (for example 0, 1/4, 1/2, 1 and 2 teaspoons per cup)',
                                 'Same size strips and time; measure change in length; repeated trials',
                                 'Find where change is zero (between the last gain and the first loss), possibly using a graph'],
                      'model': 'I would make five cups with 0, 1/4, 1/2, 1 and 2 teaspoons of salt in 1 cup of water. I would put two strips of the same size in each for 30 minutes and measure the '
                               'change in length. Then I would graph salt amount against change in length. Where the line crosses zero is the concentration that matches the potato cells, so the '
                               'strips neither gain nor lose water.'}]},
 'exit': [{'t': 'open',
           'key': 'exit_diff',
           'q': 'Define diffusion in your own words and give one everyday example.',
           'min': 12,
           'rows': 2,
           'rubric': ['Particles moving from high to low concentration', 'A correct example (smell spreading, dye in water, oxygen into cells)'],
           'model': 'Diffusion is particles spreading from where they are crowded to where they are less crowded, like the smell of cookies spreading through a house.'},
          {'t': 'text', 'q': 'What is the name for the diffusion of water across a membrane?', 'a': ['osmosis'], 'show': 'osmosis', 'pts': 2, 'why': 'Osmosis.'},
          {'t': 'text',
           'q': 'Which kind of transport needs energy from the cell?',
           'a': [{'all': [['active']], 'none': ['passive', 'not']}],
           'show': 'active transport',
           'pts': 2,
           'why': 'Active transport uses energy and protein pumps to move particles from low to high concentration.'},
          {'t': 'open',
           'key': 'exit_salad',
           'q': 'A salad with salty dressing goes limp after an hour. Why?',
           'min': 12,
           'rows': 2,
           'rubric': ['Dressing has more dissolved particles than the lettuce cells, so water moves out of the cells by osmosis'],
           'model': 'The salty dressing has more dissolved particles than the lettuce cells, so water moves out of the cells by osmosis, the vacuoles shrink and the leaves go limp.'}],
 'next': 'Week 10: the Unit 2 checkpoint and your Cell Model Project.'}

TEACHER = {
 "standards": [
  "SC.6.L.14.3: Recognize and explore how cells of all organisms undergo similar processes to maintain homeostasis, including extracting energy from food, getting rid of waste, and reproducing.",
  "SC.6.L.14.4: Compare and contrast the structure and function of major organelles of plant and animal cells, including cell wall, cell membrane, nucleus, cytoplasm, chloroplasts, mitochondria, and vacuoles.",
  "SC.6.N.1.1: Define a problem from the sixth grade curriculum, use appropriate reference materials to support scientific understanding, plan and carry out scientific investigation of various types, such as systematic observations or experiments, identify variables, collect and organize data, interpret data in charts, tables, and graphics, analyze information, make predictions, and defend conclusions.",
  "SC.6.N.1.2: Explain why scientific investigations should be replicable.",
  "NGSS MS-LS1-2: Develop and use a model to describe the function of a cell as a whole and ways the parts of cells contribute to the function."],
 "materials": ["The interactive lesson", "A clear glass of hot tap water, a glass of cold water and food coloring (for a quick diffusion demo)", "A raw potato, a knife and cutting board (adult), a ruler with millimeters, two cups and a plate, salt, paper towels, a timer", "Optional: a stalk of limp celery in water overnight; a kitchen scale", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 8 Reconnect questions."],
  [5, "Hook", "Read Coleridge's two lines and ask why sailors could not drink seawater."],
  [10, "Diffusion", "Drop food coloring in hot and cold water side by side. Observe while discussing."],
  [12, "Osmosis", "Work through the three-cup diagram. Predict the celery and the seawater questions."],
  [8, "Active transport", "Use the hill comparison. Connect pumps to mitochondria and mangroves."],
  [14, "Potato test", "Cut and measure strips together and start the 30-minute soak; the student measures and records after the lesson."],
  [5, "Assign", "Assign Think Deeper and the Exit Check."]],
 "key_questions": ["Where are the particles crowded, and where will they go?", "Which side has more dissolved particles? Which way will water move?", "Does this need energy? How do you know?", "What was your control, and why did you need it?"],
 "misconceptions": ["Salt moves into the cell in osmosis (it is water that moves).", "Diffusion stops when particles are evenly spread (they keep moving, but evenly in both directions).", "Water moves toward the side with more water.", "Only animal cells use active transport."],
 "support": ["Use the phrase \"water follows salt\" as a memory aid.", "Provide a blank data table for the potato test.", "Act out diffusion: the family crowds in one corner, then slowly spreads around the room."],
 "challenge": ["Run the design from Think Deeper and graph the results.", "Research saltwater intrusion into Florida's coastal aquifers and explain the role of osmosis in its effects on plants."],
 "background": "<p>Osmosis is described here at a Grade 6 level as water diffusing toward higher solute concentration; terms like hypotonic and hypertonic are deliberately left out. Seawater averages about 3.5 percent salt, nearly four times the salt concentration of human blood plasma (about 0.9 percent, the concentration of normal saline). Peter Agre identified the aquaporin protein (AQP1) in 1992 and shared the 2003 Nobel Prize in Chemistry. Mangroves use salt exclusion at the roots (red mangroves) and salt-excreting glands in the leaves (black and white mangroves). The Coleridge lines are from The Rime of the Ancient Mariner as revised in 1817 (the 1798 original reads \"Ne any drop to drink\"), in the public domain. The 30-minute potato soak gives measurable changes of a few millimeters; longer soaks give larger changes.</p>",
 "sources": ["Nobel Prize, Peter Agre, Nobel Prize in Chemistry 2003, Facts.", "CK-12 Life Science, Diffusion, Osmosis and Active Transport.", "Florida Department of Environmental Protection, Mangroves.", "Coleridge, S. T. (1798), The Rime of the Ancient Mariner."]
}

PRINT = {
 "directions": "Use complete sentences.",
 "items": [
  {"q":"Define diffusion and give an example.","a":"Particles move from high to low concentration, such as a smell spreading through a room.","lines":2},
  {"q":"What is osmosis?","a":"The diffusion of water across a selectively permeable membrane.","lines":2},
  {"q":"A plant cell is placed in fresh water. Which way does water move, and what happens to the cell?","a":"Water moves in; the vacuole swells and the cell becomes firm.","lines":2},
  {"q":"Why does a potato strip become floppy in salt water?","a":"Water moves out of its cells by osmosis toward the saltier water, so the vacuoles shrink.","lines":2},
  {"q":"How is active transport different from diffusion?","a":"Active transport uses energy and pumps to move particles from low to high concentration; diffusion needs no energy.","lines":2},
  {"q":"Why can't people drink seawater to stay alive?","a":"It is saltier than body fluids, so it pulls water out of cells, and the kidneys need extra water to remove the salt.","lines":2}]
}
