# Generated by Django 5.1.7 on 2025-04-02 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='ingresso_fab',
            field=models.DateField(blank=True, help_text='', null=True, verbose_name='Data de ingresso na Fábrica de Software'),
        ),
    ]
