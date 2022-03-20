# Generated by Django 4.0.3 on 2022-03-19 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organiser', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
                ('topic', models.CharField(max_length=64)),
                ('time', models.CharField(max_length=64)),
                ('day', models.IntegerField()),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]