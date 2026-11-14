def poem(title, author, lines, note=""):
    body = "<br>".join(l if l else "&nbsp;" for l in lines)
    return (f"<div class='card' style='border-left-color:#C9A84C'><h3 style='margin-top:0'>{title}</h3><p class='muted' style='margin-top:-6px'>{author}</p>"
            f"<p style='font-family:Georgia,serif;font-size:17px;line-height:1.7'>{body}</p>{note}</div>")

TRAIN = poem("From a Railway Carriage", "Robert Louis Stevenson (1885)", [
 "Faster than fairies, faster than witches,", "Bridges and houses, hedges and ditches;", "And charging along like troops in a battle,", "All through the meadows the horses and cattle:", "All of the sights of the hill and the plain", "Fly as thick as driving rain;", "And ever again, in the wink of an eye,", "Painted stations whistle by.", "",
 "Here is a child who clambers and scrambles,", "All by himself and gathering brambles;", "Here is a tramp who stands and gazes;", "And there is the green for stringing the daisies!", "Here is a cart run away in the road", "Lumping along with man and load;", "And here is a mill and there is a river:", "Each a glimpse and gone for ever!"],
 "<p class='muted' style='font-size:12px'>carriage: a railroad passenger car. brambles: blackberry bushes. tramp: a person traveling on foot without a home. green: a grassy field.</p>")

PALANQUIN = poem("Palanquin Bearers", "Sarojini Naidu (1905)", [
 "Lightly, O lightly we bear her along,", "She sways like a flower in the wind of our song;", "She skims like a bird on the foam of a stream,", "She floats like a laugh from the lips of a dream.", "Gaily, O gaily we glide and we sing,", "We bear her along like a pearl on a string.", "",
 "Softly, O softly we bear her along,", "She hangs like a star in the dew of our song;", "She springs like a beam on the brow of the tide,", "She falls like a tear from the eyes of a bride.", "Lightly, O lightly we glide and we sing,", "We bear her along like a pearl on a string."],
 "<p class='muted' style='font-size:12px'>palanquin: a covered seat carried on poles on the shoulders of bearers, used in India and other countries. bear: carry.</p>")

HAIKU = ("<div class='card' style='border-left-color:#C9A84C'><h3 style='margin-top:0'>Two haiku from Japan</h3>"
 "<p style='font-family:Georgia,serif;font-size:17px;line-height:1.7'>An old pond:<br>a frog jumps in,<br>the sound of water.</p><p class='muted' style='margin-top:-8px'>Matsuo Bashō (1686), translated by KingCretot Experience. Japanese: <i>furu ike ya / kawazu tobikomu / mizu no oto</i> (5-7-5)</p>"
 "<p style='font-family:Georgia,serif;font-size:17px;line-height:1.7'>Don't swat it!<br>The fly wrings its hands,<br>wrings its feet.</p><p class='muted' style='margin-top:-8px'>Kobayashi Issa (1821), translated by KingCretot Experience. Japanese: <i>yare utsu na / hae ga te wo suri / ashi wo suru</i> (5-7-5)</p>"
 "<p class='muted' style='font-size:12px'>In Japanese, a haiku has 17 sound units in a 5-7-5 pattern. English translations usually cannot keep that count and still keep the meaning.</p></div>")

SONNET = poem("Sonnet 18", "William Shakespeare (1609)", [
 "Shall I compare thee to a summer\u2019s day?", "Thou art more lovely and more temperate:", "Rough winds do shake the darling buds of May,", "And summer\u2019s lease hath all too short a date;",
 "Sometime too hot the eye of heaven shines,", "And often is his gold complexion dimm\u2019d;", "And every fair from fair sometime declines,", "By chance or nature\u2019s changing course untrimm\u2019d;",
 "But thy eternal summer shall not fade,", "Nor lose possession of that fair thou ow\u2019st;", "Nor shall death brag thou wander\u2019st in his shade,", "When in eternal lines to time thou grow\u2019st:",
 "So long as men can breathe or eyes can see,", "So long lives this, and this gives life to thee."],
 "<p class='muted' style='font-size:12px'>thee, thou: you. temperate: mild, calm. lease: a rental agreement for a set time. fair: beauty. untrimm\u2019d: stripped of beauty. ow\u2019st: own. eternal lines: lines of poetry that last forever.</p>")

SOUNDS = ('<svg viewBox="0 0 660 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Sound devices in poetry">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The sound toolkit</text>'
  + ''.join(f'<rect x="{x}" y="{y}" width="205" height="88" rx="10" fill="{c}"/><text x="{x+102}" y="{y+22}" text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">{t}</text><text x="{x+102}" y="{y+42}" text-anchor="middle" fill="#fff" font-size="11">{d}</text><text x="{x+102}" y="{y+66}" text-anchor="middle" fill="#fff" font-size="11" font-style="italic">{e1}</text><text x="{x+102}" y="{y+80}" text-anchor="middle" fill="#fff" font-size="11" font-style="italic">{e2}</text>'
            for x, y, c, t, d, e1, e2 in [(12, 34, "#0047BA", "Rhyme", "words that end with the same sound", "witches / ditches", "battle / cattle"),
                                          (227, 34, "#0A1F3D", "Rhythm", "the beat made by stressed syllables", "FAS-ter than FAIR-ies,", "FAS-ter than WITCH-es"),
                                          (442, 34, "#3d9a2f", "Repetition", "repeating words or lines", "\"Lightly, O lightly\"", "a refrain"),
                                          (12, 132, "#DB2F30", "Alliteration", "same first consonant sounds", "\"gaily we glide\"", "\"houses, hedges\""),
                                          (227, 132, "#C9A84C", "Onomatopoeia", "words that imitate sounds", "buzz, splash, whistle,", "sizzle, thump"),
                                          (442, 132, "#6b3fa0", "Assonance", "repeated vowel sounds", "\"Lightly, O lightly we glide\"", "\"Fly as thick as driving rain\"")]) +
  '</svg>')

SCHEME = ('<svg viewBox="0 0 660 200" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="13" role="img" aria-label="Marking a rhyme scheme">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Marking a rhyme scheme: give each new end sound a new letter</text>'
  + ''.join(f'<text x="40" y="{50+i*18}" font-family="Georgia,serif">{l}</text><text x="560" y="{50+i*18}" font-weight="bold" fill="{c}">{t}</text>'
            for i, (l, t, c) in enumerate([("Faster than fairies, faster than WITCHES,", "a", "#0047BA"), ("Bridges and houses, hedges and DITCHES;", "a", "#0047BA"),
                                            ("And charging along like troops in a BATTLE,", "b", "#DB2F30"), ("All through the meadows the horses and CATTLE:", "b", "#DB2F30"),
                                            ("All of the sights of the hill and the PLAIN", "c", "#3d9a2f"), ("Fly as thick as driving RAIN;", "c", "#3d9a2f"),
                                            ("And ever again, in the wink of an EYE,", "d", "#C9A84C"), ("Painted stations whistle BY.", "d", "#C9A84C")])) +
  '<text x="330" y="194" text-anchor="middle" font-size="12">Pairs of rhyming lines in a row are called couplets: aabbccdd.</text></svg>')

LESSON = {
 "unit": "Unit 3: The Power of Poetry",
 "title": "Sound and Structure in Poetry",
 "subtitle": "Poems are made to be heard. Rhyme, rhythm, repetition and the shape of lines and stanzas let a poem sound like a speeding train, a gentle song or a single quiet moment.",
 "objectives": [
  "Identify rhyme, rhyme scheme, rhythm, repetition, alliteration, assonance and onomatopoeia.",
  "Explain how a poem's sound imitates or supports its meaning.",
  "Describe poetic forms: stanzas, couplets, refrains, the sonnet, free verse and haiku, and how form shapes meaning.",
  "Compare how poets from Scotland, England, India and Japan use sound and structure.",
  "Use the roots son, phon, poe and metr, and write a poem whose rhythm imitates a motion."],
 "vocab": [
  ["rhyme scheme", "The pattern of end rhymes in a poem, marked with letters (aabb, abab)."],
  ["rhythm", "The beat of a poem, created by stressed and unstressed syllables."],
  ["stanza", "A group of lines in a poem, like a paragraph in prose."],
  ["couplet", "Two lines in a row that rhyme."],
  ["refrain", "A line or phrase repeated at regular places in a poem or song."],
  ["alliteration", "Repeating the same beginning consonant sound in nearby words."],
  ["onomatopoeia", "A word that imitates the sound it names, such as buzz."],
  ["roots son, phon, poe, metr", "son = sound (sonic); phon = sound (symphony); poe = make (poem, onomatopoeia: \"name-making\"); metr = measure (meter)."]],
 "reconnect": {
  "title": "Week 11: Figurative language",
  "intro": "Last week was about what poems compare. This week is about how poems sound. Review first.",
  "items": [
   {"t":"blanks","q":"Name the figurative language.","sent":"\"The fog comes on little cat feet.\" ___ metaphor &nbsp; \"The trees bow down their heads.\" ___","blanks":[[{"all":[["implied","implicit"]],"none":["not","extended"]}],[{"all":[["personification"]],"none":["not"]}]],"show":"implied; personification","pts":2,"why":"Sandburg shows the fog as a cat without saying so (implied metaphor); trees cannot bow their heads (personification)."},
   {"t":"open","key":"rc_tone","q":"What is tone? Give the tone of Dunbar's \"Sympathy\" in one or two words.","min":10,"rows":2,"rubric":["Tone: the speaker's attitude toward the subject","Sorrowful, pleading, pained (or similar)"],"model":"Tone is the speaker's attitude toward the subject. \"Sympathy\" has a sorrowful, pleading tone."},
   {"t":"open","key":"rc_iknow","q":"Dunbar repeats the line \"I know\" in every stanza of \"Sympathy.\" What effect does that repetition have?","min":15,"rows":2,"rubric":["Emphasizes that the speaker shares and understands the bird's pain; builds feeling; ties the stanzas together"],"model":"The repetition keeps reminding us that the speaker truly understands the bird's pain from experience, and it makes the feeling grow stronger with each stanza."},
   {"t":"text","q":"Which root means \"feeling,\" as in sympathy and empathy?","a":["path"],"show":"path","pts":2,"why":"path = feeling. Today's roots are about sound."}]},
 "hook": {
  "title": "Can a Poem Sound Like a Train?",
  "html": "<p>Read this line out loud, quickly: <i>\"Faster than fairies, faster than witches.\"</i> Now tap the table on the loud syllables: FAS-ter than FAIR-ies, FAS-ter than WITCH-es. Hear the beat? It sounds like train wheels clattering over the tracks.</p><p>Robert Louis Stevenson wrote that poem in 1885, when a fast train ride was still a thrilling adventure for a child. He did not just describe a fast train. He made the poem <b>sound</b> like one.</p><div class='callout'><b>Big question:</b> How do a poem's sounds and structure help create its meaning?</div>"},
 "learn": [
  {"title": "The Sound Toolkit",
   "visual": SOUNDS,
   "html": "<p>Poetry began as something spoken and sung, long before most people could read. Its sound tools helped listeners remember it and feel it:</p><ul><li><b>Rhyme:</b> words with the same ending sound. <b>End rhymes</b> come at the ends of lines; <b>internal rhymes</b> come inside a line.</li><li><b>Rhythm:</b> the pattern of stressed (strong) and unstressed (weak) syllables. A regular rhythm is called <b>meter</b>.</li><li><b>Repetition</b> and <b>refrains:</b> repeated words or lines that create emphasis and a song-like feel.</li><li><b>Alliteration:</b> repeated beginning consonant sounds: <i>gaily we glide</i>.</li><li><b>Assonance:</b> repeated vowel sounds: <i>Lightly, O lightly we glide</i> (long i).</li><li><b>Onomatopoeia:</b> words that sound like what they mean: <i>whistle, splash, buzz</i>.</li></ul><p><b>Roots:</b> <i>phon</i> and <i>son</i> both mean sound (phonics, symphony, sonic). <i>Poe</i> comes from Greek for \"make\": a poet is a maker, and <i>onomatopoeia</i> means \"making a name.\" <i>Metr</i> means measure: meter measures the beat.</p>",
   "checks": [
    {"t":"blanks","q":"Name the sound device.","sent":"\"Peter Piper picked a peck of pickled peppers.\" ___ &nbsp; \"The bacon sizzled and popped.\" ___ &nbsp; \"Go slow over the road.\" ___","blanks":[[{"all":[["alliteration"]],"none":["not"]}],[{"all":[["onomatopoeia"]],"none":["not"]}],[{"all":[["assonance"]],"none":["not"]}]],"show":"alliteration; onomatopoeia; assonance","pts":3,"why":"Repeated p sounds (alliteration); sizzled and popped imitate sounds (onomatopoeia); repeated long o sound (assonance)."},
    {"t":"open","key":"oral","q":"Why do you think rhyme, rhythm and repetition were so important when poems were mostly spoken or sung, not written?","min":20,"rows":2,"rubric":["They help people memorize and pass poems on","They make poems pleasant and powerful to hear"],"model":"Before most people could read, poems had to be remembered. Rhyme, rhythm and repetition make words easier to memorize and pass on, and they make a poem enjoyable to hear."},
    {"t":"text","q":"Which root, meaning \"sound,\" appears in symphony, phonics and telephone?","a":["phon","phone"],"show":"phon","pts":2,"why":"phon = sound. Telephone: tele (far) + phon (sound)."}]},
  {"title": "Rhythm and Rhyme That Move: Stevenson",
   "visual": SCHEME,
   "html": TRAIN + "<p>Stevenson's poem is built from <b>couplets</b>: pairs of rhyming lines (aabbccdd). The quick rhymes come one after another like stations flashing past.</p><p>The rhythm is mostly a strong beat followed by two weak ones: FAS-ter than FAIR-ies. That galloping pattern imitates the clatter of wheels on rails. Notice how the poem lists sights without stopping: bridges, houses, hedges, ditches, a child, a tramp, a cart, a mill. We see each one for only an instant, just as a passenger would. The last line, <i>Each a glimpse and gone for ever!</i>, sums up the experience of speed.</p>",
   "checks": [
    {"t":"text","q":"What is the rhyme scheme of lines 9 to 12 (the start of stanza 2) of \"From a Railway Carriage\"? Type the four letters with no spaces.","a":["aabb"],"show":"aabb","pts":2,"why":"scrambles/brambles (a), gazes/daisies (b)."},
    {"t":"open","key":"trainrhythm","q":"Explain how the rhythm and the long list of sights help the poem feel like a fast train ride.","min":30,"rows":3,"rubric":["The galloping beat imitates wheels clattering on the rails","The rapid list of sights, each seen for an instant, mimics scenery flashing past","Uses evidence from the poem"],"model":"The beat, FAS-ter than FAIR-ies, sounds like wheels clattering on the tracks. The poem also rushes through a list of sights, bridges, hedges, a child, a cart, without stopping on any of them, so we see each one for only a moment, just like looking out the window of a speeding train."},
    {"t":"open","key":"onomat","q":"Find one example of onomatopoeia or alliteration in the poem, and explain what it adds.","min":15,"rows":2,"rubric":["A real example (whistle; faster/fairies; hedges/houses; clambers and scrambles)","Explains its effect (sound of the train, speed, liveliness)"],"model":"\"Painted stations whistle by\" uses onomatopoeia: whistle sounds like the rush of air as the train passes, so we can hear the speed."}]},
  {"title": "Repetition and Refrain: Naidu",
   "html": PALANQUIN + "<p><b>Sarojini Naidu</b> (1879 to 1949) was one of India's most celebrated poets, called \"the Nightingale of India.\" She was also a leader in India's struggle for independence from British rule and became the first woman governor in India, of the United Provinces (today's Uttar Pradesh), in 1947.</p><p>\"Palanquin Bearers\" is written in the voice of the men carrying a bride in a palanquin. Its rhythm is a rocking, swaying beat: LIGHT-ly, O LIGHT-ly we BEAR her a-LONG. Read it aloud and you can feel the bearers' steady steps and the palanquin swaying on their shoulders.</p><p>The poem uses <b>repetition</b> everywhere: <i>Lightly, O lightly</i>; <i>Gaily, O gaily</i>; <i>Softly, O softly</i>. The last line of each stanza, <i>We bear her along like a pearl on a string</i>, is a <b>refrain</b>. Eight of the twelve lines also hold a simile (<i>like a flower</i>, <i>like a bird</i>, <i>like a laugh</i>), so sound and figurative language work together to show how gently and proudly the bearers carry her.</p>",
   "checks": [
    {"t":"open","key":"sway","q":"Read \"Palanquin Bearers\" aloud. How does its rhythm imitate the motion of carrying a palanquin?","min":25,"rows":3,"rubric":["A steady, swaying beat like walking in step","The repeated rocking pattern (LIGHT-ly, O LIGHT-ly) mimics the palanquin swaying"],"model":"The rhythm has a steady, rocking beat, LIGHT-ly, O LIGHT-ly we BEAR her a-LONG, like the bearers walking in step and the palanquin swaying gently on their shoulders."},
    {"t":"text","q":"Which line is repeated at the end of both stanzas as a refrain? Type the last six words.","a":[{"all":[["pearl"],["string"]],"none":["not"]}],"show":"like a pearl on a string","pts":2,"why":"\"We bear her along like a pearl on a string.\""},
    {"t":"open","key":"pearl","q":"The bearers say they carry the bride \"like a pearl on a string.\" What does that simile tell us about how they feel about her and their task?","min":20,"rows":2,"rubric":["She is precious, valuable and delicate","They carry her carefully, proudly and smoothly"],"model":"A pearl is precious and delicate, so the simile shows the bearers treat the bride as something valuable and carry her with great care and pride."},
    {"t":"open","key":"compare2","q":"Both Stevenson's and Naidu's poems use rhythm to imitate motion. How are the two motions and their rhythms different?","min":25,"rows":3,"rubric":["Stevenson: fast, rushing, clattering motion of a train","Naidu: gentle, swaying, steady motion of walking bearers","Rhythm speed and feel differ to match"],"model":"Stevenson's poem rushes with a quick, clattering beat to match a speeding train. Naidu's poem sways with a slower, gentle, steady beat to match men walking in step while carrying a bride."}]},
  {"title": "A Fixed Form: The Sonnet",
   "html": SONNET + "<p>A <b>sonnet</b> is a 14-line poem with a fixed rhyme scheme and rhythm. Shakespeare's sonnets follow this pattern: three quatrains (four-line groups) rhyming <b>abab cdcd efef</b>, then a rhyming couplet, <b>gg</b>. Each line has ten syllables in a da-DUM rhythm (iambic pentameter): shall I com-PARE thee TO a SUM-mer\u2019s DAY.</p><p>The form shapes the meaning. In lines 1 to 8, the speaker lists ways a summer day falls short: it is too windy, too short, sometimes too hot or cloudy, and all beauty fades. Line 9 begins with <b>But</b>, the turn (in Italian, <i>volta</i>): the person he loves will never fade. The final couplet explains why: as long as people read this poem, it keeps that beauty alive. The tight form lets the poem build a problem and then snap shut with an answer.</p>",
   "checks": [
    {"t":"text","q":"What is the rhyme scheme of the first quatrain (lines 1 to 4) of Sonnet 18? Type the four letters with no spaces.","a":["abab"],"show":"abab","pts":2,"why":"day/May (a), temperate/date (b)."},
    {"t":"open","key":"volta","q":"Where does the sonnet turn, and what changes at that point?","min":20,"rows":2,"rubric":["Line 9, at \"But\"","From summer's flaws and how beauty fades to the beloved's eternal beauty that will not fade"],"model":"It turns at line 9 with \"But.\" Before that, the speaker shows how summer and all beauty fade; after it, he says the person he loves will never fade."},
    {"t":"open","key":"couplet","q":"What does the final couplet claim, and how does the sonnet's form help it end with force?","min":25,"rows":3,"rubric":["As long as people live and read, the poem lives and keeps the beloved alive","The rhyming couplet comes after three quatrains, closing the argument like a final punch line"],"model":"It claims that as long as people breathe and read, this poem will live and keep the beloved's beauty alive. After twelve lines of building, the rhyming couplet snaps the argument shut like a final punch line."}]},
  {"title": "Structure: Stanzas, Free Verse and Haiku",
   "html": HAIKU + "<p>Structure is how a poem is built: its lines, stanzas and patterns.</p><ul><li><b>Stanzas</b> are groups of lines, like paragraphs. Naidu uses two six-line stanzas that mirror each other.</li><li><b>Free verse</b> has no regular rhyme or meter; the poet shapes the lines by sense and breath. Sandburg's \"Fog\" (Week 11) is free verse.</li><li><b>Haiku</b> is a Japanese form that captures a single moment in nature in three short lines. In Japanese, it has 17 sound units (5-7-5) and usually a season word.</li></ul><p>Bashō's haiku sets a silent old pond against the sudden splash of a frog: one tiny sound makes the stillness feel even deeper. Issa's haiku turns an annoying fly into a tiny creature begging for its life; the repeated <i>wrings</i> makes us look closely and feel compassion.</p>",
   "checks": [
    {"t":"open","key":"pond","q":"Bashō's haiku has only three short lines. How does the sound of the frog's splash change the feeling of the old pond?","min":20,"rows":2,"rubric":["The sudden sound breaks the silence","The contrast makes the stillness feel deeper or the moment more vivid"],"model":"The pond is old and quiet, and the sudden splash breaks the silence for just a moment. That contrast makes us notice how still and peaceful the pond is."},
    {"t":"open","key":"issa","q":"Why do you think Issa repeats the word \"wrings\"? What does the fly seem to be doing?","min":20,"rows":2,"rubric":["The fly rubbing its legs looks like a person wringing hands, as if begging","Repetition makes us look closely and feel compassion"],"model":"Flies rub their legs together, which looks like wringing hands, as if the fly is begging not to be swatted. Repeating \"wrings\" makes us look closely and feel sorry for it."},
    {"t":"text","q":"What is the name for poetry with no regular rhyme or meter?","a":[{"all":[["free verse","freeverse"]],"none":["not"]}],"show":"free verse","pts":2,"why":"Free verse, like Sandburg's \"Fog.\""}]}],
 "handson": {
  "title": "Rhythm in Motion",
  "intro": "Feel rhythm in your body, then write a poem whose rhythm imitates a motion.",
  "materials": ["The three poems from the lesson", "A table to tap or a drum (a pot and a wooden spoon work)", "A phone to record (optional)", "Paper and pencil", "Space to walk or march"],
  "steps": [
   "Tap the beat of \"From a Railway Carriage\" on the table while reading it aloud. Speed up. Does it feel more like a train?",
   "Walk slowly around the room in step while reading \"Palanquin Bearers\" aloud with a family member, as if carrying something precious together.",
   "Choose a motion from your own life: a rocking chair, a bicycle, a swing, a washing machine, rain on a tin roof, a basketball dribble.",
   "Write a poem of 8 to 12 lines whose rhythm imitates that motion. Use a rhyme scheme (aabb or abab), at least one refrain, one example of alliteration and one onomatopoeia.",
   "Perform it for your family with a clap or tap on the beat."],
  "record": [
   {"t":"open","key":"motionpoem","q":"Write your final poem with a title, and mark its rhyme scheme with letters at the end of each line.","min":50,"rows":12,"rubric":["8 to 12 lines with a title","A rhythm that imitates the chosen motion","A rhyme scheme marked correctly","A refrain, alliteration and onomatopoeia"],"model":"Swing Song\nUp to the sky and back to the ground, (a)\nWhoosh goes the wind with a whistling sound, (a)\nToes touch the treetops, then down I fall, (b)\nPast the fence and the garden wall. (b)\nUp to the sky and back again, (c)\nSwinging and singing in sunshine or rain. (c)\nUp to the sky and back to the ground, (a)\nWhoosh goes the wind with a whistling sound. (a)"},
   {"t":"open","key":"motionnotes","q":"Explain how your rhythm imitates your motion, and label your refrain, alliteration and onomatopoeia. How did your family react to the performance?","min":30,"rows":4,"rubric":["Explains the link between rhythm and motion","Labels each required device","Reports audience reaction"],"model":"The beat goes up and back like a swing: UP to the SKY and BACK to the GROUND. Refrain: \"Up to the sky and back to the ground.\" Alliteration: \"swinging and singing in sunshine.\" Onomatopoeia: \"whoosh.\" My sister started swaying while I read it."}]},
 "think": {
  "intro": "Write in complete sentences. Your teacher scores these.",
  "items": [
   {"t":"open","key":"soundmeaning","q":"Choose \"From a Railway Carriage\" or \"Palanquin Bearers.\" Write a paragraph explaining how the poem's sound and structure support its meaning. Discuss at least two devices with quotations.","min":110,"rows":10,"rubric":["Clear claim about how sound supports meaning","At least two devices (rhythm, rhyme, repetition, refrain, alliteration, assonance) with quotations","Explains each effect","Organized paragraph"],"model":"In \"Palanquin Bearers,\" Sarojini Naidu uses sound to make readers feel the gentle, proud work of carrying a bride. The rocking rhythm of \"Lightly, O lightly we bear her along\" imitates the bearers walking in step while the palanquin sways on their shoulders. The repetition of \"Lightly, O lightly\" and \"Softly, O softly\" sounds like a work song the bearers sing together to keep their steps even. Alliteration such as \"gaily we glide\" adds a smooth, flowing sound. Finally, the refrain \"We bear her along like a pearl on a string\" closes each stanza with the same image, reminding us how precious she is. Through its sounds, the poem lets us feel the motion and the care the bearers give."},
   {"t":"open","key":"translate","q":"English translations of haiku usually cannot keep the 5-7-5 sound pattern. Is it more important for a translator to keep a poem's sound pattern or its meaning? Explain your view with an example from today.","min":60,"rows":5,"rubric":["A clear position","Reasoning about trade-offs between sound and meaning","An example from Bashō, Issa or another poem"],"model":"I think meaning matters more, because if a translation changes the image, readers lose the poem. In Bashō's haiku, the important part is the silence broken by the frog's splash. A translator could add extra words to make 5-7-5, but that might clutter the simple moment, so it is better to keep the meaning and the feeling."}]},
 "exit": [
  {"t":"text","q":"Mark the rhyme scheme: \"The cat sat down (a) / upon the mat, / she wore a crown / and a feathered hat.\" Type the letters for all four lines.","a":["abab"],"show":"abab","pts":2,"why":"down/crown (a), mat/hat (b)."},
  {"t":"text","q":"In Sonnet 18, the final couplet rhymes. Type the last word of line 13 and the last word of line 14.","a":[{"all":[["see"],["thee"]]}],"show":"see; thee","pts":2,"why":"see / thee: the gg couplet."},
  {"t":"text","q":"What is the term for a word that imitates a sound, such as buzz or splash?","a":["onomatopoeia","onomatopoeic"],"show":"onomatopoeia","pts":2,"why":"Onomatopoeia: Greek for \"name-making.\""},
  {"t":"open","key":"exit_rhythm","q":"How does rhythm help a poem's meaning? Give one example from today.","min":12,"rows":2,"rubric":["Rhythm can imitate motion or feeling","Example: train clatter (Stevenson) or swaying bearers (Naidu)"],"model":"Rhythm can imitate a motion. In Stevenson's poem, the quick beat sounds like train wheels on the track."}],
 "next": "Week 13: the poets of the Harlem Renaissance."
}

TEACHER = {
 "standards": [
  "ELA.6.R.3.1: Explain how figurative language contributes to tone and meaning in text(s).",
  "ELA.6.R.1.4: Describe the impact of various poetic forms on meaning and style.",
  "ELA.6.V.1.2: Apply knowledge of Greek and Latin roots and affixes to determine meanings of words and phrases in grade-level content.",
  "ELA.6.C.1.2: Write personal or fictional narratives using narrative techniques, precise words and phrases, and figurative language. (Applied to a short poem that tells a moment.)",
  "ELA.K12.EE.1.1: Cite evidence to explain and justify reasoning."],
 "materials": ["The interactive lesson", "A table, drum, or pot and wooden spoon", "Space to walk", "A phone to record (optional)", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 11 Reconnect questions."],
  [4, "Hook", "Tap the beat of the first line together."],
  [8, "Sound toolkit", "Sort examples of each device. Introduce the roots."],
  [10, "Stevenson", "Read aloud fast. Mark the rhyme scheme. Tap the rhythm."],
  [11, "Naidu", "Give background. Read aloud while walking in step. Find the refrain and similes."],
  [10, "Sonnet", "Read Sonnet 18 aloud. Mark abab cdcd efef gg. Find the turn at \"But.\""],
  [7, "Haiku and free verse", "Read the two haiku slowly. Discuss translation."],
  [4, "Assign", "Assign the motion poem, Think Deeper and the Exit Check."]],
 "key_questions": ["What do you hear?", "How does the sound match the meaning?", "What is repeated, and why?", "How is the poem built?"],
 "misconceptions": ["All poems must rhyme.", "Rhythm means rhyme.", "Haiku in English must always be 5-7-5.", "Repetition is lazy writing (it creates emphasis and music)."],
 "support": ["Read every poem aloud twice, once slowly and once at natural speed.", "Provide a rhyme scheme template.", "Clap syllables of a line before marking stresses."],
 "challenge": ["Read Edgar Allan Poe's \"The Bells\" and find four kinds of onomatopoeia.", "Translate a short poem from another language your family speaks and explain one choice you made between sound and meaning."],
 "background": "<p>Stevenson's \"From a Railway Carriage\" appeared in A Child's Garden of Verses (1885). Sarojini Naidu's \"Palanquin Bearers\" appeared in The Golden Threshold (1905); Naidu (1879 to 1949) was president of the Indian National Congress (1925) and became Governor of the United Provinces in 1947, the first woman governor in India. Bashō's frog haiku dates to 1686 and Issa's fly haiku to 1821; the translations here are KingCretot Experience's own. All originals are in the public domain. ELA.6.R.1.4 names the sonnet and the villanelle as its forms; the sonnet is taught here and the villanelle in Week 14. Shakespeare\u2019s Sonnet 18 was published in 1609.</p>",
 "sources": ["Poetry Foundation, Sarojini Naidu; Robert Louis Stevenson.", "Naidu, S. (1905), The Golden Threshold, Heinemann.", "Stevenson, R. L. (1885), A Child's Garden of Verses.", "Academy of American Poets, Haiku (poetic form)."]
}

PRINT = {
 "directions": "Write in complete sentences.",
 "items": [
  {"q":"Define rhyme scheme. Then write four lines of your own that rhyme aabb and label each line.","a":"The pattern of end rhymes, marked with letters; lines 1 and 2 rhyme (a), lines 3 and 4 rhyme (b).","lines":2},
  {"q":"Write one example each of alliteration and onomatopoeia.","a":"e.g. slippery slithering snakes; the faucet dripped, drip, drip.","lines":2},
  {"q":"How does the rhythm of \"From a Railway Carriage\" match its subject?","a":"A quick galloping beat imitates train wheels clattering on the rails.","lines":2},
  {"q":"What is the refrain in \"Palanquin Bearers,\" and what does it show?","a":"We bear her along like a pearl on a string; she is precious and carried with care.","lines":2},
  {"q":"Describe the sonnet form and where Sonnet 18 turns.","a":"14 lines; abab cdcd efef gg; iambic pentameter; turns at line 9 (\"But\").","lines":2},
  {"q":"Use the roots: what do symphony and sonic have in common?","a":"Both contain a root that means sound: phon and son.","lines":2}]
}
