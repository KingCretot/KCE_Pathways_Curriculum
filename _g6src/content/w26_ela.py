LADDER = ('<svg viewBox="0 0 660 260" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="A question ladder from a broad topic down to a focused, researchable question with sub-questions">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The question ladder: from topic to researchable question</text>'
  + ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="8" fill="{c}"/><text x="{x+w/2}" y="{y+22}" text-anchor="middle" fill="#fff" font-weight="bold">{t}</text><text x="{x+w+10}" y="{y+22}" fill="#5b6676" font-size="11">{n}</text>'
            for x, y, w, t, c, n in [(60, 36, 220, "Topic: springs", "#5b6676", "too broad: a whole library"),
                                     (90, 82, 280, "What is happening to Florida's springs?", "#8a6d1f", "still broad; mostly facts"),
                                     (120, 128, 340, "Why is Silver Springs flowing less than in 1950?", "#0047BA", "focused, but can I find sources?"),
                                     (150, 174, 380, "How have pumping and rainfall changed Silver Springs' flow, and what could restore it?", "#2c6e22", "")]) +
  '<text x="150" y="232" fill="#2c6e22" font-weight="bold">Researchable: focused, answerable with several sources, asks how or why, and matters to someone.</text>'
  '<text x="150" y="250" fill="#5b6676" font-size="11">Sub-questions: How much has flow changed? How much water is pumped nearby? What do scientists recommend?</text></svg>')

LESSON = {
 "unit": "Unit 6: Research and Presentation",
 "title": "Asking Research Questions",
 "subtitle": "Unit 6 ends with your own research presentation. Great research starts with a great question, not a topic. This week you climb the question ladder from a broad topic to a focused question, break it into sub-questions, plan where to look, and practice changing course when your sources lead somewhere new.",
 "objectives": [
  "Distinguish a topic from a research question, and closed questions from open ones.",
  "Narrow a broad topic into a focused, researchable how or why question.",
  "Break a research question into sub-questions and plan which kinds of sources could answer each.",
  "Refocus a question when early research shows it is too broad, too narrow or unanswerable.",
  "Choose and plan the question for your Unit 6 research presentation."],
 "vocab": [
  ["inquiry", "An investigation driven by a question."],
  ["open question", "A question with many possible answers that needs explanation, often beginning with how or why."],
  ["closed question", "A question with one short factual answer, such as yes or no or a single number."],
  ["sub-question", "A smaller question that helps answer the main research question."],
  ["refocus", "To change a research question based on what you learn."],
  ["scope", "How much a question covers; whether it is broad or narrow."]],
 "reconnect": {
  "title": "Week 25: Literary analysis",
  "intro": "Last week you built an argument about a novel. Research asks you to build answers from many sources.",
  "items": [
   {"t":"text","q":"In an analysis paragraph, what do we call your explanation of how evidence supports a claim?","a":[{"all":[["commentary"]],"none":["not"]}],"show":"commentary","pts":2,"why":"Claim, evidence, commentary."},
   {"t":"text","q":"What do we call a quotation or specific detail from a text that supports a claim?","a":[{"all":[["evidence"]],"none":["not"]}],"show":"textual evidence","pts":2,"why":"Research uses evidence from many sources."},
   {"t":"open","key":"rc_novelq","q":"Think of one question you still have after reading The Call of the Wild that the novel itself can't answer (about sled dogs, the Klondike, Jack London or anything else).","min":10,"rows":2,"rubric":["A real question the novel doesn't answer"],"model":"How did real sled dogs survive temperatures of 60 below zero, and how were they treated during the gold rush?"},
   {"t":"open","key":"rc_week9","q":"In Week 9 you wrote a research question and took note cards. What made your Week 9 question work, or what would you change about it now?","min":15,"rows":2,"rubric":["Recalls the Week 9 question or process","Evaluates it honestly"],"model":"My Week 9 question about manatees was really a topic: \"What are manatees?\" Now I would ask why manatees gather at Blue Spring in winter, which needs explanation and evidence."}]},
 "hook": {
  "title": "Not a Topic, a Question",
  "visual": LADDER,
  "html": "<p>Ask a librarian for books on \"springs\" and you'll get hundreds. Ask \"Why is Silver Springs flowing less than it did in 1950?\" and you know exactly what to look for, what to skip and when you're done.</p><p>Researchers don't start with topics. They start with questions they truly want answered. In Week 9 you wrote a first research question; this unit you'll ask a sharper one, follow it through real sources and present your answer.</p><div class='callout'><b>Big question:</b> What makes a question worth researching, and how do you find out what you don't know?</div>"},
 "learn": [
  {"title": "Open and Closed Questions",
   "html": "<p>A <b>closed question</b> has one short answer you can look up: \"When did Silver Springs become a state park?\" An <b>open question</b> needs explanation and evidence from several sources: \"How has tourism changed Silver Springs?\"</p><p>Closed questions are useful as <b>sub-questions</b>, but your main research question should be open. Good starters: <i>How</i>, <i>Why</i>, <i>To what extent</i>, <i>What are the effects of</i>, <i>What would happen if</i>.</p>",
   "checks": [
    {"t":"open","key":"opencloseconvert","q":"Turn this closed question into an open one: \"How many manatees visited Blue Spring last winter?\"","min":10,"rows":2,"rubric":["A question that needs explanation or evidence","Keeps the same subject"],"model":"Why have so many more manatees been visiting Blue Spring in winter over the past 30 years?"},
    {"t":"open","key":"closeduse","q":"If closed questions aren't good main research questions, how can they still help a researcher? Give an example.","min":20,"rows":2,"rubric":["Explains closed questions as sub-questions or fact-finding","A fitting example"],"model":"Closed questions gather the facts you need to answer the bigger question. To explain why manatee numbers grew at Blue Spring, I'd first need to know how many came in 1990 and how many come now."}]},
  {"title": "Narrowing a Topic: The Question Ladder",
   "html": "<p>Climb down the ladder from a topic to a researchable question by adding <b>who</b>, <b>where</b>, <b>when</b> and <b>how or why</b>:</p><ul><li>Topic: hurricanes (too broad).</li><li>Narrower: How do hurricanes affect Florida? (still huge)</li><li>Focused: How did Hurricane Ian change Fort Myers Beach, and how has it rebuilt?</li></ul><p>A good question's <b>scope</b> is just right: broad enough to find several sources, narrow enough to answer in a short presentation. Test it: Can I find at least three reliable sources? Can I answer it in 3 to 5 minutes? Do I genuinely want to know?</p>",
   "checks": [
    {"t":"order","q":"Order these from broadest to most focused.","items":["space","the Moon","returning to the Moon","Why is NASA's Artemis program sending astronauts back to the Moon?"],"pts":2,"why":"Each step adds focus."},
    {"t":"open","key":"narrowit","q":"Narrow the topic \"African empires\" into a focused, researchable question using what you learned in Unit 5.","min":12,"rows":2,"rubric":["An open how or why question","Focused on a specific place, time or group","Researchable with several sources"],"model":"How did the trade in gold and salt make the Mali Empire rich under Mansa Musa?"},
    {"t":"open","key":"tooomuch","q":"Explain what is wrong with each question and fix one: (a) \"Why is history important?\" (b) \"What color was Mansa Musa's favorite robe?\"","min":30,"rows":3,"rubric":["Explains that (a) is too broad","Explains that (b) is too narrow or unanswerable","A fixed, researchable version of one"],"model":"(a) is so broad that no presentation could answer it. (b) is too narrow and probably impossible to answer from any source. A better version: How did Mansa Musa's hajj change the way Europe and North Africa saw Mali?"}]},
  {"title": "Sub-Questions and a Research Plan",
   "html": "<p>Break your main question into 3 to 5 <b>sub-questions</b>, then decide what kind of source could answer each:</p><ul><li>Encyclopedias and reference books for background facts.</li><li>Government and university websites (.gov, .edu) for data and research.</li><li>Museums, archives and primary sources for history.</li><li>Experts and interviews for local or current questions.</li><li>News articles for recent events (check the date and the outlet).</li></ul><p>Next week you'll learn how to judge whether a source is reliable. For now, plan where you'll look.</p>",
   "checks": [
    {"t":"open","key":"subqs","q":"Main question: \"Why are Florida's coral reefs losing coral, and what is being done to save them?\" Write three sub-questions and name a kind of source for each.","min":35,"rows":4,"rubric":["Three sub-questions that each help answer the main question","A sensible source type for each"],"model":"1. How much coral has Florida's reef lost since 1980? (NOAA or university data) 2. What causes coral bleaching and disease? (science websites, Week 24 notes) 3. What are groups like the Coral Restoration Foundation doing? (the organization's website and news articles)"}]},
  {"title": "Refocusing: When Research Changes Your Question",
   "html": "<p>Real researchers change their questions. Florida's B.E.S.T. standard for research even says to <b>refocus</b> the inquiry when appropriate. Three common reasons:</p><ul><li><b>Too broad:</b> you find thousands of sources and can't cover them. Narrow by place, time or group.</li><li><b>Too narrow:</b> you find almost nothing. Widen it a step on the ladder.</li><li><b>A better question appears:</b> your sources reveal something more interesting. Follow it, and note the change.</li></ul><p>Keep a short <b>research log</b>: each time you change your question, write the old version, the new version and why.</p>",
   "checks": [
    {"t":"open","key":"refocuscase","q":"Maya planned to research \"Why do Burmese pythons in the Everglades prefer eating raccoons?\" She found only one article about raccoons, but dozens about how pythons are hunted and tracked. How should she refocus, and what should she write in her research log?","min":30,"rows":3,"rubric":["A sensible refocused question","A log entry with the old question, new question and reason"],"model":"She could widen it to \"How are scientists and hunters trying to control Burmese pythons in the Everglades?\" Her log: Old question: why pythons prefer raccoons. New question: how pythons are being controlled. Reason: almost no sources on the old question, many reliable sources on the new one."}]}],
 "handson": {
  "title": "Question Storm and Research Plan",
  "intro": "Brainstorm dozens of questions, sort them, and choose the question you'll research for your Unit 6 presentation.",
  "materials": ["A timer", "Sticky notes or slips of paper (about 30)", "Two markers in different colors", "A large sheet of paper or a wall", "A family member", "Paper and pencil"],
  "steps": [
   "Choose three topics you genuinely care about (from this year's lessons or your own interests, such as your community, an animal, a sport, an invention or a historical event).",
   "Question storm: set a timer for 5 minutes per topic and write as many questions as you can, one per sticky note. Don't judge them yet.",
   "Sort the notes into two columns on the wall: closed and open. Turn at least three closed questions into open ones.",
   "Choose your best open question and climb the question ladder on paper, rewriting it until it passes all three tests (three sources, 3 to 5 minutes, you want to know). Have your family member ask you, \"Why does this question matter?\"",
   "Write 3 to 5 sub-questions and the kind of source you'll use for each. Start a research log with today's date and your question.",
   "Peel sticky notes off walls gently so paint isn't damaged."],
  "record": [
   {"t":"open","key":"stormrec","q":"How many questions did you write in each storm? Copy two closed questions you turned into open ones, and explain which topic produced your best question and why.","min":40,"rows":4,"rubric":["Reports the question counts","Two closed-to-open conversions","Explains the choice of topic"],"model":"I wrote 14, 9 and 17 questions. I turned \"When was the Hubble telescope launched?\" into \"How has the Hubble telescope changed what we know about the universe?\" and \"Is Lake Okeechobee polluted?\" into \"Why do algae blooms keep spreading from Lake Okeechobee, and who is affected?\" Space gave the most questions, but Lake Okeechobee won because it affects people I know."},
   {"t":"open","key":"planrec","q":"Write your final research question, your sub-questions with a source type for each, and your first research log entry.","min":45,"rows":6,"rubric":["A focused, open research question","Three to five sub-questions with source types","A dated log entry"],"model":"Question: Why do algae blooms keep spreading from Lake Okeechobee, and what could stop them? Sub-questions: 1. What causes the blooms? (South Florida Water Management District, university sites) 2. How do the blooms reach the coasts? (news articles, maps) 3. How do they affect people and wildlife? (Florida Department of Health) 4. What solutions are being tried? (Everglades restoration project site). Log, Nov 16: chose my question because my cousin in Stuart can't swim at her beach in summer."}]},
 "think": {
  "intro": "Your teacher scores these.",
  "items": [
   {"t":"open","key":"goodquestion","q":"Write your own definition of a good research question, with at least three features. Then test your Unit 6 question against your definition and explain whether it passes.","min":51,"rows":5,"rubric":["A definition with at least three features","Applies the definition to your own question","An honest conclusion"],"model":"A good research question is open (it asks how or why), focused enough to answer in a short presentation, answerable with at least three reliable sources, and important to someone. My question about Lake Okeechobee algae passes: it asks why and what, it focuses on one lake, I already found several government sources, and it matters to families on the coast."},
   {"t":"open","key":"historianq","q":"Historians and scientists both ask questions. Compare a question a historian asked in Unit 5 (such as who built Great Zimbabwe) with a question a scientist asked in Unit 5 (such as why the lynx peak comes after the hare peak). How were their methods of answering alike and different?","min":56,"rows":5,"rubric":["Accurate examples from both","At least one similarity in method","At least one difference in method"],"model":"Archaeologists asked who built Great Zimbabwe and answered by digging, dating objects and comparing them with Shona culture. Ecologists asked why the lynx peak comes after the hare peak and answered with long-term population data. Both gathered evidence and tested ideas instead of trusting assumptions. But the historians studied a past that can't be repeated, while ecologists could keep collecting new data and even build models."}]},
 "exit": [
  {"t":"open","key":"exit_openq","q":"Turn this closed question into an open research question: \"Is the Florida panther endangered?\"","min":8,"rows":2,"rubric":["An open how or why question about the same subject"],"model":"Why is the Florida panther still endangered, and what is helping its numbers grow?"},
  {"t":"text","q":"What do we call a smaller question that helps answer the main research question?","a":[{"all":[["sub-question","subquestion","sub question"]],"none":["not"]}],"show":"a sub-question","pts":2,"why":"Three to five make a research plan."},
  {"t":"open","key":"exit_refocus","q":"Give one reason a researcher might refocus a question.","min":6,"rows":2,"rubric":["A valid reason (too broad, too narrow, a better question found)"],"model":"It was too broad: there were thousands of sources and no way to cover them."}],
 "next": "Week 27: judging sources and spotting misinformation."
}

TEACHER = {
 "standards": [
  "ELA.6.C.4.1: Conduct research to answer a question, drawing on multiple reliable and valid sources, and refocusing the inquiry when appropriate.",
  "ELA.K12.EE.1.1: Cite evidence to explain and justify reasoning."],
 "materials": ["The interactive lesson", "A timer, about 30 sticky notes, two markers, a large sheet of paper", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 25 warm-up questions; recall Week 9."],
  [4, "Hook", "Topic versus question: Silver Springs."],
  [10, "Open and closed", "Convert questions; closed questions as sub-questions."],
  [13, "Question ladder", "Narrow topics; fix too broad and too narrow."],
  [11, "Sub-questions and plan", "Match sub-questions to source types."],
  [10, "Refocusing", "The python case; start a research log."],
  [6, "Assign", "Set up the question storm; preview the Unit 6 research presentation; assign Think Deeper and the Exit Check."]],
 "key_questions": ["Is this a topic or a question?", "Could you answer it in 3 to 5 minutes with three sources?", "What smaller questions do you need to answer first?", "What would make you change your question?"],
 "misconceptions": ["A topic is the same as a question.", "Changing your question means you failed.", "One good source is enough.", "Googling the question word for word is research."],
 "support": ["Provide question starters (How, Why, To what extent, What are the effects of).", "Model one question ladder aloud.", "Let students choose from a short list of topics if they are stuck."],
 "challenge": ["Write a research question that would require both a historian's and a scientist's methods.", "Interview a librarian about how they help people narrow research questions."],
 "background": "<p>This week starts the Unit 6 research presentation, due in Week 30 (see the Unit 6 projects page when it is posted). Week 9 introduced research questions and note cards; this week builds on that with open and closed questions, scope, sub-questions, planning by source type and refocusing, as ELA.6.C.4.1 requires. Students should keep their research log through Week 30.</p>",
 "sources": ["Florida Department of Education, B.E.S.T. Standards for English Language Arts (2020).", "Rothstein, Dan, and Luz Santana, Make Just One Change: Teach Students to Ask Their Own Questions (2011)."]
}

PRINT = {
 "directions": "Answer in complete sentences.",
 "items": [
  {"q":"Label each question open or closed: (a) What year did Florida become a state? (b) Why did Florida's population grow so fast after 1950?","a":"(a) closed (b) open","lines":2},
  {"q":"Narrow the topic \"sports\" into a focused research question.","a":"Model: How have new rules about head injuries changed youth football in Florida?","lines":2},
  {"q":"Write three sub-questions for: \"How did the Maya build such accurate calendars?\"","a":"Model: What did they observe in the sky? How did their number system work? How did they record dates?","lines":3},
  {"q":"Explain the three tests for a researchable question.","a":"Three or more sources; can be answered in 3 to 5 minutes; you genuinely want to know.","lines":2},
  {"q":"Write your Unit 6 research question.","a":"Answers will vary; it should be open, focused and researchable.","lines":2}]
}
