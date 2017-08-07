from django.shortcuts import render
from blog.models import * 
from mysite.settings import *
from django.http import Http404
from blog.form import CommentForm
# Create your views here.
def archive(request):
    blogs = Blog.objects.all().order_by('-created')
    return render(request,'blog_list.html',{'blogs':blogs,'BLOG_TITLE':BLOG_TITLE})

def get_details(request,blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
    ctx = {
        'blog':blog,
        'comments':blog.comment_set.all().order_by('-created'),
        'form':form
    }
    return render(request,'blog_details.html',ctx)