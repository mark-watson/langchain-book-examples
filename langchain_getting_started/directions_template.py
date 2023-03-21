from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
llm = OpenAI(temperature=0.9)

def get_directions(thing_to_do):
    prompt = PromptTemplate(
        input_variables=["thing_to_do"],
        template="How do I {thing_to_do}?",
    )
    prompt_text = prompt.format(thing_to_do=thing_to_do)
    print(f"\n{prompt_text}:")
    return llm(prompt_text)

print(get_directions("get to the store"))
print(get_directions("hang a picture on the wall"))
