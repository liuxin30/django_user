# Generated by Django 3.1 on 2020-08-28 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='questuion_test',
            new_name='question_text',
        ),
    ]