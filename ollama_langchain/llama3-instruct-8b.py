# requires "ollama serve" to be running in another terminal

from langchain_community.llms import Ollama

llm = Ollama(
    model="llama3:instruct",
    verbose=True,
)

#s = llm("how much is 1 + 2?")
#print(s)

s = llm("If Sam is 27, Mary is 42, and Jerry is 33, what are their age differences? Be concise")
print(s)