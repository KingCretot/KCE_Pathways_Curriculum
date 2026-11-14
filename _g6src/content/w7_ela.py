STRUCT = ('<svg viewBox="0 0 560 250" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Five text structures and their signal words">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Five text structures and their signal words</text>'
  + ''.join(f'<g transform="translate({8+i*110} 32)"><rect width="104" height="210" rx="10" fill="{c}"/><text x="52" y="22" text-anchor="middle" fill="#fff" font-weight="bold" font-size="12">{n}</text>{shape}'
            + ''.join(f'<text x="52" y="{150+j*14}" text-anchor="middle" fill="#fff">{w}</text>' for j, w in enumerate(ws)) + '</g>'
            for i, (n, c, shape, ws) in enumerate([
                ("Sequence", "#0A1F3D", '<rect x="12" y="40" width="80" height="18" fill="#fff"/><rect x="12" y="66" width="80" height="18" fill="#fff"/><rect x="12" y="92" width="80" height="18" fill="#fff"/><text x="52" y="53" text-anchor="middle">1</text><text x="52" y="79" text-anchor="middle">2</text><text x="52" y="105" text-anchor="middle">3</text>', ["first, next", "then, finally", "in 1954", "after that"]),
                ("Cause/Effect", "#0047BA", '<rect x="8" y="58" width="36" height="34" fill="#fff"/><rect x="60" y="58" width="36" height="34" fill="#fff"/><path d="M44 75 h14" stroke="#fff" stroke-width="3"/><text x="26" y="80" text-anchor="middle">cause</text><text x="78" y="80" text-anchor="middle">effect</text>', ["because, so", "as a result", "therefore", "led to"]),
                ("Compare", "#C9A84C", '<circle cx="38" cy="76" r="26" fill="#fff" opacity=".85"/><circle cx="66" cy="76" r="26" fill="#fff" opacity=".6"/>', ["both, alike", "however", "unlike, but", "in contrast"]),
                ("Problem/Sol.", "#DB2F30", '<rect x="12" y="44" width="80" height="26" fill="#fff"/><rect x="12" y="84" width="80" height="26" fill="#fff"/><text x="52" y="61" text-anchor="middle">problem</text><text x="52" y="101" text-anchor="middle">solution</text>', ["problem, issue", "solved, fix", "one answer", "to address"]),
                ("Description", "#0A1F3D", '<circle cx="52" cy="76" r="16" fill="#fff"/>' + ''.join(f'<line x1="52" y1="76" x2="{52+34*dx}" y2="{76+30*dy}" stroke="#fff" stroke-width="2"/>' for dx, dy in [(1, 0), (-1, 0), (0.6, 1), (-0.6, 1), (0.6, -1), (-0.6, -1)]), ["for example", "such as", "features", "includes"])])) + '</svg>')

P_SEQ = "<b>Passage A.</b> In 1954, Cheikh Anta Diop published his first book arguing that ancient Egypt was an African civilization. Next, he spent years building the evidence, including setting up a radiocarbon laboratory in Dakar in 1966. Then, in 1974, he presented his research at a UNESCO meeting in Cairo. Finally, after his death in 1986, the University of Dakar was renamed in his honor."
P_CE = "<b>Passage B.</b> Florida's springs are fed by the Floridan Aquifer, an underground layer of rock that holds fresh water. When people pump too much water from wells, the aquifer's level drops. As a result, some springs flow more weakly. Fertilizer from lawns and farms can also soak into the ground, and because of this, algae can grow quickly in spring water and crowd out native plants."
P_CC = "<b>Passage C.</b> Kemet and Kush both grew along the Nile, and both were ruled by kings who built pyramids. However, the two kingdoms were different in important ways. Egyptian pyramids, like the Great Pyramid, were huge, with gently sloping sides. In contrast, the pyramids of Meroe in Kush were smaller and much steeper. Kush also became famous for iron working, while Kemet relied more on copper and bronze for centuries."
P_PS = "<b>Passage D.</b> In many parts of the world, millions of people do not have reliable electricity at night, so children struggle to do homework after dark. One solution has been small solar lamps. A solar panel charges the lamp during the day, and the lamp gives light at night without fuel. Kerosene lamps, which solar lamps often replace, produce smoke that is harmful to breathe, so solar lamps also protect families' health."

LESSON = {'unit': 'Unit 2: Explaining the World (Informational)',
 'title': 'Text Structures',
 'subtitle': "Authors organize information on purpose. When you see the structure, you see the author's thinking.",
 'objectives': ['Identify five text structures: sequence, cause and effect, compare and contrast, problem and solution, and description.',
                'Use signal words and graphic organizers to identify a structure.',
                "Explain how a text's structure helps the author's purpose and central idea.",
                'Rewrite information in a different structure.',
                'Use the roots sequ, dict, fer and ven.'],
 'vocab': [['text structure', 'The way an author organizes information in a text.'],
           ['sequence', 'Events or steps in time order.'],
           ['cause and effect', 'A structure that explains why something happened (cause) and what happened because of it (effect).'],
           ['compare and contrast', 'A structure that shows how two or more things are alike and different.'],
           ['problem and solution', 'A structure that explains a problem and one or more ways to solve it.'],
           ['description', 'A structure that explains a topic by listing its features, characteristics or examples.'],
           ['signal words', 'Words that hint at a structure, such as because, however, first or as a result.'],
           ['sequ / dict', 'Latin roots meaning follow (sequence, consequence) and say (dictionary, predict).'],
           ['fer / ven', 'Latin roots meaning carry (transfer, refer) and come (event, convention).']],
 'reconnect': {'title': 'Week 6: central idea and supporting details',
               'intro': "Text structure is how authors arrange their supporting details. Start with last week's skills.",
               'items': [{'t': 'open',
                          'key': 'rc_ci',
                          'q': "What is the difference between a topic and a central idea? Give an example of each about Florida's springs.",
                          'min': 15,
                          'rows': 2,
                          'rubric': ['Topic is a word or phrase; central idea is a full sentence about it', 'Accurate examples'],
                          'model': "A topic is a phrase, like Florida's springs. A central idea is a sentence about it, like: Florida's springs are threatened by overpumping and pollution."},
                         {'t': 'text',
                          'q': '"About 18 million hectares were restored by 2020" is what kind of supporting detail?',
                          'a': ['statistic', 'a statistic'],
                          'pts': 2,
                          'why': 'A fact given as a number is a statistic.'},
                         {'t': 'blanks',
                          'q': 'Complete with the root meanings.',
                          'sent': 'The roots hydr and aqua mean ___. The roots geo and terr mean ___.',
                          'blanks': [['water'], ['earth', 'land', 'earth or land', 'land or earth']],
                          'pts': 3,
                          'why': 'hydr/aqua mean water; geo/terr mean earth or land.'},
                         {'t': 'open',
                          'key': 'rc_minor',
                          'q': 'Explain the difference between a supporting detail and a minor detail.',
                          'min': 15,
                          'rows': 2,
                          'rubric': ['Supporting detail helps prove the central idea', 'Minor detail is true but does not support it'],
                          'model': 'A supporting detail helps prove or explain the central idea. A minor detail may be true and interesting but does not help prove the central idea.'}]},
 'hook': {'title': 'Same Facts, Different Shapes',
          'visual': '<svg viewBox="0 0 560 250" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Five text structures and their signal words"><text '
                    'x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Five text structures and their signal words</text><g transform="translate(8 32)"><rect '
                    'width="104" height="210" rx="10" fill="#0A1F3D"/><text x="52" y="22" text-anchor="middle" fill="#fff" font-weight="bold" font-size="12">Sequence</text><rect x="12" y="40" '
                    'width="80" height="18" fill="#fff"/><rect x="12" y="66" width="80" height="18" fill="#fff"/><rect x="12" y="92" width="80" height="18" fill="#fff"/><text x="52" y="53" '
                    'text-anchor="middle">1</text><text x="52" y="79" text-anchor="middle">2</text><text x="52" y="105" text-anchor="middle">3</text><text x="52" y="150" text-anchor="middle" '
                    'fill="#fff">first, next</text><text x="52" y="164" text-anchor="middle" fill="#fff">then, finally</text><text x="52" y="178" text-anchor="middle" fill="#fff">in 1965</text><text '
                    'x="52" y="192" text-anchor="middle" fill="#fff">after that</text></g><g transform="translate(118 32)"><rect width="104" height="210" rx="10" fill="#0047BA"/><text x="52" y="22" '
                    'text-anchor="middle" fill="#fff" font-weight="bold" font-size="12">Cause/Effect</text><rect x="8" y="58" width="36" height="34" fill="#fff"/><rect x="60" y="58" width="36" '
                    'height="34" fill="#fff"/><path d="M44 75 h14" stroke="#fff" stroke-width="3"/><text x="26" y="80" text-anchor="middle">cause</text><text x="78" y="80" '
                    'text-anchor="middle">effect</text><text x="52" y="150" text-anchor="middle" fill="#fff">because, so</text><text x="52" y="164" text-anchor="middle" fill="#fff">as a '
                    'result</text><text x="52" y="178" text-anchor="middle" fill="#fff">therefore</text><text x="52" y="192" text-anchor="middle" fill="#fff">led to</text></g><g '
                    'transform="translate(228 32)"><rect width="104" height="210" rx="10" fill="#C9A84C"/><text x="52" y="22" text-anchor="middle" fill="#fff" font-weight="bold" '
                    'font-size="12">Compare</text><circle cx="38" cy="76" r="26" fill="#fff" opacity=".85"/><circle cx="66" cy="76" r="26" fill="#fff" opacity=".6"/><text x="52" y="150" '
                    'text-anchor="middle" fill="#fff">both, alike</text><text x="52" y="164" text-anchor="middle" fill="#fff">however</text><text x="52" y="178" text-anchor="middle" '
                    'fill="#fff">unlike, but</text><text x="52" y="192" text-anchor="middle" fill="#fff">in contrast</text></g><g transform="translate(338 32)"><rect width="104" height="210" rx="10" '
                    'fill="#DB2F30"/><text x="52" y="22" text-anchor="middle" fill="#fff" font-weight="bold" font-size="12">Problem/Sol.</text><rect x="12" y="44" width="80" height="26" '
                    'fill="#fff"/><rect x="12" y="84" width="80" height="26" fill="#fff"/><text x="52" y="61" text-anchor="middle">problem</text><text x="52" y="101" '
                    'text-anchor="middle">solution</text><text x="52" y="150" text-anchor="middle" fill="#fff">problem, issue</text><text x="52" y="164" text-anchor="middle" fill="#fff">solved, '
                    'fix</text><text x="52" y="178" text-anchor="middle" fill="#fff">one answer</text><text x="52" y="192" text-anchor="middle" fill="#fff">to address</text></g><g '
                    'transform="translate(448 32)"><rect width="104" height="210" rx="10" fill="#0A1F3D"/><text x="52" y="22" text-anchor="middle" fill="#fff" font-weight="bold" '
                    'font-size="12">Description</text><circle cx="52" cy="76" r="16" fill="#fff"/><line x1="52" y1="76" x2="86" y2="76" stroke="#fff" stroke-width="2"/><line x1="52" y1="76" x2="18" '
                    'y2="76" stroke="#fff" stroke-width="2"/><line x1="52" y1="76" x2="72.4" y2="106" stroke="#fff" stroke-width="2"/><line x1="52" y1="76" x2="31.6" y2="106" stroke="#fff" '
                    'stroke-width="2"/><line x1="52" y1="76" x2="72.4" y2="46" stroke="#fff" stroke-width="2"/><line x1="52" y1="76" x2="31.6" y2="46" stroke="#fff" stroke-width="2"/><text x="52" '
                    'y="150" text-anchor="middle" fill="#fff">for example</text><text x="52" y="164" text-anchor="middle" fill="#fff">such as</text><text x="52" y="178" text-anchor="middle" '
                    'fill="#fff">features</text><text x="52" y="192" text-anchor="middle" fill="#fff">includes</text></g></svg>',
          'html': '<p>Imagine you have a pile of facts about the Nile. You could tell them in time order (how Egypt was unified), explain causes and effects (how the flood created farmland), compare '
                  'Egypt with Nubia, describe a problem and its solution (how basin irrigation managed the flood), or simply describe the river. The facts are the same. The <b>structure</b> changes '
                  "what the reader notices.</p><p>Good readers spot the structure quickly, because it tells them how the ideas connect.</p><div class='callout'><b>Big idea:</b> Authors choose a "
                  'structure to fit their purpose. Signal words and the shape of the ideas reveal it.</div>'},
 'learn': [{'title': 'Sequence and Cause and Effect',
            'html': "<div class='card'><b>Passage A.</b> In 1954, Cheikh Anta Diop published his first book arguing that ancient Egypt was a Black African civilization. Next, he spent years building "
                    'the evidence, including setting up a radiocarbon laboratory in Dakar in 1966. Then, in 1974, he presented his research at a UNESCO meeting in Cairo. Finally, after his death in '
                    "1986, the University of Dakar was renamed in his honor.</div><div class='card'><b>Passage B.</b> Florida's springs are fed by the Floridan Aquifer, an underground layer of rock "
                    "that holds fresh water. When people pump too much water from wells, the aquifer's level drops. As a result, some springs flow more weakly. Fertilizer from lawns and farms can "
                    'also soak into the ground, and because of this, algae can grow quickly in spring water and crowd out native plants.</div>',
            'checks': [{'t': 'blanks',
                        'q': 'Name the structure of each passage.',
                        'sent': 'Passage A: ___   Passage B: ___',
                        'blanks': [['sequence', 'chronological', 'time order', 'sequential', 'chronological order'], ['cause and effect', 'cause effect', 'cause/effect', 'cause-and-effect']],
                        'show': 'A: sequence; B: cause and effect',
                        'pts': 3,
                        'why': 'Passage A uses dates and first-next-then-finally; Passage B uses when, as a result and because of this to explain causes and effects.'},
                       {'t': 'open',
                        'key': 'signalA',
                        'q': 'List three signal words or phrases in Passage A and explain how they help the reader.',
                        'min': 15,
                        'rows': 2,
                        'rubric': ['Three signals (In 1954, Next, Then, in 1974, Finally, after)', 'Explains they show time order'],
                        'model': "In 1954, Next and Finally. They tell the reader the order the events happened, so it is easy to follow Diop's life step by step."},
                       {'t': 'open',
                        'key': 'chainB',
                        'q': 'Passage B describes two cause-and-effect chains. Write both as Cause → Effect → Effect.',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Overpumping → aquifer drops → springs weaker', 'Fertilizer soaks in → algae grow → native plants crowded out'],
                        'model': '1. Too much pumping → the aquifer level drops → springs flow more weakly. 2. Fertilizer soaks into the ground → algae grow quickly → native plants are crowded '
                                 'out.'}]},
           {'title': 'Compare and Contrast and Problem and Solution',
            'html': "<div class='card'><b>Passage C.</b> Kemet and Kush both grew along the Nile, and both were ruled by kings who built pyramids. However, the two kingdoms were different in "
                    'important ways. Egyptian pyramids, like the Great Pyramid, were huge, with gently sloping sides. In contrast, the pyramids of Meroe in Kush were smaller and much steeper. Kush '
                    'also became famous for iron working, while Kemet relied more on copper and bronze for centuries. Kush had rich iron ore and forests for fuel, and iron tools and weapons helped '
                    "make Meroe a wealthy trading center. The Great Pyramid was built around 2560 BCE, but Kush's iron working grew at Meroe after about 500 BCE, and Meroe's pyramids were built from "
                    "about 300 BCE.</div><div class='card'><b>Passage D.</b> In many parts of the world, millions of people do not have reliable electricity at night, so children struggle to do "
                    'homework after dark. One solution has been small solar lamps. A solar panel charges the lamp during the day, and the lamp gives light at night without fuel. Kerosene lamps, '
                    "which solar lamps often replace, produce smoke that is harmful to breathe, so solar lamps also protect families' health.</div><div class='card'><b>Passage E.</b> Ichetucknee "
                    'Springs in North Florida is a chain of eight major springs that pour out millions of gallons of clear water every day. The water stays about 72 °F all year, so manatees '
                    'sometimes visit in winter. The spring run is lined with eelgrass, cypress trees and limestone banks, and its water is so clear that visitors can see fish and turtles several '
                    'feet below.</div>',
            'checks': [{'t': 'open',
                        'key': 'ccC',
                        'q': 'Passage C compares Kemet and Kush. List one similarity and two differences, and name the signal words that showed you.',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Similarity: both on the Nile with kings and pyramids',
                                   'Two differences: pyramid size and slope; iron versus copper and bronze',
                                   'Signal words: both, However, In contrast, while'],
                        'model': "Similarity: both grew along the Nile and built pyramids. Differences: Meroe's pyramids were smaller and steeper, and Kush was known for iron while Kemet used copper "
                                 'and bronze. Signal words: both, However, In contrast and while.'},
                       {'t': 'open',
                        'key': 'psD',
                        'q': 'What problem and solution does Passage D describe? What extra benefit of the solution does the author add?',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Problem: no reliable electricity at night for homework', 'Solution: solar lamps', 'Extra benefit: replace smoky kerosene lamps, protecting health'],
                        'model': 'The problem is that many children have no reliable electricity at night to do homework. The solution is small solar lamps charged by the sun. The extra benefit is '
                                 'that they replace kerosene lamps, whose smoke is harmful to breathe.'},
                       {'t': 'text',
                        'q': 'Which signal word in Passage C shows a contrast is coming? Type one word or phrase.',
                        'a': ['however', 'in contrast', 'while', 'different'],
                        'show': 'However (also In contrast, while)',
                        'pts': 2,
                        'why': 'However, in contrast and while signal differences.'},
                       {'t': 'open',
                        'key': 'descE',
                        'q': 'Name the structure of Passage E and give two pieces of evidence from the passage that prove it.',
                        'min': 15,
                        'rows': 2,
                        'rubric': ['Description', 'Lists features or characteristics (temperature, plants, clarity) with no causes, steps or problem'],
                        'model': 'Description. It lists features of the spring, like its steady 72 °F water and its eelgrass, cypress trees and clear water, without telling steps, causes or a '
                                 'problem.'}]},
           {'title': 'Why Structure Matters',
            'html': "<p>Authors choose structures to match their <b>purpose</b>:</p><table class='t'><tr><th>If the author wants to...</th><th>they might use</th></tr><tr><td>tell how something "
                    'happened over time</td><td>sequence</td></tr><tr><td>explain why something happens</td><td>cause and effect</td></tr><tr><td>help readers weigh two things</td><td>compare and '
                    'contrast</td></tr><tr><td>convince readers a problem can be fixed</td><td>problem and solution</td></tr><tr><td>help readers picture a '
                    'topic</td><td>description</td></tr></table><p>Long texts often mix structures. The Week 6 Great Green Wall article used problem and solution overall, sequence in paragraph 2, '
                    'and cause and effect in paragraph 1.</p>',
            'checks': [{'t': 'open',
                        'key': 'choose',
                        'q': 'You are writing an article to convince your town to protect a local spring. Which structure would you choose for the main body, and why?',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Problem and solution (or cause and effect)', 'Explains how the structure fits the purpose'],
                        'model': 'Problem and solution, because I want readers to understand the threat to the spring and then see clear steps the town can take, which makes them more likely to '
                                 'act.'},
                       {'t': 'open',
                        'key': 'ggwstruct',
                        'q': 'Look back at paragraph 3 of the Week 6 article: "Planting trees in a desert, however, turned out to be harder than it sounded..." What structure does that paragraph '
                             'use, and how do you know?',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Problem and solution (trees died; project changed to a patchwork planned with communities)', 'Cites the problem and the change'],
                        'model': 'It uses problem and solution. The problem is that many young trees died because no one was paid to water or protect them. The solution was to change the plan into a '
                                 'patchwork of farms, forests and grasslands planned with local people.'}]},
           {'title': 'Roots: Follow, Say, Carry, Come',
            'html': "<table class='t'><tr><th>Root</th><th>Meaning</th><th>Examples</th></tr><tr><td>sequ, secu</td><td>follow</td><td>sequence, consequence, "
                    'consecutive</td></tr><tr><td>dict</td><td>say, tell</td><td>predict, dictionary, contradict</td></tr><tr><td>fer</td><td>carry, bring</td><td>transfer, refer, '
                    'fertile</td></tr><tr><td>ven, vent</td><td>come</td><td>event, invent, convention</td></tr></table>',
            'checks': [{'t': 'text',
                        'q': 'Using the root, what is a <b>consequence</b>?',
                        'a': [{'all': [['follow', 'result', 'effect', 'happens after', 'comes after']]}],
                        'show': 'something that follows from an action (a result)',
                        'pts': 2,
                        'why': 'sequ means follow: a consequence follows from a cause.'},
                       {'t': 'blanks',
                        'q': 'Complete each sentence with a root word.',
                        'sent': 'Scientists ___ the weather for tomorrow. The movers will ___ the boxes to the new house. Nile silt made the soil ___.',
                        'blanks': [['predict', 'predicts'], ['transfer'], ['fertile']],
                        'pts': 3,
                        'why': 'predict (say before), transfer (carry across), fertile (able to bring forth crops).'},
                       {'t': 'text',
                        'q': 'Using roots, what does it mean to <b>contradict</b> someone?',
                        'a': [{'all': [['against', 'opposite', 'disagree', 'say the opposite', 'say no', 'deny']]}],
                        'show': 'to say the opposite of what they said',
                        'pts': 2,
                        'why': 'contra (against) + dict (say).'}]}],
 'handson': {'title': 'Text Structure Sort and Build',
             'intro': 'Turn the five structures into shapes you can build, then sort real sentences into them.',
             'materials': ['Five sheets of paper or poster boards labeled with the five structures',
                           'Index cards or sticky notes',
                           'Scissors, tape and markers',
                           'A news article, cereal box, recipe or manual from home'],
             'steps': ["Draw each structure's organizer on its sheet: a numbered ladder (sequence), boxes with an arrow (cause and effect), two overlapping circles (compare), two boxes (problem and "
                       'solution), a web (description).',
                       'Copy ten sentences onto cards: some from the four passages, some from a text at home.',
                       'Sort each card onto the sheet whose structure it fits, and circle its signal words.',
                       'Find one real text at home (a recipe, a manual, a news story) and decide which structure it mostly uses.',
                       'Explain your sort to a family member and let them challenge one card.'],
             'record': [{'t': 'open',
                         'key': 'sort',
                         'q': 'List your ten cards and the structure you placed each under, with signal words circled (capitalize them). Then name the home text you analyzed and its structure.',
                         'min': 60,
                         'rows': 8,
                         'rubric': ['Ten cards sorted correctly', 'Signal words identified', 'A real home text correctly analyzed'],
                         'model': 'Sequence: "NEXT, he spent years building the evidence." "FINALLY, after his death..." Cause and effect: "AS A RESULT, some springs flow more weakly." "BECAUSE OF '
                                  'THIS, algae can grow." Compare: "HOWEVER, the two kingdoms were different." "IN CONTRAST, the pyramids of Meroe were steeper." Problem and solution: "ONE SOLUTION '
                                  'has been small solar lamps." From home: "FIRST, preheat the oven" (sequence), "Contains vitamins SUCH AS iron and calcium" (description). Home text: our pancake '
                                  'mix box uses sequence, because the directions are numbered steps.'},
                        {'t': 'open',
                         'key': 'sort2',
                         'q': 'Which card did your family member challenge, and who was right? Explain.',
                         'min': 20,
                         'rows': 3,
                         'rubric': ['Names the challenged card', 'Explains the reasoning with signal words'],
                         'model': 'My mom challenged "When people pump too much water, the aquifer drops." She thought it was sequence because of when. I explained it is cause and effect, because '
                                  'the pumping causes the drop.'}]},
 'think': {'intro': 'Show that you can use structure as a writer. Your teacher scores these.',
           'items': [{'t': 'open',
                      'key': 'rewrite',
                      'q': 'Take the facts from Passage C (Kemet and Kush) and rewrite them as a short paragraph with a different structure: either sequence or cause and effect. Use at least three '
                           'signal words for your new structure and underline them by writing them in capital letters.',
                      'min': 47,
                      'rows': 8,
                      'rubric': ['Uses the chosen new structure throughout', 'Accurate facts from the passage', 'Three or more correct signal words', 'Clear paragraph'],
                      'model': 'Sequence: FIRST, around 2560 BCE, Kemet built the Great Pyramid, a huge pyramid with gently sloping sides. LATER, after about 500 BCE, iron working grew at Meroe in '
                               "Kush, while Kemet still relied mostly on copper and bronze. THEN, from about 300 BCE, the people of Kush built Meroe's pyramids, smaller and much steeper than "
                               "Egypt's."},
                     {'t': 'open',
                      'key': 'purpose',
                      'q': "Why do you think the author of Passage B (Florida's springs) chose cause and effect instead of description? What does that choice help readers understand?",
                      'min': 39,
                      'rows': 4,
                      'rubric': ['Purpose: explain why springs are in trouble', 'Cause and effect shows human actions lead to harm', 'Suggests readers can change the causes'],
                      'model': 'The author wanted readers to understand why the springs are in trouble, not just what they look like. Cause and effect shows that human actions like overpumping and '
                               'using fertilizer lead to weaker springs and algae, which suggests that changing those actions could help protect them.'}]},
 'exit': [{'t': 'open',
           'key': 'exit_new',
           'q': 'Read: <i>Unlike the Nile, the Niger River flows in a great arc through West Africa. Both rivers, however, flood each year.</i> Name the structure and quote the two signal words that '
                'prove it.',
           'min': 10,
           'rows': 2,
           'rubric': ['Compare and contrast', 'Signal words: unlike, both (or however)'],
           'model': 'Compare and contrast. The signal words unlike and both show a difference and a similarity.'},
          {'t': 'open',
           'key': 'exit_new2',
           'q': 'Read: <i>Heavy rain fell for three days, so the river rose over its banks. As a result, the town closed its roads.</i> Name the structure and explain how you know.',
           'min': 10,
           'rows': 2,
           'rubric': ['Cause and effect', 'Signal words so and as a result connect causes to effects'],
           'model': 'Cause and effect, because so and as a result show that the rain caused the river to rise, which caused the roads to close.'},
          {'t': 'open',
           'key': 'exit_ps',
           'q': 'Write one sentence about a problem in your community and one sentence offering a solution.',
           'min': 15,
           'rows': 2,
           'rubric': ['A real problem', 'A connected solution with a signal word'],
           'model': "Our park's trash cans overflow every weekend. One solution is to add recycling bins and ask families to take their trash home."},
          {'t': 'text', 'q': 'What does the root <b>sequ</b> mean?', 'a': ['follow', 'to follow'], 'pts': 2, 'why': 'sequ means follow, as in sequence.'}],
 'next': 'Week 8: summarizing without copying. How to retell an informational text in your own words, accurately and briefly.'}

TEACHER = {
 "standards": [
  "ELA.6.R.2.1: Explain how individual text sections and/or features convey meaning in texts.",
  "ELA.6.R.2.2: Analyze the central idea(s), implied or explicit, and its development throughout a text.",
  "ELA.6.C.1.4: Write expository texts to explain and/or analyze information from multiple sources, using a logical organizational structure, relevant elaboration, and varied transitions.",
  "ELA.6.V.1.2: Apply knowledge of Greek and Latin roots and affixes to determine meanings of words and phrases in grade-level content.",
  "ELA.K12.EE.2.1: Read and comprehend grade-level complex texts proficiently."],
 "materials": ["The interactive lesson", "Five sheets of paper, index cards, tape and markers", "A recipe, manual or news article from home", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 6 Reconnect questions."],
  [6, "Hook", "Show the five organizers. Ask how the same Nile facts could be told five ways."],
  [12, "Sequence and cause and effect", "Read Passages A and B. Highlight signal words and build the cause-effect chains."],
  [12, "Compare and problem and solution", "Read Passages C and D. Complete a Venn diagram and a problem-solution chart."],
  [8, "Purpose", "Match structures to purposes. Analyze paragraph 3 of last week's article."],
  [8, "Roots", "Build words with sequ, dict, fer and ven."],
  [8, "Assign", "Model the first sentence of the rewrite. Assign the sort, Think Deeper and the Exit Check."]],
 "key_questions": ["What words signal the structure?", "What shape would you draw to organize these ideas?", "Why did the author choose this structure for this purpose?", "Does the text mix structures?"],
 "misconceptions": ["Choosing a structure from one signal word without looking at the whole passage.", "Confusing sequence with cause and effect because both use time words.", "Thinking a text can have only one structure."],
 "support": ["Provide a signal word bank on a card.", "Give pre-drawn organizers for each structure.", "Start with very short passages of three sentences."],
 "challenge": ["Find a news article that mixes three structures and label each part.", "Write the same 50-word set of facts in all five structures."],
 "background": "<p>All four passages are original to KCE. Passage A: Diop published Nations nègres et culture in 1954 and founded the IFAN radiocarbon laboratory in Dakar in 1966; the University of Dakar was renamed in 1987, the year after his death. Passage B reflects Florida DEP and water management district information about the Floridan Aquifer, spring flow and nutrient pollution. Passage C connects to Social Studies Weeks 8 and 9 (Kush and Meroe). Passage D reflects the global shift from kerosene to solar lanterns in off-grid communities.</p>",
 "sources": ["Florida Department of Environmental Protection: Florida's springs and the Floridan Aquifer.", "UNESCO General History of Africa, Volume II.", "World Health Organization: household air pollution from kerosene lamps."]
}

PRINT = {
 "directions": "Use complete sentences.",
 "items": [
  {"q":"Name the five text structures and two signal words for each.","a":"Sequence (first, then); cause and effect (because, as a result); compare and contrast (both, however); problem and solution (problem, solution); description (for example, such as).","lines":4},
  {"q":"Read: \"Because the Nile flooded every year, the soil stayed rich. As a result, farmers grew extra grain.\" What is the structure? How do you know?","a":"Cause and effect; signal words because and as a result.","lines":2},
  {"q":"Write two sentences comparing Florida's springs and the Nile flood as water sources, using two compare-and-contrast signal words.","a":"For example: Both Florida's springs and the Nile flood supply fresh water. However, the springs flow from underground all year, while the Nile flood came once a year.","lines":2},
  {"q":"Write the steps Cheikh Anta Diop took to build and share his evidence, using four sequence signal words.","a":"For example: First, in 1954, he published his book. Next, he built a radiocarbon laboratory in Dakar. Then, in 1974, he presented his evidence at UNESCO. Finally, the University of Dakar was renamed for him.","lines":3},
  {"q":"Write a word with each root and its meaning: sequ ____ dict ____ fer ____ ven ____","a":"sequence (follow); predict (say); transfer (carry); event (come)","lines":2},
  {"q":"Which structure would you use to explain how to plant a garden? Why?","a":"Sequence, because planting happens in steps in a certain order.","lines":2}]
}
