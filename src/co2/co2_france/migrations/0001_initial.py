# Generated by Django 3.0.7 on 2020-06-28 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Co2Emission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co2_rate', models.IntegerField()),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]
