# Generated by Django 4.0.4 on 2022-04-23 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['date_pub']},
        ),
    ]
