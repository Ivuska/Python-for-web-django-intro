# Generated by Django 3.2.9 on 2021-11-07 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('initial_date', models.DateField()),
                ('email', models.EmailField(max_length=80)),
                ('employees', models.IntegerField()),
            ],
        ),
    ]