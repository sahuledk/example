from django.db import models


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, default='', blank=True)
    body = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['created']


