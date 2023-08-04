from django.shortcuts import render, get_object_or_404
from .models import Product, Categorys
from django.views import generic
from card.forms import CartAddProductForm


# Create your views here.

def homeviews(request):
    products = Product.objects.all()
    categories = Categorys.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'product/home_page.html', context)

def product_detail(request, id):
    product = Product.objects.get(id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'product/abautviev.html', {'product': product, 'cart_product_form': cart_product_form})

class HomePage(generic.ListView):
    model = Product
    template_name = 'product/home_page.html'
    context_object_name = 'product'

class AbautView(generic.DetailView):
    model = Product
    template_name = 'product/abautviev.html'
    context_object_name = 'product'




def Category(request, category_slug):
    categories = Categorys.objects.all()
    category = Categorys.objects.get(slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'product/category.html', {
        'category': category,
        'categorys': categories,
        'products': products
    })



