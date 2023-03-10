from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph

sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
sparql.setQuery("""
    SELECT * WHERE { wd:Q80041 ?p ?o } limit 5
""")

sparql.setReturnFormat(JSON)
results = sparql.queryAndConvert()

print("results:", results)

g = Graph()
g.parse(data=results, format="JSON")

print("\nresults:\n")
# results = g.serialize(format="nt").encode("utf-8").decode('utf-8')
print(results)

text_file = open("sample.nt", "w")
text_file.write(results)
text_file.close()

