def dnl(title, top, bot, tlab, blab, hi=None):
    n = len(top); x0, x1 = 120, 600; step = (x1 - x0) / (n - 1)
    s = (f'<svg viewBox="0 0 640 150" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="{title}">'
         f'<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">{title}</text>'
         f'<line x1="{x0}" y1="60" x2="{x1}" y2="60" stroke="#0A1F3D" stroke-width="2"/><line x1="{x0}" y1="110" x2="{x1}" y2="110" stroke="#0A1F3D" stroke-width="2"/>'
         f'<text x="15" y="65" font-weight="bold" fill="#0047BA">{tlab}</text><text x="15" y="115" font-weight="bold" fill="#DB2F30">{blab}</text>')
    for i, (a, b) in enumerate(zip(top, bot)):
        x = x0 + i * step; c = "#fff8e1" if i == hi else "none"
        s += (f'<rect x="{x-22}" y="38" width="44" height="88" rx="6" fill="{c}" fill-opacity="0.6"/>' if i == hi else '') + f'<line x1="{x}" y1="54" x2="{x}" y2="66" stroke="#0A1F3D"/><line x1="{x}" y1="104" x2="{x}" y2="116" stroke="#0A1F3D"/><text x="{x}" y="48" text-anchor="middle">{a}</text><text x="{x}" y="134" text-anchor="middle">{b}</text>'
    return s + '</svg>'

SPEED = dnl("Double number line: 150 miles in 3 hours", ["0", "50", "100", "150", "200"], ["0", "1", "2", "3", "4"], "Miles", "Hours", hi=1)

SHELF = ('<svg viewBox="0 0 640 200" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Two cereal boxes, before and after shrinkflation">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Same price, smaller box</text>'
  '<rect x="120" y="40" width="110" height="130" rx="4" fill="#C9A84C" stroke="#8a6d1f" stroke-width="2"/><text x="175" y="90" text-anchor="middle" font-weight="bold" fill="#0A1F3D">OAT RINGS</text><text x="175" y="140" text-anchor="middle" font-size="14" fill="#0A1F3D">18 oz</text>'
  '<text x="175" y="190" text-anchor="middle" font-weight="bold">Last year: $4.50</text>'
  '<rect x="410" y="62" width="100" height="108" rx="4" fill="#C9A84C" stroke="#8a6d1f" stroke-width="2"/><text x="460" y="104" text-anchor="middle" font-weight="bold" fill="#0A1F3D">OAT RINGS</text><text x="460" y="148" text-anchor="middle" font-size="14" fill="#0A1F3D">15 oz</text>'
  '<text x="460" y="190" text-anchor="middle" font-weight="bold">This year: $4.50</text>'
  '<text x="320" y="110" text-anchor="middle" font-size="22" fill="#DB2F30">→</text></svg>')

LESSON = {'unit': 'Unit 3: Rates and Percents',
 'title': 'Unit Rates',
 'subtitle': 'A rate compares two quantities with different units, like miles and hours. A unit rate tells you how much for just one, and it unlocks speed, pace, prices and more.',
 'objectives': ['Write a rate for two quantities with different units.',
                'Find and interpret unit rates, including rates with fractions.',
                'Use both unit rates of a ratio (miles per hour and hours per mile) to solve problems.',
                'Use double number lines and unit rates to predict and compare.',
                'Spot shrinkflation and compare cost per use at the store.'],
 'vocab': [['rate', 'A ratio that compares two quantities with different units, such as 150 miles in 3 hours.'],
           ['unit rate', 'A rate for one unit of the second quantity, such as 50 miles per hour.'],
           ['per', 'For each; the word that signals a rate.'],
           ['double number line', 'Two number lines lined up so that equivalent amounts sit across from each other.'],
           ['pace', 'Time per unit of distance, such as minutes per mile.'],
           ['shrinkflation', 'When a package gets smaller but the price stays the same or goes up, raising the unit price.']],
 'reconnect': {'title': 'Unit 2: Ratios and ratio tables',
               'intro': 'Unit rates grow straight out of ratio tables. Warm up first.',
               'items': [{'t': 'blanks',
                          'q': 'Complete the ratio table: 4 bottles cost $6.',
                          'sent': 'Bottles: 4, 8, 2, ___. Cost: $6, $12, $___, $1.50',
                          'blanks': [['1'], ['3', '3.00']],
                          'show': '1; 3',
                          'pts': 2,
                          'why': 'Halve 4 : 6 to get 2 : 3; halve again to get 1 : 1.50. Today, the column with 1 has a special name.'},
                         {'t': 'num', 'q': 'Find the missing number: 3 : 5 = 12 : ___', 'a': 20, 'pts': 2, 'why': '3 × 4 = 12, so 5 × 4 = 20.'},
                         {'t': 'text',
                          'q': '3/4 ÷ 1/2 = ? Type a mixed number.',
                          'a': ['1 1/2', '1-1/2', '1 and 1/2'],
                          'show': '1 1/2',
                          'pts': 2,
                          'why': '3/4 × 2/1 = 6/4 = 1 1/2. You will divide fractions to find unit rates today.'},
                         {'t': 'open',
                          'key': 'rc_budget',
                          'q': 'In the Unit 2 Field Day budget, how did you decide whether the prize money was enough?',
                          'min': 12,
                          'rows': 2,
                          'rubric': ['Found the prize budget (1/6 of $240 = $40) and compared it with the cost (24 × $3 = $72)'],
                          'model': 'I found the prize budget, 1/6 of $240, which is $40, and compared it with 24 medals at $3 each, which is $72. It was not enough.'}]},
 'hook': {'title': 'How Fast Is a World Record?',
          'html': '<p>In 2022, in Berlin, Kenyan runner <b>Eliud Kipchoge</b> ran a marathon, 26.2 miles, in 2 hours, 1 minute and 9 seconds, a world record at the time. Is that fast? It is hard to '
                  'feel 26.2 miles in about 121 minutes.</p><p>A <b>unit rate</b> makes it real. Dividing 121 minutes by 26.2 miles gives about 4.6 minutes per mile. That means Kipchoge ran each '
                  "mile in about 4 minutes and 37 seconds, 26 times in a row. Many fit adults would struggle to run one mile that fast.</p><div class='callout'><b>Big idea:</b> A unit rate answers "
                  '"how much for one?" It turns big, hard-to-compare numbers into something you can picture and compare.</div>'},
 'learn': [{'title': 'Rates and Unit Rates',
            'visual': '<svg viewBox="0 0 640 150" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Double number line: 150 miles in 3 hours"><text x="320" '
                      'y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Double number line: 150 miles in 3 hours</text><line x1="120" y1="60" x2="600" y2="60" '
                      'stroke="#0A1F3D" stroke-width="2"/><line x1="120" y1="110" x2="600" y2="110" stroke="#0A1F3D" stroke-width="2"/><text x="15" y="65" font-weight="bold" '
                      'fill="#0047BA">Miles</text><text x="15" y="115" font-weight="bold" fill="#DB2F30">Hours</text><line x1="120.0" y1="54" x2="120.0" y2="66" stroke="#0A1F3D"/><line x1="120.0" '
                      'y1="104" x2="120.0" y2="116" stroke="#0A1F3D"/><text x="120.0" y="48" text-anchor="middle">0</text><text x="120.0" y="134" text-anchor="middle">0</text><rect x="218.0" y="38" '
                      'width="44" height="88" rx="6" fill="#fff8e1" fill-opacity="0.6"/><line x1="240.0" y1="54" x2="240.0" y2="66" stroke="#0A1F3D"/><line x1="240.0" y1="104" x2="240.0" y2="116" '
                      'stroke="#0A1F3D"/><text x="240.0" y="48" text-anchor="middle">50</text><text x="240.0" y="134" text-anchor="middle">1</text><line x1="360.0" y1="54" x2="360.0" y2="66" '
                      'stroke="#0A1F3D"/><line x1="360.0" y1="104" x2="360.0" y2="116" stroke="#0A1F3D"/><text x="360.0" y="48" text-anchor="middle">100</text><text x="360.0" y="134" '
                      'text-anchor="middle">2</text><line x1="480.0" y1="54" x2="480.0" y2="66" stroke="#0A1F3D"/><line x1="480.0" y1="104" x2="480.0" y2="116" stroke="#0A1F3D"/><text x="480.0" '
                      'y="48" text-anchor="middle">150</text><text x="480.0" y="134" text-anchor="middle">3</text><line x1="600.0" y1="54" x2="600.0" y2="66" stroke="#0A1F3D"/><line x1="600.0" '
                      'y1="104" x2="600.0" y2="116" stroke="#0A1F3D"/><text x="600.0" y="48" text-anchor="middle">200</text><text x="600.0" y="134" text-anchor="middle">4</text></svg>',
            'html': '<p>A <b>rate</b> is a ratio of two quantities with <b>different units</b>: 150 miles in 3 hours, 12 eggs for $4.20, 90 heartbeats in 1 minute.</p><p>A <b>unit rate</b> tells how '
                    'much of the first quantity goes with <b>1</b> of the second. To find it, divide: 150 miles ÷ 3 hours = <b>50 miles per hour</b>. The highlighted column on the double number line '
                    'shows it: 50 miles for 1 hour.</p><p>Once you know the unit rate, you can find any amount: at 50 miles per hour, 4 hours means 4 × 50 = 200 miles, and 2 1/2 hours means 125 '
                    'miles.</p><p>A unit rate like 50 miles per hour is an <b>average</b>. It assumes the speed stays the same the whole time, but real trips speed up and slow down, so predictions '
                    'from a unit rate work best when the rate really is steady.</p><p>Notice the word <b>per</b>: it means "for each." The ratio tables from Unit 2 already contained unit rates, in '
                    'the column where one quantity equals 1.</p>',
            'checks': [{'t': 'num',
                        'q': 'A family drives 186 miles in 3 hours. What is their average speed in miles per hour?',
                        'a': 62,
                        'unit': 'miles per hour',
                        'pts': 2,
                        'why': '186 ÷ 3 = 62 miles per hour.'},
                       {'t': 'num',
                        'q': 'A heart beats 18 times in 15 seconds. How many beats is that per minute?',
                        'a': 72,
                        'unit': 'beats per minute',
                        'pts': 3,
                        'why': '15 seconds is 1/4 of a minute, so multiply by 4: 18 × 4 = 72 beats per minute.'},
                       {'t': 'num',
                        'q': 'A reader finishes 45 pages in 1 1/2 hours. How many pages per hour is that?',
                        'a': 30,
                        'unit': 'pages per hour',
                        'pts': 3,
                        'why': '45 ÷ 1 1/2 = 45 ÷ 3/2 = 45 × 2/3 = 30 pages per hour.'},
                       {'t': 'open',
                        'key': 'interpret',
                        'q': 'A sprinkler uses 120 gallons in 40 minutes. Find the unit rate and explain what it means in a complete sentence.',
                        'min': 15,
                        'rows': 2,
                        'rubric': ['3 gallons per minute', 'A sentence explaining that each minute the sprinkler uses 3 gallons'],
                        'model': '120 ÷ 40 = 3 gallons per minute. That means every minute the sprinkler runs, it uses 3 gallons of water.'}]},
           {'title': 'Two Unit Rates for Every Rate',
            'html': "<p>Every rate has <b>two</b> unit rates, depending on which quantity you put first.</p><div class='callout'>Kipchoge: 26.2 miles in about 121 minutes.<br>Miles per minute: 26.2 "
                    '÷ 121 ≈ 0.22 mile per minute.<br>Minutes per mile (pace): 121 ÷ 26.2 ≈ 4.6 minutes per mile.</div><p>Both are correct. Choose the one that answers your question. To know how far '
                    'you go in 30 minutes, miles per minute is handy: 30 × 0.22 ≈ 6.6 miles. To know how long 10 miles takes, minutes per mile is handy: 10 × 4.6 = 46 minutes.</p><p>The same idea '
                    'works with fractions. If a hiker walks 3/4 mile in 1/4 hour, the speed is 3/4 ÷ 1/4 = 3 miles per hour, and the pace is 1/4 ÷ 3/4 = 1/3 hour (20 minutes) per mile.</p>',
            'checks': [{'t': 'num',
                        'q': 'A turtle crawls 2/3 of a meter in 1/6 of a minute. What is its speed in meters per minute?',
                        'a': 4,
                        'unit': 'meters per minute',
                        'pts': 3,
                        'why': '2/3 ÷ 1/6 = 2/3 × 6 = 4 meters per minute.'},
                       {'t': 'num',
                        'q': 'A cyclist rides 12 miles in 48 minutes. What is her pace in minutes per mile?',
                        'a': 4,
                        'unit': 'minutes per mile',
                        'pts': 2,
                        'why': '48 ÷ 12 = 4 minutes per mile.'},
                       {'t': 'num', 'q': 'At that pace, how many minutes will she take to ride 7 1/2 miles?', 'a': 30, 'unit': 'minutes', 'pts': 2, 'why': '7 1/2 × 4 = 30 minutes.'},
                       {'t': 'open',
                        'key': 'which',
                        'q': 'Painting a fence: 3 gallons of paint cover 900 square feet. Write both unit rates, and explain which one you would use to find how much paint you need for a '
                             '1,500-square-foot fence.',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['300 square feet per gallon; 1/300 gallon per square foot', 'Use square feet per gallon: 1,500 ÷ 300 = 5 gallons (or gallons per square foot × 1,500)'],
                        'model': 'The rates are 300 square feet per gallon and 1/300 gallon per square foot. I would use 300 square feet per gallon: 1,500 ÷ 300 = 5 gallons of paint.'}]},
           {'title': 'Comparing with Unit Rates',
            'html': '<p>Unit rates make comparisons quick. In Unit 2 you compared deals by scaling to a common quantity. Unit rates are a shortcut: scale everything to 1.</p><div '
                    "class='callout'><b>Which bus is faster?</b> Bus A travels 135 miles in 3 hours. Bus B travels 220 miles in 4 hours.<br>Bus A: 135 ÷ 3 = 45 miles per hour. Bus B: 220 ÷ 4 = 55 "
                    'miles per hour. Bus B is faster.</div><p>Be careful to compare the same kind of unit rate. A higher miles per hour means faster, but a higher minutes per mile means '
                    '<b>slower</b>.</p>',
            'checks': [{'t': 'text',
                        'q': 'Ama types 270 words in 6 minutes. Kofi types 320 words in 8 minutes. Who types faster? Type the name.',
                        'a': [{'all': [['ama']], 'none': ['not ama', 'kofi is faster', 'kofi types faster', 'kofi faster']}],
                        'show': 'Ama (45 words per minute versus 40)',
                        'pts': 2,
                        'why': 'Ama: 270 ÷ 6 = 45 words per minute. Kofi: 320 ÷ 8 = 40 words per minute.'},
                       {'t': 'open',
                        'key': 'pacecompare',
                        'q': "Runner A's pace is 9 minutes per mile. Runner B's pace is 11 minutes per mile. Which runner is faster, and why might a student get this wrong?",
                        'min': 20,
                        'rows': 2,
                        'rubric': ['Runner A', 'A bigger pace number means more minutes per mile, which is slower; students may think bigger means faster'],
                        'model': 'Runner A is faster, because she needs only 9 minutes for each mile. A student might pick B because 11 is bigger, but a bigger pace means more time per mile, which '
                                 'is slower.'},
                       {'t': 'num',
                        'q': "A farm's well pump fills 15 gallons in 2 1/2 minutes. A garden hose fills 12 gallons in 3 minutes. How many more gallons per minute does the pump fill?",
                        'a': 2,
                        'unit': 'gallons per minute',
                        'pts': 3,
                        'why': 'Pump: 15 ÷ 2 1/2 = 15 ÷ 5/2 = 6 gallons per minute. Hose: 12 ÷ 3 = 4. 6 − 4 = 2.'}]},
           {'title': 'Money: Price per Unit at the Store',
            'visual': '<svg viewBox="0 0 640 200" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Two cereal boxes, before and after shrinkflation"><text '
                      'x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Same price, smaller box</text><rect x="120" y="40" width="110" height="130" rx="4" '
                      'fill="#C9A84C" stroke="#8a6d1f" stroke-width="2"/><text x="175" y="90" text-anchor="middle" font-weight="bold" fill="#0A1F3D">OAT RINGS</text><text x="175" y="140" '
                      'text-anchor="middle" font-size="14" fill="#0A1F3D">18 oz</text><text x="175" y="190" text-anchor="middle" font-weight="bold">Last year: $4.50</text><rect x="410" y="62" '
                      'width="100" height="108" rx="4" fill="#C9A84C" stroke="#8a6d1f" stroke-width="2"/><text x="460" y="104" text-anchor="middle" font-weight="bold" fill="#0A1F3D">OAT '
                      'RINGS</text><text x="460" y="148" text-anchor="middle" font-size="14" fill="#0A1F3D">15 oz</text><text x="460" y="190" text-anchor="middle" font-weight="bold">This year: '
                      '$4.50</text><text x="320" y="110" text-anchor="middle" font-size="22" fill="#DB2F30">→</text></svg>',
            'html': '<p>In Week 4 you found unit prices by dividing. Here are two traps where unit rates protect your money.</p><p><b>Shrinkflation.</b> Companies sometimes shrink a package while '
                    'keeping the price the same. Last year a box of Oat Rings held 18 ounces for $4.50: $4.50 ÷ 18 = $0.25 per ounce. This year it holds 15 ounces for the same $4.50: $4.50 ÷ 15 = '
                    '$0.30 per ounce. The price tag did not change, but you now pay 5 cents more for every ounce. Next week you will learn to describe a change like this as a percent.</p><p><b>Cost '
                    'per use.</b> For things you keep, the useful unit is not ounces but uses. A pair of $60 rain boots that lasts for 120 wears costs $60 ÷ 120 = $0.50 per wear. A $24 pair that '
                    'cracks after 16 wears costs $24 ÷ 16 = $1.50 per wear. The cheaper price tag turned out to cost three times as much for each use.</p>',
            'checks': [{'t': 'text',
                        'q': 'A bag of rice shrinks from 30 ounces to 24 ounces, and the price stays $3.60. By how many cents per ounce did the unit price go up?',
                        'a': ['3', '3 cents', '0.03', '$0.03', '3¢'],
                        'unit': 'cents',
                        'show': '3 cents',
                        'pts': 3,
                        'why': '$3.60 ÷ 30 = $0.12 per ounce; $3.60 ÷ 24 = $0.15 per ounce. The unit price went up 3 cents per ounce.'},
                       {'t': 'num',
                        'q': 'A pack of 60 vitamins costs $9.00 and you take 2 a day. What is the cost per day?',
                        'a': 0.3,
                        'unit': 'dollars',
                        'show': '$0.30',
                        'pts': 3,
                        'why': '60 vitamins ÷ 2 per day = 30 days. $9.00 ÷ 30 = $0.30 per day.'},
                       {'t': 'open',
                        'key': 'shrinkwhy',
                        'q': 'Why do you think companies shrink packages instead of raising prices? What can a shopper do about it?',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Shoppers notice price increases more than smaller packages', 'Check the unit price on the shelf tag, compare sizes, consider other brands'],
                        'model': 'Shoppers notice a higher price right away, but they may not notice a box that is a little smaller. A smart shopper checks the unit price on the shelf tag every time '
                                 'and compares it with other sizes and brands.'}]}],
 'handson': {'title': 'Measure Your Own Rates',
             'intro': 'Your body has rates too. Measure three of them and calculate unit rates.',
             'materials': ['A timer or phone stopwatch', 'A tape measure or a long path where you can measure 20 meters (or 60 feet)', 'A book you are reading', 'Paper and pencil', 'A water bottle'],
             'steps': ['Resting heart rate: sit still for a minute. Find your pulse on your wrist or neck, count beats for 15 seconds, and record the count.',
                       'Exercise heart rate: do jumping jacks for 1 minute, then immediately count beats for 15 seconds. Drink water and rest.',
                       'Walking pace: measure 20 meters. Walk it at a normal speed while someone times you. Repeat and use the average time.',
                       'Reading rate: read silently for exactly 5 minutes and count the pages (or paragraphs) you finished.',
                       'Calculate each unit rate: beats per minute, meters per second, and pages per minute (then pages per hour).'],
             'record': [{'t': 'open',
                         'key': 'ratedata',
                         'q': 'Record your measurements and show the work for each unit rate (beats per minute at rest and after exercise, meters per second walking, pages per hour reading).',
                         'min': 40,
                         'rows': 6,
                         'rubric': ['Measurements recorded', 'Correct calculations for each unit rate with units', 'Work shown (e.g. 19 beats in 15 s × 4 = 76 bpm)'],
                         'model': 'Resting: 19 beats in 15 seconds × 4 = 76 beats per minute. After exercise: 31 × 4 = 124 beats per minute. Walking: 20 m in 16 seconds = 1.25 meters per second. '
                                  'Reading: 6 pages in 5 minutes = 1.2 pages per minute, × 60 = 72 pages per hour.'},
                        {'t': 'open',
                         'key': 'ratepredict',
                         'q': 'Use your walking rate to predict how long it would take you to walk 1 kilometer (1,000 meters). Then use your reading rate to predict how long a 180-page book would '
                              'take. Are your predictions reasonable? Why might they be off?',
                         'min': 39,
                         'rows': 4,
                         'rubric': ['Correct predictions from their unit rates',
                                    'Reasonableness check',
                                    'Sensible reasons predictions could be off (getting tired, rest breaks, harder pages, measurement error)'],
                         'model': 'At 1.25 meters per second, 1,000 m takes 800 seconds, about 13 minutes. At 72 pages per hour, a 180-page book takes 2.5 hours. These seem reasonable, but I might '
                                  'slow down when tired, and some chapters are harder to read, so real times could be longer.'}]},
 'think': {'intro': 'Show your reasoning. Your teacher scores these.',
           'items': [{'t': 'open',
                      'key': 'roadtrip',
                      'q': 'A family drives from Arcadia to Tallahassee, about 300 miles. Their car goes 30 miles per gallon, and gas costs $3.20 per gallon. If they average 60 miles per hour, how '
                           'long will the drive take, and how much will the gas cost? Show each unit rate you use.',
                      'min': 39,
                      'rows': 6,
                      'rubric': ['Time: 300 ÷ 60 = 5 hours', 'Gas used: 300 ÷ 30 = 10 gallons', 'Cost: 10 × $3.20 = $32.00', 'Unit rates named and used correctly'],
                      'model': 'Time: at 60 miles per hour, 300 ÷ 60 = 5 hours. Gas: at 30 miles per gallon, 300 ÷ 30 = 10 gallons. Cost: at $3.20 per gallon, 10 × $3.20 = $32.00. So the trip takes '
                               'about 5 hours and costs about $32 in gas.'},
                     {'t': 'open',
                      'key': 'animal',
                      'q': "In 2012, Sarah, a cheetah at the Cincinnati Zoo, ran 100 meters in 5.95 seconds. Usain Bolt's world record is 100 meters in 9.58 seconds. Find each speed in meters per "
                           'second (round to the nearest tenth), then explain why a cheetah would not win a marathon. (Cheetahs can keep up top speed for only a short burst, usually less than a '
                           'minute.)',
                      'min': 50,
                      'rows': 5,
                      'rubric': ['Cheetah: about 16.8 meters per second; Bolt: about 10.4 meters per second',
                                 'Cheetahs can sprint only for short distances before tiring; a unit rate assumes a constant speed, which is not true over long distances'],
                      'model': 'Cheetah: 100 ÷ 5.95 ≈ 16.8 meters per second. Bolt: 100 ÷ 9.58 ≈ 10.4 meters per second. But a cheetah can keep up its top speed for only a short burst, usually less '
                               'than a minute, before it must stop and rest. A unit rate assumes the speed stays the same, which is not true over a long race.'}]},
 'exit': [{'t': 'num', 'q': 'A machine fills 240 bottles in 8 minutes. How many bottles per minute?', 'a': 30, 'unit': 'bottles per minute', 'pts': 2, 'why': '240 ÷ 8 = 30.'},
          {'t': 'num', 'q': 'A hiker walks 1 1/2 miles in 1/2 hour. What is her speed in miles per hour?', 'a': 3, 'unit': 'miles per hour', 'pts': 2, 'why': '1 1/2 ÷ 1/2 = 3/2 × 2 = 3.'},
          {'t': 'num',
           'q': "Runner A runs 3 miles in 27 minutes. Runner B runs 4 miles in 34 minutes. What is the faster runner's pace, in minutes per mile?",
           'a': 8.5,
           'unit': 'minutes per mile',
           'pts': 2,
           'why': "A: 27 ÷ 3 = 9. B: 34 ÷ 4 = 8.5. Fewer minutes per mile is faster, so B's 8.5 is faster."},
          {'t': 'open',
           'key': 'exit_shrink',
           'q': 'A chip bag shrinks from 10 ounces to 8 ounces but still costs $4.00. Find both unit prices and explain what happened.',
           'min': 12,
           'rows': 2,
           'rubric': ['$0.40 per ounce before; $0.50 per ounce after', 'The price per ounce went up even though the price tag stayed the same (shrinkflation)'],
           'model': 'Before: $4.00 ÷ 10 = $0.40 per ounce. After: $4.00 ÷ 8 = $0.50 per ounce. The unit price went up by $0.10 an ounce even though the price tag did not change.'}],
 'next': 'Week 12: understanding percents, rates per 100, and how sales tax works.'}

TEACHER = {
 "standards": [
  "MA.6.AR.3.2: Given a real-world context, determine a rate for a ratio of quantities with different units. Calculate and interpret the corresponding unit rate.",
  "MA.6.AR.3.5: Solve mathematical and real-world problems involving ratios, rates and unit rates, including comparisons, mixtures, ratios of lengths and conversions within the same measurement system.",
  "MA.6.NSO.2.2: Extend previous understanding of multiplication and division to compute products and quotients of positive fractions by positive fractions, including mixed numbers, with procedural fluency.",
  "MA.K12.MTR.7.1: Apply mathematics to real-world contexts.",
  "Financial literacy: unit pricing, shrinkflation and cost per use (Jump$tart Spending)."],
 "materials": ["The interactive lesson", "A timer, a tape measure, a book", "One package your family buys often, plus an older receipt, photo or website listing showing its earlier size (if available)", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Reconnect questions."],
  [5, "Hook", "Kipchoge's marathon. Have the student guess his minutes per mile before calculating."],
  [12, "Rates and unit rates", "Build the double number line for 150 miles in 3 hours. Practice heartbeats and pages."],
  [10, "Two unit rates", "Find both unit rates for the marathon and the fraction hiker. Choose the useful one."],
  [10, "Comparing", "Compare buses and typists. Discuss why a bigger pace means slower."],
  [10, "Money", "Work the shrinkflation and cost-per-wear examples. Check whether a package your family buys has shrunk."],
  [7, "Assign", "Start the heart rate measurement together; assign the rest of the activity, Think Deeper and the Exit Check."]],
 "key_questions": ["How much for one?", "Which unit rate answers this question?", "Does a bigger number mean better here?", "Did the package change size?"],
 "misconceptions": ["Dividing in the wrong order (hours ÷ miles when miles per hour is asked).", "Thinking a bigger pace number means faster.", "Assuming a rate stays constant forever (sprinting versus marathons).", "Trusting the price tag without checking the unit price."],
 "support": ["Use a double number line for every problem.", "Write \"___ per 1 ___\" as a frame.", "Provide a multiplication chart."],
 "challenge": ["Find two real products that have shrunk in your house and compute how much more you pay per unit.", "Convert Kipchoge's pace to miles per hour."],
 "background": "<p>Kipchoge's 2:01:09 at the 2022 Berlin Marathon (September 25, 2022) was the world record until October 2023. 121.15 minutes ÷ 26.2 miles ≈ 4.62 minutes per mile (about 4:37). Usain Bolt's 100 m world record is 9.58 seconds (Berlin, 2009). Sarah the cheetah's 5.95-second 100 m run (Cincinnati Zoo, June 2012) was reported by National Geographic. Shrinkflation examples are invented with realistic numbers.</p>",
 "sources": ["World Athletics, Marathon records.", "CPALMS, MA.6.AR.3 benchmarks.", "Bureau of Labor Statistics, Shrinkflation and the Consumer Price Index.", "Jump$tart Coalition, National Standards for Personal Financial Education."]
}

PRINT = {
 "directions": "Show your work.",
 "items": [
  {"q":"A car travels 228 miles in 4 hours. What is its speed?","a":"57 miles per hour","lines":1},
  {"q":"A printer prints 56 pages in 1 3/4 minutes. How many pages per minute?","a":"56 ÷ 7/4 = 56 × 4/7 = 32 pages per minute","lines":2},
  {"q":"A swimmer swims 1,200 meters in 30 minutes. Write both unit rates.","a":"40 meters per minute; 1/40 minute per meter","lines":2},
  {"q":"Which is faster: 200 words in 5 minutes or 252 words in 6 minutes?","a":"40 vs 42 words per minute; 252 in 6 is faster","lines":2},
  {"q":"Cereal shrinks from 20 oz to 16 oz at $5.00. Find both unit prices.","a":"$0.25 per oz → $0.3125 (about $0.31) per oz","lines":2},
  {"q":"A $45 museum membership for your co-op family is used 9 times. Single tickets cost $7 each. What is the membership's cost per visit, and which is the better deal for 9 visits?","a":"$45 ÷ 9 = $5 per visit versus $7; the membership.","lines":2}]
}
