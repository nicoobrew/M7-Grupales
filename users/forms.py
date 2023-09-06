from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from users.models import CustomUser


class SuperRegisterForm(UserCreationForm): 
    rol  = (
        ('staff', 'staff'),
        ('vendedor', 'vendedor'),
        ('logistica', 'logistica')
    )
    email = forms.EmailField()
    type_user = forms.ChoiceField(choices=rol)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'type_user']

class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(label='Full Name', max_length=150)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'rut', 'email']