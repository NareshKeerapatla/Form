from django.db import models
class ModelClass(models.Model):
    name=models.CharField(max_length=20)
    id=models.IntegerField(primary_key=True)
    email=models.EmailField()
