from django.shortcuts import render

from django.template import loader, Context
from django.http import HttpResponse
from blog.models import BlogPost

# Create your views here.
def archive(request):
    print 'request.GET:', request.GET
    print 'request.GET.getlist():', request.GET.getlist('ha')
    print 'request.POST:', request.POST
    print 'request.path:', request.path
    print 'request.encoding:', request.encoding
    posts = BlogPost.objects.all()
    t = loader.get_template('archive.html')
    c = Context({'posts':posts})
    response = HttpResponse(t.render(c))
    response['Content-Type'] = 'text'
    response['Content-Length'] = 256
    response.write('<p>fuck all you guys!!!!</p>')
    print 'response.content:', response.content
    return response

