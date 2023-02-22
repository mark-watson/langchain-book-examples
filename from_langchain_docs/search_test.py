# Derived from example in LangChain documentation:
#  https://langchain.readthedocs.io/en/latest/ecosystem/google_serper.html
# with slight modifications.

from langchain.utilities import GoogleSerperAPIWrapper

from langchain.utilities import GoogleSerperAPIWrapper
from langchain.llms.openai import OpenAI
from langchain.agents import initialize_agent, Tool

from langchain.agents import load_tools
tools = load_tools(["google-serper"])

import os

llm = OpenAI(temperature=0)
search = GoogleSerperAPIWrapper()
tools = [
    Tool(
        name="Intermediate Answer",
        func=search.run,
        description="Searches Google for an intermediate answer.",
    )
]

self_ask_with_search = initialize_agent(tools, llm, agent="self-ask-with-search", verbose=True)
self_ask_with_search.run("What is the capital of Arizona?")
