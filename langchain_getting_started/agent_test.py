from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)

def add(input: str) -> str:
    values = [int(x) for x in input.split("+")]
    return str(sum(values))

def is_prime(input: str) -> str:
    n = int(input)

    if n <= 1:
        return "no"
    if n <= 3:
        return "yes"
    if n % 2 == 0 or n % 3 == 0:
        return "no"

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return "no"
        i += 6

    return "yes"

tools = [
    Tool(
        name = "Add",
        func=add,
        description="Useful for when you need to add numbers. Input should be in the form '1 + 2 + 3'."
    ),
    Tool(
        name = "IsPrime",
        func=is_prime,
        description="Useful to know if a number is prime."
    ),
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

print(agent.run("Add the first 10 numbers and tell me if it's prime."))

