# Generated by Django 3.2.16 on 2022-12-16 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0160_add_campaign_tracking'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='unknown_origination_utm_campaign',
            field=models.CharField(blank=True, max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='origination_utm_campaign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reports', to='cts_forms.campaign'),
        ),
    ]
