# Generated by Django 2.1.4 on 2020-04-09 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='rsex',
            field=models.CharField(choices=[('男', '男'), ('女', '女')], db_column='rsex', max_length=255),
        ),
    ]
