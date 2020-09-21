from django.http import HttpResponse
import datetime
from django.template import Template,Context

def saludo(req):
    return HttpResponse("Hola pibe")

def init_attempt(req):

    require_doc = open("D:/python-backend/firstWebsite/firstWebSite/templates/index.html")
    templated_doc = Template(require_doc.read())
    require_doc.close()

    ctx = Context()
    finished_doc = templated_doc.render(ctx)

    return HttpResponse(finished_doc)

def claimDate(req):
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
