from dotenv import load_dotenv

load_dotenv() 

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model = "mistral-small-2603", temperature=0.9)

#all prompts and responses will be here in history, so that bot can have context and memory to previous chat
history = [

]

print("----------------Welcome to AI chatbot, Press 0 to exit--------------------")
while True:
    prompt = input("You: ")
    history.append(prompt)
    if(prompt == "0"):
        print("Exit Successfully")
        break

    response = model.invoke(history)
    history.append(response)
    print("Bot: ",response.content) 