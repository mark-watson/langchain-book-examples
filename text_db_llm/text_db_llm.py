# Text Database Supporting Search and Chat-based Exploration

# make sure you set the following environment variable:
#   OPENAI_API_KEY

import os
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

if os.path.exists("index.json") and os.path.getsize("index.json") > 0:
  print("Loading index from disk...")
  index = GPTSimpleVectorIndex.load_from_disk('index.json')
else:
  print("Index file odes not exist, so create it...")
  documents = SimpleDirectoryReader('data').load_data()
  index = GPTSimpleVectorIndex(documents)
  index.save_to_disk('index.json')

# search for a document


print(index.query("effect of body chemistry on exercise?"))
