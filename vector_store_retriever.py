from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_chroma import Chroma

# loader = CSVLoader(file_path='./fortune_500_2020.csv')
# raw_documents = loader.load()

# text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0)
# documents = text_splitter.split_documents(raw_documents)
openai_embedding = OpenAIEmbeddings()
# db = Chroma.from_documents(documents, openai_embedding, persist_directory="./fortune_500_db")

#db.persist() 랭체인 업데이트 후 사용 X


db_conn = Chroma(persist_directory="./fortune_500_db", embedding_function=openai_embedding)
# query = "What is amazon Revenue?"
# docs = db_conn.similarity_search(query)
# print(docs[0].page_content)

#RETRIEVER
retriever = db_conn.as_retriever() #추상화
result = retriever.get_relevant_documents('walmart')
print(result[0].page_content)