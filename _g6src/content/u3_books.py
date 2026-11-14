from urllib.parse import quote_plus
TITLE = "Unit 3 Book List"
KICKER = "Grade 6 · Unit 3 · Free to read or borrow"
LINK = "Unit 3 book list"

def gut(t): return f"https://www.gutenberg.org/ebooks/search/?query={quote_plus(t)}"
def ol(t): return f"https://openlibrary.org/search?q={quote_plus(t)}"

FREE = [
 ("The Weary Blues", "Langston Hughes (1926)", "ELA", "Hughes's first book, with \"The Negro Speaks of Rivers\" and \"Epilogue\" (\"I, too, sing America\") from Weeks 13 and 14. Read the short lyric poems aloud.", gut("The Weary Blues Hughes")),
 ("The Book of American Negro Poetry", "edited by James Weldon Johnson (1922)", "ELA", "The anthology that holds McKay's \"The Tired Worker,\" Fauset's \"Oriflamme\" and Georgia Douglas Johnson's \"The Heart of a Woman.\" Johnson's preface is a strong read for parents. Preview first: a few poems deal with violence.", gut("Book of American Negro Poetry")),
 ("The Complete Poems of Paul Laurence Dunbar", "Paul Laurence Dunbar (1913)", "ELA", "Home of \"Sympathy\" (Week 11) and \"We Wear the Mask\" (the Week 15 checkpoint). Many poems are in dialect, which Dunbar wrote alongside standard English.", gut("Complete Poems Paul Laurence Dunbar")),
 ("A Child's Garden of Verses", "Robert Louis Stevenson (1885)", "ELA", "\"From a Railway Carriage\" (Week 12) and dozens of short poems with strong rhythm, good for recitation practice.", gut("A Child's Garden of Verses")),
 ("Leaves of Grass", "Walt Whitman (1891–92 edition)", "ELA (parents and strong readers)", "Whitman's life work, including \"I Hear America Singing\" (Week 14). Long; dip in rather than read straight through.", gut("Leaves of Grass Whitman")),
 ("The Children of the Night", "Edwin Arlington Robinson (1897)", "ELA", "Robinson's early poems, including the villanelle \"The House on the Hill\" (Week 14) and the famous \"Richard Cory.\"", gut("Children of the Night Robinson")),
 ("The Chinese Classics: Confucian Analects", "translated by James Legge (1861)", "Social Studies", "The sayings of Confucius from Week 13, in the translation the lesson quotes. Short passages make good discussion starters.", gut("Confucian Analects Legge")),
 ("The Periplus of the Erythraean Sea", "translated by Wilfred H. Schoff (1912)", "Social Studies (parents and strong readers)", "The first-century merchant's guide from Week 14, with Adulis, Aksum, India and the monsoon trade. Free on Wikisource.", "https://en.wikisource.org/wiki/Periplus_of_the_Erythraean_Sea")]

BORROW = [
 ("Langston Hughes (Poetry for Young People)", "edited by David Roessel and Arnold Rampersad", "ELA", "An illustrated selection of Hughes's poems with short notes, a natural next step after Week 13.", "Poetry for Young People Langston Hughes"),
 ("Love to Langston", "Tony Medina", "ELA", "A biography of Langston Hughes told in poems, for readers who want to know the person behind the poetry.", ""),
 ("Harlem Stomp! A Cultural History of the Harlem Renaissance", "Laban Carrick Hill", "ELA and Social Studies", "A richly illustrated history of the writers, musicians and artists of the Harlem Renaissance.", ""),
 ("Seeds of Change: Wangari's Gift to the World", "Jen Cullerton Johnson", "Science", "A picture biography of Kenyan scientist Wangari Maathai, connecting plant science to community action; a quick read that fits the field guide unit.", ""),
 ("Tiny Creatures: The World of Microbes", "Nicola Davies", "Science", "An illustrated introduction to microorganisms and what they do, matching Week 14.", ""),
 ("The Silk Road: Explore the World's Most Famous Trade Route", "Kathy Ceceri", "Social Studies", "Hands-on projects and history of the Silk Roads, good support for the Week 15 travel journal.", "Silk Road Kathy Ceceri"),
 ("Search your library: ancient Mesopotamia, the Indus Valley and ancient China", "Many authors", "Social Studies", "Children's nonfiction on these topics varies by library; look for books that use museum photographs and recent archaeology.", "ancient Mesopotamia children")]

HTML = ("<h1>Unit 3 Book List</h1><p>Every book here can be read free. The first group is in the public domain and free to read online. "
        "The second group is free to borrow with a public library card: look for it in your library's catalog or its free e-book apps, "
        "or borrow a digital copy through Open Library when one is available. Availability varies by library.</p>"
        "<h2>Free to read online (public domain)</h2><table class='t'><tr><th>Book</th><th>Subject</th><th>Why read it</th></tr>" +
        "".join(f"<tr><td><a href='{u}'><b>{t}</b></a><br><span class='muted'>{a}</span></td><td>{s}</td><td>{w}</td></tr>" for t, a, s, w, u in FREE) +
        "</table><h2>Free to borrow with a library card</h2><table class='t'><tr><th>Book</th><th>Subject</th><th>Why read it</th></tr>" +
        "".join(f"<tr><td><a href='{ol(q or t)}'><b>{t}</b></a><br><span class='muted'>{a}</span></td><td>{s}</td><td>{w}</td></tr>" for t, a, s, w, q in BORROW) +
        "</table><p class='muted'>Parents: preview any book first. Links open a search on Project Gutenberg or Open Library, so you can choose the edition.</p>")
