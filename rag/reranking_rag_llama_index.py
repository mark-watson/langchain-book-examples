from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.postprocessor import SentenceTransformerRerank

# Set up the ingestion pipeline with transformations
pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=25, chunk_overlap=0),
        TitleExtractor(),
        OpenAIEmbedding(),
    ]
)

# Load documents using a directory reader
documents = SimpleDirectoryReader("../data").load_data()

# Create an index from the documents
index = VectorStoreIndex.from_documents(documents)

# Initialize the reranker with a specific model
reranker = SentenceTransformerRerank(
    model="cross-encoder/ms-marco-MiniLM-L-12-v2",  # Example model, adjust as needed
    top_n=3  # Adjust the number of top documents to rerank
)

# Set up the query engine with the reranker as a postprocessor
query_engine = index.as_query_engine(
    similarity_top_k=10,  # Set for how many results to retrieve before reranking
    node_postprocessors=[reranker]  # Add the reranker to the postprocessing steps
)

# Perform a query
#response = query_engine.query("List a few sports")
response = query_engine.query("Compare sports with the study of health issues")

# Print the response
print(response)