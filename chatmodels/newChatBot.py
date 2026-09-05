from dotenv import load_dotenv

load_dotenv() 

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage



llm = HuggingFaceEndpoint (
    repo_id = "deepseek-ai/DeepSeek-V4-Flash-0731"
  
)

#Chatbot behaviour
print("Choose Your AI Mode")
print("Enter 1 for Normal mode")
print("Enter 2 for Angry mode")
print("Enter 3 for Sad mode")

choice = int(input("Enter your mode no."))

if(choice == 1):
    mode = "You are a normal AI agent and answers normally as you usually do"
elif(choice == 2):
    mode = "You are angry AI agent and answers in angry way"
elif(choice == 3):
    mode = "You are sad AI agent and answers in sad way"


history = [
     SystemMessage(content=mode)
]

model = ChatHuggingFace(llm = llm)

print("------------------------Welcome to ChatBot, enter exit to exit, Happy chatting---------------------------")
while True:
    prompt = input("You: ")
    history.append(HumanMessage(content = prompt))
    if(prompt == "exit"):
        print("Exit Successfully")
        break;
    response = model.invoke(history)
    history.append(AIMessage(content = response.content))
    print("Bot: ", response.content)