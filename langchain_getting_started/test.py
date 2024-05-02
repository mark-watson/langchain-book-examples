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




exit(0)

from langchain_community.document_loaders import TextLoader, DirectoryLoader
#from langchain_community.embeddings.sentence_transformer import (
#    SentenceTransformerEmbeddings,
#)
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import VectorDBQA
from langchain_community.llms import OpenAI
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

#loader = TextLoader("../data/chemistry.txt", "../data/health.txt", show_progress=True)
loader = DirectoryLoader('../data', glob="**/*.txt", show_progress=False)
documents = loader.load()
print("documents:", documents)

text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(documents)
print("documents:", documents)
vector = FAISS.from_documents(documents, embeddings)
print(dir(vector))
exit(0)

# split it into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

texts = text_splitter.split_documents(documents)

docsearch = Chroma.from_documents(texts, OpenAIEmbeddings())

qa = VectorDBQA.from_chain_type(llm=OpenAI(),
                                chain_type="stuff",
                                vectorstore=docsearch)

def query(q):
    print(f"Query: {q}")
    print(f"Answer: {qa.run(q)}")

query("What kinds of equipment are in a chemistry laboratory?")
query("What is Austrian School of Economics?")
query("Why do people engage in sports?")
query("What is the effect of body chemistry on exercise?")

exit(0)
db = Chroma.from_documents(docs, SentenceTransformerEmbeddings())

# query it
query = "What is the definition of chemistry?"
docs = db.similarity_search(query)

# print results
print(docs[0].page_content)





exit(0)
from langchain.llms import OpenAI
#from langchain.document_stores import InMemoryDocumentStore
from langchain_community.vectorstores import Chroma

import os

# Initialize LangChain components
llm = OpenAI()
#document_store = InMemoryDocumentStore()
document_store = Chroma()

# Directory containing text files
text_files_directory = "../data/"

# Read text files and add them to the document store
for filename in os.listdir(text_files_directory):
    if filename.endswith(".txt"):
        with open(os.path.join(text_files_directory, filename), 'r', encoding='utf-8') as file:
            text_content = file.read()
            document_store.add_documents([{"text": text_content, "metadata": {"filename": filename}}])

# Example query
query = "What is the main topic discussed in the documents?"
response = llm.query_document_store(query, document_store=document_store)

print("Query Result:", response)
