from urllib.parse import quote_plus
TITLE = "Unit 5 Book List"
KICKER = "Grade 6 · Unit 5 · Free to read or borrow"
LINK = "Unit 5 book list"

def gut(t): return f"https://www.gutenberg.org/ebooks/search/?query={quote_plus(t)}"
def ol(t): return f"https://openlibrary.org/search?q={quote_plus(t)}"

def ia(t): return f"https://archive.org/search?query={quote_plus(t)}"

FREE = [
 ("The Call of the Wild", "Jack London (1903)", "ELA", "The Unit 5 novel. Preview first: it includes violence toward dogs and, in Chapter VII, an attack in which people are killed. Older words and a few hurtful terms of its time; read with an adult.", gut("Call of the Wild London")),
 ("White Fang", "Jack London (1906)", "ELA", "London's companion novel, which reverses Buck's journey: a wild wolf-dog comes into the human world. Same content cautions as The Call of the Wild.", gut("White Fang London")),
 ("A Geographical Historie of Africa", "Leo Africanus, translated by John Pory (1600)", "Social Studies", "The source of Week 23's description of Timbuktu's scholars and book trade. Very old spelling; best read in short passages with a parent.", ia("Leo Africanus history and description of Africa Pory")),
 ("Travels in Asia and Africa, 1325-1354", "Ibn Battuta, translated by H. A. R. Gibb (1929)", "Social Studies", "The selections quoted in Weeks 22 and 24 on Mali and Kilwa. Public domain in the United States; free scans online. Uses some terms of its time.", ia("Ibn Battuta Travels in Asia and Africa Gibb")),
]

BORROW = [
 ("Sundiata: An Epic of Old Mali", "D. T. Niane, translated by G. D. Pickett", "Social Studies", "The griot Mamadou Kouyaté's telling of the epic from Week 22. Readable for strong readers; read together.", "Sundiata Epic of Old Mali Niane"),
 ("The Royal Kingdoms of Ghana, Mali, and Songhay", "Patricia and Fredrick McKissack", "Social Studies", "An award-winning history of the three West African empires for young readers (Weeks 21 to 23).", None),
 ("Mansa Musa: The Lion of Mali", "Khephra Burns, illustrated by Leo and Diane Dillon", "Social Studies", "A beautifully illustrated story of Mansa Musa's youth.", None),
 ("The Bad-Ass Librarians of Timbuktu", "Joshua Hammer", "Social Studies", "The adult nonfiction account of the 2012 to 2013 manuscript rescue (Week 23). For parents to read and summarize; contains strong language and violence.", "Bad-Ass Librarians of Timbuktu"),
 ("Great Zimbabwe", "Ann Kerns (or another young readers' title from your library)", "Social Studies", "A short overview of the stone city and its builders (Week 24). Check that any older book credits the Shona's ancestors.", "Great Zimbabwe juvenile"),
 ("Everglades", "Jean Craighead George, illustrated by Wendell Minor", "Science", "A storyteller poles a canoe through the Everglades and its food webs (Weeks 21 and 22).", "Everglades Jean Craighead George"),
 ("The Water Cycle (or a similar title)", "Your library's young readers' science shelf", "Science", "Any clear, illustrated water cycle book supports Week 23; look for one that mentions groundwater.", "water cycle juvenile"),
 ("Manatee Winter", "Kathleen Weidner Zoehfeld", "Science", "A manatee mother and calf travel to a warm Florida spring (Weeks 21 and 23).", None),
]

HTML = ("<h1>Unit 5 Book List</h1><p>Every book here can be read free. The first group is in the public domain and free to read online. "
        "The second group is free to borrow with a public library card: look for it in your library's catalog or its free e-book apps, "
        "or borrow a digital copy through Open Library when one is available. Availability varies by library.</p>"
        "<h2>Free to read online (public domain)</h2><table class='t'><tr><th>Book</th><th>Subject</th><th>Why read it</th></tr>" +
        "".join(f"<tr><td><a href='{u}'><b>{t}</b></a><br><span class='muted'>{a}</span></td><td>{s}</td><td>{w}</td></tr>" for t, a, s, w, u in FREE) +
        "</table><h2>Free to borrow with a library card</h2><table class='t'><tr><th>Book</th><th>Subject</th><th>Why read it</th></tr>" +
        "".join(f"<tr><td><a href='{ol(q or t)}'><b>{t}</b></a><br><span class='muted'>{a}</span></td><td>{s}</td><td>{w}</td></tr>" for t, a, s, w, q in BORROW) +
        "</table><p class='muted'>Parents: preview any book first. Links open a search on Project Gutenberg or Open Library, so you can choose the edition.</p>")
