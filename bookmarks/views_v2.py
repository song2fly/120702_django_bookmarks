# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def main_page(request):
    
    template = get_template('main_page.html')
    variables = Context({
                         'head_title' : 'DJANGO BOOKMARK',
                         'page_title' : 'Welcome to bookmark',
                         'page_body' : 'save the bookmark!'
                         })
    
    output = template.render(variables)
    return HttpResponse(output)


