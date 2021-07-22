from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Item(models.Model):

    def __str__(self):
        return self.item_name

    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1) 
    item_name = models.CharField(max_length = 200)
    item_desc = models.CharField(max_length = 200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length = 500,default="https://th.bing.com/th/id/R0805d07b70205857a5d6123…WX66c3zxNDjukANZCb9EhIWD0PJP4%3d&risl=&pid=ImgRaw")

    
    def get_absolute_url(self):
        return reverse("food:detail",kwargs={"pk":self.pk})