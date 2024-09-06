from django.urls import path

from . import views

urlpatterns = [
    path('db/users', views.users, name='users'),
    path('db/users/<int:iduser>', views.user, name='users'),
]