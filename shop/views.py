from django.shortcuts import render
from .models import Category, Product, Article, Subcategory
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator

def index(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    context = {'articles': articles,
               'categories': categories}
    return render(request, 'index.html', context)

def subcategory_list(request,slug):
    subcategories = Subcategory.objects.filter(category__slug=slug)
    context = {'subcategories': subcategories,
    }
    return render(request, 'subcategory_list.html', context)

def product_list(request, slug):
    product_list = Product.objects.filter(subcategory__slug=slug)
    category = Subcategory.objects.get(slug=slug)
    paginator = Paginator(product_list, 20)
    current_page = request.GET.get('page', 1)
    products = paginator.get_page(current_page)
    prev_page, next_page = None, None
    if products.has_previous():
        prev_page = products.previous_page_number
    if products.has_next():
        next_page = products.next_page_number

    context = {'category': category,
               'product_list': products,
               'current_page': products.number,
               'prev_page_url': prev_page,
               'next_page_url': next_page,
               }

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

