from django.urls import path
from . import views

app_name = 'product'

urlpatterns=[
    path('', views.homeviews , name='home' ),
    path('<int:id>/', views.product_detail ,name='base'),
    path('<slug:category_slug>/', views.Category , name='category'),

]