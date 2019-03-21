from rest_framework import serializers
from .models import *


class TeachersInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = '__all__'

