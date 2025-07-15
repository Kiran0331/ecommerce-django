from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .models import Order, OrderItem
# Create your views here.
def homepage(request):
    products=Product.objects.all()
    return render(request, 'main/home.html', {'products': products })

def cart_view(request):
    cart=request.session.get('cart',{})
    products=[]
    total=0
    for product_id, quantity in cart.items():
        product=Product.objects.get(id=product_id)
        total+=product.price * quantity
        products.append({
            'product': product,
            'quantity': quantity,
            'total': product.price * quantity
        })
    return render(request, 'main/cart.html',{'products':products, 'total':total})

def add_to_cart(request, product_id):
    cart=request.session.get('cart',{})
    cart[str(product_id)]=cart.get(str(product_id),0) +1
    request.session['cart']=cart
    return redirect('cart')

def remove_from_cart(request, product_id):
    cart=request.session.get('cart',{})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('cart')

def increase_quantity(request, product_id):
    cart=request.session.get('cart',{})
    if str(product_id) in cart:
        cart[str(product_id)]+=1
    request.session['cart']=cart
    return redirect('cart')

def decrease_quantity(request,product_id):
    cart=request.session.get('cart',{})
    if str(product_id) in cart:
        if cart[str(product_id)]>1:
            cart[str(product_id)]-=1
        else:
            del cart[str(product_id)]
    request.session['cart']=cart
    return redirect('cart')

def checkout_view(request):
    cart= request.session.get('cart',{})
    products=[]
    total=0

    for product_id, quantity in cart.items():
        product=Product.objects.get(id=product_id)
        line_total=product.price * quantity
        total+=line_total
        products.append({'product':product, 'quantity': quantity, 'line_total':line_total}) 
    
    if request.method == 'POST':
        name= request.POST['name']
        address=request.POST['address']
        phone=request.POST['phone']

        order=Order.objects.create(name=name, address=address, phone=phone)

        for item in products:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity']
            )
        request.session['cart']={}
        return render(request, 'main/thankyou.html',{'order':order, 'order_items':order.orderitem_set.all(), 'total':total})
    return render(request,'main/checkout.html',{'product':product, 'total':total})


    




