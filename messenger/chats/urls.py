from django.urls import path

from chats.views import chat_list, chat_page, send_message_post, read_message, get_member

urlpatterns = [
    path('chat_list/', chat_list, name='chat_list'),
    path('chat_page/', chat_page, name='chat_page'),
    path('send_message/', send_message_post, name='send_message'),
    path('read_message', read_message, name='read_message'),
    path('get_member', get_member, name='get_member')
]
