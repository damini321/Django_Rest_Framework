from rest_framework import serializers
#from . models import students
from . models import *

class studentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = '__all__'

class Student_Notifications_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Notifications
        fields = '__all__'