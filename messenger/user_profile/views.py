from django.http import JsonResponse
from django.http import HttpResponseNotAllowed

from user_profile.models import User


def profile(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    return JsonResponse({'id': 1, 'name': 'Bender', 'sername': 'Rodriguez', 'birthday': '2993 year', "contacts": [2, 5, 7]})


def contacts(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    return JsonResponse({'id': 1, 'contacts': [2, 5, 7]})


def get_user_by_id(user_id):
    try:
        return User.objects.get(id=user_id)  # Норм ли так try использовать?
    except Exception:
        return -1


def get_user_by_name(name):
    return User.objects.filter(first_name=name)  # contain
