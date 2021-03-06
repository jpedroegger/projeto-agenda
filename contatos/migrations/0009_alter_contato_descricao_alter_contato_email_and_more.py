# Generated by Django 4.0.1 on 2022-05-08 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0008_alter_contato_data_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/%Y/%m/'),
        ),
    ]
