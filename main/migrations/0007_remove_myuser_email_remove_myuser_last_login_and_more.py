# Generated by Django 4.0.1 on 2022-04-07 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_myuser_alter_slider_options_alter_slider_bg_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='password',
        ),
        migrations.AddField(
            model_name='myuser',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi'),
            preserve_default=False,
        ),
    ]
