# Generated by Django 2.0.6 on 2018-07-01 23:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0009_auto_20180701_2335'),
    ]

    operations = [

        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(default='static/f1.png', upload_to='uploads/%d-%m-%y/%H_%M_%S'),
        )

    ]