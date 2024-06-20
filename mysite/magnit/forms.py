from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from magnit.models import Product, Purchase


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'

    def save(self, commit=True):
        # Call the original save() method with commit=False
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
