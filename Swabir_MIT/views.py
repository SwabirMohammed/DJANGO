from django.shortcuts import render
from .forms import UserReg


def reg(request):
    submit_button = request.POST.get("Reg")
    name = ''
    email = ''
    password = ''


