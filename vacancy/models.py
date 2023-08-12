from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models


class Vacancy(models.Model):
    CATEGORY = (
        ('PHP', 'PHP Back-end developer'),
        ('Python QA', 'Python Automation QA'),
        ('Python BE', 'Python Back-end developer'),
        ('C/C++ Emb', 'C/C++ Embedded'),
        ('JS Front', 'JavaScript/Front-end'),
        ('JS Back', 'Node.js')
    )

    ENGLISH = (
        ('A0/A1', 'Beginner/Elementary'),
        ('A2', 'Pre Intermediate'),
        ('B1', 'Intermediate'),
        ('B2', 'Upper Intermediate'),
        ('C1', 'Advanced'),
        ('C2', 'Proficient')
    )
    title = models.CharField(max_length=70)
    main_text = models.TextField(max_length=1700)
    company_name = models.CharField(max_length=25)
    years_of_experience = models.IntegerField(
        validators=[MaxValueValidator(10)], help_text='Max 10 years of experience', blank=True
    )
    category = models.CharField(max_length=20, choices=CATEGORY)
    views = models.IntegerField(default=0)
    application_filed = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    english_level = models.CharField(max_length=20, choices=ENGLISH, blank=True)
    salary = models.IntegerField(validators=[MaxValueValidator(10000)], blank=True)
    geolocation = models.CharField(max_length=20, blank=True)
    company_site = models.URLField(blank=True)





