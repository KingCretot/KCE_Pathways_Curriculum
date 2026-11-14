TONE = ('<svg viewBox="0 0 660 210" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="A tone line from tender to menacing, with London&apos;s words placed along it">'
  '<text x="330" y="22" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Diction builds tone: where do London\'s words fall?</text>'
  '<defs><linearGradient id="tg" x1="0" x2="1"><stop offset="0" stop-color="#C9A84C"/><stop offset="0.5" stop-color="#8a95a5"/><stop offset="1" stop-color="#DB2F30"/></linearGradient></defs>'
  '<rect x="40" y="90" width="580" height="16" rx="8" fill="url(#tg)"/>'
  '<text x="40" y="128" font-weight="bold" fill="#8a6d1f">tender</text><text x="330" y="128" text-anchor="middle" font-weight="bold" fill="#5b6676">neutral</text><text x="620" y="128" text-anchor="end" font-weight="bold" fill="#DB2F30">menacing</text>'
  + ''.join(f'<path d="M{x} 86 v-14" stroke="#0A1F3D" stroke-width="2"/><text x="{x}" y="{y}" text-anchor="middle" fill="#0A1F3D" font-size="11" font-style="italic">{w}</text>' for x, y, w in [(70, 66, "adoration"), (150, 50, "sun-kissed"), (230, 66, "a cheering word"), (330, 50, "camp"), (430, 66, "luring"), (515, 50, "frenzy"), (595, 66, "a thing that preyed")]) +
  '<text x="330" y="160" text-anchor="middle" fill="#0047BA" font-size="12">Denotation = what a word means. Connotation = the feelings it carries.</text>'
  '<text x="330" y="182" text-anchor="middle" fill="#0047BA" font-size="12">"Home" and "house" denote the same place; "home" connotes warmth.</text></svg>')

LESSON = {
 "unit": "Unit 5: Novel Study",
 "title": "Author's Craft",
 "subtitle": "In Chapters VI and VII, Buck finds love with John Thornton and then answers the call of the wild. This week you study how London tells the story: his word choices, his narrator, the way he plants clues, and how he portrays the people Buck meets. You'll read as a writer and as a critic.",
 "objectives": [
  "Analyze how London's diction and figurative language create tone.",
  "Explain how the narrator's point of view, and its shift at the end, shapes the story.",
  "Identify foreshadowing and explain how the novel's structure comes full circle.",
  "Evaluate London's portrayal of the Yeehats using what you know about the Klondike's real First Nations.",
  "Use the roots prim, spir and imper to understand challenging words."],
 "vocab": [
  ["diction", "An author's choice of words."],
  ["connotation", "The feelings or ideas a word suggests beyond its dictionary meaning."],
  ["tone", "The author's attitude toward a subject, shown through word choice and details."],
  ["narrator", "The voice that tells a story."],
  ["foreshadowing", "Hints or clues about what will happen later in a story."],
  ["stereotype", "An oversimplified, often unfair idea about a whole group of people."],
  ["prim / spir / imper", "Latin roots meaning first (primitive, primordial), breathe (spirit, inspire) and command (imperious, imperative)."]],
 "reconnect": {
  "title": "Week 23: Symbols and theme",
  "intro": "This week's craft tools all serve the themes you traced last week.",
  "items": [
   {"t":"text","q":"What symbol keeps pulling Buck back toward people in Chapter VI: the club, the fire or the trail?","a":[{"all":[["fire"]],"none":["not fire","club","trail"]}],"show":"the fire","pts":2,"why":"Love for Thornton \"drew him back to the fire again.\""},
   {"t":"text","q":"What do we call a character whose differences highlight another character, like Hal compared with François?","a":[{"all":[["foil"]],"none":["not"]}],"show":"a foil","pts":2,"why":"Thornton is a foil too: the ideal master."},
   {"t":"open","key":"rc_themestate","q":"Write one theme statement about The Call of the Wild as a complete sentence (not one word).","min":10,"rows":2,"rubric":["A complete sentence","States an insight about life, not just a topic"],"model":"When the old rules no longer work, survival depends on adapting, even if it means losing part of who you were."},
   {"t":"open","key":"rc_thornton","q":"Last week, John Thornton saved Buck from Hal. Predict how Thornton, as a foil to Hal, will change Buck's story.","min":12,"rows":2,"rubric":["Contrasts Thornton with Hal", "A reasonable prediction"],"model":"Because Thornton is kind where Hal was cruel, I think Buck will love him and stay near people for a while, even as the wild keeps calling."}]},
 "hook": {
  "title": "Two Ways to Say It",
  "visual": TONE,
  "html": "<p>Read these two sentences:</p><ul><li>Buck liked Thornton very much.</li><li>\"Love, genuine passionate love, was his for the first time.\"</li></ul><p>They mean almost the same thing, but only London's sentence makes you <i>feel</i> it. The repetition of <i>love</i>, the commas that slow you down and the strong word <i>passionate</i> all work together. A few lines later London pushes further: \"love that was feverish and burning, that was adoration, that was madness.\"</p><p>Writers choose every word. This week you'll ask not just <i>what</i> happens in the novel, but <i>how</i> London makes it happen, and whose story he leaves out.</p><div class='callout'><b>Big question:</b> How do an author's choices shape what readers feel and believe?</div>"},
 "learn": [
  {"title": "Diction, Connotation and Tone",
   "html": "<p><b>Diction</b> is word choice. Words have a <b>denotation</b> (dictionary meaning) and a <b>connotation</b> (the feelings they carry). In Week 4 you chose strong verbs and precise nouns for your own writing; now watch how London uses them to set <b>tone</b>.</p><ul><li>Chapter VI, Thornton's camp: warm, tender words. Thornton never forgot \"a kindly greeting or a cheering word.\"</li><li>The call: mysterious, pulling words. The call is \"mysteriously thrilling and luring.\"</li><li>Chapter VII, Buck's attack: violent, overwhelming words. Buck is \"a live hurricane of fury, hurling himself upon them in a frenzy to destroy.\"</li></ul><p>In Week 11 you learned what a metaphor is. Here, the metaphor <i>hurricane</i> does more than compare: it tells us Buck has become a force of nature, beyond human control, which fits the theme of the wild taking over.</p>",
   "checks": [
    {"t":"text","q":"The feelings a word suggests beyond its dictionary meaning are its ___.","a":[{"all":[["connotation"]],"none":["not","denotation"]}],"show":"connotation","pts":2,"why":"Denotation is the dictionary meaning."},
    {"t":"open","key":"hurricane","q":"London calls Buck \"a live hurricane of fury.\" What does the metaphor suggest about Buck that a plain sentence like \"Buck attacked angrily\" does not? Connect it to a theme.","min":30,"rows":3,"rubric":["Explains what a hurricane suggests","Connects to a theme"],"model":"A hurricane is a force of nature that destroys everything in its path and can't be reasoned with. The metaphor shows that Buck is no longer a pet thinking like a civilized dog but part of the wild itself, which fits the theme that the wild has reclaimed him."},
    {"t":"open","key":"rewritetone","q":"Rewrite this plain sentence twice, once with a tender tone and once with a menacing tone, by changing only the diction: \"The dog walked toward the man in the camp.\"","min":20,"rows":3,"rubric":["A tender version with warm connotations","A menacing version with threatening connotations","The basic action stays the same"],"model":"Tender: The loyal dog padded softly toward his beloved master by the glowing fire. Menacing: The wolfish beast stalked silently toward the stranger crouched in the shadowy camp."}]},
  {"title": "The Narrator and Point of View",
   "html": "<p>The <b>narrator</b> is a third-person voice that knows Buck's thoughts and feelings, so we see the Klondike almost entirely through a dog's senses. But the narrator also knows things Buck cannot, as in the very first line: \"Buck did not read the newspapers, or he would have known that trouble was brewing.\" Readers learn about the gold rush, but Buck never does.</p><p>At the end, the point of view <b>shifts</b>. The narrator steps back, \"And here may well end the story of Buck,\" and the final pages read like a legend told over the years: \"the Yeehats tell of a Ghost Dog that runs at the head of the pack.\" We no longer see inside Buck. He becomes a story that other people tell, which makes him seem larger than life and turns the ending into a myth.</p>",
   "checks": [
    {"t":"text","q":"Is The Call of the Wild told in first person or third person?","a":[{"all":[["third"]],"none":["not third","first"]}],"show":"third person","pts":2,"why":"A narrator outside Buck tells his story."},
    {"t":"open","key":"newspaper","q":"The first line says Buck \"did not read the newspapers.\" What does this show about the narrator, and how does it create suspense?","min":25,"rows":3,"rubric":["Explains what the line shows about the narrator", "Explains how it creates suspense"],"model":"It shows the narrator knows more than Buck does, including the gold rush and the demand for strong dogs. It creates suspense because readers know trouble is coming while Buck has no idea."},
    {"t":"open","key":"povshift","q":"Why might London end the novel by shifting from Buck's thoughts to the legend of the Ghost Dog? Give one effect of the shift.","min":30,"rows":3,"rubric":["Describes the shift","An effect"],"model":"Once Buck fully joins the wild, we can no longer see into his mind, just as people can't understand a wild wolf. Telling his story as a legend makes him seem mythic and mysterious, which shows how completely he has left the human world."}]},
  {"title": "Foreshadowing and Structure",
   "html": "<p><b>Foreshadowing</b> plants clues. Throughout Chapters VI and VII, the call grows louder. In Chapter VI it is \"Deep in the forest a call was sounding,\" but love for Thornton \"drew him back to the fire again.\" Each time, Buck goes farther into the woods and stays away longer. Readers sense that only Thornton holds Buck back, so when Thornton dies, we already know what Buck will do.</p><p>The novel's <b>structure</b> comes full circle. In Chapter I, Buck rules Judge Miller's place as a king. In Chapter VII he rules again, now at the head of a wolf pack. Chapter titles trace the journey: \"Into the Primitive\" at the start, \"The Sounding of the Call\" at the end.</p>",
   "checks": [
    {"t":"order","q":"Put these steps of Buck's pull toward the wild in story order.","items":["Buck first feels the call but returns to the fire","Buck runs with the wild brother for a day","Buck stays away hunting for days at a time","Buck joins the wolf pack after Thornton's death"],"pts":2,"why":"Each step goes farther, which is foreshadowing."},
    {"t":"open","key":"fullcircle","q":"Explain how the novel comes full circle. Compare Buck in Chapter I with Buck at the end, using one similarity and one difference.","min":35,"rows":3,"rubric":["A similarity","A difference"],"model":"In both chapters Buck is a ruler: first the king of Judge Miller's place, then the leader of a wolf pack. But in Chapter I he is a pampered pet in sunny California living by human rules, and at the end he is a wild hunter in the Yukon living by instinct."}]},
  {"title": "Reading as a Critic: How London Portrays the Yeehats",
   "html": "<p>Good readers enjoy a book and also question it. In Chapter VII, a group London calls the <b>Yeehats</b> attacks Thornton's camp and kills him and his partners. Buck kills several of them, and London describes his rage at length. Afterward, Buck feels \"a great pride\" because \"He had killed man, the noblest game of all.\" The surviving Yeehats flee, \"proclaiming as they fled the advent of the Evil Spirit.\"</p><p>Notice what London gives the Yeehats: no names, no reasons for the attack, no families except grieving women at the very end, and no point of view except fear. They appear only as attackers and victims, and the narrator calls them \"Indians\" and treats their deaths as Buck's triumph. The Yeehats don't match any real First Nation.</p><p>In Week 21 you learned the real history: the Klondike was the homeland of the <b>Tr'ondëk Hwëch'in</b>, Keish (Skookum Jim), a Tagish and Tlingit man, helped make the first strike, and Tlingit packers carried stampeders' supplies over the Chilkoot. Many novels of London's time, the early 1900s, portrayed Indigenous peoples as nameless and dangerous. That <b>stereotype</b> shaped how readers saw real people. We can admire London's craft and still say plainly what he got wrong.</p>",
   "checks": [
    {"t":"open","key":"missing","q":"List three things London leaves out about the Yeehats that he gives to other characters such as Thornton or Hal.","min":15,"rows":2,"rubric":["Three specific omissions"],"model":"He never gives them names, never explains why they attack, and never shows their thoughts or daily life, while Thornton and Hal get names, motives and personalities."},
    {"t":"open","key":"stereoharm","q":"How could a portrayal like the Yeehats in a famous, widely read novel affect how readers saw real Indigenous people in 1903 and today? Use what you learned in Week 21.","min":40,"rows":4,"rubric":["Explains the stereotype","Contrasts with real history from Week 21","Explains a real effect"],"model":"The Yeehats are nameless, violent and frightened of an \"Evil Spirit,\" so readers might picture all Indigenous people that way. In reality, the Klondike was the Tr'ondëk Hwëch'in homeland, Keish helped find the gold and Tlingit packers made the stampede possible. A stereotype like this hides that history and the harm the rush caused, and can make readers dismiss real people even today."}]}],
 "handson": {
  "title": "Craft Lab: Tone Line and Retelling the Legend",
  "intro": "Move words along a tone line, then perform the ending two ways to feel how point of view changes a story.",
  "materials": ["Painter's tape or string about 8 feet long", "15 index cards and a marker", "The Call of the Wild, Chapters VI and VII", "A flashlight (for the campfire telling)", "A family member as audience", "Paper and pencil"],
  "steps": [
   "Lay the tape on the floor as a tone line. Label one end \"tender\" and the other \"menacing.\"",
   "Find 15 words or short phrases from Chapters VI and VII (for example adoration, luring, frenzy, a cheering word). Write each on a card.",
   "Place each card on the line where its connotation belongs. Walk the line and explain your choices to your audience. Move any card your audience questions, and explain why or why not.",
   "Retelling: turn off the lights and, using a flashlight as a campfire, perform the last three paragraphs of the novel as a legend in your own words.",
   "Then perform a short version of the same ending from the point of view of a Yeehat family, giving them names, a reason for being in the valley and their own feelings. Base it on respect, not on the stereotype."],
  "record": [
   {"t":"open","key":"tonerec","q":"Which three words were hardest to place on the tone line, where did you put them, and why? What did the line show you about how London's tone changes from Chapter VI to Chapter VII?","min":45,"rows":4,"rubric":["Three hard words with placements and reasons","A conclusion about the change in tone across the chapters"],"model":"\"Luring\" was hard because it sounds both exciting and dangerous, so I put it just past the middle. \"Camp\" is neutral by itself. \"Wild brother\" sounds friendly but also wild, so I placed it near tender. Most Chapter VI words ended up on the tender side and most Chapter VII words on the menacing side, which shows London's tone darkening as Buck leaves people behind."},
   {"t":"open","key":"retellrec","q":"How did your Yeehat-perspective retelling change the story? What did you add that London left out, and how did it change how your audience felt about the ending?","min":40,"rows":4,"rubric":["Describes the perspective retelling","Names what was added","Reflects on the audience's response"],"model":"I told it from the point of view of a grandmother whose family hunts moose in the fall. I added her name, her worry about the strangers digging for gold and her grief for the hunters who never came home. My audience said the Ghost Dog seemed frightening instead of glorious, and they felt sorry for the family instead of just cheering for Buck."}]},
 "think": {
  "intro": "Use evidence from the text. Your teacher scores these.",
  "items": [
   {"t":"open","key":"craftessay","q":"Choose two craft tools from this week (diction, figurative language, point of view, foreshadowing, structure). Explain how each helps London develop one theme of the novel. Quote the text at least twice.","min":113,"rows":8,"rubric":["Two craft tools named and explained","At least two accurate quotations","Each tool clearly linked to the same theme","Organized paragraphs with a clear claim"],"model":"London uses diction and point of view to develop the theme that the wild can reclaim even a civilized creature. First, his diction shifts from tender to violent. In Chapter VI, Buck feels \"love that was feverish and burning,\" but in Chapter VII he becomes \"a live hurricane of fury.\" The words move from warmth to destruction, showing Buck's civilized side giving way to the wild. Second, the point of view shifts at the end. After \"And here may well end the story of Buck,\" we no longer see inside Buck's mind; he becomes a legend that \"runs at the head of the pack.\" Because we can no longer understand him as a human would, the shift shows he has fully joined the wild. Together these choices make the theme felt, not just stated."},
   {"t":"open","key":"stillread","q":"Some schools and families still read The Call of the Wild; others choose different books because of its violence and its portrayal of the Yeehats. Should homeschool families still read it? Make a claim, give two reasons and answer one counterclaim, as you learned in Unit 4.","min":80,"rows":7,"rubric":["A clear claim","Two reasons supported with examples from the novel or this week","A counterclaim answered with a rebuttal"],"model":"Homeschool families should still read The Call of the Wild, as long as they discuss its problems. First, it teaches craft: London's diction, foreshadowing and shifting point of view are models for any writer. Second, reading it critically, as we did with the Yeehats, teaches students to question stereotypes instead of absorbing them. Some argue the violence and the portrayal of Indigenous people make it harmful. That concern is real, but avoiding the book wouldn't teach students how to recognize those problems; reading it with guidance, alongside the true history of the Tr'ondëk Hwëch'in, does."}]},
 "exit": [
  {"t":"text","q":"An author's word choice is called ___.","a":[{"all":[["diction"]],"none":["not"]}],"show":"diction","pts":2,"why":"Diction creates tone."},
  {"t":"text","q":"Hints about what will happen later in a story are called ___.","a":[{"all":[["foreshadow"]],"none":["not"]}],"show":"foreshadowing","pts":2,"why":"Like the call growing louder."},
  {"t":"text","q":"The Latin root in primitive and primordial means ___.","a":[{"all":[["first"]],"none":["not"]}],"show":"first","pts":2,"why":"Primitive: like the first, earliest ways."},
  {"t":"open","key":"exit_critic","q":"In one or two sentences, explain how a reader can admire a book's craft and still criticize it.","min":15,"rows":2,"rubric":["Separates skill in writing from the ideas or portrayals in the book","Gives an example"],"model":"You can admire how London's words make you feel Buck's love and rage while still pointing out that his Yeehats are an unfair stereotype."}],
 "next": "Week 25: Unit 5 checkpoint and literary response project."
}

TEACHER = {
 "standards": [
  "ELA.6.R.3.1: Explain how figurative language contributes to tone and meaning in text(s).",
  "ELA.6.R.1.3: Explain the influence of multiple narrators and/or shifts in point of view in a literary text.",
  "ELA.6.R.1.2: Analyze the development of stated or implied theme(s) throughout a literary text.",
  "ELA.6.V.1.2: Apply knowledge of Greek and Latin roots and affixes to determine meanings of words and phrases in grade-level content.",
  "ELA.K12.EE.1.1: Cite evidence to explain and justify reasoning."],
 "materials": ["The interactive lesson", "The Call of the Wild, Chapters VI and VII", "Painter's tape or string, 15 index cards, a marker, a flashlight", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 23 warm-up questions."],
  [4, "Hook", "Two ways to say it: plain versus London."],
  [12, "Diction and tone", "Denotation and connotation; the hurricane metaphor; rewrite for tone."],
  [11, "Narrator and point of view", "The newspaper line; the shift to legend."],
  [10, "Foreshadowing and structure", "The growing call; full circle from Chapter I."],
  [12, "Reading as a critic", "The Yeehats; what's missing; connect to Week 21's real history."],
  [5, "Assign", "Set up the tone line; assign the retelling, Think Deeper and the Exit Check."]],
 "key_questions": ["Why this word and not another?", "Whose eyes are we seeing through, and whose are missing?", "What clues did London plant earlier?", "Can we admire a book and still criticize it?"],
 "misconceptions": ["Tone is the same as mood (tone is the author's attitude; mood is the reader's feeling).", "Third person means the narrator knows nothing about thoughts.", "Criticizing a classic means you shouldn't read it.", "The Yeehats are a real First Nation."],
 "support": ["Provide a connotation chart with sample words.", "Read the last three paragraphs aloud together before the retelling.", "Offer sentence frames: \"London's word ___ suggests ___ because ___.\""],
 "challenge": ["Compare London's portrayal of the Yeehats with an Indigenous-authored story or account of the Yukon.", "Rewrite one Chapter VI paragraph in first person from Buck's point of view and explain what changes."],
 "background": "<p>Chapter VII is violent: the Yeehats kill Thornton, his partners Hans and Pete, and the dogs at camp, and Buck kills several Yeehats; London describes the attack in graphic detail. The lesson quotes only short phrases. The Yeehats appear to be London's invention and do not correspond to a documented First Nation; their portrayal reflects stereotypes common in early twentieth-century fiction. Week 21 taught the Klondike's First Nations (Tr'ondëk Hwëch'in, Tagish, Tlingit). All quotations are checked against Project Gutenberg eBook #215. Families may preview Chapter VII and summarize the attack instead of reading it.</p>",
 "sources": ["London, Jack. The Call of the Wild (1903), Project Gutenberg eBook #215.", "Tr'ondëk Hwëch'in, Tr'ondëk-Klondike World Heritage Site (UNESCO, 2023).", "Florida Department of Education, B.E.S.T. Standards for English Language Arts (2020)."]
}

PRINT = {
 "directions": "Answer in complete sentences. Quote the novel where asked.",
 "items": [
  {"q":"Explain the difference between denotation and connotation, with an example.","a":"Denotation is the dictionary meaning; connotation is the feeling (home versus house).","lines":2},
  {"q":"How does London's diction change between Chapter VI and Chapter VII? Quote one word or phrase from each.","a":"From tender (\"a cheering word,\" \"adoration\") to violent (\"frenzy,\" \"hurricane of fury\").","lines":3},
  {"q":"What is the narrator's point of view, and how does it shift at the end?","a":"Third person, mostly inside Buck; at the end it steps back and tells Buck's story as a Yeehat legend.","lines":3},
  {"q":"Give one example of foreshadowing in Chapters VI and VII.","a":"The call grows louder and Buck stays away longer, hinting he will join the wild when Thornton is gone.","lines":2},
  {"q":"Describe London's portrayal of the Yeehats and one problem with it.","a":"Nameless attackers with no motives or point of view, called \"Indians\"; it stereotypes Indigenous peoples and erases real First Nations like the Tr'ondëk Hwëch'in.","lines":3},
  {"q":"Use the roots prim, spir and imper to define primordial, inspire and imperious.","a":"Primordial: existing from the first; inspire: breathe in, fill with an idea; imperious: commanding.","lines":3}]
}
