from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('login/', views.login, name="login")
    path("main/", views.main, name="main"),
    path('readmore/', views.readmore, name="readmore")
]
