#structured output

from dotenv import load_dotenv

load_dotenv() 

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate # to use prompt template
from pydantic import BaseModel;
from typing import List,Optional;
from langchain_core.output_parsers import PydanticOutputParser



llm = HuggingFaceEndpoint (
    repo_id = "deepseek-ai/DeepSeek-V4-Flash-0731",
    max_new_tokens=2048
  
)

model = ChatHuggingFace(llm = llm)


#schema
class Movie (BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie) 


prompt = ChatPromptTemplate.from_messages(
         [
             ('system', """
             Extract movie information from the paragraph
             {format_instructions}
             """),
             ("human","{paragraph}")
         ]
)

para = input("Enter your paragraph: ")

final_prompt = prompt.invoke(
    { "paragraph":para,
       "format_instructions":parser.get_format_instructions()
     }
    )

response = model.invoke(final_prompt)
movie_data = parser.parse(response.content)

print(movie_data)

