from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'base/index.html')

def signin(request):
    return render(request,'base/sign_in.html')

def login(request):
    return render(request,'base/login.html')

def success(request):
    return render(request,'base/success.html')

def fastfood(request):
    return render(request,'base/fast_food.html')

def food(request):
    return render(request,'base/food.html')

def vegetarian(request):
    return render(request,'base/vegetarian.html')

def nonvegetarian(request):
    return render(request,'base/non_vegetarian.html')

def juice(request):
    return render(request,'base/juice.html')

def beverages(request):
    return render(request,'base/beverages.html')

def naturaljuice(request):
    return render(request,'base/natural_juice.html')

def dessert(request):
    return render(request,'base/dessert.html')

def cake(request):
    return render(request,'base/cake.html')

def icecream(request):
    return render(request,'base/ice_cream.html')
