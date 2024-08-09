install:
	pip install llama_index langchain trafilatura openai SPARQLWrapper rdflib rdflib-jsonld pydrive kor

clean:
	rm -r -f */*~ */#*
	rm -r -f */venv */*/venv
	rm -r -f */__pycache__ */*/__pycache__

