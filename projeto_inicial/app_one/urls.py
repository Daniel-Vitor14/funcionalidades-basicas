from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teste/question/', csrf_exempt(views.teste.as_view()), name='question_teste')
]