from django.urls import path
from .views import AnimeView

app_name = "anime"

urlpatterns = [
    path("", AnimeView.as_view(), name="index")
]

