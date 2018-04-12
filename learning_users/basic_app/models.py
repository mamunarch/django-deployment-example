from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    # stablish link with User (from django)
    user = models.OneToOneField(User)

    # adding addtional info field with the User
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    # string represintation
    def __str__(self):
        return self.user.username
