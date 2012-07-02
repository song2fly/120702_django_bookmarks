# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse

def main_page(request):
    output= '''
        <html>
            <head><titie>%s</title></head>
                <body>
                    <h1>%s</h1><p>%s</p>
                </body>
        </html>
    '''%(
         'DJANGO!! | BOOKMARK',
         'welcome',
         'why'
         )
    
    return HttpResponse(output)
                    
