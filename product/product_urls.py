from django.urls import path
from .views import view_specific_product 
urlpatterns = [
    path("<int:id>/", view_specific_product, name='product_list'),
]
