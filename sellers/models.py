from django.db import models

# Create your models here.


class Seller(models.Model):
    name        = models.TextField()
    description = models.TextField()
    phone       = models.TextField()
    on_contact  = models.BooleanField(default=False)