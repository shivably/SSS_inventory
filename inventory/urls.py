from django.urls import path
from inventory import views

urlpatterns = [
    path("", views.product, name="product_list"),
    path("<int:product_id>/", views.detail, name="product_detail"),
    path("add", views.add, name="product_add"),
]