import os
from dotenv import load_dotenv

load_dotenv()

print("OPENAI_API_KEY: ", os.environ["OPENAI_API_KEY"])
print("ANTHROPIC_API_KEY: ", os.environ["ANTHROPIC_API_KEY"])
print("LANGSMITH_API_KEY: ", os.environ["LANGSMITH_API_KEY"])
