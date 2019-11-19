from django.contrib import admin
from .models import Student, Class, Lecture, Teacher,rateStudent,rateTeacher,FCMToken,Institue,Address,StudyMaterial,NotificationsTable
from .models import Quiz, Result, Question

admin.site.register(Student)
