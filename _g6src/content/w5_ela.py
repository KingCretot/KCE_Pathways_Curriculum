ARMS = ('<svg viewBox="0 0 560 170" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="ARMS revision and CUPS editing">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Revise with ARMS, then edit with CUPS</text>'
  + ''.join(f'<rect x="{12+i*68}" y="34" width="62" height="96" rx="8" fill="{c}"/><text x="{43+i*68}" y="68" text-anchor="middle" fill="#fff" font-size="26" font-family="Georgia" font-weight="bold">{L}</text><text x="{43+i*68}" y="96" text-anchor="middle" fill="#fff" font-size="11">{w}</text>'
            for i, (L, w, c) in enumerate([("A", "Add", "#0A1F3D"), ("R", "Remove", "#0A1F3D"), ("M", "Move", "#0A1F3D"), ("S", "Substitute", "#0A1F3D"),
                                           ("C", "Capitals", "#DB2F30"), ("U", "Usage", "#DB2F30"), ("P", "Punctuation", "#DB2F30"), ("S", "Spelling", "#DB2F30")])) +
  '<text x="140" y="152" text-anchor="middle" font-weight="bold" fill="#0A1F3D">Revising = making it better (ideas, words, order)</text>'
  '<text x="420" y="152" text-anchor="middle" font-weight="bold" fill="#DB2F30">Editing = making it correct</text></svg>')

STORY = '''<div class="card" style="border-left-color:#0047BA"><h3>The Recipe Card</h3><p class="muted">An original story by KingCretot Experience</p>
<p>The recipe card was soft as cloth, stained orange at one corner where a drop of sweet potato had landed years ago. Keisha held it up to the kitchen window. Her grandmother's handwriting slanted like it was running somewhere.</p>
<p>"You can't even read half of it," said her brother Andre, leaning over her shoulder. "Just look one up online."</p>
<p>Keisha didn't answer. Grandma Ruth had made her sweet potato pie every Thanksgiving for forty years, and this was the first Thanksgiving without her. A recipe from a website would not taste like Grandma's kitchen in Savannah, with the radio playing gospel and flour on every surface.</p>
<p>She squinted. <i>2 cups mashed. 1 cup sugar. Nutmeg</i> and then a word that looked like a tiny bird. <i>Bake till it tells you.</i></p>
<p>"Till it tells you?" Andre laughed. "Pies don't talk."</p>
<p>Keisha mashed, measured and stirred. When she reached the bird-word, she called her great-aunt Lorraine. Aunt Lorraine laughed so hard she had to put the phone down. "That's not a word, baby. That's a pinch. Your grandmother drew a pinch."</p>
<p>The pie went into the oven. Keisha sat on the floor and watched through the glass for almost an hour, until the center stopped jiggling and the edges cracked just a little, like the top of a loaf of bread.</p>
<p>"It's telling me," she whispered.</p>
<p>At dinner, Andre took a bite and stopped talking. Then he quietly asked for a second slice, and later, without being asked, he slid the recipe card into a plastic sleeve so it would never stain again.</p></div>'''

POEM = '''<div class="card" style="border-left-color:#C9A84C"><h3>The Road Not Taken</h3><p class="muted">by Robert Frost (first published in 1915 in <i>The Atlantic Monthly</i> and collected in <i>Mountain Interval</i>, 1916; in the public domain)</p>
<p>Two roads diverged in a yellow wood,<br>And sorry I could not travel both<br>And be one traveler, long I stood<br>And looked down one as far as I could<br>To where it bent in the undergrowth;</p>
<p>Then took the other, as just as fair,<br>And having perhaps the better claim,<br>Because it was grassy and wanted wear;<br>Though as for that the passing there<br>Had worn them really about the same,</p>
<p>And both that morning equally lay<br>In leaves no step had trodden black.<br>Oh, I kept the first for another day!<br>Yet knowing how way leads on to way,<br>I doubted if I should ever come back.</p>
<p>I shall be telling this with a sigh<br>Somewhere ages and ages hence:<br>Two roads diverged in a wood, and I&mdash;<br>I took the one less traveled by,<br>And that has made all the difference.</p></div>'''

LESSON = {'unit': 'Unit 1: Stories That Shape Us (Narrative)',
 'title': 'Unit 1 Checkpoint and Personal Narrative Project',
 'subtitle': 'Writers become great in revision. This week you polish your story, then show everything you learned in Unit 1.',
 'objectives': ['Revise a draft using ARMS (Add, Remove, Move, Substitute).',
                'Edit a draft using CUPS (Capitals, Usage, Punctuation, Spelling).',
                'Give and use specific feedback, and read your work aloud with expression.',
                'Publish the final Personal Narrative Project and score it with the rubric.',
                'Show mastery of Unit 1 reading, vocabulary and conventions on the checkpoint (85 or higher).'],
 'vocab': [['revise', 'To make writing better by changing ideas, words, details or order.'],
           ['edit', 'To make writing correct by fixing capitals, grammar, punctuation and spelling.'],
           ['feedback', 'Specific comments from a reader that help a writer improve.'],
           ['publish', 'To share a finished piece of writing with an audience.'],
           ['reflection', 'Thinking and writing about what you learned and how you grew.'],
           ['re-', 'A Latin prefix meaning again or back, as in revise (to see again) and rewrite.']],
 'reconnect': {'title': 'Week 4: dialogue, pacing and description',
               'intro': "Your revision checklist this week comes straight from last week's craft lessons.",
               'items': [{'t': 'punct',
                          'q': 'Punctuate by typing it with quotation marks, capitals and punctuation: <i>are you ready asked Coach</i>',
                          'a': ['"Are you ready?" asked Coach.', '"Are you ready?" Coach asked.', 'Coach asked, "Are you ready?"'],
                          'show': '"Are you ready?" asked Coach.',
                          'pts': 3,
                          'why': 'The question mark goes inside the closing quotation mark because the spoken words are the question.'},
                         {'t': 'open',
                          'key': 'rc_verb',
                          'q': 'Revise with a strong verb and a precise noun: <i>The dog went under the thing.</i>',
                          'min': 5,
                          'rows': 2,
                          'rubric': ['Strong verb replaces went', 'Precise noun replaces thing'],
                          'model': 'The beagle wriggled under the porch steps.'},
                         {'t': 'text', 'q': 'What does the root <b>chron</b> mean?', 'a': ['time'], 'pts': 2, 'why': 'Chron means time, as in chronological.'},
                         {'t': 'text',
                          'q': 'Name one transition that shows time has passed.',
                          'a': [{'all': [['later',
                                          'next',
                                          'after',
                                          'following',
                                          'then',
                                          'soon',
                                          'finally',
                                          'eventually',
                                          'meanwhile',
                                          'that night',
                                          'morning',
                                          'evening',
                                          'by the time',
                                          'hour',
                                          'week',
                                          'day']]}],
                          'show': 'For example: later that day',
                          'pts': 2,
                          'why': 'Transitions guide the reader through time.'},
                         {'t': 'open',
                          'key': 'rc_draft',
                          'q': 'In one or two sentences, what is your personal narrative about, and what is its climax?',
                          'min': 15,
                          'rows': 2,
                          'rubric': ['Names the true event', 'Identifies the climax'],
                          'model': 'My story is about learning to jump off the high dive at the community pool. The climax is the moment I step off the board.'}]},
 'hook': {'title': 'No One Writes It Right the First Time',
          'html': '<p>Professional authors rewrite their stories many times before anyone reads them. Ernest Hemingway said he rewrote the ending of one novel 39 times. When asked what the problem '
                  'was, he answered: getting the words right.</p><p>This week you become your own editor. You will use two tools, ARMS and CUPS, listen to feedback, and publish the final version of '
                  "your personal narrative. Then you will show what you learned this unit on the checkpoint.</p><div class='callout'><b>Big idea:</b> Revising makes writing better. Editing makes "
                  'writing correct. Do them in that order.</div>'},
 'learn': [{'title': 'Revising With ARMS',
            'visual': '<svg viewBox="0 0 560 170" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="ARMS revision and CUPS editing"><text x="280" y="18" '
                      'text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Revise with ARMS, then edit with CUPS</text><rect x="12" y="34" width="62" height="96" rx="8" '
                      'fill="#0A1F3D"/><text x="43" y="68" text-anchor="middle" fill="#fff" font-size="26" font-family="Georgia" font-weight="bold">A</text><text x="43" y="96" text-anchor="middle" '
                      'fill="#fff" font-size="11">Add</text><rect x="80" y="34" width="62" height="96" rx="8" fill="#0A1F3D"/><text x="111" y="68" text-anchor="middle" fill="#fff" font-size="26" '
                      'font-family="Georgia" font-weight="bold">R</text><text x="111" y="96" text-anchor="middle" fill="#fff" font-size="11">Remove</text><rect x="148" y="34" width="62" height="96" '
                      'rx="8" fill="#0A1F3D"/><text x="179" y="68" text-anchor="middle" fill="#fff" font-size="26" font-family="Georgia" font-weight="bold">M</text><text x="179" y="96" '
                      'text-anchor="middle" fill="#fff" font-size="11">Move</text><rect x="216" y="34" width="62" height="96" rx="8" fill="#0A1F3D"/><text x="247" y="68" text-anchor="middle" '
                      'fill="#fff" font-size="26" font-family="Georgia" font-weight="bold">S</text><text x="247" y="96" text-anchor="middle" fill="#fff" font-size="11">Substitute</text><rect x="284" '
                      'y="34" width="62" height="96" rx="8" fill="#DB2F30"/><text x="315" y="68" text-anchor="middle" fill="#fff" font-size="26" font-family="Georgia" '
                      'font-weight="bold">C</text><text x="315" y="96" text-anchor="middle" fill="#fff" font-size="11">Capitals</text><rect x="352" y="34" width="62" height="96" rx="8" '
                      'fill="#DB2F30"/><text x="383" y="68" text-anchor="middle" fill="#fff" font-size="26" font-family="Georgia" font-weight="bold">U</text><text x="383" y="96" text-anchor="middle" '
                      'fill="#fff" font-size="11">Usage</text><rect x="420" y="34" width="62" height="96" rx="8" fill="#DB2F30"/><text x="451" y="68" text-anchor="middle" fill="#fff" font-size="26" '
                      'font-family="Georgia" font-weight="bold">P</text><text x="451" y="96" text-anchor="middle" fill="#fff" font-size="11">Punctuation</text><rect x="488" y="34" width="62" '
                      'height="96" rx="8" fill="#DB2F30"/><text x="519" y="68" text-anchor="middle" fill="#fff" font-size="26" font-family="Georgia" font-weight="bold">S</text><text x="519" y="96" '
                      'text-anchor="middle" fill="#fff" font-size="11">Spelling</text><text x="140" y="152" text-anchor="middle" font-weight="bold" fill="#0A1F3D">Revising = making it better (ideas, '
                      'words, order)</text><text x="420" y="152" text-anchor="middle" font-weight="bold" fill="#DB2F30">Editing = making it correct</text></svg>',
            'html': '<p><b>A</b>dd: dialogue, sensory details, thoughts, a stronger ending.<br><b>R</b>emove: details that do not matter, repeated words, anything that slows the '
                    'climax.<br><b>M</b>ove: sentences or paragraphs to make the order clearer.<br><b>S</b>ubstitute: weak words for strong verbs and precise nouns.</p><div '
                    "class='example'><b>Before:</b> I was really scared. I went up the ladder. It was really high.<br><b>After (Add, Substitute):</b> My hands slipped on the cold, wet rungs. Halfway "
                    'up, I looked down, and the pool shrank to the size of a postage stamp.</div>',
            'checks': [{'t': 'open',
                        'key': 'armsname',
                        'q': 'Name the ARMS move in each revision and explain why it improves the story: (a) <i>went</i> becomes <i>scrambled</i>; (b) a paragraph about breakfast is deleted because '
                             'it has nothing to do with the climax.',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['(a) Substitute, with a reason (shows how the person moved)', '(b) Remove, with a reason (keeps the focus on what matters)'],
                        'model': '(a) Substitute: scrambled shows how the person moved, quickly and clumsily, so the reader can picture it. (b) Remove: the breakfast paragraph slowed the story and '
                                 'had nothing to do with the climax, so cutting it keeps the focus on the important moment.'},
                       {'t': 'open',
                        'key': 'addsense',
                        'q': 'Revise this sentence by adding two sensory details and one thought: <i>I walked into the new school.</i>',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Two different sensory details', 'A thought from the narrator', 'Still one moment, not a summary'],
                        'model': 'The hallway smelled like floor polish and pencil shavings, and a locker slammed somewhere like a gunshot. I wondered if everyone could tell I had never been there '
                                 'before.'}]},
           {'title': 'Editing With CUPS',
            'html': '<p>After revising, read your story slowly, once for each letter:</p><ul><li><b>C</b>apitals: first word of sentences, names, places, the word I, the first word inside quotation '
                    'marks.</li><li><b>U</b>sage: complete sentences, consistent past tense, pronouns that match (Week 2).</li><li><b>P</b>unctuation: end marks, commas, quotation marks around '
                    'dialogue, a new paragraph for each speaker.</li><li><b>S</b>pelling: check words you are unsure of; read backward word by word to catch mistakes.</li></ul>',
            'checks': [{'t': 'punct',
                        'q': 'Edit this sentence by retyping it correctly: <i>last summer my cousin and me visited atlanta</i>',
                        'a': ['Last summer my cousin and I visited Atlanta.', 'Last summer, my cousin and I visited Atlanta.'],
                        'show': 'Last summer, my cousin and I visited Atlanta.',
                        'pts': 3,
                        'why': 'Capitalize Last and Atlanta; use I (subject), not me; add a period.'},
                       {'t': 'open',
                        'key': 'tense',
                        'q': 'This passage switches tense. Rewrite it all in past tense: <i>I grabbed the rope. Then I swing out over the river and let go.</i>',
                        'min': 10,
                        'rows': 2,
                        'rubric': ['All verbs in past tense: grabbed, swung, let go'],
                        'model': 'I grabbed the rope. Then I swung out over the river and let go.'},
                       {'t': 'text',
                        'q': 'In <i>Everyone grabbed their towel and ran to his car,</i> the pronoun his does not match. What pronoun should replace it? Type one word.',
                        'a': ['their'],
                        'show': 'their',
                        'pts': 2,
                        'why': 'Keep pronouns consistent within the sentence.'}]},
           {'title': 'Feedback That Helps',
            'html': '<p>Useful feedback is specific. Instead of "It\'s good," a reader says exactly what worked and asks one real question.</p><table class=\'t\'><tr><th>Not '
                    'helpful</th><th>Helpful</th></tr><tr><td>I liked it.</td><td>I could feel your heartbeat when you described the clock at 0:04.</td></tr><tr><td>Add more detail.</td><td>What did '
                    "the gym sound like right before the shot?</td></tr><tr><td>It's confusing.</td><td>I lost track of who was talking in the middle of the dialogue.</td></tr></table><p>Use "
                    '<b>Praise, Question, Polish</b>: one thing that worked, one question, one suggestion.</p>',
            'checks': [{'t': 'open',
                        'key': 'pqp',
                        'q': "Here is the Week 4 mentor Version B: <i>The clock read 0:04. Dani's pass smacked into my palms, and suddenly the whole gym went quiet, like someone had pressed mute. I "
                             'could smell the floor wax and feel my heartbeat in my ears. I bent my knees, the way Coach Ortiz drilled us a thousand times, and let the ball roll off my fingertips. '
                             'It hung in the air forever. Then: swish.</i> Write feedback for that writer using Praise, Question, Polish.',
                        'min': 30,
                        'rows': 4,
                        'rubric': ['Specific praise naming a detail', 'A genuine question', 'A specific suggestion'],
                        'model': 'Praise: The simile about the gym going quiet like someone pressed mute made me feel the silence. Question: What were you thinking right before you shot? Polish: You '
                                 'could add one thought in your own words so we know how you felt, not just what happened.'}]}],
 'handson': {'title': "Author's Chair",
             'intro': 'Real authors read their work aloud to an audience. Hearing your own words also helps you catch mistakes.',
             'materials': ['Your revised personal narrative', 'A family audience of at least one person', 'A Praise, Question, Polish card for each listener', 'A chair or special spot to read from'],
             'steps': ['Read your story aloud to yourself once and mark any place you stumbled. Fix those sentences.',
                       "Sit in the Author's Chair and read your story to your family with expression. Slow down at the climax.",
                       'Ask each listener to give Praise, Question, Polish.',
                       'Choose one piece of feedback to use, and revise your story one last time.',
                       'Record your reading (optional) to share with your teacher.'],
             'record': [{'t': 'open',
                         'key': 'chair',
                         'q': 'Write down the feedback you received (Praise, Question, Polish) and explain which suggestion you used and how you changed your story.',
                         'min': 40,
                         'rows': 5,
                         'rubric': ['Records feedback from at least one listener', 'Names the change made', 'Explains why the change improved the story'],
                         'model': 'Praise: My mom liked how I described the water as brown and cold. Question: My brother asked how high the rope swing was. Polish: Mom said the ending felt fast. I '
                                  'added two sentences at the end about how I felt walking home and how I jumped again the next day, so the reader can see I changed.'}]},
 'think': {'intro': 'This is your Unit 1 Personal Narrative Project. Paste your final, revised and edited story below. Your teacher scores it with the project rubric on the Unit 1 Projects page.',
           'items': [{'t': 'open',
                      'key': 'final',
                      'q': 'Paste or type the final version of your personal narrative. Give it a title.',
                      'min': 400,
                      'rows': 24,
                      'rubric': ['Ideas and focus: a true, focused story with a clear problem, climax and change',
                                 'Organization: chronological order, transitions, an opening that hooks and an ending that reflects',
                                 'Narrative craft: dialogue, sensory details, strong verbs and a slowed-down climax',
                                 'Voice and point of view: consistent first person that sounds like the writer',
                                 'Conventions: correct capitals, usage, punctuation (including dialogue) and spelling'],
                      'model': '(Teacher note: no single model fits a personal story. Score with the five-trait project rubric. A Level 4 story is 400 to 800 words, has a title, opens in the scene, '
                               'uses at least three lines of correctly punctuated dialogue, spends the most words on the climax, and ends by reflecting on how the writer changed.)'},
                     {'t': 'open',
                      'key': 'reflect',
                      'q': 'Reflection: Compare your Week 4 draft with your final story. Name two specific changes you made (use ARMS words), and explain what you learned about yourself as a writer.',
                      'min': 60,
                      'rows': 6,
                      'rubric': ['Two specific revisions named with ARMS terms', 'Explains why each made the story better', 'Honest reflection on growth as a writer'],
                      'model': 'First, I substituted weak verbs: "I went into the water" became "I plunged into the cold, brown water." Second, I added a paragraph at the end about jumping again the '
                               'next day, which shows how I changed. I learned that my first draft tells what happened, but revising lets the reader feel it. I am better at details than endings, so '
                               'next time I will plan my ending first.'}]},
 'checkpoint': {'title': 'Unit 1 Checkpoint: Stories That Shape Us',
                'intro': 'Read the story and the poem carefully, then answer. You may look back at the texts. Mastery is 85 or higher. If you score below 85, your teacher will review with you, then '
                         'you will retake it.',
                'parts': [{'title': 'Part A: Read the story',
                           'items': [{'t': 'text',
                                      'q': '<div class=\'cp-text\'><div class="card" style="border-left-color:#0047BA"><h3>The Recipe Card</h3><p class="muted">An original story by KingCretot '
                                           'Experience</p>\n'
                                           '<p>The recipe card was soft as cloth, stained orange at one corner where a drop of sweet potato had landed years ago. Keisha held it up to the kitchen '
                                           "window. Her grandmother's handwriting slanted like it was running somewhere.</p>\n"
                                           '<p>"You can\'t even read half of it," said her brother Andre, leaning over her shoulder. "Just look one up online."</p>\n'
                                           "<p>Keisha didn't answer. Grandma Ruth had made her sweet potato pie every Thanksgiving for forty years, and this was the first Thanksgiving without her. A "
                                           "recipe from a website would not taste like Grandma's kitchen in Savannah, with the radio playing gospel and flour on every surface.</p>\n"
                                           '<p>She squinted. <i>2 cups mashed. 1 cup sugar. Nutmeg</i> and then a word that looked like a tiny bird. <i>Bake till it tells you.</i></p>\n'
                                           '<p>"Till it tells you?" Andre laughed. "Pies don\'t talk."</p>\n'
                                           '<p>Keisha mashed, measured and stirred. When she reached the bird-word, she called her great-aunt Lorraine. Aunt Lorraine laughed so hard she had to put '
                                           'the phone down. "That\'s not a word, baby. That\'s a pinch. Your grandmother drew a pinch."</p>\n'
                                           '<p>The pie went into the oven. Keisha sat on the floor and watched through the glass for almost an hour, until the center stopped jiggling and the edges '
                                           'cracked just a little, like the top of a loaf of bread.</p>\n'
                                           '<p>"It\'s telling me," she whispered.</p>\n'
                                           '<p>At dinner, Andre took a bite and stopped talking. Then he quietly asked for a second slice, and later, without being asked, he slid the recipe card '
                                           "into a plastic sleeve so it would never stain again.</p></div></div>What is Keisha's main problem in the story?",
                                      'a': [{'all': [['read', 'understand', 'figure out', 'make out', 'decipher'], ['recipe', 'card', 'handwriting', 'writing', 'word']]},
                                            {'all': [['miss', 'grandmother', 'grandma', 'without her']], 'none': ['burn', 'andre']}],
                                      'show': "She wants to make her late grandmother's pie but cannot read parts of the handwritten recipe card.",
                                      'pts': 3,
                                      'why': "The recipe card is hard to read, and Keisha wants the pie to taste like Grandma's, not a website recipe."},
                                     {'t': 'text',
                                      'q': 'From what point of view is the story told? Type first person, third person limited or third person omniscient.',
                                      'a': ['third person limited', 'third-person limited', '3rd person limited', '^third person limited', 'limited third person'],
                                      'show': 'third person limited',
                                      'pts': 2,
                                      'why': "The narrator uses she and her and shares only Keisha's thoughts and feelings."},
                                     {'t': 'open',
                                      'key': 'cp_climax',
                                      'q': 'Explain why the moment Keisha whispers, "It\'s telling me," is the climax of the story.',
                                      'min': 15,
                                      'rows': 2,
                                      'pts': 3,
                                      'rubric': ['Identifies it as the turning point', "Connects it to solving the problem (she understands Grandma's words and succeeds)"],
                                      'model': 'It is the turning point: after struggling to read the card, Keisha finally understands what Grandma meant by "bake till it tells you," and she knows '
                                               'the pie will be right.'},
                                     {'t': 'open',
                                      'key': 'cp_andre',
                                      'q': 'How does Andre change from the beginning to the end? Use two pieces of evidence from the story. Name one STEAL method the author uses to show the change.',
                                      'min': 40,
                                      'rows': 4,
                                      'rubric': ['Beginning: doubtful or mocking ("Just look one up online", "Pies don\'t talk")',
                                                 'End: respectful, quiet, protects the card',
                                                 'Two pieces of text evidence',
                                                 'Names a STEAL method (actions, speech)'],
                                      'model': 'At first Andre mocks the recipe: he says "Just look one up online" and laughs that "Pies don\'t talk." By the end he is quiet and respectful. He asks '
                                               'for a second slice and, without being asked, puts the card in a plastic sleeve so it will never stain again. The author shows his change through his '
                                               'actions instead of telling us how he feels.'},
                                     {'t': 'open',
                                      'key': 'cp_theme',
                                      'q': 'Write a theme statement for "The Recipe Card" as a complete, universal sentence.',
                                      'min': 10,
                                      'rows': 2,
                                      'rubric': ['Complete sentence', 'Universal, about life, not about Keisha', 'Fits the story (family memory, tradition, love lasting)'],
                                      'model': 'The people we love stay with us through the traditions we carry on.'}]},
                          {'title': 'Part B: Read the poem',
                           'items': [{'t': 'text',
                                      'q': '<div class=\'cp-text\'><div class="card" style="border-left-color:#C9A84C"><h3>The Road Not Taken</h3><p class="muted">by Robert Frost (first published in '
                                           '1915 in <i>The Atlantic Monthly</i> and collected in <i>Mountain Interval</i>, 1916; in the public domain)</p>\n'
                                           '<p>Two roads diverged in a yellow wood,<br>And sorry I could not travel both<br>And be one traveler, long I stood<br>And looked down one as far as I '
                                           'could<br>To where it bent in the undergrowth;</p>\n'
                                           '<p>Then took the other, as just as fair,<br>And having perhaps the better claim,<br>Because it was grassy and wanted wear;<br>Though as for that the '
                                           'passing there<br>Had worn them really about the same,</p>\n'
                                           '<p>And both that morning equally lay<br>In leaves no step had trodden black.<br>Oh, I kept the first for another day!<br>Yet knowing how way leads on to '
                                           'way,<br>I doubted if I should ever come back.</p>\n'
                                           '<p>I shall be telling this with a sigh<br>Somewhere ages and ages hence:<br>Two roads diverged in a wood, and I&mdash;<br>I took the one less traveled '
                                           'by,<br>And that has made all the difference.</p></div></div>In the poem, what does the choice between two roads stand for in real life?',
                                      'a': [{'all': [['choice', 'decision', 'decide', 'choose']]}],
                                      'show': 'an important choice or decision in life',
                                      'pts': 2,
                                      'why': 'The roads are an extended metaphor for choices in life.'},
                                     {'t': 'open',
                                      'key': 'cp_same',
                                      'q': 'In the second and third stanzas, how different are the two roads really? Quote a line as evidence, then explain why this matters for understanding the '
                                           'last stanza.',
                                      'min': 35,
                                      'rows': 4,
                                      'rubric': ['The roads are about the same',
                                                 'Quotes a line such as "Had worn them really about the same" or "both that morning equally lay"',
                                                 'Explains that the speaker will later tell the story as if his choice made all the difference, so the poem is about how we tell the story of our '
                                                 'choices'],
                                      'model': 'The roads are really about the same. The speaker says the passing there "Had worn them really about the same." This matters because in the last stanza '
                                               'he imagines telling people one day that he took the road "less traveled by." The poem shows how we tell the story of our choices later, making them '
                                               'seem more different than they were.'},
                                     {'t': 'text',
                                      'q': 'Which word in the last stanza suggests the speaker may have mixed feelings, or even some regret, about his choice? Type the word.',
                                      'a': ['sigh', 'with a sigh', 'a sigh'],
                                      'show': 'sigh',
                                      'pts': 2,
                                      'why': '"I shall be telling this with a sigh" hints that the speaker is not simply proud; a sigh can show regret, relief or longing.'}]},
                          {'title': 'Part C: Vocabulary',
                           'items': [{'t': 'text',
                                      'q': 'Using roots, what does <b>autobiography</b> mean?',
                                      'a': [{'all': [['self', 'own', 'yourself', 'themselves', 'himself', 'herself', 'by that person', 'by the person', 'written by'], ['life']],
                                             'none': ['someone else', 'another person']}],
                                      'show': "the story of a person's life written by that person",
                                      'pts': 2,
                                      'why': 'auto (self) + bio (life) + graph (write).'},
                                     {'t': 'text',
                                      'q': 'Using roots, what does <b>spectator</b> mean?',
                                      'a': [{'all': [['watch', 'look', 'see', 'view', 'observ']]}],
                                      'show': 'a person who watches',
                                      'pts': 2,
                                      'why': 'spect means look or see.'},
                                     {'t': 'text',
                                      'q': 'Using roots, what does <b>interrupt</b> mean?',
                                      'a': [{'all': [['break', 'stop', 'cut']]}],
                                      'show': 'to break in between (stop someone while they are talking)',
                                      'pts': 2,
                                      'why': 'inter (between) + rupt (break).'},
                                     {'t': 'text',
                                      'q': 'Using roots, what does <b>photograph</b> literally mean?',
                                      'a': [{'all': [['light'], ['writ', 'draw', 'record', 'picture']]}],
                                      'show': 'writing (or drawing) with light',
                                      'pts': 2,
                                      'why': 'photo (light) + graph (write).'}]},
                          {'title': 'Part D: Conventions',
                           'items': [{'t': 'punct',
                                      'q': 'Punctuate by typing it: <i>this pie is perfect said Andre</i>',
                                      'a': ['"This pie is perfect," said Andre.',
                                            '"This pie is perfect!" said Andre.',
                                            '"This pie is perfect," Andre said.',
                                            '"This pie is perfect!" Andre said.',
                                            'Andre said, "This pie is perfect."',
                                            'Andre said, "This pie is perfect!"'],
                                      'show': '"This pie is perfect," said Andre.',
                                      'pts': 3,
                                      'why': 'Quotation marks around the spoken words, a comma or exclamation point inside the closing mark, then the tag.'},
                                     {'t': 'punct',
                                      'q': 'Fix the pronoun error by retyping the sentence: <i>Keisha and me baked the pie.</i>',
                                      'a': ['Keisha and I baked the pie.'],
                                      'show': 'Keisha and I baked the pie.',
                                      'pts': 2,
                                      'why': 'Use I as part of the subject. Test it: "I baked the pie," not "me baked the pie."'},
                                     {'t': 'open',
                                      'key': 'cp_revise',
                                      'q': 'Revise this sentence using Add and Substitute, then name each move you made: <i>I was really scared when I went up.</i>',
                                      'min': 15,
                                      'rows': 3,
                                      'pts': 3,
                                      'rubric': ['Adds a sensory detail or thought', 'Substitutes a stronger verb for went', 'Names both moves correctly'],
                                      'model': "My knees shook as I climbed the slippery ladder, and I thought, don't look down. (Add: shaking knees and the thought. Substitute: climbed instead of "
                                               'went.)'}]}]},
 'next': 'Unit 2: Explaining the World. You will read and write informational texts, starting with central ideas and supporting details.'}

TEACHER = {
 "standards": [
  "ELA.6.C.1.2: Write personal or fictional narratives using narrative techniques, precise words and phrases, and figurative language.",
  "ELA.6.C.1.5: Improve writing by planning, revising, and editing, considering feedback from adults and peers.",
  "ELA.6.C.3.1: Follow the rules of standard English grammar, punctuation, capitalization, and spelling appropriate to grade level.",
  "ELA.6.C.2.1: Present information orally, in a logical sequence, using nonverbal cues, appropriate volume, clear pronunciation, and appropriate pacing.",
  "ELA.6.R.1.2: Analyze the development of stated or implied theme(s) throughout a literary text (checkpoint).",
  "ELA.6.R.1.3: Explain the influence of multiple narrators and/or shifts in point of view in a literary text (checkpoint).",
  "ELA.6.V.1.2: Apply knowledge of Greek and Latin roots and affixes to determine meanings of words and phrases in grade-level content (checkpoint)."],
 "materials": ["The interactive lesson", "The student's Week 4 draft (printed if possible)", "Two highlighters or colored pencils (one for ARMS, one for CUPS)", "The Unit 1 Projects page with the narrative rubric", "Printable practice page"],
 "flow": [
  [5, "Reconnect", "Run the Reconnect questions."],
  [5, "Hook", "Discuss rewriting. Ask the student which part of their draft they are least happy with."],
  [15, "ARMS on the student's draft", "Model ARMS on the Before/After example, then work through the student's draft together. Mark at least one change for each letter."],
  [10, "CUPS", "Model the CUPS read-through on one paragraph of the student's draft, one letter at a time."],
  [10, "Feedback", "Practice Praise, Question, Polish on the mentor text, then give the student feedback on their draft the same way."],
  [10, "Project and checkpoint", "Review the narrative project rubric together. Explain that the final story, the Author's Chair activity and the checkpoint are completed after class."],
  [5, "Close", "Set the date the final story is due and the date for the Author's Chair reading."]],
 "key_questions": ["Is this change revising or editing?", "Where can a reader feel your climax most?", "What feedback will you use, and why?", "How did you grow as a writer this unit?"],
 "misconceptions": ["Thinking revision only means fixing spelling.", "Using every suggestion instead of choosing the ones that fit the writer's goal.", "Reading the checkpoint poem as a simple message to take the unusual path, missing that the roads were about the same."],
 "support": ["Revise one paragraph at a time with the ARMS card beside it.", "Read the draft aloud to the student so they hear where it stumbles.", "Allow the student to dictate the reflection and then type it."],
 "challenge": ["Rewrite the opening paragraph two different ways and choose the stronger one.", "Write a short paragraph explaining why many readers misunderstand \"The Road Not Taken.\""],
 "background": "<p>The Personal Narrative Project is scored with the five-trait rubric on the Unit 1 Projects page (4 points per trait, 20 total; convert to 100 by multiplying by 5). Mastery is 85 (17 of 20). The checkpoint uses an original KCE story and Robert Frost's \"The Road Not Taken,\" first published in The Atlantic Monthly in August 1915 and collected in Mountain Interval (1916); it is in the public domain. Frost wrote the poem partly as a gentle joke about his friend Edward Thomas, who often regretted whichever path they had not taken on their walks. The Hemingway story about rewriting the ending of A Farewell to Arms 39 times comes from his 1958 Paris Review interview.</p>",
 "sources": ["Poetry Foundation: Robert Frost, \"The Road Not Taken.\"", "The Paris Review, \"Ernest Hemingway, The Art of Fiction No. 21\" (1958).", "CPALMS: Florida B.E.S.T. ELA Grade 6 benchmarks."]
}

PRINT = {
 "directions": "Use complete sentences. Use your own draft for item 6.",
 "items": [
  {"q":"Explain the difference between revising and editing.","a":"Revising makes writing better (ideas, words, order); editing makes it correct (capitals, usage, punctuation, spelling).","lines":2},
  {"q":"What do the letters in ARMS and CUPS stand for?","a":"Add, Remove, Move, Substitute; Capitals, Usage, Punctuation, Spelling","lines":2},
  {"q":"Edit: yesterday me and jamal walked to the park he said lets race","a":"Yesterday Jamal and I walked to the park. He said, \"Let's race.\"","lines":2},
  {"q":"Revise with a strong verb and a sensory detail: The cat went across the kitchen.","a":"For example: The cat crept across the cold tile floor, its claws clicking.","lines":2},
  {"q":"Write helpful feedback (Praise, Question, Polish) for a friend's story about a soccer game.","a":"For example: Praise: I could hear the crowd when you described the drums. Question: what did your coach say at halftime? Polish: slow down the moment you kicked the winning goal.","lines":3},
  {"q":"Copy one sentence from your draft. Then rewrite it using one ARMS move. Name the move.","a":"For example: I went into the water. → I plunged into the cold, brown water. (Substitute and Add.)","lines":3}]
}
