# Generated by Django 3.1.8 on 2021-07-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poolhall', '0008_auto_20210723_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllTables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tableNumber', models.IntegerField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
