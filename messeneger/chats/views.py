from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
# Create your views here.


def chat_list(request):
    if request.method != "GET":
        print('asdfasdf')
        return HttpResponseNotAllowed(["GET"])

    # ueser_id = request.GET.get('uder_id')
    # user = User.objects.get(id=uder_id)
    return JsonResponse({"chats": {"0": {"recipient": "b", "last_message": "sdf", "date": "2019-10-22T21:50:02.492Z", "isRead": True}}})


def chat_page(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])

    # chat_id = request.GET.get('chat_id')
    # chat = Chat.objects.get(id=chat_id)
    return JsonResponse({1: [{"sender": "a", "recipient": "b", "text": "sdf", "date": "2019-10-22T21:50:02.492Z", "isRead": True}, {"sender": "a", "recipient": "b", "text": "asdf", "date": "2019-10-22T21:50:02.869Z"}, {"sender": "a", "recipient": "b", "text": "asd", "date": "2019-10-22T21:50:03.113Z"}, {"sender": "a", "recipient": "b", "text": "asdf", "date": "2019-10-22T21:50:03.401Z"}, {"sender": "a", "recipient": "b", "text": "asdf", "date": "2019-10-22T21:50:03.603Z"}, {"sender": "a", "recipient": "b", "text": "sdf", "date": "2019-10-22T21:50:03.834Z"}, {"sender": "a", "recipient": "b", "text": "asdf", "date": "2019-10-22T21:50:04.084Z"}, {"sender": "a", "recipient": "b", "text": "asdf", "date": "2019-10-22T21:50:04.478Z"}, {"sender": "a", "recipient": "b", "text": "f", "date": "2019-10-22T21:50:10.294Z"}, {"sender": "a", "recipient": "b", "text": "asdffsadf", "date": "2019-10-28T12:14:16.806Z"}]})
