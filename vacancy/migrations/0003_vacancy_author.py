# Generated by Django 4.1.7 on 2023-08-17 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancy', '0002_alter_vacancy_years_of_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to=settings.AUTH_USER_MODEL),
        ),
    ]