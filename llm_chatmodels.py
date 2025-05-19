from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.schema import SystemMessage, HumanMessage
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import ChatPromptTemplate
import os

load_dotenv()

template = "You are a helpful assistant that translates {input_language} to {output_language}"
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages(
    [("system", template), 
     ("human", human_template),]
)

resp = chat_prompt.format_messages(
    input_language="English",
    output_language="Chinese",
    text="I love Programming"
)

# print(resp)

chat_model = ChatOpenAI()
print(chat_model(resp))



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


