from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm,OrderForm


def home(request):

    categories = [
        {
            'name': 'Mobile',
            'icon': '📱'
        },
        {
            'name': 'Laptop',
            'icon': '💻'
        },
        {
            'name': 'Electronics',
            'icon': '🔌'
        },
        {
            'name': 'Fashion',
            'icon': '👕'
        },
        {
            'name': 'Shoes',
            'icon': '👟'
        },
        {
            'name': 'Books',
            'icon': '📚'
        },
        {
            'name': 'Watches',
            'icon': '⌚'
        },
    ]

    products = Product.objects.all()

    return render(
        request,
        'products/home.html',
        {
            'categories': categories,
            'products': products
        }
    )

def product_list(request):

    products = Product.objects.all()

    return render(
        request,
        'products/product_list.html',
        {'products': products}
    )
def product_detail(request, id):

    product = get_object_or_404(Product, id=id)

    return render(
        request,
        'products/product_detail.html',
        {'product': product}
    )
def category_products(request, category):

    products = Product.objects.filter(category=category)  

    return render(
        request,
        'products/product_list.html',
        {'products': products}
    )
def add_to_cart(request, id):

    product = get_object_or_404(Product, id=id)

    cart = request.session.get('cart', {})

    product_id = str(product.id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart

    return redirect('home')
def cart(request):

    cart = request.session.get('cart', {})

    products = []

    total = 0

    for product_id, quantity in cart.items():

        product = get_object_or_404(
            Product,
            id=product_id
        )

        item_total = product.price * quantity

        total += item_total

        products.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total
        })

    return render(
        request,
        'products/cart.html',
        {
            'products': products,
            'total': total
        }
    )
def place_order(request, id):

    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':

        form = OrderForm(request.POST)

        if form.is_valid():

            order = form.save(commit=False)

            order.product = product

            order.total_price = product.price * order.quantity

            order.save()

            return render(
                request,
                'products/order_success.html',
                {'order': order}
            )

    else:

        form = OrderForm()

    return render(
        request,
        'products/place_order.html',
        {
            'form': form,
            'product': product
        }
    )
def remove_from_cart(request, id):

    cart = request.session.get('cart', {})

    product_id = str(id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')

