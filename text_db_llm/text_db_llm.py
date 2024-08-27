# Text Database Supporting Search and Chat-based Exploration

# make sure you set the following environment variable:
#   OPENAI_API_KEY

import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

chroma_client = chromadb.EphemeralClient()
chroma_collection = chroma_client.create_collection("temp")

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, embed_model=embed_model
)
query_engine = index.as_query_engine()
print(query_engine.query("effect of body chemistry on exercise?"))

exit(0)

if os.path.exists("index.json") and os.path.getsize("index.json") > 0:
  print("Loading index from disk...")
  index = VectorStoreIndex.load_from_disk('index.json')
else:
  print("Index file odes not exist, so create it...")
  documents = SimpleDirectoryReader('data').load_data()
  index = VectorStoreIndex(documents)
  print(dir(index))
  index.save_to_disk('index.json')

# search for a document


print(index.query("effect of body chemistry on exercise?"))
