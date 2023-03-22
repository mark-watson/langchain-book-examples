"Example from documentation"

from llama_index import GPTSimpleVectorIndex, Document

doc = Document("sample.nt")
doc = RDFReader().load_data("sample.nt")
index = GPTSimpleVectorIndex(doc)

result = index.query("list all countries in a quoted Python array, then explain why")

print(result.response)