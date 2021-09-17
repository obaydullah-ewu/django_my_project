from django.urls import path
from App_Dashboard import views

app_name = 'App_Dashboard'

urlpatterns = [
    path('', views.home, name="home"),
    path('country/', views.country, name="country"),
    path('add_country/', views.country_form, name="add_country"),
    path('edit_country/<int:country_id>/', views.edit_country, name="edit_country"),
    path('delete_country/<int:country_id>/', views.delete_country, name="delete_country"),
    path('taxi_company/', views.taxi_company, name='taxi_company'),
    path('add_taxi_company/', views.add_taxi_company, name='add_taxi_company'),
    path('edit_taxi_company/<int:taxi_id>/', views.edit_taxi_company, name='edit_taxi_company'),
    path('delete_taxi_company/<int:taxi_id>/', views.delete_taxi_company, name='delete_taxi_company'),
]