POEM = '''<div class="card" style="border-left-color:#0047BA"><h3>Mother to Son</h3><p class="muted">by Langston Hughes (first published in <i>The Crisis</i>, December 1922; this text from <i>The Weary Blues</i>, 1926; in the public domain)</p>
<p style="font-family:Georgia,serif;font-size:18px;line-height:1.7">Well, son, I'll tell you:<br>Life for me ain't been no crystal stair.<br>It's had tacks in it,<br>And splinters,<br>And boards torn up,<br>And places with no carpet on the floor—<br>Bare.<br>But all the time<br>I'se been a-climbin' on,<br>And reachin' landin's,<br>And turnin' corners,<br>And sometimes goin' in the dark<br>Where there ain't been no light.<br>So boy, don't you turn back.<br>Don't you set down on the steps<br>'Cause you finds it's kinder hard.<br>Don't you fall now—<br>For I'se still goin', honey,<br>I'se still climbin',<br>And life for me ain't been no crystal stair.</p></div>'''

STAIRS = '''<svg viewBox="0 0 540 220" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Two staircases compared">
<text x="270" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">An extended metaphor: two staircases</text>
<g fill="#dff1ff" stroke="#7cb6e0" stroke-width="2"><polygon points="30,200 30,170 70,170 70,140 110,140 110,110 150,110 150,80 190,80 190,200"/></g>
<text x="110" y="214" text-anchor="middle" fill="#0047BA" font-weight="bold">A crystal stair: smooth, easy, shining</text>
<g fill="#c9a77a" stroke="#6b4f2a" stroke-width="2"><polygon points="300,200 300,170 340,170 340,140 380,140 380,110 420,110 420,80 460,80 460,50 500,50 500,200"/></g>
<g stroke="#2a2a2a" stroke-width="2"><line x1="310" y1="166" x2="314" y2="160"/><line x1="320" y1="166" x2="318" y2="159"/><line x1="352" y1="137" x2="364" y2="131"/></g>
<rect x="385" y="104" width="22" height="8" fill="#efe6d2" stroke="#6b4f2a"/><rect x="460" y="44" width="40" height="40" fill="#333" opacity=".75"/>
<g font-size="10" fill="#2a2a2a"><text x="300" y="158">tacks</text><text x="342" y="128">splinters</text><text x="380" y="100">boards torn up</text><text x="455" y="40">dark</text></g>
<text x="400" y="214" text-anchor="middle" fill="#6b4f2a" font-weight="bold">The mother's stair: hard, but she keeps climbing</text></svg>'''

LESSON = {'unit': 'Unit 1: Stories That Shape Us (Narrative)',
 'title': 'Theme in Story and Poem',
 'subtitle': 'A theme is what a story teaches about life. Great writers never just tell you; they let you discover it.',
 'objectives': ['Tell the difference between a topic and a theme, and write a theme as a complete statement.',
                'Analyze how an extended metaphor develops theme in Langston Hughes\'s "Mother to Son."',
                'Explain why a writer might use dialect, and respect it as an authentic voice.',
                'Compare themes across a poem and a story.',
                'Use the roots struct, port, rupt and ject, and write a theme paragraph supported by evidence.'],
 'vocab': [['theme', 'The message about life or human nature that a text develops. It is written as a complete sentence.'],
           ['topic', 'What a text is about, in one or two words, such as courage or family.'],
           ['metaphor', 'A comparison that says one thing is another, without like or as: Life is a staircase.'],
           ['extended metaphor', 'A metaphor that continues through many lines or a whole text.'],
           ['imagery', "Words that create a picture in the reader's mind through the senses."],
           ['dialect', 'A form of a language spoken by a particular group or region, with its own words, grammar and pronunciation.'],
           ['speaker', 'The voice that is talking in a poem. The speaker is not always the poet.'],
           ['Harlem Renaissance', 'A flowering of Black art, music and literature centered in Harlem, New York, in the 1920s and 1930s.'],
           ['struct / port', 'Latin roots meaning build (structure, construct) and carry (transport, portable).'],
           ['rupt / ject', 'Latin roots meaning break (erupt, interrupt) and throw (project, reject).']],
 'reconnect': {'title': 'Weeks 1 and 2: plot, character and point of view',
               'intro': 'Theme grows out of everything you have studied: what happens (plot), who changes (character) and who tells it (point of view).',
               'items': [{'t': 'text',
                          'q': 'In Moving Day, Part 1 is told with I and my. What point of view is that?',
                          'a': ['first person', 'first-person', '1st person'],
                          'show': 'first person',
                          'pts': 2,
                          'why': 'The narrator, Priya, is a character using I.'},
                         {'t': 'text',
                          'q': 'Name the five STEAL methods of characterization.',
                          'a': [{'all': [['speech', 'speak', 'say', 'said', 'talk'], ['thought', 'think'], ['effect'], ['action', 'act', 'do'], ['look', 'appearance']]}],
                          'show': 'speech, thoughts, effect on others, actions, looks',
                          'pts': 3,
                          'why': 'Speech, Thoughts, Effect on others, Actions, Looks.'},
                         {'t': 'text',
                          'q': 'How does Mateo change from the beginning to the end of The Cast Net?',
                          'a': [{'all': [['quit', 'give up', 'doubt', 'not a fisherman', 'frustrat', 'embarrass', 'failing', 'fail', 'struggl', 'impatient', 'upset', 'bad at'],
                                         ['confident', 'succeed', 'proud', 'grin', 'learn', 'patient', 'keep going', 'happy']]}],
                          'show': 'He goes from doubting himself and wanting to quit to feeling confident and ready to keep practicing.',
                          'pts': 3,
                          'why': "A character's change often points straight to the theme."},
                         {'t': 'text',
                          'q': 'Using the root aud, what does <b>audible</b> mean?',
                          'a': [{'all': [['hear', 'heard']]}],
                          'show': 'able to be heard',
                          'pts': 2,
                          'why': 'Aud means hear; -ible means able to be.'},
                         {'t': 'text',
                          'q': 'Fix the pronoun shift: <i>I practiced every day because you have to work hard to improve.</i>',
                          'a': [{'all': [['i practiced'], ['because i', 'i have to', 'i had to', 'i needed']]}],
                          'show': 'I practiced every day because I had to work hard to improve.',
                          'pts': 3,
                          'why': 'Keep the same point of view: I throughout.'},
                         {'t': 'text',
                          'q': 'On a rubric, which trait checks spelling, capitals and punctuation?',
                          'a': ['conventions'],
                          'pts': 2,
                          'why': "Conventions. Today's paragraph is scored with the same rubric."}]},
 'hook': {'title': 'The Lesson Hidden Inside',
          'html': '<p>Think of a fable such as <i>The Tortoise and the Hare</i>. Everyone remembers its lesson: <i>slow and steady wins the race</i>. In a fable, the moral is often stated right at '
                  'the end.</p><p>Most literature is different. The writer never announces the lesson. You have to find it in what the characters do, what changes, and the images the writer chooses. '
                  "This week you will discover the theme of a famous poem published by Langston Hughes when he was 21.</p><div class='callout'><b>Big idea:</b> A topic is a word (perseverance). A "
                  'theme is a sentence that says something true about life (Real friends tell you the truth even when it is hard to hear).</div>'},
 'learn': [{'title': 'Topic Versus Theme',
            'html': "<table class='t'><tr><th>Topic (a word)</th><th>Theme (a complete statement about life)</th></tr><tr><td>courage</td><td>Courage means acting even when you are "
                    'afraid.</td></tr><tr><td>friendship</td><td>A small act of kindness can turn a stranger into a friend.</td></tr><tr><td>practice</td><td>Patience and attention matter more than '
                    "natural talent.</td></tr></table><p>A strong theme statement is <b>universal</b>: it does not name the characters, and it could apply to many people's lives. It is not an order "
                    'such as <i>Never give up</i>, and it is not a cliché copied from a poster.</p>',
            'checks': [{'t': 'text',
                        'q': '"Kindness" is a topic. Is "Kindness" alone a theme? Type yes or no.',
                        'a': ['no'],
                        'pts': 2,
                        'why': 'A single word is a topic. A theme is a full sentence about life.'},
                       {'t': 'open',
                        'key': 'weaktheme',
                        'q': 'Is this a strong theme statement? <i>Dominic helps Priya carry boxes.</i> Explain, and rewrite it as a real theme.',
                        'min': 15,
                        'rows': 3,
                        'rubric': ['Not a theme: it is plot summary naming characters', 'Rewrites as a universal statement'],
                        'model': 'No. It just tells what happens and names characters. A real theme would be: Small acts of kindness can help someone feel at home in a new place.'},
                       {'t': 'open',
                        'key': 'movingtheme',
                        'q': 'Write a theme statement for Moving Day. Make it a complete, universal sentence that does not name Priya or Dominic.',
                        'min': 10,
                        'rows': 2,
                        'rubric': ['Complete sentence', 'Universal (no character names)', 'Supported by the story (kindness, empathy, starting over)'],
                        'model': 'People who remember how it felt to be left out are often the ones who reach out to someone new.'}]},
           {'title': 'Read: Mother to Son',
            'html': '<div class="card" style="border-left-color:#0047BA"><h3>Mother to Son</h3><p class="muted">by Langston Hughes (first published in <i>The Crisis</i>, December 1922; this text '
                    'from <i>The Weary Blues</i>, 1926; in the public domain)</p>\n'
                    '<p style="font-family:Georgia,serif;font-size:18px;line-height:1.7">Well, son, I\'ll tell you:<br>Life for me ain\'t been no crystal stair.<br>It\'s had tacks in it,<br>And '
                    "splinters,<br>And boards torn up,<br>And places with no carpet on the floor—<br>Bare.<br>But all the time<br>I'se been a-climbin' on,<br>And reachin' landin's,<br>And turnin' "
                    "corners,<br>And sometimes goin' in the dark<br>Where there ain't been no light.<br>So boy, don't you turn back.<br>Don't you set down on the steps<br>'Cause you finds it's "
                    "kinder hard.<br>Don't you fall now—<br>For I'se still goin', honey,<br>I'se still climbin',<br>And life for me ain't been no crystal stair.</p></div><p><b>Langston Hughes</b> "
                    '(1901 to 1967) was one of the great American poets and a leading voice of the <b>Harlem Renaissance</b>. He wrote about the lives, dreams and struggles of ordinary Black '
                    'Americans in the language they actually spoke. You will study him and the other Harlem Renaissance poets in Unit 3.</p><p>Read the poem aloud twice. Poetry is meant to be '
                    'heard.</p>',
            'checks': [{'t': 'text',
                        'q': 'Who is the <b>speaker</b> of the poem, and who is she talking to?',
                        'a': [{'all': [['mother', 'mom', 'mama'], ['son', 'boy', 'child']]}],
                        'show': 'A mother speaking to her son',
                        'pts': 2,
                        'why': 'The title and the first line tell us: a mother speaking to her son.'},
                       {'t': 'text',
                        'q': 'The speaker repeats one line at the beginning and the end. What does she say life has <b>not</b> been for her?',
                        'a': [{'all': [['crystal stair']]}],
                        'show': 'a crystal stair',
                        'pts': 2,
                        'why': '"Life for me ain\'t been no crystal stair" opens and closes the poem.'},
                       {'t': 'blanks',
                        'q': 'Name two different problems on her staircase.',
                        'sent': 'Problem 1: ___   Problem 2: ___',
                        'blanks': [[{'all': [['tack', 'splinter', 'board', 'carpet', 'bare', 'dark', 'no light', 'light']]}],
                                   [{'all': [['tack', 'splinter', 'board', 'carpet', 'bare', 'dark', 'no light', 'light']]}]],
                        'distinct': True,
                        'show': 'tacks, splinters, boards torn up, no carpet, places with no light',
                        'pts': 2,
                        'why': 'Hughes lists tacks, splinters, boards torn up, bare places with no carpet, and climbing in the dark.'},
                       {'t': 'text',
                        'q': 'What three things does she tell her son <b>not</b> to do?',
                        'a': [{'all': [['turn back'], ['set down', 'sit down', 'sit', 'set'], ['fall']]}],
                        'show': "Don't turn back, don't sit down on the steps, don't fall",
                        'pts': 3,
                        'why': 'Her three warnings are all about not stopping.'}]},
           {'title': 'The Extended Metaphor',
            'visual': '<svg viewBox="0 0 540 220" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Two staircases compared">\n'
                      '<text x="270" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">An extended metaphor: two staircases</text>\n'
                      '<g fill="#dff1ff" stroke="#7cb6e0" stroke-width="2"><polygon points="30,200 30,170 70,170 70,140 110,140 110,110 150,110 150,80 190,80 190,200"/></g>\n'
                      '<text x="110" y="214" text-anchor="middle" fill="#0047BA" font-weight="bold">A crystal stair: smooth, easy, shining</text>\n'
                      '<g fill="#c9a77a" stroke="#6b4f2a" stroke-width="2"><polygon points="300,200 300,170 340,170 340,140 380,140 380,110 420,110 420,80 460,80 460,50 500,50 500,200"/></g>\n'
                      '<g stroke="#2a2a2a" stroke-width="2"><line x1="310" y1="166" x2="314" y2="160"/><line x1="320" y1="166" x2="318" y2="159"/><line x1="352" y1="137" x2="364" y2="131"/></g>\n'
                      '<rect x="385" y="104" width="22" height="8" fill="#efe6d2" stroke="#6b4f2a"/><rect x="460" y="44" width="40" height="40" fill="#333" opacity=".75"/>\n'
                      '<g font-size="10" fill="#2a2a2a"><text x="300" y="158">tacks</text><text x="342" y="128">splinters</text><text x="380" y="100">boards torn up</text><text x="455" '
                      'y="40">dark</text></g>\n'
                      '<text x="400" y="214" text-anchor="middle" fill="#6b4f2a" font-weight="bold">The mother\'s stair: hard, but she keeps climbing</text></svg>',
            'html': '<p>Hughes compares life to a <b>staircase</b> through the whole poem. That is an <b>extended metaphor</b>. A crystal stair would be smooth, beautiful and easy to climb, like a '
                    "life of comfort and privilege. The mother's stair has tacks, splinters, torn boards and dark corners.</p><p>Think about what the images might stand for in a real life: poverty, "
                    'unfair treatment, loss, times without hope. The mother was speaking for many Black Americans in 1922 who faced segregation and racism, and who kept climbing anyway.</p><div '
                    "class='callout'>Notice what she <i>does</i> on the stair: climbing, reaching landings, turning corners, going on in the dark. Her actions point straight to the theme.</div>",
            'checks': [{'t': 'text',
                        'q': 'In the metaphor, what do the <b>landings</b> she reaches probably stand for?',
                        'a': [{'all': [['rest', 'goal', 'achiev', 'success', 'milestone', 'progress', 'break', 'better', 'accomplish', 'good times', 'stage', 'stop', 'pause', 'relief', 'breath']]}],
                        'show': 'Goals or resting points: times of progress or relief in life',
                        'pts': 3,
                        'why': 'A landing is a flat place to rest after climbing; in life it is a point of progress.'},
                       {'t': 'text',
                        'q': 'What might "going in the dark where there ain\'t been no light" stand for in someone\'s life?',
                        'a': [{'all': [['hope', 'scar', 'hard', 'unknown', 'alone', 'sad', 'lost', 'difficult', 'fear', 'confus', 'no help', 'not know']]}],
                        'show': 'Times without hope or help, when you cannot see what comes next',
                        'pts': 3,
                        'why': 'Darkness often stands for fear, hopelessness or the unknown.'},
                       {'t': 'open',
                        'key': 'poemtheme',
                        'q': 'Write a theme statement for "Mother to Son" as a complete, universal sentence.',
                        'min': 10,
                        'rows': 2,
                        'rubric': ['Complete, universal sentence', 'About perseverance through hardship', 'Does not just say never give up'],
                        'model': 'Even when life is hard and unfair, a person who keeps moving forward can reach a better place and inspire others to do the same.'}]},
           {'title': 'Dialect and Voice',
            'html': "<p>Hughes wrote the mother's words in <b>dialect</b>: <i>ain't been no, I'se been a-climbin', 'Cause you finds it's kinder hard.</i> This is a form of African American English a "
                    'variety still spoken by millions of people today.</p><p>Hughes chose dialect on purpose. It makes the mother sound like a real person speaking from her heart, not a textbook. '
                    'Dialect has its own consistent rules, and it is not "bad English." It is a different variety of English with its own history.</p><p>In your own formal writing for school, you '
                    'use <b>Standard English</b>, such as <i>Life has not been easy for me</i>. Knowing when to use each is a skill called <b>code-switching</b>, and most people do it every day.</p>',
            'checks': [{'t': 'text',
                        'q': "Rewrite the line in Standard English: <i>Life for me ain't been no crystal stair.</i>",
                        'a': [{'all': [['life'], ['has not been', "hasn't been", 'has never been', 'has been no', 'was not', "wasn't", 'is not', "isn't", 'has been no'], ['crystal stair']]}],
                        'show': 'Life for me has not been a crystal stair.',
                        'pts': 3,
                        'why': "The double negative ain't been no becomes has not been a in Standard English."},
                       {'t': 'open',
                        'key': 'dialectwhy',
                        'q': 'Why did Hughes choose to write the poem in dialect instead of Standard English? Explain what the choice adds.',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Authentic voice of a real mother', 'Presents it as a deliberate artistic choice', 'Honors real speech as rule-governed and valuable'],
                        'model': 'Hughes made a deliberate choice to let the mother speak in her own voice, the way real people in his community spoke. It makes her sound real and strong, and it '
                                 'shows that her way of speaking is valuable and worth putting in a poem.'}]},
           {'title': 'Roots: Building and Breaking',
            'html': "<table class='t'><tr><th>Root</th><th>Meaning</th><th>Examples</th></tr><tr><td>struct</td><td>build</td><td>structure, construct, "
                    'instruct</td></tr><tr><td>port</td><td>carry</td><td>transport, portable, import</td></tr><tr><td>rupt</td><td>break</td><td>erupt, interrupt, '
                    'rupture</td></tr><tr><td>ject</td><td>throw</td><td>project, reject, eject</td></tr></table><p>Add prefixes to change the meaning: <b>con-</b> (together), <b>trans-</b> '
                    '(across), <b>inter-</b> (between), <b>re-</b> (back or again), <b>e-</b> or <b>ex-</b> (out).</p>',
            'checks': [{'t': 'text',
                        'q': 'Using the parts, what does <b>interrupt</b> mean?',
                        'a': [{'all': [['break', 'stop', 'cut'], ['between', 'in', 'middle', 'into', 'someone', 'talk', 'speak', 'conversation']]}],
                        'show': 'to break into the middle of (a conversation or activity)',
                        'pts': 3,
                        'why': 'inter (between) + rupt (break).'},
                       {'t': 'blanks',
                        'q': 'Complete each sentence with a root word.',
                        'sent': 'The volcano began to ___ and threw ash into the sky. Trucks ___ oranges across the state. The mother had to ___ her own life from almost nothing. The publisher might '
                                '___ a poem it does not like.',
                        'blanks': [['erupt'], ['transport'], ['construct', 'reconstruct'], ['reject']],
                        'pts': 4,
                        'why': 'erupt (break out), transport (carry across), construct (build together), reject (throw back).'}]}],
 'handson': {'title': 'Walk the Staircase',
             'intro': 'Turn the metaphor into something you can climb.',
             'materials': ['A staircase at home (or a row of 6 index cards laid on the floor like steps)', '6 index cards or sticky notes', 'A marker'],
             'steps': ['On five cards, write five images from the poem: tacks, splinters, boards torn up, no carpet, going in the dark. On two more cards write: landing.',
                       'Place each card on a step, in the order the images appear. Put one landing card halfway up and one at the top, because the mother reaches landings in the middle of her climb, '
                       'not only at the end.',
                       'Climb the stairs slowly. On each step, say out loud a real-life hardship that image could stand for (for example, splinters: small hurts that keep pricking you).',
                       "At the landing, say the mother's message to her son in your own words.",
                       'Recite the whole poem aloud once while standing at the top. Read it to someone at home, or record it.'],
             'record': [{'t': 'open',
                         'key': 'stairs',
                         'q': 'List each image and the real-life hardship you connected it to. Which connection felt strongest and why? What could each landing mean?',
                         'min': 45,
                         'rows': 6,
                         'rubric': ['Lists all five images', 'Each image connected to a reasonable real-life hardship', 'Explains the strongest connection with a reason'],
                         'model': 'Tacks could be hurtful words, splinters could be small daily problems, boards torn up could be losing a job, no carpet could be having no comfort or money, and the '
                                  'dark could be not knowing what comes next. The halfway landing could be a moment of rest or a small success, and the top landing could be reaching a goal. The dark '
                                  'felt strongest to me because not knowing what is ahead is scary, but she climbed anyway.'},
                        {'t': 'open', 'key': 'recite', 'q': 'Who heard you recite the poem? What did reading it aloud help you notice that silent reading did not?', 'min': 20, 'rows': 3}]},
 'think': {'intro': 'This is your first full theme paragraph. Your teacher scores it with the Week 1 rubric.',
           'items': [{'t': 'open',
                      'key': 'themepara',
                      'q': 'Write a paragraph that answers: <b>What is the theme of "Mother to Son," and how does Hughes develop it?</b> Begin with a theme statement. Support it with at least two '
                           'exact quotations from the poem, and explain how each one develops the theme.',
                      'min': 110,
                      'rows': 10,
                      'rubric': ['Ideas: a clear, universal theme statement',
                                 'Evidence: two or more exact quotations, each explained',
                                 'Organization: topic sentence, transitions, closing sentence',
                                 'Conventions: Standard English, correct quotation marks'],
                      'model': 'In "Mother to Son," Langston Hughes shows that even when life is hard and unfair, a person who keeps climbing can reach a better place. The mother admits her life has '
                               'had "tacks," "splinters" and "boards torn up," images that stand for the pain and unfairness she has faced. Still, she says, "I\'se been a-climbin\' on," which shows '
                               'she never stopped moving forward. Because she has survived, she can warn her son, "don\'t you turn back." Hughes uses the staircase to show that perseverance is a '
                               'gift one generation can pass to the next.'},
                     {'t': 'open',
                      'key': 'compare',
                      'q': 'Compare the theme of "Mother to Son" with the theme of The Cast Net. How are the messages alike, and how are they different?',
                      'min': 60,
                      'rows': 6,
                      'rubric': ['States a theme for each text',
                                 'Explains a similarity (perseverance)',
                                 'Explains a difference (lifelong hardship and unfairness versus learning a skill; advice from an elder in both)',
                                 'Uses evidence from both texts'],
                      'model': 'Both texts are about perseverance, and in both an elder teaches a young person not to quit: Abuelo says "Again," and the mother says "don\'t you turn back." The '
                               'difference is the size of the struggle. Mateo struggles to learn one skill on one morning, while the mother describes a whole life of hardship and unfairness. The '
                               'Cast Net shows that patience leads to success, while "Mother to Son" shows that you must keep going even when success is not guaranteed.'}]},
 'exit': [{'t': 'open',
           'key': 'exittopic',
           'q': 'Is "courage" a topic or a theme? Explain how you know.',
           'min': 10,
           'rows': 2,
           'rubric': ['Topic', 'A single word, not a complete statement about life'],
           'model': 'It is a topic, because it is only one word. A theme would be a complete sentence about life, like: Courage means acting even when you are afraid.'},
          {'t': 'open',
           'key': 'exittheme',
           'q': 'Turn the topic <b>honesty</b> into a universal theme statement.',
           'min': 8,
           'rows': 2,
           'rubric': ['Complete sentence about life', 'Universal, not a command'],
           'model': 'Telling the truth can be hard at first, but it builds trust that lasts.'},
          {'t': 'text',
           'q': 'A metaphor that continues through a whole poem is called an ___ metaphor.',
           'a': ['extended', 'an extended', 'extended metaphor'],
           'show': 'extended',
           'pts': 2,
           'why': 'An extended metaphor carries one comparison through the text.'},
          {'t': 'text',
           'q': 'In "Mother to Son," what is life compared to?',
           'a': [{'all': [['stair', 'staircase', 'steps']]}],
           'show': 'a staircase',
           'pts': 2,
           'why': 'The whole poem compares life to climbing a staircase.'},
          {'t': 'text', 'q': 'What does the root <b>port</b> mean?', 'a': ['carry', 'to carry', 'carrying'], 'pts': 2, 'why': 'Port means carry: transport, portable.'},
          {'t': 'text',
           'q': 'Using roots, what is a <b>projector</b>?',
           'a': [{'all': [['throw', 'shoot', 'cast', 'show', 'shine', 'display'], ['image', 'picture', 'light', 'screen', 'forward', 'video', 'movie', 'onto', 'wall']]}],
           'show': 'A machine that throws an image forward onto a screen',
           'pts': 3,
           'why': 'pro (forward) + ject (throw): it throws light and pictures forward.'},
          {'t': 'text',
           'q': 'Which 1920s movement in Harlem, New York, was Langston Hughes a leader of?',
           'a': ['harlem renaissance', 'the harlem renaissance'],
           'show': 'the Harlem Renaissance',
           'pts': 2,
           'why': 'The Harlem Renaissance celebrated Black art, music and literature.'}],
 'next': 'Week 4: crafting narrative. You will learn dialogue, pacing and description, and draft your personal narrative.'}

TEACHER = {
 "standards": [
  "ELA.6.R.1.2: Analyze the development of stated or implied theme(s) throughout a literary text.",
  "ELA.6.R.3.1: Explain how figurative language contributes to tone and meaning in text(s).",
  "ELA.K12.EE.1.1: Cite evidence to explain and justify reasoning.",
  "ELA.6.V.1.2: Apply knowledge of Greek and Latin roots and affixes to determine the meanings of words.",
  "ELA.6.C.3.1: Follow the rules of standard English grammar, punctuation, capitalization and spelling.",
  "ELA.K12.EE.2.1: Read and comprehend grade-level complex texts proficiently."],
 "materials": ["The interactive lesson", "The poem printed for annotating", "Index cards and a staircase (or cards on the floor)", "Optional: a recording of Langston Hughes reading his work (the Library of Congress and Academy of American Poets host recordings)", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Reconnect questions. Use Mateo's change to preview how character change points to theme."],
  [5, "Hook", "Discuss The Tortoise and the Hare. Contrast a stated moral with an implied theme."],
  [8, "Topic versus theme", "Sort the examples. The student writes a theme for Moving Day and you test it: does it name a character? Is it an order?"],
  [14, "Read the poem", "Student reads aloud, then you read aloud. Annotate every image of hardship in one color and every action word (climbin', reachin', turnin') in another."],
  [10, "Extended metaphor", "Use the two-staircase visual. Ask what a crystal stair would mean in a real life and who in 1922 might have had one."],
  [9, "Dialect and voice", "Discuss why Hughes chose dialect. Practice code-switching by rewriting one line in Standard English, while stressing that dialect is not an error."],
  [8, "Roots and assign", "Teach the four roots with prefixes. Assign the staircase activity, the theme paragraph and the Exit Check."]],
 "key_questions": ["What does the mother do on the stairs, and what does that show?", "Why does she repeat the crystal stair line at the end?", "Who in 1922 might have had a crystal stair, and who would not?", "Why does it matter that a mother is giving this advice to her son?", "Is your theme a sentence about life, or a summary of the poem?"],
 "misconceptions": ["Writing a one-word topic or a command (Never give up) as a theme.", "Treating dialect as incorrect English rather than a rule-governed variety.", "Assuming the speaker is the poet himself.", "Summarizing the poem instead of explaining how images develop the theme."],
 "support": ["Provide the theme sentence frame: In this text, the author shows that people who... can/will...", "Give a two-column chart: image from the poem | what it might stand for.", "Read the poem aloud together line by line."],
 "challenge": ["Read Hughes's \"The Negro Speaks of Rivers\" (1921, public domain) and compare how both poems connect one person's life to a longer history.", "Ask the student to write their own short extended-metaphor poem comparing life to a journey (a road, a river, a game)."],
 "background": "<p>\"Mother to Son\" was first published in The Crisis, the NAACP's magazine edited by W. E. B. Du Bois, in December 1922, and was collected in Hughes's first book, The Weary Blues (1926). Works published in the United States in 1930 or earlier are in the public domain as of 2026, so the full text can appear in the lesson. Hughes was born in Joplin, Missouri, in 1901 and died in New York in 1967. The poem's vernacular reflects Southern African American speech; linguists recognize African American English as a rule-governed dialect.</p>",
 "sources": ["Poetry Foundation: Langston Hughes biography.", "Academy of American Poets (poets.org): Mother to Son.", "Library of Congress: Langston Hughes reading his poetry."]
}

PRINT = {
 "directions": "Use \"Mother to Son\" and your notes. Answer in complete sentences.",
 "items": [
  {"q":"What is the difference between a topic and a theme? Give one example of each.","a":"A topic is one or two words (perseverance); a theme is a complete statement about life (People who keep going through hard times can reach a better place).","lines":3},
  {"q":"Explain the extended metaphor in \"Mother to Son.\" What is compared to what?","a":"Life is compared to a staircase; the hard parts of the stair (tacks, splinters, darkness) stand for hardships, and climbing stands for perseverance.","lines":3},
  {"q":"Choose one image (tacks, splinters, boards torn up or going in the dark). What might it stand for in a real person's life?","a":"Answers vary; must connect the image to a reasonable hardship (e.g., darkness = times without hope).","lines":2},
  {"q":"Why does the mother tell her son not to turn back or sit down?","a":"She wants him to keep going through hardship as she has; quitting would mean never reaching a better place.","lines":2},
  {"q":"Rewrite in Standard English: Don't you set down on the steps 'cause you finds it's kinder hard.","a":"Do not sit down on the steps because you find it is kind of hard.","lines":2},
  {"q":"Write the meaning of each root and a word that uses it: struct ____ port ____ rupt ____ ject ____","a":"build (structure); carry (portable); break (erupt); throw (project)","lines":2},
  {"q":"Write a theme statement that fits BOTH The Cast Net and \"Mother to Son.\"","a":"For example: People who keep going after failure or hardship can succeed and pass their strength on to others.","lines":2}]
}
