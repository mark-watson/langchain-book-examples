from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vectorstore = Chroma(collection_name="langchain_store",
                     embedding_function=embeddings,
                     persist_directory="./tmp")

# Add data to the vector store
vectorstore.add_texts(
    ["Chemicals are used in the production of many products. ",
     "The study of Physics is important for understanding the world around us.",
     "Applications of Biology include the study of plants and animals."],
     metadatas=[{"source": "Mark"}, {"source": "Mark"}, {"source": "Mark"}],
     ids=["docC", "docP", "docB"])

# Persist the data to disk
vectorstore.persist()

