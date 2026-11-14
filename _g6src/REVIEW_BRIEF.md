# KCE Pathways Grade 6 — independent review brief

You are an independent reviewer for KingCretot Experience (KCE), a homeschool-focused education company. The owner,
Jonathan, requires a second and third set of eyes on every lesson before he sees it, for consistency and value.
You did not write these lessons. Be skeptical and specific. Do NOT edit any files: report findings only.

## What to review
Lesson content lives in /home/claude/g6build/content/ as Python files (wN_subject.py: LESSON, TEACHER, PRINT dicts;
wN_parent.py: weekly parent guide; uN_*.py: unit pages). Built pages are in /home/claude/repos/KCE_Pathways_Curriculum/grade6/.
The engine is /home/claude/g6build/engine.js (answer checking: `num` exact within tol; `text`/`blanks` accept a list of
strings matched after normalizing case/punctuation/articles, or `{"all": [[...],[...]]}` meaning every group must have at
least one keyword appear as a substring of the student's answer).

## Jonathan's rules (all must hold)
- Grade 6 middle school: challenge critical thinking (analysis, evidence, multi-step problems, defending positions). No filler repetition.
- Real-world examples and experiences designed for homeschool students; hands-on (kinesthetic) activities; lots of visuals, especially science and social studies.
- Most questions make students produce the answer (type it, label, order, write), not choose it. Multiple choice only where it truly fits.
- Every lesson opens by reconnecting to the previous lesson (vocabulary, method, understanding), with as many questions as needed.
- Each lesson has a detailed, robust teacher plan; a weekly parent guide; printable page; unit supply list; projects with rubrics in ELA, Science, Social Studies.
- Standards lean on Florida B.E.S.T./FAST (and NGSSS science) but are written for global thinkers and represent all students.
- History is true and complete and includes all ethnicities; never Eurocentric; say "Indigenous Peoples" and name the nation. Egypt (Kemet) is taught as an African civilization.
- Poetry: pre-1929 poems may be printed in full; later poems (e.g., Maya Angelou) must only be linked, never reproduced.
- American English spelling always. Say "lessons," never "sessions." Brand: KingCretot Experience.
- There is NO page-count limit. Pages run as long as the content needs. Check only that nothing is cut off or broken across pages badly (a table row or a diagram split mid-way).

## Report format
For each file reviewed, list findings as: severity (HIGH = factually wrong, wrong answer key, broken/unfair auto-check,
rule violation; MEDIUM = weak pedagogy, unclear wording, answer acceptance too strict or too loose; LOW = polish),
the exact location (file, question text), the problem, and the specific fix. Verify every math answer by computing it.
Verify historical/scientific facts; flag anything doubtful and say what is accurate, citing a reliable source if you check one.
End with an overall verdict per lesson: ready / ready after fixes / needs rework.

## Added after Week 3 review
- Florida minimum wage is $15.00 since Sept 30, 2026: every wage in a Florida setting must be at least that.
- Grade 6 decimal work must include thousandths and multi-step real-world problems.
- "Name two" items must use two distinct blanks, never one text box with duplicate keyword groups.
- Hands-on record items need model answers too.

## Added after Week 5 review
- Checkpoints: one try, no answer reveal, separate checkpoint score in the payload; open checkpoint items carry pts; teacher adds rubric points.
- A checkpoint must not repeat an item or answer shown earlier on the same page.
- No content before it is taught (percents arrive in Unit 3; rhyme scheme in Unit 3).
- Printable items need model answers, never "Answers vary".
- Brand names include software (Zoom, Libby, IBM, Formspree) in student- or parent-facing text.

## Added after Week 6 review
- "Simplest form" items must be text items with the exact simplest fraction; numeric checks accept any equivalent value.
- Never let a check accept the misconception (e.g. "north to south"); add "none" lists.
- Do not score students on content the lesson did not teach (every rubric line must trace to the lesson text).
- Egypt is never set apart from "the rest of Africa" in wording.
- Use realistic amounts (a 40-person reunion is not $96).

## Week 7 additions
- Never present an etymology without checking it (ferry is Germanic, not Latin fer).
- Copy standard wording from CPALMS exactly; ELA roots = ELA.6.V.1.2 (V.1.3 is context clues).
- Model answers may use only facts that appear in the lesson text when the rubric says "from the passage".
- No bare common-word accepts (e.g. "just" for E. E. Just). Keyword keys need "none" lists for negation and wrong regions.
- "Upper Egypt in the south" not "from the south" when the meaning is inside Egypt.
- Do not modify geo.NILE for one map; use a local, more detailed river line when a map zooms in.

## Week 8 additions
- Florida B.E.S.T. Grade 6 ratio benchmarks are MA.6.AR.3.1 to 3.5 (there is no AR.4).
- Grade 6 SS benchmarks naming Kush: SS.6.W.3.18 (Kush and Axum) and SS.6.E.3.3 (economies). SS.6.W.2.8 is Mesopotamian key figures.
- Bessie Coleman's same-gate refusal was in Waxahachie, Texas (and Houston), not Orlando.
- Timelines need uniform scale; check bar positions against real dates.
- Blanks must not accept a word already printed in the sentence (circular answers).

## Week 9 additions
- MA.6.AR.3.3 is the ratio-table benchmark. Cell theory is SC.6.L.14.2; SC.6.L.14.3 is homeostasis.
- MLA 9: when an organization is author and publisher, start with the title; in-text uses a short title.
- Quote statistics as published (Ferrario 2014: an average of 97 percent, not "up to").
- Quote poems in the version you name (Coleridge 1798 vs 1817 wording).
- No circular accepts (a name printed in the question). No animal-cruelty examples.
- Salt dough and other craft materials: add no-tasting and pet-safety notes.
- After the first save(), LESSON dicts are frozen literals; edit passages and SVGs inside LESSON (constants at the top may be unused).
- Engine: numeric phrase accepts no longer match inside fractions or decimals (10 does not match 1/10).

## Week 11 additions
- Check earlier weeks before adding a scientist or context (Turner was Week 1). Keep levels of organization brief: Unit 4 Week 1 covers it in depth.
- Do not use percents before Week 12. Name the correct week in "next" lines (check scope.py).
- Public-domain text only: Dickinson from the 1891 printing, not Johnson or Franklin editions.
- ELA.6.R.1.4 names the sonnet and the villanelle: sonnet taught Week 12, villanelle Week 14.
- Present debated attributions as debated (Enheduanna). Add a primary-source excerpt when SS.6.W.1.3 is listed.

- Engine norm() strips the words a/an/the: never key letter patterns with spaces ("a b a b"); key rhyme schemes as one token ("abab") and ask for letters with no spaces.
- Quotations (Jonathan, Nov 14): if the original text is British, quote it exactly in its British spelling (e.g., Legge's "labour") and add a short note or gloss; never Americanize a quotation. All of KCE's own writing stays American English.
- Checkpoint open items never show their rubric to the student (engine fix Nov 14); do not put answers in checkpoint question text either.
- Engine (Nov 14): norm() and parseNum() turn the Unicode minus (−) and en dash into a hyphen, so −18 and -18 grade the same; keys for negatives may use either.
- Never key the symbols < or > (norm strips them). Ask for the words less/greater instead.

## Added Nov 14 (Week 16 review)
- Matching treats "-" as a word boundary: a bare key "75" also accepts "-75", and a none term "6" also rejects "-6". Anchor positive-number keys with "^" ("^75") and never put a bare number in a none list when the correct answer is its negative.
- A none term matches at any word start: "ii" in a none list rejects the correct answer "iii". Check every none term against the correct answer.
- scope.py is the authority for unit names and week titles; "next" lines must match it.
- Standards text must match CPALMS word for word (ELA.6.R.2.4 says "identifying"; ELA.6.C.1.3 is "Write and support a claim using logical reasoning, relevant evidence from sources, elaboration, and a logical organizational structure with varied transitions.").
- Integer operations (MA.6.NSO.4.1, 4.2) are Grade 6 B.E.S.T., taught in Weeks 18 and 19.
- Ordered-pair answers: key as plain strings ("(−6, −1)") so order matters; keyword groups accept swapped pairs.
- Never put a word printed in the question into its key (circular accept).
- CPALMS: SS.6.W.3.2 = Greek democratic concepts; SS.6.W.3.4 = Persian and Peloponnesian Wars; ELA.6.R.3.4 = "Identify rhetorical appeals in a text."
- scope.py also sets the math money thread for each week (math_money); follow it.
- Pet and young-child safety notes for food, bones, balloons and small parts.
- Engine: parseNum now accepts a leading "+" (e.g., "+145").
- Name Indigenous nations specifically; say "Indigenous Peoples." Present debated attributions as debated.
- CPALMS: SS.6.C.1.2 is archived; use SS.6.CG.1.2-1.4 for Rome's influence, rule of law, civic virtue.
- Every open item's model answer must meet its own min word count (the engine's word gate); keep min at or below about 85% of the model's length.
- Positive answers whose negative is a likely wrong answer need "^" anchors, even in plain-string keys ("^(4, 7)", "^-7" for "only the greater").
- Practice-item rubrics are visible to students: write them as criteria ("Correct total for Bank A"), never with the numeric answer. Superscript digits are stripped by norm(): never key "6⁵"; use blanks for base and exponent.
