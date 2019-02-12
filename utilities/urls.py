from django.urls import path
# home 폴더 내에 있는 views.py를 불러온다.
from . import views


urlpatterns = [
    path('',views.index), #utilities/
]