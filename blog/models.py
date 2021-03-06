from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 300)
    address = models.TextField()
    phone = models.CharField(max_length = 12)
    website = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(
        'User',
        on_delete = models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title
