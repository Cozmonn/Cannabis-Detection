# Generated by Django 4.0.2 on 2022-03-30 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_remove_contact_fullname_remove_contact_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]