# Generated by Django 2.1.4 on 2018-12-14 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Montreapp', '0002_auto_20181214_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pointvente',
            old_name='emaill',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='pointvente',
            old_name='usernamee',
            new_name='username',
        ),
    ]
