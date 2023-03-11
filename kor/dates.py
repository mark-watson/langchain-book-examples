" From documentation: https://eyurtsev.github.io/kor/prompt_examples.html"

from kor.extraction import Extractor
from kor.nodes import Object, Text, Number
from kor.llms import OpenAIChatCompletion, OpenAICompletion

llm = OpenAIChatCompletion(model="gpt-3.5-turbo")
model = Extractor(llm)

schema = Text(
    id="date",
    description=(
        "Any dates found in the text. Should be output in the format:"
        " January 12, 2023"
    ),
    examples=[("Someone met me on December 21, 1995",
               "Let's meet up on January 12, 2023 and discuss our yearly budget")],
)

model(
    (
        "We agreed to meet on January 12, 2023. I was born on January 12, 1999. We will have coffee on January 12, 2023. "
        " Sally's hire date is May 21, 2022. Here job performance has been good. "
        " I will start my vacation on June 1, 2022. "
    ),
    schema,
)

print(model)

prompt = model.prompt_generator.format_as_string("Does September 12, 2023 work for you?", schema)

print("prompt:", prompt)

import os

import openai

openai.api_key = os.environ.get('OPENAI_KEY')

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": prompt}]
)

print(completion)

prompt = model.prompt_generator.format_as_string("Does May 1 work for you?", schema)

print("prompt:", prompt)

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": prompt}]
)

print(completion)
