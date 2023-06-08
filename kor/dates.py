" From documentation: https://eyurtsev.github.io/kor/prompt_examples.html"

from kor.extraction import create_extraction_chain
from kor.nodes import Object, Text, Number
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0,
    max_tokens=2000,
    frequency_penalty=0,
    presence_penalty=0,
    top_p=1.0,
)

schema = Text(
    id="date",
    description=(
        "Any dates found in the text. Should be output in the format:"
        " January 12, 2023"
    ),
    examples=[("Someone met me on December 21, 1995",
               "Let's meet up on January 12, 2023 and discuss our yearly budget")],
)

chain = create_extraction_chain(llm, schema)


chain(
    (
        "We agreed to meet on January 12, 2023. I was born on January 12, 1999. We will have coffee on January 12, 2023. "
        " Sally's hire date is May 21, 2022. Here job performance has been good. "
        " I will start my vacation on June 1, 2022. "
    ),
    schema,
)

print(chain)

prompt = chain.prompt_generator.format_as_string("Does September 12, 2023 work for you?", schema)

print("prompt:", prompt)

import os

import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": prompt}]
)

print(completion)

prompt = chain.prompt_generator.format_as_string("Does May 1 work for you?", schema)

print("prompt:", prompt)

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": prompt}]
)

print(completion)
