from django import forms
from .models import Vacancy, Response


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = '__all__'
        exclude = ['views', 'application_filed', 'author']


class ResponseForm(forms.ModelForm):
    response_text = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        max_length=200,
        min_length=50
    )

    class Meta:
        model = Response
        fields = '__all__'
        exclude = ['response_user', 'vacancy']