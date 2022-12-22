from django.db import models
from django.conf import settings
from django.urls import reverse

class Visual(models.Model):
    plot_type = models.CharField(max_length=20)
    plot_image = models.FileField()

    def __str__(self):
        return self.plot_type


class DataLoad(models.Model):
    data = models.FileField()
    userid = models.CharField(max_length=20)
    
    # def get_absolute_url(self):
    #     return reverse('data_loading')







