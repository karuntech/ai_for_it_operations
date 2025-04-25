# Call openai api to ask a general question for demonstrating gpt capabilities

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input="Write a one sentence poem about the awesomeness of the python programming language"
)

print(response.output_text)