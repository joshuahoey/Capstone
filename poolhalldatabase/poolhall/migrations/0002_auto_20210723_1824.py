# Generated by Django 3.1.8 on 2021-07-23 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poolhall', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='time',
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poolhall.user')),
            ],
        ),
    ]
