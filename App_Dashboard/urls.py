from django.urls import path
from App_Dashboard import views

app_name = 'App_Dashboard'

urlpatterns = [
    path('', views.home, name="home"),
    path('country/', views.country, name="country"),
    path('add_country/', views.country_form, name="add_country"),
    path('edit_country/<int:country_id>', views.edit_country, name="edit_country"),
    path('delete_country/<int:country_id>', views.delete_country, name="delete_country"),
]