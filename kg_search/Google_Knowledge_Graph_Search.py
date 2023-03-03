"""Example of Python client calling Knowledge Graph Search API."""

from llama_index import GPTListIndex, Document

import Google_KG_helper

def kg_search(entity_name, *questions):
    ret = ""
    context_text = Google_KG_helper.get_context_text(entity_name)
    print(f"Context text: {context_text}")
    doc = Document(context_text)
    index = GPTListIndex([doc])
    for question in questions:
        response = index.query(question)
        ret += f"QUESTION:  {question}\nRESPONSE: {response}\n"
    return ret

if __name__ == "__main__":
    print(kg_search("Bill Clinton", "When was Bill president?"))
