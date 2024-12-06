from django.urls import path
from . import views

urlpatterns = [
    path('add_to_favorites_list/<int:favorites_id>/', views.add_to_favorites_list, name="add_to_favorites_list"),
    path('remove_favorite/<int:favorites_id>/', views.remove_favorite, name="remove_favorite"),
    path('', views.favoriteslist, name="favoriteslist"),
    

]

