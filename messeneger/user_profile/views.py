from django.http import JsonResponse
from django.http import HttpResponseNotAllowed

# Create your views here.


def profile(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])

    # ueser_id = request.GET.get('uder_id')
    # user = User.objects.get(id=uder_id)
    return JsonResponse({'id': 1, 'name': 'Bender', 'sername': 'Rodriguez', 'birthday': '2993 year', "contacts": [2, 5, 7]})


def contacts(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])

    # ueser_id = request.GET.get('uder_id')
    # user = User.objects.get(id=uder_id)
    return JsonResponse({'id': 1, 'contacts': [2, 5, 7]})
