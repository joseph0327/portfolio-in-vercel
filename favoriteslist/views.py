from django.shortcuts import render, redirect, get_object_or_404
from items.models import Item
from . models import FavoritesList, FavoritesListItems

# Create your views here.
def _favorites_id(request):
    favorites = request.session.session_key
    if not favorites:
        favorites = request.session.create()
    return favorites


def add_to_favorites_list(request, favorites_id):
    item = Item.objects.get(id=favorites_id)
    try:
        favoritesList = FavoritesList.objects.get(favoriteslist_id=_favorites_id(request))
        
    except FavoritesList.DoesNotExist:
        favoritesList = FavoritesList.objects.create(
            favoriteslist_id = _favorites_id(request)
        )
        
    favoritesList.save()
    
    try:
        
        favoritesL_list_item = FavoritesListItems.objects.get(item = item, favoriteslist=favoritesList)
        favoritesL_list_item.quantity +=1
        favoritesL_list_item.save()
        
    except FavoritesListItems.DoesNotExist:
        favoritesL_list_item = FavoritesListItems.objects.create(
            item = item, 
            favoriteslist=favoritesList,
            quantity=1,
        )
        favoritesL_list_item.save()
        
    return redirect('favoriteslist')
        
    
    
    
def favoriteslist(request, cart_item = None):
    
    try: 
        favoritesList = FavoritesList.objects.get(favoriteslist_id = _favorites_id(request))
        favoritesList_item = FavoritesListItems.objects.filter(favoriteslist=favoritesList, is_active=True)
    except FavoritesList.DoesNotExist:
        favoritesList_item = []
 
    
    context = {
        'favoritesList_item':favoritesList_item
    }
        
    return render(request, 'items/favoriteslist.html',context )

def remove_favorite(request, favorites_id):
    
    favoriteslist = FavoritesList.objects.get(favoriteslist_id=_favorites_id(request))
    item = get_object_or_404(Item, id = favorites_id )
    favorites_item = FavoritesListItems.objects.get(item = item, favoriteslist=favoriteslist)
    favorites_item.delete()
    
    return redirect('favoriteslist')