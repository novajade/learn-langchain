from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders import UnstructuredHTMLLoader
from langchain_community.document_loaders import BSHTMLLoader
from langchain_community.document_loaders import json_loader

loader = CSVLoader(file_path='./csv_sample.csv')
data = loader.load()
print(type(data[0]).page_content)

loaderHTML = UnstructuredHTMLLoader("sample.html")
dataHTML = loader.load()
print(dataHTML)

#Beautiful Soup 도 동일
#json loader 동일

