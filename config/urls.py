"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from product.views import *
from clients.views import *
from sell.views import *
from partner.views import *
from returned. views import ReturnedViewSet

router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')
router.register("new-product", NewProductViewSet, basename="newproduct")
router.register("client", ClientViewSet, basename="client")
router.register('sell', SellViewSet, basename="sell")
router.register("sellitem", SellItemViewSet, basename="sellitem")
router.register("partner", PartnerViewSet, basename="partner")
router.register("harajat", HarajatViewSet, basename="harajat")
router.register("returned", ReturnedViewSet, basename="returned")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
