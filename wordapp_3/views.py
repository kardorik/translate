from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

from wordapp_3.models import Translation

def home(request):
    #return HttpResponse("Found the wordsapp page.")
    context = {}
    return render(request, 'wordapp_3/home.html', context)

def show_list(request):
    translation_list = Translation.objects.all()
    context = {'translation_list': translation_list}
    return render(request, 'wordapp_3/show_list.html', context)

@login_required(login_url='/login')
def profile(request):
    context = {'current_user': request.user}
    return render(request, 'wordapp_3/profile.html', context)

# Create your views here.
