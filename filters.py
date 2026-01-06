# ===============================
# ROLE & SKILL SIGNALS (FROM YOUR RESUME)
# ===============================

CORE_SKILLS = [
    # Programming
    "python",
    "java",

    # AI / ML
    "machine learning",
    "ml",
    "ai",
    "artificial intelligence",
    "deep learning",

    # GenAI / modern signals
    "generative ai",
    "llm",
    "rag",
    "langchain",

    # Software / backend
    "software engineer",
    "software developer",
    "backend",
    "backend developer",
    "api",
    "rest",

    # Web / full stack (basic)
    "javascript",
    "html",
    "css",
    "react",
    "next.js",
    "node",

    # Data / DB
    "sql",
    "database",
    "mongodb",
    "postgres"
]

# ===============================
# ENTRY-LEVEL / FRESHER SIGNALS
# ===============================

FRESHER_SIGNALS = [
    "fresher",
    "entry level",
    "junior",
    "associate",
    "graduate",
    "new grad",
    "0-1",
    "0–1",
    "trainee",
    "intern",
    "early career"
]

# ===============================
# STRONG REJECTION SIGNALS
# (AUTO-DROP THESE)
# ===============================

STRONG_REJECT = [
    "3+ years",
    "4+ years",
    "5+ years",
    "6+ years",
    "senior",
    "lead",
    "staff",
    "principal",
    "manager",
    "architect"
]

# ===============================
# FUNCTIONS
# ===============================

def is_fresher_role(text: str) -> bool:
    """
    Reject only when there is a STRONG senior signal.
    Otherwise allow — alerts often don't mention experience clearly.
    """
    for term in STRONG_REJECT:
        if term in text:
            return False
    return True


def score_job(text: str) -> int:
    """
    Count how many resume-relevant skills appear.
    """
    score = 0
    for skill in CORE_SKILLS:
        if skill in text:
            score += 1
    return score
