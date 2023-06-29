# Derived from example:
#   https://gpt-index.readthedocs.io/en/latest/how_to/custom_llms.html

import time
import torch
from langchain.llms.base import LLM
from llama_index import SimpleDirectoryReader, LangchainEmbedding
from llama_index import ListIndex, PromptHelper
from llama_index import LLMPredictor
from transformers import pipeline

max_input_size = 512
num_output = 64
max_chunk_overlap = 0 # 10
prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)

class CustomLLM(LLM):
    model_name = "facebook/opt-iml-1.3b"
    # I am not using a GPU, but you can add device="cuda:0"
    # to the pipeline call if you have a local GPU or
    # are running this on Google Colab:
    pipeline = pipeline("text-generation", model=model_name,
                        model_kwargs={"torch_dtype":torch.bfloat16})

    def _call(self, prompt, stop = None):
        prompt_length = len(prompt)
        response = self.pipeline(prompt, max_new_tokens=num_output)
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

# Load the your data
documents = SimpleDirectoryReader('../data_small').load_data()
# llama_index < 0.5:
#index = GPTListIndex(documents, llm_predictor=llm_predictor,
#                     prompt_helper=prompt_helper)

# llama_index >= 0.5: (not yet working)
index = ListIndex.from_documents(documents=documents, 
                                 llm_predictor=llm_predictor,
                                 prompt_helper=prompt_helper)
#index = index.from_documents(documents)
index = index.as_query_engine(llm_predictor=llm_predictor)

time2 = time.time()
print(f"Time to load model from disk: {time2 - time1} seconds.")

print(dir(index))
# Query and print response
response = index.query("What is the definition of sport?")
print(response)

time3 = time.time()
print(f"Time for query/prediction: {time3 - time2} seconds.")