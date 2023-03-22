from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import DirectoryLoader
from langchain import OpenAI, VectorDBQA

embeddings = OpenAIEmbeddings()

loader = DirectoryLoader('../data/', glob="**/*.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=2500, chunk_overlap=0)

texts = text_splitter.split_documents(documents)

docsearch = Chroma.from_documents(texts, embeddings)

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