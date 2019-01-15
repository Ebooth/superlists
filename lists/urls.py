from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name="home_page"),
    path('the-only-list-in-the-world/', view_list, name='view_list')
]