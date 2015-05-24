from django.core.exceptions import ValidationError
import bleach
from django import forms
from SNUser.models import SNUser


class SNUserForm(forms.ModelForm):
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(), required=True)

    class Meta:
        model = SNUser
        fields = ('first_name', 'last_name', 'email', 'profile_image', 'password', 'confirm_password', 'bio')
        widgets = {'password': forms.PasswordInput(),
                   'bio': forms.Textarea(attrs={'rows': 4})}

    def clean(self):
        cleaned_data = super(SNUserForm, self).clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('confirm_password')
        if password1 and password2 != password1:
            error = ValidationError("Passwords don't match!")
            self.add_error('confirm_password', '')
            self.add_error('password', '')
            raise error

    def clean_bio(self):
        return bleach.clean(self.cleaned_data.get('bio'), strip=True)


class ChangeBioForm(forms.ModelForm):
    class Meta:
        model = SNUser
        fields = ('bio',)
        widgets = {'bio': forms.Textarea(attrs={'rows': 8}), }

    def clean_bio(self):
        return bleach.clean(self.cleaned_data.get('bio'), strip=True)


class ChangePasswordForm(forms.ModelForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(), required=True)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(), required=True)

    class Meta:
        model = SNUser
        fields = ('old_password', 'password', 'confirm_password')
        widgets = {'password': forms.PasswordInput()}

    def clean(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('confirm_password')
        if password1 and password2 != password1:
            error = ValidationError("Passwords don't match!")
            self.add_error('confirm_password', '')
            self.add_error('password', '')
            raise error