# Generated by Django 3.2.4 on 2021-07-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chave', models.SlugField(max_length=100, unique=True, verbose_name='Identificação')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('url', models.URLField()),
                ('criado', models.DateField(auto_now_add=True)),
                ('publicado', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
                'ordering': ['-chave'],
            },
        ),
    ]
