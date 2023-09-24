# Generated by Django 4.2.5 on 2023-09-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=20)),
                ('students', models.ManyToManyField(to='study.student')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=100)),
                ('video_link', models.CharField(max_length=200)),
                ('video_length', models.IntegerField()),
                ('products', models.ManyToManyField(to='study.product')),
                ('viewed_by_student', models.ManyToManyField(to='study.student')),
            ],
        ),
    ]
