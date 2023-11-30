# Generated by Django 4.2.4 on 2023-11-03 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_rename_action_action_actiondetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='productnintendo',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='productNS'),
        ),
        migrations.AddField(
            model_name='productnintendo',
            name='specfile',
            field=models.FileField(blank=True, null=True, upload_to='specfileNS'),
        ),
        migrations.AddField(
            model_name='productps4',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='productPS4'),
        ),
        migrations.AddField(
            model_name='productps4',
            name='specfile',
            field=models.FileField(blank=True, null=True, upload_to='specfilePS4'),
        ),
        migrations.AddField(
            model_name='productps5',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='productPS5'),
        ),
        migrations.AddField(
            model_name='productps5',
            name='specfile',
            field=models.FileField(blank=True, null=True, upload_to='specfilePS5'),
        ),
    ]