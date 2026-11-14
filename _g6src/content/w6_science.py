TIMELINE = ('<svg viewBox="0 0 560 190" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Timeline of cell theory">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Building the cell theory, one discovery at a time</text>'
  '<line x1="30" y1="80" x2="530" y2="80" stroke="#0A1F3D" stroke-width="3"/>'
  + ''.join(f'<circle cx="{x}" cy="80" r="8" fill="{c}"/><text x="{x}" y="60" text-anchor="middle" font-weight="bold" font-size="12">{y}</text>'
            + ''.join(f'<text x="{x}" y="{104+j*14}" text-anchor="middle">{t}</text>' for j, t in enumerate(lines))
            for x, y, c, lines in [(55, "1665", "#C9A84C", ["Hooke sees and", "names \"cells\"", "in cork"]),
                                   (150, "1670s", "#C9A84C", ["Leeuwenhoek sees", "living single", "cells"]),
                                   (260, "1838", "#0047BA", ["Schleiden: plants", "are made of", "cells"]),
                                   (360, "1839", "#0047BA", ["Schwann: animals", "are made of", "cells too"]),
                                   (470, "1852-55", "#DB2F30", ["Remak, then", "Virchow: cells come", "from cells"])]) + '</svg>')

def scope():
    s = ('<svg viewBox="0 0 560 300" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Parts of a compound light microscope">'
         '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Parts of a compound light microscope</text>'
         '<rect x="190" y="268" width="150" height="16" rx="4" fill="#0A1F3D"/>'
         '<path d="M300 268 L300 120 Q300 92 270 92" fill="none" stroke="#0A1F3D" stroke-width="16"/>'
         '<rect x="216" y="52" width="26" height="70" rx="4" fill="#0047BA" transform="rotate(-18 229 87)"/><rect x="214" y="30" width="18" height="26" rx="3" fill="#0A1F3D" transform="rotate(-18 223 43)"/>'
         '<rect x="200" y="122" width="60" height="14" rx="3" fill="#5b6676"/>'
         '<rect x="206" y="136" width="10" height="26" fill="#C9A84C"/><rect x="224" y="136" width="10" height="34" fill="#C9A84C"/><rect x="242" y="136" width="10" height="20" fill="#C9A84C"/>'
         '<rect x="170" y="186" width="130" height="10" fill="#0A1F3D"/><rect x="204" y="183" width="40" height="4" fill="#cfe3f5" stroke="#5b6676"/>'
         '<circle cx="226" cy="236" r="12" fill="#f2c14e" stroke="#0A1F3D"/>'
         '<circle cx="318" cy="200" r="13" fill="#5b6676"/><circle cx="318" cy="226" r="8" fill="#5b6676"/>')
    left = [(220, 40, 60, "Eyepiece, usually 10×"), (232, 150, 150, "Objectives: 4×, 10×, 40×"), (224, 185, 190, "Stage and slide"), (226, 236, 236, "Light source")]
    right = [(298, 112, 110, "Arm: carry it here"), (318, 200, 196, "Coarse focus knob"), (318, 226, 230, "Fine focus knob"), (334, 276, 276, "Base: and here")]
    for x1, y1, ty, t in left:
        s += f'<path d="M{x1} {y1} L172 {ty}" stroke="#DB2F30"/><text x="168" y="{ty+4}" text-anchor="end" font-size="11">{t}</text>'
    for x1, y1, ty, t in right:
        s += f'<path d="M{x1} {y1} L372 {ty}" stroke="#DB2F30"/><text x="376" y="{ty+4}" font-size="11">{t}</text>'
    return s + '</svg>'

def scales():
    items = [("Your hand", "about 10 cm", 1), ("A grain of salt", "about 0.5 mm", 2), ("Human hair width", "about 0.08 mm", 3), ("Red blood cell", "about 0.008 mm", 4), ("Bacterium", "about 0.002 mm", 5)]
    s = ('<svg viewBox="0 0 560 170" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="How small are cells">'
         '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">How small? From your hand down to a bacterium</text>')
    for i, (n, sz, k) in enumerate(items):
        x = 60 + i * 110; r = 40 - i * 8
        s += f'<circle cx="{x}" cy="80" r="{r}" fill="{["#C9A84C", "#e8e8e8", "#5b3a12", "#DB2F30", "#2e7d32"][i]}" stroke="#0A1F3D"/>'
        s += f'<text x="{x}" y="138" text-anchor="middle" font-weight="bold">{n}</text><text x="{x}" y="153" text-anchor="middle">{sz}</text>'
    return s + '<text x="280" y="168" text-anchor="middle" font-size="10" fill="#5b6676">Not drawn to scale. Sizes are typical values.</text></svg>'

LESSON = {
 "unit": "Unit 2: Cells, the Building Blocks of Life",
 "title": "Cell Theory and the Microscope",
 "subtitle": "Every living thing, from a bacterium to a blue whale, is made of cells. It took 200 years and a new tool to prove it.",
 "objectives": [
  "State the three parts of the cell theory.",
  "Explain how the microscope made the cell theory possible, and describe the work of Hooke, Leeuwenhoek, Schleiden, Schwann, Remak and Virchow.",
  "Name the parts of a compound light microscope and calculate total magnification.",
  "Compare the sizes of cells with everyday objects using metric units.",
  "Explain how the cell theory was built from evidence and changed over time."],
 "vocab": [
  ["cell", "The smallest unit that can carry out all the processes of life."],
  ["cell theory", "The scientific theory that all living things are made of cells, the cell is the basic unit of life, and all cells come from existing cells."],
  ["organism", "A living thing."],
  ["unicellular", "Made of one cell, such as a bacterium."],
  ["multicellular", "Made of many cells, such as a plant or a person."],
  ["microscope", "A tool that uses lenses to make small objects look larger."],
  ["magnification", "How many times larger an object appears. Total magnification = eyepiece power × objective power."],
  ["scientific theory", "A well-tested explanation supported by a large body of evidence from many scientists."]],
 "reconnect": {
  "title": "Unit 1: thinking like a scientist",
  "intro": "Cell biology runs on the same skills you practiced in Unit 1: careful observation, measurement and evidence.",
  "items": [
   {"t":"open","key":"rc_obs","q":"A scientist looks at pond water and sees tiny moving specks. Write one observation and one inference.","min":15,"rows":2,"rubric":["Observation uses the senses only","Inference is a possible explanation"],"model":"Observation: tiny green specks are moving quickly in the water. Inference: the specks might be living things that can swim."},
   {"t":"num","q":"Convert 0.5 millimeters to micrometers. (1 mm = 1,000 micrometers)","a":500,"unit":"micrometers","pts":3,"why":"0.5 × 1,000 = 500 micrometers. Micrometers are the unit scientists use for cells."},
   {"t":"num","q":"Convert 2.5 centimeters to millimeters.","a":25,"unit":"mm","pts":2,"why":"2.5 × 10 = 25 mm."},
   {"t":"open","key":"rc_replicate","q":"In Week 5 you learned that scientists replicate each other's work. Why would that matter for a big claim like \"every living thing is made of cells\"?","min":15,"rows":2,"rubric":["Many scientists checking many organisms builds trust","One person's observations could be wrong or limited"],"model":"A claim about every living thing needs evidence from many scientists looking at many kinds of organisms. If only one person checked, they might have made a mistake or looked at too few living things."}]},
 "hook": {
  "title": "A Window Into an Invisible World",
  "visual": scales(),
  "html": "<p>Before about 1600, no one had ever seen a cell. They are far too small: most of your cells are about 0.01 millimeter across, and about 100 of them side by side would fit across a single millimeter. You are made of roughly 30 trillion of them.</p><p>Then lens makers learned to grind glass into powerful lenses. Suddenly a drop of pond water, a sliver of cork or a scraping from someone's teeth revealed a hidden world. This week you follow the scientists who looked closely and figured out what that world meant.</p><div class='callout'><b>Big idea:</b> New tools lead to new evidence, and new evidence leads to new theories.</div>"},
 "learn": [
  {"title": "The Scientists Who Saw Cells",
   "visual": TIMELINE,
   "html": "<p><b>Robert Hooke</b> (England, 1665) looked at a thin slice of cork through his microscope and saw tiny boxes. He called them <i>cells</i>, from a Latin word for small rooms. He was actually seeing the empty walls of dead plant cells.</p><p><b>Antonie van Leeuwenhoek</b> (the Netherlands, 1670s), a cloth merchant, made tiny single-lens microscopes that magnified up to about 270 times. He was the first to describe living single-celled organisms in pond water and bacteria from the human mouth. He called them \"animalcules.\"</p><p>For 150 years, no one knew whether all life was made of cells. Then <b>Matthias Schleiden</b> (1838) concluded that all plants are made of cells, and <b>Theodor Schwann</b> (1839) showed that animals are too. In the 1850s, <b>Robert Remak</b> showed from his careful observations that new cells form when existing cells divide. <b>Rudolf Virchow</b> made the idea famous in 1855 with the phrase <i>omnis cellula e cellula</i>, \"every cell from a cell,\" but did not credit Remak, who had published it first.</p>",
   "checks": [
    {"t":"open","key":"hookesaw","q":"Hooke named cells, but he never saw a living one. Explain why.","min":15,"rows":2,"rubric":["Cork is dead plant tissue","He saw only empty cell walls"],"model":"Cork comes from dead bark, so the cells were empty. Hooke saw only the walls of dead plant cells, not the living material inside."},
    {"t":"text","q":"Who was the first person to describe living single-celled organisms?","a":["leeuwenhoek","van leeuwenhoek","antonie van leeuwenhoek","anton van leeuwenhoek"],"show":"Antonie van Leeuwenhoek","pts":2,"why":"In the 1670s Leeuwenhoek described tiny living organisms he called animalcules."},
    {"t":"open","key":"remak","q":"Robert Remak published the idea that cells come from cells before Rudolf Virchow, but Virchow got most of the credit. Why does it matter who gets credit in science, and what does this story teach us?","min":25,"rows":3,"rubric":["Credit rewards the people who did the work and builds trust","Recognizes that scientists can be treated unfairly (Remak faced discrimination as a Jewish scientist)","A lesson about honesty or citing sources"],"model":"Credit matters because it rewards the people who did the work and lets others find and check the original evidence. Remak, a Jewish scientist, faced discrimination and did not get the credit he earned. The story teaches that scientists must be honest and cite the people whose work they use."}]},
  {"title": "The Three Parts of the Cell Theory",
   "html": "<ol><li><b>All living things are made of one or more cells.</b> A bacterium is one cell; a person is trillions.</li><li><b>The cell is the basic unit of structure and function in living things.</b> Every job your body does happens in cells.</li><li><b>All cells come from existing cells.</b> Cells do not appear from nonliving matter; they come from cells dividing.</li></ol><p>This is called a <b>theory</b> because it is a well-tested explanation supported by an enormous amount of evidence. In science, a theory is not a guess. It is one of the strongest kinds of knowledge we have, and it can still be refined when new evidence appears.</p>",
   "checks": [
    {"t":"open","key":"threeparts","q":"Write the three parts of the cell theory in your own words.","min":20,"rows":3,"rubric":["All living things are made of cells","The cell is the basic unit of life","Cells come from other cells"],"model":"Every living thing is made of at least one cell. The cell is the smallest unit that does the jobs of life. New cells only come from cells that already exist."},
    {"t":"open","key":"theoryguess","q":"A friend says, \"The cell theory is just a theory, so it's only a guess.\" How would you respond?","min":20,"rows":3,"rubric":["Explains that a scientific theory is a well-tested explanation","Mentions large amounts of evidence from many scientists over many years"],"model":"In science, a theory is not a guess. It is an explanation that has been tested and supported by huge amounts of evidence from many scientists over almost 200 years, like Schleiden, Schwann and Virchow, and everyone who has looked at cells since."},
    {"t":"open","key":"virusq","q":"Is a rock alive? Use the cell theory to explain your answer.","min":12,"rows":2,"rubric":["Not alive","It is not made of cells"],"model":"No. A rock is not made of cells, and according to the cell theory, all living things are made of cells."}]},
  {"title": "Using a Microscope",
   "visual": scope(),
   "html": "<p>A compound light microscope uses two sets of lenses. Light passes up through the slide, through an objective lens, and then through the eyepiece to your eye.</p><p><b>Total magnification = eyepiece power × objective power.</b> With a 10× eyepiece and a 40× objective, the image is 10 × 40 = <b>400×</b>, or 400 times larger than real life.</p><p><b>Rules:</b> carry it with one hand on the arm and one under the base; start with the lowest power objective; use the coarse focus only on low power, and the fine focus on high power.</p>",
   "checks": [
    {"t":"num","q":"A microscope has a 10× eyepiece and a 4× objective. What is the total magnification?","a":40,"unit":"×","pts":2,"why":"10 × 4 = 40×."},
    {"t":"num","q":"Leeuwenhoek's best lenses magnified about 270×. How many times more powerful is a modern 10× eyepiece with a 100× objective?","a":3.7,"tol":0.05,"unit":"times","show":"about 3.7 times","pts":3,"why":"10 × 100 = 1,000×. 1,000 ÷ 270 ≈ 3.7."},
    {"t":"num","q":"A cell looks 4 mm wide at 400×. How wide is it really, in millimeters?","a":0.01,"unit":"mm","pts":3,"why":"4 ÷ 400 = 0.01 mm (10 micrometers)."},
    {"t":"open","key":"lowfirst","q":"Why should you always start focusing with the lowest-power objective?","min":12,"rows":2,"rubric":["Easier to find the object (wider view)","Avoids crashing the lens into the slide"],"model":"The low-power lens shows a wider area, so it is easier to find what you are looking for, and it sits higher above the slide so you will not crack the slide with the lens."}]},
  {"title": "Scientist Spotlight: Ernest Everett Just",
   "html": "<p><b>Ernest Everett Just</b> (1883 to 1941) was born in Charleston, South Carolina. He graduated with top honors from Dartmouth College, earned a PhD at the University of Chicago, and taught at Howard University. Each summer he studied the egg cells of sea urchins and marine worms at the Marine Biological Laboratory in Woods Hole, Massachusetts.</p><p>Just discovered how important the cell's outer surface is for fertilization and development. He showed that the point where a sperm enters the egg affects how the egg first divides. In 1915 he received the NAACP's first Spingarn Medal. Because racism kept him out of major American research universities, he moved to Europe in the 1930s, where he wrote <i>The Biology of the Cell Surface</i> (1939). Scientists today recognize how far ahead of his time he was.</p>",
   "checks": [
    {"t":"open","key":"just","q":"What part of the cell did Ernest Everett Just show was important, and what barrier did he face as a scientist?","min":20,"rows":3,"rubric":["The cell surface (in fertilization and development)","Racism kept him from positions at major U.S. research universities"],"model":"He showed that the cell's surface plays a key role in fertilization and how an egg develops. Racism kept him out of major American research universities, so he did much of his work in summers at Woods Hole and later in Europe."}]}],
 "handson": {
  "title": "Make a Water-Drop Magnifier",
  "intro": "Leeuwenhoek's microscopes used a single tiny lens. You can make a simple one with a drop of water.",
  "materials": ["A clear plastic sheet (a page protector or the lid of a takeout container)", "A dropper or straw", "Water", "A strip of newspaper or printed text", "Items to observe: salt, sugar, a leaf, onion skin, a hair, fabric", "A magnifying glass or a phone camera on zoom (optional, to compare)", "A ruler with millimeters"],
  "steps": [
   "Place the plastic sheet over printed text. Put one small, round drop of water on the plastic.",
   "Look through the drop from above. Compare the letters under the drop with the letters beside it.",
   "Try a smaller drop and a larger drop. Which magnifies more?",
   "Place each item under the plastic and observe it through the drop. Sketch what you see.",
   "Peel the thin, clear skin from the inside of an onion layer. Look at it through the drop or a magnifying glass. Can you see tiny boxes like Hooke's cork?"],
  "record": [
   {"t":"open","key":"drop","q":"Which drop size magnified more, and how do you know? Estimate how many times larger the letters looked.","min":25,"rows":3,"rubric":["Smaller, more curved drop magnifies more","Explains how they compared","Gives a reasonable estimate"],"model":"The smaller drop magnified more. A letter that was 2 mm tall looked about 6 mm tall under the small drop, so about 3 times larger. The bigger drop was flatter and only made letters a little bigger."},
   {"t":"open","key":"dropsketch","q":"Describe what you saw in two of the items, and explain what a real microscope would let you see that your water drop could not.","min":30,"rows":4,"rubric":["Two specific observations","Recognizes the limits of a water lens","Connects to individual cells needing higher magnification"],"model":"Salt grains looked like tiny clear cubes, and the onion skin looked like a thin sheet with faint lines. A real microscope at 100× or 400× would show the onion's individual cells as boxes with walls and a dark nucleus in each, which my water drop was not strong enough to show."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"toolsscience","q":"\"New tools lead to new evidence, and new evidence leads to new theories.\" Use the history of the cell theory to explain this statement, naming at least three scientists.","min":60,"rubric":["Explains the microscope as the new tool","Names three scientists and what each contributed","Shows how evidence built up into the theory over time"],"model":"Before microscopes, no one could see cells. Better lenses let Hooke see and name cells in cork in 1665 and let Leeuwenhoek see living single-celled organisms in the 1670s. Over the next 150 years, microscopes improved, and Schleiden and Schwann used them to show that plants and animals are both made of cells. Remak then observed cells dividing, and Virchow spread the idea that every cell comes from a cell. Each new tool gave new evidence, and the evidence slowly built the cell theory."},
   {"t":"open","key":"spontaneous","q":"Long ago, many people believed that mice could appear from piles of old rags and grain. How does the third part of the cell theory challenge that idea? Design a simple test that could check it.","min":45,"rubric":["Cells only come from cells, so mice must come from parent mice","A fair test: sealed versus open containers of rags and grain","Predicts mice appear only where mice can get in"],"model":"The cell theory says all cells come from existing cells, so a mouse, made of cells, must come from other mice, not from rags. To test it, I would put rags and grain in two containers, one sealed so mice cannot get in and one open. If mice appear only in the open one, it shows they came in from outside, not from the rags."}]},
 "exit": [
  {"t":"open","key":"exit_three","q":"State the three parts of the cell theory.","min":15,"rows":2,"rubric":["Living things are made of cells","The cell is the basic unit of life","Cells come from existing cells"],"model":"All living things are made of cells, the cell is the basic unit of life, and all cells come from other cells."},
  {"t":"num","q":"What is the total magnification with a 15× eyepiece and a 40× objective?","a":600,"unit":"×","pts":2,"why":"15 × 40 = 600×."},
  {"t":"text","q":"Which scientist first named cells after looking at cork?","a":["hooke","robert hooke"],"show":"Robert Hooke","pts":2,"why":"Robert Hooke, in 1665."},
  {"t":"text","q":"Is a single bacterium unicellular or multicellular?","a":["unicellular"],"pts":2,"why":"A bacterium is one cell."},
  {"t":"num","q":"A cell is 0.02 mm wide. How many of them would fit side by side across 1 millimeter?","a":50,"unit":"cells","pts":3,"why":"1 ÷ 0.02 = 50 cells."}],
 "next": "Week 8: inside an animal cell. Meet the nucleus, cell membrane, mitochondria and the other parts that keep a cell alive."
}

TEACHER = {
 "standards": [
  "SC.6.L.14.2: Investigate and explain the components of the scientific theory of cells (cell theory): all organisms are composed of cells (single-celled or multi-cellular), all cells come from pre-existing cells, and cells are the basic unit of life.",
  "SC.6.N.3.1: Recognize and explain that a scientific theory is a well-supported and widely accepted explanation of nature and is not simply a claim posed by an individual.",
  "SC.6.N.2.2: Explain that scientific knowledge is durable because it is open to change as new evidence or interpretations are encountered.",
  "SC.6.N.2.3: Recognize that scientists who make contributions to scientific knowledge come from all kinds of backgrounds and possess varied talents, interests, and goals.",
  "MA.6 connection: multiplying and dividing decimals for magnification and size."],
 "materials": ["The interactive lesson", "A clear plastic sheet, dropper and water", "An onion, salt and printed text", "A magnifying glass or microscope if available", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Unit 1 Reconnect questions."],
  [5, "Hook", "Compare sizes on the scale chart. Ask: how could anyone see something this small?"],
  [14, "History", "Tell the story from Hooke to Virchow on the timeline. Discuss Remak and fair credit."],
  [10, "Cell theory", "State the three parts. Discuss what a scientific theory is."],
  [12, "Microscope", "Label the parts. Practice total magnification and real-size calculations."],
  [7, "Spotlight", "Introduce Ernest Everett Just and the cell surface."],
  [6, "Assign", "Assign the water-drop magnifier, Think Deeper and the Exit Check."]],
 "key_questions": ["How did a new tool change what scientists could know?", "What evidence supports each part of the cell theory?", "What makes a scientific theory different from a guess?", "Who gets credit, and why does it matter?"],
 "misconceptions": ["Thinking Hooke saw living cells.", "Believing a scientific theory is a guess.", "Thinking only animals are made of cells, or that cells are all the same size.", "Adding instead of multiplying lens powers."],
 "support": ["Provide a labeled microscope diagram to keep.", "Use a timeline card with one fact per scientist.", "Model the magnification formula with two examples."],
 "challenge": ["Research how electron microscopes go beyond light microscopes and what they revealed.", "Find out how Leeuwenhoek's microscopes were built and why they were so powerful for single lenses."],
 "background": "<p>Hooke published Micrographia in 1665. Leeuwenhoek began reporting microorganisms to the Royal Society in the 1670s; his best surviving lens magnifies about 270 times. Schleiden (1838) and Schwann (1839) proposed that plants and animals are composed of cells. Robert Remak published evidence that cells arise by division in 1852; Virchow's 1855 essay popularized omnis cellula e cellula without crediting Remak, who faced antisemitic barriers to advancement. Ernest Everett Just (1883 to 1941) earned his PhD at the University of Chicago in 1916, received the first Spingarn Medal in 1915, and published The Biology of the Cell Surface in 1939. Human cell count estimates are about 30 trillion (Sender, Fuchs and Milo, 2016). Sizes on the scale chart are typical values.</p>",
 "sources": ["OpenStax Microbiology, Foundations of Modern Cell Theory.", "Embryo Project Encyclopedia (Arizona State University): Ernest Everett Just.", "American Academy of Arts and Sciences: Ernest Everett Just.", "Sender, R., Fuchs, S. and Milo, R. (2016), Revised estimates for the number of human and bacteria cells in the body, PLOS Biology."]
}

PRINT = {
 "directions": "Use complete sentences and show calculations.",
 "items": [
  {"q":"Write the three parts of the cell theory.","a":"All living things are made of cells; the cell is the basic unit of life; all cells come from existing cells.","lines":3},
  {"q":"Match each scientist to the discovery: Hooke, Leeuwenhoek, Schwann, Remak.","a":"Hooke: named cells in cork; Leeuwenhoek: saw living single-celled organisms; Schwann: animals are made of cells; Remak: cells come from dividing cells.","lines":3},
  {"q":"Find the total magnification: 10× eyepiece with 4×, 10× and 40× objectives.","a":"40×, 100×, 400×","lines":1},
  {"q":"An image of a cell is 6 mm wide at 600×. How wide is the real cell?","a":"6 ÷ 600 = 0.01 mm","lines":2},
  {"q":"Explain the difference between a scientific theory and a guess.","a":"A scientific theory is a well-tested explanation supported by lots of evidence from many scientists; a guess has not been tested.","lines":2},
  {"q":"Name one thing Ernest Everett Just discovered and one barrier he faced.","a":"The importance of the cell surface in fertilization and development; racism kept him out of major U.S. research universities.","lines":2}]
}
