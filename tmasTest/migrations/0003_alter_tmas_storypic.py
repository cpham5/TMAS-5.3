# Generated by Django 4.0.4 on 2022-05-11 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmasTest', '0002_tmas_storypic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tmas',
            name='storyPic',
            field=models.ImageField(blank=True, default='picture_placeholder.png', null=True, upload_to='media'),
        ),
    ]
