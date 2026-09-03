#Paid

from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv() 

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=64
)

texts = [
    "Hello my name is abhay"
    "Another day of learning Gen AI"
    "Btech is a course of 4 years"
]

# vector = embeddings.embed_query("hello welcome back to vs code") # we use query for one line
vector = embeddings.embed_documents(texts)
print(vector)