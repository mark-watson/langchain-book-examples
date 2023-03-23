# SqLite Chat Demo Script
# Reference:
#   https://langchain.readthedocs.io/en/latest/modules/chains/examples/sqlite.html

from langchain import OpenAI, SQLDatabase, SQLDatabaseChain

db = SQLDatabase.from_uri("sqlite:///chinook.db")
llm = OpenAI(temperature=0)

db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)

db_chain.run("How many employees are there?")
db_chain.run("What is the name of the first employee?")
db_chain.run("Which customer has the most invoices?")
db_chain.run("List all music genres in the database")
