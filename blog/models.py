from django.db import models


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ['name']


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    topics = models.ManyToManyField('Topic', related_name='posts')

    class Meta:
        ordering = ['-creation_date']


class Comment(models.Model):
    deleted = "[deleted]"

    author = models.CharField(max_length=60, default=deleted)
    body = models.TextField(default=deleted)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    reply_parent = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-creation_date']
