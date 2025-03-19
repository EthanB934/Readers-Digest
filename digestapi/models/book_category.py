from django.db import models

class BookCategory(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="BookCategory")
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="BookCategory")
    created_at = models.DateTimeField(auto_now_add=True)