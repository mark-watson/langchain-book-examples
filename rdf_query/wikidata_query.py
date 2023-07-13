from llama_index import StringIterableReader, GPTTreeIndex
from wikidata_generate_prompt_text import generate_prompt_text

def wd_query(question, *entity_names):
    prompt_texts = []
    for entity_name in entity_names:
        prompt_texts += [generate_prompt_text(entity_name)]
    documents = StringIterableReader().load_data(texts=prompt_texts)
    index = GPTTreeIndex.from_documents(documents)
    index = index.as_query_engine(child_branching_factor=2)
    return index.query(question)

if __name__ == "__main__":
    print("Sedona:", wd_query("What is Sedona?", "Sedona"))
    print("California:", wd_query("What is California?", "California"))
    print("Bill Clinton:", wd_query("When was Bill Clinton president?", "Bill Clinton"))
    print("Donald Trump:", wd_query("Who is Donald Trump?", "Donald Trump"))
