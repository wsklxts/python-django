# Generated by Django 2.0.7 on 2018-10-11 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ll', '0006_auto_20181011_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ll.Article', verbose_name='所属文章')),
            ],
        ),
    ]
