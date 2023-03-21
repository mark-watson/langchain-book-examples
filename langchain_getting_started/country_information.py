from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
llm = OpenAI(temperature=0.9)

def get_country_information(country_name):
    print(f"\nProcessing {country_name}:")
    global prompt
    if "prompt" not in globals():
        print("Creating prompt...")
        prompt = PromptTemplate(
            input_variables=["country_name"],
            template = """
Predict the capital and population of a country.

Country: {country_name}
Capital:
Population:""",
        )
    prompt_text = prompt.format(country_name=country_name)
    print(prompt_text)
    return llm(prompt_text)

print(get_country_information("Canada"))
print(get_country_information("Germany"))