from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage),
    path('product/', views.renderhtml, name= 'produk'),
    path('product/add/', views.add, name= 'add'),
    path('product/add/addrecord/', views.addrecord, name= 'addproduk'),
    path('product/delete/<int:id>', views.delete, name='delete'),
    path('product/edit/<int:id>', views.edit, name='edit'),
    path('product/edit/edited/<int:id>', views.edited, name='edited'),

]