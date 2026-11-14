SYMBOLS = ('<svg viewBox="0 0 660 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Three symbols in The Call of the Wild: the club, the fire and the trail">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Symbols: objects that stand for bigger ideas</text>'
  + ''.join(f'<g transform="translate({20+i*214},36)"><rect width="196" height="180" rx="12" fill="{c}"/><text x="98" y="24" text-anchor="middle" fill="#fff" font-weight="bold" font-size="14">{a}</text>{pic}'
            + ''.join(f'<text x="98" y="{124+j*15}" text-anchor="middle" fill="#fff" font-size="11">{t}</text>' for j, t in enumerate(lines)) + '</g>'
            for i, (a, c, pic, lines) in enumerate([
              ("The club", "#8a6d1f", '<path d="M70 92 L130 40" stroke="#fff" stroke-width="10" stroke-linecap="round"/><circle cx="132" cy="38" r="12" fill="#fff"/>', ["force, power,", "\"the law of club\"", "and fang; human control"]),
              ("The fire", "#DB2F30", '<path d="M98 96 C70 80 80 56 92 44 C92 62 104 60 100 40 C122 56 126 82 98 96Z" fill="#C9A84C"/><path d="M98 96 C86 88 90 74 98 66 C106 76 110 88 98 96Z" fill="#fff"/>', ["Buck\'s visions of the", "\"hairy man\": memory,", "ancestry, the ancient past"]),
              ("The trail", "#0047BA", '<path d="M30 96 Q80 60 120 76 T170 50" stroke="#fff" stroke-width="4" fill="none" stroke-dasharray="8 6"/>', ["work, purpose,", "pride in the traces;", "the journey of change"])])) +
  '</svg>')

VISION = ("<div class='card' style='border-left-color:#C9A84C'><h3 style='margin-top:0'>From Chapter IV: \"Who Has Won to Mastership\"</h3><p class='muted' style='margin-top:-6px'>Jack London, The Call of the Wild (1903). Buck lies by the campfire at night. ... marks words left out.</p>"
          "<p style='font-family:Georgia,serif'>... the instincts (which were but the memories of his ancestors become habits) which had lapsed in later days, and still later, in him, quickened and become alive again.</p>"
          "<p style='font-family:Georgia,serif'>Sometimes as he crouched there, blinking dreamily at the flames, it seemed that the flames were of another fire ... This other man was shorter of leg and longer of arm ... And beyond that fire, in the circling darkness, Buck could see many gleaming coals, two by two, always two by two, which he knew to be the eyes of great beasts of prey.</p>"
          "<p class='muted' style='font-size:12px'>instincts: behaviors an animal is born knowing. lapsed: faded away, stopped. quickened: came to life. crouched: bent low. beasts of prey: animals that hunt others.</p></div>")

HAL = ("<div class='card' style='border-left-color:#0047BA'><h3 style='margin-top:0'>From Chapter V: \"The Toil of Trace and Trail\"</h3><p class='muted' style='margin-top:-6px'>Buck's team is sold to Hal, Charles and Mercedes, newcomers from the States.</p>"
       "<p style='font-family:Georgia,serif'>Buck felt vaguely that there was no depending upon these two men and the woman. They did not know how to do anything, and as the days went by it became apparent that they could not learn. They were slack in all things, without order or discipline. ... Not only did they not know how to work dogs, but they did not know how to work themselves.</p>"
       "<p class='muted' style='font-size:12px'>vaguely: in an unclear way. slack: careless, loose. discipline: self-control and order.</p></div>")

LESSON = {
 "unit": "Unit 5: Novel Study",
 "title": "Symbols and Theme",
 "subtitle": "In Chapters IV and V, Buck becomes lead dog, then suffers under owners who don't know the North. Behind the action, London is saying something about survival, knowledge and the pull of the wild. This week you learn to read symbols and state a theme, the big idea of a story.",
 "objectives": [
  "Explain what a symbol is and analyze how the club, the fire and the trail work as symbols.",
  "Distinguish a topic from a theme and write a theme statement as a complete sentence.",
  "Trace how a theme develops across chapters using text evidence.",
  "Compare characters (François and Perrault versus Hal, Charles and Mercedes) to reveal theme.",
  "Use the roots anim, pathos (review) and the suffix -ity, and context clues."],
 "vocab": [
  ["symbol", "An object, person or event that stands for a bigger idea."],
  ["theme", "The central message or insight about life that a story reveals."],
  ["topic", "The subject of a story in a word or two, such as survival or loyalty."],
  ["motif", "An image, idea or object that repeats through a story."],
  ["ancestor", "A relative from long ago from whom a person or animal is descended."],
  ["instinct", "Behavior an animal is born knowing, without being taught."],
  ["foil", "A character whose differences highlight another character's qualities."]],
 "reconnect": {
  "title": "Week 22: Conflict and character change",
  "intro": "Themes grow out of conflicts and changes, so last week's work is the foundation.",
  "items": [
   {"t":"text","q":"Who was Buck's antagonist in Chapter III?","a":[{"all":[["spitz"]],"none":["not"]}],"show":"Spitz","pts":2,"why":"In Chapter IV, Buck takes his place as leader."},
   {"t":"text","q":"Buck against hunger and snow is character versus ___.","a":[{"all":[["nature"]],"none":["not"]}],"show":"nature","pts":2,"why":"Week 22."},
   {"t":"text","q":"London describes Buck's change with two words: \"development (or ___).\"","a":[{"all":[["retrogress"]],"none":["not"]}],"show":"retrogression","pts":2,"why":"Moving backward."},
   {"t":"open","key":"rc_change","q":"In one sentence, describe how Buck has changed from Chapter I to the end of Chapter III.","min":12,"rows":2,"rubric":["From a comfortable, proud house dog to a tough, cunning survivor who has fought for leadership"],"model":"Buck has gone from a proud, comfortable estate dog to a tough, cunning survivor who fought Spitz for leadership."}]},
 "hook": {
  "title": "What Is the Story Really About?",
  "visual": SYMBOLS,
  "html": "<p>If someone asks what <i>The Call of the Wild</i> is about, you could say \"a dog in the Klondike.\" That's the plot. But stories also say something about life. A dog who must forget his comfortable past and learn to survive might be saying something about all of us: about how environments shape us, about the difference between strength and cruelty, about who we are underneath.</p><p>That bigger message is the story's <b>theme</b>. Writers often deliver it through <b>symbols</b>, objects that stand for ideas.</p><div class='callout'><b>Big question:</b> How do symbols and characters reveal a story's deeper message?</div>"},
 "learn": [
  {"title": "Reading Symbols",
   "html": "<p>A <b>symbol</b> is an object that means more than itself. A <b>motif</b> is something that repeats. In this novel:</p><ul><li><b>The club</b> appears again and again. It stands for force and human power, the \"law of club and fang.\" In Chapter IV, when François comes at him with a club, Buck circles just out of reach: \"he was become wise in the way of clubs.\" He no longer fears the club; he has learned how to live with it.</li><li><b>The fire</b> is where Buck has visions of an ancient \"hairy man\" and the eyes of beasts in the dark. It stands for memory and ancestry, the deep past waking up inside Buck.</li><li><b>The trail</b> and the traces (the straps of the harness) stand for work and purpose. Dave and Sol-leks, the veteran dogs, take pride in pulling; for them the trail is meaning.</li></ul>",
   "checks": [
    {"t":"text","q":"An object, person or event that stands for a bigger idea is called a ___.","a":[{"all":[["symbol"]],"none":["not"]}],"show":"symbol","pts":2,"why":"A repeating symbol or image is a motif."},
    {"t":"open","key":"clubchange","q":"In Chapter I the club made Buck obey. In Chapter IV he \"was become wise in the way of clubs.\" How has the club's meaning changed for Buck, and what does that show about him?","min":30,"rows":3,"rubric":["Chapter I: the club was a terrifying new law that forced obedience","Chapter IV: Buck understands it and works around it to get what he wants (leadership)","Shows growth in cunning and confidence"],"model":"In Chapter I the club was terrifying and forced Buck to obey. By Chapter IV he understands it so well that he circles just out of reach and refuses to give in until he gets leadership. It shows he has grown cunning and confident; force no longer controls him."}]},
  {"title": "The Fire and the Hairy Man",
   "html": VISION + "<p>London suggests that Buck's wild instincts are not new. They are \"the memories of his ancestors become habits\" that are \"alive again.\" At the fire, Buck seems to remember a time long ago when dogs' ancestors lived beside early humans who feared the dark. The fire becomes a door to the past.</p><p>London's ideas reflect his era's fascination with Charles Darwin's theory of evolution (published in 1859) and with heredity. Scientists today understand that animals inherit instincts through their genes, though not literal \"memories\" of their ancestors' lives.</p>",
   "checks": [
    {"t":"open","key":"firesymbol","q":"What does the fire symbolize in this passage? Quote a phrase that supports your answer.","min":30,"rows":3,"rubric":["Ancestry, memory, the ancient wild past waking up in Buck","An accurate quotation (\"memories of his ancestors,\" \"the flames were of another fire,\" \"become alive again\")"],"model":"The fire symbolizes Buck's connection to his ancestors and the ancient wild past. London says Buck's instincts are \"the memories of his ancestors become habits\" that have \"become alive again,\" and the flames seem to be \"of another fire\" from long ago."},
    {"t":"text","q":"Behaviors an animal is born knowing, without being taught, are called ___.","a":[{"all":[["instinct"]],"none":["not"]}],"show":"instincts","pts":2,"why":"London calls them memories of ancestors."}]},
  {"title": "Topic Versus Theme",
   "html": "<p>A <b>topic</b> is a word or two: <i>survival</i>, <i>loyalty</i>, <i>power</i>. A <b>theme</b> is a complete sentence about life, a message the story shows rather than tells:</p><ul><li>Topic: survival. Theme: <i>To survive in a harsh world, you must adapt, even if it means leaving behind parts of who you were.</i></li><li>Topic: knowledge. Theme: <i>Ignorance and arrogance can be more dangerous than any wilderness.</i></li></ul><p>A theme statement should not name specific characters, should not be a cliché like \"never give up,\" and should be supported by evidence from many parts of the book. Stories usually have more than one theme.</p><p><b>Roots and suffixes:</b> <i>anim</i> means life or spirit (animal, animate, animosity). The suffix <i>-ity</i> turns an adjective into a noun meaning \"the state of\": able → ability, adaptable → adaptability, cruel → cruelty.</p>",
   "checks": [
    {"t":"text","q":"Is \"survival\" a topic or a theme?","a":[{"all":[["topic"]],"none":["not topic","theme"]}],"show":"a topic","pts":2,"why":"A theme is a full sentence about life."},
    {"t":"open","key":"fixtheme","q":"Rewrite this weak theme statement so it is a strong one: \"Buck learns to be tough.\"","min":11,"rows":2,"rubric":["A complete sentence about life in general, not naming Buck","Insightful, not a cliché"],"model":"Hard environments can force us to discover strengths we never knew we had."},
    {"t":"blanks","q":"Use the suffix -ity.","sent":"The state of being able to adapt is ___. The quality of being cruel is ___.","blanks":[[{"all":[["adaptability"]],"none":["not"]}],[{"all":[["cruelty"]],"none":["not"]}]],"show":"adaptability; cruelty","pts":2,"why":"-ity means the state or quality of."}]},
  {"title": "Characters as Foils: Chapter V",
   "html": HAL + "<p>In Chapter V, Buck's team is sold to <b>Hal</b>, <b>Charles</b> and <b>Mercedes</b>, newcomers who know nothing about the North. They overload the sled, overfeed and then starve the dogs, beat them when they are exhausted and ignore advice. Many dogs die. (Parents: this chapter describes the dogs' suffering and ends with the three newcomers dying when the sled breaks through the ice; preview it.)</p><p>They are <b>foils</b> to François and Perrault, the experienced drivers of Chapters II to IV, who were tough but knew the trail and cared for the dogs' food and feet (François even made moccasins for Buck's sore feet). Placing the two groups side by side reveals a theme: in the North, knowledge and respect for nature mean survival, and ignorance means disaster.</p><p>At the end of the chapter, a man named <b>John Thornton</b> warns the newcomers that the river ice is rotten and refuses to let Buck be beaten to death, cutting him free. The three go on without Buck, and the ice gives way.</p>",
   "checks": [
    {"t":"open","key":"foils","q":"Compare François and Perrault with Hal, Charles and Mercedes. What theme does the contrast reveal? State it as a complete sentence.","min":40,"rows":4,"rubric":["François and Perrault: experienced, disciplined, cared for the dogs; Hal, Charles, Mercedes: ignorant, disorganized, cruel","A theme statement about knowledge, respect for nature or arrogance, written as a full sentence"],"model":"François and Perrault knew the trail, kept order and took care of the dogs' food and feet, while Hal, Charles and Mercedes \"did not know how to do anything\" and refused to learn. The contrast reveals a theme: knowledge and respect for nature are what keep people alive in a harsh environment, and arrogance can be deadly."},
    {"t":"text","q":"Which man warns about the rotten ice and cuts Buck free?","a":[{"all":[["thornton"]],"none":["not"]}],"show":"John Thornton","pts":2,"why":"He becomes the center of Chapter VI."}]}],
 "handson": {
  "title": "Symbol Museum and Theme Tree",
  "intro": "Create objects that stand for the novel's symbols, then grow a theme tree with evidence on every branch.",
  "materials": ["Household objects or craft materials to represent symbols (a stick, a red cloth, a toy flame or candle picture, a string or rope)", "A large sheet of paper or poster board", "Markers or colored pencils", "Sticky notes or paper leaves", "The Call of the Wild, Chapters IV and V", "Paper and pencil"],
  "steps": [
   "Symbol museum: choose or make an object for three symbols (for example, a stick for the club, a red cloth for the man in the red sweater, a picture of a fire, a rope for the traces). Arrange them on a table with a museum label for each: what it is, where it appears and what it stands for.",
   "Give a family member a museum tour, explaining each symbol with a quotation.",
   "Theme tree: draw a tree trunk labeled with one topic (survival, knowledge, the wild, loyalty). Write a full theme statement on the trunk.",
   "On leaves, write evidence from at least four different chapters that supports the theme. Attach the leaves to branches.",
   "Don't use real candles or flames; draw or print a picture of a fire instead."],
  "record": [
   {"t":"open","key":"museumrec","q":"Describe your three museum objects, what each symbolizes and the quotation you used. Then write your theme statement and list your four pieces of evidence (one from each of four chapters).","min":80,"rows":7,"rubric":["Three symbols with accurate meanings and quotations","A strong theme statement (full sentence, not naming characters)","Four pieces of evidence from four chapters"],"model":"A stick for the club (force; \"a man with a club was a lawgiver\"), a red scarf for the man in the red sweater (cruelty and power), and a fire picture for Buck's visions (ancestry; \"the memories of his ancestors become habits\"). Theme: \"To survive in a harsh world, you must adapt, even if it means leaving parts of your old self behind.\" Evidence: Chapter I, Buck learns to obey the club; Chapter II, he steals food to survive; Chapter III, his \"primordial beast\" grows; Chapter V, Hal and Charles die because they never adapt."}]},
 "think": {
  "intro": "Use evidence from the novel. Your teacher scores these.",
  "items": [
   {"t":"open","key":"themeessay","q":"Write a paragraph explaining one theme of The Call of the Wild so far. State the theme as a complete sentence, support it with at least two quotations from two different chapters, and explain how each quotation develops the theme.","min":118,"rows":9,"rubric":["A clear theme statement (full sentence, not naming characters, not a cliché)","Two accurate quotations from two chapters","Explanation of how each develops the theme","Organized like a T-E-E-C paragraph"],"model":"One theme of The Call of the Wild is that ignorance and arrogance can be more dangerous than any wilderness. In Chapter II, Buck survives because he learns quickly: his theft of food shows \"his adaptability, his capacity to adjust himself to changing conditions, the lack of which would have meant swift and terrible death.\" Buck respects the harsh rules of the North and learns from them. In Chapter V, Hal, Charles and Mercedes do the opposite: London writes that \"they did not know how to do anything, and as the days went by it became apparent that they could not learn.\" They overload the sled, mistreat the dogs and ignore John Thornton's warning about the ice, and it costs them their lives. Together, these chapters show that in a harsh environment, the willingness to learn decides who survives."},
   {"t":"open","key":"symbolinvent","q":"If you were writing a story about your own life this year, what object could be a symbol, and what would it stand for? Explain why it fits.","min":47,"rows":5,"rubric":["A specific object","A clear bigger idea it stands for","An explanation connecting the object to experiences"],"model":"My library card could be a symbol of independence. This year I started going to the library by myself and choosing my own books for my homeschool reading. Every time I use the card, it reminds me that I'm becoming someone who can plan my own learning, so it would stand for growing up and freedom."}]},
 "exit": [
  {"t":"text","q":"Is \"In a harsh world, the willingness to learn decides who survives\" a topic or a theme?","a":[{"all":[["theme"]],"none":["not theme","topic"]}],"show":"a theme","pts":2,"why":"It's a complete sentence about life."},
  {"t":"text","q":"What does the fire in Buck's visions symbolize: ancestry and the ancient past, or the future?","a":[{"all":[["ancest","past","memory","ancient"]],"none":["not","future"]}],"show":"ancestry and the ancient past","pts":2,"why":"\"the memories of his ancestors become habits.\""},
  {"t":"text","q":"A character whose differences highlight another character's qualities is a ___.","a":[{"all":[["foil"]],"none":["not"]}],"show":"foil","pts":2,"why":"Hal and Charles are foils to François and Perrault."},
  {"t":"open","key":"exit_symbol","q":"Choose one symbol from the novel and explain what it stands for.","min":11,"rows":2,"rubric":["A symbol from the novel","An accurate bigger meaning"],"model":"The club stands for force and power, the law that rules the North."}],
 "next": "Week 24: author's craft, including how London portrays people."
}

TEACHER = {
 "standards": [
  "ELA.6.R.1.2: Analyze the development of stated or implied theme(s) throughout a literary text.",
  "ELA.6.R.1.1: Analyze how the interaction between characters contributes to the development of a plot in a literary text.",
  "ELA.6.V.1.2: Apply knowledge of Greek and Latin roots and affixes to determine meanings of words and phrases in grade-level content.",
  "ELA.K12.EE.1.1: Cite evidence to explain and justify reasoning."],
 "materials": ["The interactive lesson", "The Call of the Wild, Chapters IV and V", "Household objects for symbols, poster board, markers, sticky notes", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 22 warm-up questions."],
  [4, "Hook", "Plot versus message; the three symbols."],
  [11, "Symbols", "The club, the fire, the trail; how the club's meaning changes."],
  [11, "The fire vision", "Read the Chapter IV excerpt; ancestry; Darwin and London's era."],
  [11, "Topic versus theme", "Fix weak theme statements; the suffix -ity and root anim."],
  [11, "Foils", "Read the Chapter V excerpt; compare the drivers; John Thornton."],
  [6, "Assign", "Start the symbol museum; assign Chapters IV and V, Think Deeper and the Exit Check."]],
 "key_questions": ["What could this object stand for?", "Is that a topic or a theme?", "Where else in the book does this idea appear?", "How does comparing these characters reveal a message?"],
 "misconceptions": ["A theme is one word.", "Every object in a story is a symbol.", "A story has only one theme.", "The theme must be stated directly by the author."],
 "support": ["Provide a theme-statement frame: \"In [topic], people (or animals) learn that ...\"", "Read Chapters IV and V aloud together or use an audiobook.", "Use a symbol chart with columns for object, where it appears and meaning."],
 "challenge": ["Track the word \"call\" through the novel and predict what the title means.", "Compare London's view of instinct with what scientists know about dog behavior today."],
 "background": "<p><b>Content note:</b> Chapter IV describes the veteran dog Dave's illness and death on the trail with a new mail-team driver; Chapter V describes the starvation and beating of the dogs and the deaths of Hal, Charles and Mercedes when the sled breaks through the river ice. The Chapter IV vision passage includes a period label for the cook (not quoted in the lesson); explain to students that the label is outdated and hurtful. Darwin's On the Origin of Species was published in 1859; London read Darwin and Herbert Spencer, and the novel reflects ideas about heredity common in 1903 that modern science has revised.</p>",
 "sources": ["Jack London, The Call of the Wild (1903), Project Gutenberg.", "Labor, Earle, Jack London: An American Life (2013)."]
}

PRINT = {
 "directions": "Answer in complete sentences, citing the novel.",
 "items": [
  {"q":"Explain what the club, the fire and the trail symbolize.","a":"Club: force and power; fire: ancestry and the ancient past; trail: work and purpose.","lines":3},
  {"q":"What is the difference between a topic and a theme? Give an example of each from the novel.","a":"Topic: a word (survival); theme: a sentence about life (To survive, you must adapt even if you leave parts of yourself behind).","lines":3},
  {"q":"How are Hal, Charles and Mercedes foils to François and Perrault?","a":"The newcomers are ignorant and careless; the experienced drivers knew the trail and cared for the dogs.","lines":2},
  {"q":"Write a theme statement about knowledge or ignorance, supported by one quotation.","a":"Model: Ignorance can be more dangerous than the wilderness; \"They did not know how to do anything ... they could not learn.\"","lines":3},
  {"q":"What does London mean when he says Buck's instincts are \"the memories of his ancestors become habits\"?","a":"Buck's wild behaviors come from his ancestors and are waking up again in him.","lines":2},
  {"q":"Add -ity to adaptable, cruel and able. What does -ity mean?","a":"Adaptability, cruelty, ability; -ity means the state or quality of.","lines":2}]
}
