from __future__ import unicode_literals

from django.db import models


class Topic(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.TextField()
    topics = models.ManyToManyField(Topic)

    def __str__(self):
        return self.name
