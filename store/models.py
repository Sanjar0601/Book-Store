from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='cover_pics', null=True, blank=True, default='cover_pics/default_yl9hFW5.jpg')
    author = models.CharField(max_length=50)
    summary = models.TextField()
    price = models.IntegerField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})
