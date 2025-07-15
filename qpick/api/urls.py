from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HeadphoneView, CoverView

router = DefaultRouter()
router.register(r'headphone', HeadphoneView)
router.register(r'cover', CoverView)

urlpatterns = router.urls
