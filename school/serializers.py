from rest_framework import serializers
from .models import *


class studentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = '__all__'
        depth = 1


class studentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = '__all__'
