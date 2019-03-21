from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import *
from .serializers import TeachersInfoSerializer

from rest_framework.viewsets import ModelViewSet

class TeachersInfoViewSet(ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeachersInfoSerializer


def view(request):
    pass

def aaa(request):
    return HttpResponse('666')