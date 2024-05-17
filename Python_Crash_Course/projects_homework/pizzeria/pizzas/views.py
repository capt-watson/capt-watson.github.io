from django.shortcuts import render
from .models import Pizza

# Create your views here.

def index(request):
    """Pizzeria Home Page"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Show all toppings"""
    pizzas = Pizza.objects.all()   ## Django queries database for Topic objects sorted by date_added.
    context = {'pizzas': pizzas}                    ## This context (in dict format) is sent to the template.
    return render(request, 'pizzas/pizzas.html', context)  ## While building a page, render() is called with request obj + template + context dict

def pizza(request, pizza_id):
    """Show a single topping and all its entries"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {'pizza':pizza, 'toppings':toppings}
    return render(request, 'pizzas/pizza.html', context)
