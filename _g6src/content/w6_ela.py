ARTICLE = '''<div class="card" style="border-left-color:#0047BA"><h3>A Wall Made of Trees</h3><p class="muted">An informational article by KingCretot Experience</p>
<p><b>(1)</b> South of the Sahara Desert lies the Sahel, a dry band of grassland that stretches across Africa from Senegal on the Atlantic Ocean to Djibouti near the Red Sea. More than 100 million people live there, and most of them depend on the land for food. But years of drought, overgrazing and cutting trees for firewood have turned large areas of farmland into dust. To fight back, African nations are growing a wall, not of stone, but of living plants.</p>
<p><b>(2)</b> In 2007, the African Union launched the Great Green Wall. The first plan was simple: plant a strip of trees about 15 kilometers wide and 8,000 kilometers long across the continent, like a giant green belt holding back the desert. The goal by 2030 is to restore 100 million hectares of damaged land, an area roughly the size of Egypt, and to create 10 million jobs.</p>
<p><b>(3)</b> Planting trees in a desert, however, turned out to be harder than it sounded. In some places, many young trees died because no one was paid to water or protect them. Leaders learned that a straight line of trees would not work everywhere. The project changed into a patchwork of farms, forests and grasslands, planned together with the people who live on the land.</p>
<p><b>(4)</b> Some of the most successful methods are old ones. In Niger and Burkina Faso, farmers protect tree stumps and roots that are already alive underground, letting them sprout again instead of planting new seedlings. Others dig half-moon-shaped pits called <i>zaï</i> that catch rain and compost so crops can grow in hard soil. These local methods cost little and help trees and crops grow side by side.</p>
<p><b>(5)</b> Progress has been uneven. By 2020, a United Nations review estimated that only about 18 million hectares, less than one fifth of the goal, had been restored. Ethiopia and Senegal have restored large areas, while war and lack of money have slowed work in other countries. Experts now say the 2030 goal will be very hard to reach.</p>
<p><b>(6)</b> Still, the Great Green Wall has changed how the world thinks about fighting the desert. It shows that land can heal when communities lead the work, combine traditional knowledge with science, and plan for the long run. As one lesson from the project puts it, a wall of trees can only grow as strong as the people who care for it.</p></div>'''

TABLE = ('<svg viewBox="0 0 560 210" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Central idea table diagram">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The central idea is the tabletop; details are the legs</text>'
  '<rect x="60" y="36" width="440" height="56" rx="6" fill="#0A1F3D"/><text x="280" y="60" text-anchor="middle" fill="#fff" font-weight="bold">CENTRAL IDEA</text><text x="280" y="78" text-anchor="middle" fill="#fff" font-size="11">What the whole text is mostly about, stated as a sentence</text>'
  + ''.join(f'<rect x="{x}" y="92" width="80" height="80" fill="{c}"/><text x="{x+40}" y="124" text-anchor="middle" fill="#fff" font-weight="bold" font-size="11">Detail {i+1}</text><text x="{x+40}" y="142" text-anchor="middle" fill="#fff" font-size="10">{t}</text>'
            for i, (x, c, t) in enumerate([(80, "#0047BA", "fact"), (240, "#C9A84C", "example"), (400, "#DB2F30", "statistic")])) +
  '<text x="280" y="198" text-anchor="middle" font-size="11">Take away a leg and the table wobbles. Every detail must hold up the central idea.</text></svg>')

LESSON = {
 "unit": "Unit 2: Explaining the World (Informational)",
 "title": "Central Idea and Supporting Details",
 "subtitle": "Every informational text has one big point. Strong readers find it and prove it. Strong writers build every paragraph to support it.",
 "objectives": [
  "Explain how informational texts differ from narratives.",
  "Determine the central idea of a text and state it as a complete sentence.",
  "Identify supporting details (facts, examples, statistics) and explain how each supports the central idea.",
  "Tell the difference between a topic, a central idea and a minor detail.",
  "Use the roots geo, terr, hydr and aqua, and write an informational paragraph with a central idea and support."],
 "vocab": [
  ["informational text", "Writing that explains real facts and ideas, such as articles, textbooks and reports."],
  ["topic", "The subject of a text, usually a word or phrase (the Great Green Wall)."],
  ["central idea", "The most important point the author makes about the topic, stated as a complete sentence."],
  ["supporting detail", "A fact, example, statistic, quotation or explanation that proves or develops the central idea."],
  ["minor detail", "Interesting information that does not directly support the central idea."],
  ["statistic", "A fact given as a number, such as 18 million hectares."],
  ["geo / terr", "Roots meaning earth or land: geography, geology, territory, terrain."],
  ["hydr / aqua", "Roots meaning water: hydrant, dehydrated, aquarium, aquatic."]],
 "reconnect": {
  "title": "Unit 1: narrative craft and theme",
  "intro": "Unit 2 switches from stories to real-world explaining. Notice what carries over and what changes.",
  "items": [
   {"t":"open","key":"rc_theme_ci","q":"In Unit 1 you wrote theme statements. How is a theme in a story like a central idea in an article, and how is it different?","min":25,"rows":3,"rubric":["Alike: both are the big message, stated as a complete sentence","Different: a theme is a lesson about life shown through characters; a central idea is the main point about a real topic"],"model":"Both are the big idea of the text, written as a complete sentence. But a theme is a lesson about life that the reader figures out from characters and events, while a central idea is the author's main point about a real topic, usually supported with facts."},
   {"t":"open","key":"rc_dialogue","q":"Name two narrative techniques from Unit 1 that you would NOT usually find in a news article, and explain why.","min":15,"rows":2,"rubric":["Two narrative techniques (dialogue between characters, a slowed-down climax, first-person reflection, sensory scene-building)","Reason: informational texts aim to explain facts clearly"],"model":"A slowed-down climax and invented dialogue, because an article's job is to explain real facts clearly, not to build suspense in a story."},
   {"t":"text","q":"Using roots from Unit 1, what does <b>biography</b> mean?","a":[{"all":[["life"],["writ","story","about","account"]]}],"show":"writing about a person's life","pts":2,"why":"bio (life) + graph (write)."}]},
 "hook": {
  "title": "Can You Grow a Wall?",
  "html": "<p>In Social Studies this week, you are learning how the drying of the Sahara pushed people toward the Nile thousands of years ago. The desert is still on the move today. Across the Sahel, African nations are trying something bold: growing a wall of trees across an entire continent.</p><p>Read the article below. As you read, ask yourself: <i>What is the one big point the author wants me to understand?</i></p>" + ARTICLE + "<div class='callout'><b>Big idea:</b> The topic is what a text is about. The central idea is what the author says about it.</div>"},
 "learn": [
  {"title": "Topic vs. Central Idea",
   "html": "<p>The <b>topic</b> of the article is the Great Green Wall. That is just a phrase. The <b>central idea</b> is a complete sentence that tells the author's most important point about the topic.</p><table class='t'><tr><th>Topic</th><th>Central idea</th></tr><tr><td>The Great Green Wall</td><td>The Great Green Wall shows that fighting the desert works best when communities lead and combine local knowledge with science, even though progress has been slow.</td></tr></table><p><b>Where to look:</b> the title, the first and last paragraphs, and ideas that come up again and again. The central idea is not just one fact; it is the point that most of the paragraphs support.</p>",
   "checks": [
    {"t":"open","key":"notci","q":"A student says the central idea is: \"The Great Green Wall was started in 2007.\" Explain why that is not the central idea.","min":15,"rows":2,"rubric":["It is a single fact or detail","Most of the article is not about the start date; the central idea must cover the whole text"],"model":"That is just one fact from paragraph 2. The article is mostly about how the project changed and what it teaches about healing land, so the start date is a supporting detail, not the central idea."},
    {"t":"text","q":"Which paragraph most directly states the article's big lesson? Type the paragraph number.","a":["6","paragraph 6","six"],"show":"6","pts":2,"why":"The last paragraph pulls the article together: land heals when communities lead the work and plan for the long run."},
    {"t":"open","key":"myci","q":"Write the central idea of the article in your own words in one complete sentence.","min":15,"rows":2,"rubric":["Complete sentence","Covers the whole article, not one detail","In the student's own words"],"model":"African countries are learning that the desert can be pushed back when local people lead the work and use both traditional methods and science, even though the project is far from finished."}]},
  {"title": "Supporting Details",
   "visual": TABLE,
   "html": "<p>Supporting details prove or explain the central idea. They come in several kinds:</p><ul><li><b>Facts:</b> The African Union launched the project in 2007.</li><li><b>Statistics:</b> about 18 million hectares restored by 2020.</li><li><b>Examples:</b> farmers in Niger letting old tree roots sprout again.</li><li><b>Explanations:</b> why a straight line of trees did not work everywhere.</li></ul><p>A <b>minor detail</b> is true but does not help prove the central idea, like the exact width of the first plan.</p>",
   "checks": [
    {"t":"open","key":"zai","q":"Explain how the detail about zaï pits in paragraph 4 supports the central idea.","min":20,"rows":3,"rubric":["Zaï pits are a traditional local method","Shows that local knowledge helps the land heal, which is the central idea"],"model":"Zaï pits are an old, low-cost method that local farmers use to catch rain and compost. This supports the central idea that the project works best when it uses local knowledge and communities lead the work."},
    {"t":"num","q":"About what fraction of the 100-million-hectare goal had been restored by 2020, according to paragraph 5? Type a fraction in simplest form.","a":0.18,"show":"18/100 = 9/50 (less than one fifth)","pts":3,"why":"18 million out of 100 million = 18/100 = 9/50, which is less than 1/5 (20/100)."},
    {"t":"open","key":"sortdetails","q":"Sort these into supporting details and minor details, and explain one choice: (a) the first plan was 15 kilometers wide; (b) many young trees died because no one cared for them; (c) war has slowed work in some countries; (d) Djibouti is near the Red Sea.","min":25,"rows":3,"rubric":["Supporting: (b) and (c)","Minor: (a) and (d)","Explains one choice clearly"],"model":"Supporting: (b) and (c), because they explain why progress has been slow and why communities need to lead. Minor: (a) and (d). The exact width and Djibouti's location are true but do not help prove the central idea."}]},
  {"title": "Roots: Earth and Water",
   "html": "<table class='t'><tr><th>Root</th><th>Meaning</th><th>Examples</th></tr><tr><td>geo</td><td>earth</td><td>geography, geology, geothermal</td></tr><tr><td>terr</td><td>land, earth</td><td>territory, terrain, terrace</td></tr><tr><td>hydr</td><td>water</td><td>hydrant, dehydrated, hydroelectric</td></tr><tr><td>aqua</td><td>water</td><td>aquarium, aquatic, aqueduct</td></tr></table>",
   "checks": [
    {"t":"text","q":"The Aswan High Dam produces <b>hydroelectric</b> power. Using the root, what kind of power is that?","a":[{"all":[["water"]]}],"show":"electricity made from moving water","pts":2,"why":"hydr means water."},
    {"t":"blanks","q":"Complete each sentence with a root word.","sent":"A scientist who studies rocks is a ___. Animals that live in water are ___. The rough, rocky land was hard to cross; the ___ was too steep.","blanks":[["geologist"],["aquatic"],["terrain"]],"pts":3,"why":"geologist (earth + one who studies), aquatic (water), terrain (land)."},
    {"t":"text","q":"A plant that is <b>dehydrated</b> has lost what?","a":[{"all":[["water","moisture"]]}],"show":"water","pts":2,"why":"de (remove) + hydr (water)."}]}],
 "handson": {
  "title": "Build a Central Idea Table",
  "intro": "Turn the article into a table you can stand up, and test whether every leg really holds the top.",
  "materials": ["The article (printed, or copied by hand)", "Scissors and tape", "A paper plate or piece of card stock (the tabletop)", "Four to six paper strips or craft sticks (the legs)", "A marker"],
  "steps": [
   "Write the central idea on the plate in your own words.",
   "Write one supporting detail on each strip, with its paragraph number. Include at least one fact, one example and one statistic.",
   "Tape the strips under the plate as legs so it stands.",
   "Ask a family member to choose one leg and ask, \"How does this hold up the top?\" Explain it out loud.",
   "Add one minor detail on a strip that is too short to reach the table. Explain why it does not hold anything up."],
  "record": [
   {"t":"open","key":"tableci","q":"Type your central idea and each supporting detail (with paragraph numbers), labeled fact, example or statistic. Then write the minor detail you left short and why.","min":50,"rows":7,"rubric":["Central idea as a complete sentence","At least three supporting details with paragraph numbers","Each labeled correctly","A minor detail with a reason"],"model":"Central idea: Land in the Sahel can heal when local people lead the work and mix traditional methods with science, but progress is slow. Fact (2): the African Union started the project in 2007. Example (4): farmers in Niger let old tree roots sprout again. Example (4): zaï pits catch rain and compost. Statistic (5): about 18 million hectares were restored by 2020. Minor detail: Djibouti is near the Red Sea. It tells where the Sahel ends but does not prove how the land heals."}]},
 "think": {
  "intro": "Write clearly and support your ideas. Your teacher scores these.",
  "items": [
   {"t":"open","key":"infopara","q":"Write an informational paragraph of 120 to 180 words about the Nile flood (use your Social Studies lesson). Begin with a sentence that states your central idea, include at least three supporting details (one must be a number), and end with a concluding sentence. Do not tell a story.","min":120,"rows":10,"rubric":["Opening sentence states a clear central idea","Three or more accurate supporting details, including a statistic","Every detail supports the central idea; no minor details","Concluding sentence","Formal informational tone, no narrative"],"model":"The yearly flood of the Nile made it possible for a great civilization to grow in the middle of a desert. Almost no rain falls in most of Egypt, but each summer, monsoon rains in the Ethiopian Highlands filled the Blue Nile and sent a flood north. When the water went down, it left a layer of rich black silt, which is why the Egyptians called their country Kemet, the Black Land. Farmers built walled basins to trap the floodwater and planted wheat and barley in the season called Peret. Officials measured the flood with nilometers marked in cubits; a flood of about 16 cubits meant a good harvest. Because the flood could be predicted and managed, Egypt produced extra grain year after year. The Nile's flood, and the people who learned to control it, turned a desert into one of the longest-lasting civilizations in history."},
   {"t":"open","key":"author","q":"Paragraph 5 reports that progress has been slow. Why might the author include bad news in an article about a hopeful project? What does that do for the reader's trust?","min":30,"rows":4,"rubric":["Honest, balanced reporting","Builds trust because the author is not hiding problems","Connects to the central idea that the work is long-term"],"model":"The author includes the bad news to be honest and balanced. If the article only praised the project, readers might not trust it. Showing the problems also supports the central idea that healing land takes communities and a long time."}]},
 "exit": [
  {"t":"open","key":"exit_tci","q":"What is the difference between a topic and a central idea? Give an example of each for an article about the Nile.","min":15,"rows":2,"rubric":["Topic is a word or phrase; central idea is a complete sentence about the topic","Accurate Nile examples"],"model":"A topic is a word or phrase, like the Nile flood. A central idea is a complete sentence about it, like: The Nile's yearly flood made farming possible in the desert."},
  {"t":"text","q":"\"About 18 million hectares had been restored by 2020\" is what kind of supporting detail?","a":["statistic","a statistic"],"pts":2,"why":"A fact given as a number is a statistic."},
  {"t":"text","q":"What does the root <b>terr</b> mean?","a":[{"all":[["land","earth","ground"]]}],"show":"land or earth","pts":2,"why":"terr means land or earth, as in territory."},
  {"t":"text","q":"What does the root <b>aqua</b> mean?","a":["water"],"pts":2,"why":"aqua means water, as in aquarium."},
  {"t":"open","key":"exit_detail","q":"Write one supporting detail from the article and explain in one sentence how it supports the central idea.","min":15,"rows":2,"rubric":["Accurate detail","Clear connection to the central idea"],"model":"Farmers in Niger let old tree roots sprout again. This shows that local, traditional methods help the land heal, which is the central idea."}],
 "next": "Week 7: text structures. How authors organize information with cause and effect, compare and contrast, problem and solution, and sequence."
}

TEACHER = {
 "standards": [
  "ELA.6.R.2.2: Analyze the central idea(s), implied or explicit, and its development throughout a text.",
  "ELA.6.R.2.1: Analyze how the structure of a text contributes to the meaning and/or purpose (preview).",
  "ELA.6.C.1.4: Write expository texts to explain and/or analyze information from multiple sources, using relevant information and a logical organizational pattern.",
  "ELA.6.V.1.2: Apply knowledge of Greek and Latin roots and affixes to determine meanings of words and phrases in grade-level content.",
  "ELA.K12.EE.2.1: Read and comprehend grade-level complex texts proficiently."],
 "materials": ["The interactive lesson", "The article printed for annotating", "Two highlighters", "A paper plate, paper strips and tape", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Reconnect questions. Compare theme and central idea."],
  [12, "Read the article", "Read it aloud together. The student marks the sentence in each paragraph that seems most important."],
  [10, "Topic vs. central idea", "Contrast the topic with the central idea. Have the student draft a central idea sentence."],
  [12, "Supporting details", "Sort details into fact, example and statistic, and separate minor details."],
  [8, "Roots", "Build words with geo, terr, hydr and aqua, connecting to the Nile lesson."],
  [8, "Writing preview", "Plan the Nile paragraph together: central idea sentence plus three details."],
  [4, "Assign", "Assign the Central Idea Table, Think Deeper and the Exit Check."]],
 "key_questions": ["What is the topic? What does the author say about it?", "Which ideas come up in most paragraphs?", "Does this detail hold up the central idea, or is it just interesting?", "Where is your proof?"],
 "misconceptions": ["Writing the topic (one phrase) as the central idea.", "Choosing the first sentence or one interesting fact as the central idea.", "Thinking every true detail supports the central idea.", "Slipping into story mode in informational writing."],
 "support": ["Provide sentence frames: This article is mostly about ___. The author shows that ___.", "Highlight repeated words to find the central idea.", "Limit the paragraph to three details with a frame."],
 "challenge": ["Find a second article about the Great Green Wall and compare its central idea with this one.", "Rewrite paragraph 3 so it supports a different central idea, then explain the change."],
 "background": "<p>The article is original to KCE and its facts were checked against current sources. The African Union launched the Great Green Wall for the Sahara and the Sahel Initiative in 2007. Targets for 2030: restore 100 million hectares, sequester 250 million tonnes of carbon and create 10 million jobs, across an 8,000-km belt from Senegal to Djibouti. The UNCCD's 2020 status report estimated about 18 million hectares restored (later estimates differ). Farmer-managed natural regeneration (Niger) and zaï planting pits (Burkina Faso) are well-documented local methods. The quoted closing line is a paraphrase, not a direct quotation from a person.</p>",
 "sources": ["UNCCD: The Great Green Wall, Implementation Status and Way Ahead to 2030 (September 2020).", "National Geographic Education: Great Green Wall.", "Mongabay (2023 and 2025) reporting on Great Green Wall progress."]
}

PRINT = {
 "directions": "Use complete sentences. Look back at the article.",
 "items": [
  {"q":"What is the topic of the article? What is its central idea?","a":"Topic: the Great Green Wall. Central idea: land in the Sahel can heal when communities lead and use local knowledge with science, though progress is slow.","lines":3},
  {"q":"List one fact, one example and one statistic from the article, with paragraph numbers.","a":"Fact: launched in 2007 (2). Example: farmers in Niger protect old roots (4). Statistic: about 18 million hectares restored by 2020 (5).","lines":3},
  {"q":"Write one minor detail from the article and explain why it is minor.","a":"For example: Djibouti is near the Red Sea; it gives location but does not prove the central idea.","lines":2},
  {"q":"Write a word with each root and its meaning: geo ____ terr ____ hydr ____ aqua ____","a":"geography (earth); territory (land); hydrant (water); aquarium (water)","lines":2},
  {"q":"Write a central idea sentence for a paragraph about why people need clean water.","a":"For example: Clean water is essential for health, farming and daily life everywhere in the world.","lines":2},
  {"q":"Explain how a central idea is like the top of a table.","a":"The central idea is what the whole text holds up; each supporting detail is a leg that supports it.","lines":2}]
}
