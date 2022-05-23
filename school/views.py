from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import status, generics
from .models import *
from .serializers import *
from rest_framework import status, permissions
from .models import *


class studentList(generics.CreateAPIView):
    queryset = students.objects.all()
    serializer_class = studentPostSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = studentPostSerializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            dict = serializer.data
            dict["created_by"] = {
                "id": self.request.user.id,
                "username": self.request.user.username,
                "email": self.request.user.email
            }
            return Response(dict, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
