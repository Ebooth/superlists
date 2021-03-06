from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('new', new_list, name="new_list"),
    re_path('(?P<list_id>\d+)/$', view_list, name='view_list'),
    path('users/<str:email>/', my_lists, name='my_lists')
]