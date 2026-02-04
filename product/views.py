from django.shortcuts import render
#from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view()
def view_product(request):
    return Response({'message':"okay"})

@api_view()
def view_cetagoryes(request):
    return Response({'message':'cetagory'})