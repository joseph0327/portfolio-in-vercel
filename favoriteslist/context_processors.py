from .models import FavoritesList,FavoritesListItems
from .views import _favorites_id



def counter(request):
    favorites_count = 0
    if 'admin'in request.path:
        return {}
    else:
        try:
            
            favorites = FavoritesList.objects.filter(favoriteslist_id=_favorites_id(request))
            favorites_items = FavoritesListItems.objects.all().filter(favoriteslist=favorites[:1])
                
            
            for favorites_items in favorites_items:
                favorites_count += favorites_items.quantity
        
        except FavoritesList.DoesNotExist:
            favorites_count = 0
    
    return dict(favorites_count=favorites_count)