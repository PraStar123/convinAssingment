# Generated by Django 3.0.2 on 2020-01-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200103_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='encryption',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='fileName',
            field=models.CharField(max_length=256),
        ),
    ]
