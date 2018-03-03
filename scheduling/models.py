# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Curriculum(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    degreeprogram = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'curriculum'

class Studentgroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    numberofstudents = models.IntegerField(blank=True, null=True)
    curriculumid = models.ForeignKey('Curriculum', on_delete=models.CASCADE, db_column='curriculumid')

    class Meta:
        managed = True
        db_table = 'studentgroup'

		
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    cousename = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=5, blank=True, null=True)
    credit = models.IntegerField(blank=True, null=True)
    semester11 = models.IntegerField(blank=True, null=True)
    semester12 = models.IntegerField(blank=True, null=True)
    semester21 = models.IntegerField(blank=True, null=True)
    semester22 = models.IntegerField(blank=True, null=True)
    semester31 = models.IntegerField(blank=True, null=True)
    semester32 = models.IntegerField(blank=True, null=True)
    semester41 = models.IntegerField(blank=True, null=True)
    semester42 = models.IntegerField(blank=True, null=True)
    curriculumid = models.ForeignKey('Curriculum', on_delete=models.CASCADE, db_column='curriculumid')

    class Meta:
        managed = True
        db_table = 'course'

		
class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'teacher'

		
class Courseimplementation(models.Model):
    courseid = models.ForeignKey('Course', on_delete=models.CASCADE, db_column='courseid')
    teacherid = models.ForeignKey('Teacher', on_delete=models.CASCADE, db_column='teacherid')
    id = models.AutoField(primary_key=True)
    studentgroupid = models.ForeignKey('Studentgroup', on_delete=models.CASCADE, db_column='studentgroupid')

    class Meta:
        managed = True
        db_table = 'courseimplementation'
        unique_together = (('courseid', 'teacherid', 'id'),)


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'room'



