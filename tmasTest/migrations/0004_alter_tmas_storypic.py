# Generated by Django 4.0.4 on 2022-05-13 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmasTest', '0003_alter_tmas_storypic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tmas',
            name='storyPic',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
