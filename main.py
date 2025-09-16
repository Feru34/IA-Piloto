import os
import PyPDF2
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from prompts import generate_prompt

load_dotenv(find_dotenv())

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)

question = "Según la política ¿Qué se considera como efectivo y equivalentes de efectivo?"
# question = "Según la política ¿Qué incluyen los pasivos financieros medidos a costo amortizado?"

# Read PDF
pdf =""
file_path = "sura-EEFF-2024-4t-Mini.pdf"
with open(file_path, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        pdf += page.extract_text() + "\n"

response = client.responses.create(
    model="gpt-5",
    input=generate_prompt(pdf, question)
)

print(response.output_text)