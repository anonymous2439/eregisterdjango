# Generated by Django 3.1.7 on 2021-04-18 15:31

from django.db import migrations


def insert_data(apps, schema_editor):
    UserRole = apps.get_model('accounts', 'UserRole')

    UserRole.objects.bulk_create([
        UserRole(name='Organizer'),
        UserRole(name='Participant'),
    ])


def delete_data(apps, schema_editor):
    UserRole = apps.get_model('accounts', 'UserRole')
    UserRole.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210409_1044'),
    ]

    operations = [
        migrations.RunPython(insert_data, delete_data),
    ]
