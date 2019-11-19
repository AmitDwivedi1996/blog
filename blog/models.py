from django.db import models

from django.contrib.postgres.fields import ArrayField




class Student(models.Model):
    studentId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    # rollNo = models.IntegerField(null=True)
    # username = models.CharField(max_length=50)
    registered = models.BooleanField()
    email = models.EmailField(max_length=100, null =True)
    classId = ArrayField(models.CharField(max_length=100),default=list, null=True)
    phone = models.BigIntegerField(blank=False, default=0)




class Class(models.Model):
    classId = models.CharField(primary_key=True, max_length=100)
    className = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    maxLectures = models.IntegerField(default=1)


class Lecture(models.Model):
    lectureId = models.CharField(primary_key=True, max_length=50)
    lectureName = models.CharField(max_length=100)
    remarks = models.CharField(max_length=100)
    schedule = models.DateTimeField()
    teacherName = models.CharField(max_length=100, blank=False)
    teacherId = models.IntegerField()


class Teacher(models.Model):
    teacherId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    phone = models.BigIntegerField(blank=False, unique=True)
    email = models.CharField(max_length=30)
    institute = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=100, null=True)
    age = models.IntegerField( null=True)
    experience = models.IntegerField(null=True)
    classId = models.CharField(max_length=50, null=True)


class rateStudent(models.Model):
    StudentId = models.ForeignKey('Student', on_delete=models.CASCADE)
    TeacherId = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    Attentiveness = models.FloatField(default=5.0)
    attendance = models.FloatField(default=5.0)
    Doubts = models.FloatField(default=5.0)


class rateTeacher(models.Model):
    StudentId = models.ForeignKey('Student', on_delete=models.CASCADE)
    TeacherId = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    LectureQuality = models.FloatField(default=5.0)
    DoubtClearance = models.FloatField(default=5.0)


class Institue(models.Model):
    Id = models.AutoField(primary_key=True)
    address = models.IntegerField()
    name = models.CharField(max_length=50)
    profilePic = models.ImageField()


class Address(models.Model):
    house = models.CharField(max_length=15)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin = models.BigIntegerField()
    locality = models.CharField(max_length=50, default=' ')


class FCMToken(models.Model):
    FcmToken = models.CharField(max_length=20)
    PersonId = models.IntegerField()
    Person = models.CharField(max_length=15)

class Quiz(models.Model):
    Id = models.AutoField(primary_key=True)
    teacherId = models.IntegerField()
    classId = models.CharField(max_length=100)
    totalMarks = models.IntegerField()
    #questions = ArrayField(models.CharField(max_length=100))
    name = models.CharField(max_length=100)
   # schedule = ?   #Schema is not clear on what this is

class Question(models.Model):
    questionId = models.AutoField(primary_key=True)
    questionText = models.CharField(max_length=500)
    quizId = models.IntegerField()
    options = ArrayField(models.CharField(max_length = 100)) #if length = 0, subjective, =2 mcq2, =4 mcq4

class Result(models.Model):
    Id = models.AutoField(primary_key=True)
    quizId = models.CharField(max_length=100)
    studentId = models.CharField(max_length=100)
    marks = models.IntegerField()

class StudyMaterial(models.Model):
    Type = models.CharField(max_length=30)
    board = models.CharField(max_length=20)
    source = models.CharField(max_length=30)
    question = models.TextField()
    options = ArrayField(models.CharField(max_length=20), null=True)
    answer = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=50)
    Class = models.CharField(max_length=50)
    noQuiz = models.IntegerField()
    difficulty = models.CharField(max_length=20)
    chapter = models.IntegerField()


class NotificationsTable(models.Model):
    recieverType = models.CharField(max_length=30)
    recieverId = models.IntegerField()
    status = models.CharField(max_length=20)
    body = models.TextField()
    title = models.CharField(max_length=50)
    datetime = models.DateTimeField(null=True)


class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    lectureId = models.CharField(max_length=50)
    studentId = models.IntegerField()
    status = models.CharField(max_length=15)
    acknowledgement = models.CharField(max_length=15)
