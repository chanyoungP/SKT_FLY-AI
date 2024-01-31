import os 
from dotenv import load_dotenv
import langchain
import openai
from langchain.llms import AzureOpenAI
# from langchain_openai import AzureOpenAI

load_dotenv()



# llm = AzureOpenAI(
#                   deployment_name='dev-gpt-35-turbo-instruct'
#       )

# llm.invoke('why python is the most popular language?')


# from langchain.chat_models import AzureChatOpenAI

# chatgpt = AzureChatOpenAI(deployment_name='dev-gpt-35-turbo', temperature=0)
# answer = chatgpt.invoke('Why Python is the most popular language?')
# print(answer.content)


# chatgpt = AzureChatOpenAI(deployment_name='dev-gpt-35-turbo', temperature=1)
# answer = chatgpt.invoke('Why Python is the most popular language?')
# print(answer.content)

# chatgpt = AzureChatOpenAI(deployment_name='dev-gpt-35-turbo', temperature=1)
# answer = chatgpt.invoke('Why Python is the most popular language? answer the Korean')
# print(answer.content)


# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
# chatgpt = AzureChatOpenAI(
#               deployment_name='dev-gpt-35-turbo',
#               temperature=1,
#               streaming=True,
#               callbacks=[StreamingStdOutCallbackHandler]
# )

# answer = chatgpt.invoke('Why python is the most popular language?')

from langchain.chat_models import AzureChatOpenAI
from langchain.schema import SystemMessage, AIMessage, HumanMessage

# chatgpt = AzureChatOpenAI(deployment_name='dev-gpt-35-turbo',temperature=0)

# message = [
#     SystemMessage(content = "you are a helpful assistant that translates English to Korean"),
#     HumanMessage(content = "I love Azure Python")

# ]

# response = chatgpt(message)
# print(response)

##

chatgpt = AzureChatOpenAI(deployment_name='dev-gpt-35-turbo',
                          temperature=0,
)

message = [
    SystemMessage(content = "you are a helpful assistant that make study plan if you got user's study subject then you make a study plan"),
    HumanMessage(content = "Azure")

]

response = chatgpt(message)
print(response)
