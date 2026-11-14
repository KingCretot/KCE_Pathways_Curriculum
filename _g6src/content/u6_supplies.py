import importlib.util, os, html
HERE = os.path.dirname(os.path.abspath(__file__))
TITLE = "Unit 6 Supply List"
KICKER = "Grade 6 · Unit 6 · Weeks 26 to 30"
LINK = "Unit 6 supply list"
NAMES = {"math": "Math", "ela": "ELA", "science": "Life Science", "socialstudies": "World and American History"}

def _load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

EVERY = ["A computer or tablet with a camera, microphone and the video-call app used for live lessons", "A notebook or binder for each subject, pencils, an eraser and colored pencils",
         "Index cards, graph paper and a ruler with centimeters and millimeters", "A printer (or a local print shop) for printable pages and project labels"]
rows = ""
for w in range(26, 31):
    for s in ("math", "ela", "science", "socialstudies"):
        p = os.path.join(HERE, f"w{w}_{s}.py")
        if not os.path.exists(p): continue
        L = _load(p).LESSON
        mats = list(L.get("handson", {}).get("materials", []))
        T = _load(p).TEACHER
        def _w(x): return set(w.strip(',.()') for w in x.lower().split() if len(w) > 3)
        for t in ([] if mats else T.get("materials", [])):
            tl = t.lower()
            if tl.startswith("the interactive lesson") or "printable" in tl or "checkpoint" in tl or "rubric" in tl or "real event" in tl or "the student's" in tl: continue
            if any(len(_w(t) & _w(x)) >= max(2, len(_w(t)) // 2) for x in mats): continue
            if tl not in [x.lower() for x in mats]: mats.append(t)
        seen = []; mats = [x for x in mats if not (x.lower().replace("a clock or timer", "a timer or clock") in seen or seen.append(x.lower().replace("a clock or timer", "a timer or clock")))]
        if mats:
            rows += f"<tr><td>Week {w}</td><td>{NAMES[s]}</td><td><b>{L['handson']['title']}</b><ul>" + "".join(f"<li>{m}</li>" for m in mats) + "</ul></td></tr>"
HTML = ("<h1>Unit 6 Supply List</h1><p>Almost everything comes from a normal home kitchen, pantry or junk drawer. Gather each week's items before Monday. "
        "Items marked optional can be skipped. <b>Safety for Unit 6:</b> an adult helps with scissors and hole punches; keep beads, buttons, beans, marbles, coins, sugar cubes, paper dots and other small items away from young children (choking hazard) and pets; don't eat foods used in activities, check for food allergies before tasting anything, and keep salt dough away from dogs and cats; visit stores only with a parent; survey only people a parent approves and never collect personal information; use only websites your parent approves; never dig at real archaeological sites or collect artifacts from public land; peel up tape and sticky notes gently and keep string off walkways; wipe up spills; wash hands after handling soil, seeds or food.</p><h2>Unit 5 projects</h2><ul><li>ELA: The Call of the Wild, paper and markers or a device for the creative response</li><li>Science: a notebook for field data, a thermometer, a ruler or measuring tape, string and 4 stakes or pencils for a 1-meter quadrat, a phone or tablet for photos (optional), and poster board or a device for slides</li><li>Social Studies: poster board or cardboard for a game board, markers, index cards, a die and small items for game pieces</li></ul><h2>Every week</h2><ul>" + "".join(f"<li>{e}</li>" for e in EVERY) + "</ul>"
        "<h2>Week by week</h2><table class='t'><tr><th>Week</th><th>Subject</th><th>Activity and supplies</th></tr>" + rows + "</table>"
        "<style>.t tr{break-inside:avoid}.t td{vertical-align:top;font-size:13px}.t ul{margin:4px 0 0 18px;padding:0}</style>")
