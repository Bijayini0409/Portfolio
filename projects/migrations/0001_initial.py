# Generated by Django 2.2 on 2021-04-23 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=256)),
                ('client_name', models.CharField(max_length=256)),
                ('project_details', models.CharField(max_length=256)),
                ('role', models.CharField(max_length=256)),
            ],
        ),
    ]
