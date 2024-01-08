# This example uses code from https://python.langchain.com/docs/get_started

# on macOS: pip install faiss-cpu

from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

embeddings = OpenAIEmbeddings()

text_splitter = RecursiveCharacterTextSplitter()
#documents = text_splitter.split_documents(docs)


embeddings = OpenAIEmbeddings()

loader = DirectoryLoader('./text_data/', glob="**/*.txt")
documents = loader.load()

vector = FAISS.from_documents(documents, embeddings)

from langchain.chains import create_retrieval_chain

from langchain.chains.combine_documents import create_stuff_documents_chain

prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}""")

document_chain = create_stuff_documents_chain(llm, prompt)


retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

response = retrieval_chain.invoke({"input": "Create a new recipe using both Broccoli"})
print(response["answer"])

response = retrieval_chain.invoke({"input": "Create a recipe using Beans, Rice, and Chicken"})
print(response["answer"])

