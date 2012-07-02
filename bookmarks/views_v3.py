# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User

'''
def main_page(request):
    template = get_template('main_page.html')
    variables = Context({
                         'head_title' : 'DJANGO BOOKMARK',
                         'page_title' : 'Welcome to bookmark',
                         'page_body' : 'save the bookmark!'
                         })
    output = template.render(variables)
    return HttpResponse(output)
'''

def main_page(request):
    template = get_template('main_page.html')
    variables = Context({
                         'user' : request.user
                         })
    output = template.render(variables)
    return HttpResponse(output)


def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('cannot find')
    
    bookmarks = user.bookmark_set.all()
    
    template = get_template('user_page.html')
    variables = Context({
                         'username' : username,
                         'bookmarks' : bookmarks
                         })
    output = template.render(variables)
    return HttpResponse(output)
    
    
    
        