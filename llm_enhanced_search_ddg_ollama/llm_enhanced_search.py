from ddg import Duckduckgo
from langchain_community.llms.ollama import Ollama

# pip install llama-index html2text trafilatura
import trafilatura

from pprint import pprint

ddg_api = Duckduckgo()


llm = Ollama(
    model="mistral:v0.3",
    verbose=False,
    #callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
)

prompt1 = "return concisely either 'Y' or 'N' if this query | %s | is matched well by the following text: %s"
prompt2 = "Using the query | %s | summarize the following text including only material relevant to the query:\n%s"
prompt3 = "Using the query | %s | summarize in multiple paragraphs the following text including only material relevant to the query:\n%s"

def llm_search(query):
    results = ddg_api.search(query)
    data = results['data']
    good_results = []
    good_summaries = []
    for d in data:
        description = d['description']
        p = prompt1 % (query, description)
        s = llm.invoke(p)
        print(f"Prompt: {p}\nResponse: {s}\n\n")
        if s.strip()[0:1] == 'Y':
            good_results.append(d)
            uri = d['url']
            downloaded = trafilatura.fetch_url(uri)
            text = trafilatura.extract(downloaded)
            p2 = prompt2 % (query, text)
            s2 = llm.invoke(p2)
            good_summaries.append(s2)
    p3 = prompt3 % (query, "\n\n".join(good_summaries))
    final_summary = llm.invoke(p3)

    return (good_results, good_summaries, final_summary)

def test1():
    (results, summaries, final_summary) = llm_search("Common Lisp and Deep Learning consultant")

    print(f"\n\n****** Good Results ******\n\n")
    print(results)

    print(f"\n\n****** Good Summaries ******\n\n")
    print(summaries)

    print(f"\n\n****** Final Summary ******\n\n")
    print(final_summary)

test1()

def test2():
    (results, summaries, final_summary) = llm_search("Write a business plan for a new startup using LLMs and expertise in medical billing.")

    print(f"\n\n****** Good Results ******\n\n")
    print(results)

    print(f"\n\n****** Good Summaries ******\n\n")
    print(summaries)

    print(f"\n\n****** Final Summary ******\n\n")
    print(final_summary)

# test2()