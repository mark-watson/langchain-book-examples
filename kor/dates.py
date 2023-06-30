" From documentation: https://eyurtsev.github.io/kor/"

from kor.extraction import create_extraction_chain
from kor.nodes import Object, Text, Number
from langchain.chat_models import ChatOpenAI
from pprint import pprint
import warnings ; warnings.filterwarnings('ignore')

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0,
    max_tokens=2000,
    frequency_penalty=0,
    presence_penalty=0,
    top_p=1.0,
)

schema = Object(
    id="date",
    description=(
        "Any dates found in the text. Should be output in the format:"
        " January 12, 2023"
    ),
    attributes = [
        Text(id = "month",
             description = "The month of the date",
             examples=[("Someone met me on December 21, 1995",
                        "Let's meet up on January 12, 2023 and discuss our yearly budget")])
    ],
)

chain = create_extraction_chain(llm, schema, encoder_or_encoder_class='json')


pred = chain.predict_and_parse(text="I will go to California May 1, 2024")['data']
print("* month mentioned in text=", pred)
