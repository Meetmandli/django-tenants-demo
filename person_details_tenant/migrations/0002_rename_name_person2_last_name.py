# Generated by Django 4.0.6 on 2022-07-15 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person_details_tenant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person2',
            old_name='name',
            new_name='last_name',
        ),
    ]