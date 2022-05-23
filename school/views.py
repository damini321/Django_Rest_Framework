from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, generics
from . models import students
#from user.models import User
from . serializers import studentsSerializer, Student_Notifications_Serializer
from . models import * 


class studentList(generics.CreateAPIView):
    queryset = students.objects.all()
    serializer_class = studentsSerializer


class Student_Notifications(generics.ListAPIView):
    queryset = Student_Notifications.objects.all()
    serializer_class = Student_Notifications_Serializer

    
    def list(self, request):
        students1= students.objects.all()
        serializer=studentsSerializer(students1, many=True)
        return Response(serializer.data)

    # def list(self, request, *args, **kwargs):
    #     if self.request.user.is_superuser:
    #         try:
    #             query = students.objects.get(id=self.kwargs["id"])
    #             serializer = self.get_serializer(query)
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #         except ObjectDoesNotExist:
    #             return Response({"DOES_NOT_EXIST": "Does not exist"}, status=status.HTTP_404_NOT_FOUND)
    #     else:
    #         return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)

       