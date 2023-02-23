# Derived from the example at:
# https://github.com/jerryjliu/gpt_index/blob/main/examples/data_connectors/WebPageDemo.ipynb

# pip install llama-index, html2text, trafilatura

from llama_index import GPTListIndex
from llama_index import TrafilaturaWebReader

def query_website(url_list, *questions):
    documents = TrafilaturaWebReader().load_data(url_list)
    index = GPTListIndex(documents)
    for question in questions:
        print(f"\n== QUESTION: {question}\n")
        response = index.query(question)
        print(f"== RESPONSE: {response}")

if __name__ == "__main__":
  url_list = ["https://markwatson.com"]
  query_website(url_list, "What programming languages does Mark use?",
                          "How many books has Mark written?",
                          "What musical instruments does Mark play?")
