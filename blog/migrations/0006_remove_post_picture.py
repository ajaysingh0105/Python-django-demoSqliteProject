# Generated by Django 2.0.8 on 2018-10-06 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='picture',
        ),
    ]