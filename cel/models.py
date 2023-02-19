from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=119, unique=True)
    bio = models.TextField(blank=True)
    birth_date = models.TextField()
    location = models.TextField()

    def __str__(self):
        return self.name


class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='quotes')

    def __str__(self):
        return self.text
