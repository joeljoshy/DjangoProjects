from django.db import models

# Create your models here.


class AddEmployee(models.Model):

    emp_name = models.CharField(max_length=70)
    desig = models.CharField(max_length=30)
    salary = models.FloatField(default=50)
    exp = models.IntegerField()
    email = models.EmailField(max_length=250, unique=True)

    def __str__(self):
        return self.emp_name