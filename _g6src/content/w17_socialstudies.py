GMAP = ('<svg viewBox="0 0 640 330" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Schematic map of ancient Greece showing mountains, the Aegean Sea and city-states including Athens and Sparta">'
  '<rect width="640" height="330" fill="#eaf2fb"/>'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Ancient Greece: mountains, sea and city-states</text>'
  # mainland
  '<path d="M60 40 L300 40 L320 90 L290 120 L300 150 L270 170 L250 160 L240 190 L200 200 L180 180 L150 190 L130 170 L100 150 L80 110Z" fill="#f4ecd8" stroke="#b9a77a"/>'
  # Peloponnese
  '<path d="M150 210 L230 205 L250 240 L230 270 L210 300 L190 270 L170 300 L150 270 L130 250Z" fill="#f4ecd8" stroke="#b9a77a"/>'
  # Asia Minor
  '<path d="M440 40 L640 40 L640 300 L470 300 L460 260 L480 220 L450 190 L470 150 L440 120 L460 80Z" fill="#f4ecd8" stroke="#b9a77a"/>'
  # islands
  + ''.join(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#f4ecd8" stroke="#b9a77a"/>' for x, y, rx, ry in [(340, 200, 10, 6), (370, 230, 8, 5), (320, 250, 9, 6), (400, 180, 12, 7), (420, 120, 10, 14), (300, 300, 70, 10)]) +
  # mountains
  ''.join(f'<path d="M{x-10} {y+8} L{x} {y-8} L{x+10} {y+8}Z" fill="#8a6d1f"/>' for x, y in [(120, 80), (150, 100), (180, 70), (210, 110), (240, 80), (170, 140), (200, 240), (180, 260), (540, 120), (580, 200)]) +
  ''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="#0A1F3D"/><text x="{x+tx}" y="{y+ty}" font-weight="bold" fill="#0A1F3D">{n}</text>' for x, y, n, tx, ty in [(258, 160, "Athens", 8, 10), (195, 265, "Sparta", 8, 4), (180, 205, "Corinth", -50, -4), (130, 160, "Delphi", -42, 0), (282, 142, "Marathon", 8, -4), (500, 180, "Miletus", 8, 4), (150, 228, "Olympia", -52, 4)]) +
  '<text x="360" y="90" font-size="12" fill="#0047BA" font-style="italic">Aegean Sea</text><text x="60" y="300" font-size="12" fill="#0047BA" font-style="italic">Mediterranean Sea</text><text x="500" y="64" font-size="11" fill="#5b6676">Asia Minor</text><text x="500" y="78" font-size="10" fill="#5b6676">(ruled by Persia)</text><text x="285" y="304" font-size="10" fill="#5b6676">Crete</text>'
  '<path d="M18 230 h12 M24 224 v12" stroke="#0A1F3D"/><text x="12" y="220" font-size="10">N</text>'
  '<path d="M470 316 L480 304 L490 316Z" fill="#8a6d1f"/><text x="496" y="316" font-size="10">mountains</text>'
  '<text x="630" y="326" text-anchor="end" font-size="9" fill="#5b6676">Schematic map, not to scale.</text></svg>')

COMPARE = ('<svg viewBox="0 0 640 250" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Comparison of Athens and Sparta">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Two city-states, two ways of life (about 450 BCE)</text>'
  '<rect x="20" y="34" width="290" height="206" rx="12" fill="#0047BA"/><rect x="330" y="34" width="290" height="206" rx="12" fill="#DB2F30"/>'
  '<text x="165" y="58" text-anchor="middle" fill="#fff" font-weight="bold" font-size="15">Athens</text><text x="475" y="58" text-anchor="middle" fill="#fff" font-weight="bold" font-size="15">Sparta</text>'
  + ''.join(f'<text x="165" y="{84+i*24}" text-anchor="middle" fill="#fff" font-size="11">{a}</text><text x="475" y="{84+i*24}" text-anchor="middle" fill="#fff" font-size="11">{b}</text>' for i, (a, b) in enumerate([
    ("Government: direct democracy", "Government: two kings, council of elders"),
    ("Citizens vote in the Assembly", "and an assembly of citizen soldiers"),
    ("Boys: reading, music, sport, debate", "Boys: army training from age 7"),
    ("Women: mostly kept at home,", "Women: more freedom, could own land,"),
    ("no vote", "trained for fitness; no vote"),
    ("Economy: trade, crafts, navy", "Economy: farming by enslaved helots"),
    ("Enslaved people: many, no rights", "Helots outnumbered citizens")])) +
  '</svg>')

PERICLES = ("<div class='card' style='border-left-color:#C9A84C'><h3 style='margin-top:0'>Pericles' Funeral Oration</h3><p class='muted' style='margin-top:-6px'>Speech by the Athenian leader Pericles in 431 BCE, as written by the historian Thucydides in History of the Peloponnesian War, Book 2, translated by Richard Crawley (1874). ... marks words left out.</p>"
            "<p style='font-family:Georgia,serif'>Our constitution does not copy the laws of neighbouring states; we are rather a pattern to others than imitators ourselves. Its administration favours the many instead of the few; this is why it is called a democracy. If we look to the laws, they afford equal justice to all in their private differences; ... nor again does poverty bar the way, if a man is able to serve the state, he is not hindered by the obscurity of his condition.</p>"
            "<p class='muted' style='font-size:12px'>constitution: here, the system of government. neighbouring and favours: British spellings of neighboring and favors, kept as printed. administration: the way the government is run. afford: give. obscurity of his condition: being poor or unknown.</p></div>")

LESSON = {
 "unit": "Unit 4: The Mediterranean World",
 "title": "Ancient Greece",
 "subtitle": "Mountains and sea divided the ancient Greeks into hundreds of independent city-states, yet they shared a language, gods, games and big ideas. This week you compare Athens and Sparta, follow the Persian Wars from the Greek side, and judge the first democracy: who got a voice, and who didn't?",
 "objectives": [
  "Explain how geography led the Greeks to form independent city-states and to become sailors and traders.",
  "Compare the government and the status of citizens in Athens and Sparta.",
  "Describe Athenian democracy, its democratic ideas and its limits.",
  "Explain the causes and effects of the Persian Wars.",
  "Summarize Greek achievements and how Greek and African civilizations, especially Egypt, influenced each other."],
 "vocab": [
  ["polis", "A Greek city-state: a city and the farmland around it, with its own government."],
  ["democracy", "Government by the people; in Athens, citizens voted directly on laws."],
  ["citizen", "A member of a state with rights, such as voting, and duties, such as serving."],
  ["oligarchy", "Government by a small group of powerful people."],
  ["assembly", "In Athens, the meeting where citizens debated and voted on laws."],
  ["ostracism", "An Athenian vote to send a powerful citizen away from the city for ten years."],
  ["Hellenistic", "Describes the Greek-influenced cultures that spread from Egypt to India after Alexander the Great."]],
 "reconnect": {
  "title": "Week 16: Persia",
  "intro": "Last week you saw the Persian Empire from the inside. This week the Greeks fight it.",
  "items": [
   {"t":"text","q":"Which Persian king organized the empire into satrapies and built Persepolis?","a":[{"all":[["darius"]],"none":["not"]}],"show":"Darius I","pts":2,"why":"Ruled 522 to 486 BCE."},
   {"t":"text","q":"Which Greek historian described the Persian messengers?","a":[{"all":[["herodotus"]],"none":["not"]}],"show":"Herodotus","pts":2,"why":"The Histories, Book 8."},
   {"t":"text","q":"Which city in Asia Minor was at the western end of the Royal Road?","a":[{"all":[["sardis"]],"none":["not"]}],"show":"Sardis","pts":2,"why":"It ran about 1,600 miles to Susa."},
   {"t":"open","key":"rc_herobias","q":"Last week you learned Herodotus was a Greek writing about Persia's invasion of Greece. How might that affect the way he tells the story of the Persian Wars?","min":15,"rows":2,"rubric":["He may favor the Greeks, make them look heroic or exaggerate Persian numbers","So historians compare his account with other evidence"],"model":"He might make the Greeks look heroic and exaggerate the size of the Persian army, so historians check his account against other evidence."}]},
 "hook": {
  "title": "The Runner from Marathon",
  "visual": GMAP,
  "html": "<p>In 490 BCE, a Persian army sent by Darius landed at Marathon, about 26 miles from Athens. The Athenians and their Plataean allies, badly outnumbered, charged down from the hills and won. A famous legend says a messenger ran all the way back to Athens, gasped \"We have won!\" and collapsed. Herodotus tells a different story: a runner named Pheidippides ran about 150 miles to Sparta <i>before</i> the battle to ask for help. Either way, today's 26.2-mile marathon race is named for that battle.</p><p>Why did tiny Athens fight for its independence so fiercely? Part of the answer is geography, and part is a new idea: that ordinary citizens should govern themselves.</p><div class='callout'><b>Big question:</b> What did the Greeks get right about government, and what did they get wrong?</div>"},
 "learn": [
  {"title": "Mountains, Sea and the City-State",
   "html": "<p>Greece is a rocky peninsula, crossed by mountains and surrounded by the sea, with hundreds of islands. Only about one-fifth of the land is good for farming. This geography shaped Greek life:</p><ul><li>Mountains separated valleys, so communities grew into independent <b>city-states</b> (each a <b>polis</b>), each with its own government, laws and army. There were more than 1,000 of them.</li><li>No place in Greece is far from the sea, so the Greeks became skilled sailors and traders, exchanging olive oil, wine and pottery for grain, metals and timber.</li><li>When cities grew crowded, Greeks founded colonies around the Mediterranean and Black Sea, from Spain to North Africa (Cyrene, in Libya) to what is now Ukraine.</li></ul><p>Though divided, Greeks shared a language, gods such as Zeus and Athena, the oracle at Delphi and the Olympic Games, first recorded in 776 BCE.</p>",
   "checks": [
    {"t":"open","key":"geocause","q":"Explain how Greece's mountains and its coastline each shaped the way Greeks lived. Give one effect for each.","min":30,"rows":3,"rubric":["Mountains: separated communities, leading to independent city-states (or limited farming)","Coastline/sea: trade, sailing, fishing or colonies"],"model":"The mountains cut the land into separate valleys, so each community became its own independent city-state with its own government. The long coastline meant the sea was always close, so Greeks became sailors and traders and started colonies around the Mediterranean."},
    {"t":"text","q":"What is the Greek word for a city-state?","a":[{"all":[["polis"]],"none":["not"]}],"show":"polis","pts":2,"why":"It gives us politics, police and metropolis."},
    {"t":"num","q":"The first recorded Olympic Games were held in 776 BCE. The Battle of Marathon was in 490 BCE. How many years apart were they?","a":286,"unit":"years","pts":2,"why":"For two BCE dates, subtract: 776 − 490 = 286 years."}]},
  {"title": "Athens and Sparta",
   "visual": COMPARE,
   "html": "<p>The two most powerful city-states chose very different paths.</p><p><b>Sparta</b> was ruled by two kings, a council of elders and five elected officials called ephors, with an assembly of citizen men. Sparta conquered its neighbors, mainly the Messenians, and forced them to farm as <b>helots</b>, enslaved people who greatly outnumbered Spartan citizens. Fearing revolt, Sparta made every citizen man a soldier: boys left home at 7 for harsh army training. Spartan women could own land and trained for fitness, unusual in Greece.</p><p><b>Athens</b> grew rich from trade, silver mines and its navy. Around 508 BCE, a leader named <b>Cleisthenes</b> reorganized the government so that citizens, not a few wealthy families, held power. Athenian boys studied reading, music, sport and public speaking. Athenian women had few rights outside the home.</p>",
   "checks": [
    {"t":"text","q":"What were the enslaved farm workers of Sparta called?","a":[{"all":[["helot"]],"none":["not"]}],"show":"helots","pts":2,"why":"They outnumbered Spartan citizens."},
    {"t":"open","key":"spartawhy","q":"Explain the connection between Sparta's helots and its military way of life.","min":25,"rows":3,"rubric":["Helots greatly outnumbered citizens, so Spartans feared revolt","They trained every citizen man as a soldier to keep control"],"model":"Sparta enslaved so many helots that they outnumbered the citizens, and the Spartans were afraid of a revolt. So they turned every citizen man into a full-time soldier to keep the helots under control."},
    {"t":"open","key":"wherelive","q":"If you were a girl in ancient Greece, would you rather live in Athens or Sparta? If you were an enslaved person, would either be fair? Explain both answers with evidence.","min":40,"rows":4,"rubric":["A choice for a girl with evidence (Spartan women owned land and trained; Athenian women had few rights)","Recognizes that enslaved people had no rights in either city"],"model":"As a girl I would choose Sparta, because Spartan women could own land and trained their bodies, while Athenian women were mostly kept at home. But for an enslaved person, neither was fair: helots in Sparta and enslaved people in Athens had no rights at all."}]},
  {"title": "The First Democracy, and Its Limits",
   "html": PERICLES + "<p>In Athens, any citizen could speak and vote in the <b>Assembly</b>, which met roughly 40 times a year on a hill called the Pnyx. Most officials and the members of the Council of 500 were chosen by <b>lottery</b>, and juries had hundreds of citizens. Citizens could even vote to <b>ostracize</b>, or exile for ten years, a person they feared was becoming too powerful, by scratching his name on a piece of broken pottery (an ostrakon). This was a <b>direct democracy</b>: citizens voted on laws themselves. The United States is a representative democracy: citizens elect people to make laws for them.</p><p>But in Athens, only <b>adult men whose parents were Athenian</b> were citizens, perhaps 30,000 to 60,000 people out of more than 250,000. Women, enslaved people (who may have made up a third of the population) and foreign-born residents could not vote.</p>",
   "checks": [
    {"t":"open","q":"Democracy comes from the Greek demos (people) and kratos (power). In your own words, what does Pericles mean when he says Athens' government \"favours the many instead of the few\"?","key":"favoursmany","min":15,"rows":2,"rubric":["Power belongs to the many citizens, not a small rich or noble group","Uses own words"],"model":"He means that ordinary citizens, not just a few rich or noble families, hold the power to make decisions."},
    {"t":"open","key":"directvsrep","q":"Explain the difference between Athens' direct democracy and the representative democracy of the United States. Why might a direct democracy be hard to run in a country of more than 330 million people?","min":30,"rows":3,"rubric":["Direct: citizens vote on laws themselves; representative: citizens elect lawmakers","Hard with millions: too many people to meet or debate, too many laws to vote on"],"model":"In Athens citizens voted on every law themselves; in the United States we elect representatives who make laws for us. A direct democracy would be hard with more than 330 million people because they couldn't all meet, debate and vote on every law."},
    {"t":"open","key":"pericleshonest","q":"Pericles says Athens gives \"equal justice to all\" and that poverty does not \"bar the way.\" Using evidence from the lesson, judge how true this was.","min":40,"rows":4,"rubric":["Partly true: poor citizen men could vote, serve on juries and be chosen by lottery","Not true for most residents: women, enslaved people and foreign-born residents were excluded","A balanced judgment"],"model":"It was partly true: a poor Athenian citizen man could vote in the Assembly, sit on a jury and even be chosen by lottery for office. But \"all\" really meant citizen men. Women, enslaved people and foreign-born residents, most of the people in Athens, had no vote at all, so Pericles' words were only true for a minority."}]},
  {"title": "The Persian Wars and Greek Achievements",
   "html": "<p>In 499 BCE, Greek cities in Ionia (western Asia Minor, under Persian rule) revolted, and Athens sent ships to help, and Athenian soldiers helped burn the Persian city of Sardis. Darius sent armies to punish Athens and was defeated at <b>Marathon</b> (490 BCE). Ten years later his son <b>Xerxes</b> invaded with a huge army. At <b>Thermopylae</b> (480 BCE), a small Greek force under the Spartan king Leonidas held a narrow pass for three days; on the last day Leonidas, his 300 Spartans and several hundred Thespians and Thebans stayed behind and were killed. Weeks later the Athenian navy, led by Themistocles, crushed the Persian fleet at <b>Salamis</b>, and in 479 BCE the Greeks won at Plataea. Effects: Greek independence, Athens' rise as a sea power, and later the Peloponnesian War between Athens and Sparta (431 to 404 BCE), which weakened both.</p><p>Greek thinkers and artists left a lasting legacy: philosophers Socrates, Plato and Aristotle; mathematicians such as Pythagoras and Euclid; the doctor Hippocrates; theater (tragedy and comedy); and architecture like the Parthenon. The Greeks also learned from older civilizations in Africa and Asia, above all Kemet (Egypt), the African civilization you studied in Unit 2, which was already more than 2,500 years old when Athens became a democracy. Herodotus wrote that the Greeks took the names of many gods from Egypt and credited the Egyptians with the 365-day calendar you learned about in Unit 2; later Greek writers said Greek thinkers studied there. When <b>Alexander the Great</b> took Egypt from the Persian Empire in 332 BCE, he founded <b>Alexandria</b>, which became the center of Hellenistic learning, with its great Library, where scholars from Africa, Greece and Asia worked side by side.</p>",
   "checks": [
    {"t":"order","q":"Put these events in order.","items":["Ionian Revolt","Battle of Marathon","Battle of Thermopylae","Peloponnesian War begins"],"pts":3,"why":"499, 490, 480 and 431 BCE."},
    {"t":"text","q":"At which sea battle in 480 BCE did the Athenian navy defeat Xerxes' fleet?","a":[{"all":[["salamis"]],"none":["not"]}],"show":"Salamis","pts":2,"why":"Led by Themistocles."},
    {"t":"open","key":"egyptgreece","q":"Give one piece of evidence that Greek civilization learned from Egypt, and explain why it matters to tell this part of the story.","min":30,"rows":3,"rubric":["Evidence: Herodotus on gods' names or the calendar, Greek thinkers studying in Egypt, Alexandria as a center of learning","Why it matters: civilizations build on each other; Greek achievement rested partly on older African knowledge; a truthful history includes it"],"model":"Herodotus wrote that the Greeks credited the Egyptians with the 365-day calendar. It matters because it shows Greek ideas didn't come from nowhere; they built on much older African knowledge, and a truthful history gives Egypt credit."}]}],
 "handson": {
  "title": "Athenian Assembly Day",
  "intro": "Run an Athenian-style assembly at home: choose officials by lottery, debate, vote with pebbles and try an ostracism.",
  "materials": ["A bag or bowl", "Slips of paper and a pencil for each person", "Dried beans or small pebbles in two colors (or white and dark paper squares)", "2 cups or bowls for voting", "A timer", "Family members (at least 2)", "Optional: a clean, broken flowerpot or smooth stones and a marker for ostraka"],
  "steps": [
   "Lottery: put everyone's name in the bag. Draw one \"president\" for the day (in Athens, the chair changed every day) and one \"timekeeper.\"",
   "Choose a real family question, such as \"Where should we go on our next field trip?\" or \"What should we cook on Friday?\" Each person speaks for 1 minute on the timer.",
   "Vote in secret with beans or pebbles: one color for yes, one for no, dropped into the voting cup. Count and announce the result.",
   "Now run it again with Athenian rules: draw \"citizen cards\" so that only about 1 in 5 people may vote (a stand-in for adult men with Athenian parents). Notice who is left out and how they feel.",
   "Ostracism: each person writes a pretend name (a historical figure, such as Themistocles or Aristides) on a paper or stone ostrakon. Count the votes to see who is \"exiled.\"",
   "If you use a broken flowerpot, an adult handles the sharp edges, or use smooth stones instead."],
  "record": [
   {"t":"open","key":"assemblyrec","q":"Describe your question, the arguments, and both votes. How did the result or the mood change when some people couldn't vote? What does this show about Athenian democracy?","min":50,"rows":5,"rubric":["Question and main arguments","Results of both votes","Observation of the exclusion's effect","Connects to Athens' limited citizenship"],"model":"We debated a field trip to the springs or the science museum. In the first vote, springs won 3 to 1. With the \"Athenian rules,\" only my dad and I could vote, so the result was 1 to 1, and my sister was upset that her voice didn't count. It showed that when most people can't vote, the decision doesn't reflect what the whole community wants, which was true in Athens."},
   {"t":"open","key":"lotteryrec","q":"Athenians chose most officials by lottery instead of election. What is one advantage and one disadvantage of choosing leaders by lottery?","min":30,"rows":3,"rubric":["Advantage: fair chance for everyone, rich people can't buy power, prevents campaigning","Disadvantage: an unprepared or unskilled person might be chosen"],"model":"An advantage is that everyone gets an equal chance, so rich or famous people can't take over. A disadvantage is that someone who knows nothing about the job might be chosen."}]},
 "think": {
  "intro": "Use evidence. Your teacher scores these.",
  "items": [
   {"t":"open","key":"democracyjudge","q":"Some people call Athens the \"birthplace of democracy.\" Others say a government where most residents could not vote was not really a democracy. Take a position, support it with at least two pieces of evidence, and answer the other side.","min":100,"rows":8,"rubric":["A clear position","At least two pieces of evidence (Assembly, lottery, juries, Pericles' words; or exclusion of women, enslaved people, foreigners)","Acknowledges the other view","Considers how democracy has grown since"],"model":"Athens deserves credit as an early democracy, but it was a limited one. Citizen men voted directly on laws in the Assembly and were chosen by lottery for offices and juries, which gave ordinary men real power for the first time. Critics are right that women, enslaved people and foreigners, most of the population, had no voice. Still, Athens planted an idea, rule by the people, that later generations widened. The United States itself took until 1920 for women's suffrage, 1924 for citizenship for Indigenous Peoples, and 1965 to protect Black citizens' votes, so democracy is something that grows."},
   {"t":"open","key":"persiawon","q":"Imagine the Persians had won at Salamis in 480 BCE. Using what you learned about how Persia ruled conquered peoples last week, predict what might have happened to Athens. Would its democracy have survived? Explain your reasoning.","min":80,"rows":6,"rubric":["Uses accurate Persian policies (satraps, tribute, tolerance of local customs, revolts punished)","A reasoned prediction about Athens' government and culture","Acknowledges uncertainty"],"model":"Athens would probably have become part of a satrapy and paid tribute. Persia often let peoples keep their religions and customs, so Greek gods, language and festivals might have continued. But Athens had helped the Ionian Revolt and burned Sardis, so Persia might have punished it, and a Persian-appointed ruler would likely have replaced the Assembly. Democracy might not have survived, though we can't know for sure."}]},
 "exit": [
  {"t":"text","q":"Which city-state made every citizen man a soldier and was ruled by two kings?","a":[{"all":[["sparta"]],"none":["not"]}],"show":"Sparta","pts":2,"why":"Athens was a democracy."},
  {"t":"text","q":"In which year BCE was the Battle of Marathon?","a":[{"all":[["490"]],"none":["not"]}],"show":"490 BCE","pts":2,"why":"Darius's army was defeated."},
  {"t":"text","q":"Which city, founded by Alexander the Great in Egypt, became the center of Hellenistic learning?","a":[{"all":[["alexandria"]],"none":["not"]}],"show":"Alexandria","pts":2,"why":"Home of the great Library."},
  {"t":"open","key":"exit_limit","q":"Name one group that could not vote in Athenian democracy, and explain why that matters.","min":12,"rows":2,"rubric":["A correct group (women, enslaved people, foreign-born residents)","Why it matters (most people had no voice; the democracy was limited)"],"model":"Women could not vote, so about half the people had no say in laws that affected them."}],
 "next": "Week 18: Rome, from republic to empire."
}

TEACHER = {
 "standards": [
  "SS.6.W.3.4: Explain the causes and effects of the Persian and Peloponnesian Wars.",
  "SS.6.W.3.3: Compare life in Athens and Sparta (government and the status of citizens, women and children, foreigners, helots).",
  "SS.6.W.3.2: Explain the democratic concepts (polis, civic participation and voting rights, legislative bodies, written constitutions, rule of law) developed in ancient Greece.",
  "SS.6.W.3.5: Summarize the important achievements and contributions of ancient Greek civilization.",
  "SS.6.G.2.1: Explain how major physical characteristics, natural resources, climate, and absolute and relative locations have influenced settlement, interactions, and the economies of ancient civilizations of the world.",
  "SS.6.W.1.3: Interpret primary and secondary sources."],
 "materials": ["The interactive lesson", "A bag or bowl, paper slips, pencils", "Beans or pebbles in two colors, 2 cups, a timer", "Optional: broken flowerpot pieces (adult handles) or smooth stones and a marker", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 16 warm-up questions."],
  [5, "Hook", "Tell the Marathon story; compare the legend with Herodotus."],
  [10, "Geography", "Read the map; connect mountains and sea to city-states, trade and colonies."],
  [11, "Athens and Sparta", "Study the comparison chart; discuss helots and women's lives."],
  [12, "Democracy", "Read Pericles aloud; direct versus representative democracy; who was excluded."],
  [10, "Persian Wars and achievements", "Build the timeline; discuss Greek debts to Egypt and Alexandria."],
  [6, "Assign", "Draw lots for president; assign Assembly Day, Think Deeper and the Exit Check."]],
 "key_questions": ["How did geography shape Greek government?", "Who counted as a citizen, and who didn't?", "Is Pericles describing Athens as it was, or as he wanted it seen?", "How did older civilizations shape Greek ideas?"],
 "misconceptions": ["Greece was one country with one government.", "Everyone in Athens could vote.", "The Greeks invented civilization on their own.", "The marathon legend is proven history."],
 "support": ["Use a two-column Athens/Sparta organizer.", "Read Pericles one sentence at a time and paraphrase.", "Provide a timeline strip with dates filled in."],
 "challenge": ["Read more of Pericles' Funeral Oration (Thucydides 2.35-46) and find what he says about Athenian women.", "Research the kleroterion, the Athenian lottery machine."],
 "background": "<p>Dates: first recorded Olympiad 776 BCE (traditional); Cleisthenes' reforms about 508/507; Ionian Revolt 499-494; Marathon 490; Thermopylae and Salamis 480; Plataea 479; Peloponnesian War 431-404; Alexander enters Egypt 332/331 and founds Alexandria in 331. Herodotus 6.105-106 tells of Pheidippides running to Sparta; the run from Marathon to Athens appears in much later writers (Plutarch, Lucian). Herodotus 2.4 credits the Egyptians with the 365-day year, and 2.50 says the names of nearly all the gods came to Greece from Egypt. Estimates of Athenian citizens (adult men) in the 5th century range from about 30,000 to 60,000, of a total population of perhaps 250,000 to 300,000; estimates of the enslaved share vary widely. The Pericles excerpt follows Crawley's 1874 translation (Project Gutenberg) with British spellings kept and glossed; the omitted words include a phrase the Gutenberg text prints as \"if no social standing\" (a misprint for \"if to social standing\").</p>",
 "sources": ["Thucydides, History of the Peloponnesian War, translated by Richard Crawley (1874), Project Gutenberg.", "Herodotus, The Histories (Books 2 and 6).", "Stoa of Attalos and Agora Excavations, American School of Classical Studies at Athens, materials on ostraka and the kleroterion.", "Pomeroy, Burstein, Donlan and Roberts, Ancient Greece: A Political, Social, and Cultural History."]
}

PRINT = {
 "directions": "Answer in complete sentences.",
 "items": [
  {"q":"How did Greece's geography lead to independent city-states?","a":"Mountains separated communities into valleys, so each formed its own polis with its own government.","lines":2},
  {"q":"Compare Athens and Sparta in government and in the lives of women.","a":"Athens: direct democracy; women had few rights. Sparta: two kings, council and assembly; women could own land and trained for fitness.","lines":3},
  {"q":"Describe two ways Athenian democracy worked and one way it was limited.","a":"Citizens voted in the Assembly; officials chosen by lottery; ostracism. Limited: only adult citizen men could vote.","lines":3},
  {"q":"Explain one cause and two effects of the Persian Wars.","a":"Cause: Athens helped the Ionian Revolt. Effects: Greek independence, Athens' rise as a sea power, later the Peloponnesian War.","lines":3},
  {"q":"Name three Greek achievements.","a":"Philosophy (Socrates, Plato, Aristotle), mathematics (Euclid), medicine (Hippocrates), theater, the Parthenon, democracy.","lines":2},
  {"q":"What did Herodotus say the Greeks learned from Egypt?","a":"The 365-day calendar and the names of many gods.","lines":2}]
}
