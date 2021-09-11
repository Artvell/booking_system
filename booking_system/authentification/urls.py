"""файл с роутингом приложения"""
from django.urls import re_path
from authentification.views import ActivateUserView
app_name = "authentification"

urlpatterns = [
    re_path(r'auth/activateUser/(?P<user>\w+)/',ActivateUserView.as_view())
]
