from django.db import models

# Create your models here.
class Tasks(models.Model):
    task = models.CharField(max_length=32)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return self.task
    
class History(models.Model):
    htask = models.CharField(max_length=50)
    hdescription = models.CharField(max_length=1024)

    def __str__(self):
        return self.htask