from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser

chain = (
    PromptTemplate.from_template(
        """Given the user question below, classify it as either being about `Strawberry`, `Banana`, or `Other`.

Do not respond with more than one word.

<question>
{question}
</question>

Classification:"""
    )
    | ChatOpenAI()
    | StrOutputParser()
)

print(chain.invoke({"question": "What is the fruit that has red color?"}))
"""
Strawberry
"""

strawberry_chain = (
    PromptTemplate.from_template(
        """You are an expert about strawberry. \
Always answer questions starting with "As a Strawberry expert ... ". \
Respond to the following question:

# Question: {question}
# Answer:"""
    )
    | ChatOpenAI()
)

banana_chain = (
    PromptTemplate.from_template(
        """You are an expert about banana. \
Always answer questions starting with "As a Banana expert ... ". \
Respond to the following question:

# Question: {question}
# Answer:"""
    )
    | ChatOpenAI()
)

general_chain = (
    PromptTemplate.from_template(
        """Respond to the following question:

Question: {question}
Answer:"""
    )
    | ChatOpenAI()
)


from langchain.schema.runnable import RunnableBranch

# the first element is a condition (a lambda function) and 
# the second element is the chain to execute if the condition is true
branch = RunnableBranch(
    (lambda x: "strawberry" in x["topic"].lower(), strawberry_chain), # type: ignore
    (lambda x: "banana" in x["topic"].lower(), banana_chain), # type: ignore
    general_chain,
)

# chain is invoked to classify the question, and its output is stored under the key topic. 
# The original question is passed through unchanged under the key question.
full_chain = {"topic": chain, "question": lambda x: x["question"]} | branch

result1=(full_chain.invoke({"question": "What is the fruit that has red color?"}))
result2=(full_chain.invoke({"question": "What is the fruit that has yellow color?"}))
result3=(full_chain.invoke({"question": "What is the fruit that has green color?"}))

print(result1.content)
print(result2.content)
print(result3.content)