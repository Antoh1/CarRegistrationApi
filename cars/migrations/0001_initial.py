# Generated by Django 4.2 on 2023-10-13 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=20)),
                ('reg_no', models.CharField(max_length=20)),
                ('milage', models.IntegerField()),
                ('model', models.CharField(max_length=20)),
                ('owner', models.CharField(max_length=20)),
            ],
        ),
    ]
