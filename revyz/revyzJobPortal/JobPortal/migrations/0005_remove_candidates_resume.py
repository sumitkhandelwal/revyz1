# Generated by Django 4.0.3 on 2022-03-19 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JobPortal', '0004_candidates_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidates',
            name='resume',
        ),
    ]