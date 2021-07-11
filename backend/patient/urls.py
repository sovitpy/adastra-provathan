from django.urls import path
from . import views


urlpatterns = [
    path("update",  views.addHeartBeat),
    path("info" , views.getPatient),
    path("get" , views.getHeartBeat),
    path("bp/<str:bp>", views.changeBP),
    path("heart-rate/<str:heartBeat>", views.changeHeartBeat)
]
