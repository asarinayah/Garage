from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),

    path('vehicles/', views.vehicle_list, name="vehicle_list"),
    path('vehicles/add/', views.vehicle_add, name="vehicle_add"),
    path('vehicles/<int:pk>/', views.vehicle_detail, name="vehicle_detail"),

    path('jobs/add/', views.job_add, name="job_add"),

    path('invoices/', views.invoice_list, name="invoice_list"),
    path('invoices/add/', views.invoice_add, name="invoice_add"),
    path('invoices/<int:pk>/', views.invoice_detail, name="invoice_detail"),

    path('day-end/', views.day_end, name="day_end"),
]
