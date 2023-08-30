from django.urls import path
from .views import home, add, succes, logn, edit

urlpatterns = [
    path('gestion', home, name="home"),
    path('', add, name="ajouter"),
    path('edit/<str:id>', edit, name="edit"),
    path('succes', succes, name="succes"),
    path('login', logn, name="login"),
]