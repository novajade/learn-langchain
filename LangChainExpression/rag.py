from operator import itemgetter
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain_community.vectorstores.faiss import FAISS

embedding_model = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(
    ["harrison worked at kensho"], embedding=embedding_model
)

# save 예시
vectorstore.save_local("faiss_index")
# load 예시
vectorstore_new = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)

retriever = vectorstore_new.as_retriever()

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

model = ChatOpenAI()

# LCEL
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

print(chain.invoke("where did harrison work?"))

###

template = """Answer the question based only on the following context:
{context}

Question: {question}

Answer in the following language: {language}
"""
prompt = ChatPromptTemplate.from_template(template)

chain = (
    {
        "context": itemgetter("question") | retriever,
        "question": itemgetter("question"),
        "language": itemgetter("language"),
    }
    | prompt
    | model
    | StrOutputParser()
)

print(chain.invoke({"question": "where did harrison work", "language": "korean"}))
"""
Harrison ha lavorato a Kensho.
"""

# # itemgetter example
# from operator import itemgetter
# # Suppose we have a dictionary
# person = {'name': 'Alice', 'age': 30, 'job': 'Engineer'}
# # We can use itemgetter to create a function that fetches the 'name' from a dictionary
# get_name = itemgetter('name')
# # Now, when we use this function with our dictionary
# name = get_name(person)
# print(name)  # Output: Alice