import pandas as pd
from fetch_emails import fetch_job_emails
from filters import score_job, is_fresher_role
from bs4 import BeautifulSoup
import os
import re


# -------------------------
# helpers
# -------------------------

def clean_text(text):
    text = re.sub(r'&nbsp;|&zwnj;|&amp;', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def extract_link(text):
    urls = re.findall(r'https?://\S+', text)
    return urls[0] if urls else ""


def extract_text(msg):
    text_content = ""

    for part in msg.walk():
        content_type = part.get_content_type()

        if content_type == "text/plain":
            try:
                text_content += part.get_payload(decode=True).decode(errors="ignore")
            except:
                pass

        elif content_type == "text/html":
            try:
                soup = BeautifulSoup(
                    part.get_payload(decode=True),
                    "html.parser"
                )
                text_content += soup.get_text(" ", strip=True)
            except:
                pass

    return clean_text(text_content.lower())


# -------------------------
# main pipeline
# -------------------------

rows = []

for msg in fetch_job_emails():
    text = extract_text(msg)
    score = score_job(text)

    if score >= 2 and is_fresher_role(text):
        rows.append({
            "subject": msg.get("Subject"),
            "score": score,
            "link": extract_link(text),
            "snippet": text[:200]
        })

df = pd.DataFrame(rows)

df.to_csv(
    "jobs.csv",
    mode="a",
    header=not os.path.exists("jobs.csv"),
    index=False
)

print(f"Saved {len(df)} jobs")
