MAP4 = ('<svg viewBox="0 0 640 210" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Unit 4 argument toolkit by week">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Unit 4: Making the Case</text>'
  + ''.join(f'<g transform="translate({16+i*156},36)"><rect width="144" height="160" rx="12" fill="{c}"/><text x="72" y="24" text-anchor="middle" fill="#fff" font-weight="bold" font-size="12">{a}</text>'
            + ''.join(f'<text x="72" y="{50+j*18}" text-anchor="middle" fill="#fff" font-size="11">{t}</text>' for j, t in enumerate(lines)) + '</g>'
            for i, (a, c, lines) in enumerate([
              ("Week 16: Build", "#0A1F3D", ["claim, reason,", "evidence", "relevant, sufficient,", "credible", "C-R-E-E", "Anthony, 1873"]),
              ("Week 17: Test", "#0047BA", ["logic, emotion,", "credibility", "5 fallacies", "cherry-picking,", "false cause", "Douglass, 1852"]),
              ("Week 18: Answer", "#8a6d1f", ["counterclaim,", "concede, rebut", "no straw men", "analogy", "Paine, 1776", ""]),
              ("Week 19: Write", "#DB2F30", ["introduction,", "thesis, body,", "counterclaim,", "conclusion", "cite honestly", "revise"])])) +
  '</svg>')

SPLASH = ("<div class='card' style='border-left-color:#0047BA'><h3 style='margin-top:0'>Our Town Needs a Splash Pad</h3><p class='muted' style='margin-top:-6px'>A practice letter to the editor written by KingCretot Experience for this checkpoint. Paragraphs are numbered.</p>"
          "<p><b>[1]</b> Every summer, families in our town drive 40 minutes to the nearest splash pad because we have nowhere close to cool off. Our town should build a splash pad in Central Park this year.</p>"
          "<p><b>[2]</b> First, a splash pad keeps children safe in the heat. The National Weather Service warns that heat is one of the leading weather-related causes of death in the United States, and children are especially at risk. A shaded splash pad gives kids a safe place to play outdoors on hot days.</p>"
          "<p><b>[3]</b> Second, a splash pad is safer than a pool for young children because there is no standing water deep enough to swim in. My neighbor's twins love the splash pad in the next town and have never had a single problem there.</p>"
          "<p><b>[4]</b> Everyone I've talked to wants one. The people who oppose it are just grumpy residents who don't like children.</p>"
          "<p><b>[5]</b> Some council members say a splash pad costs too much. It is true that building one can cost tens of thousands of dollars. However, our state offers recreation grants for small towns, and a splash pad needs no lifeguards, so it costs far less to run than a pool. The council should apply for a grant this spring.</p></div>")

LESSON = {
 "unit": "Unit 4: Making the Case (Argument)",
 "title": "Unit 4 Checkpoint and Argument Project",
 "subtitle": "This week you finish your argument project, a researched argumentative essay you also deliver as a speech, review every tool from Unit 4, and show your mastery on the Unit 4 checkpoint.",
 "objectives": [
  "Analyze a new argument: its claim, reasons, evidence, reasoning and counterclaim.",
  "Identify fallacies and misleading evidence, and explain why they are weak.",
  "Write and revise a counterclaim paragraph with a fair concession and a rebuttal.",
  "Complete and present a researched argumentative essay.",
  "Demonstrate mastery of Unit 4 on the checkpoint (85 or higher)."],
 "vocab": [
  ["claim", "The main point an argument wants the reader to accept."],
  ["evidence", "Facts, statistics, examples or expert words that prove a reason."],
  ["fallacy", "A mistake in reasoning that makes an argument seem stronger than it is."],
  ["counterclaim", "An opposing view that an argument answers."],
  ["rebuttal", "A response that shows why a counterclaim is wrong or weaker."],
  ["thesis", "The sentence that states an essay's claim."]],
 "reconnect": {
  "title": "Unit 4, one question from each week",
  "intro": "Warm up with one question from each week of the unit.",
  "items": [
   {"t":"text","q":"Week 16: \"According to the CDC, ...\" introduces what type of evidence: an anecdote or expert testimony?","a":[{"all":[["expert","testimony","statistic","fact"]],"none":["not","anecdote"]}],"show":"expert testimony (or a statistic from an expert organization)","pts":2,"why":"The CDC is a credible expert organization."},
   {"t":"text","q":"Week 17: \"If we let you have one cookie, you'll eat the whole jar and never eat vegetables again.\" Name the fallacy.","a":[{"all":[["slippery"]],"none":["not"]}],"show":"slippery slope","pts":2,"why":"An unsupported chain of disasters."},
   {"t":"text","q":"Week 18: Which word means to admit that part of the other side's point is true?","a":[{"all":[["concede","concession"]],"none":["not"]}],"show":"concede","pts":2,"why":"con + cede: to yield."},
   {"t":"text","q":"Week 19: Restating a source's information in your own words is called ___.","a":[{"all":[["paraphras"]],"none":["not"]}],"show":"paraphrasing","pts":2,"why":"Then cite the source."}]},
 "hook": {
  "title": "Three Voices, One Thread",
  "visual": MAP4,
  "html": "<p>In this unit you studied three writers who made the case for freedom in America: Thomas Paine's pamphlet in 1776, Frederick Douglass's speech in 1852 and Susan B. Anthony's speech in 1873. Each used evidence, reasoning and a clear understanding of the other side. Each also had a purpose: to move real people to act.</p><p>This week you finish your own argument and deliver it out loud, the way Douglass and Anthony did. Then you take the Unit 4 checkpoint.</p><div class='callout'><b>Big question:</b> What makes an argument strong enough to change a reader's mind?</div>"},
 "learn": [
  {"title": "Review: Building and Testing Arguments",
   "html": "<p>A strong argument has an <b>arguable claim</b>, <b>reasons</b>, and <b>evidence</b> that is relevant, sufficient and credible, with <b>explanation</b> connecting each piece of evidence to its reason. It uses logic, emotion and credibility honestly. A weak argument relies on fallacies: overgeneralization, bandwagon, attacking the person, either-or, slippery slope, straw man; or on misleading evidence such as cherry-picking and false cause.</p>",
   "checks": [
    {"t":"text","q":"\"Our soccer team won after I got a new haircut, so my haircut brings us luck.\" Which weak reasoning is this?","a":[{"all":[["false cause","cause"]],"none":["not","cherry"]}],"show":"false cause","pts":2,"why":"One thing coming first doesn't prove it caused the other."},
    {"t":"open","key":"revappeals","q":"Write one sentence for a claim about recycling that uses credibility, and one that uses emotion. Label each.","min":20,"rows":2,"rubric":["A credibility sentence (expert or experience)","An emotion sentence (vivid image, feeling)","Correctly labeled"],"model":"Credibility: Our county's recycling coordinator, who has worked in waste management for 20 years, says recycling saves the county money. Emotion: Picture a sea turtle tangled in a plastic bag that could have been recycled."}]},
  {"title": "Review: Counterclaims and Essays",
   "html": "<p>A counterclaim paragraph states the strongest reasonable objection fairly, concedes what is true and rebuts with reasons and evidence. An argumentative essay moves from an introduction (hook, background, thesis) through body paragraphs and a counterclaim paragraph to a conclusion that restates the claim in new words and calls the reader to act. Every source is cited honestly, without stretching what it says.</p>",
   "checks": [
    {"t":"open","key":"revcounter","q":"Claim: \"Families should limit phone use during dinner.\" Write a counterclaim paragraph of three to four sentences.","min":40,"rows":4,"rubric":["A fair counterclaim","A concession","A rebuttal with a reason","Transitions"],"model":"Some people argue that phones at dinner let families share photos and look up answers to questions that come up. It is true that phones can start conversations. However, when everyone is checking messages, people stop listening to each other, and dinner may be the only time all day a family talks face to face. A few phone-free minutes protect that time."}]},
  {"title": "Finishing the Argument Project",
   "html": "<p>Your Unit 4 project has two parts (see the Unit 4 Projects and Rubrics page):</p><ol><li><b>A researched argumentative essay</b> of 500 to 800 words on a question you choose from the project list, using at least three credible sources, with a counterclaim paragraph and a works-cited list.</li><li><b>A 2- to 3-minute speech</b> of your argument, delivered to an audience and recorded, using eye contact, a clear voice and pauses for emphasis.</li></ol><p>Use the revision checklist from Week 19 before you call your essay finished. For the speech, don't read word for word: use note cards with your key points and evidence.</p>",
   "checks": [
    {"t":"open","key":"projplan","q":"Write your project question, your thesis, your three sources (title and author or organization) and the counterclaim you will answer.","min":40,"rows":5,"rubric":["A question from the list or approved by a parent","An arguable thesis","Three credible sources named","A fair counterclaim"],"model":"Question: Should our county add bike lanes on main roads? Thesis: Our county should add protected bike lanes on main roads, because they make cycling safer and give families a way to travel without a car. Sources: the Federal Highway Administration's bike lane safety page; the League of American Bicyclists' Bicycle Friendly State ranking for Florida (bikeleague.org); a county news article about traffic. Counterclaim: bike lanes take space from cars and cost money."}]}],
 "handson": {
  "title": "Speech Rehearsal Circuit",
  "intro": "Rehearse your argument speech at different stations around your home, practicing one speaking skill at each.",
  "materials": ["Your essay and 3 to 5 index cards", "A timer", "A phone or tablet to record", "A mirror", "A family member as an audience", "Paper and pencil"],
  "steps": [
   "Write your speech on 3 to 5 index cards: your hook and thesis on the first, one reason with evidence on each middle card, and your counterclaim, rebuttal and call to action on the last.",
   "Station 1 (mirror): practice your opening while watching your face and hands. Smile, stand tall and avoid fidgeting.",
   "Station 2 (across a room): practice your evidence cards loudly enough for someone across the room to hear.",
   "Station 3 (timer): deliver the whole speech and time it. Aim for 2 to 3 minutes; cut or add as needed.",
   "Station 4 (audience): deliver it to a family member and record it. Ask them for one strength and one thing to improve, then record a final version."],
  "record": [
   {"t":"open","key":"speechrec","q":"Record your practice times, the feedback you got, and what you changed between your first and final recordings.","min":40,"rows":4,"rubric":["Times recorded","Specific feedback","Specific changes made"],"model":"First run: 3 minutes 40 seconds, too long. I cut one example. Final: 2 minutes 50 seconds. My dad said my evidence about the injury statistics was strong, but I talked too fast at the start. In my final recording I paused after my hook and looked up more often."}]},
 "think": {
  "intro": "Reflect on your growth. Your teacher scores this.",
  "items": [
   {"t":"open","key":"unitreflect","q":"Compare your Week 16 C-R-E-E paragraph with your final project essay. Name three specific ways your argument writing grew during Unit 4, with an example of each.","min":63,"rows":8,"rubric":["Three specific areas of growth (evidence quality, explanation, counterclaims, honest citation, organization, transitions, avoiding fallacies)","An example from the student's own writing for each","Thoughtful reflection"],"model":"First, my evidence is stronger: in Week 16 I used one anecdote, but my project essay uses three credible sources, including a federal safety report. Second, I explain my evidence now: I used to stop after the fact, but now I add a sentence about why it matters. Third, I answer the other side: my essay has a full counterclaim paragraph that concedes bike lanes cost money but shows how grants can pay for them."}]},
 "checkpoint": {
  "title": "Unit 4 Checkpoint: Making the Case",
  "intro": "This checkpoint covers Weeks 16 to 19. Read the letter to the editor in Part A carefully; you may reread it as often as you like. Mastery is 85 or higher. If you score below 85, your teacher will review with you, then you will retake it.",
  "parts": [
   {"title": "Part A: Analyze a new argument", "items": [
    {"t":"open","q":SPLASH + "What is the writer's claim? Quote or paraphrase it.","key":"cpclaim","min":10,"rows":2,"pts":3,"rubric":["Our town should build a splash pad in Central Park this year"],"model":"The town should build a splash pad in Central Park this year."},
    {"t":"open","q":"Compare the evidence in paragraphs 2 and 3. Which is stronger? Use the words relevant, sufficient or credible.","key":"cpevid","min":30,"rows":3,"pts":4,"rubric":["Paragraph 2 is stronger: credible expert source (National Weather Service), relevant to safety","Paragraph 3 is one anecdote: not sufficient, though relevant"],"model":"Paragraph 2 is stronger because it cites the National Weather Service, a credible source, and the fact is relevant to keeping kids safe in the heat. Paragraph 3 is only one neighbor's story, which is not sufficient to prove splash pads are always safe."},
    {"t":"open","q":"Paragraph 4 contains two fallacies. Name both and explain why each is weak.","key":"cpfall","min":30,"rows":3,"pts":4,"rubric":["Bandwagon or overgeneralization: \"Everyone I've talked to wants one\" (popularity, or a few conversations, isn't proof)","Attacking the person or straw man: opponents are \"grumpy residents who don't like children\" (attacks people instead of answering their real concerns)"],"model":"\"Everyone I've talked to wants one\" is bandwagon: popularity doesn't prove it's a good idea. Calling opponents \"grumpy residents who don't like children\" attacks the people (and creates a straw man) instead of answering their real concerns, like cost."},
    {"t":"open","q":"In paragraph 5, identify the counterclaim, the concession and the rebuttal.","key":"cpcounter","min":30,"rows":3,"pts":4,"rubric":["Counterclaim: a splash pad costs too much","Concession: it can cost tens of thousands of dollars","Rebuttal: state grants and lower running costs than a pool (no lifeguards)"],"model":"Counterclaim: some council members say it costs too much. Concession: it is true it can cost tens of thousands of dollars. Rebuttal: state grants can help pay, and it needs no lifeguards, so it costs less to run than a pool."}]},
   {"title": "Part B: Reasoning and texts from Unit 4", "items": [
    {"t":"text","q":"\"Either we buy a new car or we'll be stranded forever.\" Name the fallacy.","a":[{"all":[["either","false dilemma","false choice"]],"none":["not"]}],"show":"either-or","pts":3,"why":"There are other choices."},
    {"t":"text","q":"Which document did Susan B. Anthony use as her main evidence in 1873?","a":[{"all":[["constitution","preamble"]],"none":["not"]}],"show":"the U.S. Constitution (its preamble)","pts":3,"why":"\"We, the people.\""},
    {"t":"text","q":"Douglass said \"scorching irony, not convincing argument, is needed.\" Which appeal did he mean to rely on most: logic, emotion or credibility?","a":[{"all":[["emotion","pathos"]],"none":["not emotion"]}],"show":"emotion (pathos)","pts":3,"why":"Fire and thunder, not gentle light."},
    {"t":"open","q":"Paine compared America to a child who outgrows milk. Explain how this analogy rebuts the claim that America needed Britain because it had done well under Britain.","key":"cppaine","min":20,"rows":2,"pts":4,"rubric":["What helped at one stage of growth isn't needed forever","So past success under Britain doesn't prove America still needs Britain"],"model":"A baby needs milk, but it grows and needs other food. Paine means that even if Britain helped America when it was young, that doesn't mean America needs Britain forever."}]},
   {"title": "Part C: Write and revise", "items": [
    {"t":"open","q":"Revise this weak paragraph into a strong C-R-E-E paragraph (you may invent a realistic example, but not fake statistics): \"Kids should learn to cook. It's good. Everyone should do it.\"","key":"cprevise","min":53,"rows":5,"pts":5,"rubric":["A clear claim","A reason with because","Evidence (a realistic example or general knowledge, honestly presented)","An explanation connecting evidence to the reason","No fallacies (removes the bandwagon)"],"model":"Kids ages 11 to 13 should learn to cook simple meals, because cooking builds independence and healthy habits. For example, a student who can make scrambled eggs and a salad can feed themselves a healthy lunch instead of reaching for chips. Learning to cook now means that when they live on their own someday, they'll know how to eat well and save money."},
    {"t":"open","q":"Write a counterclaim paragraph for this claim: \"Our town should build a splash pad.\" Use a different counterclaim from the one in paragraph 5.","key":"cpwritecounter","min":40,"rows":4,"pts":5,"rubric":["A fair counterclaim different from cost (water use, maintenance, crowding, location, safety)","A concession","A rebuttal with a reason","Transitions"],"model":"Some residents worry that a splash pad wastes water during droughts. It is true that Florida sometimes faces water restrictions. However, many splash pads recirculate and filter their water, and the town could choose a recirculating design and close it during droughts. A well-designed splash pad can keep kids cool without wasting water."},
    {"t":"text","q":"The root cred means ___.","a":[{"all":[["believ"]],"none":["not"]}],"show":"believe","pts":3,"why":"credible, incredible."},
    {"t":"text","q":"The root vers means ___.","a":[{"all":[["turn"]],"none":["not"]}],"show":"turn","pts":3,"why":"reverse, adversary."}]}]},
 "next": "Unit 5: the novel study, starting with setting and context."
}

TEACHER = {
 "standards": [
  "ELA.6.R.2.4: Track the development of an argument, identifying the types of reasoning used.",
  "ELA.6.R.3.4: Identify rhetorical appeals in a text.",
  "ELA.6.C.1.3: Write and support a claim using logical reasoning, relevant evidence from sources, elaboration, and a logical organizational structure with varied transitions.",
  "ELA.6.C.2.1: Present information orally, in a logical sequence, using nonverbal cues, appropriate volume, clear pronunciation, and appropriate pacing.",
  "ELA.6.C.4.1: Conduct research to answer a question, drawing on multiple reliable and valid sources, and refocusing the inquiry when appropriate.",
  "ELA.6.V.1.2: Apply knowledge of Greek and Latin roots and affixes to determine meanings of words and phrases in grade-level content."],
 "materials": ["The interactive lesson", "The student's project essay and 3 to 5 index cards", "A timer, a phone or tablet to record, a mirror", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run one question from each week of the unit."],
  [4, "Hook", "Paine, Douglass and Anthony: three voices, one thread."],
  [10, "Building and testing", "Review appeals, fallacies and misleading evidence."],
  [9, "Counterclaims and essays", "Review the counterclaim paragraph and essay shape."],
  [14, "Project", "Check the project plan; review the rubric; start note cards."],
  [7, "Assign", "Assign the rehearsal circuit and the reflection."],
  [10, "Checkpoint preview", "Explain that the checkpoint is completed after class, independently, one try per item, with no answers shown until you review it. Mastery is 85; below 85 means a review lesson and a retake."]],
 "key_questions": ["Is the evidence relevant, sufficient and credible?", "Is this sound reasoning or a fallacy?", "Has the other side been stated fairly?", "Does every source say what the writer claims?"],
 "misconceptions": ["A speech should be read word for word.", "A counterclaim weakens an argument.", "Popular opinions are proven.", "Revising means fixing spelling."],
 "support": ["Allow the essay to be dictated and then edited.", "Provide a speech note-card template.", "Read the checkpoint letter aloud if reading is a barrier."],
 "challenge": ["Write a rebuttal to your own essay as if you were your strongest opponent.", "Deliver the speech to a new audience (grandparents by video call, a co-op group)."],
 "background": "<p>The checkpoint is scored out of 44 points: Part A 15, Part B 13, Part C 16. Open items are scored with the rubric after submission. A score of 85 percent is about 38 of 44 points. The splash-pad letter is a KCE practice text; the National Weather Service does list heat among the leading weather-related causes of death in the United States.</p>",
 "sources": ["Florida Department of Education, B.E.S.T. Standards for English Language Arts (2020).", "National Weather Service, Heat Safety."]
}

PRINT = {
 "directions": "Write in complete sentences. This is review practice, not the checkpoint.",
 "items": [
  {"q":"Define claim, reason, evidence and explanation.","a":"Claim: the main arguable point. Reason: why it's true. Evidence: facts, statistics, examples, expert words. Explanation: how the evidence proves the reason.","lines":3},
  {"q":"Name and give an example of four fallacies.","a":"Bandwagon: \"Everyone has this phone, so you need it.\" Attacking the person: \"Don't listen to her; she can't even cook.\" Either-or: \"Join the team or you'll never be fit.\" Slippery slope: \"One cookie and you'll never eat vegetables again.\"","lines":4},
  {"q":"Compare how Anthony, Douglass and Paine each used evidence.","a":"Anthony: the Constitution's preamble. Douglass: slaveholders' own laws and the Declaration. Paine: an analogy and reasoning about Britain's motives.","lines":3},
  {"q":"Write a thesis for: Should every family have an emergency plan for hurricanes?","a":"Model: Every Florida family should make a written hurricane plan before June, because it saves time, money and possibly lives when a storm comes.","lines":2},
  {"q":"Write a counterclaim paragraph for your thesis above.","a":"Model: Some families argue they can just watch the news and decide when a storm comes. It is true that forecasts give several days' warning. However, stores sell out of water and supplies quickly, so a plan made in advance keeps families from scrambling.","lines":4},
  {"q":"What do the roots cred, ver, contra, log, path, fall, ced and vers mean?","a":"believe, true, against, word/reason, feeling, deceive, go/yield, turn.","lines":2}]
}
