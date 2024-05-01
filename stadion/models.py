from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=127)
    position = models.CharField(max_length=2)
    game = models.CharField(max_length=2)
    score = models.CharField(max_length=3)
