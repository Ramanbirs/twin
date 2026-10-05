from pypdf import PdfReader
import json

# Read LinkedIn PDF
try:
    reader = PdfReader("./data/linkedin.pdf")
    linkedin = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            linkedin += text
except FileNotFoundError:
    linkedin = "LinkedIn profile not available"

# Read other data files
with open("./data/summary.txt", "r", encoding="utf-8") as f:
    summary = f.read()

with open("./data/style.txt", "r", encoding="utf-8") as f:
    style = f.read()

with open("./data/facts.json", "r", encoding="utf-8") as f:
    facts = json.load(f)

try:
    reader = PdfReader("./data/supporting_projects.pdf")
    supporting_projects = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            supporting_projects += text
except FileNotFoundError:
    supporting_projects = "Supporting projects not available"

try:
    reader = PdfReader("./data/questions_and_answers.pdf")
    questions_and_answers = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            questions_and_answers += text
except FileNotFoundError:
    questions_and_answers = "Questions and answers not available"