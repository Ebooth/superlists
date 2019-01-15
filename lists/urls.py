from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', home_page, name="home_page"),
    path('new', new_list, name="new_list"),
    re_path('(?P<list_id>\d+)/$', view_list, name='view_list'),
    path('<list_id>/add_item', add_item, name="add_item"),
]