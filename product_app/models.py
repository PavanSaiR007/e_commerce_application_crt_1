from django.db import models

# Create your models here.
class ProductModel(models.Model):
    id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=100)
    p_type = models.CharField(max_length=100)
    p_price = models.FloatField()
    p_quantity = models.IntegerField()

    def __str__(self):
        return self.p_name


class Cart(models.Model):
     cart_id=models.AutoField(primary_key=True)
     product_id=models.IntegerField()
     p_price=models.FloatField()

     def __str__(self):
         return str(self.cart_id)