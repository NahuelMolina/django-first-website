from django.http import HttpResponse
from django.template import Template,Context,loader
from django.shortcuts import render
import datetime

def about_me(req):

    c = {'foo':'bar'}
    rendered = loader.render_to_string('about_me.html',c)

    return HttpResponse(rendered)

def init_attempt(req):

    c = {'fate':'final'}
    rendered = loader.render_to_string('index.html',c)

    return HttpResponse(rendered)

def claim_date(req):
    date_now = datetime.datetime.now()
    doc = """
        <html>
        <body>
        <h1>
        Date for a while: %s 
        </h1>
        </body>
        </html>""" % date_now
    
    return HttpResponse(doc)

def calculate_age(req,age_now,agno):
    period = agno - 2020
    future_age = age_now + period
    doc = "<html><body><h2>En el año %s tendrás %s años</h2></body></html>"%(agno,future_age)

    return HttpResponse(doc)
