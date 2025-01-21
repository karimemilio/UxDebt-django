# Generated by Django 5.0.10 on 2025-01-20 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_issue_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='GitHubToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'github_token',
            },
        ),
    ]
