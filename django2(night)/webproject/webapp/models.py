from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    bookid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title

class Author(models.Model):
    authorid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=15)
    emailid = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name
    
class Publisher(models.Model):
    publisherid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name