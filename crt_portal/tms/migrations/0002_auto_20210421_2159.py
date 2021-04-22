# Generated by Django 2.2.20 on 2021-04-22 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tmsemail',
            name='completed_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='tmsemail',
            name='error_message',
            field=models.TextField(help_text='If failed, this field will contain any error messages provided by TMS', null=True),
        ),
    ]
