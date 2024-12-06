from django.urls import path
from . import views

urlpatterns = [
    path('', views.certlist, name="certlist"),
    path('<slug:category_slug>/', views.certlist, name="certlist_list"),
]
