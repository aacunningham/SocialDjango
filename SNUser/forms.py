from django.forms import (
    ModelForm, PasswordInput)
from SNUser.models import SNUser

class SNUserForm(ModelForm):
    class Meta:
        model = SNUser
        fields = ('email', 'password', 'first_name', 'last_name')
        widgets = {'password': PasswordInput()}
