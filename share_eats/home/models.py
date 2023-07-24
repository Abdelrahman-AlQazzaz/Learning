from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    authorEmail = models.EmailField(blank=True)
    ip = models.GenericIPAddressField(protocol='both', blank=True, null = True)
    jsons = models.JSONField(blank=True, null=True)
    aproval = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.title
    