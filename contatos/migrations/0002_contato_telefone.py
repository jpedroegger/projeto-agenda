# Generated by Django 4.0.1 on 2022-01-15 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='telefone',
            field=models.CharField(default=9999999, max_length=11),
            preserve_default=False,
        ),
    ]
