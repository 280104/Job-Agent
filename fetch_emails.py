import imaplib
import email
from email.header import decode_header
from config import EMAIL, APP_PASSWORD, IMAP_SERVER, JOB_SENDERS

def fetch_job_emails():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, APP_PASSWORD)

    mail.select("inbox")

    # Fetch BOTH unread and recent emails (important)
    status, data = mail.search(None, "ALL")

    emails = []

    if status != "OK":
        print("IMAP search failed")
        return emails

    for num in data[0].split()[-50:]:  # limit to last 50 emails
        _, msg_data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        sender = msg.get("From", "").lower()

        if any(domain in sender for domain in JOB_SENDERS):
            emails.append(msg)

    mail.logout()
    print(f"Fetched {len(emails)} job-related emails")
    return emails
