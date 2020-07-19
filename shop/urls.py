from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('c/<slug:slug>/', views.subcategory_list,
         name='subcategory'),
    path('s/<slug:slug>/', views.product_list,
         name='products'),
    path('p/<slug:slug>/', views.product_detail,
         name='product'),
    path('a/<slug:slug>/', views.article,
         name='article'),
]