from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User)
    pic_url = models.TextField(default='https://davidkallin.files.wordpress.com/2010/11/bart-simpson.jpg')
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)

class Translation(models.Model):
  english_text = models.CharField(max_length=200)
  italian_text = models.CharField(max_length=200)
  english_description = models.TextField()
  italian_description = models.TextField()
  some_text = models.CharField(max_length=200, default='something')
  user = models.OneToOneField(User)
  

  def __str__(self):
    return self.english_text


# Create your models here.
