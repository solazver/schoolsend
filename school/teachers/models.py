from django.db import models

# Create your models here.
class Person(models.Model):
    identity_card = models.CharField(max_length=9, primary_key=True)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)

    class Meta:
        db_table = 'person'

class Specialty(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'specialty'


class Teacher(Person):
    specialties = models.ManyToManyField(Specialty)

    class Meta:
        db_table = 'teacher'

