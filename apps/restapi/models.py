from django.db import models

# Create your models here.


class Profile(models.Model):
    name=models.CharField(max_length = 180)
    email=models.EmailField(max_length=100)
    number=models.IntegerField()
    city=models.CharField(max_length = 180)

    def __str__(self):
        return self.name

