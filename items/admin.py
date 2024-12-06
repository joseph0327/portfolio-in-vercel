from django.contrib import admin
from .models import Item, Certificates, ItemGallery,ItemGalleryCerts
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class ItemGalleryInline(admin.TabularInline):
    model = ItemGallery
    extra=1
    
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('item_name',)}
    inlines = [ItemGalleryInline]
   
    
@admin_thumbnails.thumbnail('image')
class CertGalleryInline(admin.TabularInline):
    model = ItemGalleryCerts
    extra=1
    
class CerificatesAdmin(admin.ModelAdmin):
    list_display = ('cert_name', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('cert_name',)}
    inlines = [CertGalleryInline]


admin.site.register(Item, ItemAdmin)
admin.site.register(Certificates, CerificatesAdmin)
admin.site.register(ItemGallery)
