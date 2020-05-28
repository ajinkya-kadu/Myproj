# Generated by Django 3.0.6 on 2020-05-27 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firstcarousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=' ', upload_to='students/images')),
            ],
        ),
        migrations.CreateModel(
            name='Pdfupload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default=' ', upload_to='students/pdffiles')),
            ],
        ),
        migrations.CreateModel(
            name='Resultphoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=' ', upload_to='students/images')),
            ],
        ),
    ]
