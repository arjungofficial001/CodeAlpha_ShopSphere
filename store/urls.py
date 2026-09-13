from django.urls import path

from . import views


urlpatterns = [
    path(
        "",
        views.home,
        name="home",
    ),

    path(
        "product/<int:product_id>/",
        views.product_detail,
        name="product_detail",
    ),

    path(
        "cart/add/<int:product_id>/",
        views.add_to_cart,
        name="add_to_cart",
    ),

    path(
        "cart/",
        views.cart,
        name="cart",
    ),

    path(
        "cart/increase/<int:product_id>/",
        views.increase_cart,
        name="increase_cart",
    ),

    path(
        "cart/decrease/<int:product_id>/",
        views.decrease_cart,
        name="decrease_cart",
    ),

    path(
        "cart/remove/<int:product_id>/",
        views.remove_from_cart,
        name="remove_from_cart",
    ),

    # Authentication
    path(
        "register/",
        views.register,
        name="register",
    ),

    path(
        "login/",
        views.login_view,
        name="login",
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout",
    ),

    # Checkout
    path(
        "checkout/",
        views.checkout,
        name="checkout",
    ),

    path(
        "order-success/<int:order_id>/",
        views.order_success,
        name="order_success",
    ),

    # Customer Orders
    path(
        "my-orders/",
        views.my_orders,
        name="my_orders",
    ),
]