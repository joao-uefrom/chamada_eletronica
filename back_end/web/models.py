from django.db import models


class Config(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.CharField(max_length=255, null=True)


class Shift(models.Model):
    name = models.CharField(max_length=255, unique=True)
    open = models.TimeField()
    close = models.TimeField()


class Student(models.Model):
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    enrolment = models.CharField(max_length=25, unique=True)
    c_lass = models.CharField(max_length=100, null=True, db_column='class')
    shift = models.ForeignKey(Shift, on_delete=models.RESTRICT)
    training = models.BooleanField(default=False)
    photos = models.IntegerField(default=0)

    class Meta:
        ordering = ['name']


class Totem(models.Model):
    mac_address = models.CharField(max_length=12, unique=True)
    ip = models.CharField(max_length=15)
    student = models.ForeignKey(Student, on_delete=models.RESTRICT, null=True)


class Entry(models.Model):
    student = models.ForeignKey(Student, on_delete=models.RESTRICT)
    totem = models.ForeignKey(Totem, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
