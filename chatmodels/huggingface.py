from dotenv import load_dotenv

load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

#creating huggingfaceEndPoint;
llm = HuggingFaceEndpoint (
    repo_id = "deepseek-ai/DeepSeek-V4-Flash-0731"
  
)

model = ChatHuggingFace(llm = llm)

response = model.invoke("introduce cricket quickly")
print(response.content)