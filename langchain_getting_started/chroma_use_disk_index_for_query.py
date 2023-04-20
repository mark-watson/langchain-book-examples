from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
vectorstore = Chroma(collection_name="langchain_store",
                     embedding_function=embeddings,
                     persist_directory="./tmp")

# Query the vector store
results = vectorstore.similarity_search("the red chemical", k=1)
print(results)
