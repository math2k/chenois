from django.db import models


class NewsItem(models.Model):
    title = models.TextField()
    body = models.TextField()
    created = models.DateTimeField()
    published = models.BooleanField()
    author = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title


class Text(models.Model):
    key = models.CharField(max_length=255, primary_key=True)
    text = models.TextField()

    def __str__(self):
        return self.key