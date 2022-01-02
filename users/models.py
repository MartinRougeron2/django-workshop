from django.db import models
from django.contrib.auth.models import User

langs = (
    ("fr", "Français"),
    ("en", "English")
)


class BirddyTor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lang = models.CharField(verbose_name="user_language", max_length=2, choices=langs)

    def __str__(self):
        return self.user.__str__()
