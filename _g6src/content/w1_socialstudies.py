TIMELINE = '''<svg viewBox="0 0 580 160" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Timeline from 5000 BCE to 2000 CE">
<text x="290" y="16" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">BCE counts down. CE counts up.</text>
<line x1="20" y1="80" x2="560" y2="80" stroke="#0A1F3D" stroke-width="3"/>
<g text-anchor="middle"><line x1="30" y1="73" x2="30" y2="87" stroke="#0A1F3D"/><text x="30" y="101">5000 BCE</text><line x1="105" y1="73" x2="105" y2="87" stroke="#0A1F3D"/><text x="105" y="101">4000 BCE</text><line x1="180" y1="73" x2="180" y2="87" stroke="#0A1F3D"/><text x="180" y="101">3000 BCE</text><line x1="255" y1="73" x2="255" y2="87" stroke="#0A1F3D"/><text x="255" y="101">2000 BCE</text><line x1="330" y1="73" x2="330" y2="87" stroke="#0A1F3D"/><text x="330" y="101">1000 BCE</text><line x1="405" y1="73" x2="405" y2="87" stroke="#0A1F3D"/><text x="405" y="101"></text><line x1="480" y1="73" x2="480" y2="87" stroke="#0A1F3D"/><text x="480" y="101">1000 CE</text><line x1="555" y1="73" x2="555" y2="87" stroke="#0A1F3D"/><text x="555" y="101">2000 CE</text>
<line x1="405" y1="66" x2="405" y2="94" stroke="#DB2F30" stroke-width="3"/><text x="405" y="108" fill="#DB2F30" font-weight="bold">Year 1 CE</text>
<text x="200" y="48" fill="#0047BA">&#8592; older (BCE)</text><text x="500" y="48" fill="#0047BA">newer (CE) &#8594;</text>
<circle cx="45" cy="80" r="6" fill="#C9A84C"/><text x="45" y="64" font-size="10">Nabta Playa c. 4800 BCE</text>
<circle cx="180" cy="80" r="6" fill="#C9A84C"/><text x="180" y="128">Stonehenge c. 3000 BCE</text>
<circle cx="217" cy="80" r="6" fill="#C9A84C"/><text x="232" y="146">Great Pyramid c. 2500 BCE</text>
<circle cx="498" cy="80" r="6" fill="#C9A84C"/><text x="498" y="128">Mali founded c. 1235 CE</text></g></svg>'''

from geo import africa_map, florida_map
AFRICAMAP = africa_map([(30.7,22.5,'Nabta Playa'),(-3,16.8,'Timbuktu (Mali)',-6),(31.2,30,'Cairo')], 'Evidence across Africa')
FLMAP = florida_map([(-82.0,26.6,'Calusa'),(-82.3,29.6,'Timucua'),(-80.4,25.9,'Tequesta'),(-84.3,30.5,'Apalachee'),(-80.7,27.8,'Ais')], 'Some nations of Florida before 1513')
LESSON = {
 "unit": "Unit 1: How We Know the Past",
 "title": "Historians, Sources and Evidence",
 "subtitle": "History is not just a list of facts. It is detective work, and you get to be the detective.",
 "objectives": [
  "Tell the difference between primary and secondary sources and explain the strengths of each.",
  "Explain how historians learn about the past from artifacts, archaeology and oral tradition, not only from written records.",
  "Read a timeline using BCE and CE, and calculate the time between events.",
  "Identify point of view and bias, and explain why historians compare more than one source.",
  "Collect and analyze sources from your own family's history."],
 "vocab": [
  ["primary source", "A source created by someone who was there at the time: a letter, diary, photograph, artifact or eyewitness account."],
  ["secondary source", "A source created later by someone studying the past: a textbook, encyclopedia article or documentary."],
  ["artifact", "An object made or used by people in the past, such as a tool, pot or coin."],
  ["archaeology", "The study of the human past by digging up and analyzing artifacts and sites."],
  ["oral tradition", "History, stories and knowledge passed down by speaking from one generation to the next."],
  ["griot", "A West African historian, storyteller and musician who preserves a community's history through oral tradition."],
  ["BCE / CE", "Before the Common Era and Common Era. BCE years count down toward year 1; CE years count up from it."],
  ["point of view", "The position or perspective from which a person sees and describes events."],
  ["bias", "A one-sided view that favors some people or ideas over others."],
  ["corroborate", "To confirm a piece of evidence by finding another source that agrees with it."]],
 "reconnect": {
  "title": "Social studies tools from Grade 5",
  "intro": "History and geography go together. Warm up the skills you will use every week.",
  "items": [
   {"t":"num","q":"How many continents are there?","a":7,"pts":2,"why":"In the United States we count seven: Africa, Antarctica, Asia, Australia (Oceania), Europe, North America and South America. Students in many other countries learn six or five, for example by counting the Americas as one continent. Global thinkers know the count depends on the model."},
   {"t":"text","q":"Which continent is Egypt in?","a":["africa"],"show":"Africa","pts":2,"why":"Egypt is in northeastern Africa. This matters a great deal in Unit 2."},
   {"t":"text","q":"What is the largest ocean on Earth?","a":["pacific","pacific ocean","the pacific"],"show":"Pacific Ocean","pts":2,"why":"The Pacific Ocean is the largest and deepest ocean."},
   {"t":"text","q":"A map's ___ explains what the symbols and colors on the map mean. What is it called?","a":["key","legend","map key","map legend"],"show":"key (legend)","pts":2,"why":"The key, or legend, tells you what each symbol means."},
   {"t":"blanks","q":"Fill in the time words.","sent":"A decade is ___ years. A century is ___ years. A millennium is ___ years.","blanks":[["10","ten"],["100","one hundred","hundred"],["1000","1,000","one thousand","thousand"]],"pts":3,"why":"Decade 10, century 100, millennium 1,000."},
   {"t":"num","q":"On a number line, which is farther from zero: −30 or −10? Type the number.","a":-30,"pts":2,"why":"−30 is 30 units from zero; −10 is only 10. BCE dates work the same way: 30 BCE is farther back in time than 10 BCE."},
   {"t":"text","q":"A letter written by a Civil War soldier in 1863 is what kind of source?","a":["primary","primary source","a primary source"],"show":"primary","pts":2,"why":"It was written at the time by someone who lived through the event."}]},
 "hook": {
  "title": "The Shoebox in Grandma's Closet",
  "html": "<p>When Nia helped her grandmother clean out a closet in Jacksonville, she found a shoebox holding a faded photograph of a church picnic, a 1964 newspaper page, a ration book, and a handwritten letter. Her grandmother laughed and said, \"That box is the whole story of our family. You just have to know how to read it.\"</p><p>Historians work just like Nia. The past is gone, but it leaves behind <b>evidence</b>. This year you will study more than 10,000 years of human history, from the first farming towns to the meeting of the Americas, Africa and Europe. Today you learn the detective tools that make it possible.</p><div class='callout'><b>Big idea:</b> Every source tells part of a story from someone's point of view. Historians compare many sources, written, spoken and buried, to get closer to the truth.</div>"},
 "learn": [
  {"title": "Primary and Secondary Sources",
   "html": "<table class='t'><tr><th>Primary source (from the time)</th><th>Secondary source (made later)</th></tr><tr><td>Nia's 1964 newspaper page</td><td>A 2020 book about Jacksonville in the 1960s</td></tr><tr><td>A letter written by a soldier during a war</td><td>A documentary about that war</td></tr><tr><td>A clay pot made 4,000 years ago</td><td>A museum label explaining the pot</td></tr><tr><td>An interview with someone who marched for civil rights</td><td>An encyclopedia article on the civil rights movement</td></tr></table><p><b>Primary sources</b> let you hear directly from the past. <b>Secondary sources</b> pull many primary sources together and explain them. Historians need both.</p>",
   "checks": [
    {"t":"text","q":"A diary written by a girl during a hurricane in 1926. Primary or secondary?","a":["primary"],"pts":2,"why":"She wrote it at the time she lived through the event."},
    {"t":"text","q":"Your history textbook. Primary or secondary?","a":["secondary"],"pts":2,"why":"It was written later by people studying the past."},
    {"t":"open","key":"stonetool","q":"A stone tool made 10,000 years ago is a primary source even though it has no words. Name two things it can tell a historian and one thing it cannot.","min":20,"rows":3,"rubric":["Two reasonable things the tool reveals (skills, food, materials, trade)","One clear limit (names, beliefs, language, exact purpose)"],"model":"It can show what stone people used and what jobs they did, such as cutting meat or scraping hides. It cannot tell us the toolmaker's name, language or beliefs."},
    {"t":"text","q":"Name one advantage a secondary source has over a single primary source.","a":[{"all":[["many","several","different","compare","combine","overview","explain","big picture","research","multiple","lots of sources","more sources","all the"]]}],"show":"It brings together many sources and explains the big picture.","pts":3,"why":"Secondary sources combine and compare many primary sources, so they can explain more than one eyewitness can."}]},
  {"title": "Evidence Beyond Writing",
   "visual": AFRICAMAP,
   "html": "<p>Writing was invented only about 5,000 years ago, and many great societies kept their history in other ways. Historians use every kind of evidence:</p><ul><li><b>Archaeology:</b> digging up buildings, tools, bones and seeds. A stone circle at <b>Nabta Playa</b> in southern Egypt, built about 7,000 years ago by cattle-herding people, lines up with the summer sunrise. That makes it older than England's Stonehenge.</li><li><b>Oral tradition:</b> In the Mali Empire of West Africa, <b>griots</b> memorized and performed the history of kings and families. The epic of <b>Sundiata Keita</b>, founder of Mali around 1235 CE, has been passed down by griots for nearly 800 years and is still performed today.</li><li><b>Language, art and DNA:</b> how languages spread, what people painted, and what genes show about where people moved.</li></ul><div class='callout'>Some historians once dismissed oral history as \"just stories.\" Today historians treat it as serious evidence, checked like any other source.</div>",
   "checks": [
    {"t":"text","q":"What do we call a West African keeper of oral history?","a":["griot","griots","jeli","djeli"],"show":"griot","pts":2,"why":"Griots preserve history through speech, song and music."},
    {"t":"text","q":"What kind of evidence is the stone circle at Nabta Playa?","a":[{"all":[["archaeolog","artifact","site","physical","monument","structure","primary"]]}],"show":"Archaeological evidence (a primary source)","pts":3,"why":"It is a physical site studied by archaeologists."},
    {"t":"text","q":"Which is older: Nabta Playa or Stonehenge?","a":["nabta playa","nabta"],"show":"Nabta Playa","pts":2,"why":"Nabta Playa is about 7,000 years old; Stonehenge is about 5,000 years old."},
    {"t":"text","q":"Why would a historian studying the Mali Empire need oral tradition and not only written records?","a":[{"all":[["griot","spoken","passed down","memor","not written","no written","few written","not write","didn't write","spoke","speak","story","stories","song","told","sang"]]}],"show":"Because much of Mali's history was kept by griots through speaking, not writing.","pts":3,"why":"Leaving out oral tradition would leave out much of West Africa's own record of its past."}]},
  {"title": "Reading Time: BCE and CE",
   "visual": TIMELINE,
   "html": "<p>On a timeline, <b>BCE</b> years count <i>down</i> as they get closer to year 1, and <b>CE</b> years count <i>up</i>. So 2500 BCE is <b>older</b> than 1000 BCE, even though 2500 is the bigger number.</p><ul><li><b>Both BCE:</b> subtract. From 2500 BCE to 1000 BCE is 2500 − 1000 = <b>1,500 years</b>.</li><li><b>Both CE:</b> subtract. From 1235 CE to 2026 CE is 2026 − 1235 = <b>791 years</b>.</li><li><b>One BCE, one CE:</b> add. From 500 BCE to 500 CE is about 500 + 500 = <b>1,000 years</b>.</li></ul><p>Centuries are named one number ahead: the years 1201 to 1300 are the <b>13th century</b>, and the 1900s are the <b>20th century</b>. The abbreviation <i>c.</i> means <i>circa</i>, or about.</p>",
   "checks": [
    {"t":"text","q":"Which happened first: 3000 BCE or 2000 BCE?","a":["3000 bce","3000","3,000 bce","3,000"],"show":"3000 BCE","pts":2,"why":"BCE years count down, so 3000 BCE came 1,000 years before 2000 BCE."},
    {"t":"num","q":"How many years passed from 2500 BCE to 1500 BCE?","a":1000,"show":"1,000","unit":"years","pts":3,"why":"Both are BCE, so subtract: 2500 − 1500 = 1,000 years."},
    {"t":"num","q":"About how many years passed from 300 BCE to 200 CE?","a":[500,499],"unit":"years","pts":3,"why":"One BCE and one CE, so add: 300 + 200 = 500 years. (Because there is no year 0, the exact count is 499; either answer is accepted.)"},
    {"t":"num","q":"Mali was founded around 1235 CE. How many years before 2026 is that?","a":791,"unit":"years","pts":3,"why":"Both CE: 2026 − 1235 = 791 years."},
    {"t":"text","q":"In what century was the year 1776?","a":["18th","18th century","eighteenth","eighteenth century","the 18th century"],"show":"18th century","pts":3,"why":"The 1700s are the 18th century, because centuries are named one number ahead."}]},
  {"title": "Point of View and Bias",
   "visual": FLMAP,
   "html": "<p>Every source is made by a person with a point of view. Compare two descriptions of the same event.</p><div class='example'><b>Source A, a sentence like those in many older textbooks, based on Spanish accounts:</b> <i>In 1513, Juan Ponce de León discovered a new land full of flowers and named it La Florida.</i><br><br><b>Source B, a historian writing about the Calusa people:</b> <i>For more than a thousand years before 1513, the Calusa had built towns, canals and shell mounds along Florida's southwest coast. When Spanish ships arrived that year, Calusa warriors drove them away. They resisted Spanish control for generations.</i></div><p>Source A uses the word <b>discovered</b>. But the land was already home to the Calusa, the Timucua, the Tequesta and many other nations. From their point of view, it was not discovered at all. The word shows the writer's bias. Historians <b>corroborate</b>: they check every source against others before trusting it.</p>",
   "checks": [
    {"t":"text","q":"Which word in Source A shows the Spanish writer's point of view?","a":["discovered","discover"],"show":"discovered","pts":3,"why":"\"Discovered\" treats the land as unknown, ignoring the people who already lived there."},
    {"t":"text","q":"Name one Indigenous nation that lived in Florida before 1513.","a":["calusa","timucua","tequesta","apalachee","ais","tocobaga","mayaimi","jeaga"],"show":"Calusa (also Timucua, Tequesta, Apalachee and others)","pts":2,"why":"Many nations lived in Florida for thousands of years before Spanish ships arrived; you will study them in Unit 6. The Seminole formed later, in the 1700s, from Creek and other peoples who moved into Florida."},
    {"t":"text","q":"What does it mean to <b>corroborate</b> a source?","a":[{"all":[["confirm","check","compare","agree","another source","other sources","verify","support"]]}],"show":"To confirm it by checking it against another source that agrees","pts":3,"why":"Corroborating means confirming evidence with another independent source."},
    {"t":"open","key":"fair","q":"Rewrite Source A's first sentence so it is fair to both points of view.","min":15,"rows":3,"rubric":["Replaces discovered with a fair verb such as arrived or reached","Acknowledges the people already living there","Keeps the facts (1513, Ponce de León, La Florida)"]}]}],
 "handson": {
  "title": "Family History Detective",
  "intro": "Every family is a source of history. Collect evidence from your own home and interview someone who remembers the past.",
  "materials": ["Three sources from home: a photograph, a document (letter, card, certificate, recipe) and an object (anything older than you)", "A family member or family friend, older than 40 if possible, to interview", "Paper or a phone to record notes (ask permission before recording)"],
  "steps": [
   "Collect your three sources. For each, write what it is, when it was made, who made it, and whether it is primary or secondary.",
   "Interview your family member for 10 minutes. Ask: Where did you grow up? What was school like? What big event do you remember from the news? What is something young people today would not believe about your childhood?",
   "Your interview is an <b>oral history</b>, a primary source. Write down one quote exactly as they said it.",
   "Find one fact from the interview that one of your three sources can corroborate, or that you could check another way."],
  "record": [
   {"t":"open","key":"sources","q":"Describe your three sources: what each is, when and by whom it was made, and whether it is primary or secondary.","min":40,"rows":5},
   {"t":"open","key":"interview","q":"Who did you interview? Write one exact quote, and explain how you could corroborate one fact they told you.","min":40,"rows":5}]},
 "think": {
  "items": [
   {"t":"open","key":"oral","model":"I disagree. Griots trained for years to memorize Sundiata's epic exactly, and it has survived for nearly 800 years. My grandmother remembered details about her school that no written record I found includes. Written sources can also be biased, like the textbook sentence that said Ponce de León discovered Florida. Historians should corroborate both kinds of sources.","q":"A classmate says, \"Oral history is less reliable than written history, because people forget things.\" Do you agree or disagree? Use the griots, your own interview, and the idea of bias in written sources to support your answer.","min":80,"rows":7,"rubric":["Takes a clear position","Uses the griot example accurately","Uses evidence from the student's own interview","Recognizes that written sources can also be biased or wrong","Explains how corroboration helps with any kind of source"]},
   {"t":"open","key":"pov","q":"Think of an event in your own life that two people would describe differently, such as an argument or a game. How would each person's point of view change the story?","min":40,"rows":5,"rubric":["Describes a real event","Shows how two points of view differ","Connects to how historians read sources"]}]},
 "exit": [
  {"t":"text","q":"A photograph taken at a 1963 civil rights march. Primary or secondary?","a":["primary"],"pts":2,"why":"It was created at the event."},
  {"t":"text","q":"A 2025 website summarizing the history of the Calusa. Primary or secondary?","a":["secondary"],"pts":2,"why":"It was created long afterward by someone studying the past."},
  {"t":"num","q":"How many years passed from 1800 BCE to 1200 BCE?","a":600,"unit":"years","pts":3,"why":"Both BCE: 1800 − 1200 = 600 years."},
  {"t":"num","q":"About how many years passed from 100 BCE to 400 CE?","a":[500,499],"unit":"years","pts":3,"why":"One BCE, one CE: 100 + 400 = 500 years."},
  {"t":"text","q":"In what century was the year 1492?","a":["15th","15th century","fifteenth","fifteenth century","the 15th century"],"show":"15th century","pts":3,"why":"The 1400s are the 15th century."},
  {"t":"text","q":"What is the study of the past through digging up artifacts called?","a":["archaeology","archeology"],"pts":2,"why":"Archaeologists study physical remains of the past."},
  {"t":"text","q":"Why should a historian compare more than one source about the same event?","a":[{"all":[["bias","point of view","perspective","one side","different","corroborate","check","confirm","accurate","truth","wrong"]]}],"show":"Because each source has a point of view or bias, and comparing them gets closer to the truth.","pts":3,"why":"Comparing sources reveals bias and confirms facts."}],
 "next": "Week 2: maps and the true size of the world. You will discover why the map on most classroom walls makes Africa look far smaller than it really is."
}

TEACHER = {
 "standards": [
  "SS.6.W.1.3: Interpret primary and secondary sources.",
  "SS.6.W.1.4: Describe the methods of historical inquiry and how history relates to the other social sciences.",
  "SS.6.W.1.1: Use timelines to identify chronological order of historically significant persons, events and time periods within the ancient world.",
  "SS.6.W.1.6: Describe how history transmits culture and heritage and provides models of human character.",
  "C3 Framework D2.His.4.6-8 and D2.His.10.6-8: Analyze multiple factors that influenced perspectives; detect possible limitations in the historical record based on evidence."],
 "materials": ["The interactive lesson", "Two or three items from your own family to model the activity on camera", "Printable practice page"],
 "flow": [
  [5, "Reconnect", "Run the Reconnect questions. Note any confusion about continents; Africa's place in the world is central to Units 1 and 2."],
  [7, "Hook", "Read Nia's shoebox story. Hold up one item from your own home and ask: what could a historian learn from this in 100 years?"],
  [10, "Primary and secondary", "Sort the table examples. Emphasize that artifacts with no words still count as primary sources."],
  [12, "Evidence beyond writing", "Discuss Nabta Playa and the griots. Ask: if a society did not write, does that mean it had no history? Why did some historians once think so?"],
  [12, "BCE and CE", "Draw a timeline. Work one problem of each type: both BCE, both CE, and crossing year 1. Practice naming centuries."],
  [11, "Point of view", "Read Sources A and B aloud. Ask the student to find the biased word and explain whose story it leaves out. Rewrite the sentence together."],
  [3, "Assign", "Explain the family interview; suggest the student schedule it with a relative this week."]],
 "key_questions": ["Who made this source, and when?", "What can this source tell us, and what can it not tell us?", "Whose voice is missing from this account?", "How could you check whether this is true?", "Is an older number always an older date? Why not?"],
 "misconceptions": ["Thinking bigger BCE numbers are more recent.", "Thinking the 1900s are the 19th century.", "Believing primary sources are always true; they carry the creator's point of view.", "Believing societies without writing had no history or were less advanced."],
 "support": ["Draw a number line with 1 BCE and 1 CE side by side (there is no year 0) to model BCE and CE, like negative and positive numbers (connects to Math Unit 4).", "Give a sorting card set: primary on one pile, secondary on the other.", "Provide interview questions on a printed card."],
 "challenge": ["Ask the student to explain why there is no year 0 between 1 BCE and 1 CE and how that changes the exact count across the line by one year.", "Have the student find a modern news story told differently by two outlets and identify the word choices that reveal point of view."],
 "background": "<p>Nabta Playa, about 100 kilometers west of Abu Simbel in southern Egypt, was used by cattle-herding peoples during the wetter Holocene period, when the Sahara was greener. Its calendar circle is dated to about 4800 BCE (roughly 7,000 years ago) and appears aligned with the summer solstice sunrise, which came near the start of the rainy season. Stonehenge's first phase dates to about 3000 BCE. Some details at Nabta Playa, such as whether the earliest cattle were domesticated and exactly how the stones align with the sky, are still debated by archaeologists.</p><p>The Epic of Sundiata tells of Sundiata Keita, who founded the Mali Empire around 1235 CE; it has been preserved by Mande griots (jeli) for centuries. The Calusa of Southwest Florida built shell-mound towns such as Mound Key, repelled Juan Ponce de León's ships in 1513, and wounded him fatally in 1521.</p>",
 "sources": ["Malville, J. M. et al. (1998). Megaliths and Neolithic astronomy in southern Egypt. Nature 392: 488 to 491.", "Niane, D. T. (1965). Sundiata: An Epic of Old Mali. Longman.", "Florida Museum of Natural History: The Calusa.", "Smithsonian National Museum of African American History and Culture: Oral history collections."]
}

PRINT = {
 "directions": "Answer in complete sentences. Show your timeline math.",
 "items": [
  {"q":"Label each P (primary) or S (secondary).  ___ A Roman coin  ___ A documentary about Rome  ___ A soldier's letter from 1918  ___ An encyclopedia article  ___ A recorded interview with your grandfather","a":"P, S, P, S, P","lines":1},
  {"q":"Explain why a stone tool with no writing on it can still be a primary source.","a":"It was made and used by people at the time, so it gives direct evidence about their lives.","lines":2},
  {"q":"How many years passed from 3100 BCE to 2600 BCE? Show your work.","a":"3100 − 2600 = 500 years","lines":2},
  {"q":"About how many years passed from 750 BCE to 250 CE? Show your work.","a":"750 + 250 = about 1,000 years","lines":2},
  {"q":"What century is each year in?  1350 ______  1865 ______  2026 ______","a":"14th, 19th, 21st","lines":1},
  {"q":"What is a griot, and why are griots important to the history of West Africa?","a":"A griot is a West African oral historian and musician who preserves history, such as the Epic of Sundiata, through speaking and song.","lines":3},
  {"q":"A source says a European explorer \"discovered\" a river in Africa. Explain the bias in this word and rewrite the sentence fairly.","a":"People living along the river already knew it; for example: The explorer reached a river that local peoples had lived beside for centuries.","lines":3}]
}
