FORMS = ('<svg viewBox="0 0 660 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Chart of the poetic forms studied in Unit 3">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Unit 3 form finder</text>'
  + ''.join(f'<rect x="{12+i*130}" y="36" width="122" height="176" rx="10" fill="{c}"/><text x="{73+i*130}" y="60" text-anchor="middle" fill="#fff" font-weight="bold" font-size="14">{f}</text>'
            + ''.join(f'<text x="{73+i*130}" y="{86+j*20}" text-anchor="middle" fill="#fff" font-size="11">{ln}</text>' for j, ln in enumerate(lines))
            for i, (f, c, lines) in enumerate([
              ("Haiku", "#3d9a2f", ["3 lines", "5-7-5 sound units", "(in Japanese)", "a moment in nature", "Bashō, Issa", "Week 12"]),
              ("Sonnet", "#0047BA", ["14 lines", "abab cdcd efef gg", "(Shakespearean)", "volta: the turn", "Shakespeare, McKay", "Weeks 12, 13"]),
              ("Free verse", "#C9A84C", ["no regular rhyme", "or meter", "held together by", "repetition", "Hughes, Sandburg", "Weeks 11, 13"]),
              ("Villanelle", "#DB2F30", ["19 lines", "5 tercets + quatrain", "2 rhymes", "2 refrains", "Robinson", "Week 14"]),
              ("Ballad-like", "#6b3fa0", ["stanzas with", "refrains and a", "steady beat", "song-like", "Naidu, Stevenson", "Week 12"])])) +
  '<text x="330" y="226" text-anchor="middle" font-size="11" fill="#5b6676">Ask of every poem: how does its form shape its meaning?</text></svg>')

MASK = ("<div class='card' style='border-left-color:#C9A84C'><h3 style='margin-top:0'>We Wear the Mask</h3><p class='muted' style='margin-top:-6px'>Paul Laurence Dunbar (1895; text from <i>The Complete Poems of Paul Laurence Dunbar</i>, 1913)</p>"
        "<p style='font-family:Georgia,serif;font-size:17px;line-height:1.7'>We wear the mask that grins and lies,<br>It hides our cheeks and shades our eyes,—<br>This debt we pay to human guile;<br>With torn and bleeding hearts we smile,<br>And mouth with myriad subtleties.<br>&nbsp;<br>"
        "Why should the world be over-wise,<br>In counting all our tears and sighs?<br>Nay, let them only see us, while<br>&nbsp;&nbsp;&nbsp;&nbsp;We wear the mask.<br>&nbsp;<br>"
        "We smile, but, O great Christ, our cries<br>To thee from tortured souls arise.<br>We sing, but oh the clay is vile<br>Beneath our feet, and long the mile;<br>But let the world dream otherwise,<br>&nbsp;&nbsp;&nbsp;&nbsp;We wear the mask!</p>"
        "<p class='muted' style='font-size:12px'>guile: trickery. myriad: countless. subtleties: small, clever details. over-wise: too knowing. nay: no. vile: disgusting, foul.</p></div>")

LESSON = {
 "unit": "Unit 3: The Power of Poetry",
 "title": "Mid-Year Review and Poetry Analysis Project",
 "subtitle": "Bring together figurative language, sound, form and conversation across time. Then write an analysis of one poem from Unit 3, recite it from memory, and show what you know on the Unit 3 checkpoint.",
 "objectives": [
  "Identify figurative language and sound devices and explain their effect.",
  "Identify the forms studied in Unit 3 and explain how form shapes meaning.",
  "Write a poetry analysis with a clear claim, quotations and explanation (T-E-E-C).",
  "Recite a poem from memory with clear voice, pacing and expression.",
  "Use the Greek and Latin roots from Unit 3."],
 "vocab": [
  ["thesis (claim)", "The main point an analysis argues, in one or two sentences."],
  ["evidence", "Words quoted from the poem that support the claim."],
  ["recitation", "Speaking a poem from memory for an audience."],
  ["tone", "The speaker's attitude, shown through word choice and sound."],
  ["rondeau", "A French form with two rhymes and a short refrain taken from the opening words."]],
 "reconnect": {
  "title": "Week 14: Poems in conversation",
  "intro": "Start with last week's poems and forms.",
  "items": [
   {"t":"num","q":"How many lines does a villanelle have?","a":19,"unit":"lines","pts":2,"why":"Five tercets and a quatrain."},
   {"t":"text","q":"What is the term for a brief reference to a well-known person, event or work?","a":[{"all":[["allusion"]],"none":["not","illusion"]}],"show":"allusion","pts":2,"why":"From lud, play."},
   {"t":"text","q":"Which American poet's \"I Hear America Singing\" does Hughes answer with \"I, too, sing America\"?","a":[{"all":[["whitman"]],"none":["not"]}],"show":"Walt Whitman","pts":2,"why":"Whitman's 1860 poem lists America's workers."},
   {"t":"open","key":"rc_shelter","q":"Why did Georgia Douglas Johnson call the cage's bars \"sheltering\"?","min":12,"rows":2,"rubric":["The limits on the woman's life also protect her, so she is safe but not free"],"model":"The things that limit her also keep her safe, so she is protected and trapped at the same time."}]},
 "hook": {
  "title": "Your Poem, Your Voice",
  "visual": FORMS,
  "html": "<p>Across five weeks you have read poems from England, Scotland, India, Japan, Jamaica and the United States, written over four hundred years. This week you choose one of them, or a pair, and become its expert. You will write an analysis that explains how the poet makes meaning, and you will recite the poem from memory, the way poems were shared long before they were printed.</p><p>Every year, high school students across the United States compete in Poetry Out Loud, a national recitation contest. They are judged on how clearly they speak, how they use their voice and how well they show they understand the poem. You will practice the same skills.</p><div class='callout'><b>Big idea:</b> To analyze a poem is to explain not just what it says, but how it says it.</div>"},
 "learn": [
  {"title": "Review: Figurative Language and Sound",
   "html": "<p>Figurative language says one thing in terms of another:</p><ul><li><b>Simile:</b> a comparison using like or as. <b>Metaphor:</b> a comparison without like or as (implied metaphors show it without saying it). <b>Personification:</b> giving human traits to something not human. <b>Symbol:</b> something concrete that stands for a bigger idea. <b>Extended metaphor:</b> a metaphor that runs through a poem.</li></ul><p>Sound devices make a poem musical:</p><ul><li><b>Rhyme</b> and <b>rhyme scheme</b>, <b>rhythm</b>, <b>repetition</b> and <b>refrain</b>, <b>alliteration</b> (repeated first consonant sounds), <b>assonance</b> (repeated vowel sounds) and <b>onomatopoeia</b> (words that imitate sounds).</li></ul>",
   "checks": [
    {"t":"text","q":"\"The old truck coughed and groaned up the hill.\" Which figurative device is this?","a":[{"all":[["personification","personify"]],"none":["not"]}],"show":"personification","pts":2,"why":"A truck cannot really cough or groan; it is given human actions."},
    {"t":"text","q":"\"Sizzle, crackle, pop went the bacon.\" Which sound device do sizzle, crackle and pop show?","a":[{"all":[["onomatopoeia"]],"none":["not"]}],"show":"onomatopoeia","pts":2,"why":"The words imitate the sounds."},
    {"t":"text","q":"\"The classroom was a beehive before the bell.\" Simile or metaphor?","a":[{"all":[["metaphor"]],"none":["not","simile"]}],"show":"metaphor","pts":2,"why":"It compares without like or as."},
    {"t":"open","key":"rv_effect","q":"Choose one device from the sentences above and explain its effect: what does it help a reader see, hear or feel?","min":20,"rows":2,"rubric":["Names a device correctly","Explains the effect, not just the name"],"model":"The beehive metaphor makes me picture a classroom full of buzzing, busy students moving everywhere, so I feel the noise and energy before the bell."}]},
  {"title": "Review: How Form Shapes Meaning",
   "html": "<p>Every form you studied in Unit 3 does something special:</p><ul><li>A <b>haiku</b> freezes one moment in nature in very few words.</li><li>A <b>sonnet</b> builds an argument or feeling over three quatrains, then turns (the <b>volta</b>) and closes with a couplet.</li><li><b>Free verse</b> drops regular rhyme and meter but holds together with repetition and parallel structure.</li><li>A <b>villanelle</b>'s two refrains circle back, like a thought that will not leave.</li><li>A poem with a <b>refrain</b> and a steady beat can feel like a song, a work chant or a march.</li></ul>",
   "checks": [
    {"t":"text","q":"A poem has 14 lines, three quatrains and a final rhyming couplet. What form is it?","a":[{"all":[["sonnet"]],"none":["not"]}],"show":"a sonnet","pts":2,"why":"abab cdcd efef gg."},
    {"t":"text","q":"Mark the rhyme scheme of these lines. Type the four letters with no spaces. \"The rain came down on the gravel road, / The wagon creaked beneath its load, / We hurried home before the night / Could swallow up the last of light.\"","a":["aabb"],"show":"aabb","pts":2,"why":"road/load (a), night/light (b)."},
    {"t":"open","key":"rv_form","q":"Choose one poem from Unit 3 and explain how its form fits its meaning.","min":30,"rows":3,"rubric":["Names a poem and its form correctly","Explains a clear link between form and meaning with a detail from the poem"],"model":"\"The Tired Worker\" is a sonnet. Its strict 14 lines feel like the worker's fixed daily routine, and the turn at line 11, \"But what steals out the gray clouds red like wine?\", is the moment dawn arrives and his short rest ends."}]},
  {"title": "Writing a Poetry Analysis",
   "html": "<p>A poetry analysis makes a <b>claim</b> about how a poem creates meaning, then proves it with <b>evidence</b>. Use the T-E-E-C paragraph you learned in Unit 2:</p><ul><li><b>T</b>opic sentence: one point that supports your thesis.</li><li><b>E</b>vidence: a short quotation from the poem, in quotation marks, with line breaks shown by a slash ( / ).</li><li><b>E</b>xplanation: how the words create meaning; name the device and its effect.</li><li><b>C</b>oncluding sentence: tie the point back to the thesis.</li></ul><div class='card' style='font-family:Georgia,serif'><b>Model paragraph (on \"Palanquin Bearers,\" Week 12)</b><br>Sarojini Naidu makes readers feel the bride's lightness and value through simile and rhythm. The bearers say, \"She sways like a flower in the wind of our song.\" The simile compares the bride to a flower that moves gently, so she seems delicate and almost weightless, while \"our song\" reminds us that the bearers' singing sets the pace. The swaying beat of the line, LIGHT-ly, O LIGHT-ly, rocks back and forth like the palanquin itself. Through simile and rhythm, Naidu turns a hard job into a graceful dance.</div><p>Notice that the model never just retells the poem. Every sentence explains <i>how</i>.</p>",
   "checks": [
    {"t":"open","key":"thesis","q":"Write a thesis (one or two sentences) for an analysis of a poem you might choose for your project. Name the poem, the poet and two techniques.","min":25,"rows":2,"rubric":["Names a Unit 3 poem and poet","Makes a claim about meaning","Names two techniques (devices or form)"],"model":"In \"The Negro Speaks of Rivers,\" Langston Hughes uses a collective speaker and a repeated refrain to show that Black history is ancient, deep and unbroken."},
    {"t":"text","q":"When you quote two lines of a poem inside a sentence, what mark shows where one line ends and the next begins? (Type the name of the mark.)","a":[{"all":[["slash","/"]],"none":["not"]}],"show":"a slash ( / )","pts":2,"why":"Example: \"I've known rivers: / Ancient, dusky rivers.\""},
    {"t":"open","key":"retell","q":"A student writes: \"In the poem, the worker is tired, and then the sun comes up, and he has to go back to the city.\" Why is this a retelling instead of analysis? Rewrite it as analysis.","min":30,"rows":3,"rubric":["Explains it only summarizes what happens, without explaining how or why","A rewrite that names a technique and its effect, with a quotation"],"model":"It only tells what happens. Analysis explains how the poet creates meaning. Rewrite: McKay uses the volta at line 11, \"But what steals out the gray clouds red like wine?\", to show the worker's hope for rest being crushed as dawn arrives too soon."}]},
  {"title": "Reciting a Poem",
   "html": "<p>To recite a poem well:</p><ol><li><b>Understand it first.</b> You cannot express what you do not understand.</li><li><b>Memorize in chunks:</b> learn one stanza at a time; say it aloud while walking; write it from memory; use the first word of each line as a cue.</li><li><b>Voice:</b> speak loudly and clearly enough for the back of a room. Vary your volume and speed to match the meaning.</li><li><b>Pauses:</b> pause at punctuation, not just at the end of every line.</li><li><b>Presence:</b> stand still and tall, look at your audience and let your face match the tone. Avoid acting out every word; let the poem's language do the work.</li></ol>",
   "checks": [
    {"t":"open","key":"recitepause","q":"In \"Epilogue,\" where would you pause and slow down when reciting \"Tomorrow, / I'll sit at the table / When company comes\"? Explain why.","min":20,"rows":2,"rubric":["A sensible pause (after \"Tomorrow,\" at the comma)","Connects the pause to meaning (it marks the turn to hope or confidence about the future)"],"model":"I would pause after \"Tomorrow,\" because the comma and the word itself mark the turn from how things are now to the future Hughes is sure will come. The pause makes that hope stand out."},
    {"t":"text","q":"When reciting, should you pause at the end of every line, or where the punctuation and meaning tell you to? Type line or punctuation.","a":[{"all":[["punctuation","meaning"]],"none":["not","every line"]}],"show":"where the punctuation and meaning tell you to","pts":2,"why":"Many lines run on into the next without a pause."}]}],
 "handson": {
  "title": "Poetry Analysis Project Workshop",
  "intro": "Work on both parts of your Unit 3 project: the written analysis and the recitation. See the Unit 3 project rubric.",
  "materials": ["The Unit 3 poems (in the Week 11 to 14 lessons)", "Paper and pencil or a computer", "Index cards for memorizing", "A phone or tablet to record your recitation (with a parent)", "A family audience"],
  "steps": [
   "Choose one poem from Unit 3 (or two poems in conversation). Read it aloud three times.",
   "Annotate: mark the form, rhyme scheme, devices and the line you think matters most.",
   "Write your thesis, then draft three T-E-E-C body paragraphs, each with a quotation, plus an introduction and a conclusion (400 to 600 words in all). Cite the poem at the end in MLA style.",
   "Memorize your poem in chunks, writing each stanza's first words on an index card.",
   "Record your recitation. Watch it once, choose one thing to improve, and record a final version for a family audience."],
  "record": [
   {"t":"open","key":"analysisdraft","q":"Paste or type your full analysis (400 to 600 words) with your MLA citation.","min":300,"rows":18,"rubric":["Clear thesis about how the poem creates meaning","Three body paragraphs with accurate quotations","Explains effects (not retelling)","Form and at least two devices analyzed","Conclusion and correct MLA citation"],"model":"(Model opening) Langston Hughes was barely an adult when he wrote \"The Negro Speaks of Rivers,\" yet the poem's speaker sounds thousands of years old. In this free-verse poem, Hughes uses a collective speaker, parallel structure and a repeated refrain to show that Black history is ancient, deep and unbroken. ... Works Cited: Hughes, Langston. \"The Negro Speaks of Rivers.\" The Weary Blues, Alfred A. Knopf, 1926, p. 51."},
   {"t":"open","key":"recitereflect","q":"After recording, describe one thing you improved between your first and final recitation, and one thing you would still work on.","min":30,"rows":3,"rubric":["A specific improvement (volume, pacing, pauses, eye contact, accuracy)","A specific next goal"],"model":"In my first recording I rushed and paused at the end of every line. In the final one I paused only at punctuation, which made the refrain sound stronger. I would still work on looking up at my audience instead of at the floor."}]},
 "think": {
  "intro": "Reflect on the whole unit. Your teacher scores these.",
  "items": [
   {"t":"open","key":"unitpoem","q":"Which poem from Unit 3 affected you most, and why? Use one quotation and name one technique the poet used to create that effect.","min":70,"rows":5,"rubric":["Names a poem and poet","Explains a personal response","An accurate quotation","Names a technique and connects it to the effect"],"model":"\"The House on the Hill\" affected me most. The refrain \"They are all gone away\" kept coming back, and by the end it felt heavy, the way missing someone keeps returning to your mind. Robinson used the villanelle's repeating refrains to make me feel that loss instead of just reading about it."}]},
 "checkpoint": {
  "title": "Unit 3 Checkpoint: The Power of Poetry",
  "intro": "This checkpoint covers Weeks 11 to 15. Read the poem in Part A carefully; you may reread it as often as you like. Mastery is 85 or higher. If you score below 85, your teacher will review with you, then you will retake it.",
  "parts": [
   {"title": "Part A: Read a new poem", "items": [
    {"t":"open","key":"cp_maskmeaning","q":"<div class='cp-text'>" + MASK + "</div>What does the mask stand for in this poem? Explain the metaphor.","pts":4,"min":25,"rows":3,"rubric":["The mask is a metaphor for hiding true pain behind a smiling or calm face","Connects to the people speaking (\"we\"): suffering they keep from the world"],"model":"The mask is a metaphor for the smiling face people show the world to hide their real pain. The speakers, a \"we\" who suffer, grin and smile while their hearts are \"torn and bleeding,\" so no one sees how they really feel."},
    {"t":"text","q":"Type the refrain of the poem, the short line that repeats.","a":[{"all":[["wear"],["mask"]],"none":["not"]}],"show":"We wear the mask","pts":3,"why":"It closes stanzas 2 and 3."},
    {"t":"text","q":"The poem uses only two rhyme sounds. One is the sound in lies, eyes and wise. Type a word from the poem that rhymes with smile.","a":[{"all":[["guile","while","vile","mile"]],"none":["not","smile"]}],"show":"guile, while, vile or mile","pts":3,"why":"guile, smile, while, vile, mile."},
    {"t":"open","key":"cp_maskpunct","q":"The refrain ends with a period in stanza 2 and an exclamation point in stanza 3. How does that change the tone at the end of the poem?","pts":4,"min":20,"rows":2,"rubric":["Notices the shift from period to exclamation point","Explains a tone change (from quiet acceptance to stronger emotion: defiance, anguish or insistence)"],"model":"With a period, the refrain sounds quiet and resigned. With an exclamation point at the end, it sounds forceful, almost a cry, as if the speakers are insisting, with pain and pride, that they will keep hiding their suffering."},
    {"t":"open","key":"cp_maskconnect","q":"Dunbar also wrote \"Sympathy,\" with its caged bird (Week 11). Name one way \"We Wear the Mask\" and \"Sympathy\" are in conversation.","pts":4,"min":20,"rows":2,"rubric":["A connection: both show hidden suffering; the bird's song and the mask's smile both hide pain; both speak for people whose freedom is limited"],"model":"Both poems show suffering hidden behind something that looks pleasant: the caged bird's song is really a prayer, and the mask's grin hides torn and bleeding hearts."}]},
   {"title": "Part B: Devices and forms", "items": [
    {"t":"text","q":"\"The lighthouse winked at the passing ships.\" Name the device.","a":[{"all":[["personification"]],"none":["not"]}],"show":"personification","pts":3,"why":"A lighthouse cannot wink."},
    {"t":"text","q":"\"Her laugh was as bright as a brass bell.\" Simile or metaphor?","a":[{"all":[["simile"]],"none":["not","metaphor"]}],"show":"simile","pts":3,"why":"It uses as."},
    {"t":"text","q":"\"Silver stars slid slowly south.\" Which sound device repeats the s sound at the start of words?","a":[{"all":[["alliteration"]],"none":["not"]}],"show":"alliteration","pts":3,"why":"Repeated beginning consonant sounds."},
    {"t":"text","q":"What is the name of a three-line Japanese poem with 17 sound units?","a":[{"all":[["haiku"]],"none":["not"]}],"show":"haiku","pts":3,"why":"5-7-5 in Japanese."},
    {"t":"text","q":"What is the name for the turn in a sonnet?","a":[{"all":[["volta"]],"none":["not"]}],"show":"volta","pts":3,"why":"Italian for turn."}]},
   {"title": "Part C: Poems and their times", "items": [
    {"t":"text","q":"What was the name of the movement of about 6 million Black Southerners to cities in the North and West between about 1910 and 1970?","a":[{"all":[["great migration","migration"]],"none":["not"]}],"show":"the Great Migration","pts":3,"why":"It helped make the Harlem Renaissance possible."},
    {"t":"text","q":"\"The Negro Speaks of Rivers\" has no regular rhyme scheme or meter. What kind of poetry is it?","a":[{"all":[["free verse","freeverse","free-verse"]],"none":["not"]}],"show":"free verse","pts":3,"why":"It is held together by repetition and parallel structure."},
    {"t":"open","key":"cp_answer","q":"Explain how one poem from Unit 3 answers or echoes an earlier poem or text. Name both and give one specific detail.","pts":4,"min":25,"rows":3,"rubric":["Names a correct pair (Hughes/Whitman; Johnson/Dunbar; Fauset/Truth; any well-supported pair)","A specific, accurate detail showing the connection"],"model":"Hughes's \"Epilogue\" answers Whitman's \"I Hear America Singing.\" Whitman lists many singing Americans but leaves out Black Americans, so Hughes begins \"I, too, sing America\" and ends \"I, too, am America.\""}]},
   {"title": "Part D: Roots from Unit 3", "items": [
    {"t":"blanks","q":"Write the meaning of each root.","sent":"phon: ___ &nbsp; liber: ___ &nbsp; vers: ___ &nbsp; migr: ___","blanks":[[{"all":[["sound"]],"none":["not"]}],[{"all":[["free"]],"none":["not"]}],[{"all":[["turn"]],"none":["not"]}],[{"all":[["move"]],"none":["not"]}]],"show":"sound; free; turn; move","pts":4,"why":"phon = sound; liber = free; vers = turn; migr = move."},
    {"t":"text","q":"Sym means together and path means feeling. What word means feeling together with someone in their sorrow?","a":[{"all":[["sympathy","sympathize"]],"none":["not"]}],"show":"sympathy","pts":3,"why":"sym + path: Dunbar's poem title."}]}]},
 "next": "Unit 4: making the case (argument), starting with claims, reasons and evidence."
}

TEACHER = {
 "standards": [
  "ELA.6.R.1.4: Describe the impact of various poetic forms on meaning and style.",
  "ELA.6.R.3.1: Explain how figurative language contributes to tone and meaning in text(s).",
  "ELA.6.R.3.3: Compare and contrast how authors from different time periods address the same or related topics.",
  "ELA.6.C.2.1: Present information orally, in a logical sequence, using nonverbal cues, appropriate volume, clear pronunciation, and appropriate pacing.",
  "ELA.6.V.1.2: Apply knowledge of Greek and Latin roots and affixes to determine meanings of words and phrases in grade-level content.",
  "ELA.K12.EE.1.1: Cite evidence to explain and justify reasoning."],
 "materials": ["The interactive lesson", "The Unit 3 poems", "Index cards, paper and pencil or a computer", "A phone or tablet to record the recitation", "The Unit 3 project rubric", "The Unit 3 checkpoint (in the lesson)"],
 "flow": [
  [6, "Reconnect", "Run the Week 14 Reconnect questions."],
  [4, "Hook", "Introduce the project and the form finder."],
  [9, "Devices review", "Identify devices in new sentences and explain effects."],
  [8, "Forms review", "Match forms to poems; mark a rhyme scheme."],
  [12, "Writing an analysis", "Study the model paragraph; draft a thesis; fix the retelling."],
  [7, "Reciting", "Model a stanza with pauses at punctuation; the student tries one."],
  [4, "Assign", "Assign the analysis, the recitation recording and Think Deeper."],
  [10, "Checkpoint preview", "Explain that the checkpoint is completed after class, independently, one try per item, with no answers shown until you review it. Mastery is 85; below 85 means a review lesson and a retake."]],
 "key_questions": ["How does the poet create meaning, not just what does the poem say?", "Which quotation best proves your point?", "How does the form fit the feeling?", "Where do the punctuation and meaning tell you to pause?"],
 "misconceptions": ["Analysis means retelling the poem.", "Every line ending needs a pause when reciting.", "Long quotations are better evidence than short, precise ones.", "Only one interpretation of a poem is correct (strong interpretations are supported by evidence)."],
 "support": ["Offer a thesis frame: \"In ___, ___ uses ___ and ___ to show ___.\"", "Allow 10 to 14 memorized lines if the chosen poem is longer.", "Pre-highlight three possible quotations."],
 "challenge": ["Write the analysis on two poems in conversation.", "Recite \"We Wear the Mask\" in addition to your chosen poem."],
 "background": "<p>\"We Wear the Mask\" first appeared in Majors and Minors (1895) and is reprinted in Lyrics of Lowly Life (1896); the text here is from The Complete Poems of Paul Laurence Dunbar (1913; Project Gutenberg 18338). It is often described as a variation on the French rondeau: 15 lines, two rhymes, and a short refrain taken from the opening words. Poetry Out Loud is a national recitation contest for high school students run by the National Endowment for the Arts and the Poetry Foundation with state arts agencies. Checkpoint total: 57 points (Part A 18, Part B 15, Part C 10, Part D 7); score written items with their rubrics.</p>",
 "sources": ["Dunbar, P. L. (1913), The Complete Poems of Paul Laurence Dunbar (Project Gutenberg 18338).", "Poetry Out Loud, Recitation evaluation criteria.", "Academy of American Poets, Rondeau (poetic form)."]
}

PRINT = {
 "directions": "Mid-year review. Write in complete sentences.",
 "items": [
  {"q":"Define simile, metaphor, personification and symbol, with one example of each.","a":"Model: simile, a comparison using like or as (\"like a flower\"); metaphor, a comparison without like or as (\"the classroom was a beehive\"); personification, human traits for non-human things (\"the truck coughed\"); symbol, a concrete thing standing for an idea (stars for hope).","lines":4},
  {"q":"Describe the sonnet and the villanelle. Name a Unit 3 poem in each form.","a":"Sonnet: 14 lines, abab cdcd efef gg, volta (Sonnet 18 or \"The Tired Worker\"). Villanelle: 19 lines, two refrains, two rhymes (\"The House on the Hill\").","lines":3},
  {"q":"Write a thesis for an analysis of any Unit 3 poem.","a":"Model: In \"Oriflamme,\" Jessie Fauset uses an epigraph and parallel stanzas to show that hope passes from one generation to the next.","lines":2},
  {"q":"Explain the difference between retelling and analysis.","a":"Retelling says what happens; analysis explains how the poet creates meaning and why it matters.","lines":2},
  {"q":"Give the meaning of each root and one word using it: metr, voc, dia, nat.","a":"metr = measure (meter); voc = voice, call (vocal); dia = across, through (dialogue); nat = born (native).","lines":2},
  {"q":"Name two ways to memorize a poem.","a":"Learn one stanza at a time; say it aloud while walking; write it from memory; use first-word cue cards.","lines":2}]
}
