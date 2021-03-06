# Generated by Django 3.0.7 on 2020-06-29 03:29

import API.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('value', models.FloatField(validators=[API.validators.min_value_validator])),
                ('stock', models.IntegerField(validators=[API.validators.min_value_validator])),
                ('discount_value', models.FloatField(blank=True, default=0, null=True)),
            ],
        ),
    ]
