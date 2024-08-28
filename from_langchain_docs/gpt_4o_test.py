from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o") # gpt-4o-mini is less expensive and almost as good

messages = [
    SystemMessage(content="You're a helpful assistant"),
    HumanMessage(content="What is the purpose of model regularization? Be concise."),
]

results = llm.invoke(messages)
print(results.content)
print("\n\n\n")
print(results)