# Using Zapier Integrations With GMail and Google Calendar

Zapier is a service for writing integrations with hundreds of cloud services. Here we will write some demos for writing automatic integrations with Gmail and Google Calendar.

Using the Zapier service is simple. You need to register the services you want to interact with on the Zapier developer web site and then you can express how you want to interact with services using natural language prompts.

## Set Up Development Environment

You will need a developer key for [Zapier Natural Language Actions API](https://nla.zapier.com/get-started/). Go to this linked web page and look for "Dev App" in the "Provider Name" column. If a key does not exist, you'll need to set up an action to create a key. Click "Set up Actions" and follow the instructions. Your key will be in the Personal API Key column for the "Dev App." Click to reveal and copy your key. You can [read the documentation](https://nla.zapier.com/api/v1/dynamic/docs).

When I set up my Zapier account I set up three Zapier Natural Language Actions:

- Gmail: Find Email
- Gmail: Send Email
- Google Calendar: Find Event

If you do the same then you will see the Zapier registered actions:

![](zapier1.png)


## Sending a Test GMail

In the following example replace **TEST_EMAIL_ADDRESS** with an email address that you can use for testing.

```python
from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.utilities.zapier import ZapierNLAWrapper

llm = OpenAI(temperature=0)
zapier = ZapierNLAWrapper()
toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)
agent = initialize_agent(toolkit.get_tools(), llm, agent="zero-shot-react-description", verbose=True)

agent.run("Send an Email to TEST_EMAIL_ADDRESS via gmail that is a pitch for hiring Mark Watson as a consultant for deep learning and large language models")
```

Here is the sample output:

```console
$ python send_gmail.py


> Entering new AgentExecutor chain...
 I need to use the Gmail: Send Email tool
Action: Gmail: Send Email
Action Input: Send an email to TEST_EMAIL_ADDRESS with the subject "Pitch for Hiring Mark Watson as a Consultant for Deep Learning and Large Language Models" and the body "Dear Mark Watson, I am writing to you to pitch the idea of hiring you as a consultant for deep learning and large language models. I believe you have the expertise and experience to help us achieve our goals. Please let me know if you are interested in discussing further. Thank you for your time."
Cc: not enough information provided in the instruction, missing Cc
Observation: {"labelIds": "SENT"}
Thought: I now know the final answer
Final Answer: An email has been sent to TEST_EMAIL_ADDRESS with the subject "Pitch for Hiring Mark Watson as a Consultant for Deep Learning and Large Language Models" and the body "Dear Mark Watson, I am writing to you to pitch the idea of hiring you as a consultant for deep learning and large language models. I believe you have the expertise and experience to help us achieve our goals. Please let me know if you are interested in discussing further. Thank you for your time."

> Finished chain.
```

## Google Calendar Integration Example

Assuming that you configured the Zapier Natural Language Action "Google Calendar: Find Event" then the same code we used to send an email in the last section works for checking calendar entries, you just need to change the natural language prompt:

```python
from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.utilities.zapier import ZapierNLAWrapper

llm = OpenAI(temperature=0)
zapier = ZapierNLAWrapper()
toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)
agent = initialize_agent(toolkit.get_tools(), llm, 
                         agent="zero-shot-react-description", verbose=True)

agent.run("Get my Google Calendar entries for tomorrow")
```

And the output looks like: 

```console
$ python get_google_calendar.py

> Entering new AgentExecutor chain...
 I need to find events in my Google Calendar
Action: Google Calendar: Find Event
Action Input: Find events in my Google Calendar tomorrow
Observation: {"location": "Greg to call Mark on (928) XXX-ZZZZ", "kind": "calendar#event", "end__dateTime": "2023-03-23T10:00:00-07:00", "status": "confirmed", "end__dateTime_pretty": "Mar 23, 2023 10:00AM", "htmlLink": "https://zpr.io/WWWWWWWW"}
Thought: I now know the final answer
Final Answer: I have an event in my Google Calendar tomorrow at 10:00AM.

> Finished chain.
```

I edited this output to remove some private information.
