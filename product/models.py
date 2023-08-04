from django.db import models

# Create your models here.


class Categorys(models.Model):
    name = models.CharField(max_length=50,db_index=True)
    slug = models.SlugField(max_length=50,db_index=True,unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Categorys,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    desc = models.TextField() #description
    image=models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=12,decimal_places=2)
    date_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name