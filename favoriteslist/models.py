from django.db import models
from items.models import Item
from accounts.models import Account

# Create your models here.
class FavoritesList(models.Model):
    favoriteslist_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.favoriteslist_id
    

class FavoritesListItems(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    #variations = models.ManyToManyField(Variation, blank=True)
    favoriteslist    = models.ForeignKey(FavoritesList, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True) 
    
    
    def __str__(self):
        return f"{self.item.item_name} - Quantity: {self.quantity}"