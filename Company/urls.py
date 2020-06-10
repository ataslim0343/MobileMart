from django.urls import path
from . import views

urlpatterns = [
    path('addcom/',views.addcom,name="addcom"),
]