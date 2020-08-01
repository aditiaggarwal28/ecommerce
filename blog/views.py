# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Blogpost
from math import ceil
def index(request):
    blogs = Blogpost.objects.all()
    return render(request, 'blog/index.html',{'blog':blogs})


def blogpost(request,myid):
    blogs=Blogpost.objects.filter(post_id=myid)
    # nslides=(len(blogs)//2)+ceil((len(blogs)/2)-(len(blogs)//2))
    # range=range(1,len(blogs))
    # blog=[[blogs,nslides,range]]
    return render(request, 'blog/blogpost.html',{'blog':blogs})