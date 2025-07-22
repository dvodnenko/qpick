from django.urls import path

from .views import HeadphoneView, CoverView, AddToCartView, CartView


urlpatterns = [
    path('headphones', HeadphoneView.as_view()),
    path('covers', CoverView.as_view()),

    path('cart', CartView.as_view()),
    path('cart/add/', AddToCartView.as_view()),
]
