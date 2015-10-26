from django.db import models

from core.models import TimeStampedModel


class Board(TimeStampedModel):
    name = models.CharField(max_length=256)
    slug = models.SlugField()
    info = models.TextField()

    def __str__(self):
        return self.name


class Thread(TimeStampedModel):
    title = models.CharField(max_length=256)
    link = models.URLField()
    body = models.TextField()
    board = models.ForeignKey(Board)

    def __str__(self):
        return self.title


class Comment(TimeStampedModel):
    body = models.TextField()
    thread = models.ForeignKey(Thread)
    parent = models.ForeignKey(
        'self',
        related_name='replies',
        blank=True,
        null=True
    )

    def __str__(self):
        return "Thread: %s - Comment ID: %d" % (self.thread.title, self.id)