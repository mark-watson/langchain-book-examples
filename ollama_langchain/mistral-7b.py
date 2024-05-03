# requires "ollama serve" to be running in another terminal

from langchain_community.llms import Ollama

llm = Ollama(
    model="mistral:v0.2",
    verbose=False,
)

s = llm("how much is 1 + 2?")
print(s)

s = llm("If Sam is 27, Mary is 42, and Jerry is 33, what are their age differences?")
print(s)