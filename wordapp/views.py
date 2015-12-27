from django.shortcuts import render
from django.http import HttpResponse

from wordapp.models import Translation

def home(request):
    #return HttpResponse("Found the wordsapp page.")
    context = {}
    return render(request, 'wordapp/home.html', context)

def show_list(request):
    translation_list = Translation.objects.all()
    context = {'translation_list': translation_list}
    return render(request, 'wordapp/show_list.html', context)

# Create your views here.
