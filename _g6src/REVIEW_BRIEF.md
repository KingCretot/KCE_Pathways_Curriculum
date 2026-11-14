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
- Every printed page must fit cleanly (no spillover).

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
