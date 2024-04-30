from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm

from home.models import CustomUser


class RegistrationForm(UserCreationForm):
    ROLES = (
        ('Admin', 'Admin'),
        ('Speaker', 'Speaker'),
        ('Listener', 'Listener'),
    )
    role = forms.ChoiceField(choices=ROLES, widget=forms.Select(
        attrs={
            'class': 'form-control'
        }))
    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Логин',
            'id': 'hello',
            'help_text': '',
        }
    ))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Пароль',
            'id': 'hi',
            'help_text': '',
            'form_text': '',
            'label': 'Пароль',
            'title': ''
        }
    ))
    password1 = forms.CharField(label='', required=False, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            "label": "Password",
            'help_text': '',
        }
    ))
    password2 = forms.CharField(label='', required=False, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password confirm',
            "label": "Password confirm",
            'help_text': '',
        }
    ))

    class Meta(UserCreationForm.Meta):
        model = CustomUser


class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Temp',
            'id': 'hello'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Temp',
            'id': 'hi',
            'help_text': '',
        }
    ))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data
