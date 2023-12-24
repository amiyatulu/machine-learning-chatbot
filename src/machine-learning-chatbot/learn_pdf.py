# Don't work

from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import GPT4AllEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.llms import GPT4All
from langchain.chains import RetrievalQA
# from langchain.embeddings import HuggingFaceEmbeddings

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import ConversationalRetrievalChain


loader = PyMuPDFLoader("docs/example.pdf")
documents = loader.load()


text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=10)
texts = text_splitter.split_documents(documents)

persist_directory = "storage"
embeddings = GPT4AllEmbeddings(model="model/orca-mini-3b-gguf2-q4_0.gguf")
# vectordb = Chroma.from_documents(documents=texts, 
#                                  embedding=embeddings,
#                                  persist_directory=persist_directory)
# vectordb.persist()


# retriever = vectordb.as_retriever()
# callbacks = [StreamingStdOutCallbackHandler()]



# llm = GPT4All(
#     streaming=True,
#     model="model/orca-mini-3b-gguf2-q4_0.gguf",
#     verbose=True,
#     callbacks=callbacks,
# )

# qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
# qa = ConversationalRetrievalChain.from_llm(llm, db.as_retriever(), max_tokens_limit=400)


# # Chatbot loop
# chat_history = []
# print("Welcome to the State of the Union chatbot! Type 'exit' to stop.")
# while True:
#     query = input("Please enter your question: ")
    
#     if query.lower() == 'exit':
#         break
#     result = qa({"question": query, "chat_history": chat_history})

#     print("Answer:", result['answer'])