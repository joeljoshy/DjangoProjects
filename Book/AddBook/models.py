from django.db import models

# Create your models here.
class AddBooks(models.Model):
    book_name = models.CharField(max_length=70,unique=True)
    author = models.CharField(max_length=15)
    category = models.CharField(max_length=20)
    price = models.FloatField(default=50)
    copies = models.IntegerField()


    def __str__(self):
        return self.book_name