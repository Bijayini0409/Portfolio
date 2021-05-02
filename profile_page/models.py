from django.db import models


class About(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    job = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=256, null=False)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
