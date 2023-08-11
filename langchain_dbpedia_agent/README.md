# LangChain Agent Tool Example Using DBPedia SPARQL Queries

To run the example:

    python custom_func_dbpedia.py

Example output:

```
     select distinct ?s ?comment where {{
       ?s <http://www.w3.org/2000/01/rdf-schema#label>  '{name}'@en .
       ?s <http://www.w3.org/2000/01/rdf-schema#comment>  ?comment  .
       FILTER  (lang(?comment) = 'en') .
       ?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> {dbpedia_type} .
     }} limit 15



> Entering new AgentExecutor chain...

Invoking: `get_context_data` with `{'query_text': 'Berlin'}`


name='Berlin' dbpedia_type='<http://dbpedia.org/ontology/Place>'

     select distinct ?s ?comment where {
       ?s <http://www.w3.org/2000/01/rdf-schema#label>  'Berlin'@en .
       ?s <http://www.w3.org/2000/01/rdf-schema#comment>  ?comment  .
       FILTER  (lang(?comment) = 'en') .
       ?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Place> .
     } limit 15


{'context_text': "Berlin (/bɜːrˈlɪn/ bur-LIN, German: [bɛʁˈliːn]) is the capital and largest city of Germany by both area and population. Its 3.6 million inhabitants make it the European Union's most populous city, according to population within city limits. One of Germany's sixteen constituent states, Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital. Berlin's urban area, which has a population of around 4.5 million, is the second most populous urban area in Germany after the Ruhr. The Berlin-Brandenburg capital region has around 6.2 million inhabitants and is Germany's third-largest metropolitan region after the Rhine-Ruhr and Rhine-Main regions. . "}

Berlin is the capital and largest city of Germany. It is located in the northeastern part of the country. Berlin has a population of approximately 3.6 million people, making it the most populous city in the European Union. It is surrounded by the State of Brandenburg and is contiguous with Potsdam, the capital of Brandenburg. The urban area of Berlin has a population of around 4.5 million, making it the second most populous urban area in Germany after the Ruhr. The Berlin-Brandenburg capital region has a population of approximately 6.2 million, making it Germany's third-largest metropolitan region after the Rhine-Ruhr and Rhine-Main regions.

> Finished chain.
```
