from django.db import models
from django.core.mail import send_mail

gender_choices = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)

class students(models.Model):
    
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    roll_no=models.IntegerField()
    gender = models.CharField(max_length=10, choices=gender_choices)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
       return self.first_name

class Student_Notifications(models.Model):
    student = models.ForeignKey(students, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def student_registered(self, students, first_name, from_email, email):
        subject = "Register Successful"
        message = "Hi {} Thanks for registering.".format(first_name)
        Student_Notifications.objects.create(students=students,
                                                  message=message)
        try:
            send_mail(subject, message, from_email, [email])
        except:
            pass
