# Generated by Django 3.2.4 on 2021-07-17 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210716_1530'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publicado',)},
        ),
    ]
