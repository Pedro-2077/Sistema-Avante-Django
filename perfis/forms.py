from .models import Users
from django.contrib.auth import forms
from django.utils.translation import gettext, gettext_lazy as _



class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Users


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Users


class UserFormTemplate(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Users
        exclude = ['user_permissions', 'groups', 'password', 'is_superuser', 'is_staff','last_login', 'date_joined']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': field})

        self.fields['grupo_de_acesso'].widget.attrs.update({'name': 'valor'})
        self.fields['grupo_de_acesso'].widget.attrs.update({'id': 'userPerfil'})
        self.fields['username'].widget.attrs.update({'id': 'nome'})
        self.fields['tipoUsuario'].widget.attrs.update({'id':'userType'})
        self.fields['funcao'].widget.attrs.update({'id':'funcao'})
        self.fields['funcao'].widget.attrs.update({'id':'email'})


class PasswordChangeFormTemplate(forms.PasswordChangeForm):
    class Meta(forms.PasswordChangeForm):
        model = Users
        exclude = ['old_password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        # Remove the old_password field dynamically
        del self.fields['old_password']

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        for field_name in ['new_password1', 'new_password2']:
            self.fields[field_name].help_text = ''

        fields = ['new_password1', 'new_password2']
