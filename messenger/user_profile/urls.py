from django.urls import path

from user_profile.views import profile, contacts

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('contacts/', contacts, name='contacts'),
]
