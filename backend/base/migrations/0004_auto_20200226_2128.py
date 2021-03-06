# Generated by Django 2.2.8 on 2020-02-27 02:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20200226_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chatroom',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
