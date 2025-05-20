from operator import itemgetter
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough

runnable = RunnableParallel(
    passed=RunnablePassthrough()
)

print(runnable.invoke({"num": 1}))


runnable = RunnableParallel(
    passed=RunnablePassthrough(),
    extra=RunnablePassthrough.assign(mult=lambda x: x["num"] * 3),
    modified=lambda x: x["num"] + 1,
)

print(runnable.invoke({"num": 1}))


from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableParallel

model = ChatOpenAI()

joke_chain = ChatPromptTemplate.from_template("tell me a joke about {topic}") | model
poem_chain = (
    ChatPromptTemplate.from_template("write a 2-line poem about {topic}") | model
)

# easy to execute multiple Runnables in parallel
# 이렇게 하나로 다수의 답을 받을 수 있도록 처리 가능
map_chain = RunnableParallel(joke=joke_chain, poem=poem_chain)

result = map_chain.invoke({"topic": "bear"})
print("Joke:", result["joke"].content)
print("Poem:", result["poem"].content)
