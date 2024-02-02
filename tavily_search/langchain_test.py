import os
from langchain.utilities.tavily_search import TavilySearchAPIWrapper
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from langchain.tools.tavily_search import TavilySearchResults

# set TAVILY_API_KEY environment variable

# set up the agent
llm = ChatOpenAI(model_name="gpt-4", temperature=0.5)
search = TavilySearchAPIWrapper()
tavily_tool = TavilySearchResults(api_wrapper=search)

# initialize the agent
agent_chain = initialize_agent(
    [tavily_tool],
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

# run the agent
print(agent_chain.run("What are fun things to do in Sedona Arizona?"))