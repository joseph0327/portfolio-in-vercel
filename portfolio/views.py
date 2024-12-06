from django.shortcuts import render
from category.models import Category
from items.models import Item, Certificates

from django.db.models import OuterRef, Exists
from favoriteslist.models import FavoritesListItems
from favoriteslist.views import _favorites_id



def home(request):
    categoryitems = Category.objects.all()
    latestitems = Item.objects.all().order_by('created_date')[:12]
    certlist = Certificates.objects.all().order_by('-created_date')[:8]
    
    #Get the current session's favorites list
    favorites_list_id = _favorites_id(request)

    # Annotate each item with "is_in_favorites"
    latestitems = latestitems.annotate(
        is_in_favorites=Exists(
            FavoritesListItems.objects.filter(
                favoriteslist__favoriteslist_id=favorites_list_id,
                item=OuterRef('id'),
            )
        )
    )
    
    context ={
        'categoryitems' : categoryitems,
        'latestitems':latestitems,
        'certlist':certlist,
    }
    return render(request, 'home.html',context)





