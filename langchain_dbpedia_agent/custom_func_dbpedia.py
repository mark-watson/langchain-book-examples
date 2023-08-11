from QA import get_context_text

def get_context_data(query_text):
    """Method to get context text for entities from DBPedia using SPARQL query"""

    query_text_data = get_context_text(query_text)
    return {"context_text": query_text_data}


## Custom function example using DBPedia

from typing import Type
from pydantic import BaseModel, Field
from langchain.tools import BaseTool


class GetContextTextFromDbPediaInput(BaseModel):
    """Inputs for get_context_data"""

    query_text: str = Field(description="query_text user supplied query text")


class GetContextTextFromDbPediaTool(BaseTool):
    name = "get_context_data"
    description = """
        Useful when you want to make a query and get context text from DBPedia.
        You should enter and text containing entity names
        """
    args_schema: Type[BaseModel] = GetContextTextFromDbPediaInput

    def _run(self, query_text: str):
        text = get_context_data(query_text)
        return text

    def _arun(self, query_text: str):
        raise NotImplementedError("get_context_data does not support async")


## Create agent

from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent

llm = ChatOpenAI(model="gpt-3.5-turbo-0613", temperature=0)

tools = [GetContextTextFromDbPediaTool()]

agent = initialize_agent(tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True)

## Run agent

agent.run(
    "What country is Berlin in and what other information about the city do you have?"
)
