from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100, default="Anónimo")
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

