# Generated by Django 3.2.9 on 2021-11-07 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20211107_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
