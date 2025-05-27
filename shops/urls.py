from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_list, name='shop_list'),
    path('shop/<int:shop_id>/', views.rent_status, name='rent_status'),
    path('export-rent-pdf/<int:shop_id>/', views.export_rent_pdf, name='export_rent_pdf'),
     path('export-rent-excel/<int:shop_id>/', views.export_rent_excel, name='export_rent_excel'),
]
