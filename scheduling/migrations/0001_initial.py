# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-02 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=20, null=True)),
                ('cousename', models.CharField(blank=True, max_length=255, null=True)),
                ('language', models.CharField(blank=True, max_length=5, null=True)),
                ('credit', models.IntegerField(blank=True, null=True)),
                ('semester11', models.IntegerField(blank=True, null=True)),
                ('semester12', models.IntegerField(blank=True, null=True)),
                ('semester21', models.IntegerField(blank=True, null=True)),
                ('semester22', models.IntegerField(blank=True, null=True)),
                ('semester31', models.IntegerField(blank=True, null=True)),
                ('semester32', models.IntegerField(blank=True, null=True)),
                ('semester41', models.IntegerField(blank=True, null=True)),
                ('semester42', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'course',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Courseimplementation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('courseid', models.ForeignKey(db_column='courseid', on_delete=django.db.models.deletion.CASCADE, to='scheduling.Course')),
            ],
            options={
                'db_table': 'courseimplementation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('degreeprogram', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'curriculum',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('capacity', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'room',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Studentgroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('numberofstudents', models.IntegerField(blank=True, null=True)),
                ('curriculumid', models.ForeignKey(db_column='curriculumid', on_delete=django.db.models.deletion.CASCADE, to='scheduling.Curriculum')),
            ],
            options={
                'db_table': 'studentgroup',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'teacher',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='courseimplementation',
            name='studentgroupid',
            field=models.ForeignKey(db_column='studentgroupid', on_delete=django.db.models.deletion.CASCADE, to='scheduling.Studentgroup'),
        ),
        migrations.AddField(
            model_name='courseimplementation',
            name='teacherid',
            field=models.ForeignKey(db_column='teacherid', on_delete=django.db.models.deletion.CASCADE, to='scheduling.Teacher'),
        ),
        migrations.AddField(
            model_name='course',
            name='curriculumid',
            field=models.ForeignKey(db_column='curriculumid', on_delete=django.db.models.deletion.CASCADE, to='scheduling.Curriculum'),
        ),
        migrations.AlterUniqueTogether(
            name='courseimplementation',
            unique_together=set([('courseid', 'teacherid', 'id')]),
        ),
    ]