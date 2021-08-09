from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    user_type = models.CharField(max_length=50, null=True, blank=True)


class Images(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to="image/", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Images"
        ordering = ["-timestamp"]
