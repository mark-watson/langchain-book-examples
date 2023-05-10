# make sure you set the following environment variable is set:
#   OPENAI_API_KEY

from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from llama_index import StorageContext, load_index_from_storage

documents = SimpleDirectoryReader('../data').load_data()
# index = GPTListIndex(documents) # llama_index < 0.5
index = GPTVectorStoreIndex.from_documents(documents)
engine = index.as_query_engine()
print(engine.query("what are key economic indicators?"))

# save to disk
index.storage_context.persist(persist_dir='./cache')

# load from disk
storage_context = StorageContext.from_defaults(persist_dir='./cache')
index = load_index_from_storage(storage_context)
engine = index.as_query_engine()

# search for a document
print(engine.query("effect of body chemistry on exercise?"))
