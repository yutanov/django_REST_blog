# Generated by Django 4.0.4 on 2022-04-23 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_comment_parent_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='parent_id',
            new_name='parent',
        ),
    ]
