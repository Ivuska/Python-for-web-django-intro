# Generated by Django 3.2.9 on 2021-11-07 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.course'),
        ),
    ]
