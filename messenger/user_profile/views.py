from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.db.models import Q

from user_profile.models import User


def profile(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])

    user_id = request.GET.get('user_id')
    if user_id is None:
        return JsonResponse({'result': 'user invalid'}, status=400)

    try:
        required_user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({'result': 'user not found'}, status=404)

    responce_object = required_user.to_dict()

    return JsonResponse(responce_object)


def search_user(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])

    user_name = request.GET.get('user_name')

    return get_user_by_any(user_name)


def contacts(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])

    user_id = request.GET.get('user_id')

    return JsonResponse({'id': user_id, 'contacts': [2, 5, 7]})


def get_user_by_any(request):
    word = request.GET.get('word')

    required_users = User.objects.filter(Q(first_name__contains=word) | Q(
        last_name__contains=word) | Q(username__contains=word))

    return JsonResponse({'users': [user.to_dict() for user in required_users]})
