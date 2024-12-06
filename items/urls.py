from django.urls import path
from . import views

urlpatterns = [
    path('category/<slug:category_slug>/', views.items, name="item_by_category"),
    path('category/<slug:category_slug>/<slug:item_slug>/', views.item_detail, name="item_detail"),
    path('category/<slug:category_slug>/certification/<slug:item_slug>/', views.cert_detail, name="cert_detail"),
    path('search/', views.search, name='search'),
    path('', views.items, name="items"),
    

]

