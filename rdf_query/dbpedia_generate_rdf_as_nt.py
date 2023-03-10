from SPARQLWrapper import SPARQLWrapper
from rdflib import Graph

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
    PREFIX dbpedia: <http://dbpedia.org/resource>
    PREFIX dbpprop: <http://dbpedia.org/property>

    CONSTRUCT {
        ?city dbpedia-owl:country ?country .
        ?city rdfs:label ?citylabel .
        ?country rdfs:label ?countrylabel .
        <http://dbpedia.org/ontology/country> rdfs:label "country"@en .
    }
    WHERE {
        ?city rdf:type dbpedia-owl:City .
        ?city rdfs:label ?citylabel .
        ?city dbpedia-owl:country ?country .
        ?country rdfs:label ?countrylabel .
        FILTER (lang(?citylabel) = 'en')
        FILTER (lang(?countrylabel) = 'en')
    }
    LIMIT 50
""")
sparql.setReturnFormat("rdf")
results = sparql.query().convert()

g = Graph()
g.parse(data=results.serialize(format="xml"), format="xml")

print("\nresults:\n")
results = g.serialize(format="nt").encode("utf-8").decode('utf-8')
print(results)

text_file = open("sample.nt", "w")
text_file.write(results)
text_file.close()

