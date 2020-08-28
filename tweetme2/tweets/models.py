from django.db import models

# Create your models here.
class Tweet(models.Model):
    # SQL
    # id = models.AutoField(primaryField_key=True)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='image/', blank=True, null=True)

