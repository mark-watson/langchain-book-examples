# Derived from example in LangChain documentation:
#  https://langchain.readthedocs.io/en/latest/ecosystem/google_serper.html
# with slight modifications.

from langchain.utilities import BingSearchAPIWrapper
from langchain.llms.openai import OpenAI
from langchain.agents import initialize_agent, Tool

from langchain.agents import load_tools
tools = load_tools(["bing-search"])

import os

llm = OpenAI(temperature=0)
search = BingSearchAPIWrapper()
tools = [
    Tool(
        name="Intermediate Answer",
        func=search.run,
        description="Searches Bing for an intermediate answer.",
    )
]

self_ask_with_search = initialize_agent(tools, llm, agent="self-ask-with-search", verbose=True)
self_ask_with_search.run("What is the capital of Arizona?")
