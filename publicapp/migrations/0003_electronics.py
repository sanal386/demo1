# Generated by Django 3.1.7 on 2021-04-20 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicapp', '0002_vegetable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Electronics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('prize', models.FloatField()),
                ('image', models.CharField(max_length=2500)),
            ],
        ),
    ]
