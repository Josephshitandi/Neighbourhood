# Generated by Django 3.1.3 on 2020-12-02 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='hoodLocation',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='hoodName',
            new_name='name',
        ),
    ]