# Generated by Django 3.2.5 on 2021-07-21 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0006_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
