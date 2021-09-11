"""файл с классом GroupAdminForm"""
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group

User = get_user_model()

class GroupAdminForm(forms.ModelForm):
    """класс формы для отображения/сохранения данных в модели Group"""
    class Meta:
        model = Group
        fields = ("name",)

    users = forms.ModelMultipleChoiceField(
         queryset=User.objects.all(),
         required=False,
         widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):

        super(GroupAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        """метод протягивающий связи от юзера к группам"""
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, commit=True):
        instance = super(GroupAdminForm, self).save()
        self.save_m2m()
        return instance
