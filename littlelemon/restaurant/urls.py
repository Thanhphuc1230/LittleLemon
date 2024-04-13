#define URL route for index() view
from django.urls import include,path
from . import views
from .views import UserList
urlpatterns = [
    path('', views.index, name='index'),
    path('api/', UserList.as_view(), name='user-list'),
]
