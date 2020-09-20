from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola pibe")

def otherAttempt(request):
    return HttpResponse("That is a common response")
