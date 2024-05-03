from llama_index.core import VectorStoreIndex
from llama_index.core import Document

text_list = ["LlamaIndex is a powerful tool for LLM applications.",
             "It helps in structuring and retrieving data efficiently."]
documents = [Document(text=t) for t in text_list]

index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

retrieved_docs = query_engine.retrieve("What is LlamaIndex?")
print(retrieved_docs)
