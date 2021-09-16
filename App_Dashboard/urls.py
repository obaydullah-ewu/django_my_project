from django.urls import path
from App_Dashboard import views

app_name = 'App_Dashboard'

urlpatterns = [
    path('', views.home, name="home"),
    path('country/', views.country, name="country"),
    path('add_country/', views.country_form, name="add_country")
]