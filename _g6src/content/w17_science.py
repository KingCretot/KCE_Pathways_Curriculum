BONE = ('<svg viewBox="0 0 640 260" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Inside a long bone: cartilage, spongy bone, compact bone and marrow">'
  '<text x="320" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Inside a long bone (such as the femur)</text>'
  '<path d="M60 90 C30 60 50 40 80 56 C100 34 140 44 136 78 L136 172 C140 206 100 216 80 194 C50 210 30 190 60 160Z" fill="#f4ecd8" stroke="#8a6d1f" stroke-width="2" transform="rotate(-90 98 125) translate(-60 160)"/>'
  # simplified horizontal bone
  '<rect x="150" y="100" width="340" height="60" fill="#f4ecd8" stroke="#8a6d1f" stroke-width="2"/>'
  '<rect x="150" y="114" width="340" height="32" fill="#e0a85a"/>'
  '<ellipse cx="130" cy="130" rx="46" ry="56" fill="#efe2c2" stroke="#8a6d1f" stroke-width="2"/><ellipse cx="510" cy="130" rx="46" ry="56" fill="#efe2c2" stroke="#8a6d1f" stroke-width="2"/>'
  + ''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="none" stroke="#b69a5c"/>' for x in (110, 125, 140, 150, 490, 500, 515, 530) for y in (110, 125, 140, 152)) +
  '<path d="M90 86 A46 56 0 0 0 90 174" fill="none" stroke="#9fc6e8" stroke-width="7"/><path d="M550 86 A46 56 0 0 1 550 174" fill="none" stroke="#9fc6e8" stroke-width="7"/>'
  '<line x1="86" y1="80" x2="60" y2="56" stroke="#0A1F3D"/><text x="20" y="50" font-size="11" fill="#0A1F3D">cartilage (cushions joints)</text>'
  '<line x1="130" y1="112" x2="190" y2="60" stroke="#0A1F3D"/><text x="160" y="52" font-size="11" fill="#0A1F3D">spongy bone (light, strong; holds red marrow)</text>'
  '<line x1="320" y1="104" x2="380" y2="76" stroke="#0A1F3D"/><text x="384" y="74" font-size="11" fill="#0A1F3D">compact bone (hard outer layer)</text>'
  '<line x1="320" y1="130" x2="320" y2="210" stroke="#0A1F3D"/><text x="320" y="224" text-anchor="middle" font-size="11" fill="#0A1F3D">marrow cavity (yellow marrow stores fat)</text>'
  '<text x="320" y="250" text-anchor="middle" font-size="10" fill="#5b6676">Bone is living tissue with blood vessels and nerves. Simplified drawing, not to scale.</text></svg>')
BONE = BONE.replace(BONE[BONE.index('<path d="M60 90'):BONE.index('<rect x="150" y="100"')], '')

ARM = ('<svg viewBox="0 0 660 260" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Biceps and triceps work as an opposing pair to bend and straighten the elbow">'
  '<text x="330" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Muscles pull in pairs</text>'
  '<text x="150" y="48" text-anchor="middle" font-weight="bold" fill="#0A1F3D">Bending the elbow</text><text x="500" y="48" text-anchor="middle" font-weight="bold" fill="#0A1F3D">Straightening the elbow</text>'
  # bent arm
  '<line x1="40" y1="170" x2="180" y2="170" stroke="#e9e2cf" stroke-width="16" stroke-linecap="round"/>'
  '<line x1="180" y1="170" x2="232" y2="96" stroke="#e9e2cf" stroke-width="14" stroke-linecap="round"/>'
  '<path d="M52 160 Q110 112 186 150 L184 158 Q112 140 56 164Z" fill="#DB2F30"/>'
  '<path d="M52 180 Q120 190 186 178 L184 174 Q120 184 56 176Z" fill="#0047BA" opacity="0.5"/>'
  '<circle cx="180" cy="170" r="9" fill="#C9A84C"/>'
  '<text x="60" y="118" font-size="11" fill="#DB2F30" font-weight="bold">biceps contracts (shortens)</text><text x="60" y="206" font-size="11" fill="#0047BA" font-weight="bold">triceps relaxes</text>'
  # straight arm
  '<line x1="370" y1="170" x2="500" y2="170" stroke="#e9e2cf" stroke-width="16" stroke-linecap="round"/>'
  '<line x1="500" y1="170" x2="630" y2="170" stroke="#e9e2cf" stroke-width="14" stroke-linecap="round"/>'
  '<path d="M382 160 Q440 154 508 160 L508 163 Q440 158 386 164Z" fill="#DB2F30" opacity="0.5"/>'
  '<path d="M382 180 Q440 206 510 180 L506 176 Q440 194 386 176Z" fill="#0047BA"/>'
  '<circle cx="500" cy="170" r="9" fill="#C9A84C"/>'
  '<text x="390" y="146" font-size="11" fill="#DB2F30" font-weight="bold">biceps relaxes</text><text x="390" y="220" font-size="11" fill="#0047BA" font-weight="bold">triceps contracts (shortens)</text>'
  '<text x="330" y="240" text-anchor="middle" font-size="12" fill="#0A1F3D">A muscle can only pull, never push. So muscles work in opposing pairs.</text>'
  '<text x="330" y="256" text-anchor="middle" font-size="10" fill="#5b6676">Upper arm on the left of each drawing. Tendons attach muscle to bone; ligaments attach bone to bone. Simplified drawing.</text></svg>')

LESSON = {
 "unit": "Unit 4: The Human Body",
 "title": "Skeletal and Muscular Systems",
 "subtitle": "Your 206 bones and more than 600 muscles work as one team, the musculoskeletal system. This week you look inside a bone, test how joints move, and build a model arm that shows why muscles always work in pairs.",
 "objectives": [
  "Describe five functions of the skeletal system, including making blood cells and storing minerals.",
  "Identify the parts of a long bone and explain how bone's structure fits its jobs.",
  "Compare types of joints and explain the roles of cartilage, ligaments and tendons.",
  "Explain how skeletal muscles work in opposing pairs and how bones act as levers.",
  "Explain how the skeletal, muscular and nervous systems interact, and how exercise and nutrition keep them healthy."],
 "vocab": [
  ["marrow", "Soft tissue inside bones; red marrow makes blood cells, yellow marrow stores fat."],
  ["joint", "A place where two or more bones meet."],
  ["cartilage", "Smooth, flexible connective tissue that cushions the ends of bones at joints."],
  ["ligament", "A tough band of connective tissue that connects bone to bone."],
  ["tendon", "A strong cord of connective tissue that connects muscle to bone."],
  ["voluntary muscle", "Muscle you control on purpose, such as skeletal muscle."],
  ["lever", "A rigid bar that turns around a fixed point (fulcrum); bones act as levers moved by muscles."]],
 "reconnect": {
  "title": "Week 16: Levels of organization",
  "intro": "Bones and muscles are organs built from the tissues you met last week.",
  "items": [
   {"t":"text","q":"Bone is one kind of which tissue type: epithelial, connective, muscle or nervous?","a":[{"all":[["connective"]],"none":["not"]}],"show":"connective","pts":2,"why":"Bone cells sit in a hard matrix."},
   {"t":"text","q":"Unspecialized cells in bone marrow that can become blood cells are called ___ cells.","a":[{"all":[["stem"]],"none":["not"]}],"show":"stem","pts":2,"why":"Week 16: bone marrow stem cells make about 2 million red blood cells a second."},
   {"t":"text","q":"Of the three kinds of muscle tissue, which kind moves your bones?","a":[{"all":[["skeletal"]],"none":["not","smooth","cardiac"]}],"show":"skeletal","pts":2,"why":"Smooth muscle squeezes organs; cardiac muscle pumps the heart."},
   {"t":"open","key":"rc_emerge","q":"Last week you learned about emergent properties. Name one ability your arm has that a single muscle cell does not have.","min":12,"rows":2,"rubric":["A whole-arm ability (lifting, throwing, writing, waving) that needs bones, muscles and nerves together"],"model":"My arm can throw a ball. One muscle cell can only shorten a tiny bit; throwing needs bones, many muscles and nerves working together."}]},
 "hook": {
  "title": "Astronauts Who Lose Bone",
  "html": "<p>When astronauts live on the International Space Station, they float. Their legs and spines carry almost no weight. And without that weight, their bones begin to thin: NASA reports that astronauts can lose about 1 to 1.5 percent of the mineral in their leg and hip bones for every month in space. Their muscles shrink, too.</p><p>That is why astronauts exercise about two hours every day on special treadmills, bikes and resistance machines. It tells us something surprising: bones are not dead sticks. They are <b>living organs</b> that rebuild themselves depending on how they are used.</p><div class='callout'><b>Big question:</b> How do bones and muscles work together to support, protect and move your body?</div>"},
 "learn": [
  {"title": "What Bones Do",
   "visual": BONE,
   "html": "<p>An adult skeleton has <b>206 bones</b> (a newborn has about 270 to 300, many of which fuse together as the child grows). The skeleton has five main jobs:</p><ol><li><b>Support:</b> it holds the body up and gives it shape.</li><li><b>Protection:</b> the skull guards the brain; the ribs shield the heart and lungs.</li><li><b>Movement:</b> muscles pull on bones to move them.</li><li><b>Making blood cells:</b> red marrow inside many bones makes red blood cells, white blood cells and platelets.</li><li><b>Storage:</b> bones store minerals, especially calcium and phosphorus, and release them into the blood when the body needs them.</li></ol><p>A long bone has a hard outer layer of <b>compact bone</b>, lighter <b>spongy bone</b> at its ends (full of tiny spaces like a honeycomb), a central <b>marrow</b> cavity, and smooth <b>cartilage</b> where it meets other bones. Spongy bone's honeycomb shape makes the bone strong without making it heavy.</p>",
   "checks": [
    {"t":"blanks","q":"Name the bone function.","sent":"The ribs shielding the lungs: ___ &nbsp; Red marrow producing red cells, white cells and platelets: ___ &nbsp; Bones releasing calcium into the blood: ___","blanks":[[{"all":[["protect"]],"none":["not"]}],[{"all":[["blood"]],"none":["not"]}],[{"all":[["stor","mineral"]],"none":["not"]}]],"show":"protection; making blood cells; storage","pts":3,"why":"Support, protection, movement, blood cells and storage."},
    {"t":"num","q":"A newborn has about 300 bones and an adult has 206. About how many bones fuse together (or are counted as one) as a person grows?","a":94,"tol":2,"unit":"bones","pts":2,"why":"300 − 206 = 94. Skull bones and the bones at the base of the spine are examples."},
    {"t":"open","key":"spongy","q":"Why is it useful for the ends of long bones to be spongy instead of solid all the way through? Connect structure to function.","min":20,"rows":2,"rubric":["Spongy (honeycomb) structure is strong but light","Lighter bones need less muscle effort to move; spaces hold red marrow"],"model":"The honeycomb structure is strong but light, so the bone can hold weight without being so heavy that moving it wastes energy. The spaces also hold red marrow, which makes blood cells."}]},
  {"title": "Joints, Cartilage, Ligaments and Tendons",
   "html": "<p>Where bones meet, they form <b>joints</b>. Different joints allow different movements:</p><ul><li><b>Ball-and-socket</b> (shoulder, hip): movement in almost every direction.</li><li><b>Hinge</b> (elbow, knee, fingers): back and forth, like a door.</li><li><b>Pivot</b> (top of the neck): turning or rotating, as when you shake your head \"no.\"</li><li><b>Gliding</b> (between the small bones of the wrist and ankle): small sliding movements.</li><li><b>Fixed</b> (skull): almost no movement, for protection.</li></ul><p>Three connective tissues make joints work. <b>Cartilage</b> covers the ends of bones so they glide smoothly. <b>Ligaments</b> hold bone to bone. <b>Tendons</b> attach muscle to bone: you can feel the large Achilles tendon above your heel.</p><p>A <b>sprain</b> is a stretched or torn ligament; a <b>strain</b> is a stretched or torn muscle or tendon.</p>",
   "checks": [
    {"t":"text","q":"Which type of joint is your shoulder?","a":[{"all":[["ball"]],"none":["not"]}],"show":"ball-and-socket","pts":2,"why":"It moves in nearly every direction."},
    {"t":"blanks","q":"Connective tissue jobs.","sent":"Muscle to bone: ___ &nbsp; Bone to bone: ___","blanks":[[{"all":[["tendon"]],"none":["not"]}],[{"all":[["ligament"]],"none":["not"]}]],"show":"tendon; ligament","pts":2,"why":"Tip: tendons tie muscle to bone; ligaments link bone to bone."},
    {"t":"open","key":"kneedesign","q":"Your knee is a hinge joint, not a ball-and-socket joint. Why is that a good design for walking and running? What would go wrong if it could twist in every direction?","min":30,"rows":3,"rubric":["A hinge moves in one direction, giving stability for weight-bearing and pushing forward","Twisting in every direction would make the leg wobbly and easier to injure"],"model":"A hinge lets the knee bend and straighten in one direction, which is exactly what walking and running need, and it stays stable while carrying the body's weight. If the knee could twist every way, the leg would be wobbly and ligaments would be injured much more easily."}]},
  {"title": "Muscles Pull in Pairs",
   "visual": ARM,
   "html": "<p>Skeletal muscles are <b>voluntary</b>: you decide when to move them. (Smooth and cardiac muscle are <b>involuntary</b>: they work without your control.) A skeletal muscle can only <b>contract</b>, or shorten and pull. It can't push. So muscles work in <b>opposing pairs</b>.</p><p>To bend your elbow, the <b>biceps</b> on the front of your upper arm contracts and the <b>triceps</b> on the back relaxes. To straighten it, the triceps contracts and the biceps relaxes. Your thigh has the same kind of pair: the quadriceps straightens the knee and the hamstrings bend it.</p><p>Bones act as <b>levers</b>, and joints are the <b>fulcrums</b> (pivot points). The biceps attaches to your forearm just below the elbow, so a short pull by the muscle produces a large, fast movement of your hand.</p><p>Every movement begins with the <b>nervous system</b>: your brain sends a signal along nerves to tell the muscle fibers to contract.</p>",
   "checks": [
    {"t":"text","q":"When you straighten your arm, which muscle contracts: biceps or triceps?","a":[{"all":[["tricep"]],"none":["not tricep","bicep"]}],"show":"the triceps","pts":2,"why":"The biceps relaxes."},
    {"t":"text","q":"Is skeletal muscle voluntary or involuntary?","a":[{"all":[["voluntary"]],"none":["involuntary","not voluntary"]}],"show":"voluntary","pts":2,"why":"You control it on purpose."},
    {"t":"open","key":"nopush","q":"Explain why a single muscle could not both bend and straighten your elbow.","min":20,"rows":2,"rubric":["A muscle can only contract (pull), not push","So a second muscle on the other side is needed to pull the bone back"],"model":"A muscle can only pull by shortening; it can't push. One muscle can bend the elbow, but a second muscle on the other side has to pull to straighten it again."}]},
  {"title": "Keeping Bones and Muscles Healthy",
   "html": "<p>Bones keep rebuilding all your life. Cells called osteoblasts build new bone and osteoclasts break old bone down. Your teens are the most important bone-building years: by about age 18 in girls and 20 in boys, people have built up to 90 percent of their peak bone mass.</p><ul><li><b>Weight-bearing exercise</b>, such as running, jumping rope, dancing, hiking and climbing, signals bones to grow stronger, just as missing that weight weakens astronauts' bones.</li><li><b>Calcium</b> (milk, yogurt, cheese, leafy greens such as collards, fortified foods, canned fish with soft bones) and <b>vitamin D</b> (made by skin in sunlight and found in some foods) build strong bones.</li><li><b>Protective gear</b> (helmets, wrist guards) and warming up help prevent fractures, sprains and strains.</li></ul><p>When bone breaks (a <b>fracture</b>), cells rebuild it: a soft callus forms, then hardens over about 6 to 8 weeks, which is why a cast holds the bone still while it heals.</p>",
   "checks": [
    {"t":"text","q":"Which mineral do bones store the most of, and need from foods like milk and collard greens?","a":[{"all":[["calcium"]],"none":["not"]}],"show":"calcium","pts":2,"why":"Phosphorus is also stored."},
    {"t":"open","key":"astrofix","q":"Use what you learned to explain why astronauts lose bone in space and why running on a treadmill (with straps pulling them down) helps.","min":30,"rows":3,"rubric":["Without weight on the bones, bones are not signaled to rebuild, so osteoclasts break down more than osteoblasts build","Weight-bearing exercise puts load on bones, signaling them to rebuild and stay strong"],"model":"In space, bones carry almost no weight, so they aren't signaled to rebuild, and more old bone is broken down than new bone is built. Running on a treadmill with straps pulling them down puts weight on their bones again, which signals the bone cells to keep building."}]}],
 "handson": {
  "title": "Build a Model Arm and Test Your Joints",
  "intro": "Build a working model of the biceps and triceps, then investigate how your own joints move.",
  "materials": ["2 strips of stiff cardboard about 2 inches by 10 inches", "A brass paper fastener (brad)", "2 pieces of string or yarn, about 14 inches each", "Tape", "Optional: 2 long balloons to show a muscle bulging", "A hole punch or a sharp pencil (used by an adult)", "A marker", "Paper and pencil", "Optional: a chicken drumstick bone (cooked and cleaned) and a jar of white vinegar"],
  "steps": [
   "Joint test: move each of these joints and record the movements it allows: shoulder, elbow, neck, wrist, knee, fingers. Classify each joint type.",
   "Model arm: an adult punches a hole near one end of each cardboard strip. Join the strips with the paper fastener so they bend like an elbow. Label one strip \"upper arm\" and the other \"forearm.\"",
   "Tape one end of a string to the front of the forearm just past the joint. Run it up the front of the upper arm through a loop of tape near the top: this is the biceps. Do the same on the back: this is the triceps.",
   "Pull the front string: the forearm bends up. Pull the back string: it straightens. Notice that each string can only pull, and that when one shortens the other gets longer.",
   "Optional vinegar bone (takes 3 days): soak a clean, cooked chicken drumstick bone in vinegar. On day 3, rinse it and gently try to bend it. Vinegar dissolves the calcium minerals. Wash hands after handling the bone, don't taste the vinegar, keep the jar and bone where pets can't reach them (cooked chicken bones can splinter and injure dogs), and throw the bone away when you finish.",
   "Feel your own biceps and triceps as you bend and straighten your arm with your other hand on each muscle.", "If you use balloons, check for latex allergies and keep balloons and pieces away from young children."],
  "record": [
   {"t":"open","key":"jointrec","q":"Make a table or list of the six joints you tested, the movements each allowed and its joint type.","min":30,"rows":4,"rubric":["Six joints listed","Movements described","Joint types correct (shoulder ball-and-socket, elbow hinge, neck pivot, knee hinge, fingers hinge; for the wrist, a reasonable description such as bending, tilting and small gliding movements)"],"model":"Shoulder: circles, up, down, forward, back: ball-and-socket. Elbow: bends and straightens: hinge. Neck (top): turns side to side: pivot. Wrist: bends, tilts side to side and makes small slides: the small wrist bones glide against each other. Knee: bends and straightens: hinge. Fingers: bend and straighten: hinge."},
   {"t":"open","key":"modelrec","q":"Explain how your model arm shows that muscles work in pairs. In what ways is your model unlike a real arm?","min":40,"rows":4,"rubric":["Describes which muscle shortens to bend and which shortens to straighten","Notes at least one limit of the model (no nerves or brain signal, balloons don't contract on their own, real muscles attach with tendons, cardboard is not living)"],"model":"When I bent the model, the front string (biceps) got shorter and the back one (triceps) got longer; to straighten, the back string had to pull. My model is unlike a real arm because the strings don't contract by themselves, there are no nerves sending signals, and real muscles attach with tendons to living bone."}]},
 "think": {
  "intro": "Use evidence and explain your reasoning. Your teacher scores these.",
  "items": [
   {"t":"open","key":"vinegarpredict","q":"In the vinegar bone test, vinegar dissolves the calcium minerals in bone, but leaves behind a protein called collagen. Predict how the bone will change, and explain what this shows about why bones need both minerals and collagen.","min":46,"rows":5,"rubric":["Prediction: the bone becomes rubbery and bendable","Minerals give hardness and strength against crushing","Collagen gives flexibility so bones don't shatter","Both together make bone strong and slightly flexible"],"model":"The bone will become rubbery and bend instead of snapping. That shows calcium minerals make bone hard and able to hold weight, while collagen makes it slightly flexible. A bone with only minerals would be like chalk and shatter easily; with only collagen it would be floppy. Together they make bone hard but not brittle."},
   {"t":"open","key":"systemsjump","q":"Describe what happens in your body when you jump to catch a ball, naming at least three body systems and how they work together.","min":64,"rows":6,"rubric":["Nervous system: eyes see the ball, brain sends signals to muscles","Muscular system: leg muscles contract to jump, arm muscles to reach","Skeletal system: bones act as levers, joints allow movement, cartilage absorbs landing","Could include circulatory or respiratory supplying oxygen"],"model":"My eyes see the ball, and my nervous system sends signals from my brain to my muscles. My muscular system contracts my quadriceps and calf muscles to push off, and my arm muscles reach up. My skeletal system provides levers: my leg bones push against the ground, and joints like my knees and shoulders let me move. When I land, cartilage cushions my knees. My circulatory and respiratory systems keep oxygen flowing to my working muscles."}]},
 "exit": [
  {"t":"text","q":"What connects muscle to bone?","a":[{"all":[["tendon"]],"none":["not"]}],"show":"a tendon","pts":2,"why":"Ligaments connect bone to bone."},
  {"t":"text","q":"What part of a bone makes blood cells?","a":[{"all":[["red marrow","marrow"]],"none":["not","yellow"]}],"show":"red marrow","pts":2,"why":"Yellow marrow stores fat."},
  {"t":"text","q":"What type of joint lets you turn your head side to side?","a":[{"all":[["pivot"]],"none":["not"]}],"show":"a pivot joint","pts":2,"why":"At the top of the neck."},
  {"t":"open","key":"exit_pairs","q":"Why do skeletal muscles work in pairs?","min":12,"rows":2,"rubric":["Muscles can only pull, not push, so a second muscle pulls the bone back"],"model":"A muscle can only pull, so one muscle bends a joint and its partner pulls it straight again."}],
 "next": "Week 18: the circulatory and respiratory systems."
}

TEACHER = {
 "standards": [
  "SC.6.L.14.5: Identify and investigate the general functions of the major systems of the human body (digestive, respiratory, circulatory, reproductive, excretory, immune, nervous, and musculoskeletal) and describe ways these systems interact with each other to maintain homeostasis.",
  "SC.6.L.14.1: Describe and identify patterns in the hierarchical organization of organisms from atoms to molecules to cells to tissues to organs to organ systems to organisms.",
  "SC.6.N.3.4: Identify the role of models in the context of the sixth grade science benchmarks.",
  "Health connection: exercise, calcium and vitamin D for bone health (NIAMS guidance)."],
 "materials": ["The interactive lesson", "2 cardboard strips, a brass paper fastener, 2 strings (balloons optional), tape, hole punch", "Marker, paper and pencil", "Optional: a cleaned chicken drumstick bone and white vinegar", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 16 warm-up questions."],
  [4, "Hook", "Astronaut bone loss: are bones alive?"],
  [11, "What bones do", "Five functions; parts of a long bone; structure and function."],
  [11, "Joints", "Move each joint and classify it; tendons, ligaments, cartilage; sprain versus strain."],
  [12, "Muscle pairs", "Feel biceps and triceps; voluntary and involuntary; levers and fulcrums."],
  [9, "Healthy bones", "Bone remodeling, weight-bearing exercise, calcium and vitamin D; fractures."],
  [7, "Assign", "Start the model arm (and the optional vinegar bone); assign Think Deeper and the Exit Check."]],
 "key_questions": ["Which of the five jobs is this bone doing?", "Which joint type allows this movement?", "Which muscle is contracting, and which is relaxing?", "Which other systems are involved?"],
 "misconceptions": ["Bones are dead.", "Muscles can push.", "Tendons and ligaments are the same thing.", "Only old people need to think about bone health."],
 "support": ["Label your own body with sticky notes (shoulder, elbow, knee, Achilles tendon).", "Provide a joint picture card for each type.", "Pre-assemble the cardboard joint."],
 "challenge": ["Research how bones heal and how doctors use casts, pins or plates.", "Compare first-, second- and third-class levers in the body (neck, ankle, elbow)."],
 "background": "<p>NASA reports bone mineral density losses of about 1 to 1.5 percent per month in weight-bearing bones during long-duration spaceflight, countered by about 2 hours of daily exercise (including the ARED resistance device). Bone counts: about 270 to 300 at birth, 206 in a typical adult. The National Institutes of Health (NIAMS) notes that up to 90 percent of peak bone mass is acquired by about age 18 in girls and 20 in boys. Simple fractures typically heal in about 6 to 8 weeks in children and teens. The vinegar test: acetic acid dissolves calcium phosphate (hydroxyapatite) over several days, leaving collagen; use a cooked, cleaned bone and wash hands.</p>",
 "sources": ["NASA, Human Research Program: bone loss and exercise countermeasures.", "National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIAMS), Kids and Their Bones: A Guide for Parents.", "OpenStax, Anatomy and Physiology 2e, Chapters 6, 9 and 11.", "National Institutes of Health, Office of Dietary Supplements, Calcium and Vitamin D fact sheets."]
}

PRINT = {
 "directions": "Answer in complete sentences.",
 "items": [
  {"q":"List the five functions of the skeleton with an example of each.","a":"Support (spine), protection (skull), movement (leg bones as levers), making blood cells (red marrow), storing minerals (calcium).","lines":3},
  {"q":"Name four joint types and one place in the body where each is found.","a":"Ball-and-socket (shoulder), hinge (knee), pivot (neck), gliding (wrist); fixed (skull).","lines":2},
  {"q":"Compare tendons and ligaments.","a":"Tendons connect muscle to bone; ligaments connect bone to bone.","lines":2},
  {"q":"Explain how the biceps and triceps bend and straighten your arm.","a":"Biceps contracts to bend while triceps relaxes; triceps contracts to straighten while biceps relaxes.","lines":2},
  {"q":"Give two ways to build strong bones during your teen years.","a":"Weight-bearing exercise; calcium and vitamin D in the diet (also protective gear).","lines":2},
  {"q":"Explain how the nervous, muscular and skeletal systems work together to kick a ball.","a":"Brain signals muscles through nerves; muscles contract and pull on bones; bones act as levers at joints.","lines":3}]
}
