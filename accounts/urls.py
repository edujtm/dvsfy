from django.urls import path, re_path

from .views import AppView, logout_view

urlpatterns = [
    path('logout', logout_view),
    re_path(r'.*', AppView.as_view()),
]
