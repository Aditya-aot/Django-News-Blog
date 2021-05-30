from django.db import models


# Create your models here.

class task_model(models.Model) :
    task = models.TextField()
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)


