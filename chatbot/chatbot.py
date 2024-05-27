from langchain.text_splitter import RecursiveCharacterTextSplitter,CharacterTextSplitter
import os
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader
from langchain.document_loaders import WebBaseLoader
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
class ChatwithAss():
    @staticmethod
    def configure_api():
        os.environ["OPENAI_API_KEY"] = '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'

    @staticmethod
    def load_pdf(filename):
        loader = PyPDFLoader(filename)
        pages = loader.load()
        return pages

    @staticmethod
    def load_youTube(url):
        save_dir="docs/youtube/"
        loader = GenericLoader(
            YoutubeAudioLoader([url],save_dir),
            OpenAIWhisperParser()
        )
        docs=loader.load()
        return docs

    @staticmethod
    def load_website(url):
        loader=WebBaseLoader(url)
        docs = loader.load()
        return docs


    def __init__(self,pdfPath =None,youtube=None,websites = None) -> None:
        self.configure_api()
        self.docs=[]
        self.llm = ChatOpenAI( temperature=0)
        self.embedding = OpenAIEmbeddings()
        persist_directory = r'chrome/'
        self.vectordb = Chroma(persist_directory=persist_directory, embedding_function=self.embedding)
        self.qa_chain = RetrievalQA.from_chain_type(
                self.llm,
                retriever=self.vectordb.as_retriever()
            )
        if pdfPath != None:
            self.docs += self.load_pdf(pdfPath)
        if youtube !=None:
            self.docs += self.load_youTube(youtube)
        if websites != None:
            self.docs += self.load_website(websites)
        
    def chat(self,query:str):
        result = self.qa_chain({"query": query})
        return result
        

            
            
            