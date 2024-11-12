from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('manage-brands', views.manage_brands, name='manage_brands'),
	path('update-brands/<str:osm_id>', views.update_brands, name='update_brands'),
	path('view-brands/<str:osm_id>', views.view_brands, name='view_brands'),
	path('create-brands', views.create_brands, name='create_brands'),
	path('get_city_list', views.get_city_list, name='get_city_list'),
    path('form', views.dynamic_form, name='dynamic_form'),
    path('get_subcategories/', views.get_subcategories, name='get_subcategories'),
]
