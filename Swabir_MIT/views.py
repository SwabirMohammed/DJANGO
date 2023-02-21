from django.shortcuts import render
from .forms import UserReg


def reg(request):
    submit_button = request.POST.get("Reg")
    name = ''
    email = ''
    password = ''


    reg_form = UserReg(request.POST or None)
    if reg_form.is_valid():
        name = reg_form.cleaned_data.get("name")
        email = reg_form.cleaned_data.get("email")
        password = reg_form.cleaned_data.get("password")

