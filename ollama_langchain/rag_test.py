# requires "ollama serve" to be running in another terminal

from langchain.llms import Ollama
from langchain.embeddings.ollama import OllamaEmbeddings
from langchain.chains import RetrievalQA

from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders.directory import DirectoryLoader

# Create index (can be reused):

loader = DirectoryLoader('../data', glob='**/*.txt')
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100, chunk_overlap=100)
all_splits = text_splitter.split_documents(data)

persist_directory = 'cache'

vectorstore = Chroma.from_documents(
    documents = all_splits,
    embedding = OllamaEmbeddings(model="mistral:instruct"),
    persist_directory=persist_directory)

vectorstore.persist()

# Try reloading index from disk and using for search:

persist_directory = 'cache'

vectorstore = Chroma(persist_directory=persist_directory,
                     embedding_function=OllamaEmbeddings(model="mistral:instruct")
                    )

llm = Ollama(base_url = "http://localhost:11434",
             model = "mistral:instruct",
             verbose = False,
            )

retriever = vectorstore.as_retriever()

qa_chain = RetrievalQA.from_chain_type(
            llm = llm,
            chain_type = 'stuff',
            retriever = retriever,
            verbose = True,)

while True:
    query = input("Ask a question: ")
    response = qa_chain(query)
    print(response['result'])
