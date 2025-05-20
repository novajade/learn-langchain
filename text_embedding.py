from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import CSVLoader

embeddings_model = OpenAIEmbeddings()

embeddings = embeddings_model.embed_documents(
    [
        "Hello, There",
        "What's up",
        "How you doing",
        "Great, How about ya",
        "Great Thanks"
    ]
)

print(len(embeddings[0]))
print(len(embeddings[1]))

loader = CSVLoader(file_path='./csv_sample.csv')
data = loader.load()

embeddings = embeddings_model.embed_documents(
    [
        text.page_content for text in data
    ]
)
print(len(embeddings))

