from django.db import models

# Create your models here.

class Item(models.Model):

    def __str__(self):
        return self.item_name
    
    item_name = models.CharField(max_length=200)
    item_description = models.TextField(max_length=1000)
    item_price = models.IntegerField()