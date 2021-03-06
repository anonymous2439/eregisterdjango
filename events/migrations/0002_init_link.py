# Generated by Django 3.2 on 2021-05-20 23:52

from django.db import migrations


def insert_data(apps, schema_editor):
    Link = apps.get_model('events', 'Link')

    Link.objects.bulk_create([
        Link(name='home_url', url='http://localhost:8000/'),
    ])


def delete_data(apps, schema_editor):
    Link = apps.get_model('events', 'Link')
    Link.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_link'),
    ]

    operations = [
        migrations.RunPython(insert_data, delete_data),
    ]
