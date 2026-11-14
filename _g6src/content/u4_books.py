from urllib.parse import quote_plus
TITLE = "Unit 4 Book List"
KICKER = "Grade 6 · Unit 4 · Free to read or borrow"
LINK = "Unit 4 book list"

def gut(t): return f"https://www.gutenberg.org/ebooks/search/?query={quote_plus(t)}"
def ol(t): return f"https://openlibrary.org/search?q={quote_plus(t)}"

FREE = [
 ("Common Sense", "Thomas Paine (1776)", "ELA", "The pamphlet from Week 18. Short and readable in sections; try the part answering objections to independence. Older spellings throughout.", gut("Common Sense Paine")),
 ("My Bondage and My Freedom", "Frederick Douglass (1855)", "ELA", "Douglass's second autobiography; the appendix prints his 1852 Fourth of July speech from Week 17. Preview first: describes the violence of slavery.", gut("My Bondage and My Freedom")),
 ("Narrative of the Life of Frederick Douglass", "Frederick Douglass (1845)", "ELA", "His first autobiography, including how he learned to read. Preview first: describes the violence of slavery.", gut("Narrative of the Life of Frederick Douglass")),
 ("The History of Herodotus, Volume 2", "Herodotus, translated by G. C. Macaulay (1890)", "Social Studies", "Books 5 to 9 cover the Royal Road and the Persian Wars (Weeks 16 and 17). Best read in short passages with a parent.", gut("Herodotus Macaulay")),
 ("History of the Peloponnesian War", "Thucydides, translated by Richard Crawley (1874)", "Social Studies", "Book 2 has Pericles' Funeral Oration (Week 17).", gut("Thucydides Crawley")),
 ("The History of Rome, Books 1 to 8", "Livy, translated by D. Spillan (1853)", "Social Studies", "Book 3 tells the story of Cincinnatus (Week 18); Book 1 has Rome's legendary founding.", gut("Livy History of Rome Spillan")),
 ("The History of Rome, Books 9 to 26", "Livy, translated by D. Spillan and Cyrus Edmonds (1849)", "Social Studies", "Book 21 follows Hannibal over the Alps (Week 19).", gut("Livy History of Rome Books 09 to 26")),
]

BORROW = [
 ("Who Was Frederick Douglass?", "April Jones Prince", "ELA", "A short, readable biography for this age.", None),
 ("Susan B. Anthony (Who Was? series)", "Pam Pollack and Meg Belviso", "ELA", "A readable biography of the suffragist from Week 16.", "Who Was Susan B. Anthony"),
 ("Thomas Paine and the Dangerous Word", "Sarah Jane Marsh", "ELA", "An illustrated account of how Common Sense was written and received.", None),
 ("Charles Drew: Doctor Who Got the World Pumped Up to Donate Blood", "Mike Venezia", "Science", "A short, funny biography of the surgeon from Week 18.", "Charles Drew Venezia"),
 ("The Way We Work", "David Macaulay", "Science", "Detailed, beautiful drawings of every body system (Weeks 16 to 20).", None),
 ("Gifted Hands, Kids Edition", "Ben Carson with Gregg Lewis and Deborah Shaw Lewis", "Science", "The pediatric neurosurgeon's story; connects to the nervous system (Week 19).", "Gifted Hands Ben Carson"),
 ("Rotten Romans (Horrible Histories)", "Terry Deary", "Social Studies", "Funny, fact-filled and great for reluctant readers; includes Hannibal and Carthage. Preview for gross and gory jokes.", "Terry Deary Rotten Romans"),
 ("The Ancient Greek World", "Jennifer T. Roberts and Tracy Barrett", "Social Studies", "From the Oxford World in Ancient Times series; covers city-states, democracy and the Persian Wars.", None),
 ("The Ancient Roman World", "Ronald Mellor and Marni McGee", "Social Studies", "Also from the World in Ancient Times series; includes Carthage and Roman Africa.", "Ancient Roman World Mellor McGee"),
]

HTML = ("<h1>Unit 4 Book List</h1><p>Every book here can be read free. The first group is in the public domain and free to read online. "
        "The second group is free to borrow with a public library card: look for it in your library's catalog or its free e-book apps, "
        "or borrow a digital copy through Open Library when one is available. Availability varies by library.</p>"
        "<h2>Free to read online (public domain)</h2><table class='t'><tr><th>Book</th><th>Subject</th><th>Why read it</th></tr>" +
        "".join(f"<tr><td><a href='{u}'><b>{t}</b></a><br><span class='muted'>{a}</span></td><td>{s}</td><td>{w}</td></tr>" for t, a, s, w, u in FREE) +
        "</table><h2>Free to borrow with a library card</h2><table class='t'><tr><th>Book</th><th>Subject</th><th>Why read it</th></tr>" +
        "".join(f"<tr><td><a href='{ol(q or t)}'><b>{t}</b></a><br><span class='muted'>{a}</span></td><td>{s}</td><td>{w}</td></tr>" for t, a, s, w, q in BORROW) +
        "</table><p class='muted'>Parents: preview any book first. Links open a search on Project Gutenberg or Open Library, so you can choose the edition.</p>")
