from django.http import HttpResponse

def index(request):
    return HttpResponse("Bonjour B3 CDA")