# pip install xformers

from llama_index import ListIndex, SimpleDirectoryReader
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index import LangchainEmbedding, ServiceContext
from transformers import pipeline
import time
import torch
from langchain.llms.base import LLM
from llama_index import LLMPredictor

class CustomLLM(LLM):
    model_name = "facebook/opt-iml-1.3b"
    # I am not using a GPU, but you can add device="cuda:0"
    # to the pipeline call if you have a local GPU or
    # are running this on Google Colab:
    pipeline = pipeline("text-generation", model=model_name,
                        model_kwargs={"torch_dtype":torch.bfloat16})

    def _call(self, prompt, stop = None):
        prompt_length = len(prompt)
        response = self.pipeline(prompt, max_new_tokens=200)
        first_response = response[0]["generated_text"]
        # only return newly generated tokens
        returned_text = first_response[prompt_length:]
        return returned_text

    @property
    def _identifying_params(self):
        return {"name_of_model": self.model_name}

    @property
    def _llm_type(self):
        return "custom"

time1 = time.time()

# define our LLM
llm_predictor = LLMPredictor(llm=CustomLLM())

# load in HF embedding model from langchain
embed_model = LangchainEmbedding(HuggingFaceEmbeddings())
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, embed_model=embed_model)
print("Done creating service context")

# build index
documents = SimpleDirectoryReader('../data').load_data()
new_index = ListIndex.from_documents(documents, service_context=service_context)
print("Done building index")

# query with embed_model specified
query_engine = new_index.as_query_engine(
    #retriever_mode="embedding", 
    retriever_mode="default",
    response_mode = "simple_summarize",
    verbose=True, 
    service_context=service_context
)
print("Done creating query engine")

def query(query_string):
    response = query_engine.query(query_string)
    print(response)
    return response

query("what is the definition of Chemistry?")
query("what are the benefits of sports?")
query("why study economics?")
