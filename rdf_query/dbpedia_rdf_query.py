"Example from documentation"

from llama_index import GPTSimpleVectorIndex, Document, download_loader

RDFReader = download_loader("RDFReader")
doc = RDFReader().load_data("sample.nt")
index = GPTSimpleVectorIndex(doc)

result = index.query("list all countries in a quoted Python array, then explain why")

print(result.response)
