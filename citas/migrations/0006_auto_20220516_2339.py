# Generated by Django 3.1.4 on 2022-05-16 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0005_auto_20220224_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='critica_sitios',
            name='evaluador',
            field=models.CharField(choices=[('Axel E González', 'Axel E González'), ('Bianca E Monroy', 'Bianca E Monroy')], default='Bianca E Monroy', max_length=20),
        ),
    ]