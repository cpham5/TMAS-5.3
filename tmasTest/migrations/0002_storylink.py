# Generated by Django 4.0.4 on 2022-05-09 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmasTest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='storyLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
        ),
    ]