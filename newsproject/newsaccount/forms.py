from django import forms


class BaseRegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)


class VerificationForm(forms.Form):
    code = forms.CharField(label='Код подтверждения', max_length=6)
