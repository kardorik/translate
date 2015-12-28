from django.contrib.auth.models import User
from django.db import models

class Word(models.Model):
    label = models.CharField(max_length=200)
    definition = models.TextField(default='What does this word mean?')
    def __str__(self):
        return self.label

class Translation(models.Model):
    alien_word = models.ForeignKey(Word, default=1, related_name='alien_word')
    native_word = models.ForeignKey(Word, default=1, related_name='native_word')
    native_translation_word = models.ForeignKey(Word, default=1, related_name='native_translation_word')
    alien_description = models.TextField(default='')
    native_description = models.TextField(default='')
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(User, default=1, related_name='author')
    pic_url = models.TextField(default='http://s.hswstatic.com/gif/electric-car-history-2.jpg') 
    def __str__(self):
        return '%s : %s' % (self.alien_word, self.native_word)
    
class Profile(models.Model):
    user = models.OneToOneField(User)
    pic_url = models.TextField(default='https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT0mp4SuvY1YNtjFXIk7YFjT42HLjN_tpLOjnUX9dvAaSFO1jbsEQ') 
    likes = models.IntegerField(default=0)
    def __str__(self):
        return '#%s: %s' % (str(self.id), self.user.username)

# Create your models here.
