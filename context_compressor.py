from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAI
from langchain.retrievers import ContextualCompressionRetriever
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_community.vectorstores.chroma import Chroma


data = TextLoader('./state_of_the_union.txt').load()

# Split
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
splits = text_splitter.split_documents(data)

# VectorDB
embedding = OpenAIEmbeddings()
vectordb = Chroma.from_documents(documents=splits, embedding=embedding)

# Helper function for printing docs
def pretty_print_docs(docs):
    print(f"\n{'-' * 100}\n".join([f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(docs)]))

retriever = vectordb.as_retriever()
docs = retriever.get_relevant_documents("What did the president say about Ketanji Brown Jackson")

llm = OpenAI(temperature=0)
compressor = LLMChainExtractor.from_llm(llm)
compression_retriever = ContextualCompressionRetriever(
                            base_compressor=compressor,
                            base_retriever=retriever)

compressed_docs = compression_retriever.get_relevant_documents(
    "What did the president say about Ketanji Brown Jackson")
pretty_print_docs(compressed_docs)