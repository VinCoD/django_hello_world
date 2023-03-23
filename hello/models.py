from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return f"{self.body[:50]}..."


