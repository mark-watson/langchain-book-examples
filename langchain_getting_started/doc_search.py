from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader

model = ChatOpenAI()

from read_text_files import read_text_files

vectorstore = FAISS.from_texts(read_text_files("../data/"), embedding=OpenAIEmbeddings())

retriever = vectorstore.as_retriever()

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

print(chain.invoke("who tried to define what Chemistry is?"))

print(chain.invoke("What kinds of equipment are in a chemistry laboratory?"))
print(chain.invoke("What is Austrian School of Economics?"))
print(chain.invoke("Why do people engage in sports?"))
print(chain.invoke("What is the effect of body chemistry on exercise?"))