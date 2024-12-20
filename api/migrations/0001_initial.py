# Generated by Django 5.1.4 on 2024-12-16 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('repository_id', models.AutoField(primary_key=True, serialize=False)),
                ('owner', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('git_id', models.IntegerField(unique=True)),
                ('html_url', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'repository',
            },
        ),
    ]
