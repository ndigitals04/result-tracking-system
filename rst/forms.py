from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput({'placeholder': 'Reg Number'}),
            'email': forms.EmailInput({'placeholder': 'Email'}),
            'first_name': forms.TextInput({'placeholder': 'First Name'}),
            'last_name': forms.TextInput({'placeholder': 'Lastname'}),
        }

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
