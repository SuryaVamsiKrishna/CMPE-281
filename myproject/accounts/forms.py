from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import AVDriver, AVStaff

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

User = get_user_model()

class UserForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'user_type', 'password1', 'password2']

class AVDriverForm(forms.ModelForm):
    class Meta:
        model = AVDriver
        fields = ['license_number', 'vehicle_color', 'model_number', 'sensor_info']

    def __init__(self, *args, **kwargs):
        super(AVDriverForm, self).__init__(*args, **kwargs)
        self.fields['user'] = UserForm()

class AVStaffForm(forms.ModelForm):
    class Meta:
        model = AVStaff
        fields = []

    def __init__(self, *args, **kwargs):
        super(AVStaffForm, self).__init__(*args, **kwargs)
        self.fields['user'] = UserForm()
