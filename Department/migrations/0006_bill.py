# Generated by Django 4.1.3 on 2023-06-21 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Department', '0005_demandrate_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('bid', models.IntegerField(db_column='BID', primary_key=True, serialize=False)),
                ('bdate', models.DateField(blank=True, db_column='BDate', null=True)),
                ('byear', models.IntegerField(blank=True, db_column='BYear', null=True)),
                ('bmonth', models.CharField(blank=True, db_column='BMonth', max_length=14, null=True)),
                ('current_reading', models.IntegerField(blank=True, db_column='Current_Reading', null=True)),
                ('prev_reading', models.IntegerField(blank=True, db_column='Prev_Reading', null=True)),
                ('bamount', models.FloatField(blank=True, db_column='Bamount', null=True)),
            ],
            options={
                'db_table': 'bill',
                'managed': False,
            },
        ),
    ]
