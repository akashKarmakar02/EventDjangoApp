# Generated by Django 4.2 on 2023-06-07 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='phone',
            field=models.IntegerField(blank=True, verbose_name='Phone no'),
        ),
    ]