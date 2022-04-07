from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path("", views.IndexPageView.as_view(), name="index"),
    path("product/<str:slug>", views.ProductDetailPage.as_view(), name="detail"),
    path("category/<str:slug>", views.CategoryDetailPage.as_view(), name="category"),
    path("change_lang/", views.change_lang, name="change_lang"),
]
