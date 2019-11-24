from django.urls import path

from index_html.views import index

urlpatterns = [
    path('', index, name='index'),
]
