# Generated by Django 2.1.4 on 2020-03-07 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reader',
            fields=[
                ('rid', models.CharField(db_column='rid', default='', max_length=255, primary_key=True, serialize=False)),
                ('rname', models.CharField(db_column='rname', max_length=255, null=True)),
                ('rsex', models.CharField(choices=[('男', '男'), ('女', '女')], db_column='rex', max_length=255)),
                ('rtype', models.CharField(db_column='rtype', max_length=255, null=True)),
                ('rtel', models.CharField(db_column='rtel', max_length=255, null=True)),
                ('remail', models.CharField(db_column='remail', max_length=255, null=True)),
                ('rpsd', models.CharField(db_column='rpsd', max_length=255, null=True)),
            ],
            options={
                'db_table': 'reader',
                'managed': True,
            },
        ),
    ]