from django.forms import (
    CharField, ModelForm, PasswordInput, ValidationError)
from SNUser.models import SNUser

class SNUserForm(ModelForm):
    confirm_password = CharField(label='Confirm Password', widget=PasswordInput(), required=True)

    class Meta:
        model = SNUser
        fields = ('first_name', 'last_name', 'email', 'password')
        widgets = {'password': PasswordInput()}

    def clean(self):
        cleaned_data = super(SNUserForm, self).clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('confirm_password')
        if password1 and password2 != password1:
            error = ValidationError("Passwords don't match!")
            self.add_error('confirm_password', '')
            self.add_error('password', '')
            raise error
