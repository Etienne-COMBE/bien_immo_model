from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name = "upload_csv"),
    path('stats/login', views.login, name = "upload_csv"),
    path('save_data/', views.save_data, name = "save_data")
]