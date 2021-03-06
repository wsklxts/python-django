# Generated by Django 2.0.7 on 2018-10-05 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ll', '0002_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('admin_to_user', models.ManyToManyField(to='ll.user')),
            ],
        ),
        migrations.AlterModelOptions(
            name='usertype',
            options={'verbose_name_plural': '用户类型'},
        ),
        migrations.AlterField(
            model_name='usertype',
            name='name',
            field=models.CharField(max_length=32, verbose_name='用户类型'),
        ),
    ]
