from django.urls import path
from .views import view_categoryes
urlpatterns = [
    path("", view_categoryes, name='category_list')
]
