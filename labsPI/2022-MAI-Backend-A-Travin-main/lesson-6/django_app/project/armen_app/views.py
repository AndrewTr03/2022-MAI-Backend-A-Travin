from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from armen_app import models

# Create your views here.
def index(request):
    http = \
    """
    <html lang="ru">
    <head>
        <title>Веб-сервер</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></meta>
        <h1>Hello from ARMEN THE SHOEMAKER!</h1>
    </head>
    <body>
        <h4>Here you can look AT MY FINE SMELLY BOOTS. FINE BOOTS YOU BUY FROM ME.</h1>
        <ul>
            <li>/Get?boots_id=n</li>
            <li>/GetAll</li>
            <li>/Post</li>
        </ul>
    </html>
    """
    return HttpResponse(http)


def get_boots(request):
    if request.method == "GET":
        boots_id = request.GET.get("boots_id", -1)
        try:
            boot = models.Boots.objects.get(boots_id=boots_id)
            return JsonResponse({"boots_id": boot.boots_id, "name": boot.name, "description": boot.description, "countries": boot.countries, "color": boot.color.name})
        except models.Boots.DoesNotExist:
            return HttpResponse("<h2>Empty response</h2>")
    else:
        return HttpResponseBadRequest("<h2>Error!</h2>")

def getall_boots(request):
    if request.method == "GET":
        try:
            boots = models.Boots.objects.all()
            list=[]
            for boot in boots:
                list.append({"boots_id": boot.boots_id, "name": boot.name, "description": boot.description, "countries": boot.countries, "color": boot.color.name})
            
            return JsonResponse({"All boots" : [list]})
        except models.Boots.DoesNotExist:
            return HttpResponse("<h2>Empty response</h2>")

    else:
        return HttpResponseBadRequest("<h2>Error!</h2>")


@csrf_exempt
def post_boots(request):
    if request.method == "POST":
        name = request.GET.get("name", None)
        if not name:
            return HttpResponse("<h2>Empty name</h2>")
        description = request.GET.get("description", None)
        countries = request.GET.get("countries", None)
        color = request.GET.get("color", None)
        
        try:
            boot = models.Boots()
            boot.name = name
            boot.description = description
            boot.countries = countries
            boot.color = models.Colors.objects.get(name=str(color))
            boot.save()
            return HttpResponse("<h2>Successful</h2>")
        except:
            return HttpResponse("<h2>Unsuccessful</h2>")
    else:
        return HttpResponseBadRequest("<h2>Error!</h2>")
