from django.http import JsonResponse
from django.http import HttpResponseNotAllowed

from chats.models import Chat
from members.models import Member
from user_profile.models import User


def chat_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    user_id = request.GET.get('user_id')

    required_user = User.objects.get(id=user_id)

    required_members = Member.objects.filter(user=user_id)

    chats = []

    for member in required_members:
        chat = member.chat
        chats.append({'title': chat.title,
                      'is_group_chat': chat.is_group_chat,
                      'last_message': chat.is_group_chat})

    return JsonResponse({'chats': chats})

    # return JsonResponse({"chats": {"0": {"recipient": "b", "last_message": "sdf", "date": "2019-10-22T21:50:02.492Z", "isRead": True}}})


def chat_page(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    # chat_id = request.GET.get('chat_id')

    return JsonResponse({1: [{"sender": "a", "recipient": "b", "text": "sdf", "date": "2019-10-22T21:50:02.492Z", "isRead": True}, {"sender": "a", "recipient": "b", "text": "asdf", "date": "2019-10-22T21:50:02.869Z"}, {"sender": "a", "recipient": "b", "text": "asd", "date": "2019-10-22T21:50:03.113Z"}, {"sender": "a", "recipient": "b", "text": "asdf", "date": "2019-10-22T21:50:03.401Z"}, {"sender": "a", "recipient": "b", "text": "asdf", "date": "2019-10-22T21:50:03.603Z"}, {"sender": "a", "recipient": "b", "text": "sdf", "date": "2019-10-22T21:50:03.834Z"}, {"sender": "a", "recipient": "b", "text": "asdf", "date": "2019-10-22T21:50:04.084Z"}, {"sender": "a", "recipient": "b", "text": "asdf", "date": "2019-10-22T21:50:04.478Z"}, {"sender": "a", "recipient": "b", "text": "f", "date": "2019-10-22T21:50:10.294Z"}, {"sender": "a", "recipient": "b", "text": "asdffsadf", "date": "2019-10-28T12:14:16.806Z"}]})


def create_chat(is_group, user_id, second_user_id):
    chat = Chat(title='aa', is_group_chat=is_group)
    chat.save()
    first_member = Member(user=User.objects.get(
        pk=user_id), chat=chat)
    second_member = Member(user=User.objects.get(
        pk=second_user_id), chat=chat)

    first_member.save()
    second_member.save()


def get_chat_list(user_id):
    members = Member.objects.filter(user=user_id)
    chats = [member.chat for member in members]
    return chats


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
