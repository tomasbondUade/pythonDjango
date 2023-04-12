from django.http import HttpResponse

def index(request):
    return HttpResponse("hola mundo")

def product(request):
    return HttpResponse("perro")