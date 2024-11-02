from django.db import models
# Create your models here.

class Comment(models.Model):
    msg=models.CharField(max_length=100)
    review=models.CharField(max_length=20)
    
    def __str__(self):
        return self.msg
