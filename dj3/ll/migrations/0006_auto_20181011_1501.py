# Generated by Django 2.0.7 on 2018-10-11 15:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ll', '0005_auto_20181011_1142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name_plural': '用户表'},
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterModelTable(
            name='userinfo',
            table=None,
        ),
    ]
