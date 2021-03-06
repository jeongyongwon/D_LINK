# Generated by Django 2.2.14 on 2020-08-20 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('username', models.CharField(max_length=30)),
                ('articleId', models.IntegerField()),
                ('articleUserId', models.IntegerField()),
                ('thumbnailPath', models.TextField()),
                ('alarmType', models.IntegerField()),
                ('isFetch', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('username', models.CharField(max_length=30)),
                ('roomId', models.IntegerField()),
                ('profileImage', models.TextField(null=True)),
                ('choice', models.IntegerField()),
            ],
        ),
    ]
