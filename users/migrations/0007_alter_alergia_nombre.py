# Generated by Django 3.2.22 on 2023-10-22 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alergia_medicamento_medicamentoalergico_perfilusuario_tiposangre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alergia',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
    ]