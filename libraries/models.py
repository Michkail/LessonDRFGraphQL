import uuid
from django.db import models


class Book(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    title = models.TextField()
    author = models.TextField()
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "book"
        ordering = ["created_at"]
