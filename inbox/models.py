from django.db import models

# Create your models here.
class Email(models.Model):
    email = models.EmailField()
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=530)
    created = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.email