from App_Dashboard import views
from django.urls import path

app_name = 'App_Dashboard'

urlpatterns = [
    path('', views.home, name="home")
]