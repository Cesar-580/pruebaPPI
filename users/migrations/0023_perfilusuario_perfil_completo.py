# Generated by Django 3.2.22 on 2023-10-22 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_remove_perfilusuario_perfil_completo'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilusuario',
            name='perfil_completo',
            field=models.CharField(blank=True, default='Disabled', editable=False, max_length=100, null=True),
        ),
    ]