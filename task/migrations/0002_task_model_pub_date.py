# Generated by Django 3.0.7 on 2021-05-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_model',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
