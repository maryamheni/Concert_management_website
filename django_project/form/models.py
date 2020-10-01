from django.db import models

# Create your models here.
class Form (models.Model):
    first_name =models.CharField(max_length=20)
    middle_name =models.CharField(max_length=20,blank=True)
    last_name =models.CharField(max_length=20)
    phone =models.IntegerField()
    concert_name=models.CharField(max_length=20)
    concert_description=models.TextField()
    gender =models.CharField(max_length=20 ,choices=(
    ('male',"Male"),
    ("female","Female"),
    ))
    country=models.CharField(max_length=20 ,choices=(
    ('tunisia',"Tunisia"),
    ("usa","Usa"),
    ("algeria","Algeria"),
    ("afghanistan","Afghanistan"),
    ("albania","Albania"),
    ("namibia","Namibia"),
    ("canada","Canada"),
    ("egypt","Egypt"),
    ("france","France"),
    ("greece","Greece"),
    ("india","India"),
    ("japan","Japan"),
    ("kenya","Kenya")

    ))
def ___str___(self):
     return self.first_name