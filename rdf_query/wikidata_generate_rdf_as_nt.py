from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph
import pandas as pd

sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
sparql.setQuery("""
   SELECT ?description ?is_a_type_of WHERE {
      wd:Q80041 schema:description ?description FILTER (lang(?description) = 'en') .
      wd:Q80041 wdt:P31 ?instanceOf .  
      ?instanceOf rdfs:label ?is_a_type_of FILTER (lang(?is_a_type_of) = 'en') .
   } limit 50
""")

sparql.setReturnFormat(JSON)
results = sparql.query().convert()

print("results:", results)

results_df = pd.json_normalize(results['results']['bindings'])
print("\results_df:\n", results_df)
r = results_df[['description.value', 'is_a_type_of.value']].head()

print("\nresults:\n", r)
# results = g.serialize(format="nt").encode("utf-8").decode('utf-8')
#print(results)

text_file = open("sample.nt", "w")
text_file.write(r.to_string())
text_file.close()

