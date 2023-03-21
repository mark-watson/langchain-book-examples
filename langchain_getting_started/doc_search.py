# modified from the from documentation:
# https://langchain.readthedocs.io/en/latest/modules/indexes/examples/vectorstores.html

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

text_splitter = CharacterTextSplitter(chunk_size=250, chunk_overlap=10)

def text_helper(file_path):
    ret = ''
    with open(file_path) as f:
        ret = f.read()
    return ret

# TBD: finish example