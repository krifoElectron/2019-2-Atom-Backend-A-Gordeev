from django.urls import path

from chats.views import chat_list, chat_page

urlpatterns = [
    path('chat_list/', chat_list, name='chat_list'),
    path('chat_page/', chat_page, name='chat_page'),
]
