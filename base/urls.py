from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('fastfood',views.fastfood,name='fastfood'),
    path('food',views.food,name='food'),
    path('vegetarian',views.vegetarian,name='vegetarian'),
    path('nonvegetarian',views.nonvegetarian,name='nonvegetarian'),
    path('juice',views.juice,name='juice'),
    path('beverages',views.beverages,name='beverages'),
    path('naturaljuice',views.naturaljuice,name='naturaljuice'),
    path('dessert',views.dessert,name='dessert'),
    path('cake',views.cake,name='cake'),
    path('icecream',views.icecream,name='icecream'),
    path('signin',views.signin,name='signin'),
    path('login',views.login,name='login'),
    path('success',views.success,name='success'),
   
]