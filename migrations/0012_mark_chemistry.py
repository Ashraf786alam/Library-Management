# Generated by Django 3.1.2 on 2020-12-05 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0011_auto_20201205_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='Chemistry',
            field=models.IntegerField(default=0),
        ),
    ]
