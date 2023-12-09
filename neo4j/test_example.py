import json

from llama_index.llama_pack import download_llama_pack

# download and install dependencies
Neo4jQueryEnginePack = download_llama_pack(
  "Neo4jQueryEnginePack", "./neo4j_pack"
)

# Load the docs (example of Paleo diet from Wikipedia)
from llama_index import download_loader

WikipediaReader = download_loader("WikipediaReader")
loader = WikipediaReader()
docs = loader.load_data(pages=['Paleolithic diet'], auto_suggest=False)
print(f'Loaded {len(docs)} documents')

# get Neo4j credentials (assume it's stored in credentials.json)
with open('credentials.json') as f:
  neo4j_connection_params = json.load(f)
  username = neo4j_connection_params['username']
  password = neo4j_connection_params['password']
  url = neo4j_connection_params['url']
  database = neo4j_connection_params['database']

print(f'username: {username}', f'password: {password}', f'url: {url}', f'database: {database}')
# create the pack
neo4j_pack = Neo4jQueryEnginePack(
  username = username,
  password = password,
  url = url,
  database = database,
  docs = docs
)

response = neo4j_pack.run("Tell me about the benefits of paleo diet.")
print(f"{response}\n\n")


response = neo4j_pack.run("What kinds of food should I buy for a paleo diet.")
print(f"{response}")
