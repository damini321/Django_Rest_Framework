from django.urls import path
from school import views

urlpatterns = [
    path('messages/', views.studentList.as_view()),
]
