from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=256)
    client_name = models.CharField(max_length=256)
    project_details = models.CharField(max_length=256)
    role = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.project_name}"