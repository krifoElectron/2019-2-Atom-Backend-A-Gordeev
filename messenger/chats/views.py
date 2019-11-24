from django.http import JsonResponse
from django.http import HttpResponseNotAllowed

from chats.models import Chat
from members.models import Member
from user_profile.models import User


def chat_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    # ueser_id = request.GET.get('uder_id')

    return JsonResponse({"chats": {"0": {"recipient": "b", "last_message": "sdf", "date": "2019-10-22T21:50:02.492Z", "isRead": True}}})


def chat_page(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    # chat_id = request.GET.get('chat_id')

    return JsonResponse({1: [{"sender": "a", "recipient": "b", "text": "sdf", "date": "2019-10-22T21:50:02.492Z", "isRead": True}, {"sender": "a", "recipient": "b", "text": "asdf", "date": "2019-10-22T21:50:02.869Z"}, {"sender": "a", "recipient": "b", "text": "asd", "date": "2019-10-22T21:50:03.113Z"}, {"sender": "a", "recipient": "b", "text": "asdf", "date": "2019-10-22T21:50:03.401Z"}, {"sender": "a", "recipient": "b", "text": "asdf", "date": "2019-10-22T21:50:03.603Z"}, {"sender": "a", "recipient": "b", "text": "sdf", "date": "2019-10-22T21:50:03.834Z"}, {"sender": "a", "recipient": "b", "text": "asdf", "date": "2019-10-22T21:50:04.084Z"}, {"sender": "a", "recipient": "b", "text": "asdf", "date": "2019-10-22T21:50:04.478Z"}, {"sender": "a", "recipient": "b", "text": "f", "date": "2019-10-22T21:50:10.294Z"}, {"sender": "a", "recipient": "b", "text": "asdffsadf", "date": "2019-10-28T12:14:16.806Z"}]})


# def next_id_group_chat():
#     length = len(Chat.objects.filter(is_group_chat=True))

#     if length:
#         result = Chat.objects.filter(is_group_chat=True)[
#             length - 1].id_group_chat + 1
#     else:
#         result = 1
#     return result


def create_chat(is_group, user_id, second_user_id):  # title
    chat = Chat(title='aa', is_group_chat=is_group,
                id_group_chat=0, last_message=0)
    chat.save()

    # id_group_chat = next_id_group_chat() if is_group else 0
    first_member = Member(user=User.objects.get(
        pk=user_id), chat=chat, new_messages=[])
    second_member = Member(user=User.objects.get(
        pk=second_user_id), chat=chat, new_messages=[])

    first_member.save()
    second_member.save()


def get_chat_list(user_id):
    members = Member.objects.filter(user=user_id)
    chats = [member.chat for member in members]
    return chats


# заполнение БД
def create_user(name):
    u = User(first_name=name, username=name)
    u.save()
    return u.pk


def create_fake_info():
    user_ids = []
    user_ids.append(create_user('a'))
    user_ids.append(create_user('b'))
    user_ids.append(create_user('c'))
    user_ids.append(create_user('d'))
    user_ids.append(create_user('e'))

    create_chat(False, user_ids[0], user_ids[1])
    create_chat(False, user_ids[2], user_ids[3])
    create_chat(False, user_ids[0], user_ids[2])
