from django.db import models
import os
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def validate_file_extension(value):
    """
    Agar fayl kengaytmasi berilganlarning orasida bo'lmasa, xatolik beradi
    """
    # [0]  yo'li + fayl nomi
    # [1] fayl kengaytmasi,: .docx, .jpg
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=False, null=False)
    profile_image = models.ImageField(upload_to='portfolio')
    social_github = models.CharField(max_length=100, blank=False, null=True)
    social_telegram = models.CharField(max_length=100, blank=True, null=False)
    social_instagram = models.CharField(max_length=100, default="instagram")
    social_youtube = models.CharField(max_length=100)
    social_website = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='files', default='files/default.xlsx', validators=[validate_file_extension])
    video = models.FileField(upload_to='videos')
    audio = models.FileField(upload_to='audios')


