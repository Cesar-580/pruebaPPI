# Generated by Django 3.2.22 on 2023-10-23 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_auto_20231022_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='triage',
            name='triage_calculado',
            field=models.CharField(default=False, max_length=20),
        ),
    ]
