from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.schema import SystemMessage, HumanMessage
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import ChatPromptTemplate
import os

load_dotenv()




# prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")

# resp = prompt.format(product = "colorful socks")
# print(resp)

# #llm = OpenAI()
# #chat_model = ChatOpenAI()



# text = "What would be a good company name for a company that makes colorful socks?"
# message = [SystemMessage(content = "You are a oldman"),
# HumanMessage(content=text)]
# #print(llm.invoke(text))

# response = chat_model.invoke(message)
# print(response.content)


