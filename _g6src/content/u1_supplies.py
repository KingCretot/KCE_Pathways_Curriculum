import importlib.util, os, html
HERE = os.path.dirname(os.path.abspath(__file__))
TITLE = "Unit 1 Supply List"
KICKER = "Grade 6 · Unit 1 · Weeks 1 to 5"
LINK = "Unit 1 supply list"
NAMES = {"math": "Math", "ela": "ELA", "science": "Life Science", "socialstudies": "World and American History"}

def _load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

EVERY = ["A computer or tablet with a camera, microphone and Zoom for live lessons", "A notebook or binder for each subject, pencils, an eraser and colored pencils",
         "Index cards, graph paper and a ruler with centimeters and millimeters", "A printer (or a local print shop) for printable pages and project labels"]
rows = ""
for w in range(1, 6):
    for s in ("math", "ela", "science", "socialstudies"):
        p = os.path.join(HERE, f"w{w}_{s}.py")
        if not os.path.exists(p): continue
        L = _load(p).LESSON
        mats = L.get("handson", {}).get("materials", [])
        if mats:
            rows += f"<tr><td>Week {w}</td><td>{NAMES[s]}</td><td><b>{L['handson']['title']}</b><ul>" + "".join(f"<li>{m}</li>" for m in mats) + "</ul></td></tr>"
HTML = ("<h1>Unit 1 Supply List</h1><p>Almost everything comes from a normal home kitchen, pantry or junk drawer. Gather each week's items before Monday. "
        "Items marked optional can be skipped.</p><h2>Every week</h2><ul>" + "".join(f"<li>{e}</li>" for e in EVERY) + "</ul>"
        "<h2>Week by week</h2><table class='t'><tr><th>Week</th><th>Subject</th><th>Activity and supplies</th></tr>" + rows + "</table>"
        "<style>.t td{vertical-align:top;font-size:13px}.t ul{margin:4px 0 0 18px;padding:0}</style>")
