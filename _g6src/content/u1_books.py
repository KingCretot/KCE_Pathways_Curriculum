from urllib.parse import quote_plus
TITLE = "Unit 1 Book List"
KICKER = "Grade 6 · Unit 1 · Free to read or borrow"
LINK = "Unit 1 book list"

def gut(t): return f"https://www.gutenberg.org/ebooks/search/?query={quote_plus(t)}"
def ol(t): return f"https://openlibrary.org/search?q={quote_plus(t)}"

FREE = [
 ("Mountain Interval", "Robert Frost (1916)", "ELA", "The collection that includes \"The Road Not Taken\" from the Week 5 checkpoint.", gut("Mountain Interval Frost")),
 ("The Weary Blues", "Langston Hughes (1926)", "ELA", "Hughes's first book, which collected \"Mother to Son\" from Week 3.", gut("The Weary Blues Hughes")),
 ("Lyrics of Lowly Life", "Paul Laurence Dunbar (1896)", "ELA", "Poems by one of the first nationally famous Black American poets.", gut("Lyrics of Lowly Life")),
 ("Anne of Green Gables", "L. M. Montgomery (1908)", "ELA", "A novel full of strong voice, dialogue and a character who changes.", gut("Anne of Green Gables")),
 ("Black Beauty", "Anna Sewell (1877)", "ELA", "A whole novel told in first person, by a horse. Good for talking about point of view.", gut("Black Beauty Sewell"))]

BORROW = [
 ("Brown Girl Dreaming", "Jacqueline Woodson", "ELA", "A memoir in verse about growing up Black in South Carolina and Brooklyn. A model personal narrative."),
 ("Hidden Figures (Young Readers' Edition)", "Margot Lee Shetterly", "Science", "Katherine Johnson and the Black women mathematicians at NASA, from the Week 5 lesson."),
 ("The Boy Who Harnessed the Wind (Young Readers Edition)", "William Kamkwamba and Bryan Mealer", "Science", "A teenager in Malawi builds a windmill from scrap, using science to solve a real problem."),
 ("Lucy Long Ago: Uncovering the Mystery of Where We Came From", "Catherine Thimmesh", "Social Studies", "How scientists found and studied Lucy (Dinkinesh), from Week 3."),
 ("Every Bone Tells a Story: Hominin Discoveries, Deductions, and Debates", "Jill Rubalcaba and Peter Robertshaw", "Social Studies", "Four famous fossil finds and how scientists argued about what they mean."),
 ("Sundiata: Lion King of Mali", "David Wisniewski", "Social Studies", "A picture-book retelling of the griot epic from Week 1, good for a family read-aloud.")]

HTML = ("<h1>Unit 1 Book List</h1><p>Every book here can be read free. The first group is in the public domain and free to read online. "
        "The second group is free to borrow with a public library card: look for it in your library's catalog or its free reading apps (such as Libby or Hoopla), "
        "or borrow a digital copy through Open Library when one is available. Availability varies by library.</p>"
        "<h2>Free to read online (public domain)</h2><table class='t'><tr><th>Book</th><th>Subject</th><th>Why read it</th></tr>" +
        "".join(f"<tr><td><a href='{u}'><b>{t}</b></a><br><span class='muted'>{a}</span></td><td>{s}</td><td>{w}</td></tr>" for t, a, s, w, u in FREE) +
        "</table><h2>Free to borrow with a library card</h2><table class='t'><tr><th>Book</th><th>Subject</th><th>Why read it</th></tr>" +
        "".join(f"<tr><td><a href='{ol(t)}'><b>{t}</b></a><br><span class='muted'>{a}</span></td><td>{s}</td><td>{w}</td></tr>" for t, a, s, w in BORROW) +
        "</table><p class='muted'>Parents: preview any book first. Links open a search on Project Gutenberg or Open Library, so you can choose the edition.</p>")
