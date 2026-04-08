from django.db import models
from django.contrib.auth.models import User
from .book import Book

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(max_length=5)
    comment = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)