# Generated by Django 4.1.2 on 2022-10-17 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_rename_create_at_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
