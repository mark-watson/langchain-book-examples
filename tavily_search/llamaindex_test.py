from llama_hub.tools.tavily_research import TavilyToolSpec
from llama_index.agent import OpenAIAgent
import os

# set TAVILY_API_KEY environment variable

tavily_tool = TavilyToolSpec(api_key=os.environ.get("TAVILY_API_KEY"))

agent = OpenAIAgent.from_tools(tavily_tool.to_tool_list())

print(agent.chat("What are fun things to do in Sedona Arizona?"))