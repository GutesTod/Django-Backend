from django.db import models

class User(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    hashed_password = models.CharField(max_length=255)
    