from django import forms


class UserReg(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField()


class UserLogin(forms.Form):
    username = forms.CharField(max_length=100)
    user_pass = forms.CharField()


class MembersReg(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
