from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *

class AddEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['title', 'description', 'type', 'city','date_start', 'date_end', 'logo']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 50, 'rows': 10}),
            'date_start': forms.SelectDateWidget(),
            'date_end': forms.SelectDateWidget()
        }

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return description


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    email = forms.EmailField(label='Email', widget=forms.EmailInput())
    first_name = forms.CharField(label='Имя', widget=forms.TextInput())
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput())
    age = forms.CharField(label='Возраст', widget=forms.TextInput())
    city = forms.CharField(label='Город', widget=forms.TextInput())
    sex = forms.ChoiceField(label='Пол', widget=forms.Select(), choices=[('Мужчина', 'Мужчина'),
                                                                      ('Женщина', 'Женщина'),
                                                                      ('Другое', 'Другое')])
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'age', 'city', 'sex', 'password1', 'password2')



class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())

