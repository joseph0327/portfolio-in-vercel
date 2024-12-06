from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.subject}"