# Generated by Django 3.2.8 on 2021-11-11 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petshop', '0004_auto_20211111_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='detalhes',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
