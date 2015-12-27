from django.contrib import admin
from wordapp_3.models import Word
from wordapp_3.models import Translation
from wordapp_3.models import Profile

admin.site.register(Word)
admin.site.register(Translation)
admin.site.register(Profile)

# Register your models here.
