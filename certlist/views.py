from django.shortcuts import render, get_object_or_404
from items.models import Certificates
from category.models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def certlist(request, category_slug=None):
    # Initialize certlist and categories
    certlist = None
    categories = None

    # Filter by category if category_slug is provided
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        certlist = Certificates.objects.filter(
            category=categories, is_available=True
        ).order_by('-created_date')
        paginator = Paginator(certlist, 12)
        page = request.GET.get('page')
        paged_certlist = paginator.get_page(page)
    else:
        # Show all certificates if no category is specified
        certlist = Certificates.objects.filter(is_available=True).order_by('-created_date')
        paginator = Paginator(certlist, 12)
        page = request.GET.get('page')
        paged_certlist = paginator.get_page(page)

    context = {
        'certlist': paged_certlist,
        'categories': categories,  
       
    }
    return render(request, 'items/certfulllist.html', context)
