# Generated by Django 4.1.7 on 2023-08-15 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('recruiter', 'Recruiter'), ('worker', 'Worker')], default='None', max_length=10),
        ),
    ]
