from django.shortcuts import render
from .models import Category, Product, Article
from cart.forms import CartAddProductForm

def index(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    context = {'articles':articles,
               'categories':categories}
    return render(request, 'index.html', context)

def product_list(request, slug):
    product_list = Product.objects.filter(category__slug=slug)
    category = Category.objects.get(slug=slug)
    context = {'product_list': product_list,
               'category': category}
    return render(request, 'product_list.html', context)

def article(request, slug):
    article = Article.objects.get(slug=slug)
    product_list = article.products.all()
    context = {'article': article,
               'product_list': product_list}
    return render(request, 'article.html', context)

def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    cart_product_form = CartAddProductForm()
    context = {'product':product,
               'cart_product_form': cart_product_form}
    return render(request, 'product_detail.html', context)
