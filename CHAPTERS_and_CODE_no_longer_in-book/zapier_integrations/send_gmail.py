from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.utilities.zapier import ZapierNLAWrapper

llm = OpenAI(temperature=0)
zapier = ZapierNLAWrapper()
toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)
agent = initialize_agent(toolkit.get_tools(), llm, 
                         agent="zero-shot-react-description", verbose=True)

agent.run("Send an Email to mark_watson99test.com via gmail that is a pitch for hiring Mark Watson as a consultant for deep learning and large language models")
