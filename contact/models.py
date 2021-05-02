from django.db import models


class Contactme(models.Model):
    name = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=256)
    message = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.name}, {self.email}"
