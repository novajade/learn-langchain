from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
prompt_value = prompt.invoke({"topic": "ice cream"})

print(prompt_value.to_string())


model = ChatOpenAI()
message = model.invoke(prompt_value)


output_parser = StrOutputParser()
print(output_parser.invoke(message))

# similar to unix pipe operator
chain = prompt | model | output_parser

result = chain.invoke({"topic": "ice cream"})
print(result)
