CER = ('<svg viewBox="0 0 560 190" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Claim, evidence, reasoning">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Claim, Evidence, Reasoning: how scientists explain results</text>'
  '<rect x="20" y="36" width="160" height="120" rx="10" fill="#0A1F3D"/><text x="100" y="66" text-anchor="middle" fill="#fff" font-weight="bold" font-size="16">CLAIM</text>'
  '<text x="100" y="92" text-anchor="middle" fill="#fff">What did you find?</text><text x="100" y="110" text-anchor="middle" fill="#fff">One sentence that</text><text x="100" y="126" text-anchor="middle" fill="#fff">answers the question.</text>'
  '<rect x="200" y="36" width="160" height="120" rx="10" fill="#0047BA"/><text x="280" y="66" text-anchor="middle" fill="#fff" font-weight="bold" font-size="16">EVIDENCE</text>'
  '<text x="280" y="92" text-anchor="middle" fill="#fff">Your data: numbers,</text><text x="280" y="110" text-anchor="middle" fill="#fff">averages and patterns</text><text x="280" y="126" text-anchor="middle" fill="#fff">with units.</text>'
  '<rect x="380" y="36" width="160" height="120" rx="10" fill="#C9A84C"/><text x="460" y="66" text-anchor="middle" fill="#0A1F3D" font-weight="bold" font-size="16">REASONING</text>'
  '<text x="460" y="92" text-anchor="middle" fill="#0A1F3D">Why does the evidence</text><text x="460" y="110" text-anchor="middle" fill="#0A1F3D">support the claim?</text><text x="460" y="126" text-anchor="middle" fill="#0A1F3D">Use science ideas.</text>'
  '<path d="M180 96 h20 M360 96 h20" stroke="#DB2F30" stroke-width="3"/>'
  '<text x="280" y="180" text-anchor="middle" font-size="12">Then: what were the limits of your test, and what would you test next?</text></svg>')

def bars():
    data = [("Black", 41.2), ("Blue", 37.6), ("Red", 36.1), ("White", 31.4)]
    s = ('<svg viewBox="0 0 560 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Bar graph of temperature under colored paper">'
         '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Average temperature after 30 minutes in the sun (3 trials)</text>')
    x0, y0, h = 70, 196, 150
    for v in range(0, 51, 10):
        y = y0 - v / 50 * h
        s += f'<line x1="{x0}" y1="{y}" x2="530" y2="{y}" stroke="#e1e6ee"/><text x="{x0-8}" y="{y+4}" text-anchor="end">{v}</text>'
    for i, (c, v) in enumerate(data):
        bh = v / 50 * h; col = {"Black": "#222", "Blue": "#0047BA", "Red": "#DB2F30", "White": "#fff"}[c]
        s += f'<rect x="{x0+30+i*110}" y="{y0-bh}" width="60" height="{bh}" fill="{col}" stroke="#0A1F3D"/><text x="{x0+60+i*110}" y="{y0-bh-6}" text-anchor="middle" font-weight="bold">{v}</text><text x="{x0+60+i*110}" y="{y0+16}" text-anchor="middle">{c}</text>'
    s += f'<line x1="{x0}" y1="{y0}" x2="530" y2="{y0}" stroke="#0A1F3D"/><line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0-h}" stroke="#0A1F3D"/>'
    s += f'<text x="22" y="{y0-h/2}" transform="rotate(-90 22 {y0-h/2})" text-anchor="middle">Temperature (°C)</text></svg>'
    return s

STEPS = ('<svg viewBox="0 0 560 120" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Investigation project steps">'
  + ''.join(f'<rect x="{6+i*92}" y="20" width="84" height="70" rx="8" fill="{c}"/><text x="{48+i*92}" y="46" text-anchor="middle" fill="#fff" font-weight="bold" font-size="16">{i+1}</text><text x="{48+i*92}" y="66" text-anchor="middle" fill="#fff">{a}</text><text x="{48+i*92}" y="80" text-anchor="middle" fill="#fff">{b}</text>'
            for i, (a, b, c) in enumerate([("Question", "", "#0A1F3D"), ("Hypothesis", "and variables", "#0047BA"), ("Procedure", "and materials", "#0A1F3D"), ("Data", "3 trials", "#0047BA"), ("Graph", "TAILS", "#C9A84C"), ("Conclusion", "CER", "#DB2F30")])) +
  '<text x="280" y="110" text-anchor="middle" font-size="12" fill="#0A1F3D">Every step uses a skill from Weeks 1 to 4.</text></svg>')

LESSON = {'unit': 'Unit 1: Thinking Like a Scientist',
 'title': 'Unit 1 Checkpoint and Investigation Project',
 'subtitle': 'Now you are the scientist. Ask your own question, test it fairly, and explain what you found.',
 'objectives': ['Plan and carry out your own fair-test investigation with three trials.',
                'Record data in a table with units and display it in the correct type of graph.',
                'Write a conclusion using Claim, Evidence and Reasoning (CER).',
                "Explain the limits of an investigation and why scientists repeat each other's work.",
                'Show mastery of Unit 1 on the checkpoint (85 or higher).'],
 'vocab': [['claim', 'A statement that answers the investigation question.'],
           ['evidence', 'Data that supports a claim.'],
           ['reasoning', 'The explanation of why the evidence supports the claim, using science ideas.'],
           ['conclusion', 'The final section of an investigation that states and explains what was found.'],
           ['replicate', "To repeat another scientist's investigation to see if you get the same results."],
           ['peer review', 'When other scientists check a study before it is published.'],
           ['procedure', 'The step-by-step plan for an investigation, written so someone else could repeat it.']],
 'reconnect': {'title': "Weeks 1 to 4: the whole scientist's toolkit",
               'intro': 'Your project uses every skill from this unit. Make sure each one is ready.',
               'items': [{'t': 'open',
                          'key': 'rc_inf',
                          'q': '"The paper towel feels wet" is an observation. Is "It must have rained last night" an observation or an inference? Explain how you know.',
                          'min': 12,
                          'rows': 2,
                          'rubric': ['Inference', 'It explains or guesses a cause instead of using only the senses'],
                          'model': 'It is an inference, because it is a possible explanation for the wet towel, not something I observed with my senses.'},
                         {'t': 'blanks',
                          'q': 'In a test of whether paper color changes temperature in the sun, name each variable.',
                          'sent': 'Independent variable: ___   Dependent variable: ___',
                          'blanks': [[{'all': [['color', 'colour']]}], [{'all': [['temperature', 'temp', 'heat', 'degrees', 'hot']]}]],
                          'show': 'paper color; temperature',
                          'pts': 3,
                          'why': 'You change the color (independent) and measure the temperature (dependent).'},
                         {'t': 'num', 'q': 'Convert 350 milliliters to liters.', 'a': 0.35, 'unit': 'L', 'pts': 2, 'why': '350 ÷ 1,000 = 0.35 L.'},
                         {'t': 'num', 'q': 'Three trials measured 18 °C, 21 °C and 21 °C. What is the average?', 'a': 20, 'unit': '°C', 'pts': 2, 'why': '(18 + 21 + 21) ÷ 3 = 60 ÷ 3 = 20 °C.'},
                         {'t': 'text',
                          'q': 'You compare the temperature under four different colors of paper. Which kind of graph fits best?',
                          'a': [{'all': [['bar']]}],
                          'show': 'a bar graph',
                          'pts': 2,
                          'why': 'Separate categories (colors) fit a bar graph.'},
                         {'t': 'open',
                          'key': 'rc_model',
                          'q': 'Name one model you studied in Week 4, one thing it shows well and one limitation.',
                          'min': 15,
                          'rows': 2,
                          'rubric': ['Names a model (forecast cone, globe, map)', 'A real strength', 'A real limitation'],
                          'model': "The hurricane forecast cone shows where the storm's center will probably go, but it does not show how big the storm is or where the rain will fall."}]},
 'hook': {'title': 'Does Color Change the Heat?',
          'visual': '<svg viewBox="0 0 560 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Bar graph of temperature under colored paper"><text '
                    'x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Average temperature after 30 minutes in the sun (3 trials)</text><line x1="70" y1="196.0" '
                    'x2="530" y2="196.0" stroke="#e1e6ee"/><text x="62" y="200.0" text-anchor="end">0</text><line x1="70" y1="166.0" x2="530" y2="166.0" stroke="#e1e6ee"/><text x="62" y="170.0" '
                    'text-anchor="end">10</text><line x1="70" y1="136.0" x2="530" y2="136.0" stroke="#e1e6ee"/><text x="62" y="140.0" text-anchor="end">20</text><line x1="70" y1="106.0" x2="530" '
                    'y2="106.0" stroke="#e1e6ee"/><text x="62" y="110.0" text-anchor="end">30</text><line x1="70" y1="76.0" x2="530" y2="76.0" stroke="#e1e6ee"/><text x="62" y="80.0" '
                    'text-anchor="end">40</text><line x1="70" y1="46.0" x2="530" y2="46.0" stroke="#e1e6ee"/><text x="62" y="50.0" text-anchor="end">50</text><rect x="100" y="72.39999999999999" '
                    'width="60" height="123.60000000000001" fill="#222" stroke="#0A1F3D"/><text x="130" y="66.39999999999999" text-anchor="middle" font-weight="bold">41.2</text><text x="130" y="212" '
                    'text-anchor="middle">Black</text><rect x="210" y="83.2" width="60" height="112.8" fill="#0047BA" stroke="#0A1F3D"/><text x="240" y="77.2" text-anchor="middle" '
                    'font-weight="bold">37.6</text><text x="240" y="212" text-anchor="middle">Blue</text><rect x="320" y="87.7" width="60" height="108.3" fill="#DB2F30" stroke="#0A1F3D"/><text '
                    'x="350" y="81.7" text-anchor="middle" font-weight="bold">36.1</text><text x="350" y="212" text-anchor="middle">Red</text><rect x="430" y="101.8" width="60" height="94.2" '
                    'fill="#fff" stroke="#0A1F3D"/><text x="460" y="95.8" text-anchor="middle" font-weight="bold">31.4</text><text x="460" y="212" text-anchor="middle">White</text><line x1="70" '
                    'y1="196" x2="530" y2="196" stroke="#0A1F3D"/><line x1="70" y1="196" x2="70" y2="46" stroke="#0A1F3D"/><text x="22" y="121.0" transform="rotate(-90 22 121.0)" '
                    'text-anchor="middle">Temperature (°C)</text></svg>',
          'html': "<p>Jaylen, from the Week 2 paper towel test, has a new question: why does his black car seat burn his legs while his sister's tan seat doesn't? He laid four sheets of colored "
                  'construction paper in the sun, put a thermometer under each, and recorded the temperature after 30 minutes. He repeated the test on three sunny days and averaged the '
                  'results.</p><p>His graph tells a clear story. But a graph alone is not a conclusion. This week you learn how scientists turn data into an explanation, and then you run your own '
                  "investigation from start to finish.</p><div class='callout'><b>Big idea:</b> A conclusion makes a claim, backs it with evidence, explains it with reasoning, and admits its "
                  'limits.</div>'},
 'learn': [{'title': 'Writing a Conclusion With CER',
            'visual': '<svg viewBox="0 0 560 190" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Claim, evidence, reasoning"><text x="280" y="18" '
                      'text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Claim, Evidence, Reasoning: how scientists explain results</text><rect x="20" y="36" width="160" '
                      'height="120" rx="10" fill="#0A1F3D"/><text x="100" y="66" text-anchor="middle" fill="#fff" font-weight="bold" font-size="16">CLAIM</text><text x="100" y="92" '
                      'text-anchor="middle" fill="#fff">What did you find?</text><text x="100" y="110" text-anchor="middle" fill="#fff">One sentence that</text><text x="100" y="126" '
                      'text-anchor="middle" fill="#fff">answers the question.</text><rect x="200" y="36" width="160" height="120" rx="10" fill="#0047BA"/><text x="280" y="66" text-anchor="middle" '
                      'fill="#fff" font-weight="bold" font-size="16">EVIDENCE</text><text x="280" y="92" text-anchor="middle" fill="#fff">Your data: numbers,</text><text x="280" y="110" '
                      'text-anchor="middle" fill="#fff">averages and patterns</text><text x="280" y="126" text-anchor="middle" fill="#fff">with units.</text><rect x="380" y="36" width="160" '
                      'height="120" rx="10" fill="#C9A84C"/><text x="460" y="66" text-anchor="middle" fill="#0A1F3D" font-weight="bold" font-size="16">REASONING</text><text x="460" y="92" '
                      'text-anchor="middle" fill="#0A1F3D">Why does the evidence</text><text x="460" y="110" text-anchor="middle" fill="#0A1F3D">support the claim?</text><text x="460" y="126" '
                      'text-anchor="middle" fill="#0A1F3D">Use science ideas.</text><path d="M180 96 h20 M360 96 h20" stroke="#DB2F30" stroke-width="3"/><text x="280" y="180" text-anchor="middle" '
                      'font-size="12">Then: what were the limits of your test, and what would you test next?</text></svg>',
            'html': "<div class='example'><b>Claim:</b> Darker paper colors get hotter in the sun than lighter colors.<br><b>Evidence:</b> After 30 minutes, the average temperature under black paper "
                    'was 41.2 °C, compared with 31.4 °C under white paper, a difference of 9.8 °C. Blue (37.6 °C) and red (36.1 °C) were in between.<br><b>Reasoning:</b> Dark colors absorb more of '
                    "the sunlight's energy, while light colors reflect more of it. The absorbed energy turns into heat, so the space under dark paper warms up more.</div>",
            'checks': [{'t': 'num', 'q': "Using Jaylen's averages, how many degrees warmer was the black paper than the red paper?", 'a': 5.1, 'unit': '°C', 'pts': 2, 'why': '41.2 − 36.1 = 5.1 °C.'},
                       {'t': 'open',
                        'key': 'labelcer',
                        'q': 'Label the claim, evidence and reasoning in this paragraph: <i>Ice melts faster in a black cup. In my test it melted in 18 minutes in the black cup and 27 minutes in the '
                             "white cup. Dark colors absorb more of the sun's energy, which warms the ice.</i>",
                        'min': 12,
                        'rows': 3,
                        'rubric': ['Claim: first sentence', 'Evidence: the times with units', 'Reasoning: dark colors absorb more energy'],
                        'model': "Claim: Ice melts faster in a black cup. Evidence: 18 minutes in the black cup versus 27 minutes in the white cup. Reasoning: dark colors absorb more of the sun's "
                                 'energy, which warms the ice.'},
                       {'t': 'open',
                        'key': 'weakcer',
                        'q': 'A student writes: "My hypothesis was right. Black was hotter." Explain two things missing from this conclusion, then rewrite it as a stronger claim with evidence.',
                        'min': 30,
                        'rows': 4,
                        'rubric': ['Missing specific data with units', 'Missing reasoning (why)', 'Rewrite includes numbers and units'],
                        'model': 'It has no data and no reasoning. A stronger version: Black paper got hotter than white paper. After 30 minutes, the space under black paper averaged 41.2 °C and '
                                 "under white paper 31.4 °C, almost 10 degrees warmer, because dark colors absorb more of the sun's energy."}]},
           {'title': 'Limits, Errors and Replication',
            'html': '<p>Every investigation has limits. Jaylen tested on only three days, used one brand of paper, and placed the papers in one spot. A good conclusion names these limits honestly '
                    "and suggests what to test next.</p><p>Scientists also <b>replicate</b> each other's work. If many scientists in different places get the same results, everyone can trust the "
                    'finding more. Before a study is published in a science journal, other experts check it in a process called <b>peer review</b>.</p><p>Dr. Katherine Johnson, the NASA '
                    "mathematician whose calculations helped send John Glenn into orbit in 1962, was asked by Glenn himself to check the electronic computer's numbers by hand before his flight. "
                    'Checking and repeating work is how science catches mistakes. It is also why scientific knowledge is durable but open to change: ideas that survive many checks are trusted, and '
                    'new evidence can still improve them.</p>',
            'checks': [{'t': 'open',
                        'key': 'limits',
                        'q': "Name two limits of Jaylen's investigation and explain how each could change his results.",
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Two real limits (few trials, one location, cloud cover, thermometer differences, paper material)', 'Explains how each could affect results'],
                        'model': 'He only tested three days, so one cloudy afternoon could change an average a lot. He also used one kind of paper, so a thicker paper might trap heat differently.'},
                       {'t': 'text',
                        'q': "What is the word for repeating another scientist's investigation to see if you get the same results?",
                        'a': ['replicate', 'replication', 'replicating'],
                        'show': 'replicate',
                        'pts': 2,
                        'why': 'Replication builds trust in results.'},
                       {'t': 'open',
                        'key': 'whycheck',
                        'q': "Why did John Glenn want Katherine Johnson to check the computer's calculations by hand? What does this tell you about how science works?",
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Computers were new and could be wrong; a human expert confirmed the numbers', 'Science depends on checking and repeating work'],
                        'model': 'Electronic computers were new and he did not fully trust them, so he wanted an expert he trusted to confirm the numbers. It shows that science depends on checking '
                                 'work more than once before trusting it, especially when lives are at stake.'}]},
           {'title': 'Planning Your Investigation Project',
            'visual': '<svg viewBox="0 0 560 120" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Investigation project steps"><rect x="6" y="20" '
                      'width="84" height="70" rx="8" fill="#0A1F3D"/><text x="48" y="46" text-anchor="middle" fill="#fff" font-weight="bold" font-size="16">1</text><text x="48" y="66" '
                      'text-anchor="middle" fill="#fff">Question</text><text x="48" y="80" text-anchor="middle" fill="#fff"></text><rect x="98" y="20" width="84" height="70" rx="8" '
                      'fill="#1d3b66"/><text x="140" y="46" text-anchor="middle" fill="#fff" font-weight="bold" font-size="16">2</text><text x="140" y="66" text-anchor="middle" '
                      'fill="#fff">Hypothesis</text><text x="140" y="80" text-anchor="middle" fill="#fff">and variables</text><rect x="190" y="20" width="84" height="70" rx="8" fill="#0047BA"/><text '
                      'x="232" y="46" text-anchor="middle" fill="#fff" font-weight="bold" font-size="16">3</text><text x="232" y="66" text-anchor="middle" fill="#fff">Procedure</text><text x="232" '
                      'y="80" text-anchor="middle" fill="#fff">and materials</text><rect x="282" y="20" width="84" height="70" rx="8" fill="#2f5a91"/><text x="324" y="46" text-anchor="middle" '
                      'fill="#fff" font-weight="bold" font-size="16">4</text><text x="324" y="66" text-anchor="middle" fill="#fff">Data</text><text x="324" y="80" text-anchor="middle" fill="#fff">3 '
                      'trials</text><rect x="374" y="20" width="84" height="70" rx="8" fill="#C9A84C"/><text x="416" y="46" text-anchor="middle" fill="#fff" font-weight="bold" '
                      'font-size="16">5</text><text x="416" y="66" text-anchor="middle" fill="#fff">Graph</text><text x="416" y="80" text-anchor="middle" fill="#fff">TAILS</text><rect x="466" y="20" '
                      'width="84" height="70" rx="8" fill="#DB2F30"/><text x="508" y="46" text-anchor="middle" fill="#fff" font-weight="bold" font-size="16">6</text><text x="508" y="66" '
                      'text-anchor="middle" fill="#fff">Conclusion</text><text x="508" y="80" text-anchor="middle" fill="#fff">CER</text><text x="280" y="110" text-anchor="middle" font-size="12" '
                      'fill="#0A1F3D">Every step uses a skill from Weeks 1 to 4.</text></svg>',
            'html': '<p>Your project question should be <b>testable at home</b>, <b>safe</b>, and <b>finished in a few days</b>. It must change only one independent variable and measure one '
                    "dependent variable, with three trials.</p><table class='t'><tr><th>Strong project questions</th><th>Why they work</th></tr><tr><td>Does water temperature change how fast sugar "
                    'dissolves?</td><td>Easy to measure time in seconds</td></tr><tr><td>Does the height of a ramp change how far a toy car rolls?</td><td>Measure distance in '
                    'centimeters</td></tr><tr><td>Does the color of a cup change how fast an ice cube melts?</td><td>Measure time in minutes</td></tr><tr><td>Does paper color change temperature in '
                    'the sun?</td><td>Measure °C with a thermometer</td></tr></table><p>The full project directions and rubric are on the Unit 1 Projects page.</p>',
            'checks': [{'t': 'open',
                        'key': 'testable',
                        'q': 'Explain why "Which color is the prettiest?" is NOT a testable science question, then rewrite it so it is testable.',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Pretty is an opinion, cannot be measured', 'Rewrite has a measurable dependent variable'],
                        'model': 'Prettiest is an opinion, so there is nothing to measure. A testable version: Does the color of a cup change how fast an ice cube melts inside it?'},
                       {'t': 'open',
                        'key': 'plan',
                        'q': 'Write your project question, hypothesis (If... then... because...), independent variable, dependent variable and three controlled variables.',
                        'min': 40,
                        'rows': 5,
                        'rubric': ['Testable question', 'Hypothesis in If-then-because form', 'Correct independent and dependent variables', 'Three relevant controlled variables'],
                        'model': 'Question: Does the height of a ramp change how far a toy car rolls? Hypothesis: If I raise the ramp, then the car will roll farther, because it gains more speed on '
                                 'the way down. IV: ramp height (cm). DV: distance rolled (cm). Controlled: the same car, the same floor, releasing without pushing.'}]}],
 'handson': {'title': 'Run Your Investigation',
             'intro': 'Carry out the plan you wrote in Learn 3. Your teacher will score the project with the rubric on the Unit 1 Projects page.',
             'materials': ['The materials your procedure needs (gather them before you start)',
                           'A ruler, scale, thermometer, measuring cup or timer, depending on your test',
                           'Graph paper and colored pencils',
                           'A notebook for your data table',
                           "A parent's permission for anything that uses heat, sharp tools or the outdoors"],
             'steps': ['Write your numbered procedure so someone else could repeat it exactly.',
                       'Make your data table with units in every heading and room for three trials and an average.',
                       'Run the investigation three times. Record every number immediately, even surprising ones.',
                       'Calculate the averages and make the correct graph using TAILS.',
                       'Write your conclusion with CER, the limits of your test and one question to test next.',
                       'Take a photo of your setup for your project.'],
             'record': [{'t': 'open',
                         'key': 'procedure',
                         'q': 'Type your numbered procedure and your data table, including all three trials and the averages.',
                         'min': 60,
                         'rows': 10,
                         'rubric': ['Numbered, repeatable procedure', 'Table with units in headings', 'Three trials for each condition', 'Correct averages'],
                         'model': '1. Lean a board on books 10 cm high. 2. Release the toy car from the top without pushing. 3. Measure from the bottom of the ramp to the front of the car. 4. Repeat '
                                  '3 times. 5. Repeat at 20 cm and 30 cm.\n'
                                  'Ramp height (cm) | Trial 1 (cm) | Trial 2 (cm) | Trial 3 (cm) | Average (cm)\n'
                                  '10 | 92 | 88 | 95 | 91.7\n'
                                  '20 | 151 | 147 | 156 | 151.3\n'
                                  '30 | 203 | 210 | 199 | 204'},
                        {'t': 'open',
                         'key': 'projcer',
                         'q': 'Write your conclusion using CER. Then name two limits of your investigation and one question you would test next.',
                         'min': 73,
                         'rows': 8,
                         'rubric': ['Clear claim that answers the question', 'Evidence with specific averages and units', 'Reasoning with a science idea', 'Two limits', 'A next question'],
                         'model': 'Claim: Raising the ramp made the toy car roll farther. Evidence: At 10 cm the car rolled an average of 91.7 cm, at 20 cm 151.3 cm, and at 30 cm 204 cm. Reasoning: '
                                  'A higher ramp gives the car more height to fall, so it reaches the bottom moving faster and keeps going longer before friction stops it. Limits: I used only one '
                                  'car, and my measuring tape may have slipped on the carpet. Next, I would test whether the floor surface changes the distance.'}]},
 'think': {'intro': 'Explain your reasoning. Your teacher scores this.',
           'items': [{'t': 'open',
                      'key': 'designcrit',
                      'q': 'A website claims, "Our study proves plants grow faster with music." The study used one plant with music and one without, for three days. Use what you learned this unit to '
                           'explain three problems with this study and how to fix each one.',
                      'min': 60,
                      'rubric': ['Sample too small: one plant each',
                                 'Too short or only one trial: needs repeats',
                                 'Other variables not controlled or not stated (light, water, pot)',
                                 'A fix for each problem'],
                      'model': 'First, one plant in each group is far too few, because one plant might just be healthier; use at least ten in each group. Second, three days is too short to see real '
                               'growth; run it for several weeks and repeat the whole test. Third, they do not say whether light, water, soil and pot size were kept the same; control every variable '
                               'except the music. With these fixes, other scientists could replicate it.'}]},
 'checkpoint': {'title': 'Unit 1 Checkpoint: Thinking Like a Scientist',
                'intro': 'This checkpoint covers Weeks 1 to 5. Mastery is 85 or higher. If you score below 85, your teacher will review with you, then you will retake it.',
                'parts': [{'title': 'Part A: Observations, questions and fair tests',
                           'items': [{'t': 'open',
                                      'key': 'cp_obsinf',
                                      'q': 'You find a puddle under the kitchen sink. Write one observation and one inference about it.',
                                      'min': 15,
                                      'rows': 2,
                                      'rubric': ['Observation uses the senses only', 'Inference is a possible explanation'],
                                      'model': 'Observation: there is a puddle of clear water about 20 cm wide under the sink. Inference: the pipe under the sink might be leaking.'},
                                     {'t': 'blanks',
                                      'q': 'A student tests whether the amount of fertilizer changes how tall bean plants grow. Name each variable.',
                                      'sent': 'Independent: ___   Dependent: ___',
                                      'blanks': [[{'all': [['fertilizer', 'fertiliser']]}], [{'all': [['height', 'tall', 'grow', 'growth', 'cm']]}]],
                                      'show': 'amount of fertilizer; plant height',
                                      'pts': 3,
                                      'why': 'You change the fertilizer and measure the height.'},
                                     {'t': 'text',
                                      'q': 'In that test, what do we call the group of plants that gets no fertilizer?',
                                      'a': ['control group', 'the control group', 'control'],
                                      'show': 'the control group',
                                      'pts': 2,
                                      'why': 'The control group gets no change and is used for comparison.'}]},
                          {'title': 'Part B: Measurement',
                           'items': [{'t': 'num', 'q': 'Convert 4.2 kilograms to grams.', 'a': 4200, 'unit': 'g', 'pts': 2, 'why': '4.2 × 1,000 = 4,200 g.'},
                                     {'t': 'num', 'q': 'Convert 85 millimeters to centimeters.', 'a': 8.5, 'unit': 'cm', 'pts': 2, 'why': '85 ÷ 10 = 8.5 cm.'},
                                     {'t': 'open',
                                      'key': 'cp_accprec',
                                      'q': 'An oven thermometer reads 190 °C, 191 °C and 190 °C, but the oven is really at 175 °C. Is it accurate, precise, both or neither? Explain.',
                                      'min': 15,
                                      'rows': 2,
                                      'rubric': ['Precise but not accurate', 'Readings close together, but far from the true value'],
                                      'model': 'It is precise but not accurate, because the readings are almost the same each time but all about 15 degrees too high.'}]},
                          {'title': 'Part C: Graphs and models',
                           'items': [{'t': 'text',
                                      'q': "Which kind of graph best shows how a puppy's mass changed each week for 10 weeks?",
                                      'a': [{'all': [['line']]}],
                                      'show': 'a line graph',
                                      'pts': 2,
                                      'why': 'Change over time fits a line graph.'},
                                     {'t': 'num',
                                      'q': "In Jaylen's graph, how many degrees warmer was the blue paper than the white paper?",
                                      'a': 6.2,
                                      'unit': '°C',
                                      'pts': 3,
                                      'why': '37.6 − 31.4 = 6.2 °C.'},
                                     {'t': 'open',
                                      'key': 'cp_mislead',
                                      'q': 'A bar graph of the same data starts its y-axis at 30 °C. Explain how this would mislead a reader.',
                                      'min': 15,
                                      'rows': 2,
                                      'rubric': ['Bars would look many times different', 'Because the axis does not start at 0, bar length no longer matches the amount'],
                                      'model': 'The white bar would look tiny and the black bar huge, about eight times taller, even though 41.2 is only about 1.3 times 31.4. A bar graph should '
                                               "start at 0 because the bar's length shows the amount."},
                                     {'t': 'open',
                                      'key': 'cp_cone',
                                      'q': 'Your cousin lives just outside the hurricane forecast cone and says, "We\'re safe, we\'re not in the cone." What do you tell her, and why?',
                                      'min': 15,
                                      'rows': 2,
                                      'rubric': ['Not necessarily safe', "The cone shows only the probable path of the center, not the storm's size"],
                                      'model': 'She is not necessarily safe. The cone shows only where the center will probably go, not how big the storm is, so wind, rain and flooding can reach '
                                               'places outside the cone.'}]},
                          {'title': 'Part D: Conclusions',
                           'items': [{'t': 'open',
                                      'key': 'cp_evid',
                                      'q': 'A student\'s conclusion says, "My plant grew best in sunlight because plants need light." What part of CER is missing, and what should the student add?',
                                      'min': 12,
                                      'rows': 2,
                                      'pts': 3,
                                      'rubric': ['Evidence is missing', 'Should add measured data with units (heights in cm for each group)'],
                                      'model': 'The evidence is missing. The student should add the measured heights, for example: in sunlight the plants averaged 14 cm, in shade 6 cm.'},
                                     {'t': 'open',
                                      'key': 'cp_cer',
                                      'q': 'Data: sugar dissolved in 98 seconds in 10 °C water, 60 seconds in 25 °C water and 31 seconds in 50 °C water. Write a claim and evidence for the question '
                                           '"Does water temperature change how fast sugar dissolves?"',
                                      'min': 25,
                                      'rows': 3,
                                      'rubric': ['Claim: warmer water dissolves sugar faster', 'Evidence uses at least two data points with units'],
                                      'model': 'Claim: Sugar dissolves faster in warmer water. Evidence: In 10 °C water it took 98 seconds, but in 50 °C water it took only 31 seconds, about three '
                                               'times faster.'}]}]},
 'next': 'Unit 2: Cells, the Building Blocks of Life. You will look through a microscope at the tiny units that make up every living thing.'}

TEACHER = {
 "standards": [
  "SC.6.N.1.1: Define a problem from the sixth grade curriculum, use appropriate reference materials to support scientific understanding, plan and carry out scientific investigation of various types, such as systematic observations or experiments, identify variables, collect and organize data, interpret data in charts, tables, and graphics, analyze information, make predictions, and defend conclusions.",
  "SC.6.N.1.2: Explain why scientific investigations should be replicable.",
  "SC.6.N.1.4: Discuss, compare, and negotiate methods used, results obtained, and explanations among groups of students conducting the same investigation (for a homeschool student: compare with a parent or a KCE classmate).",
  "SC.6.N.2.2: Explain that scientific knowledge is durable because it is open to change as new evidence or interpretations are encountered.",
  "NGSS Science and Engineering Practices 3, 4 and 7: planning investigations; analyzing data; engaging in argument from evidence."],
 "materials": ["The interactive lesson", "The student's two testable questions from Week 4", "Graph paper and colored pencils", "The Unit 1 Projects page with the investigation rubric", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Reconnect questions."],
  [5, "Hook", "Show Jaylen's bar graph. Ask the student to state what it shows in one sentence."],
  [12, "CER", "Write Jaylen's conclusion together. Then improve the weak conclusion."],
  [10, "Limits and replication", "Discuss limits and peer review. Tell the Katherine Johnson story."],
  [17, "Plan the project", "Choose the project question together. Write the hypothesis, variables and procedure. Check safety and materials."],
  [5, "Due dates", "Set due dates for the investigation, the project write-up and the checkpoint (all after class)."],
  [5, "Close", "Review the investigation rubric."]],
 "key_questions": ["Can this question be answered by measuring something?", "What is the one thing you will change?", "What does your evidence actually show?", "What could have affected your results?"],
 "misconceptions": ["Thinking an experiment proves a hypothesis right or wrong forever.", "Writing a claim with no numbers.", "Changing more than one variable at a time.", "Believing a surprising result is a mistake and leaving it out."],
 "support": ["Choose one of the four strong project questions.", "Provide a data table template.", "Give sentence starters for CER: I claim that... My data shows... This happens because..."],
 "challenge": ["Test four or more levels of the independent variable.", "Compare your results with a classmate's or online data and explain any differences."],
 "background": "<p>Jaylen's data are illustrative. Katherine Johnson (1918 to 2020) checked the electronic computer's orbital calculations before John Glenn's Friendship 7 flight on February 20, 1962, at Glenn's request; she received the Presidential Medal of Freedom in 2015. The Investigation Project is scored with the five-trait rubric on the Unit 1 Projects page (20 points; multiply by 5 for a score out of 100; mastery 85).</p>",
 "sources": ["NASA: Katherine Johnson biography.", "CPALMS: SC.6.N.1.1, SC.6.N.1.2, SC.6.N.2.2.", "NGSS Appendix F: Science and Engineering Practices."]
}

PRINT = {
 "directions": "Use complete sentences and units.",
 "items": [
  {"q":"What do the letters C, E and R stand for in a conclusion? Describe each in a few words.","a":"Claim (answers the question), Evidence (data with units), Reasoning (science explanation).","lines":3},
  {"q":"Write a testable question about something in your kitchen. Name the independent and dependent variables.","a":"For example: Does water temperature change how fast salt dissolves? IV: water temperature; DV: time to dissolve (s).","lines":3},
  {"q":"Why should a scientist run three trials instead of one?","a":"One trial might be off because of an error or chance; averaging three gives more reliable results.","lines":2},
  {"q":"Explain what replication is and why it matters.","a":"Repeating another scientist's investigation; if others get the same results, the finding is more trustworthy.","lines":2},
  {"q":"Draw a data table for your own investigation with units in every heading and room for three trials and an average.","a":"For example: Water temperature (°C) | Trial 1 (s) | Trial 2 (s) | Trial 3 (s) | Average (s).","lines":4},
  {"q":"Name one limit of an investigation you have done this unit.","a":"For example: few trials, only one location, a thermometer that may read differently.","lines":2}]
}
