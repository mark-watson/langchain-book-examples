import openai
from openai import OpenAI
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

# Read the prompt from a text file
with open('prompt.txt', 'r') as file:
    prompt_template = file.read()

# Substitute a string variable into the prompt
input_text = "Mark Johnson enjoys living in Berkeley California at 102 Dunston Street and use mjess@foobar.com for contacting him."
prompt = prompt_template.replace("input_text", input_text)

# Use the OpenAI completion API to generate a response with GPT-4
completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": prompt,
        },
    ],
)

print(completion.choices[0].message.content)
