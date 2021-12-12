from django.db import models

# Create your models here.

'''
class Meta:
    db_table = ''
'''

class Menu(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'menu'

class Categories(models.Model):
    name = models.CharField(max_length=100)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    korean_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    discription = models.CharField(max_length=300)

    class Meta:
        db_table = 'product'

class Allergens(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'allergens'

class Product_Allergens(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    allergens = models.ForeignKey('Allergens', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_allergens'

class Image(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=2000)

    class Meta:
        db_table = 'image'

class Nutritionfacts(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    size = models.ForeignKey('Sizes', on_delete=models.CASCADE, null=True)
    calories = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    saturated_fat = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    protein = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    sodium = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    sugers = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    caffeine = models.DecimalField(max_digits=5, decimal_places=1, null=True)

    class Meta:    
        db_table = 'nutritionfacts'

class Sizes(models.Model):
    name = models.CharField(max_length=100)
    size_ml = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    size_fluid_ounce = models.DecimalField(max_digits=5, decimal_places=1, null=True)

    class Meta:    
        db_table = 'sizes'

