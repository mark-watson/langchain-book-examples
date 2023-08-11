# Copyright 2021-2023 Mark Watson
# This is an example I wriote and distributed in 2021. Here I am just
# reusing a few functions for my LangChain Agent book chapter.
#
# Original Colab notebook:
# https://colab.research.google.com/drive/1FX-0eizj2vayXsqfSB2ONuJYG8BaYpGO?usp=sharing

# !pip install import spacy
# !python -m spacy download en_core_web_sm

import spacy

nlp_model = spacy.load("en_core_web_sm")

from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")


def query(query):
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()["results"]["bindings"]


def entities_in_text(s):
    doc = nlp_model(s)
    ret = {}
    for [ename, etype] in [[entity.text, entity.label_] for entity in doc.ents]:
        if etype in ret:
            ret[etype] = ret[etype] + [ename]
        else:
            ret[etype] = [ename]
    return ret


# NOTE: !! note "{{" .. "}}" double curly brackets: this is to escape for Python String format method:

sparql_query_template = """
     select distinct ?s ?comment where {{
       ?s <http://www.w3.org/2000/01/rdf-schema#label>  '{name}'@en .
       ?s <http://www.w3.org/2000/01/rdf-schema#comment>  ?comment  .
       FILTER  (lang(?comment) = 'en') .
       ?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> {dbpedia_type} .
     }} limit 15
"""
print(sparql_query_template)


def dbpedia_get_entities_by_name(name, dbpedia_type):
    print(f"{name=} {dbpedia_type=}")
    s_query = sparql_query_template.format(name=name, dbpedia_type=dbpedia_type)
    print(s_query)
    results = query(s_query)
    return results


entity_type_to_type_uri = {
    "PERSON": "<http://dbpedia.org/ontology/Person>",
    "GPE": "<http://dbpedia.org/ontology/Place>",
    "ORG": "<http://dbpedia.org/ontology/Organisation>",
}


def get_context_text(query_text):
    entities = entities_in_text(query_text)

    def helper(entity_type):
        ret = ""
        if entity_type in entities:
            for hname in entities[entity_type]:
                results = dbpedia_get_entities_by_name(
                    hname, entity_type_to_type_uri[entity_type]
                )
                for result in results:
                    ret += ret + result["comment"]["value"] + " . "
        return ret

    context_text = helper("PERSON") + helper("ORG") + helper("GPE")
    #print("\ncontext text:\n", context_text, "\n")
    return context_text

