from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Certificates, ItemGallery,ItemGalleryCerts
from favoriteslist.models import FavoritesListItems
from category.models import Category
from favoriteslist.views import _favorites_id
from django.db.models import OuterRef, Exists
from django.db.models import Q

from django.http import HttpResponse



def items(request, category_slug=None):
    excel_items = None
    data_items = None
    web_items = None
    categories = None
    data_count = None
    web_count = None
    excel_count = None
    excel_count = 0
    data_count = 0
    web_count = 0
   
    
    
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        
        # Filter items based on the category
        if category_slug.lower() == 'excel-vba-and-macro':
            excel_items = Item.objects.filter(category=categories, is_available=True)
            excel_count = excel_items.count()
        elif category_slug.lower() == 'data-analysis':
            data_items = Item.objects.filter(category=categories, is_available=True)
            data_count = data_items.count()
        elif category_slug.lower() == 'web-development': 
            web_items = Item.objects.filter(category=categories, is_available=True)
            web_count = web_items.count()
        
        
       
        # paginator = Paginator(items, 1)
        # page = request.GET.get('page')
        # page_products = paginator.get_page(page)
    else:
        data_items = Item.objects.filter(category__category_name="Data Analysis", is_available=True)
        web_items = Item.objects.filter(category__category_name="Web Development and Programming", is_available=True)
        excel_items = Item.objects.filter(category__category_name="Excel VBA and Macro", is_available=True)
        data_count = data_items.count()
        web_count = web_items.count()
        excel_count = excel_items.count()
    #     paginator = Paginator(products, 3)
    #     page = request.GET.get('page')
    #     page_products = paginator.get_page(page)
        
    
   
    context = {
        'data_items':data_items,
        'web_items':web_items,
        'excel_items': excel_items,
        'data_count':data_count,
        'web_count':web_count,
        'excel_count':excel_count
        
    }
    return render(request, 'items/allcategory.html',context)


def item_detail(request, category_slug, item_slug):
    try: 
        item_category = get_object_or_404(Item, category__slug=category_slug, slug=item_slug)
        in_favoritelist = FavoritesListItems.objects.filter(favoriteslist__favoriteslist_id = _favorites_id(request),item=item_category).exists()
      
    
    except Exception as e:
        raise e

    #get the item images
    item_gallery = ItemGallery.objects.filter(item_id = item_category)
    
    context = {
        'item_category':item_category,
        'in_favoritelist':in_favoritelist,
        'item_gallery': item_gallery
    }
    return render(request, 'items/itemdetail.html',context)



def cert_detail(request, category_slug, item_slug):
    
    
    try: 
        cert_item = Certificates.objects.get(category__slug = category_slug, slug = item_slug )
        
    except Exception as e:
        raise e
    
     #get the item images
    cert_gallery = ItemGalleryCerts.objects.filter(cert_id = cert_item)
    
    context = {
        'cert_item':cert_item, 
        'cert_gallery': cert_gallery,
    }
    return render(request, 'items/itemdetailcert.html',context)


# def search(request):
   
#     if 'keyword' in request.GET:
#         keyword = request.GET['keyword']
    
#         if keyword:
#                 item = Item.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(item_name__icontains=keyword))
#         else:
#                 return redirect('items')
#     context = {
#         'data_items':item,
#     }
#     return render(request, 'items/allcategory.html',context)


def search(request):
    keyword = request.GET.get('keyword', '')
    items = []
    if keyword:
        items = Item.objects.filter(
            Q(item_name__icontains=keyword) | Q(description__icontains=keyword),
            is_available=True
        )
    
    context = {
        'data_items': items,
        'items': items,
        'keyword': keyword,
    }
    return render(request, 'items/allcategory.html', context)
