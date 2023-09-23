from django.shortcuts import render
from .models import Blogs


# Create your views here.
def index(request):
    blog = Blogs.objects.all()
    context = {'blog': blog}

    return render(request, 'blogs/index.html', context)


def detail(request, pk):
    blog = Blogs.objects.get(pk=pk)
    context = {'blog': blog}

    return render(request, 'blogs/detail.html', context)
