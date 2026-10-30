from re import search

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Fooditem
# Create your views here.
#registration
def registeration(request):
   return render(request,'signup.html')

def register_post(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    #to  check there is username exists
    if(User.objects.filter(username=username).exists()):
        return render(request,'signup.html',{'error':'Username already exists'})
#create user
    user = User()
    user.username = username
    user.password = make_password(password)
    user.save()
    return redirect('login')
#login
def user_login(request):
    return render(request,'login.html')

def login_post(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user =authenticate(username =username,password =password)
    print("AUTHENTICATED USER:", user)

    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return render(request,'login.html',{'error':'Login Unsuccessful. Please check username and password'})
# home page
@login_required
def home (request):
    return render(request,'home.html')
#add food
@login_required
def add_food(request):
    return render(request,'add_food.html')
#store food
@login_required
def add_food_post(request):
    food_name = request.POST.get('food_name')
    category = request.POST.get('category')
    description = request.POST.get('description')
    price = request.POST.get('price')
    quantity = request.POST.get('quantity')

    food = Fooditem()
    food.food_name = food_name
    food.category = category
    food.description = description
    food.price = price
    food.quantity = quantity
    food.save()
    return redirect('food_list')
#display food list
@login_required
def food_list(request):
    search = request.GET.get('search')
    if search:
        foods = Fooditem.objects.filter(food_name__icontains=search)
    else:
        foods = Fooditem.objects.all()
    return render(request,'food_list.html',{'foods':foods})
#edit/update  food
@login_required
def edit_food(request,id):
    food = Fooditem.objects.get(id=id)
    return render(request,'edit_food.html',{'food':food})
#store updated list
@login_required
def edit_food_post(request,id):
    food = Fooditem.objects.get(id=id)
    food.food_name = request.POST.get('food_name')
    food.category = request.POST.get('category')
    food.description = request.POST.get('description')
    food.price = request.POST.get('price')
    food.quantity = request.POST.get('quantity')

    food.save()

    return redirect('food_list')
#delete food
@login_required
def delete_food(request,id):
    food = Fooditem.objects.get(id=id)
    food.delete()
    return redirect('food_list')
@login_required
def delete_food_post(request,id):
    food = Fooditem.objects.get(id=id)
    food.food_name = request.POST.get('food_name')
    food.category = request.POST.get('category')
    food.description = request.POST.get('description')
    food.price = request.POST.get('price')
    food.quantity = request.POST.get('quantity')

    food.save()
    return redirect('food_list')
#logout user
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
#delete user
@login_required
def delete_user(request):
    user = request.user
    user.delete()
    return redirect('registeration')
