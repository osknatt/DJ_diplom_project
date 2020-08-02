from django.shortcuts import render, redirect
from .models import Order, OrderItem
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        order = Order(user=request.user)
        order.save()

        for item in cart:
            OrderItem.objects.create(order=order,
                                    product=item['product'],
                                    price=item['price'],
                                    quantity=item['quantity'])
        # clear the cart
        cart.clear()
        return redirect(f"/order/{order.id}")
    else:
        return redirect('/')


def order_view(request, ids):
    items = OrderItem.objects.filter(order__id=ids)
    context = {
        'ids': ids,
        'items': items
    }
    return render(request, "order.html", context)

