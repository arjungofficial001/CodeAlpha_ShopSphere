from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from .models import Product, Order, OrderItem


def home(request):
    products = Product.objects.all().order_by("-created_at")

    query = request.GET.get("q", "").strip()

    if query:
        products = products.filter(
            name__icontains=query
        ) | products.filter(
            category__icontains=query
        )

    return render(
        request,
        "home.html",
        {
            "products": products,
            "query": query,
        },
    )


def product_detail(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id
    )

    return render(
        request,
        "product_detail.html",
        {
            "product": product,
        },
    )


def add_to_cart(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id
    )

    if product.stock <= 0:
        messages.error(
            request,
            "This product is out of stock."
        )

        return redirect("home")

    cart = request.session.get("cart", {})

    product_id = str(product_id)

    if product_id in cart:

        if cart[product_id] < product.stock:

            cart[product_id] += 1

            messages.success(
                request,
                f"{product.name} quantity increased."
            )

        else:

            messages.warning(
                request,
                f"Only {product.stock} units of "
                f"{product.name} are available."
            )

    else:

        cart[product_id] = 1

        messages.success(
            request,
            f"{product.name} added to cart."
        )

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("home")


def cart(request):
    cart_data = request.session.get("cart", {})

    cart_items = []
    total = 0

    for product_id, quantity in cart_data.items():

        product = get_object_or_404(
            Product,
            id=product_id
        )

        if quantity > product.stock:
            quantity = product.stock
            cart_data[product_id] = quantity

        item_total = product.price * quantity

        total += item_total

        cart_items.append(
            {
                "product": product,
                "quantity": quantity,
                "item_total": item_total,
            }
        )

    request.session["cart"] = cart_data
    request.session.modified = True

    return render(
        request,
        "cart.html",
        {
            "cart_items": cart_items,
            "total": total,
        },
    )


def increase_cart(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id
    )

    cart = request.session.get("cart", {})
    product_id = str(product_id)

    if product_id in cart:

        if cart[product_id] < product.stock:

            cart[product_id] += 1

            messages.success(
                request,
                f"{product.name} quantity increased."
            )

        else:

            messages.warning(
                request,
                f"Only {product.stock} units of "
                f"{product.name} are available."
            )

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


def decrease_cart(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id
    )

    cart = request.session.get("cart", {})
    product_id = str(product_id)

    if product_id in cart:

        if cart[product_id] > 1:

            cart[product_id] -= 1

            messages.success(
                request,
                f"{product.name} quantity decreased."
            )

        else:

            del cart[product_id]

            messages.success(
                request,
                f"{product.name} removed from cart."
            )

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


def remove_from_cart(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id
    )

    cart = request.session.get("cart", {})
    product_id = str(product_id)

    if product_id in cart:

        del cart[product_id]

        messages.success(
            request,
            f"{product.name} removed from cart."
        )

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


# =========================
# USER AUTHENTICATION
# =========================

def register(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(
                request,
                "Registration successful. Welcome to ShopSphere!"
            )

            return redirect("home")

    else:

        form = UserCreationForm()

    return render(
        request,
        "register.html",
        {
            "form": form,
        },
    )


def login_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:

            login(request, user)

            messages.success(
                request,
                f"Welcome back, {user.username}!"
            )

            return redirect("home")

        else:

            messages.error(
                request,
                "Invalid username or password."
            )

    return render(
        request,
        "login.html",
    )


def logout_view(request):

    logout(request)

    messages.success(
        request,
        "You have been logged out successfully."
    )

    return redirect("home")


# =========================
# CHECKOUT
# =========================

@login_required(login_url="login")
def checkout(request):

    cart_data = request.session.get("cart", {})

    if not cart_data:

        messages.warning(
            request,
            "Your cart is empty."
        )

        return redirect("cart")

    cart_items = []
    total = 0

    for product_id, quantity in cart_data.items():

        product = get_object_or_404(
            Product,
            id=product_id
        )

        if quantity > product.stock:

            messages.error(
                request,
                f"Not enough stock available for "
                f"{product.name}."
            )

            return redirect("cart")

        item_total = product.price * quantity

        total += item_total

        cart_items.append(
            {
                "product": product,
                "quantity": quantity,
                "item_total": item_total,
            }
        )

    if request.method == "POST":

        shipping_address = request.POST.get(
            "shipping_address",
            ""
        ).strip()

        if not shipping_address:

            messages.error(
                request,
                "Please enter your shipping address."
            )

            return render(
                request,
                "checkout.html",
                {
                    "cart_items": cart_items,
                    "total": total,
                },
            )

        try:

            with transaction.atomic():

                for product_id, quantity in cart_data.items():

                    product = Product.objects.select_for_update().get(
                        id=product_id
                    )

                    if product.stock < quantity:

                        raise ValueError(
                            f"Not enough stock for {product.name}."
                        )

                order = Order.objects.create(
                    user=request.user,
                    total_amount=total,
                    shipping_address=shipping_address,
                    status="Pending",
                )

                for product_id, quantity in cart_data.items():

                    product = Product.objects.select_for_update().get(
                        id=product_id
                    )

                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        quantity=quantity,
                        price=product.price,
                    )

                    product.stock -= quantity
                    product.save()

        except ValueError as error:

            messages.error(
                request,
                str(error)
            )

            return redirect("cart")

        request.session["cart"] = {}
        request.session.modified = True

        messages.success(
            request,
            f"Order #{order.id} placed successfully!"
        )

        return redirect(
            "order_success",
            order_id=order.id
        )

    return render(
        request,
        "checkout.html",
        {
            "cart_items": cart_items,
            "total": total,
        },
    )


@login_required(login_url="login")
def order_success(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    return render(
        request,
        "order_success.html",
        {
            "order": order,
        },
    )


# =========================
# MY ORDERS
# =========================

@login_required(login_url="login")
def my_orders(request):

    orders = (
        Order.objects
        .filter(user=request.user)
        .prefetch_related("items__product")
        .order_by("-created_at")
    )

    return render(
        request,
        "my_orders.html",
        {
            "orders": orders,
        },
    )