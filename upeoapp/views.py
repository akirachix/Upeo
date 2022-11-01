from django import forms
from django.shortcuts import render

from .models import models


# Create your views here.
# def register_student(request):
#     if request.method == "POST":
#         form = models.Student.CustomerRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = forms.CustomerRegistrationForm()     
#     return render(request,'wallet/register_customer.html',
#                   {"form":form})