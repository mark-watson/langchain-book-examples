# Kor Library: a Useful Library that I did not include in my book

Note to reader: I was origianlly going to have a book chapter on other (besides LangChain and LlamaIndex) libraries but then decided keep the book more focussed. The material here was originally intended for that chapter, and I include it in case you might find it useful.

The Kor library was written by Eugene Yurtsev. Kor is useful for using LLMs to extract structured data from unstructured text. Kor works by generating appropriate prompt text to explain to GPT-3.5 what information to extract and adding in the text to be processed.

The [GitHub repository for Kor](https://github.com/eyurtsev/kor) is under active development so please check the project for updates. Here is the [documentation](https://eyurtsev.github.io/kor/tutorial.html).

For the following example I modified the example in the documentation for extracting phone numbers to instead find dates in text.


```python
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

openai.api_key = os.environ.get('OPENAI_API_KEY')

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
```

Sample output:

```console
$ python dates.py 
<kor.extraction.Extractor object at 0x102f93460>
prompt: Your goal is to extract structured information from the user's input that matches the form described below. When extracting information please make sure it matches the type information exactly. Do not add any attributes that do not appear in the schema shown below.

TypeScript:

{
 date: string[] // Any dates found in the text. Should be output in the format: January 12, 2023
}

For Union types the output must EXACTLY match one of the members of the Union type.

Please enclose the extracted information in HTML style tags with the tag name corresponding to the corresponding component ID. Use angle style brackets for the tags ('>' and '<'). Only output tags when you're confident about the information that was extracted from the user's query. If you can extract several pieces of relevant information from the query, then include all of them. If the type is an array, please repeat the corresponding tag name multiple times once for each relevant extraction. Do NOT output anything except for the extracted information. Only output information inside the HTML style tags. Do not include any notes or any clarifications. 

Input: Someone met me on December 21, 1995
Output: <date>Let's meet up on January 12, 2023 and discuss our yearly budget</date>
Input: Does September 12, 2023 work for you?
Output:
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "<date>September 12, 2023</date>",
        "role": "assistant"
      }
    }
  ],
  "created": 1679338972,
  "id": "chatcmpl-6wF4ObcixCYOFm59zi6RHmltC877Y",
  "model": "gpt-3.5-turbo-0301",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 14,
    "prompt_tokens": 285,
    "total_tokens": 299
  }
}
prompt: Your goal is to extract structured information from the user's input that matches the form described below. When extracting information please make sure it matches the type information exactly. Do not add any attributes that do not appear in the schema shown below.

TypeScript:

{
 date: string[] // Any dates found in the text. Should be output in the format: January 12, 2023
}

For Union types the output must EXACTLY match one of the members of the Union type.

Please enclose the extracted information in HTML style tags with the tag name corresponding to the component ID. Use angle style brackets for the tags ('>' and '<'). Only output tags when you're confident about the information that was extracted from the user's query. If you can extract several pieces of relevant information from the query, then include all of them. If the type is an array, please repeat the corresponding tag name multiple times once for each relevant extraction. Do NOT output anything except for the extracted information. Only output information inside the HTML style tags. Do not include any notes or any clarifications. 

Input: Someone met me on December 21, 1995
Output: <date>Let's meet up on January 12, 2023 and discuss our yearly budget</date>
Input: Does May 1 work for you?
Output:
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "<date>May 1, 2021</date>",
        "role": "assistant"
      }
    }
  ],
  "created": 1679338980,
  "id": "chatcmpl-6wF4WRuV1ABkZBDPQXOtFsqcaw1TZ",
  "model": "gpt-3.5-turbo-0301",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 14,
    "prompt_tokens": 281,
    "total_tokens": 295
  }
}
```
