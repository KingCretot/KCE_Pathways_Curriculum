PASSAGE = ("<div class='cp-text'><div class=\"card\" style=\"border-left-color:#0047BA\"><h3>Why the Ground Opens Up in Florida</h3><p class=\"muted\">An original article by KingCretot Experience · KCE Practice Reader, 2026</p>"
 "<p><b>[1]</b> On a May evening in 1981, a sinkhole opened in Winter Park, Florida. Over the next day it grew to about 350 feet wide and 75 feet deep, swallowing a house, several cars and part of a city swimming pool. Television crews from around the world came to watch. To many viewers, it looked like the earth itself was collapsing.</p>"
 "<p><b>[2]</b> Sinkholes are common in Florida because of what lies beneath the state. Much of Florida sits on thick layers of limestone, a rock made long ago from the shells and skeletons of sea creatures. Rainwater picks up carbon dioxide from the air and soil, which makes it slightly acidic. As this water seeps underground over thousands of years, it slowly dissolves the limestone, leaving cracks, tunnels and caves.</p>"
 "<p><b>[3]</b> Usually, groundwater fills these spaces and helps hold up the soil above. When the water level drops, however, the support disappears. Then the sand and clay on top can sag slowly or collapse all at once. Droughts can lower the water level, and so can heavy pumping of groundwater. In January 2010, farmers near Plant City pumped huge amounts of water to spray on their strawberries and protect them from a freeze. As a result, the water level dropped sharply, and dozens of sinkholes opened in the area.</p>"
 "<p><b>[4]</b> Not all sinkholes are disasters. Some formed long ago and have become beautiful natural places. At Devil's Millhopper Geological State Park near Gainesville, visitors walk down a staircase into a sinkhole about 120 feet deep, where small waterfalls trickle down the green walls. Many of Florida's crystal-clear springs also flow from openings in the limestone.</p>"
 "<p><b>[5]</b> Scientists cannot predict exactly where the next sinkhole will open, but they can map areas at higher risk. Homeowners can watch for warning signs, such as new cracks in walls or floors, doors that suddenly stick, or a circular depression forming in the yard. Understanding the rock beneath our feet helps Floridians live safely on a landscape that is always slowly changing.</p></div></div>")

OUTLINE = ('<svg viewBox="0 0 640 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="From note cards to article outline">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">From note card groups to an article</text>'
  + ''.join(f'<rect x="{20+i*14}" y="{40+i*8}" width="120" height="70" rx="4" fill="#fffef5" stroke="{c}" stroke-width="2"/>' for i, c in enumerate(["#0047BA", "#C9A84C", "#0047BA"])) +
  '<text x="96" y="140" text-anchor="middle" font-weight="bold">Note card groups</text><text x="96" y="156" text-anchor="middle" font-size="11">(one group = one section)</text>'
  '<path d="M180 85 h40" stroke="#0A1F3D" stroke-width="2"/><path d="M216 80 l8 5 l-8 5" fill="#0A1F3D"/>'
  '<rect x="240" y="36" width="380" height="186" rx="6" fill="#fff" stroke="#0A1F3D"/>'
  + ''.join(f'<rect x="252" y="{y}" width="356" height="{h}" rx="4" fill="{c}"/><text x="262" y="{y+17}" fill="#fff" font-weight="bold">{t1}</text><text x="262" y="{y+32}" fill="#fff" font-size="11">{t2}</text>'
            for y, h, c, t1, t2 in [(46, 38, "#0A1F3D", "Title + Introduction", "hook, background, central idea (thesis)"),
                                    (90, 38, "#0047BA", "Section 1 (heading)", "topic sentence, facts with citations, explanation"),
                                    (134, 38, "#0047BA", "Section 2 (heading)", "topic sentence, facts with citations, explanation"),
                                    (178, 38, "#C9A84C", "Conclusion + Works Cited", "restate central idea, why it matters; sources")]) +
  '</svg>')

LESSON = {'unit': 'Unit 2: Explaining the World (Informational)',
 'title': 'Unit 2 Checkpoint and Informational Article Project',
 'subtitle': 'Turn your research notes into a clear, well-organized informational article with headings and citations, then show what you know on the Unit 2 checkpoint.',
 'objectives': ['Organize note card groups into an outline with an introduction, body sections and a conclusion.',
                'Write an introduction with a hook and a central idea (thesis).',
                'Write body paragraphs that combine facts from sources, with in-text citations and varied transitions.',
                'Use text features (title, headings, a visual with a caption) to help readers.',
                'Show mastery of Unit 2 on the checkpoint (85 or higher).'],
 'vocab': [['thesis', 'In an informational article, the sentence that states the central idea the whole article explains.'],
           ['text features', 'Titles, headings, captions, diagrams and bold words that help readers find and understand information.'],
           ['elaboration', 'Explaining a fact so readers understand why it matters or how it connects.'],
           ['transition', 'A word or phrase that connects ideas, such as as a result, however or for example.'],
           ['caption', 'A short sentence under a picture or diagram that explains it.']],
 'reconnect': {'title': 'Week 9: Research notes and citations',
               'intro': 'Start with last week, then sweep back through the unit.',
               'items': [{'t': 'open',
                          'key': 'rc_cardparts',
                          'q': 'Name the four parts of a research note card.',
                          'min': 10,
                          'rows': 2,
                          'rubric': ['Subtopic heading, source label, notes in own words, exact quotes in quotation marks with location'],
                          'model': 'A subtopic heading, the source label, notes in my own words, and exact words in quotation marks with the page or paragraph.'},
                         {'t': 'text',
                          'q': 'What is the MLA name for the list of sources at the end of a paper?',
                          'a': [{'all': [['works cited']], 'none': ['not']}],
                          'show': 'works cited',
                          'pts': 2,
                          'why': 'Works Cited.'},
                         {'t': 'text',
                          'q': 'Week 8: What kind of statement must a summary leave out? Type one word.',
                          'a': [{'all': [['opinion']]}],
                          'show': 'opinions',
                          'pts': 2,
                          'why': "A summary leaves out the writer's opinions."},
                         {'t': 'text',
                          'q': 'Week 7: "First, mix the soil. Next, add water. Finally, plant the seeds." Which text structure is this?',
                          'a': [{'all': [['sequence', 'chronolog', 'order', 'steps']], 'none': ['not', 'cause', 'compare', 'problem']}],
                          'show': 'sequence',
                          'pts': 2,
                          'why': 'Sequence: the signal words first, next and finally show steps in order.'},
                         {'t': 'open',
                          'key': 'rc_central',
                          'q': 'Week 6: what is the difference between a topic and a central idea?',
                          'min': 12,
                          'rows': 2,
                          'rubric': ['Topic: word or phrase naming the subject', 'Central idea: a sentence stating the main point about it'],
                          'model': 'A topic is a word or phrase naming what a text is about. A central idea is a full sentence stating the main point the author makes about that topic.'}]},
 'hook': {'title': 'From Notes to Article',
          'visual': '<svg viewBox="0 0 640 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="From note cards to article outline"><text x="320" y="20" '
                    'text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">From note card groups to an article</text><rect x="20" y="40" width="120" height="70" rx="4" fill="#fffef5" '
                    'stroke="#0047BA" stroke-width="2"/><rect x="34" y="48" width="120" height="70" rx="4" fill="#fffef5" stroke="#C9A84C" stroke-width="2"/><rect x="48" y="56" width="120" '
                    'height="70" rx="4" fill="#fffef5" stroke="#0047BA" stroke-width="2"/><text x="96" y="140" text-anchor="middle" font-weight="bold">Note card groups</text><text x="96" y="156" '
                    'text-anchor="middle" font-size="11">(one group = one section)</text><path d="M180 85 h40" stroke="#0A1F3D" stroke-width="2"/><path d="M216 80 l8 5 l-8 5" fill="#0A1F3D"/><rect '
                    'x="240" y="36" width="380" height="186" rx="6" fill="#fff" stroke="#0A1F3D"/><rect x="252" y="46" width="356" height="38" rx="4" fill="#0A1F3D"/><text x="262" y="63" fill="#fff" '
                    'font-weight="bold">Title + Introduction</text><text x="262" y="78" fill="#fff" font-size="11">hook, background, central idea (thesis)</text><rect x="252" y="90" width="356" '
                    'height="38" rx="4" fill="#0047BA"/><text x="262" y="107" fill="#fff" font-weight="bold">Section 1 (heading)</text><text x="262" y="122" fill="#fff" font-size="11">topic '
                    'sentence, facts with citations, explanation</text><rect x="252" y="134" width="356" height="38" rx="4" fill="#0047BA"/><text x="262" y="151" fill="#fff" '
                    'font-weight="bold">Section 2 (heading)</text><text x="262" y="166" fill="#fff" font-size="11">topic sentence, facts with citations, explanation</text><rect x="252" y="178" '
                    'width="356" height="38" rx="4" fill="#C9A84C"/><text x="262" y="195" fill="#fff" font-weight="bold">Conclusion + Works Cited</text><text x="262" y="210" fill="#fff" '
                    'font-size="11">restate central idea, why it matters; sources</text></svg>',
          'html': '<p>Last week you sorted your note cards into groups. Each group is already a section of your article. Now you will turn that skeleton into a finished piece that teaches a reader '
                  'something real.</p><p>Informational articles you read every day, in magazines, on museum websites and in encyclopedias, share the same parts: a title that tells the topic, an '
                  "introduction that hooks the reader and states the central idea, body sections with headings, a conclusion, and a list of sources.</p><div class='callout'><b>This week:</b> draft "
                  'and revise your Unit 2 informational article, then take the Unit 2 checkpoint.</div>'},
 'learn': [{'title': 'Outline and Introduction',
            'html': '<p>Turn each note card group into a section heading, then put the sections in the order that makes the most sense. Use a text structure from Week 7: sequence for a process, '
                    'cause and effect for why something happens, problem and solution for a challenge.</p><p>Your <b>introduction</b> has three jobs:</p><ul><li><b>Hook</b> the reader: a surprising '
                    'fact, a short scene or a question.</li><li>Give a little <b>background</b>.</li><li>State the <b>central idea</b> (thesis): one sentence that tells what the whole article will '
                    'explain.</li></ul><div class=\'callout\'><b>Sample introduction:</b> Every summer, scientists fly airplanes straight into hurricanes on purpose. These "hurricane hunters" '
                    'collect information that helps forecasters warn millions of people. Hurricanes form from warm ocean water and spinning winds, and scientists use planes, satellites and computer '
                    'models to predict where they will go.</div>',
            'checks': [{'t': 'open',
                        'key': 'myoutline',
                        'q': "Write your article's outline: title, central idea sentence, and a heading for each body section in order. Name the text structure you chose and why.",
                        'min': 40,
                        'rows': 5,
                        'rubric': ['Title and a central idea sentence that answers the research question',
                                   'Two to four section headings in logical order',
                                   'Names a fitting text structure with a reason'],
                        'model': 'Title: Into the Eye of the Storm. Central idea: Hurricanes form from warm ocean water and spinning winds, and scientists use planes, satellites and computer models '
                                 'to predict their paths. Sections: How a Hurricane Forms; Hurricane Hunters and Satellites; Staying Safe. Structure: sequence for the first section and problem and '
                                 'solution for the article overall, because hurricanes are a danger and forecasting is part of the solution.'},
                       {'t': 'open',
                        'key': 'myintro',
                        'q': 'Draft your introduction: a hook, one or two background sentences and your central idea.',
                        'min': 50,
                        'rows': 5,
                        'rubric': ['An engaging hook', 'Background', 'A clear central idea sentence'],
                        'model': 'Every summer, scientists fly airplanes straight into hurricanes on purpose. These storms are among the most powerful on Earth, and Florida faces them almost every '
                                 'year. Hurricanes form from warm ocean water and spinning winds, and scientists use planes, satellites and computer models to predict where they will go.'}]},
           {'title': 'Body Paragraphs: Facts, Citations, Elaboration',
            'html': '<p>Each body paragraph follows a pattern you can remember as <b>T-E-E-C</b>:</p><ul><li><b>T</b>opic sentence: what this section explains.</li><li><b>E</b>vidence: facts from '
                    'your note cards, with in-text citations.</li><li><b>E</b>laboration: your explanation of what the facts mean or how they connect.</li><li><b>C</b>onnection: a sentence that '
                    'links to the central idea or the next section.</li></ul><p>Use <b>varied transitions</b>: for example, in addition, as a result, however, because of this, similarly. Avoid '
                    'starting every sentence with "Also."</p><div class=\'callout\'><b>Weak:</b> Hurricanes need warm water. Also they need wind. Also they spin.<br><b>Strong:</b> Hurricanes begin '
                    'over ocean water that is at least about 80°F (Simon). As warm, moist air rises, more air rushes in to replace it, and because Earth rotates, the rushing air begins to spin. As a '
                    'result, a small storm can grow into a giant, spinning system.</div>',
            'checks': [{'t': 'open',
                        'key': 'transfix',
                        'q': 'Rewrite this paragraph with varied transitions and one sentence of elaboration: "Public libraries are important. Also they lend books. Also they offer free internet. '
                             'Also many have lost funding."',
                        'min': 40,
                        'rows': 4,
                        'rubric': ['At least two varied transitions (in addition, as a result, however)', 'One sentence of elaboration explaining why a fact matters', 'Smooth, connected sentences'],
                        'model': 'Public libraries are important to every community. They lend books, movies and e-books for free. In addition, many families without home internet depend on library '
                                 'computers and Wi-Fi, which helps students finish schoolwork. However, many libraries have lost funding in recent years.'},
                       {'t': 'open',
                        'key': 'mybody',
                        'q': 'Draft one body paragraph for your article using T-E-E-C. Include at least two facts from your note cards with in-text citations.',
                        'min': 80,
                        'rows': 7,
                        'rubric': ['Topic sentence', 'Two facts from sources with in-text citations', "Elaboration in the writer's own words", 'Connection sentence', 'Varied transitions'],
                        'model': 'Hurricane hunters fly directly into storms to collect information that cannot be gathered any other way. The planes drop sensors that measure wind speed, air '
                                 'pressure and temperature as they fall (National Weather Service). In addition, satellites photograph the storm from space every few minutes (Simon). Together, these '
                                 "measurements help computer models predict a hurricane's path. Because of this teamwork, forecasters can warn people days before a storm arrives."}]},
           {'title': 'Text Features, Conclusion and Revision',
            'html': '<p><b>Text features</b> help readers find and understand information. Your article needs a title, a heading for each body section, and at least one visual (a diagram, map, photo '
                    'you took or chart) with a <b>caption</b> that explains it.</p><p>Your <b>conclusion</b> restates the central idea in new words and tells why it matters, without adding brand-new '
                    'facts.</p><p>Before you publish, revise with ARMS (Add, Remove, Move, Substitute) and edit with CUPS (Capitals, Usage, Punctuation, Spelling) from Week 5. Then check your '
                    'citations: every borrowed fact cited, every source in the works cited list, list in alphabetical order.</p>',
            'checks': [{'t': 'open',
                        'key': 'caption',
                        'q': 'Write a caption for a visual you plan to include. A good caption says what the visual shows and why it matters.',
                        'min': 15,
                        'rows': 2,
                        'rubric': ['Says what the visual shows', 'Explains why it matters to the article'],
                        'model': "A satellite image of Hurricane Ian approaching Florida in 2022. Images like this help forecasters track a storm's size and path."},
                       {'t': 'open',
                        'key': 'myconclusion',
                        'q': 'Draft your conclusion: restate your central idea in new words and explain why it matters.',
                        'min': 40,
                        'rows': 4,
                        'rubric': ['Restates the central idea in new words', 'Explains why it matters', 'No brand-new facts'],
                        'model': "Hurricanes may be among nature's most powerful storms, but they are no longer complete surprises. Thanks to hurricane hunters, satellites and computer models, "
                                 'scientists can now warn people in time to prepare. Understanding how these storms work helps Florida families stay safe.'}]}],
 'handson': {'title': 'Publish and Share Your Article',
             'intro': 'Finish, revise and publish your informational article, then share it with a real audience.',
             'materials': ['Your note cards, outline and drafts',
                           'A computer or paper and pen for the final copy',
                           'Your visual (drawing, map, chart or photo) and caption',
                           'The Unit 2 Projects rubric',
                           'Colored pencils for the revision check'],
             'steps': ['Assemble the full draft: title, introduction, body sections with headings, conclusion, visual with caption and works cited list.',
                       'Revise with ARMS. Use one colored pencil to underline your central idea and each topic sentence: do they match?',
                       'Edit with CUPS, then check every citation against your works cited list.',
                       'Score your own article with the rubric and fix the lowest trait.',
                       'Publish a clean copy and share it with a real audience: a family member, a grandparent by video call, or the co-op. Photograph your note cards to turn in.'],
             'record': [{'t': 'open',
                         'key': 'final',
                         'q': 'Paste or type your final article here, including the works cited list (400 to 700 words).',
                         'min': 350,
                         'rows': 20,
                         'rubric': ['Meets every requirement on the Unit 2 Informational Article rubric'],
                         'model': 'Into the Eye of the Storm\n'
                                  '\n'
                                  'Every summer, scientists fly airplanes straight into hurricanes on purpose... (full article with headings, citations, a captioned visual and a works cited list)'},
                        {'t': 'open',
                         'key': 'artreflect',
                         'q': 'Reflect: Which part of the research and writing process was hardest, how did you solve it, and what did your audience learn from your article?',
                         'min': 40,
                         'rows': 4,
                         'rubric': ['Names a real challenge and how it was solved', 'Reports what the audience learned'],
                         'model': 'Taking notes in my own words was hardest because the sources explained things so well. I solved it by covering the page before writing. My grandmother said she '
                                  'never knew planes flew into hurricanes, so she learned how forecasts are made.'}]},
 'think': {'intro': 'Write in complete sentences. Your teacher scores these.',
           'items': [{'t': 'open',
                      'key': 'growth',
                      'q': 'Compare your Unit 1 personal narrative with your Unit 2 informational article. How are narrative and informational writing different in purpose, structure and language? '
                           'Use examples from your own writing.',
                      'min': 80,
                      'rows': 7,
                      'rubric': ['Purpose: tell a story and share an experience versus explain and inform',
                                 'Structure: story mountain versus introduction, sections with headings and conclusion',
                                 'Language: first person, dialogue and sensory details versus facts, citations and precise terms',
                                 "Examples from the student's own writing"],
                      'model': 'My personal narrative told the story of the day I got lost at the fair, so its purpose was to share an experience. It followed a story mountain and used first person, '
                               'dialogue and sensory details. My informational article explains how hurricanes form and are predicted, so its purpose is to teach. It uses an introduction with a '
                               'central idea, sections with headings and a conclusion, and its language is factual, with precise terms like air pressure and citations from my sources.'},
                     {'t': 'open',
                      'key': 'trust',
                      'q': 'How can a reader tell that an informational article is trustworthy? Give three features, and explain which one your own article does best.',
                      'min': 50,
                      'rows': 5,
                      'rubric': ['Three features: citations and works cited, reliable sources, accurate facts, objective tone, author or publisher named, recent date',
                                 'Identifies and explains the strongest in their article'],
                      'model': 'A trustworthy article cites its sources, uses reliable sources like government or science organizations, and stays objective instead of giving opinions. My article '
                               'does citations best, because every fact has a source in parentheses and a matching works cited entry.'}]},
 'checkpoint': {'title': 'Unit 2 Checkpoint: Explaining the World',
                'intro': 'Read the article carefully, then answer. You may look back at the text. Mastery is 85 or higher. If you score below 85, your teacher will review with you, then you will '
                         'retake it.',
                'parts': [{'title': 'Part A: Read the article',
                           'items': [{'t': 'open',
                                      'key': 'cp_central',
                                      'q': '<div class=\'cp-text\'><div class="card" style="border-left-color:#0047BA"><h3>Why the Ground Opens Up in Florida</h3><p class="muted">An original article '
                                           'by KingCretot Experience · KCE Practice Reader, 2026</p><p><b>[1]</b> On a May evening in 1981, a sinkhole opened in Winter Park, Florida. Over the next '
                                           'day it grew to about 350 feet wide and 75 feet deep, swallowing a house, several cars and part of a city swimming pool. Television crews from around the '
                                           'world came to watch. To many viewers, it looked like the earth itself was collapsing.</p><p><b>[2]</b> Sinkholes are common in Florida because of what '
                                           'lies beneath the state. Much of Florida sits on thick layers of limestone, a rock made long ago from the shells and skeletons of sea creatures. Rainwater '
                                           'picks up carbon dioxide from the air and soil, which makes it slightly acidic. As this water seeps underground over thousands of years, it slowly '
                                           'dissolves the limestone, leaving cracks, tunnels and caves.</p><p><b>[3]</b> Usually, groundwater fills these spaces and helps hold up the soil above. '
                                           'When the water level drops, however, the support disappears. Then the sand and clay on top can sag slowly or collapse all at once. Droughts can lower the '
                                           'water level, and so can heavy pumping of groundwater. In January 2010, farmers near Plant City pumped huge amounts of water to spray on their strawberries '
                                           'and protect them from a freeze. As a result, the water level dropped sharply, and dozens of sinkholes opened in the area.</p><p><b>[4]</b> Not all '
                                           "sinkholes are disasters. Some formed long ago and have become beautiful natural places. At Devil's Millhopper Geological State Park near Gainesville, "
                                           "visitors walk down a staircase into a sinkhole about 120 feet deep, where small waterfalls trickle down the green walls. Many of Florida's crystal-clear "
                                           'springs also flow from openings in the limestone.</p><p><b>[5]</b> Scientists cannot predict exactly where the next sinkhole will open, but they can map '
                                           'areas at higher risk. Homeowners can watch for warning signs, such as new cracks in walls or floors, doors that suddenly stick, or a circular depression '
                                           'forming in the yard. Understanding the rock beneath our feet helps Floridians live safely on a landscape that is always slowly '
                                           'changing.</p></div></div>What is the central idea of the article? Write it as one sentence.',
                                      'min': 15,
                                      'rows': 2,
                                      'pts': 4,
                                      'rubric': ["Florida's limestone, dissolved by slightly acidic water, makes sinkholes common; understanding this helps people live safely (a full sentence about "
                                                 'the topic, not just "sinkholes")'],
                                      'model': 'Sinkholes are common in Florida because acidic water dissolves the limestone underground, and understanding this helps people stay safe.'},
                                     {'t': 'text',
                                      'q': 'Which text structure does paragraph 3 mainly use?',
                                      'a': [{'all': [['cause', 'effect']], 'none': ['not', 'compare', 'sequence']}],
                                      'show': 'cause and effect',
                                      'pts': 2,
                                      'why': 'Paragraph 3 explains causes (the water level drops, pumping) and effects (the soil collapses). "As a result" signals cause and effect.'},
                                     {'t': 'open',
                                      'key': 'cp_cause',
                                      'q': 'According to paragraph 3, what caused the sinkholes near Plant City in 2010? Explain the chain of events.',
                                      'min': 20,
                                      'rows': 3,
                                      'pts': 3,
                                      'rubric': ['Farmers pumped large amounts of groundwater to protect strawberries from a freeze',
                                                 'The water level dropped, removing support for the soil, so sinkholes opened'],
                                      'model': 'Farmers pumped huge amounts of groundwater to spray on their strawberries during a freeze. The water level dropped, so the water no longer supported '
                                               'the soil above the limestone spaces, and dozens of sinkholes opened.'},
                                     {'t': 'text',
                                      'q': 'Which rock lies beneath much of Florida and is slowly dissolved by acidic water?',
                                      'a': ['limestone'],
                                      'show': 'limestone',
                                      'pts': 2,
                                      'why': 'Limestone (paragraph 2).'},
                                     {'t': 'open',
                                      'key': 'cp_purpose',
                                      'q': "Why does the author include paragraph 4 about Devil's Millhopper and the springs? How does it develop the central idea?",
                                      'min': 20,
                                      'rows': 3,
                                      'pts': 3,
                                      'rubric': ['Shows that sinkholes are not always disasters; the same process creates natural wonders',
                                                 'Adds balance and develops the idea that the landscape is always changing'],
                                      'model': "Paragraph 4 shows that sinkholes are not always disasters, because the same dissolving limestone created beautiful places like Devil's Millhopper and "
                                               "the springs. It develops the central idea that Florida's landscape is shaped by the rock beneath it."}]},
                          {'title': 'Part B: Summarize and paraphrase',
                           'items': [{'t': 'open',
                                      'key': 'cp_summary',
                                      'q': 'Write an objective summary of the article in 40 to 60 words. Use your own words, with no opinions.',
                                      'min': 40,
                                      'rows': 5,
                                      'pts': 4,
                                      'rubric': ['Central idea and key points (limestone dissolved by acidic water; dropping water levels cause collapse; some sinkholes are natural wonders; warning '
                                                 'signs and mapping)',
                                                 'Objective, in own words, no 4-word copied strings, 40 to 60 words'],
                                      'model': 'The article explains that sinkholes form often in Florida because slightly acidic water dissolves the limestone below the ground, leaving empty '
                                               'spaces. When groundwater drops from drought or pumping, soil can collapse, as in Plant City in 2010. Some old sinkholes are now parks and springs, and '
                                               'residents can learn warning signs.'},
                                     {'t': 'open',
                                      'key': 'cp_para',
                                      'q': 'Paraphrase this sentence from paragraph 5: "Scientists cannot predict exactly where the next sinkhole will open, but they can map areas at higher risk."',
                                      'min': 12,
                                      'rows': 2,
                                      'pts': 3,
                                      'rubric': ['Same meaning', 'New words and structure; no 4 or more words in a row copied'],
                                      'model': 'Although no one knows the precise spot where a sinkhole will appear, researchers can show which places are more likely to have one.'},
                                     {'t': 'text',
                                      'q': 'A student writes in a summary: "I think sinkholes are the scariest thing in Florida." What rule of summarizing does this break? Type the word that names '
                                           'the rule.',
                                      'a': [{'all': [['objective']]}, 'objectivity'],
                                      'show': 'objective',
                                      'pts': 2,
                                      'why': 'A summary must be objective: no opinions.'}]},
                          {'title': 'Part C: Research and citations',
                           'items': [{'t': 'open',
                                      'key': 'cp_mla',
                                      'q': 'Write the MLA works cited entry for this article. No person is named as author. It appeared in KCE Practice Reader, published by KingCretot Experience in '
                                           '2026.',
                                      'min': 8,
                                      'rows': 2,
                                      'pts': 3,
                                      'rubric': ['Begins with the title in quotation marks (organization is author and publisher)', 'Container, publisher, year in order', 'Correct punctuation'],
                                      'model': '"Why the Ground Opens Up in Florida." KCE Practice Reader, KingCretot Experience, 2026.'},
                                     {'t': 'open',
                                      'key': 'cp_note',
                                      'q': 'Make a research note card from paragraph 2 with a subtopic heading, a source label and notes in your own words.',
                                      'min': 20,
                                      'rows': 3,
                                      'pts': 3,
                                      'rubric': ['Subtopic heading (How sinkholes form)',
                                                 'Source label',
                                                 'Accurate notes in own words: limestone from shells, rain picks up CO₂ and becomes slightly acidic, dissolves rock over thousands of years, leaves '
                                                 'caves'],
                                      'model': 'Heading: How sinkholes form. Source: KingCretot Experience article. Notes: much of FL is limestone (old shells and skeletons); rain soaks up CO₂, '
                                               'turns a bit acidic; over thousands of years eats away rock, making cracks and caves.'},
                                     {'t': 'text',
                                      'q': 'What does it mean to combine information from two or more sources into one idea? Type one word.',
                                      'a': ['synthesize', 'synthesizing', 'synthesis'],
                                      'show': 'synthesize',
                                      'pts': 2,
                                      'why': 'To synthesize.'}]},
                          {'title': 'Part D: Vocabulary from Unit 2',
                           'items': [{'t': 'text',
                                      'q': 'Scientists who study groundwater like the water in paragraph 3 are called hydrogeologists. Using the roots hydr and geo, what does a hydrogeologist study?',
                                      'a': [{'all': [['water'], ['earth', 'ground', 'underground', 'rock', 'land', 'soil']], 'none': ['not']}],
                                      'show': 'water in the ground (water and the earth)',
                                      'pts': 2,
                                      'why': 'hydr (water) + geo (earth) + -logist (one who studies): a scientist who studies water underground.'},
                                     {'t': 'text',
                                      'q': 'The root terr means land or earth. What word for the land area that an animal defends begins with terr?',
                                      'a': ['territory', 'territories'],
                                      'show': 'territory',
                                      'pts': 2,
                                      'why': 'Territory: terr (land).'},
                                     {'t': 'text',
                                      'q': 'The root dict means say or speak. What dict word names a book that tells what words mean and how to say them?',
                                      'a': ['dictionary', 'dictionaries'],
                                      'show': 'dictionary',
                                      'pts': 2,
                                      'why': 'dict (say) + -ionary: a book of words and how to say them.'},
                                     {'t': 'text',
                                      'q': "The root nav means ship. What do you call a country's fleet of warships?",
                                      'a': ['navy'],
                                      'show': 'navy',
                                      'pts': 2,
                                      'why': 'Navy: nav (ship).'}]}]},
 'next': 'Unit 3: the power of poetry, beginning with figurative language.'}

TEACHER = {
 "standards": [
  "ELA.6.C.1.4: Write expository texts to explain and/or analyze information from multiple sources, using a logical organizational structure, relevant elaboration, and varied transitions.",
  "ELA.6.C.4.1: Conduct research to answer a question, drawing on multiple reliable and valid sources, and refocusing the inquiry when appropriate.",
  "ELA.6.R.2.2: Analyze the central idea(s), implied or explicit, and its development throughout a text.",
  "ELA.6.R.3.2: Paraphrase content from grade-level texts.",
  "ELA.6.V.1.2: Apply knowledge of Greek and Latin roots and affixes to determine meanings of words and phrases in grade-level content."],
 "materials": ["The interactive lesson", "The student's note cards, outline and works cited list from Week 9", "Colored pencils", "The Unit 2 Projects rubric", "A computer or paper for the final copy"],
 "flow": [
  [6, "Reconnect", "Run the Reconnect questions across the unit."],
  [4, "Hook", "Show the outline diagram. Lay out the student's note card groups."],
  [12, "Outline and introduction", "Turn card groups into headings; draft the central idea and hook."],
  [14, "Body paragraphs", "Model T-E-E-C and transitions. The student drafts one paragraph."],
  [10, "Features and conclusion", "Plan the visual and caption. Review ARMS and CUPS."],
  [4, "Assign", "Assign finishing, revising and publishing the article."],
  [10, "Checkpoint preview", "Explain that the checkpoint is completed after class, independently, one try per item, with no answers shown until you review it. Mastery is 85; below 85 means a review lesson and a retake."]],
 "key_questions": ["Does every section support your central idea?", "Where is the citation for this fact?", "What does this fact mean? (Elaborate.)", "Would a reader who knows nothing about this topic understand it?"],
 "misconceptions": ["An informational article is a list of facts with no explanation.", "Only quotations need citations.", "The conclusion should add new facts.", "Headings are decoration."],
 "support": ["Provide a T-E-E-C paragraph frame.", "Allow a shorter article (300 to 500 words) with two body sections; note the accommodation on the rubric.", "Read the checkpoint article aloud if decoding is a barrier."],
 "challenge": ["Add a third source and a sidebar with a fun fact.", "Turn the article into a one-page infographic for the co-op."],
 "background": "<p>The checkpoint article is original, written from established facts: the Winter Park sinkhole opened on May 8, 1981, and reached about 350 feet across and 75 feet deep; freeze-protection pumping near Plant City in January 2010 dropped the aquifer level sharply and dozens of sinkholes (reports range up to about 140) were documented; Devil's Millhopper is about 120 feet deep and 500 feet across (Florida State Parks). Limestone dissolution by weak carbonic acid is the standard karst explanation (U.S. Geological Survey). The Informational Article rubric is on the Unit 2 Projects page; score it separately from the checkpoint.</p>",
 "sources": ["U.S. Geological Survey, Sinkholes.", "Florida State Parks, Devil's Millhopper Geological State Park.", "Florida Geological Survey, Sinkhole Frequently Asked Questions.", "Modern Language Association (2021), MLA Handbook, 9th ed."]
}

PRINT = {
 "directions": "Write in complete sentences.",
 "items": [
  {"q":"What three jobs does an introduction do?","a":"Hook the reader, give background, state the central idea.","lines":2},
  {"q":"What does T-E-E-C stand for?","a":"Topic sentence, Evidence, Elaboration, Connection.","lines":1},
  {"q":"Rewrite with a varied transition: \"It rained for weeks. Also the river flooded.\"","a":"It rained for weeks. As a result, the river flooded.","lines":2},
  {"q":"Name three text features and what each does.","a":"Headings organize sections; captions explain visuals; bold words mark key terms.","lines":2},
  {"q":"What should a conclusion do, and what should it not do?","a":"Restate the central idea in new words and say why it matters; no brand-new facts.","lines":2},
  {"q":"Use the roots: what do aquarium, territory and navigate have in common in how they were built?","a":"Each is built on a root: aqua (water), terr (land), nav (ship).","lines":2}]
}
