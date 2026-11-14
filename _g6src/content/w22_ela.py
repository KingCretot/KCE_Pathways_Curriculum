ARC = ('<svg viewBox="0 0 640 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Buck&apos;s change from Chapter I to Chapter III shown as steps">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Buck changes, step by step (Chapters I to III)</text>'
  + ''.join(f'<g transform="translate({20+i*124},{170-i*30})"><rect width="112" height="{40+i*30}" rx="8" fill="{c}"/><text x="56" y="18" text-anchor="middle" fill="#fff" font-weight="bold">{a}</text>'
            + ''.join(f'<text x="56" y="{34+j*13}" text-anchor="middle" fill="#fff" font-size="10">{t}</text>' for j, t in enumerate(lines)) + '</g>'
            for i, (a, c, lines) in enumerate([
              ("King", "#C9A84C", ["proud, comfortable"]),
              ("Beaten", "#8a6d1f", ["learns the club", "must be obeyed"]),
              ("Learner", "#0047BA", ["watches, sleeps in", "snow, toughens"]),
              ("Thief", "#1d6fb8", ["steals food to", "survive; moral", "nature \"decays\""]),
              ("Rival", "#DB2F30", ["the primordial beast", "grows; conflict", "with Spitz builds", ""])])) +
  '<text x="320" y="224" text-anchor="middle" font-size="10" fill="#5b6676">Is each step growth or loss? London uses both words: \"development (or retrogression).\"</text></svg>')

CH2 = ("<div class='card' style='border-left-color:#C9A84C'><h3 style='margin-top:0'>From Chapter II: \"The Law of Club and Fang\"</h3><p class='muted' style='margin-top:-6px'>Jack London, The Call of the Wild (1903). ... marks words left out.</p>"
       "<p style='font-family:Georgia,serif'>Buck's first day on the Dyea beach was like a nightmare. Every hour was filled with shock and surprise. He had been suddenly jerked from the heart of civilization and flung into the heart of things primordial. No lazy, sun-kissed life was this, with nothing to do but loaf and be bored. Here was neither peace, nor rest, nor a moment's safety. ...</p>"
       "<p style='font-family:Georgia,serif'>This first theft marked Buck as fit to survive in the hostile Northland environment. It marked his adaptability, his capacity to adjust himself to changing conditions, the lack of which would have meant swift and terrible death. It marked, further, the decay or going to pieces of his moral nature, a vain thing and a handicap in the ruthless struggle for existence. It was all well enough in the Southland, under the law of love and fellowship, to respect private property and personal feelings; but in the Northland, under the law of club and fang, whoso took such things into account was a fool ...</p>"
       "<p class='muted' style='font-size:12px'>primordial: from the earliest times; wild and basic. hostile: unfriendly, dangerous. adaptability: the ability to adjust to new conditions. vain: useless. whoso: whoever.</p></div>")

LESSON = {
 "unit": "Unit 5: Novel Study",
 "title": "Conflict and Character Change",
 "subtitle": "In Chapters II and III, Buck is thrown into the brutal world of the sled dogs. Every day brings a new conflict, and every conflict changes him. This week you name the types of conflict, trace how Buck changes and decide for yourself: is he growing, or losing something?",
 "objectives": [
  "Identify and explain types of conflict: character versus character, nature, society and self.",
  "Trace how conflicts drive a character's change using text evidence.",
  "Use indirect characterization (STEAL, Week 2) to trace how Buck changes over time.",
  "Analyze how London presents Buck's change as both adaptation and loss.",
  "Use the roots morph, mort and vit to understand challenging words."],
 "vocab": [
  ["conflict", "A struggle between opposing forces that drives a story's plot."],
  ["external conflict", "A struggle between a character and an outside force: another character, nature or society."],
  ["internal conflict", "A struggle within a character's own mind."],
  ["protagonist", "The main character of a story."],
  ["antagonist", "The character or force that opposes the protagonist."],
  ["characterization", "How an author reveals a character, directly (telling) or indirectly (showing through actions, words and thoughts)."],
  ["adaptation", "A change that helps a living thing survive in its environment."]],
 "reconnect": {
  "title": "Week 21: Setting and context",
  "intro": "Last week the setting changed from California to the Klondike. This week you see what that change does to Buck.",
  "items": [
   {"t":"text","q":"Where did Buck live before he was stolen? (Name the valley.)","a":[{"all":[["santa clara"]],"none":["not"]}],"show":"the Santa Clara Valley, California","pts":2,"why":"Judge Miller's place."},
   {"t":"text","q":"What lesson did the man in the red sweater teach Buck? Finish the phrase: \"a man with a club was a ___.\"","a":[{"all":[["lawgiver","law giver","master"]],"none":["not"]}],"show":"lawgiver (a master to be obeyed)","pts":2,"why":"Chapter I."},
   {"t":"text","q":"The root prim means ___.","a":[{"all":[["first"]],"none":["not"]}],"show":"first","pts":2,"why":"Today: primordial, from the very first times."},
   {"t":"open","key":"rc_predict","q":"Last week you predicted how Buck would change. Was your prediction right after Chapters II and III? Explain with one detail.","min":15,"rows":2,"rubric":["Compares the prediction to what happened","One accurate detail from Chapters II or III"],"model":"I predicted Buck would get tougher, and I was right: in Chapter II he learns to steal bacon to survive, and by Chapter III he and Spitz hate each other."}]},
 "hook": {
  "title": "The First Day on the Beach",
  "visual": ARC,
  "html": "<p>Buck steps off a ship onto the beach at Dyea, Alaska, and nothing is the same. Dogs fight to the death. Men beat them with clubs. Food is stolen if you don't eat it fast. Buck has just seen snow for the first time, and he doesn't know where to sleep.</p><p>A story's <b>conflicts</b>, its struggles, are what make it move. In these chapters, London stacks one conflict on another, and each one reshapes Buck.</p><div class='callout'><b>Big question:</b> How do struggles change a character, and is the change growth or loss?</div>"},
 "learn": [
  {"title": "Types of Conflict",
   "html": "<p>In Week 1 you named Mateo's internal and external conflicts. Now split external conflict into three kinds:</p><ul><li><b>External:</b> <i>character versus character</i> (Buck against Spitz, the lead dog who bullies him); <i>character versus nature</i> (Buck against snow, cold, hunger and exhaustion); <i>character versus society</i> (Buck against the rules of men with clubs and the brutal \"law\" of the dog teams).</li><li><b>Internal:</b> <i>character versus self</i> (Buck's civilized habits fighting his growing wild instincts).</li></ul><p>The <b>protagonist</b> is Buck. In Chapter III, the <b>antagonist</b> is Spitz, a cunning, experienced sled dog from Spitzbergen who leads the team and sees Buck as a threat.</p>",
   "checks": [
    {"t":"blanks","q":"Name the type of conflict.","sent":"Buck learning to dig a hole in the snow to sleep: Buck versus ___. Buck and Spitz's growing hatred: Buck versus ___ (type of conflict).","blanks":[[{"all":[["nature"]],"none":["not"]}],[{"all":[["character","spitz"]],"none":["not","nature","society"]}]],"show":"nature; character","pts":2,"why":"Snow and cold are nature; Spitz is another character."},
    {"t":"open","key":"internal","q":"Describe Buck's internal conflict in Chapters II and III. What two sides are fighting inside him?","min":25,"rows":3,"rubric":["Civilized habits and morals from the Southland (respecting property, rules)","versus wild, primitive instincts needed to survive (stealing, fighting, cunning)"],"model":"Inside Buck, the civilized habits he learned at Judge Miller's, like respecting property and feelings, are fighting the wild, primitive instincts he needs to survive in the North, like stealing food and being cunning."}]},
  {"title": "Adaptation or Loss? Chapter II",
   "html": CH2 + "<p>London describes Buck's first theft of food in two ways at once. It shows his <b>adaptability</b>, the ability to survive. But it also marks \"the decay or going to pieces of his moral nature.\" Later London calls Buck's change his \"development (or retrogression),\" which means moving backward. The narrator wants us to feel both.</p><p><b>Roots:</b> <i>mort</i> means death (mortal, immortal, mortality). <i>Vit/viv</i> means life (vital, vitamin, survive, revive). <i>Morph</i> means form or shape (metamorphosis, amorphous).</p>",
   "checks": [
    {"t":"open","key":"twowords","q":"London says the theft \"marked Buck as fit to survive\" and also marked \"the decay ... of his moral nature.\" Why does he describe the same act in two opposite ways? What is he asking readers to think about?","min":35,"rows":3,"rubric":["Stealing helps Buck survive (adaptation) but means giving up his old morals (loss)","London wants readers to question whether survival justifies losing morals, or whether morals depend on the setting"],"model":"Stealing helps Buck survive, so it's a smart adaptation, but it also means giving up the honesty he had in the Southland. London describes it both ways so readers will wonder whether surviving is worth losing your morals, and whether right and wrong depend on where you live."},
    {"t":"text","q":"London contrasts the \"law of love and fellowship\" in the Southland with what law in the Northland?","a":[{"all":[["club"],["fang"]],"none":["not"]}],"show":"the law of club and fang","pts":2,"why":"The chapter title."},
    {"t":"blanks","q":"Use the roots.","sent":"Something necessary for life is ___ (vit). A living thing that will someday die is ___ (mort).","blanks":[[{"all":[["vital"]],"none":["not"]}],[{"all":[["mortal"]],"none":["not","immortal"]}]],"show":"vital; mortal","pts":2,"why":"vit = life; mort = death."}]},
  {"title": "How London Reveals Character",
   "html": "<p>In Week 2 you used STEAL (Speech, Thoughts, Effect on others, Actions, Looks) to read characters. London relies on indirect characterization to show Buck changing. <b>Direct characterization</b> tells us what a character is like: \"He was fit, that was all.\" <b>Indirect characterization</b> shows it through actions, choices and others' reactions: Buck watches the other dogs and learns from them; he digs his first sleeping hole in the snow after watching Billee; he steals bacon so slyly that another dog is punished instead.</p><p>Buck also learns from the other dogs, each with a personality: <b>Spitz</b>, cunning and cruel; <b>Dave</b> and <b>Sol-leks</b>, steady, hardworking veterans who want only to pull; <b>Curly</b>, friendly and trusting, whose death on the first day teaches Buck that once a dog goes down in a fight, it is finished. (Parents: Curly's death is described in Chapter II.)</p><p>The human drivers, <b>François</b> and <b>Perrault</b>, are French-Canadian government couriers carrying mail. London presents them as tough but fair to the dogs.</p>",
   "checks": [
    {"t":"open","key":"stealbacon","q":"London writes that Buck \"duplicated the performance the following day, getting away with the whole chunk\" of bacon, while Dub was punished. Which STEAL method is this, and what trait does it reveal that the Buck of Chapter I did not show?","min":20,"rows":2,"rubric":["Names the STEAL method","Names a new trait and contrasts it with Buck in Chapter I"],"model":"Actions. It shows cunning and a willingness to let another dog take the blame, which the proud, honest king of Judge Miller's place never needed."},
    {"t":"open","key":"curlylesson","q":"What lesson does Buck learn from what happens to Curly, and how does it change his behavior?","min":25,"rows":3,"rubric":["Once a dog goes down in a fight, the others finish it; there is no fair play","Buck resolves never to go down; he becomes watchful and careful in fights"],"model":"Buck learns that in this world there is no fair play: once a dog goes down, it's finished. After that, he decides he will never go down in a fight, and he becomes much more watchful and careful."}]},
  {"title": "Rising Conflict: Buck and Spitz",
   "html": "<p>Chapter III opens: \"The dominant primordial beast was strong in Buck, and under the fierce conditions of trail life it grew and grew. Yet it was a secret growth.\" Buck avoids fights and waits. The conflict with Spitz builds through the chapter: Spitz steals Buck's sleeping spot, Buck challenges Spitz's leadership by protecting other dogs, and the team falls into disorder. Tension rises until the two dogs fight for leadership. (Parents: the end of Chapter III describes a fight to the death; preview it.)</p><p>This is <b>rising action</b>: each event increases the tension and pushes the story toward a <b>climax</b>, the turning point.</p>",
   "checks": [
    {"t":"open","key":"secretgrowth","q":"London says the \"primordial beast\" in Buck grew in secret. What does Buck do, and not do, that shows his wildness is growing quietly?","min":25,"rows":3,"rubric":["He avoids fights and acts with patience and control instead of rashness","He waits and plans, using cunning; his strength and instincts grow without showing"],"model":"Buck doesn't pick fights and stays patient even though he hates Spitz. He waits, watches and plans, which shows his cunning and wild instincts are growing without him showing them yet."},
    {"t":"open","key":"spitzwhy","q":"Why is Spitz the antagonist? Explain what makes the conflict between Buck and Spitz so serious.","min":25,"rows":3,"rubric":["Spitz opposes Buck and sees him as a threat to his leadership","Only one can lead the team; in this world defeat means death"],"model":"Spitz opposes Buck at every turn because he sees Buck as a threat to his position as lead dog. The conflict is serious because only one dog can lead, and in the law of club and fang, losing a fight can mean death."}]}],
 "handson": {
  "title": "Conflict Map and Character Change Timeline",
  "intro": "Map every conflict in Chapters II and III, then build a life-size timeline of Buck's change across the floor.",
  "materials": ["Index cards or sticky notes in 4 colors", "Painter's tape or string about 10 feet long", "Markers", "The Call of the Wild (Chapters II and III)", "Paper and pencil"],
  "steps": [
   "As you read Chapters II and III, write each conflict on a card, color-coded: character vs. character, vs. nature, vs. society, vs. self. Include the page or paragraph.",
   "Lay a strip of tape or string across the floor as a timeline, from \"Judge Miller's\" at one end to \"End of Chapter III\" at the other.",
   "Place each conflict card on the timeline in story order. Under each, add a card saying how Buck changed because of it.",
   "Walk the timeline from start to finish, reading the cards aloud to a family member as you go. Stand on the spot where you think Buck changed the most and explain why.",
   "Keep the tape away from doorways so no one trips."],
  "record": [
   {"t":"open","key":"conflictmap","q":"List five conflicts from Chapters II and III, labeled by type, and the change each caused in Buck. Where on your timeline did he change the most?","min":60,"rows":6,"rubric":["Five accurate conflicts with types","Change caused by each","A supported choice of the biggest change"],"model":"1. Dogs attack Curly (character vs. character): Buck vows never to go down. 2. The first snowfall at night (nature): he learns to dig a sleeping hole. 3. Hunger on the trail (nature): he learns to eat fast and steal food. 4. The club rule and team life (society): he learns to obey and to pull in harness. 5. Old morals vs. new needs (self): he steals bacon and lets another dog take the blame. He changed most at the bacon theft, because London says it marked the \"decay\" of his moral nature."}]},
 "think": {
  "intro": "Use evidence from the novel. Your teacher scores these.",
  "items": [
   {"t":"open","key":"growthloss","q":"Is Buck's change in Chapters II and III growth or loss? Take a position, support it with at least two quotations, and acknowledge the other view.","min":96,"rows":8,"rubric":["A clear position","Two accurate quotations","Explains how the evidence supports the position","Acknowledges the opposing view fairly"],"model":"Buck's change is mostly growth, because it is the only way he can survive. London says the first theft \"marked Buck as fit to survive in the hostile Northland environment,\" and that his \"adaptability\" saved him from \"swift and terrible death.\" He learns to sleep in snow, eat fast and avoid foolish fights, all signs of a stronger, smarter dog. Still, London also calls it \"the decay or going to pieces of his moral nature,\" and Buck lets an innocent dog be punished for his theft. Readers who value honesty above everything would call that a loss. I think London wants us to see both, but in the brutal Northland, survival comes first."},
   {"t":"open","key":"realworld","q":"Think of a time you (or someone you know, or a character in another book) had to change to fit into a new place: a move, a new team, a new school or co-op. What did you gain, and did you lose anything? Compare it with Buck.","min":69,"rows":6,"rubric":["A specific real or fictional example","Gains and losses identified","A thoughtful comparison with Buck's change"],"model":"When my family moved from New York to Florida, I had to get used to a new homeschool co-op where everyone already had friends. I learned to be braver about talking to new people, which was a real gain. I lost some of the inside jokes and traditions I had with my old friends. Like Buck, I adapted to survive in a new place, but unlike Buck I didn't have to give up my values. I just had to add new skills."}]},
 "exit": [
  {"t":"text","q":"Buck against the freezing snow is what type of conflict?","a":[{"all":[["nature"]],"none":["not"]}],"show":"character versus nature","pts":2,"why":"An external conflict."},
  {"t":"text","q":"Who is the antagonist in Chapter III?","a":[{"all":[["spitz"]],"none":["not"]}],"show":"Spitz","pts":2,"why":"The lead dog who opposes Buck."},
  {"t":"text","q":"The root mort means ___.","a":[{"all":[["death","die"]],"none":["not"]}],"show":"death","pts":2,"why":"mortal, mortality."},
  {"t":"open","key":"exit_change","q":"Give one way Buck changed in Chapters II and III and the conflict that caused it.","min":12,"rows":2,"rubric":["An accurate change linked to a specific conflict"],"model":"Buck learned to steal food secretly because hunger on the trail (a conflict with nature) made it the only way to get enough to eat."}],
 "next": "Week 23: symbols and theme."
}

TEACHER = {
 "standards": [
  "ELA.6.R.1.1: Analyze how the interaction between characters contributes to the development of a plot in a literary text.",
  "ELA.6.V.1.2: Apply knowledge of Greek and Latin roots and affixes to determine meanings of words and phrases in grade-level content.",
  "ELA.K12.EE.1.1: Cite evidence to explain and justify reasoning."],
 "materials": ["The interactive lesson", "The Call of the Wild, Chapters II and III", "Index cards or sticky notes in 4 colors, tape or string, markers", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 21 warm-up questions."],
  [4, "Hook", "The first day on the Dyea beach; the change staircase."],
  [10, "Types of conflict", "Sort conflicts; internal versus external."],
  [13, "Adaptation or loss?", "Read the Chapter II excerpt; discuss the two descriptions of the theft; roots mort, vit, morph."],
  [10, "Characterization", "STEAL callback: tracing change through actions; the other dogs and the drivers; Curly's lesson."],
  [11, "Buck and Spitz", "Rising action; the secret growth of the primordial beast."],
  [6, "Assign", "Start the conflict cards; assign Chapters II and III reading, Think Deeper and the Exit Check."]],
 "key_questions": ["Who or what is Buck struggling against?", "How did this conflict change him?", "Is the narrator telling us or showing us?", "Is this change growth, loss or both?"],
 "misconceptions": ["Conflict means only a fight.", "The antagonist must be a villain or a person.", "A character's change is always for the better.", "London approves of everything Buck does."],
 "support": ["Read Chapters II and III aloud together or use a free audiobook.", "Provide a conflict-type chart.", "Mark key passages with sticky notes."],
 "challenge": ["Track how London uses the words civilized, primitive and primordial across the chapters.", "Compare Buck's change with a character from another book who must adapt to survive."],
 "background": "<p><b>Content note:</b> Chapter II includes Curly's violent death; Chapter III ends with Buck and Spitz's fight to the death. Both are central to the plot; preview them and decide how to read them with your child. The lesson quotes the Gutenberg text exactly. London's portrayal of François and Perrault as French-Canadian couriers reflects the real Canadian government mail service on the Yukon trail in 1897 to 1898.</p>",
 "sources": ["Jack London, The Call of the Wild (1903), Project Gutenberg.", "Library of America, Jack London: Novels and Stories (notes)."]
}

PRINT = {
 "directions": "Answer in complete sentences, citing the novel.",
 "items": [
  {"q":"Name the four types of conflict and give an example of each from Chapters II and III.","a":"vs. character (Spitz), vs. nature (snow, hunger), vs. society (the law of club and fang, the drivers' clubs), vs. self (civilized morals vs. wild instincts).","lines":4},
  {"q":"What does London mean by \"the law of club and fang\"?","a":"In the North, survival depends on force: men's clubs and dogs' teeth make the rules.","lines":2},
  {"q":"Explain how Buck's theft of food shows both adaptation and loss.","a":"It helps him survive (adaptation) but marks the decay of his moral nature (loss).","lines":3},
  {"q":"Give one example each of direct and indirect characterization of Buck.","a":"Direct: \"He was fit, that was all.\" Indirect: he digs a sleeping hole after watching Billee.","lines":2},
  {"q":"Why is the conflict between Buck and Spitz so serious?","a":"Only one can lead the team, and in the North, losing a fight can mean death.","lines":2},
  {"q":"Use the roots: what do mortal, survive and metamorphosis have to do with mort, viv and morph?","a":"mortal: will die (death); survive: stay alive (life); metamorphosis: change of form (shape).","lines":2}]
}
