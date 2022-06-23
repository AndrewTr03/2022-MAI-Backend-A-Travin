from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from armen_app.models import Colors, Boots
from armen_app.serializers  import ColorSerializer, BootsSerializer
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework import status, viewsets
from rest_framework.response import Response

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
            <li>boots/</li>
            <li>color/</li>
        </ul>
    </html>
    """
    return HttpResponse(http)

class ColorViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Colors.objects.all()
        serializer = ColorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ColorSerializer(data=request.data)
        
        if serializer.is_valid():
            color = Colors()
            color.name = serializer.validated_data["name"]
            color.save()
            return Response({"status": "OK"})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        queryset = Colors.objects.all()
        
        color = None
        try:
            color = get_object_or_404(queryset, pk=pk)
        except:
            pass
        serializer = ColorSerializer(color)
        return Response(serializer.data)

class BootViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Boots.objects.all()
        serializer = BootsSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = BootsSerializer(data=request.data)
        
        if serializer.is_valid():
            boots = Boots()
            boots.name = serializer.validated_data["name"]
            boots.color = serializer.validated_data["color"]
            boots.countries = serializer.validated_data["countries"]
            boots.description = serializer.validated_data["description"]
            boots.save()
            return Response({"status": "OK"})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        queryset = Boots.objects.all()
        
        boots = None
        try:
            boots = get_object_or_404(queryset, pk=pk)
        except:
            pass
        serializer = BootsSerializer(boots)
        return Response(serializer.data)

