from urllib.parse import quote_plus
TITLE = "Unit 2 Book List"
KICKER = "Grade 6 · Unit 2 · Free to read or borrow"
LINK = "Unit 2 book list"

def gut(t): return f"https://www.gutenberg.org/ebooks/search/?query={quote_plus(t)}"
def ol(t): return f"https://openlibrary.org/search?q={quote_plus(t)}"

FREE = [
 ("Micrographia", "Robert Hooke (1665)", "Science", "The book where Hooke first used the word \"cell,\" with his famous drawings of cork and insects seen through a microscope (Week 6). Look at the pictures together.", gut("Micrographia Hooke")),
 ("The Rime of the Ancient Mariner", "Samuel Taylor Coleridge (1798)", "ELA and Science", "The poem behind \"Water, water, every where, / Nor any drop to drink\" (1817 wording) from the Week 9 osmosis lesson.", gut("Rime of the Ancient Mariner")),
 ("The Negro", "W. E. B. Du Bois (1915)", "Social Studies (parents and strong readers)", "Du Bois's early history of Africa, with chapters on Egypt, Ethiopia and Kush written to answer the racist histories of his time (Week 7). Some language is dated.", gut("The Negro Du Bois")),
 ("The Histories, Book II", "Herodotus, translated by G. C. Macaulay (1890)", "Social Studies (parents and strong readers)", "The Greek visitor's description of Egypt from Week 7, a primary source to read with a critical eye.", gut("Herodotus Macaulay"))]

BORROW = [
 ("Fly High! The Story of Bessie Coleman", "Louise Borden and Mary Kay Kroeger", "ELA", "A biography of the pilot from the Week 8 article, good for comparing details with the summary you wrote.", ""),
 ("Nobody Owns the Sky: The Story of \"Brave Bessie\" Coleman", "Reeve Lindbergh", "ELA", "A short illustrated biography of Bessie Coleman in verse, good for a family read-aloud.", ""),
 ("Cells: An Owner's Handbook", "Carolyn Fisher", "Science", "A funny, illustrated guide to the cells in your body, matching Weeks 6, 7 and 9.", ""),
 ("Coral Reefs", "Seymour Simon", "Science and ELA", "Photographs and facts about coral reefs, a good extra source for the Week 9 note-taking practice.", "Coral Reefs Seymour Simon"),
 ("The African Origin of Civilization: Myth or Reality", "Cheikh Anta Diop", "Social Studies (parents)", "The English translation (1974) of Diop's argument from Week 7. Adult reading, for parents who want to go deeper.", ""),
 ("Search your library: Kush, Nubia and Aksum", "Many authors", "Social Studies", "Children's nonfiction on the Kingdom of Kush, Meroe and Aksum varies by library. Search these topics in your library's catalog and check that the book treats Nubia as its own civilization, not just Egypt's neighbor.", "Kingdom of Kush Nubia")]

HTML = ("<h1>Unit 2 Book List</h1><p>Every book here can be read free. The first group is in the public domain and free to read online. "
        "The second group is free to borrow with a public library card: look for it in your library's catalog or its free e-book apps, "
        "or borrow a digital copy through Open Library when one is available. Availability varies by library.</p>"
        "<h2>Free to read online (public domain)</h2><table class='t'><tr><th>Book</th><th>Subject</th><th>Why read it</th></tr>" +
        "".join(f"<tr><td><a href='{u}'><b>{t}</b></a><br><span class='muted'>{a}</span></td><td>{s}</td><td>{w}</td></tr>" for t, a, s, w, u in FREE) +
        "</table><h2>Free to borrow with a library card</h2><table class='t'><tr><th>Book</th><th>Subject</th><th>Why read it</th></tr>" +
        "".join(f"<tr><td><a href='{ol(q or t)}'><b>{t}</b></a><br><span class='muted'>{a}</span></td><td>{s}</td><td>{w}</td></tr>" for t, a, s, w, q in BORROW) +
        "</table><p class='muted'>Parents: preview any book first. Links open a search on Project Gutenberg or Open Library, so you can choose the edition.</p>")
