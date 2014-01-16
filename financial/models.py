from django.db import models

class Prices(models.Model):
    date = models.CharField(max_length=30)
    total_stock = models.CharField(max_length=50)
    total_price = models.CharField(max_length=60)
    p_begin = models.CharField(max_length=60)
    p_max = models.CharField(max_length=60)
    p_min = models.CharField(max_length=60)
    p_end = models.CharField(max_length=60)
    p_diff = models.CharField(max_length=60)
    

'''
class Income(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
'''
