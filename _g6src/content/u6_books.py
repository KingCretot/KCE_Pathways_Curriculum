from urllib.parse import quote_plus
TITLE = "Unit 6 Book List"
KICKER = "Grade 6 · Unit 6 · Free to read or borrow"
LINK = "Unit 6 book list"

def gut(t): return f"https://www.gutenberg.org/ebooks/search/?query={quote_plus(t)}"
def ol(t): return f"https://openlibrary.org/search?q={quote_plus(t)}"

def ia(t): return f"https://archive.org/search?query={quote_plus(t)}"

FREE = [
 ("The Journal of Christopher Columbus", "translated by Clements R. Markham (1893)", "Social Studies", "The source of the Week 29 and Week 30 excerpts, preserved in Las Casas's abstract. Read short passages with a parent and ask what Columbus wanted his royal readers to believe.", ia("Journal of Christopher Columbus Markham 1893")),
 ("The Memoirs of the Conquistador Bernal Diaz del Castillo", "translated by John Ingram Lockhart (1844)", "Social Studies", "The eyewitness account quoted in Week 27, describing Tenochtitlan. Old-fashioned English and scenes of war; best for parents to preview and read aloud in short sections.", gut("Bernal Diaz del Castillo memoirs")),
 ("Experiments in Plant Hybridization", "Gregor Mendel, translated by William Bateson (1901)", "Science", "Mendel's pea-plant paper behind Weeks 26 and 27. Technical; read the opening pages together and look at his counts of tall and short plants.", ia("Mendel Experiments in Plant Hybridisation Bateson")),
 ("On the Origin of Species", "Charles Darwin (1859)", "Science", "The book that explained natural selection (Week 29). Written for adults; read the short introduction or the chapter on variation together.", gut("On the Origin of Species Darwin")),
]

BORROW = [
 ("Morning Girl", "Michael Dorris", "Social Studies", "A short novel told by a Taíno sister and brother in the Bahamas in 1492, ending with an excerpt from Columbus's journal (Week 29).", "Morning Girl Michael Dorris"),
 ("Encounter", "Jane Yolen, illustrated by David Shannon", "Social Studies", "A picture book telling Columbus's arrival from a Taíno boy's point of view; good for comparing with the journal (Week 29).", "Encounter Jane Yolen"),
 ("Fort Mose", "Glennette Tilley Turner", "Social Studies", "The story of the first legally sanctioned free Black town in what is now the United States, near St. Augustine (Week 30 preview).", "Fort Mose Glennette Tilley Turner"),
 ("Gregor Mendel: The Friar Who Grew Peas", "Cheryl Bardoe, illustrated by Jos. A. Smith", "Science", "An illustrated biography of Mendel and his pea experiments (Weeks 26 and 27).", "Gregor Mendel Friar Who Grew Peas"),
 ("One Beetle Too Many: The Extraordinary Adventures of Charles Darwin", "Kathryn Lasky, illustrated by Matthew Trueman", "Science", "Darwin's life and voyage on the Beagle for young readers (Week 29).", "One Beetle Too Many Lasky"),
 ("The Beak of the Finch", "Jonathan Weiner", "Science", "The Pulitzer Prize-winning account of the Grants' finch studies (Week 29). Adult nonfiction for parents to read and summarize.", "Beak of the Finch Weiner"),
]

HTML = ("<h1>Unit 6 Book List</h1><p>Every book here can be read free. The first group is in the public domain and free to read online. "
        "The second group is free to borrow with a public library card: look for it in your library's catalog or its free e-book apps, "
        "or borrow a digital copy through Open Library when one is available. Availability varies by library.</p>"
        "<h2>Free to read online (public domain)</h2><table class='t'><tr><th>Book</th><th>Subject</th><th>Why read it</th></tr>" +
        "".join(f"<tr><td><a href='{u}'><b>{t}</b></a><br><span class='muted'>{a}</span></td><td>{s}</td><td>{w}</td></tr>" for t, a, s, w, u in FREE) +
        "</table><h2>Free to borrow with a library card</h2><table class='t'><tr><th>Book</th><th>Subject</th><th>Why read it</th></tr>" +
        "".join(f"<tr><td><a href='{ol(q or t)}'><b>{t}</b></a><br><span class='muted'>{a}</span></td><td>{s}</td><td>{w}</td></tr>" for t, a, s, w, q in BORROW) +
        "</table><p class='muted'>Parents: preview any book first. Links open a search on Project Gutenberg, the Internet Archive or Open Library, so you can choose the edition.</p>")
