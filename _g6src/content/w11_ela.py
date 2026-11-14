def poem(title, author, lines, note=""):
    body = "<br>".join(l if l else "&nbsp;" for l in lines)
    return (f"<div class='card' style='border-left-color:#C9A84C'><h3 style='margin-top:0'>{title}</h3><p class='muted' style='margin-top:-6px'>{author}</p>"
            f"<p style='font-family:Georgia,serif;font-size:17px;line-height:1.7'>{body}</p>{note}</div>")

WIND = poem("Who Has Seen the Wind?", "Christina Rossetti (1872)", [
 "Who has seen the wind?", "Neither I nor you:", "But when the leaves hang trembling,", "The wind is passing through.", "",
 "Who has seen the wind?", "Neither you nor I:", "But when the trees bow down their heads,", "The wind is passing by."])

FOG = poem("Fog", "Carl Sandburg (1916)", ["The fog comes", "on little cat feet.", "", "It sits looking", "over harbor and city", "on silent haunches", "and then moves on."],
 "<p class='muted' style='font-size:12px'>haunches: the back legs and hips of an animal sitting down</p>")

HOPE = poem("\u201cHope\u201d is the thing with feathers", "Emily Dickinson (written about 1861; this text from the first printing, 1891)", [
 "\u201cHope\u201d is the thing with feathers", "That perches in the soul,", "And sings the tune without the words,", "And never stops at all,", "",
 "And sweetest in the gale is heard;", "And sore must be the storm", "That could abash the little bird", "That kept so many warm.", "",
 "I\u2019ve heard it in the chillest land,", "And on the strangest sea;", "Yet, never, in extremity,", "It asked a crumb of me."],
 "<p class='muted' style='font-size:12px'>gale: a strong wind. abash: embarrass, make shy. extremity: the worst, most desperate moment.</p>")

SYMP = poem("Sympathy", "Paul Laurence Dunbar (1899)", [
 "I know what the caged bird feels, alas!", "When the sun is bright on the upland slopes;", "When the wind stirs soft through the springing grass,", "And the river flows like a stream of glass;", "When the first bird sings and the first bud opes,", "And the faint perfume from its chalice steals —", "I know what the caged bird feels!", "",
 "I know why the caged bird beats his wing", "Till its blood is red on the cruel bars;", "For he must fly back to his perch and cling", "When he fain would be on the bough a-swing;", "And a pain still throbs in the old, old scars", "And they pulse again with a keener sting —", "I know why he beats his wing!", "",
 "I know why the caged bird sings, ah me,", "When his wing is bruised and his bosom sore, —", "When he beats his bars and he would be free;", "It is not a carol of joy or glee,", "But a prayer that he sends from his heart’s deep core,", "But a plea, that upward to Heaven he flings —", "I know why the caged bird sings!"],
 "<p class='muted' style='font-size:12px'>opes: opens. chalice: cup (here, a flower's cup). fain would be: would gladly be. carol: a joyful song.</p>")

TOOLS = ('<svg viewBox="0 0 660 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Figurative language toolkit">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The figurative language toolkit</text>'
  + ''.join(f'<rect x="{x}" y="{y}" width="205" height="88" rx="10" fill="{c}"/><text x="{x+102}" y="{y+22}" text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">{t}</text><text x="{x+102}" y="{y+42}" text-anchor="middle" fill="#fff" font-size="11">{d}</text><text x="{x+102}" y="{y+66}" text-anchor="middle" fill="#fff" font-size="11" font-style="italic">{e1}</text><text x="{x+102}" y="{y+80}" text-anchor="middle" fill="#fff" font-size="11" font-style="italic">{e2}</text>'
            for x, y, c, t, d, e1, e2 in [(12, 34, "#0047BA", "Simile", "compares using like or as", "The lake was as smooth", "as a mirror."),
                                          (227, 34, "#0A1F3D", "Metaphor", "says one thing IS another", "The classroom was", "a zoo."),
                                          (442, 34, "#3d9a2f", "Personification", "human traits for nonhuman things", "The thunder grumbled", "all night."),
                                          (12, 132, "#DB2F30", "Hyperbole", "exaggerates on purpose", "I have a million", "chores today."),
                                          (227, 132, "#C9A84C", "Idiom", "a saying that doesn't mean its words", "It's raining", "cats and dogs."),
                                          (442, 132, "#6b3fa0", "Imagery", "words that appeal to the senses", "the sharp smell of", "rain on hot asphalt")]) +
  '</svg>')

LESSON = {'unit': 'Unit 3: The Power of Poetry',
 'title': 'Figurative Language',
 'subtitle': "Poets say what cannot be said plainly. Similes, metaphors, personification and imagery let a few words carry big feelings, and they shape a poem's tone and meaning.",
 'objectives': ['Identify and explain simile, metaphor, personification, hyperbole, idiom and imagery.',
                'Explain how figurative language contributes to the tone and meaning of a poem.',
                'Analyze personification and implied metaphor in poems by Rossetti and Sandburg.',
                'Trace an extended metaphor and a symbol in poems by Dickinson and Dunbar.',
                'Use the roots sym, path, hyper and phor, and write an original poem using figurative language.'],
 'vocab': [['figurative language', 'Words used in a non-literal way to create a picture or feeling.'],
           ['literal', 'Meaning exactly what the words say.'],
           ['personification', 'Giving human qualities or actions to something that is not human.'],
           ['hyperbole', 'Exaggeration on purpose, for effect.'],
           ['idiom', 'A common saying whose meaning is different from the meaning of its words.'],
           ['symbol', 'Something concrete that stands for a bigger idea, such as a dove for peace.'],
           ['tone', "The speaker's attitude toward the subject, shown through word choice (hopeful, angry, playful)."],
           ['roots sym, path, hyper, phor', 'sym = together (sympathy); path = feeling (empathy); hyper = over, beyond (hyperbole); phor = carry (metaphor: "carry across").']],
 'reconnect': {'title': 'Weeks 10 and 3',
               'intro': 'Unit 3 turns from informational writing to poetry. Connect back first.',
               'items': [{'t': 'text',
                          'q': 'Week 10: what is the one sentence that states the central idea of a whole informational article called?',
                          'a': ['thesis', 'thesis statement', 'a thesis', 'the thesis'],
                          'show': 'the thesis',
                          'pts': 2,
                          'why': 'The thesis states the main idea every section supports.'},
                         {'t': 'open',
                          'key': 'rc_purpose',
                          'q': 'An informational article and a poem can both be about the ocean. How are their purposes different?',
                          'min': 15,
                          'rows': 2,
                          'rubric': ['Article: explain and inform with facts', 'Poem: express feelings, create images, share a perspective through language'],
                          'model': 'An informational article explains facts about the ocean. A poem uses images and feelings to show how the ocean seems or what it means to the speaker.'},
                         {'t': 'open',
                          'key': 'rc_stair',
                          'q': 'Week 3: In "Mother to Son," Langston Hughes compares life to a staircase. What is that kind of comparison called, and what does the "crystal stair" stand for?',
                          'min': 15,
                          'rows': 2,
                          'rubric': ['Extended metaphor', 'Crystal stair: an easy, comfortable, privileged life (which the mother has not had)'],
                          'model': 'It is an extended metaphor. The crystal stair stands for an easy, smooth life, which the mother has never had.'},
                         {'t': 'text',
                          'q': 'Week 10 root review: the root dict means "say." Using pre- (before) + dict, what does it mean to predict something?',
                          'a': [{'all': [['before', 'ahead', 'future', 'will happen', 'in advance']], 'none': ['not', 'after']}],
                          'show': 'to say what will happen before it happens',
                          'pts': 2,
                          'why': 'pre (before) + dict (say). Today: four Greek roots about language and feeling.'}]},
 'hook': {'title': 'Say It Without Saying It',
          'html': '<p>Try to describe how it feels to wait for a test score. You could say, "I was nervous." Or you could say, "My stomach was a washing machine on the spin cycle." Which one makes '
                  'the reader feel it?</p><p>The second sentence is a <b>metaphor</b>, one kind of <b>figurative language</b>. It is not literally true, but it is more true to the feeling. Poets use '
                  "figurative language to carry big emotions in a few words, and the words they choose create the poem's <b>tone</b>, the attitude you hear in its voice.</p><div "
                  "class='callout'><b>Big question:</b> How does figurative language help a poem say what plain words cannot?</div>"},
 'learn': [{'title': 'The Figurative Language Toolkit',
            'visual': '<svg viewBox="0 0 660 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Figurative language toolkit"><text x="330" y="20" '
                      'text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The figurative language toolkit</text><rect x="12" y="34" width="205" height="88" rx="10" '
                      'fill="#0047BA"/><text x="114" y="56" text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">Simile</text><text x="114" y="76" text-anchor="middle" fill="#fff" '
                      'font-size="11">compares using like or as</text><text x="114" y="100" text-anchor="middle" fill="#fff" font-size="11" font-style="italic">The lake was as smooth</text><text '
                      'x="114" y="114" text-anchor="middle" fill="#fff" font-size="11" font-style="italic">as a mirror.</text><rect x="227" y="34" width="205" height="88" rx="10" '
                      'fill="#0A1F3D"/><text x="329" y="56" text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">Metaphor</text><text x="329" y="76" text-anchor="middle" fill="#fff" '
                      'font-size="11">says one thing IS another</text><text x="329" y="100" text-anchor="middle" fill="#fff" font-size="11" font-style="italic">The classroom was</text><text x="329" '
                      'y="114" text-anchor="middle" fill="#fff" font-size="11" font-style="italic">a zoo.</text><rect x="442" y="34" width="205" height="88" rx="10" fill="#3d9a2f"/><text x="544" '
                      'y="56" text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">Personification</text><text x="544" y="76" text-anchor="middle" fill="#fff" font-size="11">gives '
                      'human traits to nonhuman things</text><text x="544" y="100" text-anchor="middle" fill="#fff" font-size="11" font-style="italic">The thunder grumbled</text><text x="544" '
                      'y="114" text-anchor="middle" fill="#fff" font-size="11" font-style="italic">all night.</text><rect x="12" y="132" width="205" height="88" rx="10" fill="#DB2F30"/><text x="114" '
                      'y="154" text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">Hyperbole</text><text x="114" y="174" text-anchor="middle" fill="#fff" font-size="11">exaggerates on '
                      'purpose</text><text x="114" y="198" text-anchor="middle" fill="#fff" font-size="11" font-style="italic">I have a million</text><text x="114" y="212" text-anchor="middle" '
                      'fill="#fff" font-size="11" font-style="italic">chores today.</text><rect x="227" y="132" width="205" height="88" rx="10" fill="#C9A84C"/><text x="329" y="154" '
                      'text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">Idiom</text><text x="329" y="174" text-anchor="middle" fill="#fff" font-size="11">a saying that doesn\'t '
                      'mean its words</text><text x="329" y="198" text-anchor="middle" fill="#fff" font-size="11" font-style="italic">It\'s raining</text><text x="329" y="212" text-anchor="middle" '
                      'fill="#fff" font-size="11" font-style="italic">cats and dogs.</text><rect x="442" y="132" width="205" height="88" rx="10" fill="#6b3fa0"/><text x="544" y="154" '
                      'text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">Imagery</text><text x="544" y="174" text-anchor="middle" fill="#fff" font-size="11">words that appeal to the '
                      'senses</text><text x="544" y="198" text-anchor="middle" fill="#fff" font-size="11" font-style="italic">the sharp smell of</text><text x="544" y="212" text-anchor="middle" '
                      'fill="#fff" font-size="11" font-style="italic">rain on hot asphalt</text></svg>',
            'html': '<p>You met similes, metaphors and imagery earlier this year. Now add three more tools, and look at imagery again:</p><ul><li><b>Personification</b> gives human traits to things '
                    'that are not human: "The old house groaned in the wind."</li><li><b>Hyperbole</b> exaggerates for effect: "This backpack weighs a ton."</li><li><b>Idioms</b> are sayings that '
                    'don\'t mean their literal words: "Break a leg" means good luck. Idioms differ between languages; in French, a heavy rain is "il pleut des cordes," it\'s raining '
                    'ropes.</li><li><b>Imagery</b> uses details that appeal to the five senses, so the reader can see, hear, smell, taste or feel the scene.</li></ul><p>Figurative language also '
                    'creates <b>tone</b>. Compare "The thunder grumbled" (annoyed, a little funny) with "The thunder roared" (powerful, frightening). Same event, different '
                    'attitude.</p><p><b>Roots:</b> <i>metaphor</i> comes from Greek <i>meta</i> (across) + <i>phor</i> (carry): a metaphor carries meaning from one thing to another. <i>Hyperbole</i> '
                    'comes from <i>hyper</i> (over, beyond): it goes over the top.</p>',
            'checks': [{'t': 'blanks',
                        'q': 'Name the figurative language in each sentence.',
                        'sent': '"My little brother is a tornado in the kitchen." ___ &nbsp; "I\'ve told you a thousand times!" ___ &nbsp; "The stars winked at us." ___',
                        'blanks': [[{'all': [['metaphor']], 'none': ['not', 'extended']}],
                                   [{'all': [['hyperbole', 'exaggeration']], 'none': ['not']}],
                                   [{'all': [['personification', 'personified', 'personify']], 'none': ['not']}]],
                        'show': 'metaphor; hyperbole; personification',
                        'pts': 3,
                        'why': 'He IS a tornado (metaphor); a thousand times is an exaggeration (hyperbole); stars cannot wink (personification).'},
                       {'t': 'open',
                        'key': 'tone1',
                        'q': 'Rewrite "The wind blew" twice: once with personification that creates a gentle tone, and once with personification that creates a frightening tone. Explain which words '
                             'changed the tone.',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Gentle personification (e.g. the wind hummed a lullaby)',
                                   'Frightening personification (e.g. the wind clawed at the windows)',
                                   'Explains the word choices that create each tone'],
                        'model': 'Gentle: The wind hummed through the pines like a lullaby. Frightening: The wind howled and clawed at the windows. Hummed and lullaby feel soft and calm, while '
                                 'howled and clawed make the wind sound like an attacking animal.'},
                       {'t': 'open',
                        'key': 'idiom',
                        'q': 'Explain the meaning of the idiom "to be on the same page." Then describe how someone learning English might misunderstand it.',
                        'min': 20,
                        'rows': 2,
                        'rubric': ['Meaning: to agree or understand the same way', 'Literal misunderstanding: reading the same page of a book'],
                        'model': 'It means two people agree or understand something the same way. Someone learning English might think it means reading the same page of a book.'}]},
           {'title': 'Personification and Implied Metaphor: Rossetti and Sandburg',
            'html': "<div class='card' style='border-left-color:#C9A84C'><h3 style='margin-top:0'>Who Has Seen the Wind?</h3><p class='muted' style='margin-top:-6px'>Christina Rossetti (1872)</p><p "
                    "style='font-family:Georgia,serif;font-size:17px;line-height:1.7'>Who has seen the wind?<br>Neither I nor you:<br>But when the leaves hang trembling,<br>The wind is passing "
                    "through.<br>&nbsp;<br>Who has seen the wind?<br>Neither you nor I:<br>But when the trees bow down their heads,<br>The wind is passing by.</p></div><div class='card' "
                    "style='border-left-color:#C9A84C'><h3 style='margin-top:0'>Fog</h3><p class='muted' style='margin-top:-6px'>Carl Sandburg (1916)</p><p "
                    "style='font-family:Georgia,serif;font-size:17px;line-height:1.7'>The fog comes<br>on little cat feet.<br>&nbsp;<br>It sits looking<br>over harbor and city<br>on silent "
                    "haunches<br>and then moves on.</p><p class='muted' style='font-size:12px'>haunches: the back legs and hips of an animal sitting down</p></div><p>In Rossetti's poem, no one can "
                    'see the wind, but we know it is there because of what it does. The leaves <b>hang trembling</b> and the trees <b>bow down their heads</b>: both are personification. Trembling '
                    'suggests fear or shyness; bowing suggests respect, as if the trees were greeting someone powerful passing by.</p><p>Sandburg never says "the fog is a cat," but every detail '
                    'makes it one: <b>little cat feet</b>, <b>sits looking</b>, <b>silent haunches</b>, <b>moves on</b>. This is an <b>implied metaphor</b>: the comparison is shown, not stated. The '
                    "poem's tone is quiet and calm, like a cat that comes and goes as it pleases.</p>",
            'checks': [{'t': 'open',
                        'key': 'trees',
                        'q': 'In "Who Has Seen the Wind?", what do the personified leaves and trees help the reader understand about the wind, which no one can see?',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['We know the wind by its effects: trembling leaves and bowing trees',
                                   'The personification makes the wind seem powerful or important, like someone the trees respect or fear'],
                        'model': 'They show that we can know the wind only by what it does: the leaves tremble and the trees bow. Making the trees bow like people suggests the wind is powerful, like '
                                 'a ruler passing by.'},
                       {'t': 'open',
                        'key': 'fogcat',
                        'q': 'List three details Sandburg uses to turn the fog into a cat, and explain what the comparison tells you about how fog moves.',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Three details: little cat feet, sits looking, silent haunches, moves on', 'Fog arrives silently and softly, stays for a while, and leaves on its own'],
                        'model': 'The fog comes on little cat feet, sits looking over the harbor, rests on silent haunches and moves on. Like a cat, fog arrives quietly, stays still for a while and '
                                 'then leaves whenever it wants.'},
                       {'t': 'text',
                        'q': 'Sandburg never says "the fog is a cat"; he only shows it with details. What is this kind of metaphor called?',
                        'a': [{'all': [['implied', 'implicit']], 'none': ['not implied', 'not implicit', 'extended metaphor']}],
                        'show': 'an implied metaphor',
                        'pts': 2,
                        'why': 'An implied metaphor shows the comparison without stating it.'}]},
           {'title': 'Extended Metaphor and Tone: Dickinson',
            'html': "<div class='card' style='border-left-color:#C9A84C'><h3 style='margin-top:0'>“Hope” is the thing with feathers</h3><p class='muted' style='margin-top:-6px'>Emily Dickinson "
                    "(written about 1861; published 1891)</p><p style='font-family:Georgia,serif;font-size:17px;line-height:1.7'>“Hope” is the thing with feathers –<br>That perches in the soul "
                    '–<br>And sings the tune without the words –<br>And never stops – at all –<br>&nbsp;<br>And sweetest – in the Gale – is heard –<br>And sore must be the storm –<br>That could '
                    'abash the little Bird<br>That kept so many warm –<br>&nbsp;<br>I’ve heard it in the chillest land –<br>And on the strangest Sea –<br>Yet – never – in Extremity,<br>It asked a '
                    "crumb – of Me.</p><p class='muted' style='font-size:12px'>Gale: a strong wind. abash: embarrass, make shy. Extremity: the worst, most desperate moment.</p></div><p>Dickinson "
                    "turns hope into a small bird that lives inside a person. This is an <b>extended metaphor</b>, like Hughes's staircase in Week 3: the comparison continues through the whole "
                    'poem.</p><ul><li>Stanza 1: the bird <b>perches in the soul</b> and sings a tune <b>without the words</b>. Hope does not need reasons; it just keeps going.</li><li>Stanza 2: the '
                    'song is <b>sweetest in the gale</b>. Hope matters most during hard times, and only a terrible storm could silence it.</li><li>Stanza 3: the bird has sung in the coldest, '
                    'strangest places, yet it <b>never asked a crumb</b>. Hope gives and gives but asks for nothing in return.</li></ul><p>The tone is warm, grateful and quietly strong. (In her '
                    'handwritten copy, Dickinson used many dashes; the editors of the 1891 printing changed them to commas and other regular punctuation.)</p>',
            'checks': [{'t': 'open',
                        'key': 'hopebird',
                        'q': 'Why do you think Dickinson chose a small bird, not an eagle or a lion, to represent hope? Use details from the poem.',
                        'min': 30,
                        'rows': 3,
                        'rubric': ['A small bird is gentle and easy to overlook, yet keeps singing; it "kept so many warm"',
                                   'Hope is quiet and modest but surprisingly strong; it survives storms and "never asked a crumb"'],
                        'model': 'A small bird is quiet and easy to overlook, just like hope inside a person. But this little bird keeps singing through gales and storms and asks for nothing, so '
                                 'Dickinson shows that hope is gentle but surprisingly strong.'},
                       {'t': 'open',
                        'key': 'hopetone',
                        'q': 'Describe the tone of the poem in one or two words, and quote two words or phrases that create that tone.',
                        'min': 20,
                        'rows': 2,
                        'rubric': ['A fitting tone word (hopeful, grateful, admiring, warm, comforting)', 'Two supporting quotations (sweetest, kept so many warm, never stops, never asked a crumb)'],
                        'model': 'The tone is grateful and admiring. Phrases like "sweetest in the gale" and "kept so many warm" show how much the speaker values hope.'},
                       {'t': 'open',
                        'key': 'crumb',
                        'q': 'What does the last line, "It asked a crumb of me," mean? Why is it a powerful ending?',
                        'min': 20,
                        'rows': 2,
                        'rubric': ['Hope never asked for anything in return; it is a free gift',
                                   'It surprises the reader and shows gratitude; the bird metaphor continues to the very end (birds eat crumbs)'],
                        'model': 'It means hope never asked for anything in return, not even a crumb, which is what you would give a bird. It is powerful because it ends the bird metaphor and shows '
                                 'how freely hope gives.'},
                       {'t': 'blanks',
                        'q': 'Complete the sentences.',
                        'sent': 'Dickinson compares hope to a ___. Because the comparison continues through all three stanzas, it is an ___ metaphor.',
                        'blanks': [[{'all': [['bird']], 'none': ['not']}], [{'all': [['extended']], 'none': ['not', 'implied']}]],
                        'show': 'bird; extended',
                        'pts': 2,
                        'why': 'Hope is a small bird from the first line to the last.'}]},
           {'title': 'Imagery and Symbol: Dunbar\'s "Sympathy"',
            'html': "<div class='card' style='border-left-color:#C9A84C'><h3 style='margin-top:0'>Sympathy</h3><p class='muted' style='margin-top:-6px'>Paul Laurence Dunbar (1899)</p><p "
                    "style='font-family:Georgia,serif;font-size:17px;line-height:1.7'>I know what the caged bird feels, alas!<br>When the sun is bright on the upland slopes;<br>When the wind stirs "
                    'soft through the springing grass,<br>And the river flows like a stream of glass;<br>When the first bird sings and the first bud opes,<br>And the faint perfume from its chalice '
                    'steals —<br>I know what the caged bird feels!<br>&nbsp;<br>I know why the caged bird beats his wing<br>Till its blood is red on the cruel bars;<br>For he must fly back to his '
                    'perch and cling<br>When he fain would be on the bough a-swing;<br>And a pain still throbs in the old, old scars<br>And they pulse again with a keener sting —<br>I know why he '
                    'beats his wing!<br>&nbsp;<br>I know why the caged bird sings, ah me,<br>When his wing is bruised and his bosom sore, —<br>When he beats his bars and he would be free;<br>It is '
                    'not a carol of joy or glee,<br>But a prayer that he sends from his heart’s deep core,<br>But a plea, that upward to Heaven he flings —<br>I know why the caged bird sings!</p><p '
                    "class='muted' style='font-size:12px'>opes: opens. chalice: cup (here, a flower's cup). fain would be: would gladly be. carol: a joyful song.</p></div><p>Paul Laurence Dunbar "
                    '(1872 to 1906) was the son of parents who had been enslaved in Kentucky. He became one of the first Black American poets to gain national fame. In "Sympathy," a bird trapped in '
                    'a cage becomes a <b>symbol</b>: it stands for a person whose freedom has been taken away, and many readers connect it to Black Americans living under racism and segregation in '
                    "Dunbar's time.</p><p>The bird in this poem is not a real bird that someone hurt. Dunbar created it as a symbol so readers could feel what losing freedom does to a person. Stanza "
                    '2 describes pain directly, so read it slowly and talk about it.</p><p>Stanza 1 is full of <b>imagery</b> of freedom: bright sun, soft wind, the river <b>like a stream of '
                    "glass</b> (a simile). Stanza 2 turns painful: the bird beats its wing <b>till its blood is red on the cruel bars</b>. Stanza 3 reveals that the bird's song is not joy but <b>a "
                    'prayer</b> and <b>a plea</b>.</p><p>The title, "Sympathy," comes from Greek <i>sym</i> (together) + <i>path</i> (feeling): feeling together with someone. The repeated line "I '
                    'know" tells us the speaker shares the bird\'s suffering. Seventy years later, Maya Angelou took the title of her famous memoir, <i>I Know Why the Caged Bird Sings</i> (1969), '
                    'from this poem.</p>',
            'checks': [{'t': 'blanks',
                        'q': 'Name the device.',
                        'sent': '"the river flows like a stream of glass" ___ &nbsp; The caged bird stands for a person who has lost freedom, so the bird is a ___.',
                        'blanks': [[{'all': [['simile']], 'none': ['not', 'metaphor']}], [{'all': [['symbol']], 'none': ['not']}]],
                        'show': 'simile; symbol',
                        'pts': 2,
                        'why': 'like signals a simile; a concrete thing standing for a bigger idea is a symbol.'},
                       {'t': 'open',
                        'key': 'stanza1',
                        'q': "Why does Dunbar fill the first stanza with images of a beautiful spring day? How does that make the caged bird's situation feel?",
                        'min': 23,
                        'rows': 3,
                        'rubric': ['The images show the freedom and beauty the bird can see but cannot reach', 'The contrast makes the cage feel more painful and unfair'],
                        'model': 'The sunny slopes, soft wind and glassy river show everything the bird can see but cannot reach. That contrast makes being trapped feel even more painful and '
                                 'unfair.'},
                       {'t': 'open',
                        'key': 'song',
                        'q': 'In stanza 3, the speaker says the bird\'s song "is not a carol of joy or glee." What is it instead, and how does that change the meaning of a bird\'s song?',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['A prayer and a plea for freedom', 'A song we might hear as happy is really a cry of suffering and hope; outsiders misunderstand'],
                        'model': 'It is a prayer and a plea sent up to Heaven. Something people might hear as a happy song is really a cry for freedom, which shows that others may not understand the '
                                 'pain of someone who is not free.'},
                       {'t': 'text',
                        'q': 'The title "Sympathy" combines the roots sym and path. What does path mean?',
                        'a': [{'all': [['feel', 'emotion', 'suffer']], 'none': ['not', 'road', 'a way']}],
                        'show': 'feeling',
                        'pts': 2,
                        'why': 'path = feeling or suffering; sym = together. Sympathy: feeling together with someone.'},
                       {'t': 'open',
                        'key': 'symtone',
                        'q': 'How does the tone of "Sympathy" differ from the tone of Dickinson\'s poem, even though both use a bird? Use one quotation from each.',
                        'min': 35,
                        'rows': 3,
                        'rubric': ['Dickinson: hopeful, grateful (e.g. "sweetest in the gale")',
                                   'Dunbar: painful, sorrowful, pleading, angry at injustice (e.g. "cruel bars", "a plea")',
                                   'Explains how word choice creates each tone'],
                        'model': 'Dickinson\'s tone is hopeful and grateful: her bird sings "sweetest in the Gale." Dunbar\'s tone is sorrowful and pleading: his bird beats against "the cruel bars" '
                                 'and sings "a plea." Dickinson\'s bird is free inside the soul, but Dunbar\'s bird is trapped, so his words are full of pain.'}]}],
 'handson': {'title': 'Weather Poem: Personify a Florida Storm',
             'intro': 'Observe the weather, collect sensory images, and write a poem that turns a Florida weather event into a character.',
             'materials': ['A notebook and pencil',
                           'Five minutes outdoors or at a window, ideally during rain, wind, heat or a thunderstorm (watch lightning from indoors)',
                           'Index cards or sticky notes',
                           'A family audience'],
             'steps': ['Spend five minutes observing the weather. On cards, write one detail for each sense (sight, sound, smell, touch, and taste if safe, such as salty air).',
                       'Choose one weather event: a summer thunderstorm, a hurricane, a heat wave, sea fog or a cold front.',
                       'Decide what kind of character it will be (an angry giant, a tired old man, a playful puppy) and what tone you want.',
                       'Write a poem of 8 to 14 lines. Use personification throughout as an extended metaphor, plus at least one simile, one example of imagery and one hyperbole.',
                       'Read it aloud to your family and ask them to name the tone.'],
             'record': [{'t': 'open',
                         'key': 'weatherpoem',
                         'q': 'Write your final poem here, with a title.',
                         'min': 50,
                         'rows': 12,
                         'rubric': ['8 to 14 lines with a title',
                                    'Extended personification of a weather event',
                                    'At least one simile, one image and one hyperbole',
                                    'A consistent tone created by word choice'],
                         'model': 'The Afternoon Storm\n'
                                  "At three o'clock the storm wakes up,\n"
                                  'stretching gray arms across the sky.\n'
                                  'He clears his throat in a thunder cough\n'
                                  'that rattles every window in Arcadia.\n'
                                  'He stomps through the orange groves\n'
                                  'like a giant late for school,\n'
                                  'spilling a million buckets on the road,\n'
                                  'and the hot asphalt hisses back at him.\n'
                                  'By five he is tired.\n'
                                  'He shuffles east toward the coast,\n'
                                  'dragging his wet coat behind him,\n'
                                  "and the sun peeks out to see if he's gone."},
                        {'t': 'open',
                         'key': 'poemlabel',
                         'q': 'Label the figurative language in your poem (quote each example and name it). What tone did your family hear? Is it the tone you intended?',
                         'min': 30,
                         'rows': 4,
                         'rubric': ['Each required device quoted and named correctly', "Reports the family's tone word and compares it with the intended tone"],
                         'model': 'Personification: "the storm wakes up," "he stomps." Simile: "like a giant late for school." Hyperbole: "a million buckets." Imagery: "the hot asphalt hisses." My '
                                  'family said the tone was playful, which is what I wanted, even though storms can be scary.'}]},
 'think': {'intro': 'Write in complete sentences. Your teacher scores these.',
           'items': [{'t': 'open',
                      'key': 'analysis',
                      'q': "Choose one of today's four poems. Write a paragraph explaining how its figurative language creates its tone and meaning. Include at least two quotations and explain each "
                           'one.',
                      'min': 96,
                      'rows': 10,
                      'rubric': ['Names the poem and a clear claim about tone and meaning',
                                 'Two or more accurate quotations',
                                 "Explains how each quotation's figurative language creates the tone or meaning",
                                 'Organized paragraph with a concluding sentence'],
                      'model': 'In "Sympathy," Paul Laurence Dunbar uses the symbol of a caged bird to create a tone of sorrow and longing for freedom. In the first stanza, imagery like "the river '
                               'flows like a stream of glass" shows the beautiful, free world the bird can see but cannot reach. In the second stanza, the image of blood "red on the cruel bars" '
                               'turns the tone painful, because the bird keeps fighting a cage it cannot escape. Finally, Dunbar reveals that the bird\'s song is "a prayer" and "a plea," not joy, '
                               'which shows that people denied freedom still hope. Through these images, Dunbar helps readers feel what it means to be trapped by injustice.'},
                     {'t': 'open',
                      'key': 'connect',
                      'q': "Dickinson's bird is free inside the soul, while Dunbar's bird is trapped in a cage. Write a short paragraph comparing what each bird represents, and explain which poem "
                           'speaks more to you and why. End with one sentence stating a theme of either poem.',
                      'min': 63,
                      'rows': 6,
                      'rubric': ['Dickinson: hope that lives inside a person and never gives up',
                                 'Dunbar: a person denied freedom, pleading to be free',
                                 'A personal response supported by the text',
                                 'A theme statement (a full sentence, not a topic)'],
                      'model': "Dickinson's bird stands for hope that lives inside every person and keeps singing even in the worst storms. Dunbar's bird stands for a person who has lost their "
                               "freedom and sings only to beg for it. Dunbar's poem speaks to me more, because it reminds me that some people's hope comes from deep suffering, and it makes me think "
                               'about fairness. One theme of "Sympathy" is that people denied freedom still hold on to hope.'}]},
 'exit': [{'t': 'blanks',
           'q': 'Name the figurative language.',
           'sent': '"The waves whispered secrets to the sand." ___ &nbsp; "Her smile was as bright as the sun." ___',
           'blanks': [[{'all': [['personification', 'personified', 'personify']], 'none': ['not']}], [{'all': [['simile']], 'none': ['not']}]],
           'show': 'personification; simile',
           'pts': 2,
           'why': 'Waves cannot whisper (personification); as bright as the sun uses as (simile).'},
          {'t': 'open',
           'key': 'exit_tone',
           'q': 'What is tone, and how does figurative language help create it?',
           'min': 15,
           'rows': 2,
           'rubric': ["Tone: the speaker's attitude toward the subject", 'Word choice and images (e.g. grumbled versus roared) shape the attitude the reader hears'],
           'model': "Tone is the speaker's attitude toward the subject. Figurative language creates it through word choice, like a storm that grumbles sounding annoyed but one that roars sounding "
                    'frightening.'},
          {'t': 'text',
           'q': 'Which root means "over" or "beyond," as in the word for exaggeration on purpose?',
           'a': ['hyper'],
           'show': 'hyper',
           'pts': 2,
           'why': 'hyper = over, beyond: hyperbole goes over the top.'},
          {'t': 'open',
           'key': 'exit_symbol',
           'q': 'In "Sympathy," what does the caged bird symbolize?',
           'min': 10,
           'rows': 2,
           'rubric': ['A person whose freedom is taken away; many readers connect it to Black Americans under racism'],
           'model': "It symbolizes a person whose freedom has been taken away, and many readers connect it to Black Americans facing racism in Dunbar's time."}],
 'next': 'Week 12: the sound and structure of poetry: rhyme, rhythm, repetition and form.'}

TEACHER = {
 "standards": [
  "ELA.6.R.3.1: Explain how figurative language contributes to tone and meaning in text(s).",
  "ELA.6.R.1.2: Analyze the development of stated or implied theme(s) throughout a literary text.",
  "ELA.6.V.1.2: Apply knowledge of Greek and Latin roots and affixes to determine meanings of words and phrases in grade-level content.",
  "ELA.6.C.1.2: Write personal or fictional narratives using narrative techniques, precise words and phrases, and figurative language.",
  "ELA.K12.EE.1.1: Cite evidence to explain and justify reasoning."],
 "materials": ["The interactive lesson", "Index cards, a notebook", "A window or a safe outdoor spot for weather observation", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Reconnect questions."],
  [4, "Hook", "Compare \"I was nervous\" with the washing-machine metaphor."],
  [10, "Toolkit", "Sort example sentences into the six types. Rewrite the wind sentence with two tones."],
  [10, "Rossetti and Sandburg", "Read both poems aloud twice. Find the personification and the cat details."],
  [12, "Dickinson", "Read aloud. Trace the bird stanza by stanza. Discuss the dashes."],
  [14, "Dunbar", "Give the background, then read aloud slowly. Before stanza 2, say the bird is a symbol for people, not a real animal. Invite questions about racism in Dunbar's time (segregation laws, limits on jobs and voting) and answer honestly and briefly; end on stanza 3, where the song is a prayer and a plea. Connect to Maya Angelou."],
  [4, "Assign", "Assign the weather poem, Think Deeper and the Exit Check."]],
 "key_questions": ["What is being compared, and why that comparison?", "What tone do you hear, and which words create it?", "What does this concrete thing stand for?", "How would the poem change if this word were different?"],
 "misconceptions": ["Every comparison is a simile.", "Figurative language is just decoration (it creates meaning and tone).", "Tone is the same as mood (tone is the speaker's attitude; mood is the reader's feeling).", "Idioms mean what their words say."],
 "support": ["Provide a toolkit card with one example of each device.", "Read each poem aloud twice before discussing.", "Use a two-column chart: quotation / what it shows."],
 "challenge": ["Read Langston Hughes's \"Dreams\" and compare its metaphors with Dickinson's.", "Find an idiom in another language your family speaks and explain its literal and real meaning."],
 "background": "<p>All four poems are in the public domain: Rossetti, Sing-Song (1872); Sandburg, Chicago Poems (1916); Dickinson, written about 1861; the text printed is the public-domain first printing (Poems, Second Series, 1891), whose editors regularized her dashes; Dunbar, Lyrics of the Hearthside (1899). Dunbar (1872 to 1906) was born in Dayton, Ohio, to Joshua and Matilda Dunbar, both formerly enslaved in Kentucky. Maya Angelou's I Know Why the Caged Bird Sings (1969) takes its title from \"Sympathy.\" The blood imagery in Dunbar's second stanza may need a brief pause for discussion.</p>",
 "sources": ["Poetry Foundation, Paul Laurence Dunbar.", "Johnson, T. H., ed. (1955), The Poems of Emily Dickinson, Harvard University Press.", "Sandburg, C. (1916), Chicago Poems, Henry Holt.", "Rossetti, C. (1872), Sing-Song: A Nursery Rhyme Book.", "CPALMS, ELA.6.R.3.1."]
}

PRINT = {
 "directions": "Write in complete sentences.",
 "items": [
  {"q":"Write one example each of personification, hyperbole and imagery.","a":"e.g. The car coughed and sputtered; I could eat a horse; the sticky sweetness of a ripe mango.","lines":3},
  {"q":"How does Sandburg make the fog seem like a cat?","a":"Details like little cat feet, sitting and looking, silent haunches, moving on (implied metaphor).","lines":2},
  {"q":"In Dickinson's poem, what is hope compared to, and why?","a":"A small bird that sings in the soul; hope is quiet but strong and asks nothing in return.","lines":2},
  {"q":"What does the caged bird symbolize in \"Sympathy\"?","a":"A person whose freedom is taken away; often read as Black Americans under racism.","lines":2},
  {"q":"Explain tone and give the tone of one poem from today.","a":"Tone is the speaker's attitude; e.g. Dunbar: sorrowful and pleading.","lines":2},
  {"q":"Use the roots: what do sympathy and empathy have in common?","a":"Both contain path (feeling); sympathy = feeling together with someone.","lines":2}]
}
