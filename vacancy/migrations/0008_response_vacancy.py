# Generated by Django 4.1.7 on 2023-08-20 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0007_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='vacancy',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='vacancy.vacancy'),
        ),
    ]
