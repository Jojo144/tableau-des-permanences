# Generated by Django 2.1.7 on 2019-03-10 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permanences', '0005_auto_20190309_1818'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indexpagedata',
            options={'verbose_name': "Données pour la page d'accueil"},
        ),
        migrations.AlterField(
            model_name='indexpagedata',
            name='txt',
            field=models.TextField(blank=True, verbose_name=''),
        ),
    ]