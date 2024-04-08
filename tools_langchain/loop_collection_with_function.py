# example from documentation: https://github.com/cristobalcl/LearningLangChain/blob/master/notebooks/01%20-%20Simple%20Agent.ipynb

from langchain.agents import initialize_agent, Tool
from langchain_community.llms import OpenAI

from typing import Callable

llm = OpenAI(temperature=0)

# define a looping tool


def loop(a_function: Callable, a_collection: list) -> list: # needs Python 3.9 or above
    print(f"Function: {a_function} Collection: {a_collection}")
    result = []
    for item in a_collection:
        result.append(a_function(item))
    return result 

def loop2(input: str) -> str:
    values = input.split("to")
    start = int(values[0])
    end = int(values[1])
    result = 0
    for i in range(start, end + 1):
        result += i
    return str(result)  


# define 2 tools to experiment with

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
        name = "Loop",
        func=loop,
        description="Applies a boolean function to each element of a collection and if the function returns true then add the element to the result. Input should be in the form 'function collection'."
    ),
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

# initialize the agent

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

def test1():
    print(agent.run("If we add 3, 5, 19 20 and 24, is the result a prime number?"))

def test2():
    print(agent.run("Loop over the collection [10, 11, 12, 13, 14] and test each for being a prime number. Sum up the prime numbers"))

def test3():
    def foo(x):
        return x + 1
    print(loop(foo, [1, 2, 3, 4, 5]))

def test4():
    print(loop("1to10"))

test2()
    
