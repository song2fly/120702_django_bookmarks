# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.template import RequestContext
from bookmarks.forms import *
from bookmarks.models import *

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
'''
def main_page(request):
    template = get_template('main_page.html')
    variables = Context({
                         'user' : request.user
                         })
    output = template.render(variables)
    return HttpResponse(output)
'''

def main_page(request):
    return render_to_response('main_page.html', RequestContext(request))
    
'''
def main_page(request):
    return render_to_response(
                             'main_page.html',
                             {'user' : request.user}
                             )
'''                                 

def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('cannot find')
    
    bookmarks = user.bookmark_set.all()
    # + user obj
    variables = RequestContext(request, {
                         'username' : username,
                         'bookmarks' : bookmarks
                         })
    return render_to_response('user_page.html', variables)

'''
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
'''
  
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
                email = form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
        variables = RequestContext(request, {'form' : form})
        return render_to_response('registration/register.html', variables)
            
def bookmark_save_page(request):
    if request.method == 'POST':
        form = BookmarkSaveForm(request.POST)
        if form.is_valid():
            
            link, dummy = Link.objects.get_or_create(
                                                     url=form.cleaned_data['url']
                                                     )
            
            bookmark, created = Bookmark.objects.get_or_create(
                                                               user=request.user,
                                                               link=link
                                                               )            
            
            bookmark.title = form.cleaned_data['title']
            
            if not created:
                bookmark.tag_set.clear()
                
            tag_names = form.cleaned_data['tags'].split()
            for tag_name in tag_names:
                tag, dummy = Tag.objects.get_or_create(name=tag_name)
                bookmark.tag_set.add(tag)
                
            bookmark.save()
            return HttpResponseRedirect(
                                        '/user/%s/'%request.user.name
                                        )
    else:
        form = BookmarkSaveForm()
        variables = RequestContext(request, {
                                             'form':form
                                             })
        return render_to_response('bookmark_save.html', variables)
                
            
    
        