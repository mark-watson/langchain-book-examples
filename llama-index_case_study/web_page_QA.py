# Derived from examples in llama_index documentation

# pip install llama-index html2text trafilatura

from pprint import pprint
from llama_index.core import Document
import trafilatura

from llama_index.core import VectorStoreIndex

def query_website(url, *questions):
    downloaded = trafilatura.fetch_url(url)
    text = trafilatura.extract(downloaded)
    #print(text)
    list_of_documents = [Document(text=text)]
    index = VectorStoreIndex.from_documents(list_of_documents)   #.from_texts([text])
    engine = index.as_query_engine()
    for question in questions:
        print(f"\n== QUESTION: {question}\n")
        response = engine.query(question)
        print(f"== RESPONSE: {response}")

if __name__ == "__main__":
  url = "https://markwatson.com"
  query_website(url, "What instruments does Mark play?",
                     "How many books has Mark written?",
                     "list company names beginning with the letter 'C'")
