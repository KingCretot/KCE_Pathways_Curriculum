ARTICLE = ("<div class='card'><h3 style='margin-top:0'>Brave Bessie: The Pilot Who Learned French to Fly</h3>"
 "<p><b>[1]</b> In 1921, a young woman from Texas did something no American flight school would let her do. Bessie Coleman, whose father had Choctaw or Cherokee ancestors, became the first African American woman and the first woman of Native American descent to earn a pilot's license. To do it, she had to cross an ocean and learn a new language.</p>"
 "<p><b>[2]</b> Coleman was born in 1892 in Atlanta, Texas, one of thirteen children. She picked cotton with her family and walked miles to a one-room school. She loved math and saved her money to attend college in Oklahoma, but after one term the money ran out. In 1915, she moved to Chicago and worked as a manicurist in a barbershop.</p>"
 "<p><b>[3]</b> In the barbershop, Coleman heard soldiers back from World War I tell stories about flying. She decided she would fly, too. Every flight school she contacted turned her down because she was Black and a woman. Robert Abbott, the publisher of the <i>Chicago Defender</i> newspaper, told her that French flight schools were more welcoming. So Coleman studied French at night, saved her pay and found supporters to help with the cost.</p>"
 "<p><b>[4]</b> In late 1920, she sailed to France. At a flight school near the coast, she trained in a fragile biplane for about seven months. She watched a fellow student die in a crash, but she kept going. On June 15, 1921, she received her international pilot's license.</p>"
 "<p><b>[5]</b> Back in the United States, Coleman became a famous stunt pilot. Crowds gasped as she flew loops and figure eights. Newspapers called her \"Queen Bess.\" She used her fame to fight unfairness: when she learned that Black and white spectators would have to enter a show in her hometown of Waxahachie, Texas, through separate gates, she refused to fly until everyone could use the same gate. She dreamed of opening a flight school so that other Black Americans would not have to leave the country to learn.</p>"
 "<p><b>[6]</b> That dream ended suddenly. On April 30, 1926, in Jacksonville, Florida, Coleman was practicing for an air show when a loose wrench jammed the plane's controls. The plane flipped, and she fell to her death. She was 34. Thousands of people attended her memorial services.</p>"
 "<p><b>[7]</b> Coleman's dream outlived her. In 1929, William J. Powell founded the Bessie Coleman Aero Club in Los Angeles to train Black pilots. Some of the pilots who learned to fly in the years after her death went on to serve with the Tuskegee Airmen in World War II. In 1995, the U.S. Postal Service honored her with a stamp. Today, pilots fly over her grave near Chicago each year to drop flowers.</p></div>")

STEPS = ('<svg viewBox="0 0 640 170" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Four steps to summarize without copying">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Summarize without copying: four steps</text>'
  + ''.join(f'<rect x="{12+i*157}" y="36" width="147" height="120" rx="10" fill="{c}"/><text x="{85+i*157}" y="62" text-anchor="middle" fill="#fff" font-weight="bold" font-size="14">{n}</text>'
            + ''.join(f'<text x="{85+i*157}" y="{86+j*17}" text-anchor="middle" fill="#fff">{t}</text>' for j, t in enumerate(lines))
            for i, (c, n, lines) in enumerate([("#0A1F3D", "1. Read", ["Read the whole text.", "Find the central idea", "(Week 6)."]),
                                               ("#0047BA", "2. Choose", ["Pick 3 or 4 key", "points. Skip small", "details and examples."]),
                                               ("#C9A84C", "3. Cover", ["Cover the text.", "Write the points", "in your own words."]),
                                               ("#DB2F30", "4. Check", ["Compare with the text.", "No 4+ words copied", "in a row? No opinions?"])])) +
  '</svg>')

LESSON = {'unit': 'Unit 2: Explaining the World (Informational)',
 'title': 'Summarizing Without Copying',
 'subtitle': "A good summary is short, accurate, objective and written in your own words. It proves you understood the text, and it keeps you from copying someone else's work.",
 'objectives': ['Explain what makes a summary objective, brief and accurate.',
                'Separate key points from minor details.',
                'Paraphrase sentences by changing words and sentence structure, not just swapping synonyms.',
                'Spot copied wording and explain why copying without credit is plagiarism.',
                'Write a 60- to 80-word objective summary of an informational article.'],
 'vocab': [['summary', 'A short restatement of the central idea and key points of a text, in your own words.'],
           ['paraphrase', 'To restate one idea or passage in your own words and sentence structure.'],
           ['objective', 'Based on facts in the text, without your opinions or feelings.'],
           ['key point', 'An important idea that supports the central idea.'],
           ['minor detail', 'A small fact, example or description that is interesting but not essential.'],
           ['plagiarism', "Presenting someone else's words or ideas as your own without giving credit."],
           ['roots aero, naut, astro, nav', 'aero = air (aerial, aeronautics); naut = sailor (nautical, astronaut); astro = star (astronomy, astronaut); nav = ship (navy, navigate).']],
 'reconnect': {'title': 'Week 7: Text structures',
               'intro': 'Knowing how a text is organized makes it easier to summarize. Review first.',
               'items': [{'t': 'open',
                          'key': 'rc_struct',
                          'q': 'Name the five text structures from last week and one signal word for each.',
                          'min': 15,
                          'rows': 3,
                          'rubric': ['Sequence, cause and effect, compare and contrast, problem and solution, description, each with an accurate signal word'],
                          'model': 'Sequence (first), cause and effect (because), compare and contrast (however), problem and solution (one solution), description (for example).'},
                         {'t': 'text',
                          'q': '"Because the money ran out, she had to leave college after one term." Which text structure do these signal words show?',
                          'a': [{'all': [['cause'], ['effect']], 'none': ['not', 'no', 'compare', 'sequence', 'problem', 'description']}],
                          'show': 'cause and effect',
                          'pts': 2,
                          'why': '"Because" signals cause and effect: the money running out caused her to leave.'},
                         {'t': 'open',
                          'key': 'rc_central',
                          'q': 'In Week 6 you learned that a central idea is different from a topic. Explain the difference with an example.',
                          'min': 15,
                          'rows': 2,
                          'rubric': ['Topic: a word or phrase (what it is about)', 'Central idea: a full sentence telling the main point about the topic'],
                          'model': 'A topic is a word or phrase, like "the Great Green Wall." The central idea is a sentence about it, like "The Great Green Wall changed from planting a line of '
                                   'trees to helping farmers restore their own land."'}]},
 'hook': {'title': 'Tell It Short',
          'html': "<p>Your friend missed a movie and asks what happened. You don't recite every line, and you don't describe every scene. You tell the most important events in a minute or two, in "
                  "your own words. That is a <b>summary</b>.</p><p>Summaries are everywhere: the back of a book, a news alert, a doctor's notes, a research paper's abstract. In school, summarizing "
                  "shows that you understood what you read. In research, it lets you use other people's ideas honestly, without copying their words.</p><div class='callout'><b>Today's text:</b> an "
                  'article about Bessie Coleman, who learned French so she could become a pilot. You will read it, then learn to shrink it to about 70 words without copying.</div>'},
 'learn': [{'title': 'Read the Article',
            'html': "<div class='card'><h3 style='margin-top:0'>Brave Bessie: The Pilot Who Learned French to Fly</h3><p><b>[1]</b> In 1921, a young woman from Texas did something no American flight "
                    "school would let her do. Bessie Coleman, whose father had Choctaw or Cherokee ancestors, became the first African American woman and the first woman of Native American descent to earn a pilot's license. To do it, she had to "
                    'cross an ocean and learn a new language.</p><p><b>[2]</b> Coleman was born in 1892 in Atlanta, Texas, one of thirteen children. She picked cotton with her family and walked '
                    'miles to a one-room school. She loved math and saved her money to attend college in Oklahoma, but after one term the money ran out. In 1915, she moved to Chicago and worked as a '
                    'manicurist in a barbershop.</p><p><b>[3]</b> In the barbershop, Coleman heard soldiers back from World War I tell stories about flying. She decided she would fly, too. Every '
                    'flight school she contacted turned her down because she was Black and a woman. Robert Abbott, the publisher of the <i>Chicago Defender</i> newspaper, told her that French flight '
                    'schools were more welcoming. So Coleman studied French at night, saved her pay and found supporters to help with the cost.</p><p><b>[4]</b> In late 1920, she sailed to France. '
                    'At a flight school near the coast, she trained in a fragile biplane for about seven months. She watched a fellow student die in a crash, but she kept going. On June 15, 1921, '
                    "she received her international pilot's license.</p><p><b>[5]</b> Back in the United States, Coleman became a famous stunt pilot. Crowds gasped as she flew loops and figure "
                    'eights. Newspapers called her "Queen Bess." She used her fame to fight unfairness: when she learned that Black and white spectators would have to enter a show in her hometown of '
                    'Waxahachie, Texas, through separate gates, she refused to fly until everyone could use the same gate. She dreamed of opening a flight school so that other Black Americans would '
                    'not have to leave the country to learn.</p><p><b>[6]</b> That dream ended suddenly. On April 30, 1926, in Jacksonville, Florida, Coleman was practicing for an air show when a '
                    "loose wrench jammed the plane's controls. The plane flipped, and she fell to her death. She was 34. Thousands of people attended her memorial services.</p><p><b>[7]</b> "
                    "Coleman's dream outlived her. In 1929, William J. Powell founded the Bessie Coleman Aero Club in Los Angeles to train Black pilots. Some of the pilots who learned to fly in the "
                    'years after her death went on to serve with the Tuskegee Airmen in World War II. In 1995, the U.S. Postal Service honored her with a stamp. Today, pilots fly over her grave near '
                    'Chicago each year to drop flowers.</p></div><p>Read the whole article once for meaning. Then read it again with a pencil, and mark the one sentence in each paragraph that '
                    "matters most.</p><div class='callout'><b>Roots for flight:</b> <b>aero</b> = air (aerial, aeronautics) · <b>naut</b> = sailor (nautical, astronaut) · <b>astro</b> = star "
                    '(astronomy, astronaut) · <b>nav</b> = ship (navy, navigate). The language of flight borrowed from sailing: pilots <i>navigate</i>, and the science of flight is '
                    '<i>aeronautics</i>, "sailing the air."</div>',
            'checks': [{'t': 'open',
                        'key': 'central',
                        'q': 'Write the central idea of the article in one sentence. Remember: a central idea is a full sentence, not a topic.',
                        'min': 15,
                        'rows': 2,
                        'rubric': ['Bessie Coleman overcame racism and sexism (learning French, going to France) to become the first Black woman pilot and inspired others'],
                        'model': "Bessie Coleman overcame racism and sexism by learning French and training in France to become the first Black woman to earn a pilot's license, and her courage "
                                 'opened the way for other Black pilots.'},
                       {'t': 'open',
                        'key': 'structure',
                        'q': 'Most of the article follows one text structure from last week. Which one, and what clues show it?',
                        'min': 14,
                        'rows': 2,
                        'rubric': ['Sequence or chronological', 'Clues: dates and years in order (1892, 1915, 1920, 1921, 1926, 1929, 1995), words like back, then'],
                        'model': 'Sequence, because it tells her life in time order with dates like 1892, 1915, 1921 and 1926.'},
                       {'t': 'blanks',
                        'q': 'Use the roots aero, naut, astro and nav to complete the sentences.',
                        'sent': 'The science of flight is ___ (aero + naut). A space traveler, a "star sailor," is an ___. To steer a ship or plane along a route is to ___.',
                        'blanks': [['aeronautics'], ['astronaut'], ['navigate']],
                        'show': 'aeronautics; astronaut; navigate',
                        'pts': 3,
                        'why': 'aero (air) + naut (sailor) = sailing the air; astro (star) + naut (sailor) = star sailor; nav (ship, Latin navis) + igate (from agere, to drive) = to drive a ship.'}]},
           {'title': 'Key Points or Minor Details?',
            'visual': '<svg viewBox="0 0 640 170" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Four steps to summarize without copying"><text x="320" '
                      'y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Summarize without copying: four steps</text><rect x="12" y="36" width="147" height="120" rx="10" '
                      'fill="#0A1F3D"/><text x="85" y="62" text-anchor="middle" fill="#fff" font-weight="bold" font-size="14">1. Read</text><text x="85" y="86" text-anchor="middle" fill="#fff">Read '
                      'the whole text.</text><text x="85" y="103" text-anchor="middle" fill="#fff">Find the central idea</text><text x="85" y="120" text-anchor="middle" fill="#fff">(Week '
                      '6).</text><rect x="169" y="36" width="147" height="120" rx="10" fill="#0047BA"/><text x="242" y="62" text-anchor="middle" fill="#fff" font-weight="bold" font-size="14">2. '
                      'Choose</text><text x="242" y="86" text-anchor="middle" fill="#fff">Pick 3 or 4 key</text><text x="242" y="103" text-anchor="middle" fill="#fff">points. Skip small</text><text '
                      'x="242" y="120" text-anchor="middle" fill="#fff">details and examples.</text><rect x="326" y="36" width="147" height="120" rx="10" fill="#C9A84C"/><text x="399" y="62" '
                      'text-anchor="middle" fill="#fff" font-weight="bold" font-size="14">3. Cover</text><text x="399" y="86" text-anchor="middle" fill="#fff">Cover the text.</text><text x="399" '
                      'y="103" text-anchor="middle" fill="#fff">Write the points</text><text x="399" y="120" text-anchor="middle" fill="#fff">in your own words.</text><rect x="483" y="36" '
                      'width="147" height="120" rx="10" fill="#DB2F30"/><text x="556" y="62" text-anchor="middle" fill="#fff" font-weight="bold" font-size="14">4. Check</text><text x="556" y="86" '
                      'text-anchor="middle" fill="#fff">Compare with the text.</text><text x="556" y="103" text-anchor="middle" fill="#fff">No 4+ words copied</text><text x="556" y="120" '
                      'text-anchor="middle" fill="#fff">in a row? No opinions?</text></svg>',
            'html': '<p>A summary keeps the <b>key points</b> that support the central idea and leaves out <b>minor details</b>. Ask: if I removed this, would the reader still understand the main '
                    'story? If yes, it is probably a minor detail.</p><p>For example, "Coleman was one of thirteen children" is interesting, but the article\'s main story still makes sense without '
                    'it. "Every flight school she contacted turned her down because she was Black and a woman" is a key point: it explains why she went to France.</p><p>A summary is also '
                    '<b>objective</b>. It does not include your opinions ("She was the coolest pilot ever") or new facts that are not in the text.</p>',
            'checks': [{'t': 'text',
                        'q': 'Which two statements are key points? Type only their numbers. (1) She worked as a manicurist in a barbershop. (2) She learned French and trained in France because U.S. '
                             'schools refused her. (3) Newspapers called her "Queen Bess." (4) She died in a crash in 1926 before she could open her flight school.',
                        'a': [{'all': [['2'], ['4']], 'none': ['1', '3']}],
                        'show': '2 and 4',
                        'pts': 2,
                        'why': '2 and 4 explain how she overcame refusal and why her dream ended; 1 and 3 are interesting, but the story makes sense without them.'},
                       {'t': 'open',
                        'key': 'opinion',
                        'q': 'Find the two sentences that do not belong in an objective summary, and explain why: "Bessie Coleman earned her pilot\'s license in France in 1921. I think she was '
                             'braver than any pilot today. She refused to perform at a show with separate entrances. She also invented the loop-the-loop."',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['"I think she was braver..." is an opinion', '"She invented the loop-the-loop" is not in the text (and is not true)'],
                        'model': '"I think she was braver than any pilot today" is an opinion, so it is not objective. "She invented the loop-the-loop" is not in the article, and a summary must not '
                                 'add facts that are not in the text.'},
                       {'t': 'open',
                        'key': 'para7',
                        'q': "Paragraph 7 has four details. Write one sentence that sums up the paragraph's key point without listing every detail.",
                        'min': 12,
                        'rows': 2,
                        'rubric': ['Her dream lived on: others trained Black pilots and honored her after her death (one sentence, not a list)'],
                        'model': "After her death, Coleman's dream lived on as others trained Black pilots in her name and honored her memory."}]},
           {'title': "Paraphrase, Don't Patch",
            'html': '<p>Some students "patch" a summary: they copy a sentence and swap a few words for synonyms. That is still copying, because the structure and most of the words belong to the '
                    'author.</p><div class=\'callout\'><b>Original:</b> "Every flight school she contacted turned her down because she was Black and a woman."<br><b>Patchwork (still copying):</b> '
                    '"Every flying school she reached turned her down because she was Black and female."<br><b>True paraphrase:</b> "American schools refused to teach her to fly due to racism and '
                    'sexism."</div><p>To paraphrase well:</p><ul><li>Cover the text, then say the idea out loud in your own words.</li><li>Change the sentence structure: start with a different part, '
                    'combine sentences or split one.</li><li>Use your own words, but keep names, dates and special terms ("pilot\'s license") that have no good substitute.</li><li><b>The 4-word '
                    "check:</b> if 4 or more words in a row match the original, rewrite them or put them in quotation marks and credit the author.</li></ul><p>Copying an author's words or ideas "
                    'without credit is <b>plagiarism</b>. Next week you will learn how to give credit with citations.</p>',
            'checks': [{'t': 'num',
                        'q': 'Original: "She used her fame to fight unfairness." A student wrote: "She used her fame to battle injustice." Use the 4-word check: how many words in a row did the '
                             'student copy?',
                        'a': 5,
                        'unit': 'words',
                        'pts': 2,
                        'why': '"She used her fame to" is 5 words in a row, and the structure is the same with two synonyms swapped. That is patchwriting, not a paraphrase.'},
                       {'t': 'open',
                        'key': 'para1',
                        'q': 'Paraphrase this sentence. Change both the words and the structure: "So Coleman studied French at night, saved her pay and found supporters to help with the cost."',
                        'min': 12,
                        'rows': 2,
                        'rubric': ['Same meaning (learned French, saved money, got financial help)', 'Different structure and wording; no 4 words in a row copied'],
                        'model': 'To pay for the trip and prepare for school in France, Coleman took evening French classes, put money aside and got help from backers.'},
                       {'t': 'open',
                        'key': 'para2',
                        'q': 'Paraphrase: "She dreamed of opening a flight school so that other Black Americans would not have to leave the country to learn."',
                        'min': 12,
                        'rows': 2,
                        'rubric': ['Same meaning', 'Different structure and wording; no 4 words in a row copied'],
                        'model': 'Coleman hoped to start a school in the United States where Black students could learn to fly without traveling abroad as she had.'}]},
           {'title': 'Write and Check a Summary',
            'html': '<p>A strong summary of an informational article usually has:</p><ul><li>A first sentence with the <b>title, author (if known) and central idea</b>.</li><li><b>Two to four '
                    "sentences</b> with the key points, in a logical order.</li><li>No opinions, no minor details and no copied strings of words.</li></ul><div class='callout'><b>Sample opening:</b> "
                    'The article "Brave Bessie: The Pilot Who Learned French to Fly" explains how Bessie Coleman overcame racism and sexism to become the first African American woman '
                    'pilot.</div><p>After writing, check: Is it shorter than one paragraph of the original? Could a reader who never saw the article understand the main story? Does any phrase match '
                    'the original word for word?</p>',
            'checks': [{'t': 'open',
                        'key': 'summary',
                        'q': 'Write a 60- to 80-word summary of the article. Start with the title and central idea. Then cover the text and write the key points in your own words.',
                        'min': 60,
                        'rows': 7,
                        'rubric': ['Opens with title and central idea',
                                   'Includes key points in order: refusal in the U.S., learning French and training in France, 1921 license, stunt flying and fighting segregation, 1926 death, legacy',
                                   'Objective: no opinions or added facts',
                                   'In own words: no 4 or more words in a row copied',
                                   '60 to 80 words'],
                        'model': 'The article "Brave Bessie: The Pilot Who Learned French to Fly" explains how Bessie Coleman overcame racism and sexism to become the first African American woman '
                                 'pilot. Because American schools would not teach her, she learned French and trained in France, earning her license in 1921. Back home, she performed daring air '
                                 'shows and refused to fly before segregated crowds. She died in a 1926 crash, but others later trained Black pilots in her honor.'},
                       {'t': 'open',
                        'key': 'selfcheck',
                        'q': 'Check your summary. Name one phrase you rewrote because it was too close to the original, and one detail you chose to leave out. Why did you leave it out?',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Names a specific phrase revised', 'Names a minor detail left out with a reason tied to the central idea'],
                        'model': 'I first wrote "turned her down because she was Black and a woman," which copied the article, so I changed it to "would not teach her." I left out that she was a '
                                 'manicurist because it does not explain how she became a pilot.'}]}],
 'handson': {'title': 'Summary Shrink Ray',
             'intro': 'Shrink a text from home step by step, and feel how a summary keeps only what matters.',
             'materials': ['A short news article, encyclopedia entry or magazine piece (about 300 to 500 words) from home or the library',
                           'Sticky notes or small strips of paper',
                           'A timer',
                           'Index cards in three sizes, or paper cut into large, medium and small pieces'],
             'steps': ['Read the article. On a sticky note for each paragraph, write its key point in 5 words or fewer. Put the article away.',
                       'Using only your sticky notes, write a summary on the large card (about 100 words).',
                       'Shrink it: rewrite it on the medium card in about 50 words. Cross out anything that is a minor detail.',
                       'Shrink it again: write a one-sentence summary (about 20 words) on the small card.',
                       'Read your one-sentence version to a family member who has not read the article. Can they tell you what it was about?'],
             'record': [{'t': 'open',
                         'key': 'shrinkcards',
                         'q': "Copy your three summaries (100, 50 and 20 words) here, with the article's title and source.",
                         'min': 80,
                         'rows': 8,
                         'rubric': ['Three summaries of decreasing length', 'Each keeps the central idea', 'In own words', 'Title and source named'],
                         'model': 'Article: "Florida\'s Manatees Are Making a Comeback" (local newspaper). 100 words: The article explains why fewer manatees are dying in Florida after the record '
                                  'losses of 2021. Polluted water had fed algae blooms that blocked sunlight, so the seagrass manatees eat died and many manatees starved. Since then, scientists and '
                                  'volunteers have replanted seagrass in lagoons, and towns have worked to cut the fertilizer and sewage that feed the algae. Wildlife workers also fed some hungry '
                                  'manatees lettuce during two winters while the seagrass recovered. The article says deaths have dropped, but manatees still face boat strikes, cold snaps and lost '
                                  'habitat, so the work must continue. 50 words: Fewer Florida manatees are dying since the record losses of 2021, when algae blocked sunlight and killed the seagrass '
                                  'they eat. People have replanted seagrass, cut pollution and fed hungry manatees lettuce. Deaths have dropped, but boats, cold weather and lost habitat still '
                                  'threaten them. 20 words: Fewer manatees are dying in Florida because seagrass is being replanted and pollution is being cut, but they still face dangers.'},
                        {'t': 'open',
                         'key': 'shrinkcut',
                         'q': 'What did you cut each time you shrank your summary? What stayed in all three, and why?',
                         'min': 26,
                         'rows': 3,
                         'rubric': ['Names what was cut at each step (examples, numbers, quotes)', 'The central idea stayed because everything else supports it'],
                         'model': 'First I cut the quotes and the exact numbers. Then I cut the examples of each cause. The central idea stayed in all three because every other detail only supports '
                                  'it.'}]},
 'think': {'intro': 'Write in complete sentences. Your teacher scores these.',
           'items': [{'t': 'open',
                      'key': 'whymatters',
                      'q': 'Explain why copying a summary from a website, even with a few words changed, is unfair to the author and harmful to the student. Give at least two reasons.',
                      'min': 50,
                      'rows': 5,
                      'rubric': ['Unfair to the author: takes credit for their words and work',
                                 'Harms the student: does not build understanding or skill; dishonest; real consequences in school and work',
                                 'Clear explanation'],
                      'model': 'Copying is unfair to the author because it takes credit for words and ideas they worked to create. It also hurts the student: writing a summary is how you prove and '
                               'build your understanding, so a copied summary teaches you nothing. In school and at work, plagiarism can lead to failing grades or losing trust, and a paraphrase with '
                               'a few swapped words is still copying.'},
                     {'t': 'open',
                      'key': 'connect',
                      'q': 'Bessie Coleman learned French to reach her goal. Write a short paragraph explaining how learning another language opened a door for her, and describe one way a second '
                           'language could open a door for you.',
                      'min': 48,
                      'rows': 6,
                      'rubric': ['Accurate: she learned French because French schools would train her, which U.S. schools would not', 'A thoughtful personal connection', 'Clear paragraph'],
                      'model': 'American flight schools refused Bessie Coleman, but French schools would train her, so learning French gave her the key to her goal. Without it, she could not have '
                               'taken classes or passed her tests in France. For me, learning Spanish could let me talk with my neighbors and someday work as a nurse in a bilingual hospital.'}]},
 'exit': [{'t': 'blanks',
           'q': 'Complete the definition.',
           'sent': 'A good summary is short, keeps the central idea and key points, is ___ (no opinions), and is written in your own ___.',
           'blanks': [['objective', 'factual'], ['words']],
           'show': 'objective; words',
           'pts': 2,
           'why': 'A summary is objective and in your own words.'},
          {'t': 'open',
           'key': 'exit_para',
           'q': 'Paraphrase: "Crowds gasped as she flew loops and figure eights."',
           'min': 8,
           'rows': 2,
           'rubric': ['Same meaning', 'Different wording and structure, no 4 words in a row copied'],
           'model': 'Her daring stunts in the air amazed the people watching.'},
          {'t': 'text',
           'q': "What is the word for presenting someone else's words or ideas as your own?",
           'a': ['plagiarism', 'plagiarizing'],
           'show': 'plagiarism',
           'pts': 2,
           'why': 'Plagiarism. Next week: how to give credit with citations.'},
          {'t': 'open',
           'key': 'exit_minor',
           'q': 'Name one minor detail from the article and explain why it does not belong in a short summary.',
           'min': 12,
           'rows': 2,
           'rubric': ['A real minor detail (13 children, manicurist, Queen Bess, the stamp, flowers dropped on her grave)', 'Reason: the main story makes sense without it'],
           'model': 'She was one of thirteen children. It is interesting, but the story of how she became a pilot makes sense without it.'}],
 'next': 'Week 9: taking research notes from more than one source and giving credit with citations.'}

TEACHER = {
 "standards": [
  "ELA.6.R.2.2: Analyze the central idea(s), implied or explicit, and its development throughout a text.",
  "ELA.6.R.3.2: Paraphrase content from grade-level texts.",
  "ELA.6.C.4.1: Conduct research to answer a question, drawing on multiple reliable and valid sources, and refocusing the inquiry when appropriate (preview).",
  "ELA.6.V.1.2: Apply knowledge of Greek and Latin roots and affixes to determine meanings of words and phrases in grade-level content.",
  "ELA.K12.EE.1.1: Cite evidence to explain and justify reasoning."],
 "materials": ["The interactive lesson", "A pencil and highlighter", "Sticky notes, index cards in three sizes and a timer", "A short article from home or the library", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 7 Reconnect questions."],
  [4, "Hook", "Ask the student to summarize a favorite movie in one minute. Notice what they leave out."],
  [12, "Read", "The student reads the article twice, marking one key sentence per paragraph."],
  [10, "Key points", "Sort key points and minor details aloud. Remove the opinion and the invented fact."],
  [12, "Paraphrase", "Model the patchwriting example, then the 4-word check. Have the student paraphrase with the text covered."],
  [12, "Write", "The student drafts the summary, then checks it against the article."],
  [4, "Assign", "Assign the Summary Shrink Ray and Think Deeper."]],
 "key_questions": ["If you removed this detail, would the reader still understand?", "Is this the author's idea or your opinion?", "Which words came straight from the text?", "Could someone who never read it understand your summary?"],
 "misconceptions": ["Swapping synonyms makes a sentence your own.", "A summary retells everything in order.", "Adding your opinion makes a summary better.", "Plagiarism only means copying whole paragraphs."],
 "support": ["Provide a summary frame: The article ___ explains how ___. First, ___. Then ___. Finally, ___.", "Let the student say the summary aloud before writing.", "Highlight copied 4-word strings for the student to rewrite."],
 "challenge": ["Write a 25-word summary and a 100-word summary and compare what changed.", "Compare the article with a biography of Bessie Coleman from the library: what details does each include or leave out?"],
 "background": "<p>The article is original, written for this lesson from established facts. Bessie Coleman (January 26, 1892 to April 30, 1926) was born in Atlanta, Texas, attended the Colored Agricultural and Normal University in Langston, Oklahoma, for one term, and moved to Chicago around 1915 to 1916. Encouraged by Robert S. Abbott of the Chicago Defender, she studied French and trained at the Caudron brothers' school at Le Crotoy, receiving her license from the Fédération Aéronautique Internationale on June 15, 1921. Her refusal to perform in Waxahachie, Texas, until Black and white spectators could use the same entrance is documented (Smithsonian National Air and Space Museum; Doris L. Rich, Queen Bess, 1993). She died in Jacksonville when a loose wrench jammed the controls of her Curtiss JN-4; her mechanic and publicity agent William Wills also died. William J. Powell founded the Bessie Coleman Aero Club in Los Angeles in 1929. The USPS Black Heritage stamp was issued in 1995. The 4-word check is a teaching heuristic, not a formal rule; teach it as a warning sign. Paragraphs 4 and 6 describe a classmate's death and Coleman's fatal crash plainly. Read them with the student, pause and invite questions. Name racism and sexism as unjust, and connect them to her courage.</p>",
 "sources": ["Rich, D. L. (1993), Queen Bess: Daredevil Aviator, Smithsonian Institution Press.", "Smithsonian National Air and Space Museum, Bessie Coleman.", "National Women's History Museum, Bessie Coleman biography.", "CPALMS, ELA.6.R.2.2, ELA.6.R.3.2 and ELA.6.V.1.2."]
}

PRINT = {
 "directions": "Write in complete sentences, in your own words.",
 "items": [
  {"q":"What is the central idea of \"Brave Bessie\"?","a":"Bessie Coleman overcame racism and sexism by learning French and training in France to become the first Black woman to earn a pilot's license, opening the way for others.","lines":2},
  {"q":"Name two key points and two minor details from the article.","a":"Key: U.S. schools refused her; she earned her license in France in 1921; she died in 1926. Minor: thirteen children; manicurist; Queen Bess.","lines":3},
  {"q":"Paraphrase: \"In late 1920, she sailed to France.\"","a":"Coleman crossed the Atlantic by ship near the end of 1920 to train in France.","lines":2},
  {"q":"Explain the difference between paraphrasing and patchwriting.","a":"Paraphrasing changes words and structure; patchwriting keeps the author's structure and swaps a few words.","lines":2},
  {"q":"Write a 40-word summary of the article.","a":"The article \"Brave Bessie\" explains how Bessie Coleman, refused by American flight schools, learned French, trained in France and earned her pilot's license in 1921. She became a stunt pilot who fought segregation, died in 1926, and inspired Black pilots.","lines":4},
  {"q":"Use the roots: what do aerial and nautical mean, and what root do navy and navigate share?","a":"aerial = of the air (aero); nautical = having to do with sailors or ships (naut); navy and navigate share nav = ship.","lines":2}]
}
