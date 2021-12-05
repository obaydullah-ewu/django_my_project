from django.urls import path
from App_Dashboard import views

app_name = 'App_Dashboard'

urlpatterns = [
    path('', views.home, name="home"),
    path('country/', views.country, name="country"),
    path('add_country/', views.country_form, name="add_country"),
    path('edit_country/<int:country_id>/', views.edit_country, name="edit_country"),
    path('delete_country/<int:country_id>/', views.delete_country, name="delete_country"),

    path('designer_info/', views.designer_info, name='designer_info'),
    path('add_designer/', views.add_designer, name='add_designer'),
    path('view_designer/<int:designer_id>/', views.view_designer, name='view_designer'),
    path('edit_designer/<int:designer_id>/', views.edit_designer, name='edit_designer'),
    path('delete_designer/<int:designer_id>/', views.delete_designer, name='delete_designer'),

    path('post/', views.post, name='post')
]