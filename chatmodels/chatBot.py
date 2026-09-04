from dotenv import load_dotenv

load_dotenv() 

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage #to add distinct roles in our history;



model = ChatMistralAI(model = "mistral-small-2603", temperature=0.9)

#all prompts and responses will be here in history, so that bot can have context and memory to previous chat
history = [
     SystemMessage(content = "You are a Rude AI agent")
]

print("----------------Welcome to AI chatbot, Press 0 to exit--------------------")
while True:
    prompt = input("You: ")
    history.append(HumanMessage(content = prompt))
    if(prompt == "0"):
        print("Exit Successfully")
        break

    response = model.invoke(history)
    history.append(AIMessage(content = response.content))
    print("Bot: ",response.content) 