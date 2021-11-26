from django.urls import path
from . import views

app_name = 'meeting'
urlpatterns = [
    path('topics/<int:pk>/video/', views.videologin, name='video'),
]