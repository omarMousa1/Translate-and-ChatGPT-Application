from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
from django.shortcuts import render
from django.http import HttpResponse
from chatbot.chatbot import ChatwithAss

def nlp_task(chat_style,chat_text):
    # Use a breakpoint in the code line below to debug your script.
    os.environ["OPENAI_API_KEY"] = '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'
    # Define a template string
    template_string = """Translate  the text that is delimited by triple backticks \
                    into a style that is {style}. text: ```{text}```
                    """
    chat = ChatOpenAI(temperature=0.9)
    prompt_template = ChatPromptTemplate.from_template(template_string)

    # customer_message will generate the prompt and it will be passed into
    # the llm to get a response.
    customer_messages = prompt_template.format_messages(
        style=chat_style,
        text=chat_text)

    # Call the LLM to translate to the style of the customer message.
    customer_response = chat(customer_messages)
    return customer_response

def index(request):
    hello = "ass"
    context={
        'hello':hello,
    }
    return render(request,'homepage.html',context=context)


def machineTranslation(request):
    chat_style = "Arabic"
    if request.method == 'GET':
        chat_text = request.GET.get('message', '')
        chat_style = request.GET.get('lang', '')
    else:
        chat_text="My name is Abdukarim assistant professor at university of petra"

    # Call your NLP function with the provided style and text
    processed_text = nlp_task(chat_style, chat_text)
    context={
        'response':processed_text.content.replace("```",''),
        'message':chat_text,


    }

    # Pass the processed text to the template for rendering
    return render(request,'index.html', context)

# def index(request):
#     chat_style = """Arabic"""
#     chat_text = """My name is abdulkarim albanna I am Assistant professor at university of petra amman"""

#     response=nlp_task(chat_style,chat_text)
#     return HttpResponse(response.content)

def chatbot(request):
    chatbot = ChatwithAss()
    if request.method == 'GET':
        chat_text = request.GET.get('message', '')
        # chat_style = request.GET.get('lang', '')
        
        if chat_text =='':
            chat_text="My name is Abdukarim assistant professor at university of petra"
    else:
        chat_text="My name is Abdukarim assistant professor at university of petra"

    
    # Call your NLP function with the provided style and text
    resutls = chatbot.chat(chat_text)
    context={
    'response':resutls['result'],
    'message':chat_text,

}


    # Pass the processed text to the template for rendering
    return render(request,'index.html', context)