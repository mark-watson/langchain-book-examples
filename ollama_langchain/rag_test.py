# requires "ollama serve" to be running in another terminal

# pip install python-docx


from langchain_community.llms.ollama import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains import RetrievalQA

from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader

model = "mistral:v0.3"

# Create index (can be reused):

loader = DirectoryLoader('../data/', glob="**/*.txt", show_progress=True)
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100, chunk_overlap=100)
all_splits = text_splitter.split_documents(data)

persist_directory = 'cache'

vectorstore = Chroma.from_documents(
    documents = all_splits,
    embedding = OllamaEmbeddings(model=model),
    persist_directory=persist_directory)

vectorstore.persist()

# Try reloading index from disk and using for search:

persist_directory = 'cache'

vectorstore = Chroma(persist_directory=persist_directory,
                     embedding_function=OllamaEmbeddings(model=model)
                    )

llm = Ollama(base_url = "http://localhost:11434",
             model = model,
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
