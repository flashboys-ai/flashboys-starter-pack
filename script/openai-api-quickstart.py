from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

prompt_example = (
  "You are my new prompting expert"
  "Give me 3 of your best prompting tips"
  "Use your tips and give me 1 example"
  "Write it out in the style of a humanoid"
)

response = client.responses.create(
  model="gpt-5-nano",
  input=prompt_example
)

print(response.output_text)

response_output = response.output_text

with open("../prompt-collection/prompt1.txt", "w") as file:
  file.writelines(response_output)
