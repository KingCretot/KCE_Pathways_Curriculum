def strips():
    s = ('<svg viewBox="0 0 560 200" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="How many 3/4-cup servings are in 3 cups">'
         '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">3 ÷ 3/4: how many 3/4-cup servings fit in 3 cups?</text>')
    x0, w = 40, 480
    for c in range(3):
        s += f'<rect x="{x0+c*w/3}" y="40" width="{w/3}" height="40" fill="#fff" stroke="#0A1F3D" stroke-width="2"/><text x="{x0+c*w/3+w/6}" y="65" text-anchor="middle">1 cup</text>'
    for q in range(13):
        s += f'<line x1="{x0+q*w/12}" y1="80" x2="{x0+q*w/12}" y2="90" stroke="#0A1F3D"/>'
    cols = ["#0047BA", "#C9A84C", "#DB2F30", "#0A1F3D"]
    for g in range(4):
        s += f'<rect x="{x0+g*w/4}" y="100" width="{w/4}" height="40" fill="{cols[g]}" stroke="#fff" stroke-width="2"/><text x="{x0+g*w/4+w/8}" y="125" text-anchor="middle" fill="#fff" font-weight="bold">serving {g+1}: 3/4</text>'
    s += '<text x="280" y="170" text-anchor="middle">Four 3/4-cup servings fill 3 cups exactly, so 3 ÷ 3/4 = 4.</text>'
    s += '<text x="280" y="190" text-anchor="middle" fill="#0047BA">Same as 3 × 4/3 = 12/3 = 4. Dividing by a fraction = multiplying by its reciprocal.</text></svg>'
    return s

KCF = ('<svg viewBox="0 0 560 140" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Keep, change, flip">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Dividing fractions: keep, change, flip, then think</text>'
  + ''.join(f'<rect x="{20+i*135}" y="34" width="120" height="70" rx="10" fill="{c}"/><text x="{80+i*135}" y="62" text-anchor="middle" fill="#fff" font-weight="bold" font-size="15">{a}</text><text x="{80+i*135}" y="86" text-anchor="middle" fill="#fff" font-size="13">{b}</text>'
            for i, (a, b, c) in enumerate([("Keep", "2/3", "#0A1F3D"), ("Change", "÷ becomes ×", "#0047BA"), ("Flip", "5/6 → 6/5", "#C9A84C"), ("Think", "is it sensible?", "#DB2F30")])) +
  '<text x="280" y="128" text-anchor="middle">2/3 ÷ 5/6 = 2/3 × 6/5 = 12/15 = 4/5. Check: 4/5 × 5/6 = 20/30 = 2/3.</text></svg>')

LABEL = ('<svg viewBox="0 0 560 210" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Nutrition label and price for a bag of rice">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Reading a package: servings and cost</text>'
  '<rect x="40" y="32" width="220" height="170" fill="#fff" stroke="#0A1F3D" stroke-width="2"/>'
  '<text x="52" y="56" font-weight="bold" font-size="16">Nutrition Facts</text><line x1="52" y1="64" x2="248" y2="64" stroke="#0A1F3D" stroke-width="3"/>'
  '<text x="52" y="84">Serving size</text><text x="248" y="84" text-anchor="end" font-weight="bold">1/4 cup dry</text>'
  '<text x="52" y="104">Servings per bag</text><text x="248" y="104" text-anchor="end" font-weight="bold">about 20</text>'
  '<line x1="52" y1="114" x2="248" y2="114" stroke="#0A1F3D"/><text x="52" y="134">Calories</text><text x="248" y="134" text-anchor="end" font-weight="bold">160</text>'
  '<text x="52" y="154">Net weight</text><text x="248" y="154" text-anchor="end">2 lb (907 g)</text>'
  '<rect x="300" y="60" width="220" height="110" rx="10" fill="#f2c14e" stroke="#8a6d1f" stroke-width="2"/>'
  '<text x="410" y="96" text-anchor="middle" font-weight="bold" font-size="15">LONG GRAIN RICE</text><text x="410" y="122" text-anchor="middle">about 5 cups dry</text>'
  '<text x="410" y="152" text-anchor="middle" font-size="20" font-weight="bold">$2.80</text></svg>')

LESSON = {'unit': 'Unit 2: Fractions and Ratios',
 'title': 'Dividing Fractions and Mixed Numbers',
 'subtitle': 'How many servings are in a bag? How much does each one cost? Dividing fractions answers the questions every family shopper asks.',
 'objectives': ['Explain what dividing by a fraction means using a model.',
                'Divide fractions and mixed numbers using reciprocals.',
                'Predict whether a quotient will be greater or less than the dividend.',
                'Find the number of servings in a package and the cost per serving.',
                'Solve multi-step problems with recipes, servings and grocery costs.'],
 'vocab': [['reciprocal', 'The number you multiply by to get 1. The reciprocal of 3/4 is 4/3; the reciprocal of 5 is 1/5.'],
           ['dividend', 'The number being divided.'],
           ['divisor', 'The number you divide by.'],
           ['quotient', 'The answer to a division problem.'],
           ['serving size', 'The amount of food a nutrition label counts as one serving.'],
           ['cost per serving', 'The price of one serving: total cost ÷ number of servings.']],
 'reconnect': {'title': 'Week 6: multiplying fractions',
               'intro': "Dividing fractions is built on multiplying them, so start with last week's skills.",
               'items': [{'t': 'text', 'q': '3/4 × 8/9 = ? Type in simplest form.', 'a': ['2/3'], 'show': '2/3', 'pts': 2, 'why': 'Simplify first: (1 × 2)/(1 × 3) = 2/3.'},
                         {'t': 'num', 'q': '2 1/2 × 1 1/5 = ?', 'a': 3, 'pts': 3, 'why': '5/2 × 6/5 = 30/10 = 3.'},
                         {'t': 'text',
                          'q': 'A recipe uses 3/4 cup of milk. How much milk for 2/3 of the recipe? Type a fraction.',
                          'a': ['1/2'],
                          'show': '1/2 cup',
                          'pts': 2,
                          'why': '2/3 × 3/4 = 6/12 = 1/2 cup.'},
                         {'t': 'open',
                          'key': 'rc_recip',
                          'q': 'What number times 3/4 equals 1? Explain how you know.',
                          'min': 10,
                          'rows': 2,
                          'rubric': ['4/3', 'Explains 3/4 × 4/3 = 12/12 = 1'],
                          'model': '4/3, because 3/4 × 4/3 = 12/12 = 1. The numerator and denominator switch places.'},
                         {'t': 'open',
                          'key': 'rc_jada',
                          'q': 'Explain why 1 1/2 × 1 1/2 is not 1 1/4, and give the correct product.',
                          'min': 15,
                          'rows': 2,
                          'rubric': ['Cannot multiply whole parts and fraction parts separately', 'Correct product 2 1/4'],
                          'model': 'You cannot multiply the whole numbers and the fractions separately, because that skips the cross parts. 3/2 × 3/2 = 9/4 = 2 1/4.'}]},
 'hook': {'title': 'How Many Servings Are in the Bag?',
          'visual': '<svg viewBox="0 0 560 210" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Nutrition label and price for a bag of rice"><text '
                    'x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Reading a package: servings and cost</text><rect x="40" y="32" width="220" height="170" '
                    'fill="#fff" stroke="#0A1F3D" stroke-width="2"/><text x="52" y="56" font-weight="bold" font-size="16">Nutrition Facts</text><line x1="52" y1="64" x2="248" y2="64" '
                    'stroke="#0A1F3D" stroke-width="3"/><text x="52" y="84">Serving size</text><text x="248" y="84" text-anchor="end" font-weight="bold">1/4 cup dry</text><text x="52" '
                    'y="104">Servings per bag</text><text x="248" y="104" text-anchor="end" font-weight="bold">about 20</text><line x1="52" y1="114" x2="248" y2="114" stroke="#0A1F3D"/><text x="52" '
                    'y="134">Calories</text><text x="248" y="134" text-anchor="end" font-weight="bold">160</text><text x="52" y="154">Net weight</text><text x="248" y="154" text-anchor="end">2 lb '
                    '(907 g)</text><rect x="300" y="60" width="220" height="110" rx="10" fill="#f2c14e" stroke="#8a6d1f" stroke-width="2"/><text x="410" y="96" text-anchor="middle" '
                    'font-weight="bold" font-size="15">LONG GRAIN RICE</text><text x="410" y="122" text-anchor="middle">about 5 cups dry</text><text x="410" y="152" text-anchor="middle" '
                    'font-size="20" font-weight="bold">$2.80</text></svg>',
          'html': "<p>Amara's family is planning meals for the week on a budget. A 2-pound bag of rice costs $2.80 and holds about 5 cups of dry rice. The label says one serving is 1/4 cup dry. How "
                  'many servings are in the bag, and what does each serving cost? And if her family cooks 3/4 cup of dry rice at each dinner, how many dinners will the bag last?</p><p>Each of those '
                  "questions asks, <i>how many of these fit in that?</i> That is division.</p><div class='callout'><b>Big idea:</b> Dividing by a fraction asks how many groups of that size fit. To "
                  'divide, multiply by the reciprocal.</div>'},
 'learn': [{'title': 'What Dividing by a Fraction Means',
            'visual': '<svg viewBox="0 0 560 200" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="How many 3/4-cup servings are in 3 cups"><text x="280" '
                      'y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">3 ÷ 3/4: how many 3/4-cup servings fit in 3 cups?</text><rect x="40.0" y="40" width="160.0" '
                      'height="40" fill="#fff" stroke="#0A1F3D" stroke-width="2"/><text x="120.0" y="65" text-anchor="middle">1 cup</text><rect x="200.0" y="40" width="160.0" height="40" fill="#fff" '
                      'stroke="#0A1F3D" stroke-width="2"/><text x="280.0" y="65" text-anchor="middle">1 cup</text><rect x="360.0" y="40" width="160.0" height="40" fill="#fff" stroke="#0A1F3D" '
                      'stroke-width="2"/><text x="440.0" y="65" text-anchor="middle">1 cup</text><line x1="40.0" y1="80" x2="40.0" y2="90" stroke="#0A1F3D"/><line x1="80.0" y1="80" x2="80.0" y2="90" '
                      'stroke="#0A1F3D"/><line x1="120.0" y1="80" x2="120.0" y2="90" stroke="#0A1F3D"/><line x1="160.0" y1="80" x2="160.0" y2="90" stroke="#0A1F3D"/><line x1="200.0" y1="80" '
                      'x2="200.0" y2="90" stroke="#0A1F3D"/><line x1="240.0" y1="80" x2="240.0" y2="90" stroke="#0A1F3D"/><line x1="280.0" y1="80" x2="280.0" y2="90" stroke="#0A1F3D"/><line '
                      'x1="320.0" y1="80" x2="320.0" y2="90" stroke="#0A1F3D"/><line x1="360.0" y1="80" x2="360.0" y2="90" stroke="#0A1F3D"/><line x1="400.0" y1="80" x2="400.0" y2="90" '
                      'stroke="#0A1F3D"/><line x1="440.0" y1="80" x2="440.0" y2="90" stroke="#0A1F3D"/><line x1="480.0" y1="80" x2="480.0" y2="90" stroke="#0A1F3D"/><rect x="40.0" y="100" '
                      'width="120.0" height="40" fill="#0047BA" stroke="#fff" stroke-width="2"/><text x="100.0" y="125" text-anchor="middle" fill="#fff" font-weight="bold">serving 1: 3/4</text><rect '
                      'x="160.0" y="100" width="120.0" height="40" fill="#C9A84C" stroke="#fff" stroke-width="2"/><text x="220.0" y="125" text-anchor="middle" fill="#fff" font-weight="bold">serving '
                      '2: 3/4</text><rect x="280.0" y="100" width="120.0" height="40" fill="#DB2F30" stroke="#fff" stroke-width="2"/><text x="340.0" y="125" text-anchor="middle" fill="#fff" '
                      'font-weight="bold">serving 3: 3/4</text><rect x="400.0" y="100" width="120.0" height="40" fill="#0A1F3D" stroke="#fff" stroke-width="2"/><text x="460.0" y="125" '
                      'text-anchor="middle" fill="#fff" font-weight="bold">serving 4: 3/4</text><text x="280" y="170" text-anchor="middle">Four 3/4-cup servings fill 3 cups exactly, so 3 ÷ 3/4 = '
                      '4.</text><text x="280" y="190" text-anchor="middle" fill="#0047BA">Same as 3 × 4/3 = 12/3 = 4. Dividing by a fraction = multiplying by its reciprocal.</text></svg>',
            'html': '<p>6 ÷ 2 asks, "How many 2s fit in 6?" (3). In the same way, 3 ÷ 3/4 asks, "How many 3/4-cup servings fit in 3 cups?" The model shows the answer is 4.</p><p>Notice that 4 is '
                    '<b>greater</b> than 3. Dividing by a number less than 1 gives a quotient greater than the dividend, because many small pieces fit.</p>',
            'checks': [{'t': 'num', 'q': 'How many 1/3-cup scoops of flour are in 2 cups?', 'a': 6, 'unit': 'scoops', 'pts': 2, 'why': 'Each cup holds three 1/3-cup scoops, so 2 ÷ 1/3 = 6.'},
                       {'t': 'num', 'q': 'A 4-foot board is cut into pieces 2/3 of a foot long. How many pieces?', 'a': 6, 'unit': 'pieces', 'pts': 3, 'why': '4 ÷ 2/3 = 4 × 3/2 = 12/2 = 6.'},
                       {'t': 'open',
                        'key': 'predictdiv',
                        'q': 'Without calculating, will 5 ÷ 1/4 be more or less than 5? Explain using what the division means.',
                        'min': 12,
                        'rows': 2,
                        'rubric': ['More', 'Explains how many quarters fit into 5 (many small pieces)'],
                        'model': 'More, because I am asking how many quarters fit into 5, and there are four in each whole, so 20.'}]},
           {'title': 'Keep, Change, Flip, Then Think',
            'visual': '<svg viewBox="0 0 560 140" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Keep, change, flip"><text x="280" y="18" '
                      'text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Dividing fractions: keep, change, flip, then think</text><rect x="20" y="34" width="120" height="70" '
                      'rx="10" fill="#0A1F3D"/><text x="80" y="62" text-anchor="middle" fill="#fff" font-weight="bold" font-size="15">Keep</text><text x="80" y="86" text-anchor="middle" fill="#fff" '
                      'font-size="13">2/3</text><rect x="155" y="34" width="120" height="70" rx="10" fill="#0047BA"/><text x="215" y="62" text-anchor="middle" fill="#fff" font-weight="bold" '
                      'font-size="15">Change</text><text x="215" y="86" text-anchor="middle" fill="#fff" font-size="13">÷ becomes ×</text><rect x="290" y="34" width="120" height="70" rx="10" '
                      'fill="#C9A84C"/><text x="350" y="62" text-anchor="middle" fill="#fff" font-weight="bold" font-size="15">Flip</text><text x="350" y="86" text-anchor="middle" fill="#fff" '
                      'font-size="13">5/6 → 6/5</text><rect x="425" y="34" width="120" height="70" rx="10" fill="#DB2F30"/><text x="485" y="62" text-anchor="middle" fill="#fff" font-weight="bold" '
                      'font-size="15">Think</text><text x="485" y="86" text-anchor="middle" fill="#fff" font-size="13">is it sensible?</text><text x="280" y="128" text-anchor="middle">2/3 ÷ 5/6 = '
                      '2/3 × 6/5 = 12/15 = 4/5. Check: 4/5 × 5/6 = 20/30 = 2/3.</text></svg>',
            'html': '<p>To divide by a fraction, <b>multiply by its reciprocal</b>. Keep the first fraction, change ÷ to ×, flip the second fraction, then simplify. Then <b>think</b>: does the '
                    "answer make sense? Check by multiplying the quotient by the divisor.</p><div class='example'><b>Why it works:</b> 3 ÷ 3/4 asks how many 3/4s are in 3. Each whole holds 4/3 of a "
                    '3/4-serving, so 3 wholes hold 3 × 4/3 = 4.</div><p>For mixed numbers, change them to improper fractions first: 2 1/4 ÷ 1 1/2 = 9/4 ÷ 3/2 = 9/4 × 2/3 = 18/12 = 1 1/2.</p>',
            'checks': [{'t': 'text', 'q': '3/5 ÷ 9/10 = ? Type in simplest form.', 'a': ['2/3'], 'show': '2/3', 'pts': 3, 'why': '3/5 × 10/9 = 30/45 = 2/3.'},
                       {'t': 'text', 'q': '7/8 ÷ 1/4 = ? Type a mixed number.', 'a': ['3 1/2'], 'show': '3 1/2', 'pts': 3, 'why': '7/8 × 4/1 = 28/8 = 3 1/2.'},
                       {'t': 'num', 'q': '4 1/2 ÷ 1 1/8 = ?', 'a': 4, 'pts': 3, 'why': '9/2 ÷ 9/8 = 9/2 × 8/9 = 72/18 = 4.'},
                       {'t': 'open',
                        'key': 'flipwrong',
                        'q': 'Malik solved 2/3 ÷ 4 by flipping the first fraction: 3/2 × 4 = 6. Explain his mistake, find the correct quotient, and use estimation to show why 6 cannot be right.',
                        'min': 30,
                        'rows': 3,
                        'rubric': ['He flipped the wrong number; flip the divisor', 'Correct: 2/3 × 1/4 = 1/6', 'Estimate: sharing less than 1 among 4 must give less than 1'],
                        'model': 'He flipped the dividend instead of the divisor. The correct way is 2/3 × 1/4 = 2/12 = 1/6. Splitting 2/3 into 4 equal parts must give a small piece, less than 1, so '
                                 '6 is impossible.'}]},
           {'title': 'Servings and Cost per Serving',
            'html': "<p><b>Servings in a package = amount in the package ÷ serving size.</b><br><b>Cost per serving = price ÷ number of servings.</b></p><div class='example'>The rice bag holds about "
                    '5 cups dry, and a serving is 1/4 cup: 5 ÷ 1/4 = 5 × 4 = 20 servings (that is why the label says about 20).<br>Cost per serving: $2.80 ÷ 20 = $0.14.</div>',
            'checks': [{'t': 'num',
                        'q': "Amara's family cooks 3/4 cup of dry rice at each dinner. How many full dinners will the 5-cup bag provide?",
                        'a': 6,
                        'unit': 'dinners',
                        'pts': 3,
                        'why': '5 ÷ 3/4 = 5 × 4/3 = 20/3 = 6 2/3, so 6 full dinners (with 1/2 cup left over).'},
                       {'t': 'num',
                        'q': 'What is the cost of the rice for one of those dinners, to the nearest cent? (3/4 cup is 3 servings.)',
                        'a': 0.42,
                        'tol': 0.001,
                        'unit': 'dollars',
                        'show': '$0.42',
                        'pts': 3,
                        'why': '3 servings × $0.14 = $0.42.'},
                       {'t': 'num',
                        'q': 'A 12-ounce box of oats costs $3.60. One serving is 1 1/2 ounces. What is the cost per serving?',
                        'a': 0.45,
                        'tol': 0.001,
                        'unit': 'dollars',
                        'show': '$0.45',
                        'pts': 3,
                        'why': '12 ÷ 3/2 = 8 servings. $3.60 ÷ 8 = $0.45.'},
                       {'t': 'open',
                        'key': 'perserving',
                        'q': 'Store A sells a 16-ounce jar of peanut butter (serving size 2 tablespoons, about 14 servings) for $3.22. Store B sells a 40-ounce jar (about 35 servings) for $7.35. '
                             'Find the cost per serving for each and decide which is the better buy for a family that eats peanut butter every day.',
                        'min': 30,
                        'rows': 4,
                        'rubric': ['A: $0.23 per serving', 'B: $0.21 per serving', 'Chooses B with a real-life reason, or explains a reason to choose A'],
                        'model': 'Store A: $3.22 ÷ 14 = $0.23 per serving. Store B: $7.35 ÷ 35 = $0.21 per serving. Store B is the better buy for a family that eats it every day, because they will '
                                 'finish the big jar before it spoils.'}]},
           {'title': 'Scaling Recipes With Division',
            'html': "<p>Division also helps when you know how much of an ingredient you have and want to know how many batches it makes.</p><div class='example'>Grandma's cornbread needs 1 3/4 cups "
                    'of cornmeal per pan. Kwame has 5 1/4 cups left over from the reunion. Number of pans: 5 1/4 ÷ 1 3/4 = 21/4 ÷ 7/4 = 21/4 × 4/7 = 3 pans.</div>',
            'checks': [{'t': 'num',
                        'q': 'A smoothie recipe uses 2/3 cup of yogurt. How many smoothies can you make with 4 cups of yogurt?',
                        'a': 6,
                        'unit': 'smoothies',
                        'pts': 2,
                        'why': '4 ÷ 2/3 = 4 × 3/2 = 6.'},
                       {'t': 'num',
                        'q': 'A family has 3 3/4 pounds of ground turkey. Each meal uses 1 1/4 pounds. How many meals?',
                        'a': 3,
                        'unit': 'meals',
                        'pts': 3,
                        'why': '15/4 ÷ 5/4 = 15/4 × 4/5 = 3 meals.'},
                       {'t': 'text',
                        'q': 'A 7 1/2-cup pot of soup is shared equally among 6 people. How much does each person get? Type a mixed number.',
                        'a': ['1 1/4'],
                        'show': '1 1/4 cups',
                        'pts': 3,
                        'why': '15/2 ÷ 6 = 15/2 × 1/6 = 15/12 = 1 1/4 cups.'}]}],
 'handson': {'title': 'Pantry Servings Investigation',
             'intro': "Use real packages to find out how many servings your family's food really holds, and what each serving costs.",
             'materials': ['Three packages from your pantry with nutrition labels (rice, pasta, oats, cereal, beans or flour)',
                           'The price of each (receipt, store app or website, or a flyer)',
                           'Measuring cups',
                           'Paper and pencil'],
             'steps': ['For each package, record the total amount, the serving size and the price.',
                       'Calculate the number of servings by dividing, and compare with the label.',
                       'Calculate the cost per serving.',
                       'Measure how much your family actually uses at one meal. Calculate how many family meals the package lasts and the cost per family meal.',
                       'Share your findings: which food gives your family the most meals for the money?'],
             'record': [{'t': 'open',
                         'key': 'pantryserv',
                         'q': 'Type a table for your three foods: total amount, serving size, servings (your calculation), price, cost per serving, and cost per family meal. Show the division for '
                              'one of them.',
                         'min': 50,
                         'rows': 7,
                         'rubric': ['Three foods with all columns', 'Correct division with fractions', 'Cost per serving and per meal correct to the cent'],
                         'model': 'Oats: 42 oz, serving 1 1/2 oz, 42 ÷ 3/2 = 28 servings, $4.79, $0.17 per serving; family uses 6 oz per breakfast = 4 servings = $0.68 per meal. Pasta: 16 oz, '
                                  'serving 2 oz, 8 servings, $1.25, $0.16 per serving, family meal 16 oz = $1.25. Rice: 5 cups, serving 1/4 cup, 20 servings, $2.80, $0.14 per serving, family meal '
                                  '3/4 cup = $0.42.'},
                        {'t': 'open',
                         'key': 'pantryserv2',
                         'q': "Which food gave your family the most meals for the money? Did the label's servings match how much your family really eats? Explain.",
                         'min': 29,
                         'rows': 3,
                         'rubric': ['Names the best-value food with numbers', 'Compares label serving to real use'],
                         'model': 'Rice gave us the most meals for the money at $0.42 per family dinner. The label serving is 1/4 cup, but our family uses 3/4 cup, so a bag lasts about 6 dinners, '
                                  'not 20.'}]},
 'think': {'intro': 'Explain your reasoning. Your teacher scores these.',
           'items': [{'t': 'open',
                      'key': 'story',
                      'q': 'Write a real-world word problem that is solved by 2 1/2 ÷ 1/4, solve it, and explain what the quotient means in your story. Then write a different problem solved by 2 1/2 '
                           '× 1/4 and explain how the two situations differ.',
                      'min': 56,
                      'rubric': ['Division story asks how many 1/4s fit in 2 1/2 (answer 10)',
                                 'Multiplication story asks for 1/4 of 2 1/2 (answer 5/8)',
                                 'Explains the difference between the two situations'],
                      'model': 'Division: I have 2 1/2 cups of trail mix and put 1/4 cup in each snack bag. How many bags? 2 1/2 ÷ 1/4 = 10 bags. Multiplication: I eat 1/4 of a 2 1/2-cup bag of '
                               'trail mix. How much did I eat? 1/4 × 2 1/2 = 5/8 cup. Division asks how many groups of 1/4 fit; multiplication asks for a part of the amount.'},
                     {'t': 'open',
                      'key': 'budgetweek',
                      'q': "Amara's family has $12.00 for breakfast for 5 days for 4 people. A 42-ounce canister of oats costs $4.79 and a serving is 1 1/2 ounces. A gallon of milk costs $3.89 and "
                           'holds 16 one-cup servings. Each person eats one serving of oats and 1/2 cup of milk each day. Is $12.00 enough? Show every step.',
                      'min': 44,
                      'rubric': ['Oats: 20 servings needed; canister has 28; buy one canister $4.79', 'Milk: 10 cups needed; one gallon $3.89', 'Total $8.68, so yes, with $3.32 left'],
                      'model': '4 people × 5 days = 20 servings of oats. One canister has 42 ÷ 3/2 = 28 servings, so one canister ($4.79) is enough. Milk: 20 × 1/2 = 10 cups, and one gallon has 16 '
                               'cups ($3.89). Total: $4.79 + $3.89 = $8.68. Yes, $12.00 is enough, with $3.32 left.'}]},
 'exit': [{'t': 'num', 'q': '5/6 ÷ 5/12 = ?', 'a': 2, 'pts': 2, 'why': '5/6 × 12/5 = 60/30 = 2.'},
          {'t': 'num', 'q': '3 1/3 ÷ 5/6 = ?', 'a': 4, 'pts': 3, 'why': '10/3 × 6/5 = 60/15 = 4.'},
          {'t': 'num', 'q': '6 ÷ 3/8 = ?', 'a': 16, 'pts': 2, 'why': '6 × 8/3 = 48/3 = 16.'},
          {'t': 'text',
           'q': 'A 3/4-pound block of cheese is cut into 6 equal pieces. How much does each piece weigh? Type a fraction.',
           'a': ['1/8'],
           'show': '1/8 pound',
           'pts': 3,
           'why': '3/4 ÷ 6 = 3/4 × 1/6 = 3/24 = 1/8 pound.'},
          {'t': 'num',
           'q': 'A 15-ounce can of beans costs $1.08 and has about 3 1/2 servings. What is the cost per serving, to the nearest cent?',
           'a': 0.31,
           'tol': 0.001,
           'unit': 'dollars',
           'show': '$0.31',
           'pts': 3,
           'why': '1.08 ÷ 3.5 = 0.3085..., about $0.31 per serving.'}],
 'next': 'Week 8: ratios and ratio language, and comparing deals with ratios.'}

TEACHER = {
 "standards": [
  "MA.6.NSO.2.2: Extend previous understanding of multiplication and division to compute products and quotients of positive fractions by positive fractions, including mixed numbers, with procedural fluency.",
  "MA.6.NSO.2.3: Solve multi-step real-world problems involving any of the four operations with positive multi-digit decimals or positive fractions, including mixed numbers.",
  "MA.K12.MTR.2.1: Demonstrate understanding by representing problems in multiple ways.",
  "MA.K12.MTR.6.1: Assess the reasonableness of solutions.",
  "Financial literacy: reading labels, servings and cost per serving (Jump$tart Spending)."],
 "materials": ["The interactive lesson", "Measuring cups (1, 1/2, 1/3, 1/4) and dry rice or water", "Three pantry packages with labels and prices", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 6 Reconnect questions."],
  [4, "Hook", "Show the rice label. Ask what questions a family shopper would ask."],
  [12, "Meaning", "Use measuring cups: how many 3/4-cup scoops are in 3 cups? Connect to the strip model."],
  [12, "Keep, change, flip, think", "Explain why multiplying by the reciprocal works. Analyze Malik's error."],
  [12, "Servings and cost", "Work the rice and oats examples. Compare the peanut butter jars."],
  [8, "Recipes", "Solve the cornbread and soup problems."],
  [6, "Assign", "Assign the pantry investigation, Think Deeper and the Exit Check."]],
 "key_questions": ["How many of these fit in that?", "Will the quotient be bigger or smaller than the dividend? Why?", "Which number do you flip, and why?", "Does the label's serving match real life?"],
 "misconceptions": ["Flipping the dividend instead of the divisor.", "Believing division always makes numbers smaller.", "Forgetting to change mixed numbers to improper fractions.", "Rounding a number of meals up when only full meals count."],
 "support": ["Use measuring cups to model every division before computing.", "Provide a keep-change-flip-think card.", "Start with whole numbers divided by unit fractions."],
 "challenge": ["Explain why dividing by a fraction is the same as multiplying by its reciprocal using a number line.", "Plan a week of family dinners on a set budget using cost per serving."],
 "background": "<p>Prices and package details are illustrative and realistic for Florida in 2026; Florida does not charge sales tax on most groceries. The rice bag: 2 lb (907 g) of long grain rice is about 5 cups dry and about 20 quarter-cup servings, as real labels show. The \"think\" step stresses estimation and checking by multiplication.</p>",
 "sources": ["CPALMS: MA.6.NSO.2.2 and MA.6.NSO.2.3.", "U.S. Food and Drug Administration: How to Understand and Use the Nutrition Facts Label."]
}

PRINT = {
 "directions": "Show your work. Simplify every answer and check one by multiplying.",
 "items": [
  {"q":"4 ÷ 2/5 = ____     3/4 ÷ 3/8 = ____","a":"10; 2","lines":2},
  {"q":"5/9 ÷ 10/27 = ____     2 2/3 ÷ 1 1/3 = ____","a":"1 1/2; 2","lines":2},
  {"q":"Draw a model to show how many 1/2-cup servings are in 2 1/2 cups.","a":"Five 1/2-cup servings (2 1/2 ÷ 1/2 = 5).","lines":3},
  {"q":"A 24-ounce bag of frozen vegetables costs $2.76. A serving is 3/4 cup and the bag has about 8 servings. What is the cost per serving?","a":"2.76 ÷ 8 = $0.345, about $0.35","lines":2},
  {"q":"You have 3 3/4 cups of flour. A batch of muffins uses 1 1/4 cups. How many batches can you make?","a":"15/4 ÷ 5/4 = 3 batches","lines":2},
  {"q":"Explain why 8 ÷ 1/2 is greater than 8.","a":"It asks how many halves fit in 8; there are 16 halves, so the quotient is greater.","lines":2}]
}
