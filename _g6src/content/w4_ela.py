PACING = ('<svg viewBox="0 0 540 190" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Pacing: how much space a writer gives each part">'
  '<text x="270" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Pacing: give the most words to the moments that matter</text>'
  + ''.join(f'<rect x="{x}" y="{170-h}" width="80" height="{h}" fill="{c}"/><text x="{x+40}" y="{164-h}" text-anchor="middle" font-size="11">{n}</text><text x="{x+40}" y="184" text-anchor="middle" font-size="11">{lab}</text>'
            for x, h, c, n, lab in [(20, 40, '#9ec3f0', 'short', 'Exposition'), (125, 70, '#5b8def', 'medium', 'Rising action'), (230, 130, '#DB2F30', 'longest', 'Climax'), (335, 45, '#9ec3f0', 'short', 'Falling action'), (440, 30, '#9ec3f0', 'short', 'Resolution')]) + '</svg>')

DIALOGUE = '''<div class="card" style="border-left-color:#0047BA"><h3>Dialogue rules, shown in The Cast Net</h3>
<p>"Turn your hips, then let it go," Abuelo said. "The net wants to open. You only have to let it."</p>
<p>"Maybe I'm just not a fisherman," Mateo muttered.</p>
<ol><li>Put the exact words a character says inside quotation marks.</li><li>Commas and periods go <b>inside</b> the closing quotation mark: "...let it go," Abuelo said.</li><li>Use a comma, not a period, before the dialogue tag (Abuelo said) when the sentence continues.</li><li>Start a <b>new paragraph</b> every time the speaker changes.</li><li>Use a precise tag only when it adds meaning: <i>muttered</i> tells us more than <i>said</i>. Most of the time, <i>said</i> is fine.</li></ol></div>'''

MENTOR = '''<div class="card" style="border-left-color:#C9A84C"><h3>Two versions of the same climax</h3>
<p><b>Version A (rushed):</b> I went up for the last shot of the game and made it, and we won.</p>
<p><b>Version B (slowed down):</b> The clock read 0:04. Dani's pass smacked into my palms, and suddenly the whole gym went quiet, like someone had pressed mute. I could smell the floor wax and feel my heartbeat in my ears. I bent my knees, the way Coach Ortiz drilled us a thousand times, and let the ball roll off my fingertips. It hung in the air forever. Then: swish. The buzzer screamed, and my teammates crashed into me so hard we all fell in a heap on the free-throw line.</p></div>'''

LESSON = {'unit': 'Unit 1: Stories That Shape Us (Narrative)',
 'title': 'Crafting Narrative: Dialogue, Pacing and Description',
 'subtitle': 'A true story becomes a great story when the writer controls time, voices and details.',
 'objectives': ['Punctuate dialogue correctly and use it to reveal character and move the plot forward.',
                'Control pacing by slowing down the climax and summarizing less important moments.',
                'Write vivid description with sensory details, precise nouns and strong verbs.',
                'Use transitional words and phrases to show the order of events.',
                'Use the roots chron, tele, photo and meter/metr, and draft a complete personal narrative.'],
 'vocab': [['dialogue', 'The words characters speak to each other in a story, shown in quotation marks.'],
           ['dialogue tag', 'The words that tell who is speaking, such as Abuelo said.'],
           ['pacing', 'How fast or slow a story moves. Writers slow down important moments and speed through less important ones.'],
           ['strong verb', 'A precise action word that creates a picture, such as smacked instead of hit.'],
           ['precise noun', 'A specific naming word, such as pinfish instead of fish.'],
           ['transition', 'A word or phrase that connects ideas and shows order, such as at first, suddenly, later that night or finally.'],
           ['chronological order', 'Events told in the order they happened in time.'],
           ['chron / tele', 'Greek roots meaning time (chronological, chronic) and far (telephone, telescope).'],
           ['photo / meter, metr', 'Greek roots meaning light (photograph) and measure (thermometer, metric).']],
 'reconnect': {'title': 'Weeks 1 to 3: plot, point of view and theme',
               'intro': 'This week you draft your personal narrative, so every tool from the unit comes together.',
               'items': [{'t': 'text',
                          'q': 'Which part of the plot is the turning point, where the tension is highest?',
                          'a': ['climax', 'the climax'],
                          'pts': 2,
                          'why': 'The climax. Today you learn to slow it down.'},
                         {'t': 'text',
                          'q': 'Your personal narrative is a true story about you, told with I and me. What point of view is that?',
                          'a': ['first person', 'first-person', '1st person'],
                          'show': 'first person',
                          'pts': 2,
                          'why': 'First person uses I and me.'},
                         {'t': 'text', 'q': 'Is <i>perseverance</i> a topic or a theme?', 'a': ['topic'], 'pts': 2, 'why': 'One word is a topic. A theme is a full sentence about life.'},
                         {'t': 'open',
                          'key': 'rc_hughes',
                          'q': 'In "Mother to Son," what is life compared to, and what does the mother tell her son not to do? Answer in one or two sentences.',
                          'min': 12,
                          'rows': 2,
                          'rubric': ['Life is compared to a staircase', 'Do not turn back, sit down or fall'],
                          'model': 'Life is compared to a staircase, and the mother tells her son not to turn back, sit down on the steps or fall.'},
                         {'t': 'text',
                          'q': 'Using the root struct, what does <b>construct</b> mean?',
                          'a': [{'all': [['build', 'make', 'put together', 'create']]}],
                          'show': 'to build',
                          'pts': 2,
                          'why': 'con (together) + struct (build).'},
                         {'t': 'text',
                          'q': 'Which STEAL method reveals character through what the character says aloud?',
                          'a': ['speech', 'speaking', 'dialogue'],
                          'show': 'speech',
                          'pts': 2,
                          'why': 'Speech. Today you learn to write it correctly.'}]},
 'hook': {'title': 'Slow Motion and Fast Forward',
          'html': '<p>Think about how movies handle time. A whole week can pass in a few seconds of music and quick scenes. But the big moment, the catch, the kiss, the fall, gets filmed in slow '
                  'motion so you feel every second.</p><p>Writers do the same thing with words. This week you will learn to fast-forward through the boring parts, slow down the moment that matters, '
                  "and let your characters speak for themselves. Then you will draft your whole personal narrative.</p><div class='callout'><b>Big idea:</b> Pacing is a choice. Spend the most words "
                  'on the moment that changes everything.</div>'},
 'learn': [{'title': 'Writing Dialogue That Works',
            'html': '<div class="card" style="border-left-color:#0047BA"><h3>Dialogue rules, shown in The Cast Net</h3>\n'
                    '<p>"Turn your hips, then let it go," Abuelo said. "The net wants to open. You only have to let it."</p>\n'
                    '<p>"Maybe I\'m just not a fisherman," Mateo muttered.</p>\n'
                    '<ol><li>Put the exact words a character says inside quotation marks.</li><li>Commas and periods go <b>inside</b> the closing quotation mark: "...let it go," Abuelo '
                    'said.</li><li>Use a comma, not a period, before the dialogue tag (Abuelo said) when the sentence continues.</li><li>Start a <b>new paragraph</b> every time the speaker '
                    'changes.</li><li>Use a precise tag only when it adds meaning: <i>muttered</i> tells us more than <i>said</i>. Most of the time, <i>said</i> is fine.</li></ol></div><p>Good '
                    'dialogue does a job. It reveals what a character is like (Abuelo is calm and patient) or moves the story forward. Characters rarely say everything they feel; what they leave '
                    'unsaid matters too.</p>',
            'checks': [{'t': 'punct',
                        'q': 'Punctuate this correctly by typing it with quotation marks, commas and capitals: <i>lets go home now said Mom</i>',
                        'a': ['"Let\'s go home now," said Mom.',
                              '"Let\'s go home now," Mom said.',
                              '"Let\'s go home now!" said Mom.',
                              '"Let\'s go home now!" Mom said.',
                              'Mom said, "Let\'s go home now."',
                              'Mom said, "Let\'s go home now!"'],
                        'show': '"Let\'s go home now," said Mom.',
                        'pts': 3,
                        'why': "Quotation marks around the spoken words, a comma inside the closing quotation mark, then the tag. (Let's needs an apostrophe: let us.)"},
                       {'t': 'text',
                        'q': 'When the speaker changes in dialogue, what must a writer start?',
                        'a': [{'all': [['new paragraph', 'paragraph', 'new line']]}],
                        'show': 'a new paragraph',
                        'pts': 2,
                        'why': 'Each new speaker gets a new paragraph so the reader can follow who is talking.'},
                       {'t': 'text',
                        'q': 'Replace <i>said</i> with a tag that shows the speaker was scared: <i>"Don\'t look down," I said.</i> Type only the new tag.',
                        'a': ['whispered', 'stammered', 'gasped', 'stuttered', 'murmured', 'squeaked', 'breathed', 'whimpered', 'trembled', 'quavered'],
                        'show': 'whispered (or stammered, gasped)',
                        'pts': 2,
                        'why': 'A precise tag shows how the words were spoken. Use one only when it adds meaning.'},
                       {'t': 'open',
                        'key': 'dialogue_reveal',
                        'q': 'Write two lines of dialogue between yourself and someone in your personal narrative. Make the dialogue reveal something about one of you. Punctuate it correctly.',
                        'min': 20,
                        'rows': 4,
                        'rubric': ['Correct quotation marks, commas and capitals', 'New paragraph (new line) for each speaker', 'Reveals character or moves the plot forward'],
                        'model': '"You\'re not scared, are you?" my cousin asked, already halfway up the ladder.\n'
                                 '"Of course not," I said, gripping the bottom rung so hard my knuckles turned white.'}]},
           {'title': 'Pacing: Slow Down the Moment',
            'visual': '<svg viewBox="0 0 540 190" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Pacing: how much space a writer gives each part"><text '
                      'x="270" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Pacing: give the most words to the moments that matter</text><rect x="20" y="130" '
                      'width="80" height="40" fill="#9ec3f0"/><text x="60" y="124" text-anchor="middle" font-size="11">short</text><text x="60" y="184" text-anchor="middle" '
                      'font-size="11">Exposition</text><rect x="125" y="100" width="80" height="70" fill="#5b8def"/><text x="165" y="94" text-anchor="middle" font-size="11">medium</text><text '
                      'x="165" y="184" text-anchor="middle" font-size="11">Rising action</text><rect x="230" y="40" width="80" height="130" fill="#DB2F30"/><text x="270" y="34" text-anchor="middle" '
                      'font-size="11">longest</text><text x="270" y="184" text-anchor="middle" font-size="11">Climax</text><rect x="335" y="125" width="80" height="45" fill="#9ec3f0"/><text x="375" '
                      'y="119" text-anchor="middle" font-size="11">short</text><text x="375" y="184" text-anchor="middle" font-size="11">Falling action</text><rect x="440" y="140" width="80" '
                      'height="30" fill="#9ec3f0"/><text x="480" y="134" text-anchor="middle" font-size="11">short</text><text x="480" y="184" text-anchor="middle" '
                      'font-size="11">Resolution</text></svg>',
            'html': '<div class="card" style="border-left-color:#C9A84C"><h3>Two versions of the same climax</h3>\n'
                    '<p><b>Version A (rushed):</b> I went up for the last shot of the game and made it, and we won.</p>\n'
                    "<p><b>Version B (slowed down):</b> The clock read 0:04. Dani's pass smacked into my palms, and suddenly the whole gym went quiet, like someone had pressed mute. I could smell "
                    'the floor wax and feel my heartbeat in my ears. I bent my knees, the way Coach Ortiz drilled us a thousand times, and let the ball roll off my fingertips. It hung in the air '
                    'forever. Then: swish. The buzzer screamed, and my teammates crashed into me so hard we all fell in a heap on the free-throw line.</p></div><p>Version B takes the same few '
                    'seconds and stretches them with <b>sensory details</b> (smell of floor wax, heartbeat in ears), <b>a simile</b> (like someone pressed mute), <b>thoughts</b> and <b>small '
                    'actions</b>. That is how writers make readers hold their breath.</p><p>Speed up the parts that only connect events: <i>Two weeks later, we were back at practice.</i></p>',
            'checks': [{'t': 'text',
                        'q': 'Find the simile in Version B. What is the quiet gym compared to?',
                        'a': [{'all': [['mute']]}],
                        'show': 'someone pressed mute',
                        'pts': 2,
                        'why': '"Like someone had pressed mute" compares the sudden silence to a muted sound.'},
                       {'t': 'text',
                        'q': 'Name two senses Version B uses besides sight.',
                        'a': [{'all': [['smell', 'wax'], ['hear', 'heard', 'sound', 'heartbeat', 'buzzer', 'quiet', 'mute']]},
                              {'all': [['smell', 'wax'], ['touch', 'feel', 'palm', 'fingertip']]},
                              {'all': [['hear', 'heard', 'sound', 'heartbeat', 'buzzer', 'quiet', 'mute'], ['touch', 'feel', 'palm', 'fingertip']]}],
                        'show': "smell (floor wax), hearing (heartbeat, buzzer), touch (the ball in the narrator's palms)",
                        'pts': 3,
                        'why': 'Smell, sound and touch put the reader inside the moment.'},
                       {'t': 'text',
                        'q': 'Write a one-sentence transition that fast-forwards through a week of time.',
                        'a': [{'all': [['week', 'days', 'later', 'after', 'next', 'following', 'monday', 'friday']]}],
                        'show': 'For example: The rest of the week crawled by until Saturday finally came.',
                        'pts': 2,
                        'why': 'A transition moves the reader quickly past time that does not matter to the story.'}]},
           {'title': 'Description: Strong Verbs and Precise Nouns',
            'html': "<table class='t'><tr><th>Weak</th><th>Strong</th></tr><tr><td>The dog went across the yard.</td><td>The beagle bolted across the yard.</td></tr><tr><td>She put the bag "
                    'down.</td><td>She dropped the grocery bag on the counter.</td></tr><tr><td>I ate the food.</td><td>I gobbled the plantains.</td></tr></table><p>Strong verbs and precise nouns '
                    'paint pictures without extra adjectives. Notice that <i>bolted</i> already tells you the dog was fast.</p><p><b>Transitions for order:</b> <i>at first, before long, meanwhile, '
                    'suddenly, an hour later, by the time, finally, that night.</i></p>',
            'checks': [{'t': 'open',
                        'key': 'strongverb',
                        'q': 'Revise this sentence with a strong verb and a precise noun: <i>The bird went up into the tree.</i>',
                        'min': 6,
                        'rows': 2,
                        'rubric': ['Replaces went with a strong verb', 'Replaces bird or tree with a precise noun'],
                        'model': 'The blue jay darted into the live oak.'},
                       {'t': 'text',
                        'q': 'Which word is the strongest verb: <i>moved, walked, stomped</i>?',
                        'a': ['stomped'],
                        'pts': 2,
                        'why': 'Stomped shows how the person walked, and probably how they felt.'},
                       {'t': 'blanks',
                        'q': 'Add transitions to show the order of events.',
                        'sent': '___, I could not find my shoes. ___ I found them under the couch. ___, we were only five minutes late.',
                        'blanks': [['at first', 'first', 'in the morning', 'that morning', 'to begin', 'in the beginning', 'this morning', 'earlier', 'yesterday'],
                                   ['then',
                                    'later',
                                    'after that',
                                    'finally',
                                    'eventually',
                                    'after searching',
                                    'soon',
                                    'next',
                                    'after looking everywhere',
                                    'after looking',
                                    'a few minutes later',
                                    'soon after'],
                                   ['finally', 'in the end', 'luckily', 'in the end luckily', 'amazingly', 'somehow', 'at last', 'thankfully', 'fortunately']],
                        'show': 'At first / Then / Finally (other transitions that show order are fine)',
                        'pts': 3,
                        'why': 'Transitions guide the reader through time.'}]},
           {'title': 'Roots: Time, Distance, Light and Measure',
            'html': "<table class='t'><tr><th>Root</th><th>Meaning</th><th>Examples</th></tr><tr><td>chron</td><td>time</td><td>chronological, chronic, "
                    'synchronize</td></tr><tr><td>tele</td><td>far</td><td>telephone, telescope, television</td></tr><tr><td>photo</td><td>light</td><td>photograph, '
                    'photosynthesis</td></tr><tr><td>meter, metr</td><td>measure</td><td>thermometer, metric, perimeter</td></tr></table>',
            'checks': [{'t': 'text',
                        'q': 'A personal narrative is usually told in <b>chronological</b> order. Using the root, what does that mean?',
                        'a': [{'all': [['time', 'order it happened', 'happened', 'sequence', 'first to last', 'happen', 'occur', 'beginning to end', 'when']]}],
                        'show': 'in the order events happened in time',
                        'pts': 2,
                        'why': 'Chron means time.'},
                       {'t': 'text',
                        'q': 'Using roots, what does a <b>telescope</b> help you do?',
                        'a': [{'all': [['far', 'distance', 'distant', 'space', 'stars', 'planets', 'long way']]}],
                        'show': 'see things that are far away',
                        'pts': 2,
                        'why': 'tele (far) + scope (look).'},
                       {'t': 'blanks',
                        'q': 'Complete with root words.',
                        'sent': 'Plants use light to make food through ___. A ___ measures temperature. I took a ___ of the sunset.',
                        'blanks': [['photosynthesis'], ['thermometer'], ['photo', 'photograph', 'picture']],
                        'pts': 3,
                        'why': 'photosynthesis (light + putting together), thermometer (heat + measure), photograph (light + write).'}]}],
 'handson': {'title': 'Act Out Your Climax in Slow Motion',
             'intro': 'Your body remembers details your brain forgets. Act out the climax of your personal narrative before you write it.',
             'materials': ['A family member or friend to help', 'Your Week 1 story mountain cards', 'A phone to record (optional)'],
             'steps': ['Read your climax card. Stand where it happened, or set up your room to look like the place.',
                       'Act out the climax in super slow motion, taking at least 60 seconds for something that took 5 seconds in real life.',
                       'As you move, say out loud what you see, hear, smell, feel and think at each moment. Your helper writes down your words.',
                       'Act it again at normal speed, and ask your helper what they noticed.',
                       "Circle the three best details from your helper's notes to use in your draft."],
             'record': [{'t': 'open',
                         'key': 'slowmo',
                         'q': 'List the details you said out loud while acting in slow motion, and circle (put stars next to) your three best ones.',
                         'min': 32,
                         'rows': 6,
                         'rubric': ['At least six details from the acted climax', 'Details use several senses and thoughts', 'Three strongest details marked'],
                         'model': 'rope burns my palms *; the water below looks brown and still; my cousin counting "three... two..."; I smell sunscreen and mud *; my stomach flips; I think "just '
                                  'let go" * (stars mark my three best details)'}]},
 'think': {'intro': 'This is the full first draft of your personal narrative. It will be revised and finished in Week 5 for your project.',
           'items': [{'t': 'open',
                      'key': 'draft',
                      'q': 'Write the complete first draft of your personal narrative. Use your story mountain, your Week 1 opening paragraph (revise it if you like), at least three lines of '
                           'correctly punctuated dialogue, a slowed-down climax with sensory details, transitions, and an ending that shows how you changed or what you learned.',
                      'min': 63,
                      'rows': 22,
                      'rubric': ['Ideas: a true story with a clear problem, climax and change',
                                 'Organization: chronological order with transitions; strong opening and ending',
                                 'Narrative craft: dialogue, sensory details, strong verbs, a slowed-down climax',
                                 'Point of view: consistent first person',
                                 'Conventions: correct dialogue punctuation, capitals and spelling'],
                      'model': '(Teacher note: no single model fits a personal story. A strong Grade 6 draft is 300 to 700 words, opens in the setting with sensory detail, uses at least three lines '
                               'of punctuated dialogue, spends the most words on the climax, and ends by reflecting on what the writer learned, for example: "I still think about that ladder every '
                               'time I am scared to try something. My hands shook then too, but I climbed anyway.")'},
                     {'t': 'open',
                      'key': 'selfcheck',
                      'q': 'Reread your draft. Which part did you slow down the most, and why is that the right moment? Name one place you will add a strong verb or a sensory detail when you revise.',
                      'min': 36,
                      'rows': 4,
                      'rubric': ['Identifies the slowed-down moment', 'Explains why it is the climax or most important moment', 'Names a specific revision'],
                      'model': 'I slowed down the moment I let go of the rope swing, because that is when I stopped being afraid. When I revise, I will change "I went into the water" to "I plunged '
                               'into the cold, brown water" in the falling action.'}]},
 'exit': [{'t': 'punct',
           'q': 'Punctuate by typing it with quotation marks, capitals and punctuation: <i>wait for me yelled Jordan</i>',
           'a': ['"Wait for me!" yelled Jordan.',
                 '"Wait for me," yelled Jordan.',
                 '"Wait for me!" Jordan yelled.',
                 '"Wait for me," Jordan yelled.',
                 'Jordan yelled, "Wait for me!"',
                 'Jordan yelled, "Wait for me."'],
           'show': '"Wait for me!" yelled Jordan. (A comma also works.)',
           'pts': 3,
           'why': 'Quotation marks around the spoken words with the comma or exclamation point inside, then the tag.'},
          {'t': 'text', 'q': 'Which part of a story should usually get the most words?', 'a': ['climax', 'the climax'], 'pts': 2, 'why': 'Slow down the most important moment.'},
          {'t': 'open',
           'key': 'exit_strong',
           'q': 'Revise with a strong verb: <i>The car went down the street fast.</i>',
           'min': 5,
           'rows': 2,
           'rubric': ['Replaces went ... fast with a strong verb such as raced or zoomed'],
           'model': 'The car raced down the street.'},
          {'t': 'text', 'q': 'What does the root <b>chron</b> mean?', 'a': ['time'], 'pts': 2, 'why': 'Chron means time.'},
          {'t': 'text', 'q': 'What does the root <b>photo</b> mean?', 'a': ['light'], 'pts': 2, 'why': 'Photo means light.'},
          {'t': 'text',
           'q': 'Name one transition word or phrase that shows something happened all at once.',
           'a': ['suddenly', 'all of a sudden', 'without warning', 'in an instant', 'instantly', 'just then', 'all at once', 'out of nowhere', 'out of the blue', 'immediately'],
           'show': 'suddenly (or all of a sudden, without warning)',
           'pts': 2,
           'why': 'These transitions signal a sudden change.'}],
 'next': 'Week 5: revise and finish your personal narrative, and take the Unit 1 checkpoint.'}

TEACHER = {
 "standards": [
  "ELA.6.C.1.2: Write personal or fictional narratives using narrative techniques, precise words and phrases, and figurative language.",
  "ELA.6.C.3.1: Follow the rules of standard English grammar, punctuation, capitalization, and spelling appropriate to grade level (dialogue punctuation).",
  "ELA.6.C.1.5 (preview): Improve writing by planning, revising, and editing, considering feedback from adults and peers.",
  "ELA.6.V.1.2: Apply knowledge of Greek and Latin roots and affixes to determine meanings of words and phrases in grade-level content."],
 "materials": ["The interactive lesson", "The student's story mountain cards and opening paragraph from Week 1", "Space to act out the climax", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Reconnect questions."],
  [4, "Hook", "Discuss slow motion in movies. Ask the student to name a movie moment that was slowed down and why."],
  [12, "Dialogue", "Study the five rules using The Cast Net. The student punctuates two sentences live, then writes two lines of dialogue from their own story."],
  [12, "Pacing", "Read Versions A and B aloud. Have the student list every technique in Version B. Show the pacing bar graph."],
  [10, "Description", "Revise three weak sentences together, then the student revises one from their own opening paragraph."],
  [6, "Roots", "Build words with chron, tele, photo and meter."],
  [10, "Plan the draft", "Review the student's story mountain. Decide together where the climax is and what dialogue to include. Assign the slow-motion activity before drafting."]],
 "key_questions": ["What job is this line of dialogue doing?", "Which moment in your story deserves slow motion? Why that one?", "Can you replace that verb with one that shows how?", "Where can you fast-forward?", "How did you change by the end of your story?"],
 "misconceptions": ["Putting commas and periods outside the closing quotation mark.", "Writing all dialogue in one paragraph regardless of speaker.", "Thinking every tag must be a fancy word instead of said.", "Spending equal time on every event, so the climax feels rushed."],
 "support": ["Provide a dialogue punctuation card with the five rules.", "Let the student dictate the climax aloud while you type, then they revise it.", "Give a transition word bank sorted by time order."],
 "challenge": ["Write the climax twice: once in present tense and once in past tense, and decide which is more powerful.", "Use a flashback for one paragraph, marked with clear transitions."],
 "background": "<p>The draft written this week is revised and finished in Week 5 as the Unit 1 Personal Narrative Project, scored with the project rubric. Mentor Version B is original to KCE. The draft is scored this week for completion and craft; the finished narrative is scored with the Week 5 project rubric.</p>"
}

PRINT = {
 "directions": "Use complete sentences. Punctuate dialogue correctly.",
 "items": [
  {"q":"Rewrite with correct punctuation and paragraphs: did you finish your chores asked Dad not yet I said","a":"\"Did you finish your chores?\" asked Dad. / \"Not yet,\" I said. (New paragraph for each speaker.)","lines":3},
  {"q":"Write a rushed one-sentence version of an exciting moment from your life. Then rewrite it slowed down with at least two senses and one thought.","a":"Answers vary; the slowed version must use two or more senses and a thought.","lines":5},
  {"q":"Replace each weak verb with a strong verb:  The baby cried ______   She walked into the room ______   He ate his lunch ______","a":"For example: wailed; stormed or tiptoed; devoured","lines":1},
  {"q":"Write three transitions that show time order.","a":"For example: at first, later that day, finally","lines":1},
  {"q":"Write the meaning of each root and one word: chron ____ tele ____ photo ____ meter ____","a":"time (chronological); far (telescope); light (photograph); measure (thermometer)","lines":2},
  {"q":"Why should a writer slow down the climax but speed through other parts?","a":"The climax is the most important moment, so slowing it down builds tension and lets the reader feel it; other parts only connect events.","lines":3}]
}
