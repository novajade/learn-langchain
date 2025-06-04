from operator import itemgetter
from langchain_openai import ChatOpenAI
# 메모리
from langchain.memory import ConversationBufferMemory

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough

model = ChatOpenAI()
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful chatbot"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

#메모리를 가져올 수 있게
memory = ConversationBufferMemory(return_messages=True)

chain = (
    RunnablePassthrough.assign(
        history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
    )
    | prompt
    | model
)

inputs = {"input": "Hello, My name is Joon"}
response = chain.invoke(inputs)
print(response)

memory.save_context(inputs, {"output": response.content}) # type: ignore

print(memory.load_memory_variables({}))


inputs = {"input": "whats my name"}
response = chain.invoke(inputs)
print(response)
