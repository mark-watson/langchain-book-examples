from llama_index import ListIndex, SimpleDirectoryReader
#from llama_index import QueryEngine

# Load documents from a directory
documents = SimpleDirectoryReader('../data').load_data()

# Create a new index from the documents
new_index = ListIndex.from_documents(documents)

# Create a query engine from the new index
query_engine = new_index.as_query_engine()

# Query the index
results = query_engine.query('what is the histry of economics?')
print(f"results: {results}")
