from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
import time
import traceback
import json

from chats.models import Chat
from chats.models import Message
from members.models import Member
from user_profile.models import User

from .forms import MessageForm


def chat_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    user_id = int(request.GET.get('user_id'))

    required_user = User.objects.get(id=user_id)

    required_members = Member.objects.filter(user=user_id)

    chats = []

    for member in required_members:
        chat = member.chat
        print(member.user_id, 'id')
        members = Member.objects.filter(chat=chat)
        name = ''
        if members[0].user.id != user_id:
            name = members[0].user.first_name
        else:
            name = members[1].user.first_name

        chats.append({'title': chat.title,
                      'isGroupChat': chat.is_group_chat,
                      'lastMessage': chat.last_message.text if chat.last_message else '',
                      'date': chat.last_message.added_at if chat.last_message else '',
                      'chatId': chat.id,
                      'name': name})

    return JsonResponse({'chats': chats})


def chat_page(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    chat_id = request.GET.get('chat_id')
    user_id = request.GET.get('user_id')
    chat = Chat.objects.get(id=chat_id)

    members = Member.objects.filter(chat=chat)
    name = ''
    if members[0].user.id != user_id:
        name = members[0].user.first_name
    else:
        name = members[1].user.first_name

    message_objects = Message.objects.filter(chat=chat)

    messages = []
    for msg_obj in message_objects:
        messages.append({'text': msg_obj.text,
                         'addedAt': msg_obj.added_at,
                         'senderId': msg_obj.user.id,
                         'messageId': msg_obj.id})

    response = {'interlocutor': name, 'messages': messages}

    return JsonResponse(response)


def get_chat_list(user_id):
    members = Member.objects.filter(user=user_id)
    chats = [member.chat for member in members]
    return chats


def send_message_post(request):
    if request.method == 'POST':
        

        
        # return JsonResponse({'user_id': user_id})

        response = {}
        try:
            form_data = json.loads(request.body)

            form = MessageForm(form_data)
            if form.is_valid():
                user_id = form_data['user_id']
                chat_id = form_data['chat_id']
                text = form_data['text']
            else:
                print('invalid')
            # user_id = request.POST.get('user_id')
            # chat_id = request.POST.get('chat_id')
            # text = request.POST.get('text')
            # body = request.POST.get('body')

            print(user_id, chat_id, text)

            response = send_message(user_id, chat_id, text)

        except Exception as e:
            response['result'] = traceback.format_exc()

        return JsonResponse(response)

    else:
        return JsonResponse({'answer': 'No!'})


def send_message(user_id, chat_id, text):
    response = {'result': ''}
    try:
        
        # added_at = request.GET.get('added_at')
        added_at = time.time()

        user = User.objects.get(id=int(user_id))
        chat = Chat.objects.get(id=int(chat_id))

        # member = Member.objects.filter(chat=chat)

        message = Message(text=text, added_at=added_at, user=user, chat=chat)
        message.save()

        chat.last_message = message
        chat.save()
    except Exception as e:
        response['result'] = traceback.format_exc()
    else:
        response['result'] = 'ok'
    
    return response


def read_message(request):
    response = {'result': ''}
    try:
        user_id = request.GET.get('user_id')
        chat_id = request.GET.get('chat_id')
        message_id = request.GET.get('message_id')

        message = Message.objects.get(id=message_id)

        member = Member.objects.get(user=user_id, chat=chat_id)
        member.last_read_message = message
        member.save()

    except Exception as e:
        response['result'] = traceback.format_exc()
    else:
        response['result'] = 'ok'

    return JsonResponse(response)


def get_member(request):
    response = {'result': ''}
    try:
        user_id = request.GET.get('user_id')

        members = Member.objects.filter(user=user_id)

        mems = []
        for member in members:
            mems.append({'chat_id': member.chat.id,
                         'last_msg': member.last_read_message.text if member.last_read_message else 'none'})
        response['members'] = mems

    except Exception as e:
        response['result'] = traceback.format_exc()
    else:
        response['result'] = 'ok'

    return JsonResponse(response)


def create_chat(is_group, user_id, second_user_id):
    chat = Chat(title='aa', is_group_chat=is_group)
    chat.save()
    first_member = Member(user=User.objects.get(
        pk=user_id), chat=chat)
    second_member = Member(user=User.objects.get(
        pk=second_user_id), chat=chat)

    first_member.save()
    second_member.save()


# заполнение БД


def create_user(name, last_name, username):
    u = User(first_name=name, last_name=last_name, username=username)
    u.save()
    return u.pk


def create_fake_info():
    user_ids = []
    user_ids.append(create_user('aelectron', 'kolobok', 'x'))
    user_ids.append(create_user('bproton', 'molotok', 'lisa'))
    user_ids.append(create_user('cneutron', 'gnom', 'koleso'))
    user_ids.append(create_user('dneuele', 'Verhovin', 'kozlina'))
    user_ids.append(create_user('etron', 'Ololoev', 'Eric'))

    create_chat(False, user_ids[0], user_ids[1])
    create_chat(False, user_ids[2], user_ids[3])
    create_chat(False, user_ids[0], user_ids[2])

    send_message(1, 1, 'ghbdtn')
    send_message(2, 1, 'привет')

    send_message(3, 2, 'ок')
    send_message(4, 2, 'чё')
    send_message(4, 2, 'ничё')

    send_message(1, 3, 'фыва')
    send_message(3, 3, 'прол')
