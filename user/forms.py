from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
class RegisterUserForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = (
            'phone_number',
            'first_name'
        )

