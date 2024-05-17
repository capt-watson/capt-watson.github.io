from django.urls import path


from . import views

app_name = 'pizzas'

urlpatterns = [
    ## Home Page
    path('', views.index, name='index'),
    ## Page that shows all pizzas
    path('pizzas/', views.pizzas, name='pizzas'),
    ## page that shows a single pizza
    path('pizza/<int:pizza_id>/', views.pizza, name='pizza'),
]
