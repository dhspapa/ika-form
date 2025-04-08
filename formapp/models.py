
from django.db import models

class Submission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    description = models.TextField()
    excel_file = models.FileField(upload_to='uploads/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
