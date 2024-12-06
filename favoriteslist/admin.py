from django.contrib import admin
from .models import FavoritesList, FavoritesListItems

class FavoritesListAdmin(admin.ModelAdmin):
    list_display = ('favoriteslist_id', 'date_added')

class FavoritesListItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'favoriteslist', 'user','quantity', 'is_active')


# Register your models here.
admin.site.register(FavoritesList, FavoritesListAdmin)
admin.site.register(FavoritesListItems , FavoritesListItemAdmin)