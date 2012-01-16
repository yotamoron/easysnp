
from django.db import models

class BaseModel(models.Model):
    oid = models.CharField(max_length=36)
