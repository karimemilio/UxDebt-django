# Generated by Django 5.0.10 on 2024-12-20 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_issue_tags_alter_issue_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tag_id',
            new_name='tagId',
        ),
    ]
