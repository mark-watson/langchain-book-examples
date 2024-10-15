from langchain.agents import create_react_agent, Tool, AgentExecutor
from langchain.agents.agent_types import AgentType
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os

openai_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3, openai_api_key=openai_key)

ddg_api = DuckDuckGoSearchRun()

class DuckDuckGoSearchAPIWrapper:
    def __call__(self, query):
        results = ddg_api.invoke(query)
        #print(f"**** {results=}")
        return results if results else 'No results found'

class SimpleCalculator:
    def __call__(self, expression):
        try:
            return eval(expression)
        except Exception as e:
            return f"Error in calculation: {e}"

# Initialize the tools
search_tool = Tool(
    name="duckduckgo_search",
    func=DuckDuckGoSearchAPIWrapper(),
    description="Searches the web using DuckDuckGo"
)

calculator_tool = Tool(
    name="simple_calculator",
    func=SimpleCalculator(),
    description="Performs simple calculations"
)

# Define the tool chain
tools = [search_tool, calculator_tool]
tool_names = ["duckduckgo_search", "simple_calculator"]

agent_scratchpad = "thoughts: "

template = '''Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}'''

prompt = PromptTemplate.from_template(template)
print(prompt)

# Initialize the agent with tools
agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools)

# Example #1 input for the chain
input_text = "search: What is the population of Canada?"

# Run the chain
result = agent_executor.invoke({"input": input_text, "chat_history": agent_scratchpad})

# Print the result
print(result)

# Example #2 input for the chain
input_text = "calculator: 250 * 4"

# Run the chain
result = agent_executor.invoke({"input": input_text, "chat_history": agent_scratchpad})

# Print the result
print(result)