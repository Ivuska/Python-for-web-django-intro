# Generated by Django 3.2.9 on 2021-11-07 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_branch_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.branch'),
        ),
    ]
