# Generated by Django 3.2.13 on 2022-06-07 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]