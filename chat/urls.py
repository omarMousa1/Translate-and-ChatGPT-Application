from django.urls import path

from . import views

urlpatterns = [
    path("nlp", views.machineTranslation, name="machine translation"),
    path('chatbot',views.chatbot,name= 'chatbot'),
    path("",view=views.index,name="index")
]