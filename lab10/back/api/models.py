from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


# >>> Product.objects.values('id', 'name')
# <QuerySet [{'id': 21, 'name': 'iPhone 15 Pro'}, {'id': 22, 'name': 'Samsung Galaxy S23'}, {'id': 23, 'name': 'Xiaomi 13'}, {'id': 24, 'name': 'iPhone 14'}, {'id': 25, 'name': 'Samsung Galaxy A54'}, {'id': 26, 'name': 'MacBook Air M2'}, {'id': 27, 'name': 'HP Pavilion 15'}, {'id': 28, 'name': 'Lenovo ThinkPad X1'}, {'id': 29, 'name': 'Dell XPS 13'}, {'id': 30, 'name': 'iPad Pro 11'}, {'id': 31, 'name': 'Samsung Galaxy Tab S8'}, {'id': 32, 'name': 'Amazon Kindle Paperwhite'}, {'id': 33, 'name': 'Sony WH‑1000XM5'}, {'id': 34, 'name': 'Bose QuietComfort 45'}, {'id': 35, 'name': 'Logitech MX Master 3'}, {'id': 36, 'name': 'Razer BlackWidow V3'}, {'id': 37, 'name': 'iPad Pro 11'}, {'id': 38, 'name': 'Samsung Galaxy Tab S8'}, {'id': 39, 'name': 'Amazon Kindle Paperwhite'}, {'id': 40, 'name': 'Samsung Galaxy Tab S10+'}]>
# >>> Category.objects.values('id', 'name')
# <QuerySet [{'id': 29, 'name': 'Smartphones'}, {'id': 30, 'name': 'Laptops'}, {'id': 31, 'name': 'Headphones'}, {'id': 32, 'name': 'Tablets'}]>