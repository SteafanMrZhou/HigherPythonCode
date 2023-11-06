from django.db import models

class HpUser(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    sex = models.CharField(max_length=20, default="男")