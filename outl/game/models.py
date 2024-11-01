# bot/models.py
from django.db import models

class UserData(models.Model):
    name = models.CharField(max_length=100)
    interests = models.TextField()
    preferences = models.TextField()
    # Add more fields as needed
