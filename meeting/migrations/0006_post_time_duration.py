# Generated by Django 3.2.9 on 2021-11-24 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0005_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='time_duration',
            field=models.IntegerField(null=True),
        ),
    ]
