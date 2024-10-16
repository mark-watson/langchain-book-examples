from langchain.llms import OpenAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain_experimental.sql.base import SQLDatabase

# Initialize the database and LLM
db = SQLDatabase.from_uri("sqlite:///chinook.db")
llm = OpenAI(temperature=0)

# Create a SQLDatabaseChain
db_chain = SQLDatabaseChain.from_llm(llm=llm, db=db, verbose=True)

# Run queries
db_chain.run("How many employees are there?")
db_chain.run("What is the name of the first employee?")
db_chain.run("Which customer has the most invoices?")
db_chain.run("List all music genres in the database")