from django.db import models


class ClassCodes(models.Model):
    code = models.CharField(max_length=250, null=False)
    semester = models.SmallIntegerField(null=True)
    major = models.CharField(max_length=250)


class Professors(models.Model):
    name = models.CharField(max_length=250, null=False)
    photoURL = models.URLField(null=True)
    description = models.TextField(null=True)


class Students(models.Model):
    campusCode = models.CharField(max_length=100, null=False)
    registration = models.CharField(max_length=250, null=False)


class Classes(models.Model):
    professorId = models.ForeignKey(Professors, on_delete=models.RESTRICT, null=False)
    classCodeId = models.ForeignKey(ClassCodes, on_delete=models.RESTRICT, null=False)
    label = models.CharField(max_length=250, null=False)
    period = models.CharField(max_length=10)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)


class EnrolledStudentClasses(models.Model):
    classId = models.ForeignKey(Classes, on_delete=models.RESTRICT, null=False)
    studentId = models.ForeignKey(Students, on_delete=models.CASCADE, null=False)


class Feedbacks(models.Model):
    studentClassId = models.ForeignKey(
        EnrolledStudentClasses, on_delete=models.CASCADE, null=False
    )
    review = models.SmallIntegerField(null=False)
    comment = models.TextField(null=True)
