"""файл с формой для изменения данных юзера"""
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from authentification.models import User
class UserChangeForm(forms.ModelForm):
    """Форма для изменения юзеров. Поле пароля заменено полем хэша
    """
    password = ReadOnlyPasswordHashField(label=("Password"),
        help_text=("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"../password/\">this form</a>."))

    class Meta:
        model = User
        fields = ('email', 'password', 'is_active')

    def clean_password(self):
        """Возвращает введенный пароль"""
        return self.initial["password"]
