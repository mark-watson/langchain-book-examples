from langchain import HuggingFaceHub, LLMChain
from langchain.prompts import PromptTemplate

hub_llm = HuggingFaceHub(
    repo_id='google/flan-t5-xl',
    model_kwargs={'temperature':1e-6}
)

prompt = PromptTemplate(
    input_variables=["name"],
    template="What year did {name} get elected as president?",
)

llm_chain = LLMChain(prompt=prompt, llm=hub_llm)

print(llm_chain.run("George Bush"))

