from django.db import models
from django.contrib.auth.models import User
from .book import Book
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)