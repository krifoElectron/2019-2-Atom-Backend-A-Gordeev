from django.urls import path

from user_profile.views import profile, contacts, search_user, get_user_by_any

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('contacts/', contacts, name='contacts'),
    path('search_user', search_user, name='search_user'),
    path('get_user_by_any', get_user_by_any, name='get_user_by_any')
]
