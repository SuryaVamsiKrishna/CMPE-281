from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

class CustomLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid username or password")
            self.user_cache = user
        return self.cleaned_data

    def get_user(self):
        return getattr(self, 'user_cache', None)
