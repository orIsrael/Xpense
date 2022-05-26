from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to="images/", default="https://bootdey.com/img/Content/avatar/avatar1.png")

    def __str__(self) -> str:
        return str(self.username)
