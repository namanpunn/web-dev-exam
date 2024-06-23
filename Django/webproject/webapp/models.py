from django.db import models
import uuid
# Create your models here.

class Book(models.Model):
    bookid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    title = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Author(models.Model):
    authorid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    name = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    Publisherid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    name = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name
