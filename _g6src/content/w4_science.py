HOURS = [8, 10, 12, 14, 16]
SUN = [24, 29, 35, 37, 33]
SHADE = [23, 25, 28, 29, 28]

def linegraph():
    x0, y0, w, h = 70, 210, 420, 170
    X = lambda i: x0 + i * (w / 4)
    Y = lambda t: y0 - (t - 20) * (h / 20)
    s = ('<svg viewBox="0 0 560 260" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Line graph of temperature in sun and shade">'
         '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Temperature in the Sun and in the Shade, Okafor yard (Gainesville)</text>')
    for t in range(20, 41, 5):
        s += f'<line x1="{x0}" y1="{Y(t)}" x2="{x0+w}" y2="{Y(t)}" stroke="#e1e6ee"/><text x="{x0-8}" y="{Y(t)+4}" text-anchor="end">{t}</text>'
    for i, hr in enumerate(HOURS):
        lab = f'{hr if hr <= 12 else hr-12} {"AM" if hr < 12 else "PM"}'
        s += f'<text x="{X(i)}" y="{y0+18}" text-anchor="middle">{lab}</text>'
    s += f'<line x1="{x0}" y1="{y0}" x2="{x0+w}" y2="{y0}" stroke="#0A1F3D"/><line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0-h}" stroke="#0A1F3D"/>'
    for data, c in [(SUN, '#DB2F30'), (SHADE, '#0047BA')]:
        s += '<polyline fill="none" stroke="%s" stroke-width="3" points="%s"/>' % (c, ' '.join(f'{X(i)},{Y(t)}' for i, t in enumerate(data)))
        s += ''.join(f'<circle cx="{X(i)}" cy="{Y(t)}" r="4" fill="{c}"/>' for i, t in enumerate(data))
    s += (f'<text x="{x0+w+6}" y="{Y(33)+4}" fill="#DB2F30" font-weight="bold">Sun</text><text x="{x0+w+6}" y="{Y(28)+4}" fill="#0047BA" font-weight="bold">Shade</text>'
          f'<text x="20" y="{y0-h/2}" transform="rotate(-90 20 {y0-h/2})" text-anchor="middle">Temperature (°C)</text>'
          f'<text x="{x0+w/2}" y="{y0+38}" text-anchor="middle">Time of day</text></svg>')
    return s

CHOOSE = ('<svg viewBox="0 0 560 200" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Four kinds of graphs and what each is for">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Pick the graph that fits the question</text>'
  '<g transform="translate(15 35)"><rect width="125" height="150" rx="8" fill="#fff" stroke="#0047BA"/><polyline points="15,95 45,70 75,78 105,35" fill="none" stroke="#DB2F30" stroke-width="3"/><text x="62" y="122" text-anchor="middle" font-weight="bold">Line graph</text><text x="62" y="140" text-anchor="middle" font-size="11">change over time</text></g>'
  '<g transform="translate(150 35)"><rect width="125" height="150" rx="8" fill="#fff" stroke="#0047BA"/><rect x="18" y="60" width="20" height="40" fill="#0047BA"/><rect x="48" y="35" width="20" height="65" fill="#0047BA"/><rect x="78" y="75" width="20" height="25" fill="#0047BA"/><text x="62" y="122" text-anchor="middle" font-weight="bold">Bar graph</text><text x="62" y="140" text-anchor="middle" font-size="11">compare categories</text></g>'
  '<g transform="translate(285 35)"><rect width="125" height="150" rx="8" fill="#fff" stroke="#0047BA"/><circle cx="62" cy="62" r="40" fill="#C9A84C"/><path d="M62 62 L62 22 A40 40 0 0 1 100 74Z" fill="#DB2F30"/><path d="M62 62 L100 74 A40 40 0 0 1 40 96Z" fill="#0047BA"/><text x="62" y="122" text-anchor="middle" font-weight="bold">Circle graph</text><text x="62" y="140" text-anchor="middle" font-size="11">parts of a whole</text></g>'
  '<g transform="translate(420 35)"><rect width="125" height="150" rx="8" fill="#fff" stroke="#0047BA"/>'
  + ''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="#0A1F3D"/>' for x, y in [(20, 95), (32, 88), (45, 84), (55, 74), (68, 70), (80, 58), (92, 52), (104, 40)]) +
  '<text x="62" y="122" text-anchor="middle" font-weight="bold">Scatter plot</text><text x="62" y="140" text-anchor="middle" font-size="11">is there a relationship?</text></g></svg>')

def misleading():
    s = ('<svg viewBox="0 0 560 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="The same rainfall data graphed two ways">'
         '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Same data, two graphs: yearly rainfall (inches)</text>')
    for gx, base, title in [(40, 40, 'Graph A: axis starts at 40'), (310, 0, 'Graph B: axis starts at 0')]:
        top = 48 if base == 40 else 50
        sc = 150 / (top - base)
        s += f'<text x="{gx+105}" y="42" text-anchor="middle" font-weight="bold">{title}</text>'
        for v in range(base, top + 1, 2 if base == 40 else 10):
            y = 200 - (v - base) * sc
            s += f'<line x1="{gx+30}" y1="{y}" x2="{gx+200}" y2="{y}" stroke="#e1e6ee"/><text x="{gx+24}" y="{y+4}" text-anchor="end" font-size="10">{v}</text>'
        for i, (town, v) in enumerate([("Palmdale", 42), ("Cedar Key", 46)]):
            hgt = (v - base) * sc
            s += f'<rect x="{gx+55+i*80}" y="{200-hgt}" width="50" height="{hgt}" fill="{["#0047BA", "#DB2F30"][i]}"/><text x="{gx+80+i*80}" y="216" text-anchor="middle" font-size="11">{town}</text>'
        s += f'<line x1="{gx+30}" y1="200" x2="{gx+200}" y2="200" stroke="#0A1F3D"/><line x1="{gx+30}" y1="200" x2="{gx+30}" y2="50" stroke="#0A1F3D"/>'
    return s + '</svg>'

CONE = ('<svg viewBox="0 -30 560 280" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Simplified hurricane forecast cone">'
  '<rect y="-30" width="560" height="280" fill="#dbeaf7"/>'
  '<path d="M330 -30 L330 60 Q300 90 318 130 Q340 170 330 210 L345 250 L560 250 L560 -30Z" fill="#d9c7a0" stroke="#8a6d1f"/>'
  '<text x="470" y="150" text-anchor="middle" font-weight="bold" fill="#5b4a1c">FLORIDA</text><text x="470" y="166" text-anchor="middle" font-size="10" fill="#5b4a1c">(simplified)</text>'
  '<path d="M72 222 L166 190 L262 164 L348 134 L414 112 L469 95 A62 62 0 0 0 411 -15 L411 -15 L366 20 L312 62 L238 112 L154 160 L68 214Z" fill="#ffffff" fill-opacity=".6" stroke="#DB2F30" stroke-dasharray="6 4"/><polyline points="70,218 160,175 250,138 330,98 390,66 440,40" fill="none" stroke="#0A1F3D" stroke-width="2.5"/>'
  '<circle cx="70" cy="218" r="6" fill="#DB2F30" stroke="#fff"/><text x="60" y="236" text-anchor="end" font-size="10" font-weight="bold">Now</text><circle cx="160" cy="175" r="6" fill="#DB2F30" stroke="#fff"/><text x="150" y="193" text-anchor="end" font-size="10" font-weight="bold">Day 1</text><circle cx="250" cy="138" r="6" fill="#DB2F30" stroke="#fff"/><text x="240" y="156" text-anchor="end" font-size="10" font-weight="bold">Day 2</text><circle cx="330" cy="98" r="6" fill="#DB2F30" stroke="#fff"/><text x="320" y="116" text-anchor="end" font-size="10" font-weight="bold">Day 3</text><circle cx="390" cy="66" r="6" fill="#DB2F30" stroke="#fff"/><text x="380" y="84" text-anchor="end" font-size="10" font-weight="bold">Day 4</text><circle cx="440" cy="40" r="6" fill="#DB2F30" stroke="#fff"/><text x="430" y="58" text-anchor="end" font-size="10" font-weight="bold">Day 5</text>'
  '<text x="20" y="22" font-weight="bold" fill="#0A1F3D" font-size="15">A forecast cone is a model</text>'
  '<text x="20" y="42" font-size="11">White area: where the storm\'s CENTER will probably go.</text>'
  '<text x="20" y="58" font-size="11">It widens because forecasts are less certain further ahead.</text>'
  '<text x="20" y="74" font-size="11" fill="#DB2F30">It does NOT show the size of the storm. Wind, rain and</text>'
  '<text x="20" y="90" font-size="11" fill="#DB2F30">flooding can reach far outside the cone.</text></svg>')

LESSON = {'unit': 'Unit 1: Thinking Like a Scientist',
 'title': 'Graphs, Models and Scientific Tools',
 'subtitle': 'A good graph lets data speak. A good model lets scientists study what is too big, too small or too far away to touch.',
 'objectives': ['Choose the right graph (line, bar, circle or scatter) for a question and a set of data.',
                'Build and read a line graph with a title, labeled axes, units and an even scale.',
                'Spot a misleading graph and explain how it tricks the reader.',
                'Explain what scientific models are, why scientists use them, and their limits.',
                'Read a hurricane forecast cone correctly as a model of uncertainty.'],
 'vocab': [['graph', 'A picture of data that shows patterns, comparisons or relationships.'],
           ['axis (plural axes)', 'The reference lines of a graph. The x-axis runs across; the y-axis runs up and down.'],
           ['scale', 'The evenly spaced numbers along an axis.'],
           ['trend', 'The general direction data moves, such as increasing, decreasing or staying the same.'],
           ['model', 'A representation of an object, process or system that helps scientists study or explain it. Models can be physical, drawings, math or computer programs.'],
           ['limitation', 'A way a model is different from the real thing, so it cannot show or predict everything.'],
           ['uncertainty', 'How much a measurement or prediction might be off. Honest science reports it.'],
           ['misleading', 'Giving the wrong idea, even when the numbers themselves are true.']],
 'reconnect': {'title': 'Week 3: measuring and recording data',
               'intro': 'Graphs are built from data tables, so every graph starts with good measurement.',
               'items': [{'t': 'num', 'q': 'Convert 2.5 kilometers to meters.', 'a': 2500, 'unit': 'm', 'pts': 2, 'why': 'Down three steps: 2.5 × 1,000 = 2,500 m.'},
                         {'t': 'num', 'q': 'Convert 480 milliliters to liters.', 'a': 0.48, 'unit': 'L', 'pts': 2, 'why': 'Up three steps: 480 ÷ 1,000 = 0.48 L.'},
                         {'t': 'text',
                          'q': 'When you read a graduated cylinder, which part of the curved surface do you read?',
                          'a': [{'all': [['bottom', 'lowest']]}],
                          'show': 'the bottom of the meniscus',
                          'pts': 2,
                          'why': 'Read at eye level at the bottom of the meniscus.'},
                         {'t': 'text',
                          'q': 'Three measurements of 51.2 g, 51.3 g and 51.2 g are close together but the true mass is 60 g. Are they accurate, precise, both or neither?',
                          'a': [{'all': [['precise']], 'none': ['both', 'and accurate', 'is accurate', 'are accurate', 'precise and accurate']}],
                          'show': 'precise but not accurate',
                          'pts': 2,
                          'why': 'Close together (precise) but far from the true value (not accurate).'},
                         {'t': 'num', 'q': 'Trials of 14 cm, 17 cm and 14 cm were recorded. What is the average?', 'a': 15, 'unit': 'cm', 'pts': 2, 'why': '(14 + 17 + 14) ÷ 3 = 45 ÷ 3 = 15 cm.'},
                         {'t': 'open',
                          'key': 'rc_table',
                          'q': 'What belongs in the heading of every column in a data table, besides the name of the variable? Why does it matter?',
                          'min': 10,
                          'rows': 2,
                          'rubric': ['Names units', 'Explains that numbers without units can be misread (Mars Climate Orbiter)'],
                          'model': 'The units, like cm or °C, because a number without a unit can be misread. That is how the Mars Climate Orbiter was lost.'}]},
 'hook': {'title': 'Is the Shade Really Cooler?',
          'html': '<p>Every kid in a hot place knows to park the bike in the shade. But how much cooler is it, and does the difference change during the day? The Okafor family from Week 1 set two '
                  'thermometers in their yard outside Gainesville, one in full sun and one under the live oak, and recorded the temperature every two hours.</p><table '
                  "class='t'><tr><th>Time</th><th>8 AM</th><th>10 AM</th><th>12 PM</th><th>2 PM</th><th>4 PM</th></tr><tr><td>Sun "
                  '(°C)</td><td>24</td><td>29</td><td>35</td><td>37</td><td>33</td></tr><tr><td>Shade (°C)</td><td>23</td><td>25</td><td>28</td><td>29</td><td>28</td></tr></table><p>The table holds '
                  "the facts, but it is hard to <i>see</i> the story. Watch what happens when the same numbers become a graph.</p><div class='callout'><b>Big idea:</b> Graphs and models are tools "
                  'for thinking. Each one shows some things clearly and hides others.</div>'},
 'learn': [{'title': 'Reading a Line Graph',
            'visual': '<svg viewBox="0 0 560 260" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Line graph of temperature in sun and shade"><text '
                      'x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Temperature in the Sun and in the Shade, Okafor yard (Gainesville)</text><line x1="70" y1="210.0" '
                      'x2="490" y2="210.0" stroke="#e1e6ee"/><text x="62" y="214.0" text-anchor="end">20</text><line x1="70" y1="167.5" x2="490" y2="167.5" stroke="#e1e6ee"/><text x="62" y="171.5" '
                      'text-anchor="end">25</text><line x1="70" y1="125.0" x2="490" y2="125.0" stroke="#e1e6ee"/><text x="62" y="129.0" text-anchor="end">30</text><line x1="70" y1="82.5" x2="490" '
                      'y2="82.5" stroke="#e1e6ee"/><text x="62" y="86.5" text-anchor="end">35</text><line x1="70" y1="40.0" x2="490" y2="40.0" stroke="#e1e6ee"/><text x="62" y="44.0" '
                      'text-anchor="end">40</text><text x="70.0" y="228" text-anchor="middle">8 AM</text><text x="175.0" y="228" text-anchor="middle">10 AM</text><text x="280.0" y="228" '
                      'text-anchor="middle">12 PM</text><text x="385.0" y="228" text-anchor="middle">2 PM</text><text x="490.0" y="228" text-anchor="middle">4 PM</text><line x1="70" y1="210" '
                      'x2="490" y2="210" stroke="#0A1F3D"/><line x1="70" y1="210" x2="70" y2="40" stroke="#0A1F3D"/><polyline fill="none" stroke="#DB2F30" stroke-width="3" points="70.0,176.0 '
                      '175.0,133.5 280.0,82.5 385.0,65.5 490.0,99.5"/><circle cx="70.0" cy="176.0" r="4" fill="#DB2F30"/><circle cx="175.0" cy="133.5" r="4" fill="#DB2F30"/><circle cx="280.0" '
                      'cy="82.5" r="4" fill="#DB2F30"/><circle cx="385.0" cy="65.5" r="4" fill="#DB2F30"/><circle cx="490.0" cy="99.5" r="4" fill="#DB2F30"/><polyline fill="none" stroke="#0047BA" '
                      'stroke-width="3" points="70.0,184.5 175.0,167.5 280.0,142.0 385.0,133.5 490.0,142.0"/><circle cx="70.0" cy="184.5" r="4" fill="#0047BA"/><circle cx="175.0" cy="167.5" r="4" '
                      'fill="#0047BA"/><circle cx="280.0" cy="142.0" r="4" fill="#0047BA"/><circle cx="385.0" cy="133.5" r="4" fill="#0047BA"/><circle cx="490.0" cy="142.0" r="4" '
                      'fill="#0047BA"/><text x="496" y="103.5" fill="#DB2F30" font-weight="bold">Sun</text><text x="496" y="146.0" fill="#0047BA" font-weight="bold">Shade</text><text x="20" '
                      'y="125.0" transform="rotate(-90 20 125.0)" text-anchor="middle">Temperature (°C)</text><text x="280.0" y="248" text-anchor="middle">Time of day</text></svg>',
            'html': '<p>Every good graph has <b>TAILS</b>: a <b>T</b>itle, <b>A</b>xes labeled, <b>I</b>ntervals that are even, <b>L</b>abels with units, and a <b>S</b>cale that fits the data. The '
                    'independent variable (time) goes on the x-axis; the dependent variable (temperature) goes on the y-axis.</p>',
            'checks': [{'t': 'num', 'q': 'At 2 PM, how many degrees warmer is the sun than the shade?', 'a': 8, 'unit': '°C', 'pts': 2, 'why': '37 − 29 = 8 °C.'},
                       {'t': 'text',
                        'q': 'At what time is the difference between sun and shade the smallest?',
                        'a': ['8 am', '8', '8:00', '8:00 am', '8 a.m.', '8am', '8 in the morning', '8 oclock', "8 o'clock", 'eight'],
                        'show': '8 AM',
                        'pts': 2,
                        'why': 'At 8 AM the difference is only 1 °C, because the sun has not had time to heat the open ground.'},
                       {'t': 'text',
                        'q': 'Describe the trend in the sun temperature from 2 PM to 4 PM.',
                        'a': [{'all': [['decrease', 'down', 'drop', 'fell', 'fall', 'cool', 'lower', 'colder', 'declin', 'less']],
                               'none': ['goes up', 'went up', 'increas', 'rise', 'rose', 'not go down', "doesn't go down"]}],
                        'show': 'It decreases (drops from 37 °C to 33 °C).',
                        'pts': 2,
                        'why': 'The line slopes down: the temperature is decreasing as the sun gets lower.'},
                       {'t': 'text',
                        'q': 'Which variable is on the x-axis, and is it the independent or dependent variable?',
                        'a': [{'all': [['time'], ['independent']]}],
                        'show': 'time, the independent variable',
                        'pts': 3,
                        'why': 'Time goes on the x-axis. The temperature depends on the time, not the other way around.'},
                       {'t': 'open',
                        'key': 'predict6',
                        'q': 'Predict the sun and shade temperatures at 6 PM. Use the trend on the graph to explain your prediction.',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Predicts both temperatures lower than at 4 PM', 'Predicts the gap narrowing', 'Uses the trend to justify'],
                        'model': 'I predict about 30 °C in the sun and 27 °C in the shade. Both lines are going down after 2 PM, and the gap is getting smaller as the sun gets lower, so by 6 PM they '
                                 'should be closer together.'}]},
           {'title': 'Choosing the Right Graph',
            'visual': '<svg viewBox="0 0 560 200" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Four kinds of graphs and what each is for"><text '
                      'x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Pick the graph that fits the question</text><g transform="translate(15 35)"><rect '
                      'width="125" height="150" rx="8" fill="#fff" stroke="#0047BA"/><polyline points="15,95 45,70 75,78 105,35" fill="none" stroke="#DB2F30" stroke-width="3"/><text x="62" y="122" '
                      'text-anchor="middle" font-weight="bold">Line graph</text><text x="62" y="140" text-anchor="middle" font-size="11">change over time</text></g><g transform="translate(150 '
                      '35)"><rect width="125" height="150" rx="8" fill="#fff" stroke="#0047BA"/><rect x="18" y="60" width="20" height="40" fill="#0047BA"/><rect x="48" y="35" width="20" height="65" '
                      'fill="#0047BA"/><rect x="78" y="75" width="20" height="25" fill="#0047BA"/><text x="62" y="122" text-anchor="middle" font-weight="bold">Bar graph</text><text x="62" y="140" '
                      'text-anchor="middle" font-size="11">compare categories</text></g><g transform="translate(285 35)"><rect width="125" height="150" rx="8" fill="#fff" stroke="#0047BA"/><circle '
                      'cx="62" cy="62" r="40" fill="#C9A84C"/><path d="M62 62 L62 22 A40 40 0 0 1 100 74Z" fill="#DB2F30"/><path d="M62 62 L100 74 A40 40 0 0 1 40 96Z" fill="#0047BA"/><text x="62" '
                      'y="122" text-anchor="middle" font-weight="bold">Circle graph</text><text x="62" y="140" text-anchor="middle" font-size="11">parts of a whole</text></g><g '
                      'transform="translate(420 35)"><rect width="125" height="150" rx="8" fill="#fff" stroke="#0047BA"/><circle cx="20" cy="95" r="4" fill="#0A1F3D"/><circle cx="32" cy="88" r="4" '
                      'fill="#0A1F3D"/><circle cx="45" cy="84" r="4" fill="#0A1F3D"/><circle cx="55" cy="74" r="4" fill="#0A1F3D"/><circle cx="68" cy="70" r="4" fill="#0A1F3D"/><circle cx="80" '
                      'cy="58" r="4" fill="#0A1F3D"/><circle cx="92" cy="52" r="4" fill="#0A1F3D"/><circle cx="104" cy="40" r="4" fill="#0A1F3D"/><text x="62" y="122" text-anchor="middle" '
                      'font-weight="bold">Scatter plot</text><text x="62" y="140" text-anchor="middle" font-size="11">is there a relationship?</text></g></svg>',
            'html': '<p>Before you graph, ask what question the graph should answer.</p><ul><li><b>How did something change over time?</b> Line graph.</li><li><b>How do separate groups compare?</b> '
                    'Bar graph.</li><li><b>What fraction of the whole is each part?</b> Circle graph. The parts must add up to 100%.</li><li><b>When one thing goes up, does another change too?</b> '
                    'Scatter plot.</li></ul>',
            'checks': [{'t': 'text',
                        'q': "A student measures her bean plant's height every day for three weeks. Which graph fits best?",
                        'a': [{'all': [['line']]}],
                        'show': 'a line graph',
                        'pts': 2,
                        'why': 'Height changing over time calls for a line graph.'},
                       {'t': 'text',
                        'q': 'A survey asks 40 families which pet they own, and you want to show what fraction of families chose each pet. Which graph fits best?',
                        'a': [{'all': [['circle', 'pie']]}],
                        'show': 'a circle graph',
                        'pts': 2,
                        'why': 'Parts of one whole group fit a circle graph.'},
                       {'t': 'text',
                        'q': 'You test how far four different balls bounce. Which graph fits best?',
                        'a': [{'all': [['bar']]}],
                        'show': 'a bar graph',
                        'pts': 2,
                        'why': 'Comparing separate categories (types of balls) fits a bar graph.'},
                       {'t': 'open',
                        'key': 'scatter',
                        'q': "A coach records each runner's hours of sleep and their race time. What graph should she use, and what would she look for in it?",
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Scatter plot', 'Looks for a relationship or pattern between the two variables', 'Notes that a pattern does not prove one causes the other'],
                        'model': 'A scatter plot, with hours of sleep on one axis and race time on the other. She would look for a pattern, such as runners who sleep more having faster times. Even '
                                 'if there is a pattern, it does not prove sleep caused the faster times.'}]},
           {'title': 'How Graphs Can Mislead',
            'visual': '<svg viewBox="0 0 560 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="The same rainfall data graphed two ways"><text x="280" '
                      'y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Same data, two graphs: yearly rainfall (inches)</text><text x="145" y="42" text-anchor="middle" '
                      'font-weight="bold">Graph A: axis starts at 40</text><line x1="70" y1="200.0" x2="240" y2="200.0" stroke="#e1e6ee"/><text x="64" y="204.0" text-anchor="end" '
                      'font-size="10">40</text><line x1="70" y1="162.5" x2="240" y2="162.5" stroke="#e1e6ee"/><text x="64" y="166.5" text-anchor="end" font-size="10">42</text><line x1="70" '
                      'y1="125.0" x2="240" y2="125.0" stroke="#e1e6ee"/><text x="64" y="129.0" text-anchor="end" font-size="10">44</text><line x1="70" y1="87.5" x2="240" y2="87.5" '
                      'stroke="#e1e6ee"/><text x="64" y="91.5" text-anchor="end" font-size="10">46</text><line x1="70" y1="50.0" x2="240" y2="50.0" stroke="#e1e6ee"/><text x="64" y="54.0" '
                      'text-anchor="end" font-size="10">48</text><rect x="95" y="162.5" width="50" height="37.5" fill="#0047BA"/><text x="120" y="216" text-anchor="middle" '
                      'font-size="11">Palmdale</text><rect x="175" y="87.5" width="50" height="112.5" fill="#DB2F30"/><text x="200" y="216" text-anchor="middle" font-size="11">Cedar Key</text><line '
                      'x1="70" y1="200" x2="240" y2="200" stroke="#0A1F3D"/><line x1="70" y1="200" x2="70" y2="50" stroke="#0A1F3D"/><text x="415" y="42" text-anchor="middle" '
                      'font-weight="bold">Graph B: axis starts at 0</text><line x1="340" y1="200.0" x2="510" y2="200.0" stroke="#e1e6ee"/><text x="334" y="204.0" text-anchor="end" '
                      'font-size="10">0</text><line x1="340" y1="170.0" x2="510" y2="170.0" stroke="#e1e6ee"/><text x="334" y="174.0" text-anchor="end" font-size="10">10</text><line x1="340" '
                      'y1="140.0" x2="510" y2="140.0" stroke="#e1e6ee"/><text x="334" y="144.0" text-anchor="end" font-size="10">20</text><line x1="340" y1="110.0" x2="510" y2="110.0" '
                      'stroke="#e1e6ee"/><text x="334" y="114.0" text-anchor="end" font-size="10">30</text><line x1="340" y1="80.0" x2="510" y2="80.0" stroke="#e1e6ee"/><text x="334" y="84.0" '
                      'text-anchor="end" font-size="10">40</text><line x1="340" y1="50.0" x2="510" y2="50.0" stroke="#e1e6ee"/><text x="334" y="54.0" text-anchor="end" font-size="10">50</text><rect '
                      'x="365" y="74.0" width="50" height="126.0" fill="#0047BA"/><text x="390" y="216" text-anchor="middle" font-size="11">Palmdale</text><rect x="445" y="62.0" width="50" '
                      'height="138.0" fill="#DB2F30"/><text x="470" y="216" text-anchor="middle" font-size="11">Cedar Key</text><line x1="340" y1="200" x2="510" y2="200" stroke="#0A1F3D"/><line '
                      'x1="340" y1="200" x2="340" y2="50" stroke="#0A1F3D"/></svg>',
            'html': '<p>Both graphs use the same true numbers: Palmdale gets 42 inches of rain a year and Cedar Key gets 46. (Example data.) Graph A starts its y-axis at 40, so the Cedar Key bar '
                    'looks three times taller. Graph B starts at 0 and shows the honest picture: the towns get similar amounts of rain.</p><p>Other tricks: uneven intervals, missing labels, '
                    'cherry-picked dates, or pictures that grow in two directions at once. A careful scientist always checks the axes first.</p><p><b>Bar graphs must start at 0</b>, because the '
                    'length of a bar shows the amount. A line graph, like the Okafor temperature graph, may start at another value if the axis is clearly labeled, because it shows change, and 0 °C '
                    'does not mean "no temperature."</p>',
            'checks': [{'t': 'num', 'q': 'How many more inches of rain does Cedar Key get than Palmdale?', 'a': 4, 'unit': 'inches', 'pts': 2, 'why': '46 − 42 = 4 inches.'},
                       {'t': 'num',
                        'q': 'In Graph A, the Palmdale bar rises 2 units above the axis and the Cedar Key bar rises 6. How many times taller does the Cedar Key bar look?',
                        'a': 3,
                        'unit': 'times',
                        'pts': 3,
                        'why': '6 ÷ 2 = 3, even though 46 is only about 1.1 times 42.'},
                       {'t': 'open',
                        'key': 'whymislead',
                        'q': 'Why might someone choose to make a graph like Graph A? Give a real-world example of who might do this.',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Explains it exaggerates differences', 'Gives a plausible real example (an ad, a campaign, a company report)', 'Suggests how a reader should respond'],
                        'model': "Someone might want a small difference to look huge. A company could use it in an ad to make its battery look like it lasts much longer than a competitor's. A reader "
                                 'should check where the y-axis starts before believing the picture.'}]},
           {'title': 'Models and Their Limits',
            'visual': '<svg viewBox="0 -30 560 280" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Simplified hurricane forecast cone"><rect width="560" '
                      'height="250" fill="#dbeaf7"/><path d="M330 -30 L330 60 Q300 90 318 130 Q340 170 330 210 L345 250 L560 250 L560 -30Z" fill="#d9c7a0" stroke="#8a6d1f"/><text x="470" y="150" '
                      'text-anchor="middle" font-weight="bold" fill="#5b4a1c">FLORIDA</text><text x="470" y="166" text-anchor="middle" font-size="10" fill="#5b4a1c">(simplified)</text><path d="M72 '
                      '222 L166 190 L262 164 L348 134 L414 112 L469 95 A62 62 0 0 0 411 -15 L411 -15 L366 20 L312 62 L238 112 L154 160 L68 214Z" fill="#ffffff" fill-opacity=".6" stroke="#DB2F30" '
                      'stroke-dasharray="6 4"/><polyline points="70,218 160,175 250,138 330,98 390,66 440,40" fill="none" stroke="#0A1F3D" stroke-width="2.5"/><circle cx="70" cy="218" r="6" '
                      'fill="#DB2F30" stroke="#fff"/><text x="60" y="236" text-anchor="end" font-size="10" font-weight="bold">Now</text><circle cx="160" cy="175" r="6" fill="#DB2F30" '
                      'stroke="#fff"/><text x="150" y="193" text-anchor="end" font-size="10" font-weight="bold">Day 1</text><circle cx="250" cy="138" r="6" fill="#DB2F30" stroke="#fff"/><text '
                      'x="240" y="156" text-anchor="end" font-size="10" font-weight="bold">Day 2</text><circle cx="330" cy="98" r="6" fill="#DB2F30" stroke="#fff"/><text x="320" y="116" '
                      'text-anchor="end" font-size="10" font-weight="bold">Day 3</text><circle cx="390" cy="66" r="6" fill="#DB2F30" stroke="#fff"/><text x="380" y="84" text-anchor="end" '
                      'font-size="10" font-weight="bold">Day 4</text><circle cx="440" cy="40" r="6" fill="#DB2F30" stroke="#fff"/><text x="430" y="58" text-anchor="end" font-size="10" '
                      'font-weight="bold">Day 5</text><text x="20" y="22" font-weight="bold" fill="#0A1F3D" font-size="15">A forecast cone is a model</text><text x="20" y="42" font-size="11">White '
                      'area: where the CENTER of the storm will probably go.</text><text x="20" y="58" font-size="11">It widens because forecasts are less certain further ahead.</text><text x="20" '
                      'y="74" font-size="11" fill="#DB2F30">It does NOT show the size of the storm. Wind, rain and</text><text x="20" y="90" font-size="11" fill="#DB2F30">flooding can reach far '
                      'outside the cone.</text></svg>',
            'html': '<p>Scientists use <b>models</b> when the real thing is too big (the solar system), too small (a cell), too slow (a mountain forming), too fast, too dangerous or too far away. '
                    'Models can be physical (a globe), drawings (a diagram of the water cycle), mathematical (a formula) or computer programs (weather forecasts).</p><p>Every model has '
                    "<b>limitations</b>. A globe shows Earth's shape but not its mountains' true height. The National Hurricane Center's forecast cone is a model built from the size of past forecast "
                    'errors. It shows the area where the center of a storm will probably travel, and the center stays inside the cone roughly two out of three times. It does <b>not</b> show how big '
                    'the storm is. People outside the cone can still get dangerous wind, rain and flooding.</p><p>Meteorologist Dr. J. Marshall Shepherd of the University of Georgia, who served as '
                    'president of the American Meteorological Society in 2013, has spent years helping the public understand forecasts like this, because a misread model can put lives at risk.</p>',
            'checks': [{'t': 'text',
                        'q': 'Why does the forecast cone get wider further into the future?',
                        'a': [{'all': [['uncertain',
                                        'less sure',
                                        'less certain',
                                        'harder to predict',
                                        'less accurate',
                                        'error',
                                        'not sure',
                                        'predict',
                                        'could change',
                                        'more possib',
                                        'more places',
                                        'guess']]}],
                        'show': 'Forecasts are less certain the further ahead they go.',
                        'pts': 2,
                        'why': 'Small errors grow over time, so the possible path widens.'},
                       {'t': 'text',
                        'q': 'Your town is 40 miles outside the cone. Can the hurricane still affect you? Type yes or no.',
                        'a': ['yes'],
                        'pts': 2,
                        'why': "Yes. The cone shows the likely path of the center only, not the storm's size. Wind, rain and storm surge often reach far outside it."},
                       {'t': 'open',
                        'key': 'model_limit',
                        'q': 'A globe is a model of Earth. Describe one thing the globe shows well and one limitation it has.',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Names a real strength (shape, relative positions, true sizes of continents)',
                                   'Names a real limitation (no true mountain heights, no weather, no detail, cannot show change)'],
                        'model': "A globe shows Earth's round shape and the true sizes and positions of the continents better than a flat map. One limitation is that it cannot show how tall "
                                 'mountains really are, and it does not show anything changing, like weather or cities.'}]}],
 'handson': {'title': 'Sun vs. Shade Temperature Investigation',
             'intro': 'Repeat the Okafor investigation in your own yard, balcony or windowsill, then graph your data.',
             'materials': ['Two thermometers that read the same (check them side by side first), or one thermometer moved between spots',
                           'A sunny spot and a shady spot',
                           'A timer or clock',
                           'Graph paper',
                           'Two colored pencils',
                           'A clock or timer'],
             'steps': ['Put both thermometers side by side indoors for 10 minutes. If they read differently, note the difference so you can correct for it.',
                       'Place one thermometer in full sun and one in the shade, both at the same height, off the ground and out of direct contact with metal or pavement.',
                       'Record both temperatures in °C every hour (or every 30 minutes) for at least four readings. If you use one thermometer, wait 5 minutes after moving it before reading.',
                       'Make a line graph with both lines on the same axes. Use TAILS.',
                       'Write what your graph shows, and compare it with the Okafor graph.',
                       'Write two testable questions you could investigate for your Week 5 project, such as: Does ground color change temperature?'],
             'record': [{'t': 'open',
                         'key': 'sundata',
                         'q': 'Type your data table with times and both temperatures, including units.',
                         'min': 20,
                         'rows': 6,
                         'rubric': ['At least four readings for each location', 'Times and °C units shown', 'Data looks reasonable'],
                         'model': 'Time | Sun (°C) | Shade (°C)\n9 AM | 27 | 25\n10 AM | 30 | 26\n11 AM | 33 | 27\n12 PM | 35 | 28'},
                        {'t': 'open',
                         'key': 'sunconclude',
                         'q': "Describe your graph: When was the difference greatest? How did your results compare with the Okafor family's? What would you change if you did it again?",
                         'min': 34,
                         'rows': 5,
                         'rubric': ['Identifies the time of greatest difference',
                                    'Compares with the Okafor data',
                                    'Names one way to improve the investigation (more trials, same height, same type of ground)'],
                         'model': 'The biggest difference was 7 °C at 12 PM. Like the Okafor data, the gap grew toward midday, but my readings were a little lower. Next time I would take readings '
                                  'until 4 PM and keep both thermometers over grass.'},
                        {'t': 'open',
                         'key': 'nextq',
                         'q': 'Write two testable questions you could investigate yourself for your Week 5 project. For one of them, name the independent and dependent variables.',
                         'min': 20,
                         'rows': 3,
                         'rubric': ['Two testable questions', 'Correct independent variable', 'Correct dependent variable'],
                         'model': '1. Does black or white paper get hotter in the sun? 2. Does the amount of water change how fast a bean seed sprouts? For question 1, the independent variable is '
                                  'paper color and the dependent variable is temperature in °C.'}]},
 'think': {'intro': 'Use evidence and explain your reasoning. Your teacher scores these.',
           'items': [{'t': 'open',
                      'key': 'claim',
                      'q': 'A website shows a graph with a y-axis from 98 to 100 and claims a new juice "skyrockets" energy. The bar for the juice drinkers is at 99.6 and the bar for water drinkers '
                           'is at 99.1. Write three questions a scientist would ask before believing the claim.',
                      'min': 35,
                      'rubric': ['Asks about the axis or scale',
                                 'Asks about the sample size or how the test was done (fair test, variables)',
                                 'Asks what was measured and in what units, or who paid for the study'],
                      'model': '1. Why does the y-axis start at 98 instead of 0, and what is the real difference? 2. How many people were tested, and was it a fair test with only the drink changed? '
                               '3. What exactly was measured, in what units, and who paid for the study?'},
                     {'t': 'open',
                      'key': 'designmodel',
                      'q': 'Design a model you could build at home to show why the shady spot stays cooler. Describe the materials, what each part represents, and one limitation of your model.',
                      'min': 40,
                      'rubric': ['Describes realistic materials', 'Explains what each part represents (lamp = sun, cardboard = tree)', 'Names a genuine limitation'],
                      'model': "I would use a desk lamp as the sun, two cups of water as the ground, and a piece of cardboard held above one cup as the tree's shade. After 20 minutes I would measure "
                               'both cups. A limitation is that a real tree also cools the air by releasing water from its leaves, which my cardboard cannot do.'}]},
 'exit': [{'t': 'text',
           'q': 'A family wants to show what fraction of its monthly budget goes to food, rent, gas and savings. Which graph fits best?',
           'a': [{'all': [['circle', 'pie']]}],
           'show': 'a circle graph',
           'pts': 2,
           'why': 'Parts of one whole (the budget) fit a circle graph.'},
          {'t': 'text', 'q': 'What does the T in TAILS stand for?', 'a': ['title', 'a title'], 'pts': 2, 'why': 'Every graph needs a title.'},
          {'t': 'num', 'q': 'Using the Okafor data, how much did the shade temperature rise from 8 AM to 2 PM?', 'a': 6, 'unit': '°C', 'pts': 2, 'why': '29 − 23 = 6 °C.'},
          {'t': 'num',
           'q': 'Using the Okafor data, how much did the sun temperature rise from 8 AM to 2 PM?',
           'a': 13,
           'unit': '°C',
           'pts': 2,
           'why': '37 − 24 = 13 °C, more than twice the rise in the shade.'},
          {'t': 'text',
           'q': 'A forecast cone does not show the size of a storm. What does it show?',
           'a': [{'all': [['center', 'centre', 'eye'], ['path', 'track', 'go', 'travel', 'move']]}],
           'show': "the probable path of the storm's center",
           'pts': 2,
           'why': 'The cone shows where the center of the storm will probably travel.'},
          {'t': 'open',
           'key': 'exit_axis',
           'q': 'What is the first thing you should check on any graph to see if it is misleading, and why?',
           'min': 10,
           'rows': 2,
           'rubric': ['Names the y-axis or scale', 'Explains that a scale not starting at zero can exaggerate differences'],
           'model': 'Check where the y-axis starts and whether the scale is even, because on a bar graph, starting above zero can make small differences look huge.'}],
 'next': 'Week 5: the Unit 1 checkpoint and your own investigation project.'}

TEACHER = {
 "standards": [
  "SC.6.N.1.1: Define a problem from the sixth grade curriculum, use appropriate reference materials to support scientific understanding, plan and carry out scientific investigation of various types, such as systematic observations or experiments, identify variables, collect and organize data, interpret data in charts, tables, and graphics, analyze information, make predictions, and defend conclusions.",
  "SC.6.N.3.4: Identify the role of models in the context of the sixth grade science benchmarks.",
  "SC.6.N.1.5: Recognize that science involves creativity, not just in designing experiments, but also in creating explanations that fit evidence.",
  "MA.6.DP.1 connection: displaying and interpreting numerical data.",
  "NGSS Science and Engineering Practices 2 and 4: developing and using models; analyzing and interpreting data."],
 "materials": ["The interactive lesson", "A thermometer", "Graph paper and two colored pencils", "A globe or map to discuss models", "A current or past NHC forecast graphic on screen (optional)", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 3 Reconnect questions."],
  [5, "Hook", "Show the Okafor table. Ask what story the numbers tell before showing the graph."],
  [12, "Line graphs", "Reveal the graph. Teach TAILS. Answer the reading questions together and make a 6 PM prediction."],
  [8, "Choosing graphs", "Sort four example questions into the four graph types. Ask the student to invent one question for each."],
  [9, "Misleading graphs", "Compare Graphs A and B. Have the student sketch an honest version of a misleading graph."],
  [12, "Models and the cone", "List models the student already uses (a globe, a map app, a recipe). Read the cone correctly. Stress that it does not show storm size."],
  [8, "Plan the investigation", "Plan the sun vs. shade investigation and the graph. Assign Think Deeper and the Exit Check."]],
 "key_questions": ["What question is this graph trying to answer?", "Where does the y-axis start? Is the scale even?", "What does this model show well, and what does it leave out?", "What would a person misunderstand if they misread this model?"],
 "misconceptions": ["Putting the dependent variable on the x-axis.", "Uneven intervals on an axis.", "Using a line graph for separate categories.", "Thinking the forecast cone shows the size of the storm, or that areas outside the cone are safe.", "Believing a model is a perfect copy of reality."],
 "support": ["Provide a pre-drawn graph frame with axes labeled.", "Use the TAILS checklist as a card.", "Limit the investigation to four readings."],
 "challenge": ["Calculate the average difference between sun and shade across all five Okafor readings (5 °C).", "Research how the size of the NHC cone has shrunk over the years as forecasts improved, and explain why."],
 "background": "<p>The NHC cone represents the probable track of the center of a tropical cyclone. Its size is set from historical official forecast errors over the previous five years, so the entire track of the center remains within the cone about 60 to 70 percent of the time. The cone does not depict storm size, and hazards frequently occur outside it. The rainfall numbers in the misleading-graph example are illustrative, not official climate data. Dr. J. Marshall Shepherd directs the Atmospheric Sciences Program at the University of Georgia and was the 2013 president of the American Meteorological Society.</p>",
 "sources": ["National Hurricane Center: Definition of the NHC Track Forecast Cone (nhc.noaa.gov/aboutcone.shtml).", "National Weather Service: hurricane safety and hazards outside the cone.", "University of Georgia Department of Geography: J. Marshall Shepherd faculty profile.", "American Meteorological Society: list of past presidents."]
}

PRINT = {
 "directions": "Use TAILS for every graph. Show your work.",
 "items": [
  {"q":"Name the best graph for each: (a) a puppy's mass each week for 10 weeks; (b) the favorite sport of 30 students as fractions of the class; (c) the number of birds seen at four feeders; (d) hours of practice and number of free throws made.","a":"(a) line; (b) circle; (c) bar; (d) scatter","lines":2},
  {"q":"On graph paper, graph this data as a line graph: Time (min) 0, 5, 10, 15, 20; Water temperature (°C) 80, 66, 55, 47, 42. Then describe the trend.","a":"Line graph with time on x-axis, temperature on y-axis; the water cools quickly at first, then more slowly.","lines":6},
  {"q":"What do the letters in TAILS stand for?","a":"Title, Axes labeled, Intervals even, Labels with units, Scale that fits","lines":2},
  {"q":"A bar graph's y-axis starts at 90. Bar A shows 92 and Bar B shows 96. Explain why this graph could be misleading.","a":"Starting at 90 makes B look three times taller than A, even though the real difference is only 4 out of about 94.","lines":2},
  {"q":"Explain what a hurricane forecast cone shows and what it does not show.","a":"It shows the probable path of the storm's center, getting wider with uncertainty. It does not show the storm's size or where wind, rain and flooding will reach.","lines":3},
  {"q":"Name a model you use in everyday life, what it represents, and one limitation.","a":"For example: a map app represents roads and places but does not show every pothole or live traffic perfectly.","lines":2}]
}
