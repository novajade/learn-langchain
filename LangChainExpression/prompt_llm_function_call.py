from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers.openai_functions import (
    JsonOutputFunctionsParser,
    JsonKeyOutputFunctionsParser)
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
model = ChatOpenAI()

# function call
functions = [
    {
        "name": "joke",
        "description": "A joke",
        "parameters": {
            "type": "object",
            "properties": {
                "setup": {"type": "string", "description": "The setup for the joke"},
                "punchline": {
                    "type": "string",
                    "description": "The punchline for the joke",
                },
            },
            "required": ["setup", "punchline"],
        },
    }
]
chain = prompt | model.bind(function_call={"name": "joke"}, functions=functions)
print(chain.invoke({"topic": "ice cream"}, config={}))

# chain = prompt | model.bind(function_call={"name": "joke"}, functions=functions) | JsonOutputFunctionsParser()
# print(chain.invoke({"topic": "ice cream"}))

# chain = prompt | model.bind(function_call={"name": "joke"}, functions=functions) | JsonKeyOutputFunctionsParser(key_name="setup")
# print(chain.invoke({"topic": "ice cream"}))


map_ = RunnableParallel(topic=RunnablePassthrough())
chain = (
    map_
    | prompt
    | model.bind(function_call={"name": "joke"}, functions=functions)
    | JsonKeyOutputFunctionsParser(key_name="setup")
)
print(chain.invoke("ice cream"))


chain = (
    {"topic": RunnablePassthrough()}
    | prompt
    | model.bind(function_call={"name": "joke"}, functions=functions)
    | JsonKeyOutputFunctionsParser(key_name="setup")
)
print(chain.invoke("ice cream"))