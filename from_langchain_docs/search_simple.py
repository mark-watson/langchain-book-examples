# make sure SERPER_API_KEY is set in your environment

from langchain_community.utilities import GoogleSerperAPIWrapper
search_helper = GoogleSerperAPIWrapper()

def search(query):
    return search_helper.run(query)

print(search("What is the capital of Arizona?"))
#print(search("Sedona Arizona?"))