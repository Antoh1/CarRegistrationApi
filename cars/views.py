from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Car
from .serializers import CarSerializer
 

# Create your views here.
def index(request):
    cars = Car.objects.all()
    serializers = CarSerializer(cars, many=True)
    return JsonResponse({'cars':serializers.data})
