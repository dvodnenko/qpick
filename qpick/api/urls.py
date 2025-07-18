from django.urls import path

from .views import HeadphoneView, CoverView


urlpatterns = [
    path('headphones', HeadphoneView.as_view()),
    path('covers', CoverView.as_view()),
]
