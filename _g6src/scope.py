# KCE Pathways Grade 6 — scope and sequence (30 weeks, 6 units of 5 weeks).
# Week 5 of every unit = new learning + unit checkpoint (+ unit project due in ELA, Science, Social Studies).
# Mid-year comprehensive mastery test after Week 15; end-of-year comprehensive mastery test after Week 30.

UNITS = {
    "math": [
        ("Unit 1: Number Power", ["Whole-Number Operations and Long Division", "Adding and Subtracting Decimals", "Multiplying Decimals", "Dividing Decimals", "GCF, LCM and Unit 1 Checkpoint"]),
        ("Unit 2: Fractions and Ratios", ["Multiplying Fractions", "Dividing Fractions and Mixed Numbers", "Ratios and Ratio Language", "Ratio Tables and Equivalent Ratios", "Unit 2 Review and Checkpoint"]),
        ("Unit 3: Rates and Percents", ["Unit Rates", "Understanding Percents", "Percents in Real Life", "Converting Units with Ratios", "Mid-Year Review"]),
        ("Unit 4: Integers and the Coordinate Plane", ["Integers, Opposites and Absolute Value", "The Four-Quadrant Coordinate Plane", "Adding and Subtracting Integers", "Multiplying and Dividing Integers", "Unit 4 Review and Checkpoint"]),
        ("Unit 5: Expressions and Equations", ["Exponents and Order of Operations", "Writing and Evaluating Expressions", "Solving One-Step Equations", "Inequalities", "Unit 5 Review and Checkpoint"]),
        ("Unit 6: Geometry and Data", ["Area of Triangles, Quadrilaterals and Composite Figures", "Nets, Surface Area and Volume", "Statistical Questions and Data Displays", "Mean, Median, Mode and Range", "End-of-Year Review"]),
    ],
    "math_money": [  # financial literacy thread woven into each math week
        ["Building a weekly budget", "Reading receipts and making change", "Earnings: hourly pay and hours worked", "Unit prices and buying in bulk", "Saving goals: how long will it take?"],
        ["Splitting costs fairly", "Recipes, servings and grocery costs", "Comparing deals with ratios", "Price tables and better buys", "Budget review"],
        ["Price per unit at the store", "Sales tax", "Discounts, tips and markups", "Currency exchange", "Mid-year money review"],
        ["Bank balances, deposits and withdrawals", "Mapping a business route", "Debt and credit: going below zero", "Profit and loss", "Money review"],
        ["Simple interest and growth", "Writing cost formulas", "Solving for a missing price", "Staying within a budget (inequalities)", "Money review"],
        ["Pricing a room makeover by area", "Packaging and shipping costs", "Surveying customers", "Comparing prices with averages", "End-of-year money review"],
    ],
    "ela": [
        ("Unit 1: Stories That Shape Us (Narrative)", ["Reading Like a Writer: Story Elements and How Rubrics Work", "Character and Point of View", "Theme in Story and Poem", "Crafting Narrative: Dialogue, Pacing and Description", "Unit 1 Checkpoint and Personal Narrative Project"]),
        ("Unit 2: Explaining the World (Informational)", ["Central Idea and Supporting Details", "Text Structures", "Summarizing Without Copying", "Writing to Inform: Research Notes and Citations", "Unit 2 Checkpoint and Informational Article Project"]),
        ("Unit 3: The Power of Poetry", ["Figurative Language", "Sound and Structure in Poetry", "The Harlem Renaissance Poets", "Poems in Conversation Across Time", "Mid-Year Review and Poetry Analysis Project"]),
        ("Unit 4: Making the Case (Argument)", ["Claims, Reasons and Evidence", "Evaluating Arguments and Spotting Weak Reasoning", "Counterclaims and Rebuttals", "Writing an Argumentative Essay", "Unit 4 Checkpoint and Argument Project"]),
        ("Unit 5: Novel Study", ["Launching the Novel: Setting and Context", "Conflict and Character Change", "Symbols and Theme", "Author's Craft", "Unit 5 Checkpoint and Literary Response Project"]),
        ("Unit 6: Research and Presentation", ["Asking Research Questions", "Judging Sources and Spotting Misinformation", "Organizing and Drafting a Report", "Speaking and Presenting", "End-of-Year Review and Research Presentation"]),
    ],
    "science": [
        ("Unit 1: Thinking Like a Scientist", ["Observations, Inferences and Questions", "Designing a Fair Test: Variables", "Measuring and Recording Data", "Graphs, Models and Scientific Tools", "Unit 1 Checkpoint and Investigation Project"]),
        ("Unit 2: Cells, the Building Blocks of Life", ["Cell Theory and the Microscope", "Inside an Animal Cell", "Plant Cells and Photosynthesis", "How Things Move In and Out of Cells", "Unit 2 Checkpoint and Cell Model Project"]),
        ("Unit 3: The Diversity of Life", ["Characteristics of Living Things", "Classification and Scientific Names", "Dichotomous Keys", "Microorganisms: Helpful and Harmful", "Mid-Year Review and Field Guide Project"]),
        ("Unit 4: The Human Body", ["Levels of Organization", "Skeletal and Muscular Systems", "Circulatory and Respiratory Systems", "Digestive and Nervous Systems", "Unit 4 Checkpoint and Body Systems Project"]),
        ("Unit 5: Ecosystems", ["Living and Nonliving Parts of an Ecosystem", "Food Chains, Food Webs and Energy", "Cycles of Matter: Water and Carbon", "How Organisms Interact", "Unit 5 Checkpoint and Ecosystem Study Project"]),
        ("Unit 6: Heredity and Adaptation", ["Traits and Inheritance", "Punnett Squares", "Adaptations", "Natural Selection Over Time", "End-of-Year Review and Capstone Investigation"]),
    ],
    "socialstudies": [
        ("Unit 1: How We Know the Past", ["Historians, Sources and Evidence", "Maps, Projections and the True Size of the World", "Human Beginnings in Africa", "Farming, Villages and the First Towns", "Unit 1 Checkpoint and Museum Exhibit Project"]),
        ("Unit 2: The Nile Valley and Ancient Africa", ["The Nile: Geography and the Rise of Kemet (Egypt)", "Kemet as an African Civilization", "Nubia and the Kingdom of Kush", "The Kushite Pharaohs, Meroe and Aksum", "Unit 2 Checkpoint and Nile Valley Project"]),
        ("Unit 3: Ancient Asia", ["Mesopotamia and the First Writing", "The Indus Valley", "Ancient China: Dynasties and Ideas", "The Silk Road", "Mid-Year Review and Ancient Asia Project"]),
        ("Unit 4: The Mediterranean World", ["Persia: An Empire of Many Peoples", "Ancient Greece", "Rome: Republic to Empire", "Carthage and Roman Africa", "Unit 4 Checkpoint and Mediterranean Project"]),
        ("Unit 5: Empires and Global Trade", ["Ghana and the Trans-Saharan Trade", "Mali and Mansa Musa", "Songhai, Timbuktu and Centers of Learning", "The Swahili Coast, Great Zimbabwe and the Indian Ocean", "Unit 5 Checkpoint and Trade Route Project"]),
        ("Unit 6: The Americas and the Meeting of Worlds", ["The Olmec and the Maya", "The Mexica (Aztec), the Inca and Cahokia", "Indigenous Peoples of Florida", "1492, the Taino and the Columbian Exchange", "End-of-Year Review: The Atlantic World Begins"]),
    ],
}

SUBJECT_NAMES = {"math": "Math", "ela": "ELA", "science": "Life Science", "socialstudies": "World and American History"}


def weeks(subject):
    out, n = [], 0
    for unit, titles in UNITS[subject]:
        for t in titles:
            n += 1
            out.append((n, unit, t))
    return out
