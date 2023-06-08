from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph
import pandas as pd

def get_possible_entity_uris_from_wikidata(entity_name):
   sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
   sparql.setQuery("""
      SELECT ?entity ?entityLabel WHERE {
         ?entity rdfs:label "%s"@en .
      } limit 5
   """ % entity_name)

   sparql.setReturnFormat(JSON)
   results = sparql.query().convert()

   results = pd.json_normalize(results['results']['bindings']).values.tolist()
   results = ["<" + x[1] + ">" for x in results]
   return [*set(results)] # remove duplicates

def wikidata_query_to_df(entity_uri):
   sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
   sparql.setQuery("""
      SELECT ?description ?is_a_type_of WHERE {
        %s schema:description ?description FILTER (lang(?description) = 'en') .
        %s wdt:P31 ?instanceOf .  
        ?instanceOf rdfs:label ?is_a_type_of FILTER (lang(?is_a_type_of) = 'en') .
      } limit 10
   """ % (entity_uri, entity_uri))

   sparql.setReturnFormat(JSON)
   results = sparql.query().convert()
   results2 = pd.json_normalize(results['results']['bindings'])
   prompt_text = ""
   for index, row in results2.iterrows():
        prompt_text += row['description.value'] + " is a type of " + row['is_a_type_of.value'] + "\n" 
   return prompt_text

def generate_prompt_text(entity_name):
   entity_uris = get_possible_entity_uris_from_wikidata(entity_name)
   prompt_text = ""
   for entity_uri in entity_uris:
       p = wikidata_query_to_df(entity_uri)
       if "disambiguation page" not in p:
           prompt_text += entity_name + " is " + wikidata_query_to_df(entity_uri)
   return prompt_text

if __name__ == "__main__":
   print("Sedona:", generate_prompt_text("Sedona"))
   print("California:", generate_prompt_text("California"))
   print("Bill Clinton:", generate_prompt_text("Bill Clinton"))
   print("Donald Trump:", generate_prompt_text("Donald Trump"))