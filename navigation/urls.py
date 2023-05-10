from django.urls import path

from .views import MakeTokenView
urlpatterns = [
    path("generate/", MakeTokenView.as_view(), name="index"),
]   