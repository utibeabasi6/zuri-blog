from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
    name = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    email = models.EmailField()

    def __str__(self):
        if len(self.message) > 50:
            return self.message[:50] + '...'
        return self.message[:50] 