import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from collections import Counter

URL = "https://sih.gov.in/sih2026PS"

# ============================================================
# YOUR SKILLS
# ============================================================

MY_SKILLS = [
    "Python",
    "Django",
    "Flask",
    "FastAPI",
    "React",
    "JavaScript",
    "TypeScript",
    "PostgreSQL",
    "MySQL",
    "REST API",
    "Full Stack",
    "AI",
    "Artificial Intelligence",
    "Machine Learning",
    "Deep Learning",
    "Generative AI",
    "LLM",
    "RAG",
    "LangChain",
    "Computer Vision",
    "NLP",
    "Data Science",
    "GIS",
    "Cloud",
    "Docker",
    "Git",
    "Flutter",
    "Mobile App",
    "godot"
]

# ============================================================
# OPTIONAL FILTERS
# ============================================================

ONLY_SOFTWARE = True

# Put themes you DON'T want here if required
EXCLUDED_THEMES = [
    "MedTech / BioTech / HealthTech",
    "Disaster Management",
    "Transportation & Logistics",
    "Smart Automation",
    "Smart Education",
    "Clean & Green Technology"
    # "Hardware",
]

# Minimum score to shortlist
MIN_SCORE = 15

# ============================================================
# DOWNLOAD PAGE
# ============================================================

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 Chrome/151.0 Safari/537.36"
    )
}

print("Downloading SIH 2026 problem statements...")

response = requests.get(
    URL,
    headers=headers,
    timeout=(15, 120)
)

response.raise_for_status()

print("Page downloaded successfully.")

# ============================================================
# PARSE HTML
# ============================================================

soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text("\n", strip=True)

# ============================================================
# EXTRACT PROBLEM STATEMENTS
# ============================================================

pattern = re.compile(
    r"""
    Problem\ Statement\ ID\s+(?P<id>\d+)
    .*?
    Problem\ Statement\ Title\s+(?P<title>.*?)
    \s+
    Description\s+(?P<description>.*?)
    \s+
    Organization\s+(?P<organization>.*?)
    \s+
    Department\s+(?P<department>.*?)
    \s+
    Category\s+(?P<category>Software|Hardware)
    \s+
    Theme\s+(?P<theme>.*?)
    \s+
    Youtube\ Link
    """,
    re.IGNORECASE | re.DOTALL | re.VERBOSE
)

matches = pattern.finditer(text)

problems = []

for match in matches:

    data = match.groupdict()

    problem = {
        "id": data["id"].strip(),
        "title": data["title"].strip(),
        "description": data["description"].strip(),
        "organization": data["organization"].strip(),
        "department": data["department"].strip(),
        "category": data["category"].strip(),
        "theme": data["theme"].strip(),
    }

    problems.append(problem)


print(f"Extracted {len(problems)} problem statements.")

# ============================================================
# REMOVE DUPLICATES
# ============================================================

unique = {}

for problem in problems:
    unique[problem["id"]] = problem

problems = list(unique.values())

print(f"After duplicate removal: {len(problems)}")

# ============================================================
# SOFTWARE ONLY
# ============================================================

if ONLY_SOFTWARE:

    problems = [
        p for p in problems
        if p["category"].lower() == "software"
    ]

print(f"Software problem statements: {len(problems)}")

# ============================================================
# NORMALIZE TEXT
# ============================================================

def normalize(text):

    text = text.lower()

    text = re.sub(
        r"[^a-z0-9+#.\-/ ]",
        " ",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text


# ============================================================
# SKILL MATCHING
# ============================================================

def calculate_score(problem):

    searchable_text = normalize(
        problem["title"]
        + " "
        + problem["description"]
        + " "
        + problem["theme"]
    )

    matched_skills = []

    for skill in MY_SKILLS:

        skill_normalized = normalize(skill)

        if skill_normalized in searchable_text:
            matched_skills.append(skill)

    # --------------------------------------------------------
    # Weighting
    # --------------------------------------------------------

    title_text = normalize(problem["title"])
    theme_text = normalize(problem["theme"])
    description_text = normalize(problem["description"])

    score = 0

    for skill in matched_skills:

        skill_normalized = normalize(skill)

        # Title match = very strong
        if skill_normalized in title_text:
            score += 10

        # Theme match = strong
        elif skill_normalized in theme_text:
            score += 7

        # Description match
        elif skill_normalized in description_text:
            score += 4

    return score, matched_skills


# ============================================================
# SCORE ALL PROBLEMS
# ============================================================

for problem in problems:

    score, matched = calculate_score(problem)

    problem["score"] = score
    problem["matched_skills"] = ", ".join(matched)

# ============================================================
# FILTER EXCLUDED THEMES
# ============================================================

if EXCLUDED_THEMES:

    problems = [
        p for p in problems
        if p["theme"] not in EXCLUDED_THEMES
    ]

# ============================================================
# SORT
# ============================================================

problems.sort(
    key=lambda x: x["score"],
    reverse=True
)

# ============================================================
# SHORTLIST
# ============================================================

shortlisted = [
    p for p in problems
    if p["score"] >= MIN_SCORE
]

print()
print("=" * 80)
print("TOP SIH 2026 SOFTWARE PROBLEM STATEMENTS FOR YOUR SKILLS")
print("=" * 80)

for index, problem in enumerate(shortlisted[:20], 1):

    print()
    print(f"#{index}")
    print(f"ID       : SIH{problem['id']}")
    print(f"Title    : {problem['title']}")
    print(f"Theme    : {problem['theme']}")
    print(f"Score    : {problem['score']}")
    print(f"Matched  : {problem['matched_skills']}")

    print(
        f"Description:\n"
        f"{problem['description'][:500]}..."
    )

# ============================================================
# SAVE EVERYTHING
# ============================================================

df = pd.DataFrame(problems)

df.to_csv(
    "sih_2026_software.csv",
    index=False,
    encoding="utf-8-sig"
)

df.to_json(
    "sih_2026_software.json",
    orient="records",
    indent=4,
    force_ascii=False
)

# ============================================================
# SAVE SHORTLIST
# ============================================================

shortlist_df = pd.DataFrame(shortlisted)

shortlist_df.to_csv(
    "sih_2026_shortlisted.csv",
    index=False,
    encoding="utf-8-sig"
)

print()
print("=" * 80)
print("FILES CREATED")
print("=" * 80)

print("sih_2026_software.csv")
print("sih_2026_software.json")
print("sih_2026_shortlisted.csv")

print()
print(f"Total software PS : {len(problems)}")
print(f"Shortlisted       : {len(shortlisted)}")