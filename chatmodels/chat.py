from dotenv import load_dotenv

load_dotenv()  #importing and using dotenv so that we can use env file api here;

#one more method using model class
# from langchain_openai import ChatOpenAI

# model = ChatOpenAI(model="gpt-5.5")
# --------------------------------------------------------------

#and this one is using init chat model -below
# from langchain.chat_models import init_chat_model

# model = init_chat_model("gpt-4.1")
# -----------------------------------------------------------------

#below we are using google gemini 3.5 as its free
# model = init_chat_model(
#     model="gemini-3.5-flash-lite",  # Free tier eligible model
#     model_provider="google_genai"   # Explicitly defines the provider
# )

# model = init_chat_model("google_genai:gemini-3.5-flash-lite") here dont need to provide model and provider as parameter
# ---------------------------------------------------------------------

# lets use mistral ai as its free
from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model = "mistral-small-2603", temperature=0.9, max_tokens=20)

response = model.invoke("write a poem about AI")
print(response.content) 
# print(response.content[0]["text"]) #to get only content not other things in gemini model