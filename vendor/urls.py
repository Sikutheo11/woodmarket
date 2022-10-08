from django.urls import path, include
from . import views
from accounts import views as AccountViews


urlpatterns = [
    path('', AccountViews.vendorDashboard, name='vendor'),
    path('profile/', views.vprofile, name='vprofile'),
    path('myProduct/', views.myProduct, name='myProduct'),
    path('myProduct/category/<int:pk>/', views.productitems_by_category, name='productitems_by_category'),

    # Category CRUD
    path('myProduct/category/add/', views.add_category, name='add_category'),
    path('myProduct/category/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('myProduct/category/delete/<int:pk>/', views.delete_category, name='delete_category'),

    # # FoodItem CRUD
    # path('menu-builder/food/add/', views.add_food, name='add_food'),
    # path('menu-builder/food/edit/<int:pk>/', views.edit_food, name='edit_food'),
    # path('menu-builder/food/delete/<int:pk>/', views.delete_food, name='delete_food'),

    # # Opening Hour CRUD
    # path('opening-hours/', views.opening_hours, name='opening_hours'),
    # path('opening-hours/add/', views.add_opening_hours, name='add_opening_hours'),
    # path('opening-hours/remove/<int:pk>/', views.remove_opening_hours, name='remove_opening_hours'),

]