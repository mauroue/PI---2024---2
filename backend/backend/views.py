from django.http import HttpResponse, HttpResponseNotModified

def register(request):
    #todo: check if user already exists
    #todo: check if all data are correct
    #todo: create user
    #todo: return user
    return HttpResponse(b"teste")

def login(request):
    #authentication
    return HttpResponseNotModified()
