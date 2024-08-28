# Running the example

You will need Google and OpenAI API keys (see book text).

Install virtualenv if required and set up a local environment:

    pip install virtualenv  # if not already installed
    python3 -m venv env     # create virtual env in current directory
    source env/bin/activate # activate virtual environment
    pip install -U llama-index
    python Google_Knowledge_Graph_Search.py