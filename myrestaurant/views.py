from django.shortcuts import render, redirect
from .models import Dish

def index(request):
    context = {
        'data': {
            'appetizers': Dish.objects.filter(category='Appetizers'),
            'main_courses': Dish.objects.filter(category='Main Courses'),
            'desserts': Dish.objects.filter(category='Desserts'),
        }
    }
    return render(request, 'index.html', context)

def add_dish(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        category = request.POST['category']
        Dish.objects.create(name=name, description=description, price=price, category=category)
        return redirect('add_dish')
    
    context = {
        'dishes': Dish.objects.all()
    }
    return render(request, 'add_dish.html', context)
