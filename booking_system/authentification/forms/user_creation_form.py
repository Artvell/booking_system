"""файл с классом UserCreationForm, переопределенной формой для создания юзеров"""
from random import choice
from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from authentification.models import User
from authentification.functions import Encoder,SendMail
from string import ascii_uppercase,ascii_lowercase , digits

class UserCreationForm(forms.ModelForm):
    """Форма для создания новых юзеров. Сордержит поля стандартной формы и поле Роль"""
    choices = [
        ("manager","manager"),
        ("admin","admin")
    ]
    role = forms.ChoiceField(label="Роль", choices=choices)
    password = forms.CharField(label="Пароль", max_length=20)
    available_roles = ["manager","admin"]
    def clean_role(self):
        """"Валидирует данные из поля Роль"""
        data = self.cleaned_data['role']
        if data not in self.available_roles:
            raise ValidationError("Доступные роли: {}".format(",".join(self.available_roles)))
        return data

    class Meta:
        model = User
        fields = ('email', 'role',"password")

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


