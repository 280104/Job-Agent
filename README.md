# Job Search Automation (Safe Mode)

A **free, no-risk job search automation** that collects job alerts from email, filters them for **fresher / entry-level relevance**, and exports clean, clickable job listings for **manual application**.

Built to save time without violating job platform rules.

---

## What it does
- Fetches job alert emails via IMAP (Gmail)
- Filters roles using resume-aligned keywords
- Rejects senior-only positions automatically
- Extracts job title, relevance score, apply link, and snippet
- Exports to CSV (Google Sheets / Notion ready)

No scraping. No auto-apply. No paid APIs.

---

## Tech
- Python
- IMAP (email parsing)
- BeautifulSoup
- Pandas

---

## Project Structure
job_agent/
├── fetch_emails.py
├── parse_jobs.py
├── filters.py
├── config.py # ignored (secrets)
├── config.example.py
├── jobs.csv # ignored
└── README.md

---

## Setup
```bash
pip install pandas beautifulsoup4
python parse_jobs.py
Configure email credentials in config.py (see config.example.py).

Usage
Enable job alerts on platforms (Indeed, Naukri, Internshala, LinkedIn)

Run the script daily

Import jobs.csv into Google Sheets

Apply manually

Why manual apply?
Auto-apply bots get accounts banned and lower interview quality.
This tool filters and organizes — you decide and apply.

Disclaimer
This project does not scrape websites or auto-apply to jobs.
Use responsibly.
