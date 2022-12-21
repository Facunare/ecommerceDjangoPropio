
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import  HttpResponseRedirect
from carrito.models import carrito

from ecommerce import models
import operator
from django.db.models import Sum





        
def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

    
