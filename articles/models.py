from django.db import models

from django.contrib.auth import get_user_model


class Section(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=2000)


    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='articles')
    body = models.TextField(max_length=2000)
    created_on = models.DateTimeField(auto_now_add=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title