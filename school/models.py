from django.db import models


class students(models.Model):
    created_by = models.ForeignKey("user.User", on_delete=models.CASCADE)
    messages = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
