from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path("", views.IndexPageView.as_view(), name="index"),
    path("shop/", views.ProductsView.as_view(), name="shop"),
    path("about-us/", views.AboutUs.as_view(), name="about_us"),
    path("contact-us/", views.ContactUs.as_view(), name="contact_us"),
    path("product/<str:slug>", views.ProductDetailPage.as_view(), name="detail"),
    path("category/<str:slug>", views.CategoryDetailPage.as_view(), name="category"),
    path("change_lang/", views.change_lang, name="change_lang"),
    path("order/", views.order, name="order"),
    
    #auth
    path("login-register/", views.loginRegister, name="auth"),
    path("login/", views.loginview, name="login"),
    path("logout/", views.logoutview, name="logout"),
    path("register/", views.registerview, name="register"),
]
