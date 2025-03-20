from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class UserBookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserBookReview")
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="UserBookReview")
    rating = models.IntegerField(validators=[MinValueValidator(1, message="Rating must be at least 1."),
                                             MaxValueValidator(10, message="Rating cannot exceed 10.")])
    comment = models.TextField()
    date= models.DateTimeField(auto_now_add=True)