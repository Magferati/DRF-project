from django.urls import path
from .views import view_product , view_cetagoryes
urlpatterns = [
    path("", view_product, name='product_list'),
    path("cetagory/",view_cetagoryes, name='cetagory_lst')
]
