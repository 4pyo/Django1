from django.urls import path
from .import views

app_name = 'market'
urlpatterns = [
    path ('' , views.product_list) , 
    path('<int:id>' , views.product_detail , name = 'product_detail') , 
]
