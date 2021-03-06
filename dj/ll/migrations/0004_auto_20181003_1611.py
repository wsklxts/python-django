# Generated by Django 2.0.7 on 2018-10-03 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ll', '0003_auto_20180713_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='student2',
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
