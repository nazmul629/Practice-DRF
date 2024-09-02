from django.db import models

# Create your models here.
class Movidata(models.Model):
    name = models.CharField(max_length=20)
    duration = models.FloatField()
    rating = models.FloatField()
    image = models.ImageField(default='nothing.jpg', upload_to='media/movies')


    def __str__(self):
        return  self.name