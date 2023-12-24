# Don't work

import os
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import GPT4AllEmbeddings
from gpt4all import GPT4All
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS


loader = PyMuPDFLoader("docs/example.pdf")
documents = loader.load()


text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)
embeddings = GPT4AllEmbeddings()
db = FAISS.from_documents(docs, embeddings)

query = "The study of great apes is highly relevant to the understanding of human evolution."
docs = db.similarity_search(query)

print(docs[0].page_content)