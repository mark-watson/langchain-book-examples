# make sure you set the following environment variable is set:
#   OPENAI_API_KEY

from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader('data').load_data()
index = GPTSimpleVectorIndex(documents)

# save to disk
index.save_to_disk('index.json')
# load from disk
index = GPTSimpleVectorIndex.load_from_disk('index.json')

# search for a document
print(index.query("What is the definition of sport?"))
