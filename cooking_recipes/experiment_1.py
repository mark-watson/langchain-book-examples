from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import DirectoryLoader
from langchain import OpenAI, VectorDBQA

embeddings = OpenAIEmbeddings()

loader = DirectoryLoader('./text_data/', glob="**/*.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=2500, chunk_overlap=0)

texts = text_splitter.split_documents(documents)

docsearch = Chroma.from_documents(texts, embeddings)

qa = VectorDBQA.from_chain_type(llm=OpenAI(temperature=0,
                                model_name="text-davinci-002"),
                                chain_type="stuff",
                                vectorstore=docsearch)
#qa.save_to_disk('index.json')

def query(q):
    print(f"\n\nRecipe creation request: {q}\n")
    print(f"{qa.run(q)}\n\n")

query("Create a new recipes using both Broccoli")
query("Create a new recipes using Beans, Rice, and Chicken")
