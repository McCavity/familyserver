# Generated by Django 2.0 on 2018-01-07 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_auto_20180107_1902'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('list', 'text')},
        ),
    ]