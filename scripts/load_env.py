import os
from dotenv import load_dotenv

load_dotenv()

print("OPENAI_API_KEY: ", os.environ["OPENAI_API_KEY"])
print("ANTHROPIC_API_KEY: ", os.environ["ANTHROPIC_API_KEY"])
print("LANGSMITH_API_KEY: ", os.environ["LANGSMITH_API_KEY"])
print("GMAIL_EMAIL: ", os.environ["GMAIL_EMAIL"])
print("GMAIL_TOKEN: ", os.environ["GMAIL_TOKEN"])
print("GMAIL_CLIENT_SECRET: ", os.environ["GMAIL_CLIENT_SECRET"])
print("GMAIL_CLIENT_ID: ", os.environ["GMAIL_CLIENT_ID"])
