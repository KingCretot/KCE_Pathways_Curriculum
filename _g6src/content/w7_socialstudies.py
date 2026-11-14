from geo import NILE, BLUE_NILE

def roots():
    k = 11.0
    P = lambda lon, lat: (round((lon - 18) * k + 20, 1), round((33 - lat) * k + 34, 1))
    pts = lambda L: ' '.join('%s,%s' % P(*p) for p in L)
    mapw = 26 * k; W = int(mapw + 40 + 190); H = int(28 * k + 50)
    s = (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Map of the Nile Valley, Nubia and the eastern Sahara">'
         f'<text x="{W/2}" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Kemet\'s African neighborhood</text>'
         f'<rect x="20" y="34" width="{mapw}" height="{28*k}" fill="#efe1bd"/>')
    s += f'<polygon points="{pts([(18,33),(44,33),(44,31.4),(34.2,31.2),(32,31.5),(30,31.6),(25,31.8),(20,32.3),(18,31.5)])}" fill="#bcd9ef"/>'
    west = [(32.6,29.9),(33.6,27.5),(35.4,24),(37.2,21),(38.6,18),(39.7,15.5),(41.5,13.3),(43,12.5)]
    east = [(44,12.6),(44,14.5),(41.2,17.5),(39.6,20.5),(38,24),(36.2,27),(34.9,29.5)]
    s += f'<polygon points="{pts(west + east)}" fill="#bcd9ef"/>'
    s += f'<text x="{P(23.5,26)[0]}" y="{P(23.5,26)[1]}" text-anchor="middle" font-size="13" fill="#8a6d1f" font-style="italic">Eastern Sahara</text><text x="{P(23.5,25)[0]}" y="{P(23.5,25)[1]}" text-anchor="middle" font-size="10" fill="#8a6d1f">green and wet about</text><text x="{P(23.5,24.1)[0]}" y="{P(23.5,24.1)[1]}" text-anchor="middle" font-size="10" fill="#8a6d1f">10,000 to 5,000 years ago</text>'
    s += f'<polyline points="{pts(NILE[2:])}" fill="none" stroke="#0047BA" stroke-width="3"/><polyline points="{pts(BLUE_NILE)}" fill="none" stroke="#0047BA" stroke-width="3"/>'
    marks = [(31.2, 29.85, 'Memphis'), (32.8, 25.1, 'Hierakonpolis'), (32.9, 24.1, 'Aswan'), (30.7, 22.5, 'Nabta Playa'), (31.6, 21.0, 'Lower Nubia'), (30.4, 19.6, 'Kerma'), (32.5, 15.6, 'Khartoum'), (37.3, 12.0, 'Ethiopian Highlands')]
    lx = mapw + 34; last = -99
    for lon, lat, lab in marks:
        x, y = P(lon, lat); ly = max(y, last + 17); last = ly
        s += f'<circle cx="{x}" cy="{y}" r="4" fill="#DB2F30" stroke="#fff"/><path d="M{x+4} {y} L{lx-4} {ly}" stroke="#8a8f99" stroke-width=".8"/><text x="{lx}" y="{ly+4}" font-size="11">{lab}</text>'
    s += (f'<text x="{P(33.5,27)[0]}" y="{P(33.5,27)[1]}" font-weight="bold" fill="#0A1F3D" font-size="11" style="paint-order:stroke;stroke:#efe1bd;stroke-width:4">KEMET</text>'
          f'<text x="{P(33.2,19)[0]}" y="{P(33.2,19)[1]}" font-weight="bold" fill="#5b4a1c" font-size="11" style="paint-order:stroke;stroke:#efe1bd;stroke-width:4">NUBIA</text></svg>')
    return s

ROOTS = roots()

def evidence():
    cats = [("Geography", "Egypt is in Africa. Its river, its flood and its first kings came from the south.", "#0047BA"),
            ("Archaeology", "Early Nile cultures shared pottery, cattle traditions and burial customs with Nubia and the Sahara.", "#0A1F3D"),
            ("Culture", "Divine kingship, headrests and cattle goddesses connect Kemet to many African societies.", "#C9A84C"),
            ("Language", "Egyptian belongs to the Afroasiatic family; many linguists place its origin in Africa.", "#DB2F30"),
            ("Written sources", "Egyptians called themselves the people of Kemet. A Greek visitor described them as dark-skinned.", "#0047BA"),
            ("Biology", "Early southern skeletons resemble Saharan and tropical Africans. Ancient DNA: mostly North African.", "#0A1F3D")]
    s = ('<svg viewBox="0 0 560 300" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Six kinds of evidence">'
         '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Six kinds of evidence that Kemet was African</text>')
    for i, (t, d, c) in enumerate(cats):
        x, y = 12 + (i % 3) * 182, 34 + (i // 3) * 132
        s += f'<rect x="{x}" y="{y}" width="172" height="122" rx="10" fill="{c}"/><text x="{x+86}" y="{y+24}" text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">{t}</text>'
        words, line, lines = d.split(), '', []
        for w in words:
            if len(line + ' ' + w) > 27: lines.append(line); line = w
            else: line = (line + ' ' + w).strip()
        lines.append(line)
        for j, l in enumerate(lines):
            s += f'<text x="{x+86}" y="{y+46+j*15}" text-anchor="middle" fill="#fff">{l}</text>'
    return s + '</svg>'

TIMELINE = ('<svg viewBox="0 0 560 200" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="How Egypt was separated from Africa in European thinking and how scholars responded">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">How Egypt was pulled out of Africa, and put back</text>'
  '<line x1="30" y1="90" x2="530" y2="90" stroke="#0A1F3D" stroke-width="3"/>'
  + ''.join(f'<circle cx="{x}" cy="90" r="8" fill="{c}"/><text x="{x}" y="70" text-anchor="middle" font-weight="bold" font-size="12">{y}</text>'
            + ''.join(f'<text x="{x}" y="{114+j*14}" text-anchor="middle">{t}</text>' for j, t in enumerate(lines))
            for x, y, c, lines in [(60, "about 450 BCE", "#C9A84C", ["Herodotus calls", "Egyptians dark-", "skinned"]),
                                   (165, "1820s", "#DB2F30", ["Hegel claims Egypt", "does not belong to", "\"the African spirit\""]),
                                   (275, "1800s-1900s", "#DB2F30", ["Race theories claim", "outsiders brought", "civilization"]),
                                   (385, "1954 and 1974", "#0047BA", ["Diop and Obenga", "argue Egypt was", "African"]),
                                   (490, "today", "#0047BA", ["Most scholars:", "Kemet grew from", "African roots"])]) + '</svg>')

LESSON = {
 "unit": "Unit 2: The Nile Valley and Ancient Africa",
 "title": "Kemet as an African Civilization",
 "subtitle": "For two centuries, some writers tried to separate ancient Egypt from Africa. The evidence puts it right back where it belongs.",
 "objectives": [
  "Use six kinds of evidence to explain why Kemet was an African civilization.",
  "Explain how the ancient Egyptians described themselves and how a Greek visitor described them.",
  "Describe how European writers in the 1800s and 1900s separated Egypt from Africa, and why those ideas were wrong.",
  "Explain the work of Cheikh Anta Diop and Théophile Obenga.",
  "Evaluate evidence carefully, including what DNA can and cannot tell us."],
 "vocab": [
  ["civilization", "A complex society with cities, government, writing, specialized jobs and shared beliefs."],
  ["evidence", "Information that helps prove or disprove a claim."],
  ["divine kingship", "The belief that a ruler is sacred or connected to the gods."],
  ["Afroasiatic", "A large language family that includes ancient Egyptian, Amazigh (Berber), Hausa, Somali, Amharic, Arabic and Hebrew."],
  ["bias", "A one-sided view that leads someone to favor or ignore certain evidence."],
  ["racism", "The false belief that some groups of people are better than others because of their race, and the unfair treatment that follows."],
  ["Eurocentric", "Viewing history and the world mainly from a European point of view."],
  ["ancestry", "The people a person is descended from."]],
 "reconnect": {
  "title": "Week 6: the Nile and the rise of Kemet",
  "intro": "This week's evidence builds directly on last week's geography and history.",
  "items": [
   {"t":"blanks","q":"Complete the sentence.","sent":"Upper Egypt is in the ___, and Egypt was unified by a ruler from Upper Egypt named ___.","blanks":[["south"],["narmer"]],"pts":3,"why":"Upper Egypt is upstream (south). Narmer, from the south, is believed to have united Egypt around 3100 BCE."},
   {"t":"text","q":"What did the Egyptians call their country, and what does the name mean?","a":[{"all":[["kemet","kmt"],["black"]]}],"show":"Kemet, the Black Land","pts":2,"why":"Kemet means the Black Land."},
   {"t":"open","key":"rc_ethiopia","q":"Explain why the Nile flood depended on Ethiopia.","min":15,"rows":2,"rubric":["Monsoon rains in the Ethiopian Highlands","Fed the Blue Nile, which caused most of the flood"],"model":"Heavy summer rains in the Ethiopian Highlands filled the Blue Nile, which brought most of the floodwater and silt north to Egypt."},
   {"t":"open","key":"rc_sahara","q":"How did the drying of the Sahara help shape early Egypt?","min":15,"rows":2,"rubric":["Herders and farmers moved from the Sahara toward the Nile","They brought traditions that helped form Nile cultures"],"model":"As the Sahara dried, herders and farmers moved toward the Nile Valley for water, bringing their cattle, pottery and customs, which helped form the early cultures of Upper Egypt."}]},
 "hook": {
  "title": "Who Gets to Tell the Story?",
  "visual": TIMELINE,
  "html": "<p>Open many older textbooks, movies or museum displays and you will see ancient Egypt shown almost as if it were part of Europe or the Middle East, with the rest of Africa left out. In the 1820s, the German philosopher Georg Hegel claimed that Egypt did not belong to what he called \"the African spirit.\" In the 1800s and early 1900s, other writers invented race theories claiming that a lighter-skinned people from outside Africa must have brought civilization to the Nile.</p><p>Those claims were not based on evidence. They came from <b>racism</b>: the false belief that Black Africans could not have built pyramids, invented writing or run a great kingdom.</p><div class='callout'><b>Big idea:</b> Kemet was an African civilization, built by Africans along an African river. Historians prove this the same way they prove anything: with evidence.</div>"},
 "learn": [
  {"title": "Kemet's African Roots",
   "visual": ROOTS,
   "html": "<p><b>Geography.</b> Egypt is in Africa. Its water came from Central and East Africa, and its unification came from the south.</p><p><b>Archaeology.</b> The earliest farming cultures of Upper Egypt, the Badarian and Naqada, shared black-topped pottery, cattle herding and burial customs with peoples of Lower Nubia and the eastern Sahara. Archaeologists such as Maria Gatto and Stuart Tyson Smith describe these cultures as closely related, with roots in the Saharan wet period. Cattle were so important that the goddess Hathor was often shown as a cow or with cow horns.</p><p><b>Culture.</b> Kemet shared customs with many African societies: a sacred, divine king who kept the world in balance; wooden headrests used as pillows (still used in parts of East Africa); and ceremonies honoring cattle and ancestors.</p><p><b>Language.</b> Ancient Egyptian belongs to the Afroasiatic language family, along with Amazigh (Berber), Hausa, Somali and Amharic, as well as Arabic and Hebrew. Most branches of this family are spoken in Africa, and many linguists, such as Christopher Ehret, place its origin in Africa.</p>",
   "checks": [
    {"t":"open","key":"pottery","q":"Explain how pottery and cattle traditions help show that early Egypt grew from African roots.","min":20,"rows":3,"rubric":["Early Upper Egyptian cultures shared pottery and cattle traditions with Nubia and the Sahara","Shared traditions suggest shared origins and contact"],"model":"The earliest cultures of Upper Egypt made the same kind of black-topped pottery and herded cattle like the peoples of Nubia and the eastern Sahara. Sharing these traditions shows they came from the same African roots and were connected."},
    {"t":"blanks","q":"Name two African languages in the same language family as ancient Egyptian.","sent":"___ and ___","blanks":[["amazigh","berber","hausa","somali","amharic","oromo","tigrinya","coptic"],["amazigh","berber","hausa","somali","amharic","oromo","tigrinya","coptic"]],"distinct":True,"show":"For example: Hausa and Somali","pts":2,"why":"Afroasiatic includes Amazigh (Berber), Hausa, Somali, Amharic and others, as well as Arabic and Hebrew."},
    {"t":"open","key":"headrest","q":"Wooden headrests used as pillows are found in ancient Egyptian tombs and are still used in parts of East Africa today. What could this connection suggest, and why is one object alone not enough to prove it?","min":25,"rows":3,"rubric":["Suggests a shared cultural tradition across Africa","Explains one object could be a coincidence; historians need many kinds of evidence"],"model":"It suggests that Egypt and East Africa shared a cultural tradition that lasted thousands of years. But one object alone could be a coincidence, so historians look for many kinds of evidence, like pottery, language and beliefs, that all point the same way."}]},
  {"title": "What the Ancient Sources Say",
   "html": "<p>The Egyptians called themselves <i>remetch en Kemet</i>, \"the people of the Black Land.\" They also lived next to Nubia for thousands of years, trading, fighting, intermarrying and sometimes ruling one another.</p><p>The Greek historian <b>Herodotus</b> visited Egypt around 450 BCE. In his <i>Histories</i> (Book 2), arguing that a people called the Colchians were descended from Egyptian soldiers, he wrote that they were \"dark-skinned and woolly-haired\" like the Egyptians. He added that this alone proved little, since other peoples looked that way too.</p><p><b>Egyptian art</b> showed people in many shades. By custom, artists often painted men a reddish brown and women a lighter yellow, so art colors were partly symbolic. Paintings also show Nubians, Libyans and people from Southwest Asia with different features and clothing. The population itself varied: darker in the south near Nubia and lighter in parts of the north, as it still is along the Nile today.</p>",
   "checks": [
    {"t":"text","q":"What did the ancient Egyptians call themselves?","a":[{"all":[["remetch","people"],["kemet","black land"]]}],"show":"remetch en Kemet, the people of the Black Land","pts":2,"why":"They called themselves the people of Kemet, the Black Land."},
    {"t":"open","key":"herodotus","q":"Herodotus described Egyptians as dark-skinned. Is he a primary source for what Egyptians looked like? Give one strength and one weakness of his evidence.","min":30,"rows":3,"rubric":["Yes, an eyewitness who visited Egypt","Strength: he saw Egyptians in person","Weakness: one outsider's view, made while arguing about another people, possibly with his own biases; he himself said appearance proved little"],"model":"Yes, he is a primary source because he visited Egypt and saw people himself. A strength is that he is an eyewitness. A weakness is that he was one foreign visitor making an argument about the Colchians, and he admitted appearance alone proves little, so historians compare him with other evidence."},
    {"t":"open","key":"artcolor","q":"Egyptian artists usually painted men reddish brown and women light yellow. Why does this mean we should be careful using paint colors alone to decide what Egyptians looked like?","min":20,"rows":3,"rubric":["Colors followed artistic custom or symbolism, not exact skin tone","Need other evidence too"],"model":"The colors followed an artistic custom, so they were partly symbolic instead of exact skin tones. Real people varied, so we need other evidence, like skeletons and written descriptions, along with the art."}]},
  {"title": "Pulling Egypt Out of Africa",
   "html": "<p>Ancient Greeks and Romans had no doubt that Egypt was part of Africa. The idea that it was not came much later, during the era of European colonialism and the transatlantic slave trade.</p><ul><li><b>Hegel (1820s)</b> divided Africa into parts and claimed that Egypt belonged to a world outside \"Africa proper.\"</li><li><b>The Hamitic theory</b> claimed that lighter-skinned outsiders, not Black Africans, brought every achievement in Africa. It was used to justify colonial rule and is now completely rejected by scholars.</li><li><b>The \"dynastic race\" theory</b> claimed a foreign master race invaded and founded Egypt's dynasties. Archaeology has shown Egyptian civilization grew gradually inside the Nile Valley, so this theory has been abandoned.</li></ul><p>These ideas spread because they supported a racist picture of the world, not because the evidence supported them.</p>",
   "checks": [
    {"t":"open","key":"whysplit","q":"Why would writers during the era of colonialism and slavery want to separate Egypt from the rest of Africa? Explain the connection.","min":30,"rows":3,"rubric":["Colonizers and enslavers claimed Africans could not build civilizations","Egypt's achievements contradicted that claim, so they separated Egypt from Africa","Connects bias to how history was written"],"model":"Colonizers and enslavers claimed Africans had no history and could not build civilizations, which they used to excuse taking land and enslaving people. Egypt's pyramids and writing proved that claim wrong, so some writers separated Egypt from Africa instead of admitting it."},
    {"t":"open","key":"hamitic","q":"In your own words, what was the Hamitic theory, and what does evidence show instead?","min":25,"rows":3,"rubric":["Claimed lighter-skinned outsiders brought achievements to Africa","Evidence shows African civilizations developed from African roots; the theory is rejected"],"model":"The Hamitic theory claimed that lighter-skinned people from outside Africa brought every great achievement to the continent. Evidence from archaeology, language and history shows that civilizations like Kemet grew from African roots, so scholars reject the theory."}]},
  {"title": "Putting Egypt Back: Diop, Obenga and the Evidence Today",
   "visual": evidence(),
   "html": "<p><b>Cheikh Anta Diop</b> (1923 to 1986), a Senegalese historian, anthropologist and physicist, argued in his 1954 book <i>Nations nègres et culture</i> that ancient Egypt was a Black African civilization. At a 1974 UNESCO symposium in Cairo, he and the Congolese scholar <b>Théophile Obenga</b> presented evidence from language, culture and biology. The symposium report praised their contributions as painstakingly researched. Not every expert agreed with all of Diop's conclusions, and some of his methods are debated, but his work forced Egyptology to take Egypt's African roots seriously. The University of Dakar is now named Cheikh Anta Diop University.</p><p><b>Modern science</b> adds evidence. Studies of skeletons from early southern Egypt, by scientists such as S. O. Y. Keita, find they resemble other Saharan and tropical African populations. In 2025, scientists sequenced the first complete genome of an ancient Egyptian, a man who lived about 4,500 to 4,800 years ago. Most of his ancestry was North African, and about one fifth came from the eastern Fertile Crescent, showing Egypt was also a crossroads. The scientists cautioned that one person cannot represent a whole population.</p><p>Applying today's race labels to ancient people is tricky, because the Egyptians did not think in modern categories. But one thing is not in doubt: <b>the ancient Egyptians were Africans</b>, a varied African people who built their civilization in Africa and traded with neighbors in every direction.</p>",
   "checks": [
    {"t":"open","key":"diop","q":"Who was Cheikh Anta Diop, and why is his work important even though not every expert agreed with every conclusion?","min":30,"rows":3,"rubric":["Senegalese historian and scientist who argued Egypt was a Black African civilization","His evidence (1954 book, 1974 UNESCO symposium) forced scholars to take Egypt's African roots seriously","Recognizes that debate is normal in scholarship"],"model":"Cheikh Anta Diop was a Senegalese historian and scientist who argued that ancient Egypt was a Black African civilization. Even though some experts disagreed with parts of his work, his carefully researched evidence, shown at the 1974 UNESCO symposium, forced scholars to stop separating Egypt from Africa and to study its African roots."},
    {"t":"open","key":"dna","q":"The 2025 genome came from one man. Explain why scientists said his DNA cannot represent all ancient Egyptians, and what this teaches about using evidence.","min":25,"rows":3,"rubric":["One person out of millions over 3,000 years and different regions","Need many samples; avoid overgeneralizing from one piece of evidence"],"model":"He was one person from one place and one time, but millions of people lived in Egypt over 3,000 years, and people in the south and north differed. Scientists need many samples before making conclusions, so we should not overgeneralize from a single piece of evidence."},
    {"t":"open","key":"sixkinds","q":"Look at the six kinds of evidence. Which kind do you find most convincing that Kemet was an African civilization, and why?","min":25,"rows":3,"rubric":["Chooses a kind of evidence","Explains why it is convincing with specifics"],"model":"Archaeology is most convincing to me, because pottery, cattle bones and burials are physical evidence that shows the early Nile cultures were closely related to Nubia and the Sahara, without depending on one writer's opinion."}]}],
 "handson": {
  "title": "Build an Evidence Wall",
  "intro": "Historians build arguments the way builders build walls: one piece of evidence at a time. Build yours on a wall, a door or a large poster.",
  "materials": ["12 or more sticky notes or index cards and tape", "Markers in two colors", "A wall, door or poster board", "A world map or a printed map of Africa"],
  "steps": [
   "Write the claim at the top: Kemet was an African civilization.",
   "Make six column headers: Geography, Archaeology, Culture, Language, Written sources, Biology.",
   "Write each piece of evidence from the lesson on its own card and place it in the right column. Aim for at least two cards per column.",
   "In a second color, add a card for any evidence that is limited or debated (for example, one genome, or art colors that were symbolic), and place it beside the evidence it limits.",
   "Present your wall to a family member in 3 minutes. Ask them which card convinced them most."],
  "record": [
   {"t":"open","key":"wall","q":"Type the cards from your evidence wall, column by column, including your limit cards.","min":80,"rows":10,"rubric":["Six columns, at least two cards each","Accurate evidence from the lesson","At least two limit cards that explain weaknesses"],"model":"Geography: Egypt is in Africa; unification came from the south. Archaeology: Badarian and Naqada pottery like Nubia's; cattle herding. Culture: divine kingship; headrests; Hathor as a cow. Language: Egyptian is Afroasiatic; related to Hausa and Somali. Written sources: Egyptians called themselves people of Kemet; Herodotus said dark-skinned. Biology: early southern skeletons resemble Saharan and tropical Africans; 2025 genome mostly North African. Limit cards: Herodotus was one outsider; art colors were symbolic; the genome is only one person."},
   {"t":"open","key":"walltalk","q":"Which card did your family member find most convincing, and what question did they ask? How did you answer?","min":25,"rows":3,"rubric":["Reports the listener's choice","Reports a question and an evidence-based answer"],"model":"My dad thought the pottery and cattle card was most convincing. He asked why movies show Egyptians as European. I explained that writers in the 1800s separated Egypt from Africa because of racism, and that the evidence shows Egyptians were Africans."}]},
 "think": {
  "intro": "Write an evidence-based argument. Your teacher scores these.",
  "items": [
   {"t":"open","key":"argument","q":"Write a paragraph arguing that ancient Kemet was an African civilization. Use at least four pieces of evidence from at least three different kinds (geography, archaeology, culture, language, written sources, biology). Then explain why some writers in the past claimed otherwise and why they were wrong.","min":150,"rows":14,"rubric":["Clear claim","Four or more accurate pieces of evidence from three or more kinds","Explains the history of the opposing claims (Hegel, Hamitic theory, dynastic race theory)","Explains why those claims were wrong (racism, no evidence)","Organized, with a conclusion"],"model":"Ancient Kemet was an African civilization, built by Africans along an African river. Geographically, Egypt is in Africa: the Nile's water came from Central and East Africa, and the kingdom was united by Narmer, a ruler from the south. Archaeologists have found that the earliest Upper Egyptian cultures, the Badarian and Naqada, made the same black-topped pottery and herded cattle like their neighbors in Nubia and the Sahara. Culturally, Kemet shared divine kingship and wooden headrests with many African societies. Its language belonged to the Afroasiatic family, along with Hausa and Somali. Even the Egyptians' name for themselves, the people of Kemet, and Herodotus's description of them as dark-skinned point to an African people. In the 1800s, writers like Hegel and the creators of the Hamitic theory claimed that civilization must have come from outside Africa. They had no evidence; they were defending a racist view of the world that was used to justify colonialism and slavery. When historians follow the evidence instead of prejudice, Kemet stands where it always stood: in Africa."},
   {"t":"open","key":"media","q":"A movie about ancient Egypt casts only actors of European descent as the pharaoh and his family. Using this week's evidence, write a short, respectful letter to the filmmakers explaining what is inaccurate and what you would suggest.","min":70,"rows":7,"rubric":["Respectful tone and letter format","Explains with evidence why the casting misrepresents Egyptians","Offers a constructive suggestion","Acknowledges Egypt's variety without erasing its African identity"],"model":"Dear Filmmakers, I enjoyed seeing ancient Egypt on screen, but your casting gives viewers a false picture. The ancient Egyptians were Africans: their kingdom was united from the south, their early cultures were closely related to Nubia and the Sahara, and a Greek visitor described them as dark-skinned. Showing only actors of European descent repeats an idea from the 1800s that separated Egypt from Africa. I suggest casting actors who reflect the people of the Nile Valley and Nubia, and working with Egyptian and African historians. Thank you for considering this. Sincerely, a Grade 6 historian"}]},
 "exit": [
  {"t":"open","key":"exit_claim","q":"Give two different kinds of evidence that Kemet was an African civilization.","min":15,"rows":2,"rubric":["Two accurate pieces of evidence from two different kinds"],"model":"Archaeology: early Upper Egyptian pottery and cattle traditions match Nubia and the Sahara. Language: Egyptian is in the Afroasiatic family with Hausa and Somali."},
  {"t":"text","q":"Which Senegalese scholar argued that ancient Egypt was a Black African civilization and presented evidence at the 1974 UNESCO symposium?","a":["cheikh anta diop","diop","anta diop"],"show":"Cheikh Anta Diop","pts":2,"why":"Cheikh Anta Diop, with Théophile Obenga."},
  {"t":"open","key":"exit_hamitic","q":"Why do historians reject the Hamitic theory?","min":12,"rows":2,"rubric":["It was based on racism, not evidence","Evidence shows African civilizations grew from African roots"],"model":"Because it was based on racist ideas, not evidence. Archaeology and language show that civilizations like Kemet grew from African roots."},
  {"t":"text","q":"In the 2025 genome study, where did most of the ancient Egyptian man's ancestry come from?","a":[{"all":[["north africa","north african","africa"]]}],"show":"North Africa","pts":2,"why":"About four fifths of his ancestry was North African; about one fifth came from the eastern Fertile Crescent."},
  {"t":"open","key":"exit_limit","q":"Name one limit of the evidence about what ancient Egyptians looked like.","min":10,"rows":2,"rubric":["A real limit (art colors were symbolic; Herodotus was one outsider; one genome)"],"model":"Egyptian art colors followed a custom, so paint alone does not show exact skin tones."}],
 "next": "Week 8: Nubia and the Kingdom of Kush, Kemet's powerful neighbor to the south, with its own kings, queens, pyramids and gold."
}

TEACHER = {
 "standards": [
  "SS.6.W.2.5: Summarize important achievements of Egyptian civilization.",
  "SS.6.W.1.5: Describe the roles of historians and recognize varying historical interpretations (historiography).",
  "SS.6.W.1.3: Interpret primary and secondary sources.",
  "SS.6.G.2.4: Explain how the geographical location of ancient civilizations contributed to the culture and politics of those societies.",
  "C3 Framework D2.His.6.6-8: Analyze how people's perspectives influenced what information is available in the historical sources they created."],
 "materials": ["The interactive lesson", "Sticky notes or index cards in two colors", "A map of Africa", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 6 Reconnect questions."],
  [8, "Hook", "Show the timeline. Ask: why would anyone want to separate Egypt from Africa?"],
  [12, "African roots", "Use the map. Discuss archaeology, culture and language as evidence."],
  [10, "Ancient sources", "Read the Herodotus passage and discuss art conventions as evidence with limits."],
  [10, "Pulling Egypt out", "Explain Hegel, the Hamitic theory and the dynastic race theory, and the racism behind them."],
  [10, "Putting Egypt back", "Introduce Diop and Obenga, modern skeletal and DNA evidence, and its limits."],
  [4, "Assign", "Assign the Evidence Wall, Think Deeper and the Exit Check."]],
 "key_questions": ["What kind of evidence is this, and how strong is it?", "Whose perspective shaped this source?", "Why did false ideas spread even without evidence?", "What can one genome tell us, and what can't it?"],
 "misconceptions": ["Picturing ancient Egypt as part of Europe or the Middle East rather than Africa.", "Believing outsiders brought civilization to Africa.", "Treating Egyptian paint colors as exact skin tones.", "Overgeneralizing from a single DNA sample, in either direction.", "Assuming all ancient Egyptians looked exactly alike."],
 "support": ["Provide the six evidence categories as a printed organizer.", "Give sentence frames for the argument: One piece of evidence is... This shows... Some writers claimed... However...", "Let the student talk through the Evidence Wall before writing."],
 "challenge": ["Read a short excerpt from Diop's The African Origin of Civilization (1974 English translation) and summarize one argument.", "Research the Seventeenth Dynasty king Seqenenre Tao or the Twelfth Dynasty, whose rulers came from the far south, and report what the evidence shows."],
 "background": "<p>This lesson follows Jonathan's rule that Kemet is taught as an African civilization with the true story of Africans in Egypt. It presents the mainstream archaeological view that Egyptian civilization developed indigenously in the Nile Valley with strong Saharan and Nubian connections (Gatto; Smith 2018; Wengrow), the historiography of racist separation (Hegel's Lectures on the Philosophy of World History; the Hamitic hypothesis; Petrie's dynastic race theory), Diop's Nations nègres et culture (1954) and the 1974 UNESCO Cairo symposium (where the rapporteur called Diop's and Obenga's contributions painstakingly researched, while many participants disagreed with parts of their conclusions), Keita's craniometric work describing predynastic southern Egyptians as a Saharo-tropical African variant, and the 2025 Nature genome from Nuwayrat (Morez Jacobs et al.; radiocarbon dated about 2855 to 2570 BCE; about 80 percent North African Neolithic ancestry and about 20 percent eastern Fertile Crescent ancestry; the authors caution that one individual may not represent the population). Herodotus 2.104 (Godley translation) describes the Colchians as \"dark-skinned and woolly-haired\" in comparing them with Egyptians. Egyptian art conventions (reddish-brown men, yellow women) are partly symbolic. The lesson avoids imposing modern racial categories while stating clearly that the ancient Egyptians were Africans.</p>",
 "sources": ["UNESCO General History of Africa, Volume II, including the report of the 1974 Cairo symposium.", "Diop, C. A. (1974), The African Origin of Civilization: Myth or Reality.", "Morez Jacobs, A. et al. (2025), Whole-genome ancestry of an Old Kingdom Egyptian, Nature 644.", "Herodotus, Histories 2.104 (trans. A. D. Godley, Loeb Classical Library).", "Smith, S. T. (2018), Ethnicity: constructions of self and other in ancient Egypt, Journal of Egyptian History.", "Keita, S. O. Y. (1990, 1993), studies of early Nile Valley crania."]
}

PRINT = {
 "directions": "Use complete sentences and specific evidence.",
 "items": [
  {"q":"Name the six kinds of evidence from this lesson and give one example of two of them.","a":"Geography, archaeology, culture, language, written sources, biology. For example: archaeology, black-topped pottery like Nubia's; language, Egyptian is Afroasiatic with Hausa.","lines":3},
  {"q":"What did the ancient Egyptians call themselves?","a":"remetch en Kemet, the people of the Black Land","lines":1},
  {"q":"Explain what Hegel and the Hamitic theory claimed, and why historians reject those claims.","a":"They claimed Egypt was not truly African and that outsiders brought civilization; historians reject them because they were based on racism, not evidence.","lines":3},
  {"q":"Who was Cheikh Anta Diop, and what happened at the 1974 UNESCO symposium?","a":"A Senegalese historian and scientist who argued Egypt was a Black African civilization; he and Théophile Obenga presented evidence in Cairo, and their work was praised as painstakingly researched.","lines":3},
  {"q":"Give one strength and one limit of DNA evidence about ancient Egyptians.","a":"Strength: it shows real ancestry (the 2025 genome was mostly North African). Limit: one person cannot represent millions over 3,000 years.","lines":2},
  {"q":"Write a one-sentence claim about Kemet that you can support with evidence.","a":"For example: Kemet was an African civilization whose earliest cultures grew from the traditions of Nubia and the Sahara.","lines":2}]
}
