# Generated by Django 4.0.1 on 2022-02-10 01:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0007_alter_contato_data_criacao_alter_contato_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]