from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.db.models import Q

from user_profile.models import User


def profile(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])

    user_id = request.GET.get('user_id')

    required_user = User.objects.get(id=user_id)

    responce_object = {}

    responce_object['id'] = required_user.id
    responce_object['email'] = required_user.email
    responce_object['about'] = required_user.about
    responce_object['birthday'] = required_user.birthday
    responce_object['date_joined'] = required_user.date_joined
    responce_object['first_name'] = required_user.first_name
    responce_object['is_active'] = required_user.is_active
    responce_object['last_login'] = required_user.last_login
    responce_object['last_name'] = required_user.last_name
    responce_object['location'] = required_user.location
    responce_object['username'] = required_user.username
    responce_object['avatar'] = required_user.avatar

    return JsonResponse(responce_object)


def search_user(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])

    user_name = request.GET.get('user_name')

    return get_user_by_any(user_name)


def contacts(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    return JsonResponse({'id': 1, 'contacts': [2, 5, 7]})


def get_user_by_any(request):
    word = request.GET.get('word')

    required_users = User.objects.filter(Q(first_name__contains=word) | Q(
        last_name__contains=word) | Q(username__contains=word))
    responce_object = {'users': []}

    i = 0
    for user in required_users:
        responce_object['users'].append({})
        responce_object['users'][i]['id'] = user.id
        responce_object['users'][i]['email'] = user.email
        responce_object['users'][i]['about'] = user.about
        responce_object['users'][i]['birthday'] = user.birthday
        responce_object['users'][i]['date_joined'] = user.date_joined
        responce_object['users'][i]['first_name'] = user.first_name
        responce_object['users'][i]['is_active'] = user.is_active
        responce_object['users'][i]['last_login'] = user.last_login
        responce_object['users'][i]['last_name'] = user.last_name
        responce_object['users'][i]['location'] = user.location
        responce_object['users'][i]['username'] = user.username
        responce_object['users'][i]['avatar'] = user.avatar
        i += 1

    return JsonResponse(responce_object)
