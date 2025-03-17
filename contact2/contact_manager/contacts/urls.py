from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_contact, name='add_contact'),
    path('delete/<str:email>/', views.delete_contact, name='delete_contact'),
    path('send_email/<str:email>/', views.send_email, name='send_email'),
]
