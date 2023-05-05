from django.shortcuts import render
from products.models import Product

# Create your views here.

def index(request):
    context = {
        "products" : Product.objects.all()
    }
    return render(request, 'products/index.html', context)


def about(request):
    return render(request, 'products/about.html')


def services(request):
    return render(request, 'products/service.html')


def room(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, 'products/room.html', context)


def booking(request):
    return render(request, 'products/booking.html')


def team(request):
    return render(request, 'products/team.html')


def testimonial(request):
    return render(request, 'products/testimonial.html')


def contact(request):
    return render(request, 'products/contact.html')
