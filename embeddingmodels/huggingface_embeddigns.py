#free: using model through huggingface

from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv

load_dotenv() 

embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2",

)

texts = [
    "Hello my name is abhay"
    "Another day of learning Gen AI"
    "Btech is a course of 4 years"
]

vector = embeddings.embed_documents(texts)

print(vector)