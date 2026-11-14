ARC = ('<svg viewBox="0 0 660 240" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Buck&apos;s journey across seven chapters, from Judge Miller&apos;s place to the wolf pack, with the unit&apos;s four reading tools">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Unit 5 review: Buck\'s journey and your reading tools</text>'
  '<path d="M40 150 Q140 70 220 120 T400 110 T620 60" fill="none" stroke="#C9A84C" stroke-width="5"/>'
  + ''.join(f'<circle cx="{x}" cy="{y}" r="7" fill="#0A1F3D"/><text x="{x}" y="{y+(24 if up else -14)}" text-anchor="middle" fill="#0A1F3D" font-weight="bold">{a}</text><text x="{x}" y="{y+(38 if up else -28)}" text-anchor="middle" fill="#5b6676" font-size="10">{b}</text>'
            for x, y, a, b, up in [(40, 150, "I", "stolen from the Judge's", True), (130, 99, "II", "club and fang", False), (220, 120, "III", "beats Spitz", True), (310, 125, "IV", "lead dog", True), (400, 110, "V", "Hal; Thornton", False), (510, 98, "VI", "love for Thornton", True), (620, 60, "VII", "the wolf pack", True)]) +
  ''.join(f'<rect x="{20+i*160}" y="196" width="148" height="34" rx="8" fill="{c}"/><text x="{94+i*160}" y="212" text-anchor="middle" fill="#fff" font-weight="bold">{a}</text><text x="{94+i*160}" y="225" text-anchor="middle" fill="#fff" font-size="10">{b}</text>'
          for i, (a, b, c) in enumerate([("Week 21: setting", "context and the Klondike", "#0A1F3D"), ("Week 22: conflict", "character change", "#0047BA"), ("Week 23: symbols", "theme across chapters", "#2c6e22"), ("Week 24: craft", "and the critic's lens", "#DB2F30")])) +
  '</svg>')

PASSAGE = ("<div class='passage'><p class='small'><b>From Chapter VI of <i>The Call of the Wild</i> (1903).</b> Thornton has bet that Buck can start a sled loaded with a thousand pounds of flour and pull it a hundred yards.</p>"
  "<p style='font-family:Georgia,serif'>Thornton knelt down by Buck's side. He took his head in his two hands and rested cheek on cheek. He did not playfully shake him, as was his wont, or murmur soft love curses; but he whispered in his ear. \"As you love me, Buck. As you love me,\" was what he whispered. Buck whined with suppressed eagerness.</p>"
  "<p style='font-family:Georgia,serif'>The crowd was watching curiously. The affair was growing mysterious. It seemed like a conjuration. As Thornton got to his feet, Buck seized his mittened hand between his jaws, pressing in with his teeth and releasing slowly, half-reluctantly. It was the answer, in terms, not of speech, but of love. Thornton stepped well back.</p>"
  "<p style='font-family:Georgia,serif'>\"Now, Buck,\" he said.</p>"
  "<p style='font-family:Georgia,serif'>Buck tightened the traces, then slacked them for a matter of several inches. It was the way he had learned.</p>"
  "<p style='font-family:Georgia,serif'>\"Gee!\" Thornton's voice rang out, sharp in the tense silence.</p>"
  "<p style='font-family:Georgia,serif'>Buck swung to the right, ending the movement in a plunge that took up the slack and with a sudden jerk arrested his one hundred and fifty pounds. The load quivered, and from under the runners arose a crisp crackling.</p>"
  "<p style='font-family:Georgia,serif'>\"Haw!\" Thornton commanded.</p>"
  "<p style='font-family:Georgia,serif'>Buck duplicated the manœuvre, this time to the left. The crackling turned into a snapping, the sled pivoting and the runners slipping and grating several inches to the side. The sled was broken out. Men were holding their breaths, intensely unconscious of the fact.</p>"
  "<p class='muted' style='font-size:12px'>wont: habit. conjuration: a magic spell. traces: harness straps. Gee and Haw: commands to turn right and left. arrested: stopped. manœuvre: the 1903 spelling of maneuver. broken out: freed from the ice frozen around the runners.</p></div>")

LESSON = {
 "unit": "Unit 5: Novel Study",
 "title": "Unit 5 Checkpoint and Literary Response Project",
 "subtitle": "You've followed Buck from a sunny California estate to the head of a wolf pack. This week you pull together everything you learned about setting, conflict, character, symbols, theme and craft, finish your literary response project, and show your mastery on the Unit 5 checkpoint.",
 "objectives": [
  "Explain how setting, conflict and character change work together across a whole novel.",
  "Trace a theme from beginning to end using symbols, foils and craft choices as evidence.",
  "Analyze an unfamiliar passage from the novel for character, tone and craft.",
  "Write a literary analysis with a clear claim, accurate quotations and explanation.",
  "Demonstrate mastery of Unit 5 on the checkpoint (85 or higher)."],
 "vocab": [
  ["literary analysis", "Writing that makes a claim about how a text works and supports it with evidence."],
  ["character arc", "The change a character goes through from the beginning of a story to the end."],
  ["thematic statement", "A complete sentence stating a theme, without naming characters."],
  ["textual evidence", "Quotations or specific details from a text that support a claim."],
  ["commentary", "Your explanation of how evidence supports your claim."]],
 "reconnect": {
  "title": "Unit 5, one question from each week",
  "intro": "Warm up with one question from each week of the unit.",
  "items": [
   {"t":"text","q":"Week 21: What event in the Yukon in 1896 created the demand for strong sled dogs?","a":[{"all":[["gold"]],"none":["not"]}],"show":"the Klondike Gold Rush (the gold strike)","pts":2,"why":"Men needed dogs to haul supplies north."},
   {"t":"text","q":"Week 22: The title of Chapter II names a law of the North. Complete it: the law of club and ___.","a":[{"all":[["fang"]],"none":["not"]}],"show":"fang","pts":2,"why":"Force rules in the North."},
   {"t":"text","q":"Week 23: A symbol that keeps returning through a novel is called a ___.","a":[{"all":[["motif"]],"none":["not"]}],"show":"motif","pts":2,"why":"Like the club or the call."},
   {"t":"text","q":"Week 24: An author's word choice is called ___.","a":[{"all":[["diction"]],"none":["not"]}],"show":"diction","pts":2,"why":"Diction creates tone."}]},
 "hook": {
  "title": "The Whole Journey",
  "visual": ARC,
  "html": "<p>Seven chapters, one journey. Buck begins as \"king\" of Judge Miller's place and ends as a legend running at the head of the pack. Every tool you practiced this unit, from reading the Klondike setting to questioning how London portrays the Yeehats, helps you explain not just what happens to Buck but why the novel works the way it does, and where it falls short.</p><div class='callout'><b>Big question:</b> How do all the parts of a novel work together to say something about life?</div>"},
 "learn": [
  {"title": "Review: Setting, Conflict and Character Change",
   "html": "<p>The Klondike setting (Week 21) creates the conflicts (Week 22): character versus nature (cold, hunger, ice), versus other characters (Spitz), versus society (the law of club and fang) and versus self (civilized habits against wild instincts). Those conflicts drive Buck's <b>character arc</b>: from pampered pet, to obedient sled dog, to cunning leader, to devoted companion, to wild hunter.</p>",
   "checks": [
    {"t":"order","q":"Put Buck's character arc in order.","items":["pampered pet at Judge Miller's","beaten into obedience by the man in the red sweater","lead dog after defeating Spitz","devoted companion to John Thornton","leader of the wolf pack"],"pts":2,"why":"Each conflict pushes him to the next stage."},
    {"t":"open","key":"settingconflict","q":"Choose one conflict from the novel and explain how the Klondike setting created it. Name the conflict type.","min":25,"rows":3,"rubric":["Names a specific conflict and its type","Explains how the setting caused or shaped it"],"model":"Buck's struggle to sleep in the snow is character versus nature. In California he slept warm in the Judge's house, but the Yukon winter forced him to learn to dig a hole in the snow like the other dogs, or freeze."}]},
  {"title": "Review: Symbols, Theme and Craft",
   "html": "<p>Symbols and motifs (the club, the fire, the trail, the call) carry the themes. Foils (François and Perrault against Hal, Charles and Mercedes; Thornton against Hal) sharpen them. Craft choices make them felt: tender diction for love, violent diction for the wild, a narrator who knows more than Buck, and a final shift into legend. A critical reader also asks whose story is missing, as with the Yeehats.</p>",
   "checks": [
    {"t":"open","key":"symboltheme","q":"Pick one symbol or motif and trace how its meaning changes from an early chapter to a late chapter. What theme does that change support?","min":35,"rows":3,"rubric":["Names a symbol and its early meaning, with a chapter","Names its later meaning, with a chapter","Connects the change to a theme stated as a sentence"],"model":"The call starts as a faint pull Buck can't name and grows louder until, after Thornton's death, Buck answers it in Chapter VII. That change supports the theme that the wild part of a creature can be buried by comfort but never erased."},
    {"t":"open","key":"crafteffect","q":"Name one craft choice London makes (diction, narrator, foreshadowing or structure) and explain how it affects you as a reader.","min":25,"rows":3,"rubric":["Names a specific craft choice with an example","Explains its effect on the reader"],"model":"London's foreshadowing with the call made me nervous every time Buck wandered into the woods. I knew that only Thornton was holding him back, so when Thornton died I already felt where the story was going."}]},
  {"title": "Finishing the Literary Response Project",
   "html": "<p>Your project has two parts (see the Unit 5 projects page): a <b>literary analysis essay</b> of 500 to 800 words and a <b>creative response</b>. A strong analysis paragraph follows <b>claim, evidence, commentary</b>:</p><ul><li><b>Claim:</b> a sentence about how the novel works, not a summary.</li><li><b>Evidence:</b> a short quotation, introduced with its context and chapter.</li><li><b>Commentary:</b> two or more sentences explaining <i>how</i> the evidence proves the claim. Commentary should be longer than the quotation.</li></ul><p>Before you turn it in, check that every quotation matches the book exactly.</p>",
   "checks": [
    {"t":"open","key":"fixparagraph","q":"This body paragraph is weak: \"Buck changes a lot. In Chapter III he fights Spitz. Then he becomes lead dog. This shows he changes.\" Rewrite it with a real claim, one piece of evidence and commentary.","min":45,"rows":5,"rubric":["A claim about how or why Buck changes, not a summary","Evidence introduced with context","Commentary that explains how the evidence supports the claim"],"model":"Buck's victory over Spitz shows that the North rewards cunning more than strength. London calls Buck \"the dominant primordial beast who had made his kill.\" Spitz is the more experienced fighter, but Buck wins by faking one attack and striking another. London's word primordial shows that this cunning comes from deep, ancient instincts, which is why Buck can rise to lead dog in a world where the old rules no longer work."}]}],
 "handson": {
  "title": "Evidence Gallery Walk",
  "intro": "Turn a room into a gallery of evidence for your essay, then test your argument on a visitor.",
  "materials": ["8 to 10 sheets of paper or sticky notes", "Markers", "Painter's tape", "The Call of the Wild", "Your project draft or outline", "A family member as a gallery visitor", "Paper and pencil"],
  "steps": [
   "Write your essay's claim in large letters on one sheet and tape it at eye level.",
   "On separate sheets, write your best pieces of evidence (one quotation per sheet, with the chapter). Check each quotation against the book.",
   "Tape the evidence around the room in the order you plan to use it, with a sticky note of commentary under each.",
   "Walk your visitor through the gallery. At each sheet, explain how the evidence supports your claim. Your visitor asks one \"So what?\" question at each stop.",
   "Revise any commentary that couldn't answer the question, then take down the tape so no one trips."],
  "record": [
   {"t":"open","key":"galleryrec","q":"Write your claim and your strongest piece of evidence. What \"So what?\" question did your visitor ask, and how did you revise your commentary to answer it?","min":45,"rows":4,"rubric":["Claim and evidence written out accurately","The visitor's question","A specific revision to the commentary"],"model":"Claim: London uses foils to show that knowledge of nature matters more than wealth. Evidence: Hal, Charles and Mercedes \"did not know how to do anything.\" My visitor asked, \"So what if they didn't know things?\" I revised my commentary to explain that their ignorance kills the dogs and finally themselves, while François and Perrault, who are not rich, survive because they know the trail."}]},
 "think": {
  "intro": "Your teacher scores this.",
  "items": [
   {"t":"open","key":"unitreflect","q":"Look back at the whole novel study. Which reading tool from this unit (setting, conflict, symbols, theme, craft or reading as a critic) changed how you understood The Call of the Wild the most? Explain with an example, and name one tool you want to use on your next book.","min":51,"rows":5,"rubric":["Names a tool and explains how it changed your understanding","A specific example from the novel","Names a tool for the next book, with a reason"],"model":"Reading as a critic changed my understanding most. At first I just cheered for Buck in Chapter VII, but after comparing the Yeehats with the real Tr'ondëk Hwëch'in, I noticed London never gave them names or reasons. On my next book I want to use symbols, because tracking the call showed me how one image can carry a whole theme."}]},
 "checkpoint": {
  "title": "Unit 5 Checkpoint: Novel Study",
  "intro": "This checkpoint covers Weeks 21 to 24. Part A uses a passage from Chapter VI; you may reread it as often as you like. You may use your copy of the novel for Parts B and C but not your notes. Mastery is 85 or higher. If you score below 85, your teacher will review with you, then you will retake it.",
  "parts": [
   {"title": "Part A: Analyze a passage", "items": [
    {"t":"open","key":"cpcharacter","q":PASSAGE + "<p>What does this passage reveal about the relationship between Buck and Thornton? Support your answer with two quotations from the passage.</p>","min":30,"rows":4,"pts":5,"rubric":["A clear statement about the relationship","Two accurate quotations from the passage","Explanation of how each quotation shows the relationship"],"model":"The passage shows that Buck works for Thornton out of love, not fear. Thornton whispers, \"As you love me, Buck,\" instead of commanding him, and Buck answers by gently holding Thornton's hand in his jaws, which London calls \"the answer, in terms, not of speech, but of love.\" Unlike the man with the club, Thornton gets Buck's best effort through trust."},
    {"t":"open","key":"cptone","q":"Reread the passage from \"Gee!\" to the end. How does London's diction create suspense? Name two words or phrases and explain their effect.","min":25,"rows":3,"pts":4,"rubric":["Two specific words or phrases from the passage","Explains how each builds tension or suspense"],"model":"London uses sounds that grow louder: a \"crisp crackling\" turns into \"a snapping,\" so readers hear the ice breaking little by little. Then \"Men were holding their breaths\" makes the reader hold their breath too, waiting to see if Buck can move the sled."},
    {"t":"open","key":"cpcontrast","q":"Compare this scene with the scene in Chapter I where Buck faces the man in the red sweater. How has the source of Buck's obedience changed, and what does that change show about the novel's themes?","min":35,"rows":4,"pts":5,"rubric":["Describes the Chapter I source of obedience","Describes the Chapter VI source of obedience","Connects the change to a theme"],"model":"In Chapter I, Buck obeys because the club beats him into it; the man rules by force. In Chapter VI, Buck strains with all his strength because he loves Thornton. The change shows a theme of the novel: force can make a creature obey, but only love and respect earn its full loyalty."},
    {"t":"text","q":"In the passage's last paragraph, which word tells you the men did not realize they were holding their breaths?","a":[{"all":[["unconscious"]],"none":["not"]}],"show":"unconscious","pts":2,"why":"\"intensely unconscious of the fact\" means they didn't notice."}]},
   {"title": "Part B: The whole novel", "items": [
    {"t":"open","key":"cpsetting","q":"Explain how the historical setting of the Klondike Gold Rush makes Buck's story possible. Include one fact about the real history you learned in Week 21.","min":25,"rows":3,"pts":4,"rubric":["Explains the connection between the gold rush and Buck's kidnapping or journey","One accurate historical fact from Week 21"],"model":"The gold rush created a huge demand for strong dogs to haul supplies, which is why Manuel steals Buck and sells him north. In real history, the strike was made in 1896 on a creek off the Klondike River, and the Klondike was the homeland of the Tr'ondëk Hwëch'in."},
    {"t":"open","key":"cpfoil","q":"Choose one pair of foils in the novel. Explain what the contrast reveals about a theme, and state that theme as a complete sentence.","min":30,"rows":3,"pts":4,"rubric":["Names a valid pair of foils with a specific difference","A thematic statement as a full sentence that names no characters","Explains how the contrast reveals it"],"model":"Thornton and Hal are foils. Thornton treats his dogs \"as if they were his own children,\" while Hal beats Buck when he refuses to move. The contrast reveals the theme that kindness earns loyalty, while cruelty only destroys."},
    {"t":"open","key":"cppov","q":"Explain how the point of view shifts at the end of the novel and why that shift fits Buck's final change.","min":25,"rows":3,"pts":4,"rubric":["Describes the shift from inside Buck to a legend told from outside","Explains why it fits his change into a wild animal"],"model":"Most of the novel stays close to Buck's thoughts, but at the end the narrator steps back and tells Buck's story as a legend the Yeehats tell about a Ghost Dog. The shift fits because Buck has left the human world; we can no longer see inside his mind, just as people can't understand a wild wolf."},
    {"t":"open","key":"cpcritic","q":"A friend says, \"The Call of the Wild is a great adventure, so there's nothing to criticize.\" Respond with one strength of the novel's craft and one problem a critical reader should notice, using specific examples.","min":35,"rows":4,"pts":5,"rubric":["One specific strength of craft, with an example","One specific problem, with an example","A balanced response to the friend"],"model":"It is a great adventure: London's diction, like calling Buck \"a live hurricane of fury,\" makes every scene feel alive. But a critical reader should notice that the Yeehats have no names, motives or point of view and are described only as attackers, a stereotype that hides the real Tr'ondëk Hwëch'in and other First Nations of the Klondike. A book can be exciting and still deserve criticism."}]},
   {"title": "Part C: Write an analysis paragraph", "items": [
    {"t":"open","key":"cpparagraph","q":"Write one analysis paragraph (claim, evidence, commentary) answering this question: Is Buck's ending a triumph, a loss or both? Use at least one quotation from Chapter VII and one from an earlier chapter.","min":98,"rows":9,"pts":8,"rubric":["A clear, arguable claim that answers the question","At least two accurate quotations, one from Chapter VII and one earlier","Commentary that explains how each quotation supports the claim","Organized, with a concluding sentence"],"model":"Buck's ending is both a triumph and a loss. In Chapter VII he finally answers the call and runs \"at the head of the pack,\" free and powerful, a triumph over every man who tried to rule him with a club. Yet the ending also costs him the only love he ever knew. In Chapter VI London says that \"Love, genuine passionate love, was his for the first time,\" and that love dies with Thornton. Buck becomes a legend, but he returns each summer to Thornton's valley to howl \"long and mournfully.\" London shows that freedom and loss can arrive together: Buck wins the wild only after losing the one bond that held him to people."}]}]},
 "next": "Unit 6: research and presentation, starting with asking research questions."
}

TEACHER = {
 "standards": [
  "ELA.6.R.1.1: Analyze how the interaction between characters contributes to the development of a plot in a literary text.",
  "ELA.6.R.1.2: Analyze the development of stated or implied theme(s) throughout a literary text.",
  "ELA.6.R.1.3: Explain the influence of multiple narrators and/or shifts in point of view in a literary text.",
  "ELA.6.R.3.1: Explain how figurative language contributes to tone and meaning in text(s).",
  "ELA.6.C.1.4: Write expository texts to explain and/or analyze information from multiple sources, using a logical organizational structure, relevant elaboration, and varied transitions.",
  "ELA.K12.EE.1.1: Cite evidence to explain and justify reasoning."],
 "materials": ["The interactive lesson", "The Call of the Wild (the whole novel)", "8 to 10 sheets of paper or sticky notes, markers, painter's tape", "The student's project draft", "The Unit 5 projects page and rubric", "The Unit 5 checkpoint"],
 "flow": [
  [6, "Reconnect", "Run one question from each week of the unit."],
  [4, "Hook", "Buck's whole journey and the four tools."],
  [10, "Setting, conflict, character", "Order the arc; setting creates conflict."],
  [10, "Symbols, theme, craft", "Trace a symbol; name a craft effect."],
  [12, "Project workshop", "Claim, evidence, commentary; fix the weak paragraph."],
  [8, "Assign", "Set up the evidence gallery; review the project rubric; assign the reflection."],
  [10, "Checkpoint preview", "Explain that the checkpoint is completed after class, independently, one try per item, with no answers shown until you review it. The novel may be used for Parts B and C, notes may not. Mastery is 85; below 85 means a review lesson and a retake."]],
 "key_questions": ["Is this a claim or a summary?", "Does your commentary explain how, not just what?", "Is the quotation exact?", "What does the novel get right, and what does it leave out?"],
 "misconceptions": ["Literary analysis means retelling the plot.", "One quotation proves a claim by itself, without commentary.", "Criticizing a book means you didn't like it.", "A theme can be one word."],
 "support": ["Provide a claim-evidence-commentary paragraph frame.", "Let the student mark passage evidence with colored pencils before writing.", "Read the passage aloud together before Part A (reading support does not change the scoring)."],
 "challenge": ["Compare The Call of the Wild with London's White Fang (1906), which reverses Buck's journey.", "Write a short literary analysis of London's ending from the point of view of a Tr'ondëk Hwëch'in reader."],
 "background": "<p>The Part A passage is from Chapter VI, checked against Project Gutenberg eBook #215 (\"manœuvre\" keeps its 1903 spelling). Checkpoint totals: Part A 16, Part B 17, Part C 8, total 41; mastery is about 35 of 41. Part C is scored with the four-trait rubric (2 points each). Students who read Chapter VII in summary can still answer every item.</p>",
 "sources": ["London, Jack. The Call of the Wild (1903), Project Gutenberg eBook #215.", "Florida Department of Education, B.E.S.T. Standards for English Language Arts (2020)."]
}

PRINT = {
 "directions": "Use the novel to answer. Quote exactly.",
 "items": [
  {"q":"List Buck's five stages of change in order.","a":"Pampered pet; beaten into obedience; lead dog; devoted to Thornton; leader of the wolf pack.","lines":2},
  {"q":"Name the four types of conflict and give one example of each from the novel.","a":"Versus nature (snow, ice); versus character (Spitz); versus society (law of club and fang); versus self (civilized versus wild).","lines":4},
  {"q":"Choose one symbol and explain what it stands for.","a":"The club: force and human power; the fire: ancestry; the call: the wild.","lines":2},
  {"q":"Write a thematic statement for the novel and give two pieces of evidence.","a":"Model: Comfort can bury the wild in a creature, but cannot erase it; Buck's dreams by the fire; Buck answering the call.","lines":4},
  {"q":"Explain the parts of an analysis paragraph.","a":"Claim (a point about how the text works), evidence (an exact quotation with context), commentary (explanation of how the evidence proves the claim).","lines":3}]
}
