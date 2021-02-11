#  Copyright (c) 2020-2021 Ojas Anand.
#
#  This file is part of GNU package. GNU package is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version. GNU package is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
#  PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of
#  the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.

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
