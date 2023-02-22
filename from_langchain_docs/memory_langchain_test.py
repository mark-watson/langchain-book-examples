# Derived from:
#   https://langchain.readthedocs.io/en/latest/modules/memory/examples/adding_memory.html
# with slight modifications.

from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain import OpenAI, LLMChain, PromptTemplate

template = """You are a chatbot having a conversation with a human.

{chat_history}
Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], 
    template=template
)
memory = ConversationBufferMemory(memory_key="chat_history")

llm_chain = LLMChain(
    llm=OpenAI(), 
    prompt=prompt, 
    verbose=True, 
    memory=memory,
)

print(llm_chain.predict(human_input="Hi there my friend. What is your name?"))

print(llm_chain.predict(human_input="My name is Mark. How are you?"))

print(llm_chain.predict(human_input="What do you have planned for today?"))
