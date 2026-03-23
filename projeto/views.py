from django.http import HttpResponse

def view_test(request):
    return HttpResponse("Minha primeira rota")