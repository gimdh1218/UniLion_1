from django.shortcuts import render
from .models import Gift
from .models import Notice

# Create your views here.
def home(request):
    return render(request, 'home.html')

def introduce(request):
    return render(request, 'introduce.html')

def story(request):
    return render(request, 'story.html')

def community(request):
    notices = Notice.objects.all()
    return render(request, 'community.html', {'notices': notices})

def question(request):
    return render(request, 'question.html')
