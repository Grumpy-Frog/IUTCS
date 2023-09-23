from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from .models import Blogs
from .forms import MDEditorForm

# Create your views here.
def index(request):
    blog = Blogs.objects.all()
    context = {'blog': blog}

    return render(request, 'blogs/index.html', context)


def detail(request, pk):
    blog = Blogs.objects.get(pk=pk)
    context = {'blog': blog}

    return render(request, 'blogs/detail.html', context)


def createBlog(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            blog = Blogs()
            blog.title = request.POST.get('title')
            blog.author = request.POST.get('author')
            blog.content = request.POST.get('content')

            blog.save()

            return redirect("blogs:blogs")

    else:
        return render(request, 'blogs/createBlog.html')


class editBlog(TemplateView):
    template_name = 'blogs/editBlog.html'

    def get_context_data(self, *args, **kwargs):
        blog = Blogs.objects.get(pk=self.kwargs.get('pk'))
        context = super().get_context_data(*args, **kwargs)

        context['blog'] = blog

        return context


def updateBlog(request, *args, **kwargs):
    pk = kwargs.get('pk')

    blog = Blogs.objects.get(pk=pk)

    title = request.POST['title']
    author = request.POST['author']

    content = request.POST['content']

    blog.title = title
    blog.author = author
    blog.content = content

    blog.save()

    return HttpResponseRedirect(
        reverse("blogs:blogs"))


def deleteBlog(request, *args, **kwargs):
    pk = kwargs.get('pk')
    d_blog = Blogs.objects.get(pk=pk)
    d_blog.delete()

    return HttpResponseRedirect(
        reverse("blogs:blogs"))


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import markdown

