from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label="Kullanıcı Adı Giriniz")
    password = forms.CharField(max_length=30, label="Parola Giriniz", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            pass



class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=30, label="Kullanıcı Adı Giriniz")
    password1 = forms.CharField(max_length=30, label="Parola Giriniz", widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=30, label="Parolayı Tekrar Giriniz", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Parolalar Eşleşmiyor!!")
        return password2
