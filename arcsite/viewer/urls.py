from django.urls import path
from .views import viewer

app_name = "viewer"

urlpatterns = [
    path('', viewer, name="viewer"),
]
