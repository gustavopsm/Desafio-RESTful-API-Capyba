from django.db import models

class Item(models.Model):
    name = models.CharField(default='', max_length=50)
    album = models.CharField(default='', max_length=50)
    explicit = models.BooleanField(default=False)
    duration = models.IntegerField(default=0, blank=True)

    def __str__(self) -> str:
        return self.name
