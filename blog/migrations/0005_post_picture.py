# Generated by Django 2.0.8 on 2018-10-06 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
