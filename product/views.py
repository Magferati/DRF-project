from django.shortcuts import get_object_or_404 #render
#from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .models import Product, Category
@api_view()
def view_specific_product(request, id):
    # try:
       # product = Product.objects.get(pk=id)
        product = get_object_or_404(Product, pk=id)
        product_dict = {'id':product.id, 'name':product.name, 'price':product.price}
        return Response(product_dict)
    # except Product.DoesNotExist:
    #     return Response({"message":'Product does not existed.'}, status=status.HTTP_404_NOT_FOUND)

@api_view()
def view_categoryes(request):
    return Response({'message':'category'})