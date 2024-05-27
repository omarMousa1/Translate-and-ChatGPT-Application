import os
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader
from langchain.document_loaders import WebBaseLoader

# PDF Loader example
def configure_api():
    os.environ["OPENAI_API_KEY"] = 'API Key'


def load_pdf(filename):

    loader = PyPDFLoader(filename)
    pages = loader.load()
    return pages


def load_youTube(url):
    save_dir="docs/youtube/"
    loader = GenericLoader(
        YoutubeAudioLoader([url],save_dir),
        OpenAIWhisperParser()
    )
    docs=loader.load()
    return docs


def load_website(url):
    loader=WebBaseLoader(url)
    docs = loader.load()
    return docs


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    configure_api()
    print("Connect to Open AI")
    # pages=load_pdf("docs/paper.pdf")
    # print(len(pages))
    # print(pages[4].page_content[0:500])
    #
    # # docs = load_youTube("https://www.youtube.com/watch?v=jGwO_UgTS7I")
    docs=load_website("https://medium.com/@onkarmishra/using-langchain-for-question-answering-on-own-data-3af0a82789ed")
    print(len(docs))
    # print(docs[0].page_content[0:500])



