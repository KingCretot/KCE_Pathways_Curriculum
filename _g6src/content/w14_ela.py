def poem(title, author, lines, note="", indent=None):
    out = []
    for i, l in enumerate(lines):
        if not l:
            out.append("&nbsp;")
        elif indent and i in indent:
            out.append("&nbsp;&nbsp;&nbsp;&nbsp;" + l)
        else:
            out.append(l)
    body = "<br>".join(out)
    return (f"<div class='card' style='border-left-color:#C9A84C'><h3 style='margin-top:0'>{title}</h3><p class='muted' style='margin-top:-6px'>{author}</p>"
            f"<p style='font-family:Georgia,serif;font-size:17px;line-height:1.7'>{body}</p>{note}</div>")

WHITMAN = poem("I Hear America Singing", "Walt Whitman (first published 1860; this text from <i>Leaves of Grass</i>, 1891–92 edition)", [
 "I hear America singing, the varied carols I hear,",
 "Those of mechanics, each one singing his as it should be blithe and strong,",
 "The carpenter singing his as he measures his plank or beam,",
 "The mason singing his as he makes ready for work, or leaves off work,",
 "The boatman singing what belongs to him in his boat, the deckhand singing on the steamboat deck,",
 "The shoemaker singing as he sits on his bench, the hatter singing as he stands,",
 "The wood-cutter's song, the ploughboy's on his way in the morning, or at noon intermission or at sundown,",
 "The delicious singing of the mother, or of the young wife at work, or of the girl sewing or washing,",
 "Each singing what belongs to him or her and to none else,",
 "The day what belongs to the day—at night the party of young fellows, robust, friendly,",
 "Singing with open mouths their strong melodious songs."],
 "<p class='muted' style='font-size:12px'>carols: joyful songs. mechanics: skilled workers who make or fix things. blithe: cheerful. mason: a worker who builds with stone or brick. hatter: a hat maker. ploughboy: Whitman's spelling of plowboy, a boy who guides a plow. robust: strong and healthy.</p>")

EPILOGUE = poem("Epilogue", "Langston Hughes (from <i>The Weary Blues</i>, 1926; often printed as \"I, Too\")", [
 "I, too, sing America.", "",
 "I am the darker brother.", "They send me to eat in the kitchen", "When company comes,", "But I laugh,", "And eat well,", "And grow strong.", "",
 "Tomorrow,", "I'll sit at the table", "When company comes.", "Nobody'll dare", "Say to me,", "\"Eat in the kitchen,\"", "Then.", "",
 "Besides,", "They'll see how beautiful I am", "And be ashamed,—", "",
 "I, too, am America."],
 "<p class='muted' style='font-size:12px'>epilogue: a closing section at the end of a book. In <i>The Weary Blues</i>, this poem ends the whole collection.</p>")

HEART = poem("The Heart of a Woman", "Georgia Douglas Johnson (text from <i>The Book of American Negro Poetry</i>, 1922; first published 1918)", [
 "The heart of a woman goes forth with the dawn,", "As a lone bird, soft winging, so restlessly on,", "Afar o'er life's turrets and vales does it roam", "In the wake of those echoes the heart calls home.", "",
 "The heart of a woman falls back with the night,", "And enters some alien cage in its plight,", "And tries to forget it has dreamed of the stars", "While it breaks, breaks, breaks on the sheltering bars."],
 "<p class='muted' style='font-size:12px'>o'er: over. turrets: towers. vales: valleys. in the wake of: following. alien: strange, not its own. plight: a hard situation.</p>")

HOUSE = poem("The House on the Hill", "Edwin Arlington Robinson (first published 1894; text from <i>The Children of the Night</i>, 1897)", [
 "They are all gone away,", "The House is shut and still,", "There is nothing more to say.", "",
 "Through broken walls and gray", "The winds blow bleak and shrill:", "They are all gone away.", "",
 "Nor is there one to-day", "To speak them good or ill:", "There is nothing more to say.", "",
 "Why is it then we stray", "Around that sunken sill?", "They are all gone away,", "",
 "And our poor fancy-play", "For them is wasted skill:", "There is nothing more to say.", "",
 "There is ruin and decay", "In the House on the Hill:", "They are all gone away,", "There is nothing more to say."],
 "<p class='muted' style='font-size:12px'>bleak: cold and gloomy. shrill: high and piercing. to-day: the old spelling of today. speak them good or ill: say good or bad things about them. stray: wander. sill: the bottom of a door or window frame. fancy-play: imagining.</p>",
 indent=[1, 5, 9, 13, 17, 21])

FORM = ('<svg viewBox="0 0 660 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Diagram of the villanelle form: five tercets and a quatrain with two refrains">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The villanelle: 19 lines, 2 rhymes, 2 refrains</text>'
  + ''.join(f'<rect x="{18+i*107}" y="40" width="98" height="{24*n+12}" rx="8" fill="#f6f1e3" stroke="#C9A84C"/>'
            + ''.join(f'<rect x="{26+i*107}" y="{48+j*24}" width="82" height="20" rx="4" fill="{c}"/><text x="{67+i*107}" y="{62+j*24}" text-anchor="middle" fill="{"#fff" if c != "#e6e6e6" else "#0A1F3D"}" font-weight="bold" font-size="11">{t}</text>'
                      for j, (t, c) in enumerate(lines))
            + f'<text x="{67+i*107}" y="{40+24*n+30}" text-anchor="middle" font-size="11" fill="#5b6676">{lab}</text>'
            for i, (n, lines, lab) in enumerate([
              (3, [("A1 refrain", "#0047BA"), ("b", "#e6e6e6"), ("A2 refrain", "#DB2F30")], "tercet 1"),
              (3, [("a", "#e6e6e6"), ("b", "#e6e6e6"), ("A1 refrain", "#0047BA")], "tercet 2"),
              (3, [("a", "#e6e6e6"), ("b", "#e6e6e6"), ("A2 refrain", "#DB2F30")], "tercet 3"),
              (3, [("a", "#e6e6e6"), ("b", "#e6e6e6"), ("A1 refrain", "#0047BA")], "tercet 4"),
              (3, [("a", "#e6e6e6"), ("b", "#e6e6e6"), ("A2 refrain", "#DB2F30")], "tercet 5"),
              (4, [("a", "#e6e6e6"), ("b", "#e6e6e6"), ("A1 refrain", "#0047BA"), ("A2 refrain", "#DB2F30")], "quatrain")])) +
  '<text x="330" y="196" text-anchor="middle" font-size="12">Blue refrain (A1) and red refrain (A2) alternate, then come together at the end.</text>'
  '<text x="330" y="216" text-anchor="middle" font-size="11" fill="#5b6676">Every a line rhymes with the refrains; every b line rhymes with the other b lines.</text></svg>')

LESSON = {
 "unit": "Unit 3: The Power of Poetry",
 "title": "Poems in Conversation Across Time",
 "subtitle": "Poets answer one another, sometimes across decades. A poem can echo, argue with or complete an earlier poem, and an old form like the villanelle can make a new poem sound like a voice that cannot stop repeating itself.",
 "objectives": [
  "Explain how poems can be \"in conversation\" through response, echo and allusion.",
  "Compare how Walt Whitman and Langston Hughes address America and work, and explain how Hughes answers Whitman.",
  "Compare how Paul Laurence Dunbar and Georgia Douglas Johnson use the image of a caged bird.",
  "Identify the parts of a villanelle and explain how its refrains shape the meaning of Robinson's \"The House on the Hill.\"",
  "Use the roots vers, log, dia and lud, and write a poem in conversation with another poem."],
 "vocab": [
  ["allusion", "A brief reference to a well-known person, place, event or work, which the reader is expected to recognize."],
  ["response poem", "A poem written to answer, argue with or build on an earlier poem."],
  ["echo", "Repeating or closely imitating words from an earlier text."],
  ["villanelle", "A 19-line poem with five tercets and a final quatrain, two rhymes, and two refrains that repeat in a fixed pattern."],
  ["tercet", "A stanza of three lines."],
  ["extended metaphor", "A metaphor that continues through several lines or a whole poem."]],
 "reconnect": {
  "title": "Week 13: Harlem Renaissance poets",
  "intro": "Langston Hughes returns this week, in conversation with a poet who wrote 66 years before him.",
  "items": [
   {"t":"text","q":"In \"The Negro Speaks of Rivers,\" the \"I\" speaks for a whole people across history. What kind of voice is that?","a":[{"all":[["collective"]],"none":["not"]}],"show":"a collective voice","pts":2,"why":"One speaker who lived through all of history stands for a people."},
   {"t":"text","q":"What is the name for the turn in a sonnet, like line 11 of McKay's \"The Tired Worker\"?","a":[{"all":[["volta","turn"]],"none":["not"]}],"show":"the volta","pts":2,"why":"\"But what steals out...\" turns the poem."},
   {"t":"blanks","q":"Recall last week's roots.","sent":"The root migr means ___. The root nat means ___.","blanks":[[{"all":[["move"]],"none":["not"]}],[{"all":[["born","birth"]],"none":["not"]}]],"show":"move; born","pts":2,"why":"migrate; native, nation, renaissance."},
   {"t":"open","key":"rc_epigraph","q":"Why did Jessie Fauset begin \"Oriflamme\" with an epigraph from Sojourner Truth? Explain in one or two sentences.","min":12,"rows":2,"rubric":["The epigraph introduces the mother and the stars","The poem builds on and answers that memory"],"model":"Truth's memory of her mother looking at the stars gave Fauset the image her poem builds on, so the poem answers and continues Truth's words."}]},
 "hook": {
  "title": "A Poem That Answers a Poem",
  "html": "<p>In 1860, Walt Whitman published a poem listing the workers of America: carpenters, masons, boatmen, shoemakers, mothers. Each one, he wrote, was \"singing\" their own song, and together they made America's music.</p><p>Sixty-six years later, Langston Hughes ended his first book with a poem that begins, \"I, too, sing America.\" That little word <i>too</i> is a reply. Hughes is talking back to Whitman, and to every reader who imagined an America where some singers were left out.</p><div class='callout'><b>Big question:</b> How do poets use earlier poems and forms to say something new?</div>"},
 "learn": [
  {"title": "How Poems Talk to Each Other",
   "html": "<p>Poems can be <b>in conversation</b> in several ways:</p><ul><li><b>Response:</b> a poem answers an earlier poem directly, agreeing, disagreeing or adding a missing voice.</li><li><b>Echo:</b> a poem repeats or imitates words from an earlier one, so readers hear both at once.</li><li><b>Allusion:</b> a brief reference to a famous person, event or work that readers are expected to recognize. Hughes's \"Abe Lincoln\" in last week's poem is an allusion.</li><li><b>Form:</b> a poet chooses an old form, like the sonnet or villanelle, and joins a centuries-long conversation about how that form can be used.</li></ul><p><b>Roots:</b> <i>vers</i> means turn (verse, reverse, conversation); a line of poetry is a verse because it turns back at the end. <i>Log</i> means word or speech, and <i>dia</i> means across or through: a <i>dialogue</i> is speech across two people. <i>Lud</i> means play: an <i>allusion</i> playfully points to something else.</p>",
   "checks": [
    {"t":"text","q":"What is the term for a brief reference to a well-known person, event or work that the reader is expected to recognize?","a":[{"all":[["allusion"]],"none":["not","illusion"]}],"show":"allusion","pts":2,"why":"From lud, play: an allusion plays on something the reader already knows."},
    {"t":"blanks","q":"Use the roots.","sent":"Speech across two or more people (dia + log) is a ___. To turn something back the other way (re + vers) is to ___ it.","blanks":[[{"all":[["dialogue","dialog"]],"none":["not"]}],[{"all":[["reverse"]],"none":["not"]}]],"show":"dialogue; reverse","pts":2,"why":"dia (across) + log (word); re (back) + vers (turn)."},
    {"t":"open","key":"whyanswer","q":"Why might a poet choose to answer an earlier poem instead of writing a completely new one? Give one reason.","min":20,"rows":2,"rubric":["A reasonable purpose: to add a missing voice, correct or challenge an idea, honor an earlier poet, or make readers compare two points of view"],"model":"A poet might answer an earlier poem to add a voice that was left out. Readers who know the first poem will compare the two and notice what was missing."}]},
  {"title": "Whitman and Hughes: Who Sings America?",
   "html": WHITMAN + EPILOGUE + "<p>Whitman's poem is a celebration. Every worker has a song that \"belongs to him or her and to none else,\" and together they are America. But in 1860, millions of Black Americans were enslaved, and Whitman's list of free, singing workers does not mention them.</p><p>Hughes's \"Epilogue\" uses Whitman's own word, <i>sing</i>, and adds <i>too</i>. His speaker is \"the darker brother,\" a member of the family who is sent to eat in the kitchen \"when company comes,\" an image of segregation. He does not ask permission or argue angrily. He laughs, eats well, grows strong and predicts that \"Tomorrow\" he will sit at the table. The poem's first line, \"I, too, sing America,\" changes in the last line to \"I, too, <b>am</b> America.\"</p>",
   "checks": [
    {"t":"text","q":"In the last line of Hughes's poem, one word replaces sing from the first line. Type that word.","a":[{"all":[["am"]],"none":["not","sing"]}],"show":"am","pts":2,"why":"\"I, too, sing America\" becomes \"I, too, am America.\""},
    {"t":"open","key":"kitchen","q":"What does being sent \"to eat in the kitchen / When company comes\" stand for? Explain the image.","min":25,"rows":3,"rubric":["Stands for segregation or exclusion: being treated as less than a full member of the family or nation","Notes he is still part of the household (\"darker brother\") but kept out of sight"],"model":"It stands for segregation. The speaker is part of the family, a \"darker brother,\" but he is hidden away when guests come, the way Black Americans were kept separate and treated as less than full citizens."},
    {"t":"open","key":"singam","q":"Why is changing \"sing\" to \"am\" in the last line so powerful? Connect it to Whitman's poem.","min":30,"rows":3,"rubric":["Moves from taking part in America's song to claiming to be America itself","Answers Whitman: not just one more singer added to the list, but part of America's identity"],"model":"In Whitman's poem, Americans sing; in Hughes's first line, he joins that singing. But in the last line he claims more: he doesn't just sing America, he is America. He is not asking to be added to Whitman's list; he is saying America cannot be described without him."},
    {"t":"blanks","q":"Compare the two poems.","sent":"Whitman's poem names many workers, such as the carpenter and the ___. Hughes's speaker calls himself the darker ___.","blanks":[[{"all":[["mason","boatman","deckhand","shoemaker","hatter","wood-cutter","woodcutter","ploughboy","plowboy","mechanic","mother"]],"none":["not","carpenter"]}],[{"all":[["brother"]],"none":["not"]}]],"show":"(any worker such as mason, shoemaker, hatter); brother","pts":2,"why":"Whitman lists many workers; Hughes is a \"brother\" in the American family."}]},
  {"title": "Dunbar and Johnson: The Caged Bird",
   "html": "<p>In Week 11 you read Paul Laurence Dunbar's \"Sympathy\" (1899), where a caged bird beats its wings against the bars, and the speaker says, \"I know why the caged bird sings!\" Seventy years later, Maya Angelou took that line as the title of her famous memoir. Dunbar's image became part of a long conversation.</p>" + HEART + "<p><b>Georgia Douglas Johnson</b> (1880 to 1966) hosted Harlem Renaissance writers at her home in Washington, D.C. In \"The Heart of a Woman,\" she builds an <b>extended metaphor</b>: a woman's heart is a bird. By day it flies far and free \"with the dawn\"; by night it \"falls back\" into a cage. Like Dunbar's bird, it hurts itself on the bars, but Johnson calls them \"sheltering bars\": a cage that also feels like protection, a life with safety but without freedom.</p>",
   "checks": [
    {"t":"text","q":"In Johnson's first stanza, what does the heart of a woman go forth with?","a":[{"all":[["dawn","morning"]],"none":["not","night"]}],"show":"the dawn","pts":2,"why":"\"The heart of a woman goes forth with the dawn\"; stanza 2 begins with night."},
    {"t":"open","key":"sheltering","q":"Johnson calls the cage's bars \"sheltering.\" Why is that word surprising, and what does it suggest about the woman's life?","min":30,"rows":3,"rubric":["Surprising: bars usually trap or imprison, but sheltering means protecting","Suggests her limits are also her safety (home, expectations), so she is trapped and protected at once; a mixed or painful feeling"],"model":"Bars usually trap you, so calling them \"sheltering\" is surprising. It suggests her limits, like home and what society expects of women, also keep her safe. She is protected and trapped at the same time, which makes her situation more painful and complicated."},
    {"t":"open","key":"dunbarjohnson","q":"Both Dunbar and Johnson use a bird in a cage. Name one similarity and one difference in how they use it.","min":30,"rows":3,"rubric":["Similarity: the bird stands for a person whose freedom is limited; the bird hurts itself on the bars","Difference: Dunbar's bird is caged all the time and sings or prays; Johnson's flies free by day and returns at night, and its bars are \"sheltering\"; Johnson focuses on women"],"model":"Both poets use the caged bird for a person whose freedom is limited, and both birds hurt themselves on the bars. But Dunbar's bird is caged all the time and sings a prayer, while Johnson's flies free by day and only returns to the cage at night, and Johnson focuses on a woman's life."},
    {"t":"text","q":"In Johnson's last line, which word is repeated three times in a row?","a":[{"all":[["break","breaks"]],"none":["not"]}],"show":"breaks","pts":2,"why":"\"While it breaks, breaks, breaks\": the repetition sounds like the heart hitting the bars again and again."}]},
  {"title": "The Villanelle: A Form That Cannot Let Go",
   "visual": FORM,
   "html": HOUSE + "<p>The <b>villanelle</b> came to English from French poetry in the 1800s. It has strict rules: 19 lines in five <b>tercets</b> and a final quatrain, only two rhyme sounds, and two <b>refrains</b> that keep returning. The first line (A1) and the third line (A2) take turns ending the tercets, then both close the poem.</p><p>Edwin Arlington Robinson, who grew up in Gardiner, Maine, published \"The House on the Hill\" in 1894. His refrains, \"They are all gone away\" and \"There is nothing more to say,\" return again and again, the way a person grieving keeps coming back to the same thought. The form itself acts out the meaning: the speaker cannot stop circling the empty house.</p>",
   "checks": [
    {"t":"num","q":"How many lines are in a villanelle? Count Robinson's poem to check.","a":19,"unit":"lines","pts":2,"why":"Five tercets (15 lines) + one quatrain (4 lines) = 19."},
    {"t":"text","q":"Type the rhyme scheme of the first tercet of \"The House on the Hill.\" Type the three letters with no spaces.","a":["aba"],"show":"aba","pts":2,"why":"away (a), still (b), say (a)."},
    {"t":"open","key":"refrains","q":"How do the two refrains, \"They are all gone away\" and \"There is nothing more to say,\" create the poem's feeling? Use the word refrain in your answer.","min":30,"rows":3,"rubric":["The refrains repeat throughout, creating a feeling of grief, emptiness or loss that won't go away","The repetition imitates someone who cannot stop thinking about the loss (or the circling of the house); saying \"nothing more to say\" again and again is ironic"],"model":"Each refrain keeps returning, like a sad thought someone can't escape. Repeating \"They are all gone away\" makes the emptiness feel permanent. And repeating \"There is nothing more to say\" is ironic: the speaker keeps saying it because he cannot stop thinking about the people who left."},
    {"t":"text","q":"Robinson's poem uses only two rhyme sounds. One is the sound in away, say and gray. Type a word from the poem that has the other rhyme sound.","a":[{"all":[["still","shrill","ill","sill","skill","hill"]],"none":["not"]}],"show":"still, shrill, ill, sill, skill or Hill","pts":2,"why":"The b rhymes: still, shrill, ill, sill, skill, Hill."}]}],
 "handson": {
  "title": "Build a Villanelle with Cards",
  "intro": "Assemble Robinson's villanelle by hand to feel how the refrains work, then build a short poem of your own that answers another poem.",
  "materials": ["About 30 index cards or paper strips", "Two colored markers (one blue, one red) and a pencil", "A table or floor space", "Paper", "Tape"],
  "steps": [
   "Write each line of \"The House on the Hill\" on its own card, but only once: write the first refrain on a blue card and the second refrain on a red card. Write the other lines in pencil.",
   "Shuffle the pencil cards. Using the villanelle diagram, lay the poem out on the floor or table, making extra copies of the blue and red refrain cards whenever the pattern calls for them. Count how many blue and red cards you needed.",
   "Read the finished layout aloud, walking along it. Stomp once on every refrain.",
   "Now write your own response poem of 8 to 14 lines (any form) that answers one poem from Weeks 11 to 14. Echo at least one line or image from the earlier poem. Challenge: write it as a villanelle using two refrain cards of your own.",
   "Tape your poem's cards in order onto a sheet of paper."],
  "record": [
   {"t":"open","key":"cardcount","q":"How many times did each refrain appear in Robinson's poem? What did you notice when you stomped on every refrain?","min":25,"rows":3,"rubric":["Each refrain appears 4 times (blue: lines 1, 6, 12, 18; red: lines 3, 9, 15, 19)","A thoughtful observation about the rhythm of repetition and the feeling it creates"],"model":"Each refrain appeared 4 times. Stomping on them made me notice that they come every third line, like footsteps walking around the house over and over, which matches the feeling of someone who cannot leave the past behind."},
   {"t":"open","key":"myresponse","q":"Write your response poem. Then, in one or two sentences, name the poem you answered and the line or image you echoed.","min":60,"rows":10,"rubric":["8 to 14 lines (or a villanelle)","Clearly answers a poem from Weeks 11 to 14","Echoes at least one line or image","Explanation names the poem and the echo"],"model":"I, Too, Build America\nI hear the hammers ringing on my street,\nthe roofer's song, my uncle on the beam,\nmy mother's footsteps, steady, strong and fleet.\nThey never wrote our names in Whitman's dream,\nbut here we are, the ones who pour the floor,\nwho frame the walls and paint the doors of cream.\nTomorrow, we will walk in through the door.\n\nI answered Whitman's \"I Hear America Singing\" and Hughes's \"Epilogue.\" I echoed Whitman's list of workers and Hughes's \"Tomorrow\" and \"I, too.\""}]},
 "think": {
  "intro": "Use evidence from the poems. Your teacher scores these.",
  "items": [
   {"t":"open","key":"rejectclaim","q":"Is Hughes rejecting Whitman's America, or claiming his place in it? Take a position and support it with at least two quotations from \"Epilogue\" and one from \"I Hear America Singing.\"","min":100,"rows":8,"rubric":["Clear position (claiming his place is the strongest reading, but a well-supported reading of rejection is acceptable)","At least two accurate quotations from Hughes","At least one accurate quotation from Whitman","Explains how the quotations support the position"],"model":"Hughes is claiming his place in Whitman's America, not rejecting it. He uses Whitman's own verb when he writes \"I, too, sing America,\" which shows he wants to join the chorus Whitman described, where everyone sings \"what belongs to him or her and to none else.\" He criticizes the way he is treated, sent \"to eat in the kitchen / When company comes,\" but he does not leave the house; he predicts \"Tomorrow, / I'll sit at the table.\" His last line, \"I, too, am America,\" shows he believes in America's promise and insists it include him."},
   {"t":"open","key":"formmeaning","q":"Why do you think Robinson chose the villanelle, with its repeating refrains, for a poem about an empty house? Would the poem be as powerful as a short paragraph? Explain.","min":80,"rows":6,"rubric":["Connects the repeating refrains to grief, memory or the speaker's inability to let go","Explains that a paragraph would lose the repetition, rhythm and circling effect","Uses at least one quotation"],"model":"Robinson chose the villanelle because its refrains circle back, just as the speaker keeps returning to the house. \"They are all gone away\" comes back four times, so the reader feels the loss growing heavier. As a paragraph, the same words would say it once and move on, and we would lose the feeling of someone who cannot stop remembering."}]},
 "exit": [
  {"t":"num","q":"How many lines does a villanelle have?","a":19,"unit":"lines","pts":2,"why":"Five tercets and a quatrain."},
  {"t":"text","q":"In a villanelle, what are the two lines that keep repeating called?","a":[{"all":[["refrain"]],"none":["not"]}],"show":"refrains","pts":2,"why":"A1 and A2 repeat in a fixed pattern."},
  {"t":"text","q":"Type the root that means turn, found in verse and conversation.","a":[{"all":[["vers","vert"]],"none":["not"]}],"show":"vers","pts":2,"why":"vers = turn."},
  {"t":"open","key":"exit_answer","q":"Give one way Hughes's \"Epilogue\" answers Whitman's \"I Hear America Singing.\"","min":12,"rows":2,"rubric":["An accurate connection (adds the left-out voice of Black Americans; reuses \"sing America\"; moves from singing to being America)"],"model":"Whitman's list of singing Americans left out Black Americans, so Hughes adds his voice with \"I, too, sing America.\""}],
 "next": "Week 15: mid-year review and the Poetry Analysis Project."
}

TEACHER = {
 "standards": [
  "ELA.6.R.1.4: Describe the impact of various poetic forms on meaning and style.",
  "ELA.6.R.3.3: Compare and contrast how authors from different time periods address the same or related topics.",
  "ELA.6.R.1.2: Analyze the development of stated or implied theme(s) throughout a literary text.",
  "ELA.6.V.1.2: Apply knowledge of Greek and Latin roots and affixes to determine meanings of words and phrases in grade-level content.",
  "ELA.K12.EE.1.1: Cite evidence to explain and justify reasoning."],
 "materials": ["The interactive lesson", "About 30 index cards, blue and red markers, a pencil, tape and paper", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 13 Reconnect questions."],
  [4, "Hook", "Read Whitman's first line and Hughes's first line side by side."],
  [7, "Poems in conversation", "Define response, echo, allusion and form. Teach the four roots."],
  [15, "Whitman and Hughes", "Read both poems aloud. Discuss what Whitman leaves out and how Hughes answers, ending on \"sing\" to \"am.\""],
  [11, "Dunbar and Johnson", "Recall \"Sympathy.\" Read Johnson's poem and trace the extended metaphor; discuss \"sheltering bars.\""],
  [11, "The villanelle", "Read Robinson's poem aloud twice. Mark the refrains with two colors and count lines."],
  [6, "Assign", "Start the card layout together; assign the response poem, Think Deeper and the Exit Check."]],
 "key_questions": ["What is the later poem answering?", "What does the earlier poem leave out?", "How does the form shape the feeling?", "Why repeat a line?"],
 "misconceptions": ["An allusion is the same as an illusion.", "A response poem must disagree with the original.", "Repetition in a poem is just filler.", "Every refrain repeats in exactly the same place in every form (the villanelle's pattern is specific)."],
 "support": ["Give a two-column chart: first poem / answering poem.", "Color-code the villanelle refrains before reading.", "Offer sentence frames: \"Hughes answers Whitman by ___.\""],
 "challenge": ["Read Whitman's longer \"Song of Myself\" section 1 (public domain) and look for more ideas Hughes might be answering.", "Write a full 19-line villanelle."],
 "background": "<p>Whitman's \"I Hear America Singing\" first appeared untitled in the 1860 Leaves of Grass and took its final title and form in later editions; the text here is the 1891–92 edition (Project Gutenberg 1322), including Whitman's spelling \"ploughboy.\" Hughes's poem appears as \"Epilogue\" at the end of The Weary Blues (1926; Gutenberg 74745); it was first published in 1925 and is widely anthologized as \"I, Too.\" Georgia Douglas Johnson (1880 to 1966) published \"The Heart of a Woman\" as the title poem of her 1918 collection; text from The Book of American Negro Poetry (1922; Gutenberg 11986). Her Washington, D.C., home was a gathering place for writers (the \"S Street Salon\"). Dunbar's \"Sympathy\" (1899) was taught in Week 11; Maya Angelou's memoir I Know Why the Caged Bird Sings appeared in 1969 (only the title is mentioned). Robinson's \"The House on the Hill\" appeared in the Globe in 1894 and in The Children of the Night (1897; Gutenberg 313). ELA.6.R.1.4's clarification names the sonnet and the villanelle.</p>",
 "sources": ["Whitman, W. (1891–92), Leaves of Grass (Project Gutenberg 1322).", "Hughes, L. (1926), The Weary Blues, Knopf (Project Gutenberg 74745).", "Johnson, J. W., ed. (1922), The Book of American Negro Poetry (Project Gutenberg 11986).", "Robinson, E. A. (1897), The Children of the Night (Project Gutenberg 313).", "Academy of American Poets, Villanelle (poetic form)."]
}

PRINT = {
 "directions": "Write in complete sentences and use evidence from the poems.",
 "items": [
  {"q":"Define allusion and response poem.","a":"Allusion: a brief reference to a well-known person, event or work. Response poem: a poem that answers an earlier poem.","lines":2},
  {"q":"Explain how Hughes's \"Epilogue\" answers Whitman's \"I Hear America Singing.\"","a":"Hughes adds the voice of Black Americans left out of Whitman's list, reuses \"sing America,\" and ends by claiming \"I, too, am America.\"","lines":3},
  {"q":"What does the image of eating in the kitchen \"when company comes\" represent?","a":"Segregation: being treated as less than a full member of the family and nation.","lines":2},
  {"q":"Explain Johnson's extended metaphor in \"The Heart of a Woman.\"","a":"The heart is a bird that flies free by day and returns at night to a cage with \"sheltering bars.\"","lines":2},
  {"q":"Label the villanelle pattern: which lines are refrains in Robinson's poem?","a":"\"They are all gone away\" (lines 1, 6, 12, 18) and \"There is nothing more to say\" (lines 3, 9, 15, 19).","lines":2},
  {"q":"Use the roots: what do dialogue and monologue share, and what does dia add?","a":"Both contain log (word, speech); dia means across, so a dialogue is speech across two or more people.","lines":2}]
}
